#!/usr/bin/env python3
"""
Add 'Results We've Delivered' sections to service pages.
"""
import os

SITE_ROOT = os.path.expanduser("~/clients/kalindi-marketing/Kalindi-Site")

SERVICE_PAGES = {
    "geo-services-india": ["/case-study-parampara-farm/"],
    "aeo-services-india": ["/case-study-parampara-farm/"],
    "services": ["/case-study-parampara-farm/", "/case-study-bks-pani-puri/"],
    "ai-search-optimization": ["/case-study-parampara-farm/"],
    "llm-optimization": ["/case-study-parampara-farm/"],
    "chatgpt-seo": ["/case-study-parampara-farm/"],
    "ai-visibility-optimization": ["/case-study-parampara-farm/"],
    "agentic-digital-marketing": ["/case-study-parampara-farm/"],
    "ai-marketing-automation-india": ["/case-study-parampara-farm/"],
}

for service_path, case_studies in SERVICE_PAGES.items():
    file_path = os.path.join(SITE_ROOT, service_path, 'index.html')
    if not os.path.exists(file_path):
        print(f"Skipping {service_path}: file not found")
        continue

    with open(file_path, 'r') as f:
        content = f.read()

    if 'Results We' in content:
        print(f"Skipping {service_path}: section already exists")
        continue

    # Generate case study links
    links = []
    for cs in case_studies:
        name = cs.replace('/', '').replace('-', ' ').title()
        links.append(f'<a href="{cs}" class="btn btn--secondary" style="margin: 0.5rem; padding: 0.75rem 1.5rem; display: inline-block;">Case Study: {name}</a>')
    case_study_links = ''.join(links)

    results_section = f'''\n\n          <div class="results-section" style="background: var(--off-white); padding: 2.5rem; border-radius: var(--radius-md); margin-top: 4rem; border: 1px solid var(--grey-200);">
            <h2 style="margin-top: 0;">Results We've Delivered</h2>
            <p>See real outcomes from our clients:</p>
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;">
              {case_study_links}
            </div>
          </div>'''

    insert_pos = content.rfind('</main>')
    if insert_pos == -1:
        print(f"Skipping {service_path}: no </main> found")
        continue

    new_content = content[:insert_pos] + results_section + content[insert_pos:]

    with open(file_path, 'w') as f:
        f.write(new_content)

    print(f"Added results section to {service_path}")

print("Phase 2b complete: Added 'Results We've Delivered' to service pages")
