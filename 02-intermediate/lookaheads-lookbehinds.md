# Lookaheads and Lookbehinds

Lookaheads and lookbehinds are **zero-width assertions** - they check for patterns without consuming characters. They're powerful tools for complex matching scenarios.

## What Are Lookarounds?

Lookarounds allow you to:
- Match a pattern only if it's followed by another pattern (lookahead)
- Match a pattern only if it's preceded by another pattern (lookbehind)
- Match a pattern only if it's NOT followed/preceded by another pattern (negative)

**Key Point:** Lookarounds don't consume characters - they just "peek" ahead or behind.

## Positive Lookahead

### Syntax: `(?=pattern)`

Matches a position where the pattern **follows** the current position.

### Example: Password with Number

```
\w+(?=\d)
```

**Matches:** "password123"
- `\w+` matches "password"
- `(?=\d)` checks that a digit follows (but doesn't consume it)

**Result:** Matches "password" (not "password123")

### Practical Example: Extract Words Before "is"

```
\w+(?=\s+is\b)
```

**Text:** "The cat is sleeping"

**Matches:** "cat" (followed by " is")

### Code Example

**Python:**
```python
import re

pattern = r'\w+(?=\s+is\b)'
text = "The cat is sleeping"
match = re.search(pattern, text)
print(match.group())  # "cat"
```

**JavaScript:**
```javascript
const pattern = /\w+(?=\s+is\b)/;
const text = "The cat is sleeping";
const match = text.match(pattern);
console.log(match[0]); // "cat"
```

## Negative Lookahead

### Syntax: `(?!pattern)`

Matches a position where the pattern does **NOT** follow.

### Example: Word Not Followed by "ing"

```
\w+(?!ing\b)
```

**Text:** "running jumping walk"

**Matches:**
- ✅ "jumping" (not followed by "ing")
- ✅ "walk" (not followed by "ing")
- ❌ "running" (followed by "ing")

### Practical: Extract Non-HTML Tags

```
<(?!/)[^>]+>
```

**Matches:** HTML tags but not closing tags
- `<` - Opening bracket
- `(?!/)` - Not followed by `/`
- `[^>]+` - One or more non-`>` characters
- `>` - Closing bracket

## Positive Lookbehind

### Syntax: `(?<=pattern)` (Python) or `(?<=pattern)` (JavaScript)

Matches a position where the pattern **precedes** the current position.

**Note:** Lookbehind patterns usually need fixed length in some engines.

### Example: Extract Amount After "$"

```
(?<=\$)\d+
```

**Text:** "Price is $100"

**Matches:** "100" (preceded by "$")

### Practical: Extract Domain from URL

```
(?<=://)[^/]+
```

**Text:** "https://www.example.com/path"

**Matches:** "www.example.com" (preceded by "://")

### Code Example

**Python:**
```python
import re

pattern = r'(?<=\$)\d+'
text = "Price is $100 and $50"
matches = re.findall(pattern, text)
print(matches)  # ['100', '50']
```

**JavaScript:**
```javascript
const pattern = /(?<=\$)\d+/g;
const text = "Price is $100 and $50";
const matches = text.match(pattern);
console.log(matches); // ['100', '50']
```

## Negative Lookbehind

### Syntax: `(?<!pattern)`

Matches a position where the pattern does **NOT** precede.

### Example: Number Not Preceded by "$"

```
(?<!\$)\d+
```

**Text:** "Price is $100 and 50 dollars"

**Matches:**
- ✅ "50" (not preceded by "$")
- ❌ "100" (preceded by "$")

### Practical: Find Unquoted Words

```
(?<!")[a-z]+(?!")
```

**Text:** "hello "world" test"

**Matches:** "hello" and "test" (not quoted)

## Combining Lookarounds

You can combine multiple lookarounds for complex conditions.

### Example: Extract Number Between "$" and "."

```
(?<=\$)\d+(?=\.)
```

**Text:** "Price is $100.50"

**Matches:** "100" (preceded by "$", followed by ".")

### Example: Word Surrounded by Spaces

```
(?<=\s)\w+(?=\s)
```

**Text:** "hello world test"

**Matches:** "world" (surrounded by spaces)

## Practical Examples

### Example 1: Validate Password Requirements

Requirement: Password must contain a digit, but we want to match the whole password.

```
^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$
```

- `^` - Start of string
- `(?=.*\d)` - Lookahead: contains a digit
- `(?=.*[a-z])` - Lookahead: contains lowercase
- `(?=.*[A-Z])` - Lookahead: contains uppercase
- `.{8,}` - At least 8 characters
- `$` - End of string

**Matches:**
- ✅ "Password123"
- ❌ "password" (no uppercase, no digit)
- ❌ "PASS123" (no lowercase)

### Example 2: Extract Words in Quotes

```
(?<=")[^"]+(?=")
```

**Text:** 'He said "hello world" and left'

**Matches:** "hello world" (between quotes)

### Example 3: Find Overlapping Matches

Regex normally doesn't find overlapping matches, but lookarounds can help:

```
(?=(\d{3}))
```

**Text:** "12345"

**Matches:** Positions before "123", "234", "345"

### Example 4: Validate Email (Better Pattern)

```
^[a-zA-Z0-9._%+-]+@(?=[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$
```

This ensures the domain part has a valid TLD.

## Common Patterns

### Extract Text Between Tags

```
(?<=<tag>).*?(?=</tag>)
```

### Find Words Not at Start/End

```
(?<=\s)\w+(?=\s)
```

### Validate Phone Format

```
^(?=\d{10}$)\d{3}-\d{3}-\d{4}$
```

### Extract Domain from Email

```
(?<=@)[^.]+
```

## Limitations and Considerations

### Fixed-Length Lookbehind

Some engines (like JavaScript) require fixed-length patterns in lookbehind:

```
(?<=abc)     ✅ Fixed length
(?<=ab|c)    ✅ Fixed length (alternatives)
(?<=a+)      ❌ Variable length (may not work)
(?<=a{2,5})  ❌ Variable length (may not work)
```

### Performance

Lookarounds can be slower than regular matching. Use them when necessary, but consider alternatives.

### Readability

Complex lookarounds can be hard to read. Consider:
- Adding comments
- Breaking into multiple patterns
- Using named groups

## Tips and Best Practices

1. **Use lookarounds sparingly** - they can make patterns complex
2. **Test thoroughly** - lookarounds behave differently across engines
3. **Consider alternatives** - sometimes simpler patterns work better
4. **Document complex patterns** - explain what each lookaround does
5. **Be aware of engine limitations** - check your language's support

## Exercises

Try these:

1. Match a word followed by "ing": `_____`
2. Extract number after "$" but before ".": `_____`
3. Find words not at the start of line: `_____`
4. Match password with digit and special char: `_____`
5. Extract text between HTML tags: `_____`

---

**Next:** [medium-examples.md](medium-examples.md) for practical applications!

