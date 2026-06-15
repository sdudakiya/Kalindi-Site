#!/usr/bin/env python3
"""
Add 'Want to Learn More?' sections to all blog posts based on their cluster.
"""
import os

SITE_ROOT = os.path.expanduser("~/clients/kalindi-marketing/Kalindi-Site")

# Cluster mappings
BLOG_CLUSTER_MAPPING = {
    "blog-geo-guide": {  # GEO Cluster
        "service": "/geo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/state-of-geo-india-2026/"
    },
    "state-of-geo-india-2026": {  # GEO Cluster
        "service": "/geo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/blog-geo-guide/"
    },
    "geo-vs-seo-india": {  # GEO Cluster
        "service": "/geo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/blog-geo-guide/"
    },
    "top-geo-agencies-india-2026": {  # GEO Cluster
        "service": "/geo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/blog-geo-guide/"
    },
    "ai-search-optimization": {  # GEO Cluster
        "service": "/geo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/geo-vs-seo-india/"
    },
    "llm-optimization": {  # GEO Cluster
        "service": "/geo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/ai-search-optimization/"
    },
    "chatgpt-seo": {  # GEO Cluster
        "service": "/geo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/ai-search-optimization/"
    },
    "ai-visibility-optimization": {  # GEO Cluster
        "service": "/geo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/llm-optimization/"
    },
    "agentic-digital-marketing": {  # GEO Cluster
        "service": "/geo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/ai-marketing-automation-india/"
    },
    "ai-marketing-automation-india": {  # GEO Cluster
        "service": "/geo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/agentic-digital-marketing/"
    },
    # SEO Cluster
    "blog-technical-seo": {
        "service": "/services/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/blog-link-building/"
    },
    "blog-link-building": {
        "service": "/services/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/blog-technical-seo/"
    },
    "blog-eeat-llms": {
        "service": "/services/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/blog-technical-seo/"
    },
    "blog-voice-search": {
        "service": "/aeo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/blog-google-ai-overviews/"
    },
    "blog-seo-vs-aeo-vs-geo": {
        "service": "/services/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/blog-technical-seo/"
    },
    "blog-strategy-from-scratch": {
        "service": "/services/",
        "case_study": "/case-study-bks-pani-puri/",
        "related_blog": "/blog-in-house-vs-agency/"
    },
    "blog-local-seo-checklist": {
        "service": "/services/",
        "case_study": "/case-study-bks-pani-puri/",
        "related_blog": "/blog-local-business-launch/"
    },
    "blog-linkedin-b2b": {
        "service": "/services/",
        "case_study": "/case-study-bks-pani-puri/",
        "related_blog": "/blog-strategy-from-scratch/"
    },
    "blog-local-business-launch": {
        "service": "/services/",
        "case_study": "/case-study-bks-pani-puri/",
        "related_blog": "/blog-local-seo-checklist/"
    },
    "blog-in-house-vs-agency": {
        "service": "/services/",
        "case_study": "/case-study-bks-pani-puri/",
        "related_blog": "/blog-strategy-from-scratch/"
    },
    "blog-google-ads-bidding": {
        "service": "/services/#ppc",
        "case_study": "/case-study-bks-pani-puri/",
        "related_blog": "/seo-vs-ppc-india/"
    },
    "blog-google-ai-overviews": {
        "service": "/aeo-services-india/",
        "case_study": "/case-study-parampara-farm/",
        "related_blog": "/blog-voice-search/"
    },
}

# Process each blog post
for blog_path, mapping in BLOG_CLUSTER_MAPPING.items():
    file_path = os.path.join(SITE_ROOT, blog_path, 'index.html')
    if not os.path.exists(file_path):
        print(f"Skipping {blog_path}: file not found")
        continue

    with open(file_path, 'r') as f:
        content = f.read()

    # Check if already added
    if 'Want to Learn More?' in content:
        print(f"Skipping {blog_path}: section already exists")
        continue

    # Find insertion point before </article>
    insert_pos = content.rfind('</article>')
    if insert_pos == -1:
        print(f"Skipping {blog_path}: no </article> found")
        continue

    service_url = mapping['service']
    case_study_url = mapping['case_study']
    related_blog_url = mapping['related_blog']

    # Generate HTML snippet
    learn_more_html = f'''\n\n          <div class="learn-more-section" style="background: var(--off-white); padding: 2.5rem; border-radius: var(--radius-md); margin-top: 4rem; border: 1px solid var(--grey-200);">
            <h3 style="margin-top: 0;">Want to Learn More?</h3>
            <p>Explore our services, read a case study, or dive deeper into related articles:</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1.5rem;">
              <a href="{service_url}" class="btn btn--primary" style="text-align: center; padding: 1rem; display: block;">Services</a>
              <a href="{case_study_url}" class="btn btn--secondary" style="text-align: center; padding: 1rem; display: block;">Case Study</a>
              <a href="{related_blog_url}" class="btn btn--secondary" style="text-align: center; padding: 1rem; display: block;">Related Article</a>
            </div>
          </div>'''

    # Insert before </article>
    new_content = content[:insert_pos] + learn_more_html + content[insert_pos:]

    with open(file_path, 'w') as f:
        f.write(new_content)

    print(f"Added learn-more section to {blog_path}")

print("Phase 2a complete: Added 'Want to Learn More?' to all GEO/SEO/AEO blog posts")
