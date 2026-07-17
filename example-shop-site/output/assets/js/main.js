// main.js - Website Builder Harness
// Shared interactive behaviour for all pages.
// No frameworks. No inline handlers. addEventListener only.

document.addEventListener('DOMContentLoaded', () => {
  function initMobileNav() {
    const toggle = document.querySelector('[data-nav-toggle]');
    const header = document.querySelector('.site-header');

    if (!toggle || !header) {
      return;
    }

    toggle.addEventListener('click', () => {
      const isOpen = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!isOpen));
      toggle.setAttribute('aria-label', isOpen ? 'Open navigation menu' : 'Close navigation menu');
      header.classList.toggle('is-open', !isOpen);
      document.body.classList.toggle('nav-open', !isOpen);
    });

    document.querySelectorAll('.nav-links a, .nav-cta').forEach((link) => {
      link.addEventListener('click', () => {
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Open navigation menu');
        header.classList.remove('is-open');
        document.body.classList.remove('nav-open');
      });
    });
  }

  function initActiveNav() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const normalizedPage = currentPage.replace('.html', '');

    document.querySelectorAll('[data-page]').forEach((link) => {
      if (link.dataset.page === normalizedPage || (normalizedPage === '' && link.dataset.page === 'index')) {
        link.classList.add('active');
        link.setAttribute('aria-current', 'page');
      }
    });
  }

  function initFooterYear() {
    document.querySelectorAll('[data-year]').forEach((element) => {
      element.textContent = String(new Date().getFullYear());
    });
  }

  function initFaqAccordion() {
    document.querySelectorAll('[data-faq-button]').forEach((button) => {
      button.addEventListener('click', () => {
        const isExpanded = button.getAttribute('aria-expanded') === 'true';
        const answer = button.nextElementSibling;

        button.setAttribute('aria-expanded', String(!isExpanded));
        if (answer) {
          answer.hidden = isExpanded;
        }
      });
    });
  }

  function initRevealSections() {
    const observedSections = document.querySelectorAll('[data-reveal]');

    if (!('IntersectionObserver' in window) || !observedSections.length) {
      observedSections.forEach((section) => {
        section.classList.add('is-visible');
      });
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.15,
      }
    );

    observedSections.forEach((section) => observer.observe(section));
  }

  initMobileNav();
  initActiveNav();
  initFooterYear();
  initFaqAccordion();
  initRevealSections();
});
