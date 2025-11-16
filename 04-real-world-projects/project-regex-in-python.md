# Project: Regex in Python - Complete Guide

A comprehensive guide to using regex in Python with the `re` module, including common patterns and best practices.

## Python `re` Module Overview

The `re` module provides regex functionality in Python. Key functions:

- `re.search()` - Find first match
- `re.match()` - Match at start of string
- `re.findall()` - Find all matches
- `re.finditer()` - Iterator over matches
- `re.sub()` - Substitute matches
- `re.split()` - Split by pattern
- `re.compile()` - Compile pattern for reuse

## Common Patterns and Examples

### 1. Basic Matching

```python
import re

# Search for pattern
text = "Hello, my phone number is 123-456-7890"
pattern = r'\d{3}-\d{3}-\d{4}'
match = re.search(pattern, text)
if match:
    print(match.group())  # "123-456-7890"
```

### 2. Finding All Matches

```python
import re

text = "Contact: email1@example.com or email2@test.org"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(pattern, text)
print(emails)  # ['email1@example.com', 'email2@test.org']
```

### 3. Using Groups

```python
import re

text = "Date: 25/12/2023"
pattern = r'(\d{2})/(\d{2})/(\d{4})'
match = re.search(pattern, text)
if match:
    day = match.group(1)      # "25"
    month = match.group(2)     # "12"
    year = match.group(3)      # "2023"
    print(f"Day: {day}, Month: {month}, Year: {year}")
```

### 4. Named Groups

```python
import re

text = "Date: 25/12/2023"
pattern = r'(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})'
match = re.search(pattern, text)
if match:
    print(match.group('day'))    # "25"
    print(match.group('month'))   # "12"
    print(match.group('year'))   # "2023"
```

### 5. Substitution

```python
import re

text = "Phone: 123-456-7890"
pattern = r'\d{3}-\d{3}-\d{4}'
replacement = "XXX-XXX-XXXX"
result = re.sub(pattern, replacement, text)
print(result)  # "Phone: XXX-XXX-XXXX"
```

### 6. Using Compiled Patterns

```python
import re

# Compile pattern for reuse
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')

text1 = "Call 123-456-7890"
text2 = "Or 987-654-3210"

match1 = pattern.search(text1)
match2 = pattern.search(text2)

if match1:
    print(match1.group())
if match2:
    print(match2.group())
```

### 7. Flags

```python
import re

# Case-insensitive matching
text = "Hello HELLO hello"
pattern = r'hello'
matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)  # ['Hello', 'HELLO', 'hello']

# Multiline matching
text = "Line 1\nLine 2\nLine 3"
pattern = r'^Line'
matches = re.findall(pattern, text, re.MULTILINE)
print(matches)  # ['Line', 'Line', 'Line']

# Dot matches newline
text = "Start\nEnd"
pattern = r'Start.*End'
match = re.search(pattern, text, re.DOTALL)
if match:
    print(match.group())  # "Start\nEnd"
```

## Common Use Cases

### Email Validation

```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

emails = ["user@example.com", "invalid.email", "@example.com"]
for email in emails:
    print(f"{email}: {validate_email(email)}")
```

### Phone Number Extraction

```python
import re

def extract_phone_numbers(text):
    pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
    return re.findall(pattern, text)

text = "Call 123-456-7890 or 987.654.3210"
numbers = extract_phone_numbers(text)
print(numbers)  # ['123-456-7890', '987.654.3210']
```

### URL Extraction

```python
import re

def extract_urls(text):
    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)

text = "Visit https://example.com and http://test.org"
urls = extract_urls(text)
print(urls)  # ['https://example.com', 'http://test.org']
```

### Text Cleaning

```python
import re

def clean_text(text):
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters (keep letters, digits, spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.strip()

text = "Hello!!!   World@@@"
cleaned = clean_text(text)
print(cleaned)  # "Hello World"
```

### Log Parsing

```python
import re

def parse_log(log_line):
    pattern = r'(\d+\.\d+\.\d+\.\d+)\s+.*?\[([^\]]+)\]\s+"(\w+)\s+([^\s]+).*?"\s+(\d+)'
    match = re.match(pattern, log_line)
    if match:
        return {
            'ip': match.group(1),
            'timestamp': match.group(2),
            'method': match.group(3),
            'path': match.group(4),
            'status': match.group(5)
        }
    return None

log = '127.0.0.1 - - [25/Dec/2023:10:30:45] "GET /page HTTP/1.1" 200'
parsed = parse_log(log)
print(parsed)
```

## Best Practices

### 1. Use Raw Strings

Always use raw strings (`r''`) for regex patterns to avoid escaping issues:

```python
# Good
pattern = r'\d+'

# Avoid
pattern = '\\d+'  # Harder to read
```

### 2. Compile Patterns for Reuse

If using a pattern multiple times, compile it:

```python
# Good for multiple uses
pattern = re.compile(r'\d+')
matches1 = pattern.findall(text1)
matches2 = pattern.findall(text2)

# Fine for single use
matches = re.findall(r'\d+', text)
```

### 3. Handle None Results

Always check if match is None:

```python
match = re.search(pattern, text)
if match:
    print(match.group())
else:
    print("No match found")
```

### 4. Use Appropriate Function

- `re.match()` - Only matches at start
- `re.search()` - Finds first match anywhere
- `re.findall()` - Finds all matches
- `re.finditer()` - Iterator for large texts

### 5. Be Careful with Greedy Matching

```python
# Greedy (matches too much)
text = "<div>content</div><div>more</div>"
match = re.search(r'<div>.*</div>', text)
print(match.group())  # "<div>content</div><div>more</div>"

# Lazy (matches correctly)
match = re.search(r'<div>.*?</div>', text)
print(match.group())  # "<div>content</div>"
```

## Common Pitfalls

### 1. Forgetting Anchors

```python
# Without anchors - matches partial strings
pattern = r'\d{3}'
re.match(pattern, "abc123def")  # Matches!

# With anchors - matches full string
pattern = r'^\d{3}$'
re.match(pattern, "abc123def")  # No match
```

### 2. Not Escaping Special Characters

```python
# Wrong - dot matches any character
pattern = r'example.com'
re.search(pattern, "exampleXcom")  # Matches!

# Correct - escape dot
pattern = r'example\.com'
re.search(pattern, "exampleXcom")  # No match
```

### 3. Confusing match() and search()

```python
text = "Hello 123 World"

# match() only checks start
re.match(r'\d+', text)  # None (doesn't start with digit)

# search() finds anywhere
re.search(r'\d+', text)  # Matches "123"
```

## Performance Tips

1. **Compile patterns** for repeated use
2. **Use specific patterns** instead of `.*`
3. **Avoid catastrophic backtracking**
4. **Consider alternatives** - sometimes string methods are faster

## Resources

- [Python `re` module documentation](https://docs.python.org/3/library/re.html)
- [Regex101 Python tester](https://regex101.com/)
- Practice with exercises in this repository

---

**Next:** [project-regex-in-js.md](project-regex-in-js.md) for JavaScript regex guide

