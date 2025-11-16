# Regex Syntax Cheatsheet

A quick reference guide for basic regex syntax and meta characters.

## Meta Characters

### Anchors

| Symbol | Name | Description | Example |
|--------|------|-------------|---------|
| `^` | Caret | Start of string/line | `^Hello` matches "Hello" at start |
| `$` | Dollar | End of string/line | `world$` matches "world" at end |
| `\b` | Word boundary | Boundary between word and non-word | `\bcat\b` matches "cat" as whole word |
| `\B` | Non-word boundary | Not a word boundary | `\Bcat\B` matches "cat" inside words |

### Character Classes

| Symbol | Name | Description | Example |
|--------|------|-------------|---------|
| `.` | Dot | Any single character (except newline) | `c.t` matches "cat", "cot", "cut" |
| `[abc]` | Character class | Matches any one character inside | `[aeiou]` matches any vowel |
| `[^abc]` | Negated class | Matches any character NOT inside | `[^aeiou]` matches non-vowels |
| `[a-z]` | Range | Matches any character in range | `[0-9]` matches any digit |
| `\d` | Digit | Matches any digit (0-9) | Equivalent to `[0-9]` |
| `\D` | Non-digit | Matches any non-digit | Equivalent to `[^0-9]` |
| `\w` | Word character | Matches letter, digit, underscore | Equivalent to `[a-zA-Z0-9_]` |
| `\W` | Non-word character | Matches non-word character | Opposite of `\w` |
| `\s` | Whitespace | Matches space, tab, newline, etc. | `\s+` matches one or more spaces |
| `\S` | Non-whitespace | Matches non-whitespace | Opposite of `\s` |

### Quantifiers

| Symbol | Name | Description | Example |
|--------|------|-------------|---------|
| `*` | Asterisk | Zero or more of preceding | `a*` matches "", "a", "aa", "aaa" |
| `+` | Plus | One or more of preceding | `a+` matches "a", "aa", "aaa" |
| `?` | Question mark | Zero or one of preceding | `colou?r` matches "color" or "colour" |
| `{n}` | Exact count | Exactly n occurrences | `\d{3}` matches exactly 3 digits |
| `{n,}` | At least n | n or more occurrences | `\d{3,}` matches 3+ digits |
| `{n,m}` | Range | Between n and m occurrences | `\d{2,4}` matches 2-4 digits |

### Groups and Alternation

| Symbol | Name | Description | Example |
|--------|------|-------------|---------|
| `()` | Group | Captures group for backreference | `(abc)` captures "abc" |
| `(?:)` | Non-capturing group | Groups without capturing | `(?:abc)` groups but doesn't capture |
| `\|` | Pipe | Alternation (OR) | `cat\|dog` matches "cat" or "dog" |

### Escaping

| Symbol | Description | Example |
|--------|-------------|---------|
| `\` | Escape special characters | `\.` matches literal dot |
| `\\` | Match literal backslash | `\\` matches "\" |

## Common Patterns

### Numbers

```
\d+           # One or more digits
\d{3}         # Exactly 3 digits
\d{1,3}       # 1 to 3 digits
\d{3,}        # 3 or more digits
```

### Words

```
\w+           # One or more word characters
\b\w+\b       # Whole word
[a-zA-Z]+     # Letters only (no digits)
```

### Whitespace

```
\s+           # One or more whitespace characters
\s{2,}        # Two or more spaces
[ \t]+        # Spaces and tabs only
```

### Common Validations

```
^[a-zA-Z]+$           # Letters only (entire string)
^\d+$                 # Digits only (entire string)
^[a-zA-Z0-9]+$        # Alphanumeric only
^.{3,}$               # At least 3 characters
```

## Flags/Modifiers

Different engines use different syntax, but common flags include:

| Flag | Name | Description |
|------|------|-------------|
| `i` | Case-insensitive | `/[a-z]/i` matches "A" and "a" |
| `g` | Global | Find all matches, not just first |
| `m` | Multiline | `^` and `$` match line boundaries |
| `s` | Dotall | `.` matches newline too |
| `x` | Extended | Ignore whitespace, allow comments |

## Escaping Special Characters

To match literal special characters, escape them with `\`:

```
\.            # Literal dot
\*            # Literal asterisk
\+            # Literal plus
\?            # Literal question mark
\(            # Literal opening parenthesis
\)            # Literal closing parenthesis
\[            # Literal opening bracket
\]            # Literal closing bracket
\{            # Literal opening brace
\}            # Literal closing brace
\^            # Literal caret
\$            # Literal dollar
\|            # Literal pipe
\\            # Literal backslash
```

## Precedence

Regex operators have precedence (order of evaluation):

1. **Escaping** (`\`)
2. **Groups** (`()`)
3. **Quantifiers** (`*`, `+`, `?`, `{}`)
4. **Anchors** (`^`, `$`)
5. **Alternation** (`|`)

### Example

```
^cat|dog$     # Matches "cat" at start OR "dog" at end
^(cat|dog)$   # Matches entire string as "cat" OR "dog"
```

## Quick Tips

1. **Use anchors** (`^` and `$`) when you want to match the entire string
2. **Escape special characters** when you want literal matches
3. **Use character classes** (`[]`) for matching specific sets
4. **Quantifiers are greedy** by default (match as much as possible)
5. **Test your patterns** before using them in production

## Practice

Try these patterns:

```
^Hello        # Matches "Hello" at start
world$        # Matches "world" at end
^Hello world$ # Matches entire string exactly
\d{3}-\d{4}   # Matches phone format like "123-4567"
[a-z]+@[a-z]+\.com  # Simple email pattern
```

---

**Next:** [simple-examples.md](simple-examples.md) for hands-on examples!

