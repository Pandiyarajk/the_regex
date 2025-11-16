# Introduction to Regular Expressions

## What is Regex?

**Regular Expressions (Regex)** are powerful pattern-matching tools used to search, match, and manipulate text. Think of them as a supercharged "Find" feature that can match complex patterns, not just exact text.

A regex is a sequence of characters that forms a search pattern. This pattern can be used to:
- Find specific text in a document
- Validate input (emails, phone numbers, etc.)
- Extract information from text
- Replace text based on patterns
- Parse structured data

### Example

Instead of searching for exact text like "hello", regex allows you to search for patterns like:
- All words starting with "h"
- All phone numbers
- All email addresses
- All dates in a specific format

## Why & Where is Regex Used?

### Common Use Cases

1. **Form Validation**
   - Email addresses
   - Phone numbers
   - Passwords
   - Credit card numbers
   - Postal codes

2. **Text Processing**
   - Find and replace operations
   - Data extraction
   - Text parsing
   - Log file analysis

3. **Web Development**
   - URL routing
   - Input sanitization
   - Data extraction from HTML
   - API endpoint matching

4. **Data Science**
   - Cleaning datasets
   - Extracting patterns from text
   - Log analysis
   - Text mining

5. **System Administration**
   - Log file parsing
   - Configuration file processing
   - Search and replace in files
   - Pattern matching in scripts

### Real-World Examples

- **Email Validation**: Check if user input matches email format
- **Log Parsing**: Extract IP addresses, timestamps, and error messages
- **Web Scraping**: Find URLs, phone numbers, or specific content
- **Code Search**: Find function definitions, variable names, or patterns
- **Data Cleaning**: Remove unwanted characters, format data consistently

## Regex Engines

Different programming languages and tools use different regex engines. Understanding these differences helps you write compatible patterns.

### PCRE (Perl Compatible Regular Expressions)

- Used in: PHP, Python (with `regex` module), many text editors
- Features: Very powerful, supports advanced features
- Example: `(?P<name>pattern)` for named groups

### JavaScript Regex Engine

- Used in: JavaScript, Node.js
- Features: ECMAScript standard, some limitations
- Example: `/pattern/flags` syntax

### Python `re` Module

- Used in: Python
- Features: PCRE-like, but with some differences
- Example: `re.search(pattern, text)`

### Other Engines

- **POSIX**: Basic regex support
- **Vim**: Extended regex with Vim-specific features
- **Grep**: Basic to extended regex depending on flags

### Important Notes

- **Not all features work the same** across engines
- **Test your patterns** in the target environment
- **Be aware of escaping** differences (e.g., `\d` vs `[0-9]`)
- **Flags/Modifiers** vary by engine (case-insensitive, multiline, etc.)

## Basic Concepts

### Literal Characters

The simplest regex pattern matches literal characters:

```
hello
```

This matches the exact text "hello" in a string.

### Meta Characters

Special characters that have meaning in regex:

- `.` - Matches any single character (except newline)
- `^` - Start of string/line
- `$` - End of string/line
- `*` - Zero or more of preceding element
- `+` - One or more of preceding element
- `?` - Zero or one of preceding element
- `[]` - Character class (matches any one character inside)
- `()` - Grouping
- `|` - Alternation (OR)
- `\` - Escape character

### Pattern Matching Process

1. **Compile**: The regex engine compiles your pattern
2. **Search**: It searches through the text
3. **Match**: When a match is found, it returns the result
4. **Continue**: It may continue searching for more matches

## Getting Started

### Your First Regex

Let's start with a simple example:

**Pattern**: `cat`

**Matches**: 
- ✅ "I have a cat"
- ✅ "category"
- ✅ "scatter"
- ❌ "dog"

This matches the literal text "cat" anywhere in the string.

### Testing Regex

Before writing complex patterns, always test them! Use:
- Online tools: regex101.com, regexr.com
- Your programming language's regex tester
- Command-line tools: `grep`, `sed`

## Next Steps

Now that you understand what regex is and why it's useful, let's dive into the syntax:

1. Read [syntax-cheatsheet.md](syntax-cheatsheet.md) for a quick reference
2. Try [simple-examples.md](simple-examples.md) to see regex in action
3. Practice with [exercises-basic.md](exercises-basic.md)
4. Test your knowledge with [quiz-basic.md](quiz-basic.md)

## Key Takeaways

- ✅ Regex is a pattern-matching language for text
- ✅ It's used everywhere: validation, parsing, searching, replacing
- ✅ Different engines have different features
- ✅ Always test your patterns
- ✅ Start simple, build complexity gradually

---

**Ready to learn the syntax?** → [syntax-cheatsheet.md](syntax-cheatsheet.md)

