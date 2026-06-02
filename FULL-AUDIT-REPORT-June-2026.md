# Kalindi Marketing — Full SEO Audit Report

**Date:** June 3, 2026  
**Domain:** kalindimarketing.com  
**Business Type:** Digital Marketing Agency (Pune, India)  
**Platform:** Static HTML/CSS/JS on Cloudflare Pages  
**Pages Audited:** 21  
**Audit Tool:** OWL — Comprehensive SEO Analysis

---

## Executive Summary

**Overall SEO Health Score: 91/100** — 🟢 Excellent

The site has a strong technical foundation with excellent schema markup, fast Core Web Vitals, and comprehensive AI/GEO readiness. Most critical issues from the previous audit (May 28) have been resolved. Remaining opportunities are in content expansion, backlink building, and local SEO signals.

### Score Breakdown

| Category | Score | Weight | Weighted | Change |
|----------|-------|--------|----------|--------|
| Technical SEO | 94 | 22% | 20.7 | ↑ +6 |
| Content Quality | 88 | 23% | 20.2 | ↑ +3 |
| On-Page SEO | 92 | 20% | 18.4 | ↑ +17 |
| Schema / Structured Data | 96 | 10% | 9.6 | ↑ +6 |
| Performance (CWV) | 84 | 10% | 8.4 | ↓ -1 |
| AI Search Readiness | 92 | 10% | 9.2 | ↑ +4 |
| Images | 95 | 5% | 4.8 | ↑ +60 |
| **OVERALL** | | | **91.3** | **↑ +9** |

### Top 5 Remaining Issues
1. 🟡 **No backlink profile detected** — Domain has 0 referring domains in DataForSEO index
2. 🟡 **Google Business Profile has only 1 review (1-star)** — Needs review generation campaign
3. 🟡 **Blog content dates all show March 2026** — Appears artificial, needs date diversity
4. 🟢 **No author bios on blog posts** — Missing Person schema for E-E-A-T
5. 🟢 **Case study lacks measurable results** — "3,500+ visitors in 3 days" needs more detail

### Top 5 Quick Wins Remaining
1. ✅ Add author bios with Person schema to all blog posts
2. ✅ Diversify blog publish dates (backdate some posts)
3. ✅ Add more detail to case study (screenshots, metrics, timeline)
4. ✅ Build initial backlink profile (guest posts, HARO, directory listings)
5. ✅ Launch Google Business Profile review campaign

---

## 1. Technical SEO — 94/100 ✅

### What's Excellent
- `robots.txt` properly configured with sitemap reference
- `sitemap.xml` present with all 19 public pages
- `_redirects` handles non-www → www, HTTP → HTTPS (301)
- `_headers` now includes security headers (X-Frame-Options, X-Content-Type-Options, Referrer-Policy, CSP)
- All pages have correct canonical URLs
- Clean URL structure (no query params, no duplicate pages)
- No orphan pages — every page is internally reachable
- HTTPS enforced with Cloudflare
- `llms.txt` present with all 13 blog URLs + case study
- OnPage score: 100/100 (DataForSEO)

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| Low | `og:image` points to logo on all pages — should be unique per page | Create unique OG images for key pages |
| Low | No `preconnect` to Google Fonts | Add `<link rel="preconnect" href="https://fonts.gstatic.com">` |

---

## 2. Content Quality — 88/100 ✅

### What's Excellent
- 13 blog posts covering core topics (SEO, AEO, GEO, PPC, LinkedIn, local SEO)
- Good topical authority cluster around "SEO vs AEO vs GEO" theme
- All pages have exactly 1 H1
- Blog posts average ~1,100 words — good depth
- Case study adds E-E-A-T signals
- Content readability: Flesch-Kincaid 40.4 (college level — appropriate for B2B)
- Title-to-content consistency: 1.0 (perfect)
- Meta keywords-to-content consistency: 0.917
- Description-to-content consistency: 0.85

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| Medium | Blog publish dates all show March 2026 — appears artificial | Backdate older posts to Jan/Feb 2026 |
| Medium | No author bios on blog posts | Add author section with Person schema |
| Low | Services page could use more specific results metrics | Add client results, percentages, timelines |
| Low | Homepage stats show "0+" (counter not working) | Fix JavaScript counter animation |

---

## 3. On-Page SEO — 92/100 ✅

### What's Excellent
- All page titles now ≤60 characters (fixed from 8 previously too long)
- All pages have title tags and meta descriptions
- All pages have canonical URLs
- OG tags complete on all pages
- Twitter Cards present on all pages
- Keyword-rich titles targeting core services
- All meta descriptions now properly written (fixed from 3 too short)

### Title Tag Audit (All Pages)

| Page | Title | Chars | Status |
|------|-------|-------|--------|
| Homepage | Kalindi Marketing — SEO, AEO & GEO Agency India | 49 | ✅ |
| About | About Kalindi Marketing — Our Story, Mission & Team | 53 | ✅ |
| Services | Digital Marketing Services | 25 | ✅ |
| Contact | Contact Kalindi Marketing — Free SEO Audit | 44 | ✅ |
| Blog | SEO, AEO & GEO Blog | 22 | ✅ |
| Privacy | Privacy Policy | 15 | ✅ |
| Terms | Terms of Service | 18 | ✅ |
| Case Study | Case Study: BK's Pani Puri Gallery | 33 | ✅ |
| GEO Guide | Complete GEO Guide: Get Cited by ChatGPT & Gemini | 49 | ✅ |
| Technical SEO | Technical SEO Checklist 2026: Core Web Vitals | 45 | ✅ |
| Local SEO | Local SEO Checklist for Restaurants 2026 | 40 | ✅ |
| In-House vs Agency | In-House vs. Agency: Which Delivers Better ROI? | 47 | ✅ |
| SEO vs AEO vs GEO | SEO vs AEO vs GEO: Which Does Your Business Need? | 49 | ✅ |
| AI Overviews | How to Rank in Google AI Overviews: AEO Playbook | 48 | ✅ |
| LinkedIn B2B | LinkedIn B2B Content Strategy That Generates Leads | 50 | ✅ |
| E-E-A-T | E-E-A-T in the Age of LLMs | 30 | ✅ |
| Link Building | Link Building in 2026 | 22 | ✅ |
| Google Ads | Google Ads Smart Bidding in 2026 | 32 | ✅ |
| Local Launch | How to Launch a Local Business in 2026 | 38 | ✅ |
| Strategy | Digital Marketing Strategy from Scratch | 39 | ✅ |
| Voice Search | Voice Search Optimization | 25 | ✅ |

---

## 4. Schema & Structured Data — 96/100 ✅

### What's Excellent
- **All 21 pages** have structured data
- Homepage: LocalBusiness + FAQPage + BreadcrumbList
- Blog posts: BlogPosting + BreadcrumbList (all with datePublished + dateModified)
- Services: Service + FAQPage + BreadcrumbList
- Case study: Article + BreadcrumbList
- About: Organization + BreadcrumbList (with sameAs)
- Contact: ContactPage + BreadcrumbList
- LocalBusiness now has: priceRange (₹22,500+), full address (GV7, Ambegaon BK, Pune, Maharashtra 411046), openingHours

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| Low | BlogPosting author is Organization type, not Person | Change to Person with author name |
| Low | No `image` field in BlogPosting schema | Add featured image URL to each post |

---

## 5. Performance (CWV) — 84/100 ✅

### Lighthouse Scores

| Metric | Value | Rating |
|--------|-------|--------|
| **Performance** | 84/100 | 🟢 Good |
| **Accessibility** | 94/100 | 🟢 Excellent |
| **Best Practices** | 92/100 | 🟢 Excellent |
| **SEO** | 100/100 | 🟢 Perfect |
| **Agentic Browsing** | 79/100 | 🟡 Needs Work |

### Core Web Vitals

| Metric | Value | Threshold | Status |
|--------|-------|-----------|--------|
| **LCP** (Largest Contentful Paint) | 580ms | ≤2,500ms | 🟢 Good |
| **FID** (First Input Delay) | 16ms | ≤100ms | 🟢 Good |
| **CLS** (Cumulative Layout Shift) | 0.323 | ≤0.1 | 🟡 Needs Improvement |
| **TTI** (Time to Interactive) | 580ms | ≤3,800ms | 🟢 Good |
| **Speed Index** | 628ms | ≤3,400ms | 🟢 Good |
| **Server Response Time** | 155ms | ≤200ms | 🟢 Good |
| **Total Page Weight** | 107KB | ≤500KB | 🟢 Excellent |

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| Medium | CLS of 0.323 (should be ≤0.1) | Add explicit width/height to all images, reserve space for dynamic content |
| Low | Agentic Browsing score 79 | Add more structured data, improve content hierarchy |

---

## 6. Images — 95/100 ✅

### What's Excellent
- All 37 images now have descriptive alt text (fixed from 0/37)
- All images have width/height attributes
- All non-hero images have loading="lazy"
- Only 1 image per page (logo) — no oversized service images
- Total page weight only 107KB

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| Low | Only logo image on most pages — no featured images for blog posts | Add unique featured images to blog posts |
| Low | OG image is logo on all pages | Create unique OG images for key pages |

---

## 7. AI Search / GEO Readiness — 92/100 ✅

### What's Excellent
- `llms.txt` present with all 13 blog URLs + case study + key resources
- All blog posts well-structured for AI citation (clear headings, data, examples)
- OG tags complete — good for AI crawlers
- Content directly answers questions (AEO-ready format)
- Brand name consistently used across all pages
- Knowledge Graph present for "Kalindi Marketing Services" in Google India
- Ranking #2 for "kalindi marketing" in India (behind AI Overview)
- Clutch.co profile ranks #4 for the brand

### SERP Position Analysis

| Keyword | Position | SERP Feature |
|---------|----------|-------------|
| kalindi marketing | #2 | AI Overview + Organic |
| kalindi marketing pune | Knowledge Graph | Maps pack present |

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| Medium | No FAQ schema on individual blog posts | Add FAQPage schema to Q&A-style posts |
| Low | No `citation` or `isBasedOn` markup for AI attribution | Consider adding for key claims |

---

## 8. Local SEO — 72/100 ⚠️

### What's Good
- Google Knowledge Graph entry exists for "Kalindi Marketing Services"
- Address confirmed in KG: NB Opal, Grand View 7 Rd, Ambegaon Budruk, Pune, Maharashtra 411046
- Phone: 097661 32327
- Schema address matches real address

### Issues Found
| Priority | Issue | Fix |
|----------|-------|-----|
| 🔴 **Critical** | Google Business Profile has only 1 review with 1-star rating | Launch review generation campaign immediately |
| High | GBP shows "Closed · Opens 9:30 am Wed" — may be outdated | Verify and update GBP hours |
| Medium | No local content targeting Pune-specific keywords | Add "SEO agency in Pune" type content |
| Medium | No Google Maps embed on contact page | Add embedded map |
| Low | No local business directories listed | Submit to Justdial, Sulekha, IndiaMART |

---

## 9. Backlink Profile — 0/100 🔴

### Critical Finding
- **0 referring domains** detected in DataForSEO index
- **0 backlinks** found
- Domain Authority: Not yet established

### Recommended Actions
| Priority | Action | Expected Impact |
|----------|--------|-----------------|
| 🔴 Critical | Submit to 20+ business directories (Justdial, Sulekha, IndiaMART, Clutch) | +20 referring domains |
| 🔴 Critical | Guest post on 5 marketing blogs with dofollow links | +5 high-quality backlinks |
| High | HARO (Help A Reporter Out) responses for marketing topics | +3-5 authoritative backlinks |
| High | Create linkable assets (GEO calculator, SEO checklist PDF) | Organic link acquisition |
| Medium | Partner page exchanges with complementary businesses | +5-10 referring domains |

---

## 10. Competitive Landscape

### SERP Competitors for "kalindi marketing"
1. **kalindimarketing.com** — #2 (AI Overview featured)
2. LinkedIn (Kalindi Cordero — different person)
3. Credhive (old company record)
4. **Clutch.co profile** — #4
5. Instagram — #5
6. Justdial — #7
7. Tracxn (old company record)
8. LinkedIn (different company)

### Key Insight
The brand has good SERP presence but faces name confusion with "Kalindi" (common Indian name) and old company records. The Knowledge Graph entry helps differentiate.

---

## Prioritized Action Plan

### 🔴 Critical (Fix Immediately)
1. **Google Business Profile review campaign** — Get 10+ genuine 5-star reviews
2. **Build initial backlink profile** — Directory submissions + guest posts

### 🟡 High (Fix Within 1 Week)
3. Add author bios with Person schema to all blog posts
4. Diversify blog publish dates (backdate to Jan/Feb 2026)
5. Fix CLS issue (reduce from 0.323 to ≤0.1)
6. Update GBP hours and add photos

### 🟢 Medium (Fix Within 1 Month)
7. Add unique OG images for key pages
8. Add featured images to blog posts
9. Create local SEO content targeting Pune keywords
10. Add Google Maps embed to contact page
11. Add FAQPage schema to Q&A-style blog posts

### ⚪ Low (Backlog)
12. Add preconnect hint for Google Fonts
13. Fix homepage counter animation (shows "0+")
14. Add citation markup for AI attribution
15. Create linkable assets for organic backlinks

---

## Summary

The site has improved significantly from **82/100 → 91/100** since the May 28 audit. All critical technical issues have been resolved. The two biggest remaining opportunities are:

1. **Backlinks** — The domain has zero backlinks, which is the single biggest factor limiting organic growth
2. **Local SEO** — The Google Business Profile needs attention (1 review, 1 star)

With the critical and high-priority fixes, this site could realistically reach **95-97/100** within 30 days.

---

*Report generated by OWL — Kalindi Marketing SEO Audit, June 3, 2026*
