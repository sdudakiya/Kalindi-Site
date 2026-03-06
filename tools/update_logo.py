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

for path in all_html_files:
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the logo file extension from .png to .webp
    content = re.sub(r'logo\.png', r'logo.webp', content)
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Updated {len(all_html_files)} files with new logo.webp path")
