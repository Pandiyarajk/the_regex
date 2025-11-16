# Intermediate Regex Exercise Solutions

Solutions for exercises in `02-intermediate/exercises-intermediate.md`.

## Exercise 1: Validate Strong Password

**Pattern:** `^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$`

**Explanation:**
- `^` - Start of string
- `(?=.*[A-Z])` - Lookahead: contains uppercase letter
- `(?=.*[a-z])` - Lookahead: contains lowercase letter
- `(?=.*\d)` - Lookahead: contains digit
- `(?=.*[!@#$%^&*])` - Lookahead: contains special character
- `.{8,}` - At least 8 characters
- `$` - End of string

**Note:** Each lookahead checks the entire string, so order doesn't matter.

---

## Exercise 2: Extract Hashtags

**Pattern:** `#(\w+)`

**Explanation:**
- `#` - Literal hash symbol
- `(\w+)` - Capture word characters (letters, digits, underscore)

**Usage:**
```python
import re
hashtags = re.findall(r'#(\w+)', text)
```

**JavaScript:**
```javascript
const hashtags = text.match(/#(\w+)/g)?.map(m => m.slice(1));
```

---

## Exercise 3: Extract Price Values

**Pattern:** `\$(\d{1,3}(?:,\d{3})*(?:\.\d{2})?)`

**Explanation:**
- `\$` - Literal dollar sign
- `(\d{1,3}` - 1-3 digits (first group)
- `(?:,\d{3})*` - Zero or more groups of comma + 3 digits
- `(?:\.\d{2})?` - Optional decimal part (.XX)

**Simpler version (without thousands separator):**
```
\$(\d+(?:\.\d{2})?)
```

---

## Exercise 4: Match All Capitalized Words

**Pattern:** `\b[A-Z][a-z]+\b`

**Explanation:**
- `\b` - Word boundary
- `[A-Z]` - Uppercase letter (first character)
- `[a-z]+` - One or more lowercase letters
- `\b` - Word boundary

**Note:** This excludes words like "HELLO" (all caps) and "iPhone" (starts lowercase).

---

## Exercise 5: Extract Domain from URLs

**Pattern:** `https?://(?:www\.)?([^/]+)`

**Explanation:**
- `https?` - "http" or "https"
- `://` - Literal "://"
- `(?:www\.)?` - Optional "www." (non-capturing)
- `([^/]+)` - Capture domain (one or more non-slash characters)

**Alternative (more specific):**
```
https?://(?:www\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})
```

---

## Exercise 6: Parse Log Entry

**Pattern:** `\[([^\]]+)\]\s+(\w+):\s+(.*)`

**Explanation:**
- `\[([^\]]+)\]` - Capture timestamp (content in brackets)
- `\s+` - One or more spaces
- `(\w+)` - Capture log level
- `:\s+` - Colon and spaces
- `(.*)` - Capture message (rest of line)

**Full pattern with all components:**
```
\[(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\]\s+(\w+):\s+(.*)
```

---

## Exercise 7: Validate Credit Card Format

**Pattern:** `^\d{4}([- ]?)\d{4}\1\d{4}\1\d{4}$`

**Explanation:**
- `^` - Start of string
- `\d{4}` - Exactly 4 digits
- `([- ]?)` - Capture separator (hyphen or space) in group 1
- `\d{4}` - Exactly 4 digits
- `\1` - Same separator as group 1 (ensures consistency)
- `\d{4}` - Exactly 4 digits
- `\1` - Same separator
- `\d{4}` - Exactly 4 digits
- `$` - End of string

**Alternative (allows no separators):**
```
^(\d{4}[- ]?){3}\d{4}$|^\d{16}$
```

---

## Exercise 8: Extract Email Local Part and Domain

**Pattern:** `([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})`

**Explanation:**
- `([a-zA-Z0-9._%+-]+)` - Capture local part (group 1)
- `@` - Literal @ symbol
- `([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})` - Capture domain (group 2)

**Usage:**
```python
import re
match = re.search(r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', email)
if match:
    local = match.group(1)
    domain = match.group(2)
```

---

## Exercise 9: Find Repeated Phrases

**Pattern:** `\b(\w+)\W+\1\b`

**Explanation:**
- `\b` - Word boundary
- `(\w+)` - Capture word (group 1)
- `\W+` - One or more non-word characters (spaces, punctuation)
- `\1` - Same word as group 1
- `\b` - Word boundary

**More flexible (handles punctuation):**
```
(\w+)[\s,]+?\1
```

---

## Exercise 10: Extract Time in 12-Hour Format

**Pattern:** `(0[1-9]|1[0-2]):([0-5]\d)\s+(AM|PM)`

**Explanation:**
- `(0[1-9]|1[0-2])` - Hour: 01-12
  - `0[1-9]` - 01-09
  - `1[0-2]` - 10-12
- `:` - Literal colon
- `([0-5]\d)` - Minutes: 00-59
- `\s+` - One or more spaces
- `(AM|PM)` - AM or PM

**Case-insensitive version:**
```
(0[1-9]|1[0-2]):([0-5]\d)\s+(AM|PM)
```
(Add `i` flag or use `[Aa][Mm]|[Pp][Mm]`)

---

## Challenge Exercise: Validate Complex Password

**Pattern:** `^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*])(?!.*\s)(?!.*(.)\1{2,}).{8,}$`

**Explanation:**
- `^` - Start of string
- `(?=.*[A-Z])` - Contains uppercase
- `(?=.*[a-z])` - Contains lowercase
- `(?=.*\d)` - Contains digit
- `(?=.*[!@#$%^&*])` - Contains special char
- `(?!.*\s)` - Negative lookahead: no spaces
- `(?!.*(.)\1{2,})` - Negative lookahead: no 3+ repeated chars
  - `(.)` - Capture any character
  - `\1{2,}` - Same character repeated 2+ more times (3+ total)
- `.{8,}` - At least 8 characters
- `$` - End of string

---

## Tips for Intermediate Solutions

1. **Lookaheads are powerful** - Use for multiple conditions
2. **Backreferences ensure consistency** - Use `\1` for matching separators
3. **Non-capturing groups** - Use `(?:)` when you don't need the capture
4. **Character classes** - Use `[^x]` for "not x" patterns
5. **Test edge cases** - Empty strings, boundaries, special characters

---

**Next:** [advanced-solutions.md](advanced-solutions.md)

