Website Builder Harness Decision Log
====================================

Content Brief
-------------
ENTITY TYPE: Local business / service provider
AUDIENCE: Local clients who want a trusted beauty salon for hair, skin, brows, lashes, nails, and gifting. They need pricing, booking options, location, and confidence in the team.
TONE: Casual | Warm | Simple
PRIORITY MESSAGE: Bella's Beauty Salon is a welcoming Surry Hills salon where clients can book hair, skin, brow, lash, nail, and pamper services with confidence.
PRIMARY CTA: Book Now
SECONDARY CTA: View Services

CONTENT INVENTORY:
- About: Salon story, experience, welcoming positioning
- Contact Details: Phone, email, website, Instagram
- Location and Hours: Address, opening hours, holiday note
- Getting Here: Parking, train, and bus details
- Bookings: Online, phone, walk-ins, cancellation policy
- Services and Prices: Hair, skin, brows, lashes, waxing, nails
- Packages and Deals: The Works, Bride-to-Be, monthly membership
- Products: Kerastase, Dermalogica, OPI, retail advice
- Gift Vouchers: In-store and online purchase
- Team: Owner and four specialists
- FAQs: Consultation, timing, sensitive skin, age, payments
- Loyalty Program: Points and reward threshold
- Social Media and Reviews: Instagram sharing and Google reviews

Image Assignment Map
--------------------
- Home hero -> salon_interior_hero.jpg: Warm, polished salon setting fits the strongest first impression.
- Services hero -> hair_colouring.avif with hair_colouring.jpg fallback: Skilled service image reinforces colour expertise and active treatment.
- About feature -> salon_tools.avif: Organised workstation supports professionalism, product quality, and craft.
- Packages hero -> facial_spa_treatment.jpg: Calm, restorative mood matches bundle and pamper messaging.
- Visit hero -> backwash_area.jpg: Clean interior supports comfort, arrival confidence, and service environment.
- Unassigned -> hair_colouring.jpg: Held as fallback for AVIF delivery only.
- Unassigned -> nail_treatment.avif: Good fit, but not required once pages had stronger unique assignments.
- Unassigned -> website_logo.png: Brand asset left unused because the shared header/footer use a text logo.

Design Token Set
----------------
COLOURS:
  --bg-primary: #fffaf6
  --bg-secondary: #f5ebe5
  --accent: #c86f5b
  --accent-dark: #8e4c3f
  --text-primary: #342726
  --text-muted: #6f5d59
  --border: rgba(52, 39, 38, 0.14)
  --white: #ffffff

TYPOGRAPHY:
  --font-body: Georgia, "Times New Roman", serif
  --font-heading: "Palatino Linotype", "Book Antiqua", Palatino, serif
  --font-mono: Consolas, "Courier New", monospace

SPACING:
  --space-section: 96px
  --space-card: 32px
  --space-gap: 24px

SHAPE:
  --radius-card: 24px
  --radius-btn: 999px

ANIMATION:
  --transition: 0.28s ease

Site Map
--------
Type: Multi-Page
Total pages: 5

1. HOME
   Filename: index.html
   Title: Friendly Beauty Services in Surry Hills
   Nav label: Home
   Sections: Hero, stats, service highlights, salon intro, packages teaser, booking CTA
   Primary CTA: Book Now
   Images: salon_interior_hero.jpg -> Hero
   Links to: services.html, about.html, packages.html, visit.html

2. SERVICES
   Filename: services.html
   Title: Beauty Services and Prices
   Nav label: Services
   Sections: Hero, services grid, product brands marquee, booking policies, CTA banner
   Primary CTA: Book a Service
   Images: hair_colouring.avif -> Hero
   Links to: visit.html, packages.html

3. ABOUT
   Filename: about.html
   Title: About Bella's Beauty Salon
   Nav label: About
   Sections: Hero, salon story, team grid, training and products, CTA banner
   Primary CTA: Meet the Team and Book
   Images: salon_tools.avif -> Salon story
   Links to: services.html, visit.html

4. PACKAGES
   Filename: packages.html
   Title: Packages, Membership and Gift Ideas
   Nav label: Packages
   Sections: Hero, package cards, loyalty strip, gift vouchers, CTA banner
   Primary CTA: Reserve a Package
   Images: facial_spa_treatment.jpg -> Hero
   Links to: visit.html, services.html

5. VISIT
   Filename: visit.html
   Title: Visit Bella's Beauty Salon
   Nav label: Visit
   Sections: Hero, booking options, contact and hours, getting here, FAQs, CTA banner
   Primary CTA: Call or Book Online
   Images: backwash_area.jpg -> Hero
   Links to: index.html, services.html

Navigation order: Home | Services | About | Packages | Visit

Section Blueprints and Component Selections
-------------------------------------------
index.html
- NAV -> nav-sticky
- HERO -> hero-fullscreen
- Stats -> section-highlight-strip
- Service Highlights -> section-grid-cards
- Why Locals Return -> section-split-feature
- Packages and Perks -> section-grid-cards
- Booking CTA -> section-cta-banner
- FOOTER -> footer-full

services.html
- NAV -> nav-sticky
- HERO -> hero-split
- Services Grid -> section-grid-cards
- Product Marquee -> section-marquee
- Booking Details -> section-list-detail
- CTA Banner -> section-cta-banner
- FOOTER -> footer-full

about.html
- NAV -> nav-sticky
- HERO -> hero-minimal
- Salon Story -> section-split-feature
- Team -> team-grid
- Training and Brands -> section-list-detail
- CTA Banner -> section-cta-banner
- FOOTER -> footer-full

packages.html
- NAV -> nav-sticky
- HERO -> hero-split
- Packages -> section-grid-cards
- Loyalty Strip -> section-highlight-strip
- Gift Vouchers -> section-split-feature
- CTA Banner -> section-cta-banner
- FOOTER -> footer-full

visit.html
- NAV -> nav-sticky
- HERO -> hero-split
- Booking Options -> section-grid-cards
- Contact and Hours -> section-list-detail
- Getting Here -> section-grid-cards
- FAQs -> section-list-detail
- CTA Banner -> section-cta-banner
- FOOTER -> footer-full
