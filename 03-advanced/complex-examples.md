# Complex Regex Examples

Advanced patterns combining multiple concepts: backreferences, lookarounds, greedy/lazy matching, and nested groups.

## Example 1: Validate Complex Password Rules

### Requirements
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character (!@#$%^&*)
- No spaces
- No repeated characters (3+ in a row)

### Pattern
```
^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])(?!.*\s)(?!.*(.)\1{2,}).{8,}$
```

### Explanation
- `^` - Start of string
- `(?=.*[A-Z])` - Lookahead: contains uppercase
- `(?=.*[a-z])` - Lookahead: contains lowercase
- `(?=.*\d)` - Lookahead: contains digit
- `(?=.*[!@#$%^&*])` - Lookahead: contains special char
- `(?!.*\s)` - Negative lookahead: no spaces
- `(?!.*(.)\1{2,})` - Negative lookahead: no 3+ repeated chars
- `.{8,}` - At least 8 characters
- `$` - End of string

### Code Examples

**Python:**
```python
import re

def validate_complex_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])(?!.*\s)(?!.*(.)\1{2,}).{8,}$'
    return bool(re.match(pattern, password))

passwords = [
    "Password123!",
    "PASS123!word",  # No lowercase
    "password123!",  # No uppercase
    "Pass123!",      # Too short
    "Pass 123!",     # Contains space
    "Paass123!",     # Repeated chars
]
for pwd in passwords:
    print(f"{pwd}: {validate_complex_password(pwd)}")
```

---

## Example 2: Extract HTML Tag Content Safely

### Pattern
```
<(\w+)[^>]*>([^<]*(?:<(?!/\1)[^<]*[^<])*?)</\1>
```

### Simpler Version (for nested tags, use parser instead)
```
<(\w+)[^>]*>([^<]+)</\1>
```

### Explanation
- `<(\w+)` - Opening tag, capture tag name
- `[^>]*>` - Rest of opening tag
- `([^<]+)` - Content (no `<` characters)
- `</\1>` - Closing tag matching opening

### Code Examples

**Python:**
```python
import re

def extract_tag_content(html, tag_name):
    pattern = f'<{tag_name}[^>]*>([^<]+)</{tag_name}>'
    matches = re.findall(pattern, html)
    return matches

html = "<div>Hello</div><p>World</p><div>Test</div>"
contents = extract_tag_content(html, "div")
print(contents)  # ['Hello', 'Test']
```

---

## Example 3: Find Repeated Sequences

### Pattern
```
(.{2,})\1+
```

### Explanation
- `(.{2,})` - Capture 2+ characters
- `\1+` - Same sequence repeated one or more times

### Matches
- ✅ "ababab" → Matches "ab" repeated
- ✅ "hellohello" → Matches "hello" repeated
- ✅ "123123123" → Matches "123" repeated

### Code Examples

**Python:**
```python
import re

def find_repeated_sequences(text):
    pattern = r'(.{2,})\1+'
    matches = []
    for match in re.finditer(pattern, text):
        matches.append(match.group(1))
    return matches

text = "ababab hellohello 123123123"
sequences = find_repeated_sequences(text)
print(sequences)  # ['ab', 'hello', '123']
```

---

## Example 4: Log Parsing with Named Groups

### Pattern
```
(?P<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+\[(?P<level>\w+)\]\s+(?P<message>.*)
```

### Explanation
- `(?P<timestamp>...)` - Named group for timestamp
- `(?P<level>...)` - Named group for log level
- `(?P<message>...)` - Named group for message

### Code Examples

**Python:**
```python
import re
from datetime import datetime

def parse_log_entry(log_line):
    pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+\[(?P<level>\w+)\]\s+(?P<message>.*)'
    match = re.match(pattern, log_line)
    if match:
        return {
            'timestamp': match.group('timestamp'),
            'level': match.group('level'),
            'message': match.group('message')
        }
    return None

log = "2023-12-25 10:30:45 [ERROR] Database connection failed"
parsed = parse_log_entry(log)
print(parsed)
# {'timestamp': '2023-12-25 10:30:45', 'level': 'ERROR', 'message': 'Database connection failed'}
```

**JavaScript:**
```javascript
function parseLogEntry(logLine) {
    const pattern = /(?<timestamp>\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+\[(?<level>\w+)\]\s+(?<message>.*)/;
    const match = logLine.match(pattern);
    if (match) {
        return {
            timestamp: match.groups.timestamp,
            level: match.groups.level,
            message: match.groups.message
        };
    }
    return null;
}
```

---

## Example 5: Extract IP and Port Combinations

### Pattern
```
(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d{1,5})
```

### Better Pattern (with validation)
```
(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):([1-9]\d{0,4}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])
```

### Simplified Version
```
(\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5})
```

### Code Examples

**Python:**
```python
import re

def extract_ip_port(text):
    pattern = r'(\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5})'
    matches = re.findall(pattern, text)
    return [{'ip': ip, 'port': port} for ip, port in matches]

text = "Server at 192.168.1.1:8080 and 10.0.0.1:443"
results = extract_ip_port(text)
print(results)
# [{'ip': '192.168.1.1', 'port': '8080'}, {'ip': '10.0.0.1', 'port': '443'}]
```

---

## Example 6: Parse JSON-like Logs

### Pattern (Simplified - real JSON needs a parser)
```
"(\w+)":\s*"([^"]*)"
```

### Explanation
- `"(\w+)"` - Capture key (in quotes)
- `:\s*` - Colon and optional whitespace
- `"([^"]*)"` - Capture value (in quotes)

### Code Examples

**Python:**
```python
import re

def parse_json_like(log_line):
    pattern = r'"(\w+)":\s*"([^"]*)"'
    matches = re.findall(pattern, log_line)
    return dict(matches)

log = '{"level": "ERROR", "message": "Connection failed", "code": "500"}'
parsed = parse_json_like(log)
print(parsed)
# {'level': 'ERROR', 'message': 'Connection failed', 'code': '500'}
```

---

## Example 7: Match Nested Parentheses (Limited)

### Pattern (2 levels deep)
```
\(([^()]+|\([^()]*\))*\)
```

### Explanation
- `\(` - Opening parenthesis
- `([^()]+|\([^()]*\))*` - Content: non-parentheses OR parentheses with content
- `\)` - Closing parenthesis

**Note:** True nested matching requires recursion (not supported in all engines).

### Code Examples

**Python:**
```python
import re

def find_nested_parens(text):
    # Simplified - only handles 2 levels
    pattern = r'\(([^()]+|\([^()]*\))*\)'
    matches = re.findall(pattern, text)
    return matches

text = "outer (inner (nested) more) text"
matches = find_nested_parens(text)
print(matches)  # ['inner (nested) more']
```

---

## Example 8: Extract URLs with Query Parameters

### Pattern
```
(https?://[^\s]+)
```

### Better Pattern (extracts components)
```
(https?)://([^/]+)(/[^\s?]*)?(\?[^\s]*)?
```

### Code Examples

**Python:**
```python
import re
from urllib.parse import urlparse

def extract_urls(text):
    pattern = r'(https?://[^\s]+)'
    return re.findall(pattern, text)

text = "Visit https://example.com/page?param=value and http://test.org"
urls = extract_urls(text)
print(urls)
# ['https://example.com/page?param=value', 'http://test.org']
```

---

## Tips for Complex Patterns

1. **Break it down** - Build pattern incrementally
2. **Test each part** - Verify each component works
3. **Use named groups** - Makes extraction clearer
4. **Document thoroughly** - Explain complex parts
5. **Consider alternatives** - Sometimes a parser is better
6. **Test edge cases** - Empty strings, special characters, boundaries
7. **Performance matters** - Complex patterns can be slow

---

**Next:** Try the [exercises-advanced.md](exercises-advanced.md) to practice!

