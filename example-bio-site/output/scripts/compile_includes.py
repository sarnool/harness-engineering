from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output"
PARTIALS_DIR = OUTPUT_DIR / "partials"

HEADER_MARKER = "<!-- include: partials/header.html -->"
FOOTER_MARKER = "<!-- include: partials/footer.html -->"


def main() -> None:
    header_path = PARTIALS_DIR / "header.html"
    footer_path = PARTIALS_DIR / "footer.html"

    if not header_path.exists() or not footer_path.exists():
        missing = []
        if not header_path.exists():
            missing.append(str(header_path))
        if not footer_path.exists():
            missing.append(str(footer_path))
        raise FileNotFoundError(f"Missing partial file(s): {', '.join(missing)}")

    header_html = header_path.read_text(encoding="utf-8").rstrip()
    footer_html = footer_path.read_text(encoding="utf-8").rstrip()

    updated = 0
    skipped = 0

    for page_path in sorted(OUTPUT_DIR.glob("*.html")):
        page_html = page_path.read_text(encoding="utf-8")

        if HEADER_MARKER not in page_html or FOOTER_MARKER not in page_html:
            skipped += 1
            continue

        page_html = page_html.replace(HEADER_MARKER, header_html)
        page_html = page_html.replace(FOOTER_MARKER, footer_html)
        page_path.write_text(page_html, encoding="utf-8")
        updated += 1

    print(f"Compiled includes for {updated} page(s). Skipped {skipped} page(s).")


if __name__ == "__main__":
    main()