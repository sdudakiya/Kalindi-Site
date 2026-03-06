import os
import re

base_dir = '/Users/chakshu/Desktop/Kalindi-Site'
animations_css = os.path.join(base_dir, 'styles', 'animations.css')

with open(animations_css, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace any non-performant top/left/bottom/right animations with transforms if they exist.
# Usually floats mutate translateY. Looking at the CSS previously, the animations look pretty clean, using transform and opacity.
# The only issue might be `background-position` in shimmer, which isn't fully hardware accelerated, but it's acceptable for small areas. Let's make sure `box-shadow` is optimized or leave it if it's the only way. The float animation uses translateY which is good.

all_html_files = []
for root, dirs, files in os.walk(base_dir):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            all_html_files.append(os.path.join(root, file))

for path in all_html_files:
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Add defer to scripts/main.js
    content = re.sub(r'<script src="/scripts/main\.js"></script>', r'<script src="/scripts/main.js" defer></script>', content)
    
    # Preload main fonts if not already
    preload_fonts = '<link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" as="style" onload="this.onload=null;this.rel=\'stylesheet\'" />\n    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" /></noscript>'
    
    # This is a bit complex to regex reliably if it's imported in CSS, let's actually remove the @import from CSS and put it in HTML
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Added defer to main.js across all HTML files.")

# Update main.css to remove @import and recommend font-display: swap (which is already there in the Google fonts URL)
main_css = os.path.join(base_dir, 'styles', 'main.css')
with open(main_css, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = re.sub(r"@import url\('https://fonts\.googleapis\.com[^']+'\);", "", css_content)

with open(main_css, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Removed @import from main.css")
