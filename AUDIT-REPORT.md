# Kalindi Marketing — Full SEO Audit Report

**Date:** May 28, 2026  
**Domain:** kalindimarketing.com  
**Pages Audited:** 21  
**Business Type:** Digital Marketing Agency (India, Pune)  
**Platform:** Static HTML/CSS/JS on Cloudflare Pages

---

## Executive Summary

**Overall SEO Health Score: 82/100** — 🟢 Good foundation with clear optimization opportunities.

The site has strong technical infrastructure, comprehensive schema markup, and excellent AI/GEO readiness. The biggest wins are in image optimization and on-page title/description tuning.

### Top 5 Critical Issues
1. 🔴 **All 39 images missing alt text** — accessibility + SEO penalty
2. 🔴 **9 oversized images (560–664 KB each)** — will tank LCP scores
3. 🟡 **8 page titles exceed 60 chars** — will truncate in SERPs
4. 🟡 **3 pages have very short meta descriptions** (17–25 chars)
5. 🟡 **1 blog post is thin** (639 words vs 1,200+ target)

### Top 5 Quick Wins
1. ✅ Add descriptive alt text to all images (30 min with AI)
2. ✅ Compress/resize service images to <200 KB each
3. ✅ Shorten 8 long titles to 50–60 chars
4. ✅ Write proper meta descriptions for Privacy, Terms, Services pages
5. ✅ Expand "In-House vs Agency" blog to 1,200+ words

---

## Category Breakdown

| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Technical SEO | 88 | 22% | 19.4 |
| Content Quality | 85 | 23% | 19.6 |
| On-Page SEO | 75 | 20% | 15.0 |
| Schema / Structured Data | 90 | 10% | 9.0 |
| Performance (CWV) | 85 | 10% | 8.5 |
| AI Search Readiness | 88 | 10% | 8.8 |
| Images | 35 | 5% | 1.8 |
| **OVERALL** | | | **82.0** |

---

## 1. Technical SEO — 88/100 ✅

### What's Good
- `robots.txt` properly configured with sitemap reference
- `sitemap.xml` present with all 19 public pages, correct `<lastmod>` dates
- `_redirects` handles non-www → www, HTTP → HTTPS (301)
- `_headers` sets 1-year cache on assets/styles/scripts
- `.htaccess` has fallback cache headers for images/CSS/JS
- All pages have correct canonical URLs
- Clean URL structure (no query params, no duplicate paths)
- No orphan pages — every page is internally reachable

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| Medium | `_headers` missing security headers (X-Frame-Options, X-Content-Type-Options, Referrer-Policy) | Add security headers block |
| Medium | No `X-Robots-Tag` in headers for legal pages | Add noindex for privacy/terms if desired |
| Low | `.htaccess` is fallback-only (Cloudflare handles it) | Document that CF is primary |

---

## 2. Content Quality — 85/100 ✅

### What's Good
- 13 blog posts covering core topics (SEO, AEO, GEO, PPC, LinkedIn, local SEO)
- Good topical authority cluster around "SEO vs AEO vs GEO" theme
- All pages have exactly 1 H1
- Blog posts average ~1,050 words — decent depth
- Case study adds E-E-A-T signals (real client results)

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| High | `blog-in-house-vs-agency` only 639 words | Expand to 1,200+ words with ROI data, comparison tables |
| Medium | No author bios on blog posts | Add `author` field with Person schema to BlogPosting |
| Medium | No visible publish/modify dates on blog posts | Add `datePublished` / `dateModified` visibly |
| Low | Services page could use more descriptive copy (currently 1,222 words but generic) | Add case study snippets, results metrics |

---

## 3. On-Page SEO — 75/100 ⚠️

### What's Good
- All pages have title tags and meta descriptions
- All pages have canonical URLs
- OG tags complete on all pages (title, description, image, url, type)
- Twitter Cards present on all pages
- Keyword-rich titles targeting core services

### Issues Found

**Title Tags Too Long (>60 chars) — 8 pages:**
| Page | Current Title | Chars |
|------|--------------|-------|
| blog-geo-guide | The Complete Guide to GEO: How to Get Your Brand Cited by ChatGPT & Gemini \| Kalindi Marketing | 94 |
| blog-technical-seo | Technical SEO Checklist for 2026: Core Web Vitals & AI Readiness \| Kalindi Marketing | 84 |
| blog-local-seo-checklist | The Ultimate Local SEO Checklist for Restaurants & Cafes in 2026 \| Kalindi Marketing | 84 |
| blog-in-house-vs-agency | In-House vs. Digital Marketing Agency: Which is Better for ROI in 2026? \| Kalindi Marketing | 91 |
| blog-seo-vs-aeo-vs-geo | SEO vs AEO vs GEO: Which One Does Your Business Need? \| Kalindi Marketing | 73 |
| blog-google-ai-overviews | How to Appear in Google AI Overviews: The AEO Playbook \| Kalindi Marketing | 74 |
| blog-linkedin-b2b | LinkedIn Content Strategy That Generates B2B Leads \| Kalindi Marketing | 70 |
| contact | Contact Kalindi Marketing — Get Your Free Digital Marketing Audit | 65 |

**Meta Descriptions Too Short — 3 pages:**
| Page | Current Desc | Chars |
|------|-------------|-------|
| privacy-policy | "Kalindi Marketing" | 17 |
| services | "Explore Kalindi Marketing" | 25 |
| terms | "Kalindi Marketing" | 17 |

---

## 4. Schema & Structured Data — 90/100 ✅

### What's Good
- **All 21 pages** have structured data — excellent coverage
- Homepage: LocalBusiness + FAQPage + BreadcrumbList
- Blog posts: BlogPosting + BreadcrumbList
- Services: Service + FAQPage + BreadcrumbList
- Case study: Article + BreadcrumbList
- About: Organization + BreadcrumbList
- Contact: ContactPage + BreadcrumbList

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| Medium | LocalBusiness missing `priceRange` | Add `"priceRange": "₹₹"` or similar |
| Medium | LocalBusiness missing `openingHours` | Add if applicable |
| Medium | LocalBusiness.address missing `streetAddress`, `postalCode` | Add full address |
| Low | BlogPosting on in-house-vs-agency missing `dateModified` | Add dateModified field |
| Low | Organization (about page) missing `sameAs` for social profiles | Add LinkedIn, Twitter URLs |

---

## 5. Performance (CWV) — 85/100 ✅

### What's Good
- Static HTML — no JS framework overhead
- 1-year cache headers on all static assets
- Fonts loaded with `preload` + `noscript` fallback
- CSS animations loaded with `media="print"` trick
- No render-blocking resources detected in HTML

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| 🔴 Critical | 9 service images are 560–664 KB each (PNG) | Convert to WebP, compress to <150 KB |
| High | No lazy loading on below-fold images | Add `loading="lazy"` to non-hero images |
| Medium | No explicit width/height on images (causes CLS) | Add width/height attributes |
| Low | No preconnect to external domains | Add `<link rel="preconnect" href="https://fonts.googleapis.com">` |

---

## 6. AI Search / GEO Readiness — 88/100 ✅

### What's Good
- `llms.txt` present with 4 sections (Core Services, Key Resources, Case Studies, Further Reading)
- All blog posts well-structured for AI citation (clear headings, data, examples)
- OG tags complete — good for AI crawlers that read OG
- Content directly answers questions (AEO-ready format)
- Brand name consistently used across all pages

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| Medium | llms.txt could include more blog post links | Add all 13 blog URLs under Further Reading |
| Medium | No FAQ schema on individual blog posts | Add FAQPage schema to Q&A-style posts |
| Low | No `citation` or `isBasedOn` markup for AI attribution | Consider adding for key claims |

---

## 7. Images — 35/100 🔴

### Critical Issues
- **39/39 images have NO alt text** — this is an accessibility violation and SEO miss
- **9 service images are oversized** (560–664 KB PNGs) — will severely impact LCP
- No lazy loading on any image
- No explicit dimensions (width/height) — causes CLS

### Image Inventory (assets/images/)
| File | Size | Format | Alt Text |
|------|------|--------|----------|
| about-team.png | 572 KB | PNG | ❌ Missing |
| aeo-service.png | 573 KB | PNG | ❌ Missing |
| blog-featured.png | 597 KB | PNG | ❌ Missing |
| contact-visual.png | 646 KB | PNG | ❌ Missing |
| geo-service.png | 664 KB | PNG | ❌ Missing |
| hero-visual.png | 622 KB | PNG | ❌ Missing |
| ppc-service.png | 561 KB | PNG | ❌ Missing |
| seo-service.png | 578 KB | PNG | ❌ Missing |
| social-service.png | 621 KB | PNG | ❌ Missing |

### Recommended Actions
1. Convert all PNGs to WebP (60–80% size reduction)
2. Resize to max 800px width for service images
3. Add descriptive alt text to every image
4. Add `loading="lazy"` to non-hero images
5. Add `width` and `height` attributes to prevent CLS

---

## 8. Internal Linking — 92/100 ✅

### What's Good
- **Zero orphan pages** — every page is reachable
- All 13 blog posts link to `/services/` (strong topical authority flow)
- Homepage links to all key pages (services, blog, about, contact)
- Blog posts average 17 outgoing internal links
- Blog index page links to all 13 posts

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| Low | Blog posts don't cross-link to related posts | Add "Related Articles" section at bottom |
| Low | Case study doesn't link to relevant blog posts | Link to local-business-launch, local-seo-checklist |

---

## Prioritized Action Plan

### 🔴 Critical (Fix Immediately)
1. **Add alt text to all 39 images** — use AI to generate descriptions, then review
2. **Compress and convert 9 service images** — PNG → WebP, target <150 KB each

### 🟡 High (Fix Within 1 Week)
3. **Shorten 8 long page titles** to 50–60 characters
4. **Write proper meta descriptions** for Privacy Policy, Terms, Services pages (120–155 chars)
5. **Expand "In-House vs Agency" blog** to 1,200+ words with data/tables
6. **Add `loading="lazy"` and `width`/`height`** to all `<img>` tags

### 🟢 Medium (Fix Within 1 Month)
7. Add `priceRange`, `openingHours`, full address to LocalBusiness schema
8. Add `dateModified` to all BlogPosting schemas
9. Add `sameAs` (social URLs) to Organization schema
10. Add author bios with Person schema to blog posts
11. Add security headers to `_headers` file
12. Expand llms.txt with all blog post URLs

### ⚪ Low (Backlog)
13. Add "Related Articles" cross-links between blog posts
14. Add FAQPage schema to Q&A-style blog posts
15. Add preconnect hint for Google Fonts
16. Link case study to related blog posts

---

## Summary

The site is in **good shape overall (82/100)** with a solid technical foundation. The two biggest areas for improvement are:

1. **Images** — completely missing alt text and oversized (this alone is dragging 5% of your score)
2. **On-Page tuning** — title tags and descriptions need tightening

The schema implementation is excellent, AI/GEO readiness is strong, and the internal linking structure is clean. With the critical and high-priority fixes, this site could realistically reach **90–92/100**.

---

*Report generated by OWL — Kalindi Marketing SEO Audit, May 28, 2026*
