# Basic Regex Exercise Solutions

Solutions for exercises in `01-basics/exercises-basic.md`.

## Exercise 1: Match Numbers

**Pattern:** `\d+`

**Explanation:**
- `\d` - Any digit
- `+` - One or more

**Alternative:** `[0-9]+`

---

## Exercise 2: Detect Mobile Number

**Pattern:** `\d{10}` or `^\d{10}$` (with anchors for full string)

**For formatted numbers:**
```
\d{3}[-.\s]?\d{3}[-.\s]?\d{4}
```

**Explanation:**
- `\d{3}` - Exactly 3 digits
- `[-.\s]?` - Optional separator (hyphen, dot, or space)
- `\d{3}` - Exactly 3 digits
- `[-.\s]?` - Optional separator
- `\d{4}` - Exactly 4 digits

**For strict 10 digits only:**
```
^\d{10}$
```

---

## Exercise 3: Find All Words Starting with 'A'

**Pattern:** `\b[Aa]\w+\b` or `\ba\w+\b` (with case-insensitive flag)

**Explanation:**
- `\b` - Word boundary
- `[Aa]` or `a` (with `i` flag) - Letter 'A' or 'a'
- `\w+` - One or more word characters
- `\b` - Word boundary

---

## Exercise 4: Match Valid PIN Code

**Pattern:** `^\d{4}$|^\d{6}$` or `^(\d{4}|\d{6})$`

**Explanation:**
- `^` - Start of string
- `\d{4}` - Exactly 4 digits
- `|` - OR
- `\d{6}` - Exactly 6 digits
- `$` - End of string

**Alternative:** `^(\d{4}|\d{6})$`

---

## Exercise 5: Extract Domain Names

**Pattern:** `https?://(?:www\.)?([^/]+)`

**Explanation:**
- `https?` - "http" or "https"
- `://` - Literal "://"
- `(?:www\.)?` - Optional "www." (non-capturing)
- `([^/]+)` - Capture domain (one or more non-slash characters)

**For simpler case (domain already isolated):**
```
([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})
```

---

## Exercise 6: Match Time Format (HH:MM)

**Pattern:** `([01]\d|2[0-3]):([0-5]\d)`

**Explanation:**
- `([01]\d|2[0-3])` - Hours: 00-23
  - `[01]\d` - 00-19
  - `2[0-3]` - 20-23
- `:` - Literal colon
- `([0-5]\d)` - Minutes: 00-59

**Simpler version (less strict):**
```
\d{2}:\d{2}
```

---

## Exercise 7: Find Repeated Words

**Pattern:** `\b(\w+)\s+\1\b`

**Explanation:**
- `\b` - Word boundary
- `(\w+)` - Capture word (group 1)
- `\s+` - One or more spaces
- `\1` - Backreference to group 1 (same word)
- `\b` - Word boundary

---

## Exercise 8: Validate Username (Stricter)

**Pattern:** `^[a-zA-Z][a-zA-Z0-9_]{4,19}$`

**Explanation:**
- `^` - Start of string
- `[a-zA-Z]` - Must start with letter
- `[a-zA-Z0-9_]{4,19}` - 4-19 more characters (letters, digits, underscore)
- `$` - End of string

**Total length:** 5-20 characters (1 initial + 4-19 more)

---

## Exercise 9: Match IP Address (Simple)

**Pattern:** `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`

**Explanation:**
- `\d{1,3}` - 1-3 digits (simplified - doesn't validate 0-255)
- `\.` - Literal dot
- Repeated 4 times

**Better version (validates 0-255):**
```
(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)
```

---

## Exercise 10: Remove Extra Spaces

**Pattern:** `\s{2,}` or ` {2,}` (for spaces only)

**Explanation:**
- `\s{2,}` - Two or more whitespace characters
- ` {2,}` - Two or more spaces (spaces only)

**For replacement:**
```python
import re
text = re.sub(r'\s{2,}', ' ', text)
```

---

## Challenge Exercise: Extract Dates

**Pattern:** `(\d{1,2})[/-](\d{1,2})[/-](\d{2,4})`

**Explanation:**
- `(\d{1,2})` - Day (1-2 digits)
- `[/-]` - Separator: `/` or `-`
- `(\d{1,2})` - Month (1-2 digits)
- `[/-]` - Separator: `/` or `-`
- `(\d{2,4})` - Year (2-4 digits)

**Note:** This pattern doesn't validate date ranges (e.g., month 1-12, day 1-31). For full validation, use a date parsing library.

---

## Tips for Understanding Solutions

1. **Anchors matter** - Use `^` and `$` when matching entire strings
2. **Word boundaries** - Use `\b` for whole word matching
3. **Groups** - Use `()` to capture parts of matches
4. **Backreferences** - Use `\1`, `\2` to reference captured groups
5. **Test your patterns** - Always test with various inputs

---

**Next:** [intermediate-solutions.md](intermediate-solutions.md)

