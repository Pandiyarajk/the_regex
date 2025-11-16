# Medium-Level Regex Examples

Practical examples combining intermediate concepts: character classes, grouping, quantifiers, and lookarounds.

## Example 1: Validate Indian Phone Number

### Pattern
```
^(\+91|91|0)?[6-9]\d{9}$
```

### Explanation
- `^` - Start of string
- `(\+91|91|0)?` - Optional country code (+91, 91, or 0)
- `[6-9]` - First digit must be 6, 7, 8, or 9
- `\d{9}` - Exactly 9 more digits
- `$` - End of string

**Total:** 10 digits (with optional prefix)

### Matches
- ✅ "9876543210"
- ✅ "+919876543210"
- ✅ "919876543210"
- ✅ "09876543210"
- ❌ "5876543210" (doesn't start with 6-9)
- ❌ "987654321" (only 9 digits)

### Code Examples

**Python:**
```python
import re

def validate_indian_phone(phone):
    pattern = r'^(\+91|91|0)?[6-9]\d{9}$'
    return bool(re.match(pattern, phone))

phones = ["9876543210", "+919876543210", "5876543210"]
for phone in phones:
    print(f"{phone}: {validate_indian_phone(phone)}")
```

**JavaScript:**
```javascript
function validateIndianPhone(phone) {
    const pattern = /^(\+91|91|0)?[6-9]\d{9}$/;
    return pattern.test(phone);
}

const phones = ["9876543210", "+919876543210", "5876543210"];
phones.forEach(phone => {
    console.log(`${phone}: ${validateIndianPhone(phone)}`);
});
```

---

## Example 2: Validate Email (Improved)

### Pattern
```
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

### Explanation
- `^` - Start of string
- `[a-zA-Z0-9._%+-]+` - Local part (one or more allowed chars)
- `@` - Literal @ symbol
- `[a-zA-Z0-9.-]+` - Domain name
- `\.` - Literal dot
- `[a-zA-Z]{2,}` - TLD (2+ letters)
- `$` - End of string

### Matches
- ✅ "user@example.com"
- ✅ "john.doe@company.co.uk"
- ✅ "user+tag@example.com"
- ❌ "@example.com" (missing local part)
- ❌ "user@.com" (missing domain)
- ❌ "user@example" (missing TLD)

### Code Examples

**Python:**
```python
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

emails = ["user@example.com", "@example.com", "user@.com"]
for email in emails:
    print(f"{email}: {validate_email(email)}")
```

**JavaScript:**
```javascript
function validateEmail(email) {
    const pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return pattern.test(email);
}
```

---

## Example 3: Extract Domain Name

### Pattern
```
https?://(?:www\.)?([^/]+)
```

### Explanation
- `https?` - "http" or "https"
- `://` - Literal "://"
- `(?:www\.)?` - Optional "www." (non-capturing)
- `([^/]+)` - Capture domain (one or more non-slash chars)

### Matches
- "https://www.example.com/path" → Captures: "www.example.com"
- "http://example.com" → Captures: "example.com"
- "https://subdomain.example.org/page" → Captures: "subdomain.example.org"

### Code Examples

**Python:**
```python
import re

def extract_domain(url):
    pattern = r'https?://(?:www\.)?([^/]+)'
    match = re.search(pattern, url)
    return match.group(1) if match else None

urls = [
    "https://www.example.com/path",
    "http://example.com",
    "https://subdomain.example.org/page"
]
for url in urls:
    print(f"{url} → {extract_domain(url)}")
```

**JavaScript:**
```javascript
function extractDomain(url) {
    const pattern = /https?:\/\/(?:www\.)?([^/]+)/;
    const match = url.match(pattern);
    return match ? match[1] : null;
}
```

---

## Example 4: Extract Date in Multiple Formats

### Pattern
```
(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})
```

### Explanation
- `(\d{1,2})` - Day (1-2 digits)
- `[/-]` - Separator: `/` or `-`
- `(\d{1,2})` - Month (1-2 digits)
- `[/-]` - Separator: `/` or `-`
- `(\d{2,4})` - Year (2-4 digits)

### Matches
- "25/12/2023" → Groups: ("25", "12", "2023")
- "1-1-23" → Groups: ("1", "1", "23")
- "12/25/2023" → Groups: ("12", "25", "2023")

### Code Examples

**Python:**
```python
import re
from datetime import datetime

def parse_date(date_str):
    pattern = r'(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})'
    match = re.match(pattern, date_str)
    if match:
        day, month, year = match.groups()
        year = int(year) if len(year) == 4 else 2000 + int(year)
        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"
    return None

dates = ["25/12/2023", "1-1-23", "12/25/2023"]
for date in dates:
    print(f"{date} → {parse_date(date)}")
```

**JavaScript:**
```javascript
function parseDate(dateStr) {
    const pattern = /(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})/;
    const match = dateStr.match(pattern);
    if (match) {
        const [, day, month, year] = match;
        const fullYear = year.length === 4 ? year : `20${year}`;
        return `${fullYear}-${month.padStart(2, '0')}-${day.padStart(2, '0')}`;
    }
    return null;
}
```

---

## Example 5: Find Duplicate Words

### Pattern
```
\b(\w+)\s+\1\b
```

### Explanation
- `\b` - Word boundary
- `(\w+)` - Capture word (group 1)
- `\s+` - One or more spaces
- `\1` - Backreference to group 1 (same word)
- `\b` - Word boundary

### Matches
- "the the cat" → Matches "the the"
- "hello hello world" → Matches "hello hello"
- "the cat sat" → No match

### Code Examples

**Python:**
```python
import re

def find_duplicates(text):
    pattern = r'\b(\w+)\s+\1\b'
    matches = re.findall(pattern, text)
    return matches

text = "the the cat sat on the the mat"
duplicates = find_duplicates(text)
print(duplicates)  # ['the', 'the']
```

**JavaScript:**
```javascript
function findDuplicates(text) {
    const pattern = /\b(\w+)\s+\1\b/g;
    const matches = [];
    let match;
    while ((match = pattern.exec(text)) !== null) {
        matches.push(match[1]);
    }
    return matches;
}
```

---

## Example 6: Extract Hashtags

### Pattern
```
#(\w+)
```

### Explanation
- `#` - Literal hash symbol
- `(\w+)` - Capture word characters (hashtag name)

### Matches
- "Check out #regex and #coding!" → Captures: "regex", "coding"
- "#python #javascript #webdev" → Captures: "python", "javascript", "webdev"

### Code Examples

**Python:**
```python
import re

def extract_hashtags(text):
    pattern = r'#(\w+)'
    return re.findall(pattern, text)

text = "Check out #regex and #coding! #python"
hashtags = extract_hashtags(text)
print(hashtags)  # ['regex', 'coding', 'python']
```

**JavaScript:**
```javascript
function extractHashtags(text) {
    const pattern = /#(\w+)/g;
    const matches = [];
    let match;
    while ((match = pattern.exec(text)) !== null) {
        matches.push(match[1]);
    }
    return matches;
}
```

---

## Example 7: Extract Price Values

### Pattern
```
\$(\d+(?:\.\d{2})?)
```

### Explanation
- `\$` - Literal dollar sign
- `(\d+(?:\.\d{2})?)` - Capture price:
  - `\d+` - One or more digits
  - `(?:\.\d{2})?` - Optional decimal part (non-capturing)

### Matches
- "$100" → Captures: "100"
- "$99.99" → Captures: "99.99"
- "$1,234.56" → Matches but doesn't handle commas (needs improvement)

### Code Examples

**Python:**
```python
import re

def extract_prices(text):
    pattern = r'\$(\d+(?:\.\d{2})?)'
    return re.findall(pattern, text)

text = "Prices: $100, $99.99, and $50.00"
prices = extract_prices(text)
print(prices)  # ['100', '99.99', '50.00']
```

**JavaScript:**
```javascript
function extractPrices(text) {
    const pattern = /\$(\d+(?:\.\d{2})?)/g;
    const matches = [];
    let match;
    while ((match = pattern.exec(text)) !== null) {
        matches.push(match[1]);
    }
    return matches;
}
```

---

## Example 8: Match All Capitalized Words

### Pattern
```
\b[A-Z][a-z]+\b
```

### Explanation
- `\b` - Word boundary
- `[A-Z]` - Uppercase letter (first character)
- `[a-z]+` - One or more lowercase letters
- `\b` - Word boundary

### Matches
- "Hello World Test" → Matches: "Hello", "World", "Test"
- "HELLO world" → Matches: "world" only (HELLO is all caps)
- "iPhone" → No match (starts with lowercase)

### Code Examples

**Python:**
```python
import re

def find_capitalized_words(text):
    pattern = r'\b[A-Z][a-z]+\b'
    return re.findall(pattern, text)

text = "Hello World from Python"
words = find_capitalized_words(text)
print(words)  # ['Hello', 'World', 'Python']
```

**JavaScript:**
```javascript
function findCapitalizedWords(text) {
    const pattern = /\b[A-Z][a-z]+\b/g;
    return text.match(pattern) || [];
}
```

---

## Tips for Medium-Level Patterns

1. **Combine concepts** - Use character classes, groups, and quantifiers together
2. **Test edge cases** - Empty strings, special characters, boundaries
3. **Use anchors** - `^` and `$` for full string validation
4. **Capture strategically** - Only capture what you need
5. **Consider performance** - Complex patterns can be slow on large text
6. **Document your patterns** - Explain complex parts

---

**Next:** Try the [exercises-intermediate.md](exercises-intermediate.md) to practice!

