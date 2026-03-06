import os
import re

base_dir = '/Users/chakshu/Desktop/Kalindi-Site'

all_html_files = []
for root, dirs, files in os.walk(base_dir):
    if 'node_modules' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            all_html_files.append(os.path.join(root, file))

font_link = '<link rel="preload" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" as="style" onload="this.onload=null;this.rel=\'stylesheet\'" />\n    <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" /></noscript>'

for path in all_html_files:
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if "fonts.googleapis.com" not in content:
        content = re.sub(r'</title>', f'</title>\n    {font_link}', content)
        
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Injected Google Fonts preloads into all HTML files.")
