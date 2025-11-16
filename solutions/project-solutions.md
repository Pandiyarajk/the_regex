# Project Solutions

Complete solutions and code for real-world projects.

## Project 1: Email Validator CLI

See complete implementation in:
- `04-real-world-projects/project-email-validator.md`

### Key Regex Pattern

```python
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

### Testing Examples

```python
# Valid
"user@example.com"
"john.doe@company.co.uk"
"user+tag@example.org"

# Invalid
"invalid.email"
"@example.com"
"user@.com"
```

---

## Project 2: Log File Parser

See complete implementation in:
- `04-real-world-projects/project-log-parser.md`

### Key Regex Pattern

```python
pattern = r'(\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+\[([^\]]+)\]\s+"(\w+)\s+([^\s]+)\s+([^"]+)"\s+(\d+)\s+(\d+|-)'
```

### Sample Log Entry

```
127.0.0.1 - - [25/Dec/2023:10:30:45 +0000] "GET /page HTTP/1.1" 200 1234
```

### Extracted Fields

- IP: `127.0.0.1`
- Timestamp: `25/Dec/2023:10:30:45 +0000`
- Method: `GET`
- Path: `/page`
- Protocol: `HTTP/1.1`
- Status: `200`
- Size: `1234`

---

## Project 3: HTML Scraper

See complete implementation in:
- `04-real-world-projects/project-scrape-html.md`

### Key Regex Patterns

**URLs:**
```python
href_pattern = r'href=["\']([^"\']+)["\']'
src_pattern = r'src=["\']([^"\']+)["\']'
```

**Phone Numbers:**
```python
patterns = [
    r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
    r'\(\d{3}\)\s*\d{3}[-.]?\d{4}',
    r'\+\d{1,3}[-.\s]?\d{1,4}[-.\s]?\d{1,4}[-.\s]?\d{1,9}',
]
```

**Emails:**
```python
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
```

---

## Project 4: Form Validator (JavaScript)

### Implementation Example

```javascript
function validateForm(formData) {
    const errors = {};
    
    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(formData.email)) {
        errors.email = "Invalid email format";
    }
    
    // Phone validation (XXX-XXX-XXXX)
    const phonePattern = /^\d{3}-\d{3}-\d{4}$/;
    if (!phonePattern.test(formData.phone)) {
        errors.phone = "Phone must be in format XXX-XXX-XXXX";
    }
    
    // Password validation
    const passwordPattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/;
    if (!passwordPattern.test(formData.password)) {
        errors.password = "Password must be 8+ chars with uppercase, lowercase, and digit";
    }
    
    // PIN validation (4 or 6 digits)
    const pinPattern = /^(\d{4}|\d{6})$/;
    if (!pinPattern.test(formData.pin)) {
        errors.pin = "PIN must be 4 or 6 digits";
    }
    
    return errors;
}
```

---

## Project 5: Regex Search Tool

### Python Implementation

```python
#!/usr/bin/env python3
import re
import sys
import argparse

def search_in_file(filename, pattern, flags=0):
    """Search for pattern in file."""
    try:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, 1):
                if re.search(pattern, line, flags):
                    print(f"{filename}:{line_num}: {line.rstrip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description='Regex search tool')
    parser.add_argument('pattern', help='Regex pattern')
    parser.add_argument('files', nargs='+', help='Files to search')
    parser.add_argument('-i', '--ignore-case', action='store_true', help='Case-insensitive')
    parser.add_argument('-m', '--multiline', action='store_true', help='Multiline mode')
    
    args = parser.parse_args()
    
    flags = 0
    if args.ignore_case:
        flags |= re.IGNORECASE
    if args.multiline:
        flags |= re.MULTILINE
    
    try:
        pattern = re.compile(args.pattern, flags)
    except re.error as e:
        print(f"Invalid regex pattern: {e}")
        sys.exit(1)
    
    for filename in args.files:
        search_in_file(filename, pattern, flags)

if __name__ == "__main__":
    main()
```

### Usage

```bash
python regex_search.py "pattern" file1.txt file2.txt
python regex_search.py -i "hello" *.txt
python regex_search.py -m "^Error" logs/*.log
```

---

## Common Patterns Reference

### Email Validation
```python
r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
```

### Phone Number (US Format)
```python
r'^\d{3}-\d{3}-\d{4}$'
```

### URL Extraction
```python
r'https?://[^\s]+'
```

### Date (DD/MM/YYYY)
```python
r'(\d{2})/(\d{2})/(\d{4})'
```

### Strong Password
```python
r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$'
```

### IP Address
```python
r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
```

### Credit Card (Simplified)
```python
r'\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}'
```

---

## Testing Your Solutions

### Python Testing

```python
import re
import unittest

class TestRegexPatterns(unittest.TestCase):
    def test_email(self):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        self.assertTrue(re.match(pattern, "user@example.com"))
        self.assertFalse(re.match(pattern, "invalid.email"))
    
    def test_phone(self):
        pattern = r'^\d{3}-\d{3}-\d{4}$'
        self.assertTrue(re.match(pattern, "123-456-7890"))
        self.assertFalse(re.match(pattern, "1234567890"))

if __name__ == '__main__':
    unittest.main()
```

### JavaScript Testing

```javascript
// Using Jest or similar
describe('Regex Patterns', () => {
    test('email validation', () => {
        const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        expect(pattern.test("user@example.com")).toBe(true);
        expect(pattern.test("invalid.email")).toBe(false);
    });
    
    test('phone validation', () => {
        const pattern = /^\d{3}-\d{3}-\d{4}$/;
        expect(pattern.test("123-456-7890")).toBe(true);
        expect(pattern.test("1234567890")).toBe(false);
    });
});
```

---

## Best Practices

1. **Always test your patterns** with various inputs
2. **Use raw strings** in Python (`r''`)
3. **Escape special characters** when needed
4. **Consider performance** for large texts
5. **Document complex patterns** with comments
6. **Handle edge cases** - empty strings, null values
7. **Use appropriate functions** - `match()` vs `search()` vs `findall()`

---

**Congratulations!** You've completed all projects. Keep practicing and building!

