# GSC Setup Required for Kalindi Marketing

## Issue
Google Search Console is currently configured for wrong domain (paramppara.farm). 
Need to fix for kalindimarketing.com.

## Steps for Sourabh to do manually:

### 1. Add kalindimarketing.com to GSC
- Go to https://search.google.com/search-console
- Add property: https://www.kalindimarketing.com (URL-prefix type)
- Verify ownership (DNS record or HTML file upload)

### 2. Grant Service Account Access
- In GSC → Settings → Users & Permissions
- Add the service account email as Owner
- This enables API-based sitemap submission and indexing

### 3. Submit Sitemap
Once GSC is set up correctly, run:
- Submit: https://www.kalindimarketing.com/sitemap.xml
- Request indexing for key pages:
  - /best-digital-marketing-agency-india/
  - /state-of-geo-india-2026/
  - /services/
  - /case-study-parampara-farm/
  - /case-study-bks-pani-puri/

### Why This Matters
Without GSC, we can't:
- Track keyword rankings and impressions in Google
- Submit new pages for indexing quickly
- Monitor for crawl errors or penalties
- See which queries drive traffic

**This is the #1 priority task for this week.**
