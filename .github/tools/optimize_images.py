from __future__ import annotations

import argparse
import io
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

try:
    from PIL import Image, ImageOps, features
except ImportError as exc:  # pragma: no cover - import guard
    raise SystemExit(
        "Pillow is required. Install with: pip install pillow pillow-avif-plugin"
    ) from exc

# Optional AVIF plugin. Importing is enough to register AVIF support in Pillow.
try:  # pragma: no cover - depends on environment
    import pillow_avif  # type: ignore  # noqa: F401
except Exception:
    pillow_avif = None


SUPPORTED_INPUT_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".avif"}


@dataclass
class OptimizationConfig:
    source_dir: Path
    output_dir: Path
    recursive: bool
    max_width: int
    max_height: int
    jpeg_quality: int
    webp_quality: int
    avif_quality: int
    formats: tuple[str, ...]
    overwrite: bool


@dataclass
class RunStats:
    processed: int = 0
    skipped: int = 0
    failed: int = 0


def parse_formats(raw: str) -> tuple[str, ...]:
    normalized = tuple(part.strip().lower() for part in raw.split(",") if part.strip())
    if not normalized:
        raise ValueError("At least one output format is required.")

    allowed = {"jpg", "webp", "avif"}
    invalid = [fmt for fmt in normalized if fmt not in allowed]
    if invalid:
        raise ValueError(f"Unsupported format(s): {', '.join(invalid)}")
    return normalized


def is_avif_writable() -> bool:
    # Some Pillow builds expose AVIF via plugin without a direct feature flag.
    if features.check("avif"):
        return True
    try:
        with io.BytesIO() as buf:
            Image.new("RGB", (1, 1), (0, 0, 0)).save(buf, format="AVIF")
        return True
    except Exception:
        return False


def iter_images(source_dir: Path, recursive: bool) -> Iterable[Path]:
    pattern = "**/*" if recursive else "*"
    for path in sorted(source_dir.glob(pattern)):
        if not path.is_file():
            continue
        if path.suffix.lower() in SUPPORTED_INPUT_EXTENSIONS:
            yield path


def get_resized_image(image: Image.Image, max_width: int, max_height: int) -> Image.Image:
    image = ImageOps.exif_transpose(image)
    if image.mode not in {"RGB", "L"}:
        image = image.convert("RGB")

    width, height = image.size
    if width <= max_width and height <= max_height:
        return image

    # Keep aspect ratio while capping dimensions.
    ratio = min(max_width / width, max_height / height)
    new_size = (max(1, int(width * ratio)), max(1, int(height * ratio)))
    return image.resize(new_size, Image.Resampling.LANCZOS)


def save_variant(image: Image.Image, out_path: Path, fmt: str, config: OptimizationConfig) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if fmt == "jpg":
        image.save(out_path, format="JPEG", quality=config.jpeg_quality, optimize=True)
        return

    if fmt == "webp":
        if not features.check("webp"):
            raise RuntimeError("WEBP support is not available in your Pillow build.")
        image.save(out_path, format="WEBP", quality=config.webp_quality, method=6)
        return

    if fmt == "avif":
        if not is_avif_writable():
            raise RuntimeError(
                "AVIF support is not available. Install/update pillow-avif-plugin."
            )
        image.save(out_path, format="AVIF", quality=config.avif_quality)
        return

    raise RuntimeError(f"Unknown format '{fmt}'.")


def optimize_one(image_path: Path, config: OptimizationConfig) -> str:
    relative = image_path.relative_to(config.source_dir)
    stem_output_dir = config.output_dir / relative.parent

    with Image.open(image_path) as src:
        optimized = get_resized_image(src, config.max_width, config.max_height)

        for fmt in config.formats:
            suffix = ".jpg" if fmt == "jpg" else f".{fmt}"
            out_path = stem_output_dir / f"{image_path.stem}{suffix}"

            if out_path.exists() and not config.overwrite:
                continue

            save_variant(optimized, out_path, fmt, config)

    return str(relative)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Resize and optimize images for web delivery. "
            "Supports JPG/PNG/WEBP/AVIF input and writes JPG/WEBP/AVIF variants."
        )
    )
    parser.add_argument(
        "--source-dir",
        required=True,
        type=Path,
        help="Folder containing original images.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output folder. Defaults to source-dir.",
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Process images recursively.",
    )
    parser.add_argument("--max-width", type=int, default=1920)
    parser.add_argument("--max-height", type=int, default=1920)
    parser.add_argument("--jpeg-quality", type=int, default=82)
    parser.add_argument("--webp-quality", type=int, default=80)
    parser.add_argument("--avif-quality", type=int, default=50)
    parser.add_argument(
        "--formats",
        default="jpg,webp,avif",
        help="Comma-separated output formats. Allowed: jpg,webp,avif",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite files if they already exist.",
    )
    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()

    source_dir: Path = args.source_dir.resolve()
    output_dir: Path = (args.output_dir or args.source_dir).resolve()

    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Source directory not found: {source_dir}", file=sys.stderr)
        return 2

    try:
        formats = parse_formats(args.formats)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    config = OptimizationConfig(
        source_dir=source_dir,
        output_dir=output_dir,
        recursive=args.recursive,
        max_width=args.max_width,
        max_height=args.max_height,
        jpeg_quality=args.jpeg_quality,
        webp_quality=args.webp_quality,
        avif_quality=args.avif_quality,
        formats=formats,
        overwrite=args.overwrite,
    )

    stats = RunStats()

    for image_path in iter_images(config.source_dir, config.recursive):
        try:
            rel = optimize_one(image_path, config)
            print(f"Optimized: {rel}")
            stats.processed += 1
        except Exception as exc:  # pragma: no cover - command line behavior
            print(f"Failed: {image_path} ({exc})", file=sys.stderr)
            stats.failed += 1

    if stats.processed == 0 and stats.failed == 0:
        print("No supported images found.")
        return 0

    print(
        f"Done. Processed: {stats.processed}, Failed: {stats.failed}, Output: {config.output_dir}"
    )
    return 1 if stats.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
