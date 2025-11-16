# Character Classes

Character classes allow you to match any one character from a set of characters. They're one of the most powerful and commonly used regex features.

## Basic Character Classes

### Syntax: `[characters]`

Matches any **one** character from the set inside the brackets.

### Examples

```
[aeiou]        # Matches any vowel
[0123456789]   # Matches any digit
[abc]          # Matches 'a', 'b', or 'c'
```

### In Text

```
"hello" → [aeiou] matches: 'e', 'o'
"123"   → [0123456789] matches: '1', '2', '3'
"cat"   → [abc] matches: 'c', 'a'
```

## Character Ranges

### Syntax: `[start-end]`

Use a hyphen to specify a range of characters.

### Common Ranges

```
[a-z]          # Lowercase letters a to z
[A-Z]          # Uppercase letters A to Z
[0-9]          # Digits 0 to 9
[a-zA-Z]       # All letters (lowercase and uppercase)
[0-9a-f]       # Hexadecimal digits
```

### Examples

```
"Hello123" → [a-z] matches: 'e', 'l', 'l', 'o'
"Hello123" → [A-Z] matches: 'H'
"Hello123" → [0-9] matches: '1', '2', '3'
"Hello123" → [a-zA-Z] matches: 'H', 'e', 'l', 'l', 'o'
```

## Negated Character Classes

### Syntax: `[^characters]`

The `^` inside `[]` negates the character class - matches any character **NOT** in the set.

### Examples

```
[^aeiou]       # Matches any non-vowel
[^0-9]         # Matches any non-digit
[^a-z]         # Matches any character not lowercase
```

### In Text

```
"hello" → [^aeiou] matches: 'h', 'l', 'l'
"abc123" → [^0-9] matches: 'a', 'b', 'c'
"Hello" → [^a-z] matches: 'H'
```

## Predefined Character Classes (Shorthand)

Most regex engines provide shorthand for common character classes.

### Digits

```
\d              # Matches any digit [0-9]
\D              # Matches any non-digit [^0-9]
```

### Word Characters

```
\w              # Matches word character [a-zA-Z0-9_]
\W              # Matches non-word character [^a-zA-Z0-9_]
```

**Note:** `\w` includes:
- Letters (a-z, A-Z)
- Digits (0-9)
- Underscore (_)

### Whitespace

```
\s              # Matches whitespace (space, tab, newline, etc.)
\S              # Matches non-whitespace
```

**Whitespace includes:**
- Space (` `)
- Tab (`\t`)
- Newline (`\n`)
- Carriage return (`\r`)
- Form feed (`\f`)
- Vertical tab (`\v`)

## Combining Character Classes

You can combine multiple character classes and ranges.

### Examples

```
[a-zA-Z0-9]    # Alphanumeric characters
[a-z0-9._-]    # Lowercase letters, digits, dot, underscore, hyphen
[^a-zA-Z]      # Non-letter characters
[\d\s]         # Digits or whitespace
```

## Special Characters in Character Classes

Most special regex characters lose their special meaning inside `[]`, but some still need attention.

### Characters That Lose Special Meaning

Inside `[]`, these characters are treated literally:
- `.` (dot)
- `*` (asterisk)
- `+` (plus)
- `?` (question mark)
- `{` `}` (braces)

### Characters That Keep Special Meaning

- `^` - Negation (only at the start)
- `-` - Range operator (unless escaped or at start/end)
- `]` - Closing bracket (must be escaped)
- `\` - Escape character

### Escaping in Character Classes

```
[\^\.]         # Matches literal '^' or '.'
[\-]           # Matches literal '-' (or place at start/end)
[\[\]]        # Matches '[' or ']'
[\\]           # Matches literal backslash
```

## Practical Examples

### Example 1: Match Hex Color Code

```
#[0-9a-fA-F]{6}
```

- `#` - Literal hash
- `[0-9a-fA-F]` - Hex digits
- `{6}` - Exactly 6 characters

**Matches:**
- ✅ "#FF5733"
- ✅ "#00ff00"
- ❌ "#GGG" (invalid hex)

### Example 2: Extract Words (Letters Only)

```
\b[a-zA-Z]+\b
```

- `\b` - Word boundary
- `[a-zA-Z]+` - One or more letters
- `\b` - Word boundary

**Matches:**
- ✅ "hello"
- ✅ "World"
- ❌ "user123" (contains digits)

### Example 3: Find Non-Alphanumeric Characters

```
[^a-zA-Z0-9]
```

**Matches:**
- ✅ "hello world" → matches space
- ✅ "user@email.com" → matches '@' and '.'
- ❌ "Hello123" → matches nothing

### Example 4: Match Valid Filename Characters

```
^[a-zA-Z0-9._-]+$
```

**Matches:**
- ✅ "file.txt"
- ✅ "my-file_123"
- ❌ "file name" (contains space)
- ❌ "file/name" (contains slash)

## Common Patterns

### Alphanumeric Username

```
^[a-zA-Z0-9_]{3,20}$
```

### Phone Number Digits Only

```
^\d{10}$
```

### Find All Vowels

```
[aeiouAEIOU]
```

### Match Consonants Only

```
[^aeiouAEIOU\s\d]
```

### Extract Numbers (Including Decimals)

```
\d+\.?\d*
```

## Tips and Best Practices

1. **Use ranges** for consecutive characters: `[a-z]` instead of `[abcdefghijklmnopqrstuvwxyz]`
2. **Combine ranges** for multiple sets: `[a-zA-Z0-9]`
3. **Use shorthand** when available: `\d` instead of `[0-9]`
4. **Be careful with negation**: `[^a-z]` matches many characters, not just uppercase
5. **Test edge cases**: Empty strings, special characters, Unicode
6. **Consider Unicode**: `[a-z]` may not match accented characters in some engines

## Unicode Considerations

Some regex engines support Unicode character classes:

```
\p{L}          # Any letter (Unicode)
\p{N}          # Any number (Unicode)
\p{Lu}         # Uppercase letter
\p{Ll}         # Lowercase letter
```

**Note:** Unicode support varies by engine. Check your language's documentation.

## Exercises

Try these patterns:

1. Match only uppercase letters: `_____`
2. Match any punctuation: `_____`
3. Match hexadecimal digits: `_____`
4. Match non-whitespace characters: `_____`
5. Match valid email local part characters: `_____`

---

**Next:** [grouping-capturing.md](grouping-capturing.md) to learn about groups!

