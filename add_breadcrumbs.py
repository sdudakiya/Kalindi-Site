#!/usr/bin/env python3
"""
Add visible breadcrumb HTML to all Kalindi Marketing site pages.
Only skips pages that already have visible breadcrumbs.
"""

import os
import re

SITE = os.path.expanduser("~/clients/kalindi-marketing/Kalindi-Site")

# Pages that already have visible breadcrumbs - SKIP
ALREADY_HAS = {
    "about/index.html",
    "blog/index.html", 
    "contact/index.html",
    "privacy-policy/index.html",
    "services/index.html",
    "terms/index.html",
}

# Page title mapping for breadcrumb text (short names)
PAGE_TITLES = {
    "index.html": None,  # homepage - no breadcrumb
    "aeo-services-india/index.html": "AEO Services India",
    "agentic-digital-marketing/index.html": "Agentic Digital Marketing",
    "ai-marketing-automation-india/index.html": "AI Marketing Automation",
    "ai-search-optimization/index.html": "AI Search Optimization",
    "ai-visibility-optimization/index.html": "AI Visibility Optimization",
    "best-digital-marketing-agency-india/index.html": "Best Digital Marketing Agency India",
    "blog-eeat-llms/index.html": "E-E-A-T in the Age of LLMs",
    "blog-geo-guide/index.html": "Complete Guide to GEO",
    "blog-google-ads-bidding/index.html": "Google Ads Smart Bidding",
    "blog-google-ai-overviews/index.html": "Google AI Overviews Playbook",
    "blog-in-house-vs-agency/index.html": "In-House vs Agency SEO",
    "blog-link-building/index.html": "Link Building 2026",
    "blog-linkedin-b2b/index.html": "LinkedIn B2B Content Strategy",
    "blog-local-business-launch/index.html": "Local Business Launch Guide",
    "blog-local-seo-checklist/index.html": "Local SEO Checklist",
    "blog-seo-vs-aeo-vs-geo/index.html": "SEO vs AEO vs GEO",
    "blog-strategy-from-scratch/index.html": "Digital Strategy from Scratch",
    "blog-technical-seo/index.html": "Technical SEO Checklist",
    "blog-voice-search/index.html": "Voice Search Optimization",
    "case-studies/bks-pani-puri-local-seo/index.html": "BK's Pani Puri Case Study (Dupe)",
    "case-studies/parampara-farm-seo-success/index.html": "Parampara.farm Case Study (Dupe)",
    "case-study-bks-pani-puri/index.html": "BK's Pani Puri Case Study",
    "case-study-parampara-farm/index.html": "Parampara.farm Case Study",
    "chatgpt-seo/index.html": "ChatGPT SEO Services",
    "digital-marketing-guide-india/index.html": "Digital Marketing Guide India",
    "geo-services-india/index.html": "GEO Services India",
    "geo-vs-seo-india/index.html": "GEO vs SEO India",
    "how-to-choose-seo-agency-india/index.html": "How to Choose SEO Agency India",
    "llm-optimization/index.html": "LLM Optimization Services",
    "seo-agency-vs-in-house-india/index.html": "SEO Agency vs In-House India",
    "seo-cost-india-2026/index.html": "SEO Cost India 2026",
    "seo-for-ecommerce-india/index.html": "SEO for E-Commerce India",
    "seo-for-food-brands-india/index.html": "SEO for Food Brands India",
    "seo-for-saas-india/index.html": "SEO for SaaS India",
    "seo-tools-templates-india/index.html": "SEO Tools & Templates India",
    "seo-trends-india-2026/index.html": "SEO Trends India 2026",
    "seo-vs-ppc-india/index.html": "SEO vs PPC India",
    "free-seo-audit-food-brands-india/index.html": "Free SEO + GEO Audit for Food Brands",
    "state-of-geo-india-2026/index.html": "State of GEO India 2026",
    "top-geo-agencies-india-2026/index.html": "Top GEO Agencies India 2026",
    "seo-for-restaurant-chains-india/index.html": "SEO for Restaurant Chains India",
    "seo-for-d2c-food-brands-india/index.html": "SEO for D2C Food Brands India",
    "seo-for-fmcg-brands-india/index.html": "SEO for FMCG Brands India",
    "geo-for-food-brands-india/index.html": "GEO for Food Brands India",
    "social-media-food-brands-india/index.html": "Social Media for Food Brands India",
    "content-marketing-food-brands-india/index.html": "Content Marketing for Food Brands India",
    "seo-for-beverage-brands-india/index.html": "SEO for Beverage Brands India",
    "digital-marketing-food-tech-india/index.html": "Digital Marketing for Food Tech India",
}

def make_breadcrumb(path_items, is_blog=False, is_service=False):
    """Generate breadcrumb HTML."""
    parts = []
    # Home link
    parts.append('<a href="/" style="color:rgba(255,255,255,0.7);text-decoration:none;">Home</a>')
    
    for item in path_items[:-1]:
        if isinstance(item, tuple):
            href, name = item
            parts.append(f'<span style="margin:0 0.35rem;">→</span>')
            parts.append(f'<a href="{href}" style="color:rgba(255,255,255,0.7);text-decoration:none;">{name}</a>')
        else:
            parts.append(f'<span style="margin:0 0.35rem;">→</span>')
            parts.append(f'<span style="color:white;">{item}</span>')
    
    # Last item
    parts.append(f'<span style="margin:0 0.35rem;">→</span>')
    parts.append(f'<span style="color:white;">{path_items[-1]}</span>')
    
    html = '<div class="breadcrumb" style="margin-bottom:1.5rem;font-size:0.85rem;color:rgba(255,255,255,0.7);">' + ''.join(parts) + '</div>'
    return html

def find_insertion_point(content, page_type):
    """Find where to insert breadcrumb based on page type."""
    if page_type == 'blog':
        # Blog posts: inside <header class="blog-header"> after <div class="container">
        # Look for the tag span line
        m = re.search(r'(<span class="blog-card__tag"[^>]*>)', content)
        if m:
            return m.start(1), 'before_tag'
        # Fallback: after container opening inside blog-header
        m = re.search(r'(<header class="blog-header">.*?<div class="container"[^>]*>)', content, re.DOTALL)
        if m:
            return m.end(1), 'after_container'
    
    elif page_type == 'service':
        # Service pages: inside <section class="X-hero"> after <div class="container">
        # Look for h1 or the tag/badge before h1
        patterns = [r'<h1[^>]*>', r'(<div[^>]*class="[^"]*badge[^"]*"[^>]*>)', r'(<div style="display:inline-flex[^>]*>)']
        for p in patterns:
            m = re.search(p, content)
            if m:
                return m.start(1 if '(' in p else 0), 'before_h1'
        # Fallback
        m = re.search(r'(<div class="container"[^>]*>)\s*\n', content)
        if m:
            return m.end(1), 'after_container'
    
    elif page_type == 'case_study':
        # Case studies: inside <section class="case-study-header"> after <div class="container">
        m = re.search(r'(<div class="container"[^>]*>)\s*\n\s*<h1', content)
        if m:
            return m.end(1), 'before_h1'
        m = re.search(r'(<div class="container"[^>]*>)', content)
        if m:
            return m.end(1), 'after_container'
    
    elif page_type == 'report':
        # Report pages: inside <section class="report-hero"> after <div class="container">
        patterns = [r'(<div style="display:inline-flex[^>]*>)', r'<h1[^>]*>']
        for p in patterns:
            m = re.search(p, content)
            if m:
                return m.start(1 if '(' in p else 0), 'before_element'
        m = re.search(r'(<div class="container"[^>]*>)', content)
        if m:
            return m.end(1), 'after_container'
    
    elif page_type == 'pricing':
        m = re.search(r'(<h1[^>]*>)', content)
        if m:
            return m.start(1), 'before_h1'
        m = re.search(r'(<div class="container"[^>]*>)', content)
        if m:
            return m.end(1), 'after_container'
    
    elif page_type == 'standard':
        # Standard content page
        m = re.search(r'(<div class="container"[^>]*>)\s*\n\s*<h1', content)
        if m:
            return m.end(1), 'before_h1'
        m = re.search(r'(<div class="container"[^>]*>)', content)
        if m:
            return m.end(1), 'after_container'
    
    elif page_type == 'legal':
        # Privacy policy, terms - already have breadcrumbs
        return None, None
    
    return None, None


def get_page_type(filename):
    """Determine page type based on filename and content."""
    base = os.path.basename(os.path.dirname(filename))
    name = os.path.basename(filename)
    
    if name == 'index.html':
        dirname = os.path.basename(os.path.dirname(filename))
        if not dirname or dirname == 'Kalindi-Site':
            return 'homepage'
    
    short = filename.replace(SITE + '/', '')
    
    if short in ALREADY_HAS:
        return 'skip'
    
    if 'case-studies' in short or 'case-study' in short:
        return 'case_study'
    
    if 'blog-' in short and 'blog/index' not in short:
        return 'blog'
    
    if 'privacy-policy' in short or 'terms' in short:
        return 'legal'
    
    if 'seo-cost' in short:
        return 'pricing'
    
    if 'state-of-geo' in short:
        return 'report'
    
    if short in PAGE_TITLES:
        return 'standard'
    
    return 'standard'


def get_breadcrumb_path(short_name):
    """Get the breadcrumb navigation path for a page."""
    title = PAGE_TITLES.get(short_name, short_name.replace('/index.html', '').replace('/', ' ').title())
    
    if short_name == 'index.html':
        return None  # Homepage
    
    if short_name.startswith('blog-') and short_name != 'blog/index.html':
        return make_breadcrumb(['Blog', title], is_blog=True)
    
    if 'case-studies/' in short_name or 'case-study' in short_name:
        return make_breadcrumb(['Case Studies', title])
    
    if short_name.startswith(('seo-', 'geo-', 'aeo-', 'ai-', 'agentic-', 'chatgpt-', 'llm-', 'digital-', 'how-to-', 'top-geo-')):
        return make_breadcrumb([('/services/', 'Services'), title], is_service=True)
    
    if short_name in ('best-digital-marketing-agency-india/index.html',):
        return make_breadcrumb(['Digital Marketing', title])
    
    return make_breadcrumb([title])


# Main loop
count_added = 0
count_skipped = 0
count_errors = 0

for root, dirs, files in os.walk(SITE):
    for fname in files:
        if not fname.endswith('.html'):
            continue
        
        fpath = os.path.join(root, fname)
        short = fpath.replace(SITE + '/', '')
        
        if short in ALREADY_HAS:
            # print(f"SKIP (has breadcrumb): {short}")
            count_skipped += 1
            continue
        
        if short == 'index.html':
            # Homepage - no breadcrumb
            count_skipped += 1
            continue
        
        page_type = get_page_type(fpath)
        if page_type == 'skip' or page_type == 'homepage':
            count_skipped += 1
            continue
        
        # Read file
        with open(fpath, 'r') as f:
            content = f.read()
        
        # Check if already has visible breadcrumb
        if 'class="breadcrumb"' in content:
            count_skipped += 1
            continue
        
        # Get the breadcrumb HTML
        bc_html = get_breadcrumb_path(short)
        if not bc_html:
            count_skipped += 1
            continue
        
        # Determine insertion point
        if page_type == 'blog':
            # Insert after <div class="container" ...> inside blog-header
            pattern = r'(<div class="container"[^>]*>\s*\n\s*)(<span class="blog-card__tag")'
            repl = rf'\1{bc_html}\n\n\2'
            new_content = re.sub(pattern, repl, content, count=1)
        
        elif page_type == 'case_study':
            # Insert after <div class="container"> inside case-study-header, before <h1>
            pattern = r'(<section class="case-study-header">.*?<div class="container"[^>]*>\s*\n\s*)(<h1)'
            repl = rf'\1{bc_html}\n\n\2'
            new_content = re.sub(pattern, repl, content, count=1, flags=re.DOTALL)
        
        elif page_type == 'report':
            # Insert after container in report-hero, before the badge div
            pattern = r'(<section class="report-hero">.*?<div class="container"[^>]*>\s*\n\s*)(<div style="display:inline-flex)'
            repl = rf'\1{bc_html}\n\n\2'
            new_content = re.sub(pattern, repl, content, count=1, flags=re.DOTALL)
        
        elif page_type == 'pricing':
            # Insert after container in pricing-hero, before h1
            pattern = r'(<section class="pricing-hero">.*?<div class="container"[^>]*>\s*\n\s*)(<h1)'
            repl = rf'\1{bc_html}\n\n\2'
            new_content = re.sub(pattern, repl, content, count=1, flags=re.DOTALL)
        
        elif page_type == 'standard':
            # Generic approach: find the first <div class="container"> after <main> or first <section class="*-hero">
            # Try to find a section with hero class, then container inside
            pattern = r'(<section class="[^"]*-hero[^"]*">.*?<div class="container"[^>]*>\s*\n\s*)(<h1|<div|<p[^>]*>)'
            m = re.search(pattern, content, re.DOTALL)
            if m:
                repl = rf'\1{bc_html}\n\n\2'
                new_content = re.sub(pattern, repl, content, count=1, flags=re.DOTALL)
            else:
                # Last resort: after first <div class="container"> in <main>
                pattern = r'(<main>.*?<div class="container"[^>]*>\s*\n\s*)(<h1|<div|<p[^>]*>)'
                m = re.search(pattern, content, re.DOTALL)
                if m:
                    repl = rf'\1{bc_html}\n\n\2'
                    new_content = re.sub(pattern, repl, content, count=1, flags=re.DOTALL)
                else:
                    # Try bare div class="container" anywhere
                    pattern = r'(<div class="container"[^>]*>\s*\n\s*)(<h1[^>]*>)'
                    new_content = re.sub(pattern, rf'\1{bc_html}\n\n\2', content, count=1)
        
        else:
            count_skipped += 1
            continue
        
        if new_content == content:
            print(f"WARN: No change in {short}")
            count_skipped += 1
            continue
        
        with open(fpath, 'w') as f:
            f.write(new_content)
        
        print(f"ADDED: {short} ({page_type})")
        count_added += 1

print(f"\nDone! Added breadcrumbs to {count_added} pages, skipped {count_skipped}, errors {count_errors}")
