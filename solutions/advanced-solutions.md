# Advanced Regex Exercise Solutions

Solutions for exercises in `03-advanced/exercises-advanced.md`.

## Exercise 1: Parse JSON-like Logs

**Pattern:** `"(\w+)":\s*"([^"]*)"`

**Explanation:**
- `"(\w+)"` - Capture key in quotes (group 1)
- `:\s*` - Colon and optional whitespace
- `"([^"]*)"` - Capture value in quotes (group 2)

**Usage:**
```python
import re
pattern = r'"(\w+)":\s*"([^"]*)"'
matches = re.findall(pattern, log_line)
result = dict(matches)
```

**Note:** This is simplified. Real JSON parsing should use a JSON parser.

---

## Exercise 2: Match Nested Parentheses (2 Levels)

**Pattern:** `\(([^()]+|\([^()]*\))*\)`

**Explanation:**
- `\(` - Opening parenthesis
- `([^()]+|\([^()]*\))*` - Content:
  - `[^()]+` - One or more non-parenthesis characters
  - `|` - OR
  - `\([^()]*\)` - Parentheses with non-parenthesis content inside
  - `*` - Zero or more of the above
- `\)` - Closing parenthesis

**Note:** This handles 2 levels. True nested matching requires recursion (not supported in all engines).

---

## Exercise 3: Extract IP + Port Combinations

**Pattern:** `(\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5})`

**Explanation:**
- `(\d{1,3}(?:\.\d{1,3}){3})` - Capture IP (group 1)
  - `\d{1,3}` - 1-3 digits
  - `(?:\.\d{1,3}){3}` - Three groups of dot + 1-3 digits
- `:` - Literal colon
- `(\d{1,5})` - Capture port (group 2): 1-5 digits (1-65535, simplified)

**Better port validation:**
```
(\d{1,3}(?:\.\d{1,3}){3}):([1-9]\d{0,4}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])
```

---

## Exercise 4: Find Repeated Substrings

**Pattern:** `(.{2,})\1+`

**Explanation:**
- `(.{2,})` - Capture 2+ characters (group 1)
- `\1+` - Same substring repeated one or more times

**Usage:**
```python
import re
pattern = r'(.{2,})\1+'
for match in re.finditer(pattern, text):
    print(f"Found '{match.group(1)}' repeated")
```

---

## Exercise 5: Validate Complex Password

**Pattern:** `^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])(?!.*\s)(?!.*(.)\1{2,}).{8,}$`

**Explanation:**
- `^` - Start of string
- `(?=.*[A-Z])` - Contains uppercase
- `(?=.*[a-z])` - Contains lowercase
- `(?=.*\d)` - Contains digit
- `(?=.*[!@#$%^&*])` - Contains special char
- `(?!.*\s)` - No spaces
- `(?!.*(.)\1{2,})` - No 3+ repeated chars
  - `(.)` - Capture any char
  - `\1{2,}` - Same char 2+ more times
- `.{8,}` - At least 8 chars
- `$` - End of string

---

## Exercise 6: Extract HTML Tag Attributes

**Pattern:** `(\w+)=["']([^"']+)["']`

**Explanation:**
- `(\w+)` - Capture attribute name (group 1)
- `=` - Literal equals
- `["']` - Opening quote (single or double)
- `([^"']+)` - Capture value (group 2) - non-quote characters
- `["']` - Closing quote

**Usage:**
```python
import re
pattern = r'(\w+)=["\']([^"\']+)["\']'
matches = re.findall(pattern, html_tag)
attributes = dict(matches)
```

---

## Exercise 7: Match Balanced Quotes

**Pattern:** `(["'])(.*?)\1`

**Explanation:**
- `(["'])` - Capture quote character (single or double) in group 1
- `(.*?)` - Capture content (lazy match) in group 2
- `\1` - Match same quote character as group 1

**Usage:**
```python
import re
pattern = r'(["\'])(.*?)\1'
matches = re.findall(pattern, text)
# Returns list of tuples: (quote_char, content)
```

---

## Exercise 8: Extract URLs with Components

**Pattern:** `(https?)://([^/]+)(/[^\s?]*)?(\?[^\s]*)?`

**Explanation:**
- `(https?)` - Capture protocol (group 1): "http" or "https"
- `://` - Literal "://"
- `([^/]+)` - Capture domain (group 2): one or more non-slash chars
- `(/[^\s?]*)?` - Optional path (group 3)
- `(\?[^\s]*)?` - Optional query string (group 4)

**Usage:**
```python
import re
pattern = r'(https?)://([^/]+)(/[^\s?]*)?(\?[^\s]*)?'
match = re.search(pattern, url)
if match:
    protocol = match.group(1)
    domain = match.group(2)
    path = match.group(3) or ""
    query = match.group(4) or ""
```

---

## Exercise 9: Find Palindromic Words

**Pattern:** `\b([a-zA-Z])([a-zA-Z]?)[a-zA-Z]*\2\1\b`

**Explanation:**
- `\b` - Word boundary
- `([a-zA-Z])` - Capture first letter (group 1)
- `([a-zA-Z]?)` - Capture optional second letter (group 2)
- `[a-zA-Z]*` - Zero or more middle letters
- `\2` - Second letter (if exists)
- `\1` - First letter
- `\b` - Word boundary

**Simpler version (for even-length palindromes):**
```
\b([a-zA-Z])([a-zA-Z])\w*\2\1\b
```

**For any length (more complex):**
```
\b([a-zA-Z])[a-zA-Z]*\1\b
```
(This matches words starting and ending with same letter - simpler but less strict)

---

## Exercise 10: Parse Apache Log Entry

**Pattern:** `^(\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+\[([^\]]+)\]\s+"(\w+)\s+([^\s]+)\s+([^"]+)"\s+(\d+)\s+(\d+|-)$`

**Explanation:**
- `^` - Start of line
- `(\d+\.\d+\.\d+\.\d+)` - Capture IP (group 1)
- `\s+-\s+-\s+` - Remote logname and user (usually "-")
- `\[([^\]]+)\]` - Capture timestamp (group 2)
- `\s+"(\w+)` - Capture HTTP method (group 3)
- `\s+([^\s]+)` - Capture path (group 4)
- `\s+([^"]+)"` - Capture protocol (group 5)
- `\s+(\d+)` - Capture status code (group 6)
- `\s+(\d+|-)` - Capture size (group 7)
- `$` - End of line

**Usage:**
```python
import re
pattern = r'^(\d+\.\d+\.\d+\.\d+)\s+-\s+-\s+\[([^\]]+)\]\s+"(\w+)\s+([^\s]+)\s+([^"]+)"\s+(\d+)\s+(\d+|-)$'
match = re.match(pattern, log_line)
if match:
    ip, timestamp, method, path, protocol, status, size = match.groups()
```

---

## Challenge Exercise: CSV Parsing (Simplified)

**Pattern:** `(?:^|,)(?:"([^"]*(?:""[^"]*)*)"|([^,]+))`

**Explanation:**
- `(?:^|,)` - Start of string or comma (non-capturing)
- `(?:"([^"]*(?:""[^"]*)*)"|([^,]+))` - Field:
  - `"([^"]*(?:""[^"]*)*)"` - Quoted field with escaped quotes
  - `|` - OR
  - `([^,]+)` - Unquoted field

**Note:** This is simplified. Real CSV parsing needs proper handling of:
- Escaped quotes within quoted fields
- Newlines within quoted fields
- Edge cases and malformed CSV

**Better approach:** Use a CSV library for production code.

---

## Tips for Advanced Solutions

1. **Know limitations** - Some problems need parsers, not regex
2. **Use backreferences wisely** - Great for consistency checks
3. **Combine techniques** - Lookarounds + groups + quantifiers
4. **Test thoroughly** - Edge cases matter
5. **Document complex patterns** - Explain each part
6. **Consider performance** - Complex patterns can be slow

---

**Next:** [project-solutions.md](project-solutions.md) for project implementations

