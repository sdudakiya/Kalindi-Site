#!/usr/bin/env python3
"""
Add 'Related Articles' sections to blog posts within the same cluster.
"""
import os

SITE_ROOT = os.path.expanduser("~/clients/kalindi-marketing/Kalindi-Site")

BLOG_CLUSTERS = {
    "GEO": [
        "blog-geo-guide",
        "state-of-geo-india-2026",
        "geo-vs-seo-india",
        "top-geo-agencies-india-2026",
        "ai-search-optimization",
        "llm-optimization",
        "chatgpt-seo",
        "ai-visibility-optimization",
        "agentic-digital-marketing",
        "ai-marketing-automation-india",
    ],
    "SEO": [
        "blog-technical-seo",
        "blog-link-building",
        "blog-eeat-llms",
        "blog-voice-search",
        "blog-seo-vs-aeo-vs-geo",
        "blog-strategy-from-scratch",
        "blog-local-seo-checklist",
        "blog-linkedin-b2b",
        "blog-local-business-launch",
        "blog-in-house-vs-agency",
        "blog-google-ads-bidding",
        "blog-google-ai-overviews",
    ],
}

for cluster_name, blog_paths in BLOG_CLUSTERS.items():
    for blog_path in blog_paths:
        file_path = os.path.join(SITE_ROOT, blog_path + '/index.html')
        if not os.path.exists(file_path):
            print(f"Skipping {blog_path}: file not found")
            continue

        with open(file_path, 'r') as f:
            content = f.read()

        if 'Related Articles' in content:
            print(f"Skipping {blog_path}: section already exists")
            continue

        other_blogs = [b for b in blog_paths if b != blog_path]
        selected = other_blogs[:3]

        link_lines = []
        for sb in selected:
            title = sb.replace('-', ' ').title()
            link_lines.append(f'<a href="/{sb}/" style="color: var(--primary); text-decoration: underline;">{title}</a>')

        related_section = "\n\n          <div class=\"related-articles-section\" style=\"background: var(--off-white); padding: 2.5rem; border-radius: var(--radius-md); margin-top: 4rem; border: 1px solid var(--grey-200);\">\n            <h3 style=\"margin-top: 0;\">Related Articles</h3>\n            <div style=\"display: flex; flex-direction: column; gap: 1rem;\">\n              " + "\n              ".join(link_lines) + "\n            </div>\n          </div>"

        insert_pos = content.rfind('</main>')
        if insert_pos == -1:
            print(f"Skipping {blog_path}: no </main> found")
            continue

        new_content = content[:insert_pos] + related_section + content[insert_pos:]

        with open(file_path, 'w') as f:
            f.write(new_content)

        print(f"Added related articles to {blog_path}")

print("Phase 4 complete: Added cluster interlinking for blog posts")
