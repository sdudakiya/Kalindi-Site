#!/usr/bin/env python3
"""
Add contextual in-content links across all pages.
Matches key phrases and wraps them in links to relevant pages.
"""
import os
import re

SITE_ROOT = os.path.expanduser("~/clients/kalindi-marketing/Kalindi-Site")

# Anchor text patterns → target URL
# Format: (regex_pattern, replacement_url, max_links_per_page)
ANCHOR_RULES = [
    # High-priority conversion pages
    (r'\b(GEO services?|generative engine optimization)\b', '/geo-services-india/', 2),
    (r'\b(AEO services?|answer engine optimization)\b', '/aeo-services-india/', 2),
    (r'\b(SEO services?|search engine optimization)\b', '/services/', 2),
    (r'\b(SEO cost|SEO pricing)\b', '/seo-cost-india-2026/', 1),
    (r'\b(contact us|free audit|get.*audit)\b', '/contact/', 2),
    (r'\bour services?\b', '/services/', 1),

    # Case studies
    (r'\b(Parampara\.farm)\b', '/case-study-parampara-farm/', 1),
    (r"\b(BK'?s? Pani Puri)\b", '/case-study-bks-pani-puri/', 1),
    (r'\bcase stud(y|ies)\b', '/case-study-parampara-farm/', 1),

    # GEO/AI cluster
    (r'\b(AI search|AI optimization)\b', '/ai-search-optimization/', 1),
    (r'\b(LLM optimization)\b', '/llm-optimization/', 1),
    (r'\b(ChatGPT SEO)\b', '/chatgpt-seo/', 1),
    (r'\b(AI visibility)\b', '/ai-visibility-optimization/', 1),
    (r'\b(agentic digital marketing)\b', '/agentic-digital-marketing/', 1),
    (r'\b(AI marketing automation)\b', '/ai-marketing-automation-india/', 1),

    # SEO cluster blog posts
    (r'\b(technical SEO)\b', '/blog-technical-seo/', 1),
    (r'\b(link building)\b', '/blog-link-building/', 1),
    (r'\b(E-E-A-T)\b', '/blog-eeat-llms/', 1),
    (r'\b(voice search)\b', '/blog-voice-search/', 1),
    (r'\b(local SEO)\b', '/blog-local-seo-checklist/', 1),
    (r'\b(digital marketing strategy)\b', '/blog-strategy-from-scratch/', 1),
    (r'\b(in-house vs agency)\b', '/blog-in-house-vs-agency/', 1),
    (r'\b(Google AI Overviews?)\b', '/blog-google-ai-overviews/', 1),
    (r'\b(SEO vs AEO vs GEO)\b', '/blog-seo-vs-aeo-vs-geo/', 1),
    (r'\b(local business launch)\b', '/blog-local-business-launch/', 1),
    (r'\b(LinkedIn B2B)\b', '/blog-linkedin-b2b/', 1),
    (r'\b(SEO trends)\b', '/seo-trends-india-2026/', 1),
    (r'\b(SEO for (SaaS|ecommerce|food brands?))\b', '/seo-for-\\1-india/', 1),
]

# Pages to skip (already processed or special)
SKIP_PAGES = {
    'index.html',
    'add_breadcrumbs.py',
    'add_learn_more.py',
    'add_results_section.py',
    'add_related_services.py',
}

def get_all_html_files():
    files = []
    for root, dirs, fnames in os.walk(SITE_ROOT):
        for f in fnames:
            if f.endswith('.html'):
                rel = os.path.relpath(os.path.join(root, f), SITE_ROOT)
                if rel not in SKIP_PAGES:
                    files.append(rel)
    return files

def add_contextual_links(content, page_path):
    """Add contextual links to body content only."""
    added_count = 0
    modified = content

    for pattern, url, max_links in ANCHOR_RULES:
        # Only add if target URL isn't the current page
        if page_path.endswith(url.rstrip('/') + '/index.html') or page_path == url.rstrip('/') + '.html':
            continue

        # Skip if this link already exists in content
        if f'href="{url}"' in content or f"href='{url}'" in content:
            continue

        # Find matches in body content only (between <main> and </main> or <article> and </article>)
        # For simplicity, just search the whole content but avoid replacing inside tags
        matches = list(re.finditer(pattern, modified, re.IGNORECASE))
        count = 0

        for match in reversed(matches):  # Process in reverse to maintain positions
            if count >= max_links:
                break

            start, end = match.span()
            matched_text = match.group()

            # Check if this text is already inside an <a> tag
            # Look backward for unclosed <a
            before = modified[max(0, start-50):start]
            after = modified[end:end+50]
            if 'href=' in before and '</a>' not in before:
                continue  # Already inside a link
            if '<a ' in after and 'href=' in after[:20]:
                continue  # Next is a link

            # Wrap in anchor
            replacement = f'<a href="{url}" style="color: var(--primary); text-decoration: underline;">{matched_text}</a>'
            modified = modified[:start] + replacement + modified[end:]
            added_count += 1
            count += 1

    return modified, added_count

# Process all files
all_files = get_all_html_files()
total_links = 0

for rel_path in all_files:
    file_path = os.path.join(SITE_ROOT, rel_path)
    try:
        with open(file_path, 'r') as f:
            content = f.read()

        new_content, added = add_contextual_links(content, rel_path)
        if added > 0:
            with open(file_path, 'w') as f:
                f.write(new_content)
            total_links += added
            print(f"Added {added} contextual links to {rel_path}")

    except Exception as e:
        print(f"Error processing {rel_path}: {e}")

print(f"\nTotal contextual links added: {total_links}")
