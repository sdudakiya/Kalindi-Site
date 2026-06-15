#!/usr/bin/env python3
"""
Add 'Related Services' sections to case study pages.
"""
import os

SITE_ROOT = os.path.expanduser("~/clients/kalindi-marketing/Kalindi-Site")

CASE_STUDIES = {
    "case-study-bks-pani-puri": [
        ("/services/", "SEO Services"),
        ("/geo-services-india/", "GEO Services"),
        ("/services/#seo", "Local SEO"),
    ],
    "case-study-parampara-farm": [
        ("/services/", "SEO Services"),
        ("/geo-services-india/", "GEO Services"),
        ("/services/#content", "Content Marketing"),
    ],
    "case-studies/bks-pani-puri-local-seo": [
        ("/services/", "SEO Services"),
        ("/geo-services-india/", "GEO Services"),
        ("/services/#seo", "Local SEO"),
    ],
    "case-studies/parampara-farm-seo-success": [
        ("/services/", "SEO Services"),
        ("/geo-services-india/", "GEO Services"),
        ("/services/#content", "Content Marketing"),
    ],
}

for case_path, services in CASE_STUDIES.items():
    file_path = os.path.join(SITE_ROOT, case_path, 'index.html')
    if not os.path.exists(file_path):
        print(f"Skipping {case_path}: file not found")
        continue

    with open(file_path, 'r') as f:
        content = f.read()

    if 'Related Services' in content:
        print(f"Skipping {case_path}: section already exists")
        continue

    links = []
    for url, name in services:
        links.append(f'<a href="{url}" class="btn btn--primary" style="margin: 0.5rem; padding: 0.75rem 1.5rem; display: inline-block;">{name}</a>')
    service_links = ''.join(links)

    related_section = f'''\n\n          <div class="related-services-section" style="background: var(--off-white); padding: 2.5rem; border-radius: var(--radius-md); margin-top: 4rem; border: 1px solid var(--grey-200);">
            <h2 style="margin-top: 0;">Related Services</h2>
            <p>The services that powered these results:</p>
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
              {service_links}
            </div>
          </div>'''

    insert_pos = content.rfind('</main>')
    if insert_pos == -1:
        print(f"Skipping {case_path}: no </main> found")
        continue

    new_content = content[:insert_pos] + related_section + content[insert_pos:]

    with open(file_path, 'w') as f:
        f.write(new_content)

    print(f"Added related services section to {case_path}")

print("Phase 2c complete: Added 'Related Services' to case studies")
