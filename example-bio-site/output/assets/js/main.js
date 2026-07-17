// main.js — Website Builder Harness
// Shared interactive behaviour for all pages.
// No frameworks. No inline handlers. addEventListener only.

document.addEventListener('DOMContentLoaded', () => {
	// ── Mobile Nav Toggle ──
	function initMobileNav() {
		const toggle = document.querySelector('[data-nav-toggle]');
		const nav = document.querySelector('[data-nav]');

		if (!toggle || !nav) {
			return;
		}

		toggle.addEventListener('click', () => {
			const expanded = toggle.getAttribute('aria-expanded') === 'true';
			toggle.setAttribute('aria-expanded', String(!expanded));
			nav.classList.toggle('is-open', !expanded);
			document.body.classList.toggle('nav-open', !expanded);
		});
	}

	// ── Active Nav Link ──
	function initActiveNav() {
		const currentPage = window.location.pathname.split('/').pop() || 'index.html';
		const pageKey = currentPage.replace('.html', '');

		document.querySelectorAll('[data-page]').forEach((link) => {
			if (link.dataset.page === pageKey) {
				link.classList.add('active');
				link.setAttribute('aria-current', 'page');
			}
		});
	}

	// ── Footer Year ──
	function initFooterYear() {
		document.querySelectorAll('[data-year]').forEach((element) => {
			element.textContent = new Date().getFullYear();
		});
	}

	// ── Scroll Animations ──
	function initRevealSections() {
		const revealItems = document.querySelectorAll('[data-reveal]');

		if (!revealItems.length || !('IntersectionObserver' in window)) {
			revealItems.forEach((item) => item.classList.add('is-visible'));
			return;
		}

		const observer = new IntersectionObserver((entries) => {
			entries.forEach((entry) => {
				if (entry.isIntersecting) {
					entry.target.classList.add('is-visible');
					observer.unobserve(entry.target);
				}
			});
		}, {
			threshold: 0.2,
		});

		revealItems.forEach((item) => observer.observe(item));
	}

	initMobileNav();
	initActiveNav();
	initFooterYear();
	initRevealSections();
});
