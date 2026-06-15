#!/usr/bin/env python3
"""
Replace minimal footer with standard footer__grid on 8 GEO/AI service pages.
"""
import os
import re

SITE_ROOT = os.path.expanduser("~/clients/kalindi-marketing/Kalindi-Site")

PAGES_TO_FIX = [
    "ai-search-optimization",
    "aeo-services-india", 
    "agentic-digital-marketing",
    "chatgpt-seo",
    "geo-services-india",
    "ai-marketing-automation-india",
    "llm-optimization",
    "ai-visibility-optimization",
]

STANDARD_FOOTER = '''    <footer class="footer">
        <div class="container">
            <div class="footer__grid">
                <div class="footer__brand">
                    <img src="/assets/logo.webp" style="height:48px;margin-bottom:1rem;" alt="Kalindi Marketing" width="160" height="160" loading="lazy">
                    <p>India's premier agency for SEO, AEO, GEO, and digital marketing.</p>
                    <div class="footer__socials">
                        <a href="https://www.linkedin.com/company/kalindimarketing" class="social-icon" aria-label="LinkedIn" target="_blank" rel="noopener">in</a>
                        <a href="https://www.instagram.com/kalindimarketing" class="social-icon" aria-label="Instagram" target="_blank" rel="noopener">&#9638;</a>
                    </div>
                </div>
                <div class="footer__col">
                    <h4>Services</h4>
                    <ul class="footer__links">
                        <li><a href="/services/#seo">SEO</a></li>
                        <li><a href="/services/#aeo">AEO</a></li>
                        <li><a href="/services/#geo">GEO</a></li>
                        <li><a href="/services/#social">Social Media</a></li>
                        <li><a href="/services/#ppc">PPC</a></li>
                        <li><a href="/services/#content">Content Marketing</a></li>
                    </ul>
                </div>
                <div class="footer__col">
                    <h4>Company</h4>
                    <ul class="footer__links">
                        <li><a href="/about/">About Us</a></li>
                        <li><a href="/case-study-parampara-farm/">Parampara.farm Case Study</a></li>
                        <li><a href="/case-study-bks-pani-puri/">BK's Pani Puri Case Study</a></li>
                        <li><a href="/blog/">Blog &amp; Resources</a></li>
                        <li><a href="/contact/">Contact</a></li>
                    </ul>
                </div>
                <div class="footer__col">
                    <h4>Get in Touch</h4>
                    <ul class="footer__links">
                        <li><a href="mailto:hello@kalindimarketing.com">hello@kalindimarketing.com</a></li>
                        <li><a href="tel:+918****2856">+91-8160342856</a></li>
                        <li><a href="/contact/">Book a Free Call</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer__bottom">
                <p>&copy; 2026 Kalindi Marketing. All rights reserved.</p>
                <div class="footer__bottom-links">
                    <a href="/privacy-policy/">Privacy Policy</a>
                    <a href="/terms/">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>'''

for page in PAGES_TO_FIX:
    file_path = os.path.join(SITE_ROOT, page, 'index.html')
    if not os.path.exists(file_path):
        print(f"Skipping {page}: file not found")
        continue

    with open(file_path, 'r') as f:
        content = f.read()

    # Find and replace minimal footer with standard footer
    minimal_footer = '<footer class="footer">\n    <div class="container">\n      <div class="footer__bottom">\n        <p>&copy; 2026 Kalindi Marketing. All rights reserved.</p>\n        <div class="footer__bottom-links"><a href="/privacy-policy/">Privacy Policy</a><a href="/terms/">Terms</a></div>\n      </div>\n    </div>\n  </footer>'

    if minimal_footer in content:
        new_content = content.replace(minimal_footer, STANDARD_FOOTER)
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Fixed footer: {page}")
    else:
        print(f"Pattern not found: {page}")

print("Done")
