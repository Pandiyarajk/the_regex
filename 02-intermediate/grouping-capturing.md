# Grouping and Capturing

Groups allow you to treat multiple characters as a single unit and capture matched text for later use.

## Basic Grouping

### Syntax: `(pattern)`

Parentheses create a **capturing group** - they group characters together and save the matched text.

### Simple Example

```
(abc)+
```

This matches one or more occurrences of "abc":
- ✅ "abc"
- ✅ "abcabc"
- ✅ "abcabcabc"
- ❌ "ab" (incomplete group)

### Without Grouping

```
abc+
```

This matches "ab" followed by one or more "c"s:
- ✅ "abc"
- ✅ "abcc"
- ✅ "abccc"
- ❌ "abcabc" (only matches first "abc")

## Capturing Groups

### What is Capturing?

Capturing groups save the matched text so you can:
- Extract specific parts of a match
- Use backreferences (see advanced section)
- Apply quantifiers to groups

### Example: Extracting Date Components

```
(\d{2})/(\d{2})/(\d{4})
```

This pattern captures:
- Group 1: Day (2 digits)
- Group 2: Month (2 digits)
- Group 3: Year (4 digits)

**Match:** "25/12/2023"

**Captured Groups:**
- Group 1: "25"
- Group 2: "12"
- Group 3: "2023"

### Code Examples

**Python:**
```python
import re

pattern = r'(\d{2})/(\d{2})/(\d{4})'
text = "Date: 25/12/2023"

match = re.search(pattern, text)
if match:
    day = match.group(1)      # "25"
    month = match.group(2)    # "12"
    year = match.group(3)     # "2023"
    print(f"Day: {day}, Month: {month}, Year: {year}")
```

**JavaScript:**
```javascript
const pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
const text = "Date: 25/12/2023";

const match = text.match(pattern);
if (match) {
    const day = match[1];      // "25"
    const month = match[2];    // "12"
    const year = match[3];     // "2023"
    console.log(`Day: ${day}, Month: ${month}, Year: ${year}`);
}
```

## Non-Capturing Groups

### Syntax: `(?:pattern)`

Sometimes you want to group without capturing. Use `?:` at the start of the group.

### When to Use

- Group for quantifiers only
- Improve performance (fewer captures)
- Cleaner group numbering

### Example

```
(?:Mr|Mrs|Ms)\.\s+(\w+)
```

- `(?:Mr|Mrs|Ms)` - Non-capturing group (title)
- `\.` - Literal dot
- `\s+` - One or more spaces
- `(\w+)` - Capturing group (name)

**Match:** "Mr. John Smith"

**Captured Groups:**
- Group 1: "John" (title not captured)

### Comparison

```
(Mr|Mrs|Ms)\.\s+(\w+)     # Title captured as Group 1, name as Group 2
(?:Mr|Mrs|Ms)\.\s+(\w+)   # Only name captured as Group 1
```

## Named Groups

### Syntax: `(?P<name>pattern)` (Python) or `(?<name>pattern)` (JavaScript)

Named groups make your regex more readable and maintainable.

### Python Example

```python
import re

pattern = r'(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})'
text = "Date: 25/12/2023"

match = re.search(pattern, text)
if match:
    day = match.group('day')      # "25"
    month = match.group('month')  # "12"
    year = match.group('year')    # "2023"
```

### JavaScript Example

```javascript
const pattern = /(?<day>\d{2})\/(?<month>\d{2})\/(?<year>\d{4})/;
const text = "Date: 25/12/2023";

const match = text.match(pattern);
if (match) {
    const { day, month, year } = match.groups;
    console.log(`Day: ${day}, Month: ${month}, Year: ${year}`);
}
```

## Group Numbering

Groups are numbered from left to right, starting at 1 (group 0 is the entire match).

### Example

```
(\d{2})-(\d{2})-(\d{4})
```

**Match:** "25-12-2023"

- Group 0: "25-12-2023" (entire match)
- Group 1: "25"
- Group 2: "12"
- Group 3: "2023"

### Nested Groups

```
((\d{2})-(\d{2}))-(\d{4})
```

**Match:** "25-12-2023"

- Group 0: "25-12-2023" (entire match)
- Group 1: "25-12" (outer group)
- Group 2: "25" (inner group)
- Group 3: "12" (inner group)
- Group 4: "2023"

## Quantifiers with Groups

Groups allow you to apply quantifiers to multiple characters.

### Examples

```
(abc){2,3}          # "abc" repeated 2-3 times
(\d{3}-){2}\d{4}    # Phone format: XXX-XXX-XXXX
([a-z]+\.){2}com    # Domain: something.something.com
```

### Practical Example: Phone Number

```
(\d{3}-){2}\d{4}
```

- `(\d{3}-)` - Group: 3 digits + hyphen
- `{2}` - Repeat group twice
- `\d{4}` - 4 digits

**Matches:**
- ✅ "123-456-7890"
- ❌ "123-456" (incomplete)

## Alternation with Groups

### Syntax: `(option1|option2|option3)`

Groups enable alternation (OR logic).

### Example

```
(cat|dog|bird)
```

**Matches:**
- ✅ "cat"
- ✅ "dog"
- ✅ "bird"
- ❌ "fish"

### With Quantifiers

```
(cat|dog)+
```

**Matches:**
- ✅ "cat"
- ✅ "dog"
- ✅ "catdog"
- ✅ "dogcatdog"

### Practical: File Extensions

```
\.(jpg|jpeg|png|gif)$
```

**Matches:**
- ✅ ".jpg"
- ✅ ".jpeg"
- ✅ ".png"
- ❌ ".txt"

## Practical Examples

### Example 1: Extract Email Components

```
(\w+)@(\w+\.\w+)
```

**Match:** "user@example.com"

- Group 1: "user" (local part)
- Group 2: "example.com" (domain)

### Example 2: Parse Log Entry

```
(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)
```

**Match:** "2023-12-25 10:30:45 ERROR Database connection failed"

- Group 1: "2023-12-25" (date)
- Group 2: "10:30:45" (time)
- Group 3: "ERROR" (level)
- Group 4: "Database connection failed" (message)

### Example 3: Extract URL Components

```
(https?)://([\w\.-]+)(/.*)?
```

**Match:** "https://www.example.com/path/to/page"

- Group 1: "https" (protocol)
- Group 2: "www.example.com" (domain)
- Group 3: "/path/to/page" (path)

## Common Patterns

### Extract Domain from URL

```
https?://(?:www\.)?([^/]+)
```

### Parse Name (First Last)

```
(\w+)\s+(\w+)
```

### Extract Phone Area Code

```
\((\d{3})\)
```

### Match Repeated Words

```
\b(\w+)\s+\1\b
```

(Note: `\1` is a backreference - see advanced section)

## Tips and Best Practices

1. **Use non-capturing groups** when you don't need the captured text
2. **Use named groups** for better readability
3. **Be aware of group numbering** - it changes when you add/remove groups
4. **Test group extraction** - verify you're capturing the right parts
5. **Consider performance** - fewer captures can improve speed
6. **Document complex patterns** - groups can make regex hard to read

## Exercises

Try these:

1. Create a group to match "Mr." or "Mrs." or "Ms.": `_____`
2. Extract the username from "user@example.com": `_____`
3. Match "hello" repeated 2-3 times: `_____`
4. Extract area code from "(123) 456-7890": `_____`
5. Match file extensions: jpg, png, gif: `_____`

---

**Next:** [lookaheads-lookbehinds.md](lookaheads-lookbehinds.md) for advanced matching!

