#!/usr/bin/env python3
"""
HTML Scraper - Project Implementation

Extracts URLs, phone numbers, and email addresses from HTML files.
"""

import re
import sys
from urllib.parse import urljoin, urlparse


def extract_urls(html, base_url=None):
    """Extract all URLs from HTML."""
    urls = []
    
    # Pattern for href attributes
    href_pattern = r'href=["\']([^"\']+)["\']'
    href_matches = re.findall(href_pattern, html, re.IGNORECASE)
    
    # Pattern for src attributes
    src_pattern = r'src=["\']([^"\']+)["\']'
    src_matches = re.findall(src_pattern, html, re.IGNORECASE)
    
    # Combine and deduplicate
    all_urls = set(href_matches + src_matches)
    
    for url in all_urls:
        # Handle relative URLs
        if base_url and not url.startswith(('http://', 'https://', '//')):
            url = urljoin(base_url, url)
        urls.append(url)
    
    return sorted(set(urls))


def extract_phone_numbers(html):
    """Extract phone numbers from HTML."""
    phone_numbers = []
    
    # Pattern for various phone formats
    patterns = [
        r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',           # XXX-XXX-XXXX
        r'\(\d{3}\)\s*\d{3}[-.]?\d{4}',             # (XXX) XXX-XXXX
        r'\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}',  # International
        r'\b\d{10}\b',                               # XXXXXXXXXX
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, html)
        phone_numbers.extend(matches)
    
    # Remove duplicates and clean
    return sorted(set(phone_numbers))


def extract_emails(html):
    """Extract email addresses from HTML."""
    # Pattern for email addresses
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, html)
    
    # Remove duplicates
    return sorted(set(emails))


def scrape_html_file(filename, base_url=None):
    """Scrape HTML file and extract all data."""
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
    # Remove script and style content (they often contain false positives)
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    
    results = {
        'urls': extract_urls(html, base_url),
        'phone_numbers': extract_phone_numbers(html),
        'emails': extract_emails(html)
    }
    
    return results


def print_results(results):
    """Print extracted data in formatted way."""
    print("\n" + "="*60)
    print("EXTRACTED DATA")
    print("="*60)
    
    # URLs
    print(f"\n📎 URLs ({len(results['urls'])}):")
    if results['urls']:
        for url in results['urls']:
            print(f"  • {url}")
    else:
        print("  (none found)")
    
    # Phone Numbers
    print(f"\n📞 Phone Numbers ({len(results['phone_numbers'])}):")
    if results['phone_numbers']:
        for phone in results['phone_numbers']:
            print(f"  • {phone}")
    else:
        print("  (none found)")
    
    # Emails
    print(f"\n📧 Email Addresses ({len(results['emails'])}):")
    if results['emails']:
        for email in results['emails']:
            print(f"  • {email}")
    else:
        print("  (none found)")
    
    print("\n" + "="*60)


def save_results(results, output_file):
    """Save results to a text file."""
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("EXTRACTED DATA\n")
            f.write("="*60 + "\n\n")
            
            f.write(f"URLs ({len(results['urls'])}):\n")
            for url in results['urls']:
                f.write(f"  • {url}\n")
            f.write("\n")
            
            f.write(f"Phone Numbers ({len(results['phone_numbers'])}):\n")
            for phone in results['phone_numbers']:
                f.write(f"  • {phone}\n")
            f.write("\n")
            
            f.write(f"Email Addresses ({len(results['emails'])}):\n")
            for email in results['emails']:
                f.write(f"  • {email}\n")
        
        print(f"\n✓ Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving results: {e}")


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python html_scraper.py <html_file> [base_url] [output.txt]")
        sys.exit(1)
    
    html_file = sys.argv[1]
    base_url = sys.argv[2] if len(sys.argv) > 2 else None
    output_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    print(f"Scraping HTML file: {html_file}")
    results = scrape_html_file(html_file, base_url)
    
    if results:
        print_results(results)
        if output_file:
            save_results(results, output_file)


if __name__ == "__main__":
    main()

