## Build Decisions

- Entry knowledge file: `knowledge-files/01_BIO_SUMMARY.txt`
- Stage 1 source scope: all files in `knowledge-files/` except `assets/`
- Site type: multi-page portfolio
- Page set: Home, About, Projects, Research, Contact
- Primary site CTA: View Projects
- Visual direction: cool, precise, enterprise AI aesthetic with light backgrounds
- Header CTA target: `projects.html`
- Runtime images reference `knowledge-files/assets/images/` paths relatively from `output/` to preserve metadata fidelity
- Brand logo image is used once per page in the header to avoid duplicate-image validation failures
