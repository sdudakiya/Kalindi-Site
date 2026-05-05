# 🔍 Full Site Audit: kalindimarketing.com × Google Search Console
**Date**: May 5, 2026 | **Total Pages Audited**: 19 | **GSC Period**: Last 90 Days

---

## 📊 Audit Summary

| Category | Score | Details |
| :--- | :---: | :--- |
| 🔴 **Critical Issues** | **3** | Sitemap/canonical mismatch, wildcard caching, .htaccess bug |
| 🟠 **High Priority** | **5** | Pages invisible to Google, missing schema, placeholder links |
| 🟡 **Medium Priority** | **4** | Thin content, stale dates, internal linking gaps |
| 🟢 **Good Practices** | **7** | Schema markup, meta descriptions, canonical tags, OG tags |

---

## 🔴 CRITICAL ISSUES

### 1. Sitemap vs Canonical Domain Mismatch

> [!CAUTION]
> **Your sitemap and canonical tags point to DIFFERENT domains.** This is the #1 reason Google is splitting your impressions between `www` and `non-www`.

| File | Domain Used |
| :--- | :--- |
| `sitemap.xml` | `https://kalindimarketing.com/` (non-www) ❌ |
| All `<link rel="canonical">` tags | `https://www.kalindimarketing.com/` (www) ✅ |
| `robots.txt` | `https://www.kalindimarketing.com/sitemap.xml` (www) ✅ |
| Schema `"url"` | `https://www.kalindimarketing.com` (www) ✅ |
| `llms.txt` | `https://www.kalindimarketing.com/` (www) ✅ |

**GSC Impact**: Your homepage impressions are split across 2 versions:
- `https://kalindimarketing.com/` → 95 impressions, 12 clicks
- `https://www.kalindimarketing.com/` → 61 impressions, 1 click

**Fix**: Update every `<loc>` in `sitemap.xml` to use `https://www.kalindimarketing.com/` to match your canonicals.

---

### 2. Wildcard Cache Header Caches HTML Pages

> [!CAUTION]
> Your `_headers` file applies `Cache-Control: public, max-age=31536000` (1 year) to **ALL files** (`/*`), including HTML pages. This means browsers and CDNs will cache your HTML for a full year.

```
# _headers - Current (BROKEN)
/*
  Cache-Control: public, max-age=31536000
```

**Fix**: Scope the caching rule to static assets only:
```
/*.css
  Cache-Control: public, max-age=31536000
/*.js
  Cache-Control: public, max-age=31536000
/assets/*
  Cache-Control: public, max-age=31536000
```

---

### 3. `.htaccess` Syntax Error

> [!WARNING]
> Line 15 of `.htaccess` has a missing space: `ExpiresByTypetext/css` instead of `ExpiresByType text/css`. Apache will silently ignore this directive, meaning your CSS files won't get browser-level cache headers on Apache servers.

```diff
- ExpiresByTypetext/css "access plus 1 year"
+ ExpiresByType text/css "access plus 1 year"
```

---

## 🟠 HIGH PRIORITY ISSUES

### 4. 12 of 19 Pages Have ZERO Search Impressions

Cross-referencing your sitemap (19 URLs) with GSC data (90 days), **only 7 pages** have generated any impressions at all:

| Page | In Sitemap | GSC Impressions | GSC Clicks | Status |
| :--- | :---: | :---: | :---: | :--- |
| `/` (Homepage) | ✅ | **156** (split) | 13 | ✅ Indexed |
| `/about/` | ✅ | **42** (split) | 0 | ✅ Indexed |
| `/services/` | ✅ | **13** | 0 | ✅ Indexed |
| `/contact/` | ✅ | **29** | 0 | ✅ Indexed |
| `/blog-local-business-launch/` | ✅ | **47** (split) | 0 | ✅ Indexed |
| `/blog-link-building/` | ✅ | **8** | 0 | ✅ Indexed |
| `/blog-google-ads-bidding/` | ✅ | **13** | 0 | ✅ Indexed |
| `/blog-linkedin-b2b/` | ✅ | **5** | 0 | ✅ Indexed |
| `/blog/` | ✅ | **0** | 0 | ❌ Invisible |
| `/blog-geo-guide/` | ✅ | **0** | 0 | ❌ Invisible |
| `/blog-technical-seo/` | ✅ | **0** | 0 | ❌ Invisible |
| `/blog-google-ai-overviews/` | ✅ | **0** | 0 | ❌ Invisible |
| `/blog-seo-vs-aeo-vs-geo/` | ✅ | **0** | 0 | ❌ Invisible |
| `/blog-eeat-llms/` | ✅ | **0** | 0 | ❌ Invisible |
| `/blog-voice-search/` | ✅ | **0** | 0 | ❌ Invisible |
| `/blog-strategy-from-scratch/` | ✅ | **0** | 0 | ❌ Invisible |
| `/blog-local-seo-checklist/` | ✅ | **0** | 0 | ❌ Invisible |
| `/blog-in-house-vs-agency/` | ✅ | **0** | 0 | ❌ Invisible |
| `/case-study-bks-pani-puri/` | ✅ | **0** | 0 | ❌ Invisible |

> [!IMPORTANT]
> **12 pages have zero impressions.** This likely means they are either not indexed, not ranking for any query, or too new. Consider using GSC's URL Inspection tool or submitting the sitemap to trigger re-crawling.

---

### 5. Missing Schema Markup on 2 Pages

| Page | Schema (ld+json) | OG Image |
| :--- | :---: | :---: |
| `/blog-local-seo-checklist/` | ❌ Missing | ❌ Missing |
| `/case-study-bks-pani-puri/` | ❌ Missing | ❌ Missing |
| `/blog-in-house-vs-agency/` | ⚠️ Only 1 block (no Article schema?) | ✅ Present |

All other blog posts have 2 schema blocks (Article + BreadcrumbList). These two pages are missing both.

---

### 6. Placeholder Social Media Links

Your footer has 4 social links all pointing to `href="#"`:

```html
<a href="#" class="social-icon" aria-label="LinkedIn">in</a>
<a href="#" class="social-icon" aria-label="Instagram">▦</a>
<a href="#" class="social-icon" aria-label="Twitter">𝕏</a>
<a href="#" class="social-icon" aria-label="YouTube">▶</a>
```

Yet your schema declares actual social URLs:
```json
"sameAs": [
  "https://www.linkedin.com/company/kalindimarketing",
  "https://www.instagram.com/kalindimarketing",
  ...
]
```

**Fix**: Replace `#` with actual social profile URLs, or remove the `sameAs` from schema if profiles don't exist yet. Google penalizes mismatched structured data.

---

### 7. Privacy Policy & Terms Link to `#`

```html
<a href="#">Privacy Policy</a>
<a href="#">Terms of Service</a>
```

Google's E-E-A-T signals include having real legal pages. Create `/privacy-policy/` and `/terms/` pages.

---

## 🟡 MEDIUM PRIORITY

### 8. Thin Content on Some Blog Posts

Blog post word counts (HTML source, includes markup — actual content is lower):

| Blog Post | Word Count (HTML) | Assessment |
| :--- | :---: | :--- |
| `/blog-local-seo-checklist/` | **643** | ⚠️ Very thin |
| `/blog-linkedin-b2b/` | **748** | ⚠️ Thin |
| `/blog-in-house-vs-agency/` | **797** | ⚠️ Thin |
| `/blog-link-building/` | **840** | 🟡 Below average |
| `/blog-strategy-from-scratch/` | **842** | 🟡 Below average |
| `/blog-eeat-llms/` | **854** | 🟡 Below average |
| `/blog-voice-search/` | **826** | 🟡 Below average |
| `/blog-google-ads-bidding/` | **851** | 🟡 Below average |
| `/blog-seo-vs-aeo-vs-geo/` | **907** | 🟡 Okay |
| `/blog-google-ai-overviews/` | **952** | 🟡 Okay |
| `/blog-technical-seo/` | **1,071** | ✅ Good |
| `/blog-local-business-launch/` | **1,110** | ✅ Good |
| `/blog-geo-guide/` | **1,321** | ✅ Good |

> [!TIP]
> Given these are HTML word counts (including boilerplate nav/footer), actual content word counts are likely 40-60% lower. For competitive SEO topics, aim for **1,500-2,500 words** of actual body content.

---

### 9. Stale `lastmod` Dates in Sitemap

All 19 URLs show `lastmod` dates of either `2026-03-13` or `2026-03-28`. If you've updated content since then, update these dates. Google uses `lastmod` to prioritize re-crawling.

---

### 10. Internal Linking Gaps

Two blog posts have significantly fewer internal links than the others:

| Post | Links to `/services/` | Cross-links to other blogs | Links to `/contact/` |
| :--- | :---: | :---: | :---: |
| `/blog-in-house-vs-agency/` | **1** | **0** | 3 |
| `/blog-local-seo-checklist/` | **1** | **0** | 1 |
| Average (other posts) | **6** | **3** | **4** |

These two posts are also the ones with missing schema and OG tags — they appear to have been built with a different template.

---

### 11. HTTP URL Still in Google's Index

GSC shows `http://www.kalindimarketing.com/blog-local-business-launch/` (19 impressions). This is the **HTTP** version. Ensure your hosting enforces HTTPS redirects for all traffic.

---

## 🟢 WHAT'S WORKING WELL

| ✅ | Detail |
| :--- | :--- |
| **Title Tags** | All 19 pages have unique, keyword-rich titles |
| **Meta Descriptions** | All 19 pages have unique meta descriptions |
| **Canonical Tags** | All pages have canonical tags (consistently `www`) |
| **H1 Tags** | All pages have exactly 1 `<h1>` tag |
| **Schema Markup** | 16 of 19 pages have structured data (LocalBusiness, Article, FAQ, BreadcrumbList) |
| **OG Tags** | 17 of 19 pages have Open Graph meta tags |
| **Image Alt Text** | All images have descriptive alt attributes |
| **Font Loading** | Smart preload + noscript fallback pattern |
| **Browser Caching** | `.htaccess` configured (minus the CSS typo) |
| **llms.txt** | Present for AI crawler discoverability (GEO-aware!) |
| **FAQPage Schema** | Homepage has comprehensive FAQ structured data |

---

## 🛠️ Prioritized Fix List

| Priority | Action | Impact | Effort |
| :--- | :--- | :---: | :---: |
| 🔴 1 | Fix sitemap.xml domain → `www.kalindimarketing.com` | High | 5 min |
| 🔴 2 | Fix `_headers` wildcard → scope to static assets only | High | 5 min |
| 🔴 3 | Fix `.htaccess` typo: `ExpiresByTypetext/css` | Medium | 1 min |
| 🟠 4 | Add schema + OG tags to `/blog-local-seo-checklist/` and `/case-study-bks-pani-puri/` | Medium | 30 min |
| 🟠 5 | Replace `href="#"` social links with real URLs or remove | Medium | 10 min |
| 🟠 6 | Create Privacy Policy and Terms of Service pages | Medium | 1 hr |
| 🟠 7 | Submit updated sitemap to GSC for re-crawling | High | 5 min |
| 🟡 8 | Expand thin blog posts to 1,500+ words | High | 3-5 hrs |
| 🟡 9 | Add internal links to `/blog-in-house-vs-agency/` and `/blog-local-seo-checklist/` | Medium | 15 min |
| 🟡 10 | Update `lastmod` dates in sitemap | Low | 5 min |
| 🟡 11 | Ensure HTTPS redirect for all HTTP traffic | High | 15 min |
