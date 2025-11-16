# Project: Web Scraping Lite

Extract URLs, phone numbers, and email addresses from HTML files using regex.

## Project Overview

Create a tool that:
- Reads HTML files
- Extracts URLs, phone numbers, and email addresses
- Outputs results in organized format
- Supports both Python and JavaScript

## Implementation

### Python Version

**File: `html_scraper.py`**

```python
#!/usr/bin/env python3
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
```

### JavaScript Version

**File: `html_scraper.js`**

```javascript
#!/usr/bin/env node
const fs = require('fs');
const { URL } = require('url');

function extractUrls(html, baseUrl = null) {
    const urls = new Set();
    
    // Pattern for href attributes
    const hrefPattern = /href=["']([^"']+)["']/gi;
    let match;
    while ((match = hrefPattern.exec(html)) !== null) {
        urls.add(match[1]);
    }
    
    // Pattern for src attributes
    const srcPattern = /src=["']([^"']+)["']/gi;
    while ((match = srcPattern.exec(html)) !== null) {
        urls.add(match[1]);
    }
    
    // Handle relative URLs
    const processedUrls = Array.from(urls).map(url => {
        if (baseUrl && !url.match(/^(https?:|\/\/)/)) {
            try {
                return new URL(url, baseUrl).href;
            } catch (e) {
                return url;
            }
        }
        return url;
    });
    
    return processedUrls.sort();
}

function extractPhoneNumbers(html) {
    const phoneNumbers = new Set();
    
    // Patterns for various phone formats
    const patterns = [
        /\b\d{3}[-.]?\d{3}[-.]?\d{4}\b/g,                    // XXX-XXX-XXXX
        /\(\d{3}\)\s*\d{3}[-.]?\d{4}/g,                       // (XXX) XXX-XXXX
        /\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}/g, // International
        /\b\d{10}\b/g,                                         // XXXXXXXXXX
    ];
    
    patterns.forEach(pattern => {
        let match;
        while ((match = pattern.exec(html)) !== null) {
            phoneNumbers.add(match[0]);
        }
    });
    
    return Array.from(phoneNumbers).sort();
}

function extractEmails(html) {
    const pattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g;
    const emails = new Set();
    let match;
    
    while ((match = pattern.exec(html)) !== null) {
        emails.add(match[0]);
    }
    
    return Array.from(emails).sort();
}

function scrapeHtmlFile(filename, baseUrl = null) {
    let html;
    
    try {
        html = fs.readFileSync(filename, 'utf-8');
    } catch (error) {
        console.error(`Error reading file: ${error.message}`);
        return null;
    }
    
    // Remove script and style content
    html = html.replace(/<script[^>]*>[\s\S]*?<\/script>/gi, '');
    html = html.replace(/<style[^>]*>[\s\S]*?<\/style>/gi, '');
    
    return {
        urls: extractUrls(html, baseUrl),
        phoneNumbers: extractPhoneNumbers(html),
        emails: extractEmails(html)
    };
}

function printResults(results) {
    console.log('\n' + '='.repeat(60));
    console.log("EXTRACTED DATA");
    console.log('='.repeat(60));
    
    // URLs
    console.log(`\n📎 URLs (${results.urls.length}):`);
    if (results.urls.length > 0) {
        results.urls.forEach(url => console.log(`  • ${url}`));
    } else {
        console.log("  (none found)");
    }
    
    // Phone Numbers
    console.log(`\n📞 Phone Numbers (${results.phoneNumbers.length}):`);
    if (results.phoneNumbers.length > 0) {
        results.phoneNumbers.forEach(phone => console.log(`  • ${phone}`));
    } else {
        console.log("  (none found)");
    }
    
    // Emails
    console.log(`\n📧 Email Addresses (${results.emails.length}):`);
    if (results.emails.length > 0) {
        results.emails.forEach(email => console.log(`  • ${email}`));
    } else {
        console.log("  (none found)");
    }
    
    console.log('\n' + '='.repeat(60));
}

function saveResults(results, outputFile) {
    let content = "EXTRACTED DATA\n";
    content += '='.repeat(60) + "\n\n";
    
    content += `URLs (${results.urls.length}):\n`;
    results.urls.forEach(url => content += `  • ${url}\n`);
    content += "\n";
    
    content += `Phone Numbers (${results.phoneNumbers.length}):\n`;
    results.phoneNumbers.forEach(phone => content += `  • ${phone}\n`);
    content += "\n";
    
    content += `Email Addresses (${results.emails.length}):\n`;
    results.emails.forEach(email => content += `  • ${email}\n`);
    
    try {
        fs.writeFileSync(outputFile, content, 'utf-8');
        console.log(`\n✓ Results saved to ${outputFile}`);
    } catch (error) {
        console.error(`Error saving results: ${error.message}`);
    }
}

function main() {
    const args = process.argv.slice(2);
    
    if (args.length < 1) {
        console.log("Usage: node html_scraper.js <html_file> [base_url] [output.txt]");
        process.exit(1);
    }
    
    const htmlFile = args[0];
    const baseUrl = args[1] || null;
    const outputFile = args[2] || null;
    
    console.log(`Scraping HTML file: ${htmlFile}`);
    const results = scrapeHtmlFile(htmlFile, baseUrl);
    
    if (results) {
        printResults(results);
        if (outputFile) {
            saveResults(results, outputFile);
        }
    }
}

if (require.main === module) {
    main();
}
```

## Sample HTML File

Create `sample.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Information</h1>
    <p>Email: contact@example.com</p>
    <p>Phone: (555) 123-4567</p>
    <p>Alternative: 555-987-6543</p>
    <a href="https://www.example.com">Home</a>
    <a href="/about">About</a>
    <img src="/images/logo.png" alt="Logo">
</body>
</html>
```

## Usage

### Python

```bash
python html_scraper.py sample.html
python html_scraper.py sample.html https://example.com output.txt
```

### JavaScript

```bash
node html_scraper.js sample.html
node html_scraper.js sample.html https://example.com output.txt
```

## Extensions

1. **Extract more data types**
   - Social media links
   - Images and media files
   - Metadata (title, description)

2. **Better URL handling**
   - Validate URLs
   - Filter by domain
   - Handle different URL schemes

3. **Export formats**
   - JSON output
   - CSV export
   - Database storage

## Key Learning Points

- Extracting multiple patterns from text
- Handling HTML content
- URL normalization
- Pattern matching for various formats
- File I/O operations

---

**Next:** [project-regex-in-python.md](project-regex-in-python.md) or [project-regex-in-js.md](project-regex-in-js.md)

