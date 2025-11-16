# Recommended Regex Tools

A curated list of tools to help you learn, test, and master regular expressions.

## Online Regex Testers

### 1. Regex101
**URL:** https://regex101.com/

**Features:**
- Real-time pattern testing
- Explanation of regex patterns
- Code generation for multiple languages
- Match highlighting
- PCRE, JavaScript, Python, Go support
- Detailed error messages

**Best for:** Learning and debugging patterns

---

### 2. Regexr
**URL:** https://regexr.com/

**Features:**
- Interactive regex testing
- Reference guide built-in
- Community patterns library
- Cheat sheet
- JavaScript and PHP support

**Best for:** Quick testing and reference

---

### 3. RegexOne
**URL:** https://regexone.com/

**Features:**
- Interactive tutorials
- Step-by-step lessons
- Practice exercises
- Pattern explanations

**Best for:** Learning regex from scratch

---

### 4. Debuggex
**URL:** https://www.debuggex.com/

**Features:**
- Visual regex debugger
- Regex diagram visualization
- Step-by-step matching explanation
- Python, JavaScript, PCRE support

**Best for:** Understanding how regex engines work

---

### 5. RegEx Pal
**URL:** https://www.regexpal.com/

**Features:**
- Simple, clean interface
- Real-time matching
- JavaScript regex support

**Best for:** Quick pattern testing

---

## Desktop Applications

### 1. RegexBuddy
**Platform:** Windows, Mac, Linux

**Features:**
- Advanced regex testing
- Code generation
- Library of regex patterns
- Debugging tools
- Multiple engine support

**Best for:** Professional regex development

---

### 2. Expresso
**Platform:** Windows

**Features:**
- .NET regex testing
- Visual regex builder
- Pattern library
- Code generation

**Best for:** .NET developers

---

## Command-Line Tools

### 1. grep
**Platform:** Unix/Linux/Mac

**Usage:**
```bash
grep -E "pattern" file.txt
grep -P "pattern" file.txt  # Perl-compatible (GNU grep)
```

**Features:**
- Built into most Unix systems
- Fast text searching
- Multiple regex flavors

---

### 2. ripgrep (rg)
**Platform:** Cross-platform

**Installation:**
```bash
# macOS
brew install ripgrep

# Linux
sudo apt install ripgrep

# Windows
choco install ripgrep
```

**Usage:**
```bash
rg "pattern" file.txt
rg -i "pattern" .  # Case-insensitive, recursive
```

**Features:**
- Extremely fast
- Recursive directory search
- Colored output
- Respects .gitignore

---

### 3. sed
**Platform:** Unix/Linux/Mac

**Usage:**
```bash
sed -E 's/pattern/replacement/g' file.txt
```

**Features:**
- Stream editor
- Pattern substitution
- In-place editing

---

### 4. awk
**Platform:** Unix/Linux/Mac

**Usage:**
```bash
awk '/pattern/ { print }' file.txt
```

**Features:**
- Pattern matching
- Text processing
- Data extraction

---

## Browser Extensions

### 1. RegExp Tester (Chrome)
**Features:**
- Test regex in browser console
- Visual highlighting
- Multiple flags support

---

### 2. Regex Tester (Firefox)
**Features:**
- Built-in regex testing
- Pattern validation
- Match highlighting

---

## IDE Plugins

### 1. VS Code Extensions
- **Regex Previewer** - Visual regex testing
- **Regex Tester** - Test patterns in editor
- **Regex** - Syntax highlighting

### 2. IntelliJ IDEA / PyCharm
- Built-in regex tester
- Pattern validation
- Code completion for regex

### 3. Sublime Text
- **RegReplace** - Advanced find/replace with regex
- Built-in regex support

---

## Mobile Apps

### 1. RegEx (iOS)
**Features:**
- Test regex patterns
- Reference guide
- Examples library

### 2. Regex Tester (Android)
**Features:**
- Pattern testing
- Match highlighting
- Reference materials

---

## Learning Resources

### 1. Regex Crossword
**URL:** https://regexcrossword.com/

**Features:**
- Learn regex through puzzles
- Interactive challenges
- Progressive difficulty

**Best for:** Fun way to learn regex

---

### 2. Regex Golf
**URL:** https://alf.nu/RegexGolf

**Features:**
- Challenge-based learning
- Pattern optimization
- Competitive element

**Best for:** Advanced practice

---

## Libraries and Frameworks

### Python
- **`re`** - Built-in module
- **`regex`** - Advanced regex (PCRE support)
- **`re2`** - Fast regex engine

### JavaScript
- Built-in `RegExp` object
- **XRegExp** - Extended regex features

### Other Languages
- **Perl** - Original regex implementation
- **PCRE** - Perl Compatible Regular Expressions
- **Oniguruma** - Ruby's regex engine

---

## Tips for Choosing Tools

1. **For Learning:** Start with Regex101 or RegexOne
2. **For Quick Testing:** Use Regexr or RegEx Pal
3. **For Debugging:** Use Debuggex for visualization
4. **For Production:** Use language-specific libraries
5. **For Command Line:** Use grep, ripgrep, or sed

---

## Best Practices

1. **Always test your patterns** before using in production
2. **Use online testers** for learning and debugging
3. **Test with various inputs** - valid and invalid cases
4. **Check engine compatibility** - different engines have differences
5. **Document your patterns** - explain complex regex
6. **Consider performance** - some patterns can be slow

---

## Quick Reference

### Most Popular Tools
1. **Regex101** - Best overall
2. **Regexr** - Quick testing
3. **Debuggex** - Visualization
4. **RegexOne** - Learning

### Command Line
1. **ripgrep** - Fastest
2. **grep** - Most common
3. **sed** - Substitution

---

**Next:** [regex-playgrounds.md](regex-playgrounds.md) for more testing environments

