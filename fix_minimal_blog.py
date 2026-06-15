#!/usr/bin/env python3
"""
Apply standard template to the minimal blog/best-digital-marketing-agency-india.html page.
"""
import os

SITE_ROOT = os.path.expanduser("~/clients/kalindi-marketing/Kalindi-Site")
file_path = os.path.join(SITE_ROOT, 'blog/best-digital-marketing-agency-india.html')

with open(file_path, 'r') as f:
    content = f.read()

# This page has minimal structure. We need to add:
# 1. Link to styles/main.css
# 2. Navbar after <body>
# 3. Proper footer before </body>
# 4. Scripts before </body>

# Check what's already there
print("Current head section:")
print(content[:500])

# The page already has styles in <style> tags - we need to add external CSS links
# Add CSS links after the internal <style> block if present, or after the last meta tag

# For now, let's use the standard template approach:
# Read the standard template from index.html and adapt it

# Actually, the simplest approach: convert this to use the directory structure
# Create blog/best-digital-marketing-agency-india/index.html from the root version
# and delete the .html file, or just add the missing template elements to the existing file

# Let's add the missing elements to the existing file

# 1. Add CSS links after <noscript> or at end of head
# 2. Add navbar after <body> 
# 3. Add footer + scripts before </body>

# Current structure analysis
import re

# Find head end
head_end = content.find('</head>')
if head_end == -1:
    print("No </head> found!")
    
# Find body start
body_start = content.find('<body>')
if body_start == -1:
    print("No <body> found!")

# Find body end
body_end = content.find('</body>')

print(f"head_end: {head_end}")
print(f"body_start: {body_start}")
print(f"body_end: {body_end}")

# Check for existing CSS links
if 'styles/main.css' in content:
    print("Has main.css")
else:
    print("MISSING main.css")

# Check for navbar
if 'class="navbar"' in content:
    print("Has navbar")
else:
    print("MISSING navbar")

# Check for footer
if '</footer>' in content:
    print("Has footer")
else:
    print("MISSING footer")

# Check for main.js
if 'main.js' in content:
    print("Has main.js")
else:
    print("MISSING main.js")

# Check for back-to-top
if 'back-to-top' in content:
    print("Has back-to-top")
else:
    print("MISSING back-to-top")
