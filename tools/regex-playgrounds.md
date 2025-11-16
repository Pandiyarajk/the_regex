# Regex Playgrounds and Testing Environments

Interactive environments for testing and learning regular expressions.

## Online Playgrounds

### 1. Regex101
**URL:** https://regex101.com/

**Supported Engines:**
- PCRE (PHP)
- JavaScript
- Python
- Go
- Java

**Features:**
- Real-time pattern explanation
- Match information
- Code generator
- Unit test generator
- Community patterns

**Best Use Cases:**
- Learning regex syntax
- Debugging complex patterns
- Generating code snippets
- Understanding pattern behavior

---

### 2. Regexr
**URL:** https://regexr.com/

**Supported Engines:**
- JavaScript
- PHP/PCRE

**Features:**
- Interactive reference
- Cheat sheet
- Community patterns
- Text highlighting
- Match details

**Best Use Cases:**
- Quick pattern testing
- Reference lookup
- JavaScript regex development

---

### 3. Debuggex
**URL:** https://www.debuggex.com/

**Supported Engines:**
- Python
- JavaScript
- PCRE

**Features:**
- Visual regex diagram
- Step-by-step matching
- Backtracking visualization
- Error detection

**Best Use Cases:**
- Understanding regex execution
- Debugging complex patterns
- Learning how engines work
- Visualizing pattern structure

---

### 4. Regex Storm
**URL:** https://regexstorm.net/

**Supported Engines:**
- .NET

**Features:**
- .NET regex testing
- Match highlighting
- Group capturing
- Replace functionality

**Best Use Cases:**
- .NET development
- C# regex testing

---

### 5. Pythex
**URL:** https://pythex.org/

**Supported Engines:**
- Python

**Features:**
- Python-specific testing
- Match groups display
- Quick reference
- Simple interface

**Best Use Cases:**
- Python regex development
- Quick pattern testing

---

## Browser-Based Testing

### Browser Console

**Chrome/Edge DevTools:**
```javascript
// Test regex in console
const pattern = /\d{3}-\d{3}-\d{4}/;
const text = "Call 123-456-7890";
console.log(pattern.test(text));  // true
console.log(text.match(pattern));  // ["123-456-7890"]
```

**Firefox Console:**
```javascript
// Similar to Chrome
const pattern = /\d{3}-\d{3}-\d{4}/;
const text = "Call 123-456-7890";
pattern.test(text);  // true
```

---

## IDE Integration

### VS Code

**Extensions:**
- **Regex Previewer** - Side-by-side regex testing
- **Regex Tester** - Inline pattern testing
- **Regex** - Syntax highlighting

**Usage:**
1. Install Regex Previewer extension
2. Open regex pattern file
3. Use Ctrl+Alt+M (Cmd+Alt+M on Mac) to open preview
4. Test patterns in real-time

---

### IntelliJ IDEA / PyCharm

**Built-in Features:**
- Regex tester in Find/Replace dialog
- Pattern validation
- Match highlighting
- Code completion

**Usage:**
1. Open Find/Replace (Ctrl+R / Cmd+R)
2. Enable regex mode (.* icon)
3. Enter pattern
4. See matches highlighted

---

### Sublime Text

**Built-in Features:**
- Regex support in Find/Replace
- Pattern highlighting
- Match preview

**Usage:**
1. Open Find (Ctrl+F / Cmd+F)
2. Enable regex mode (.* icon)
3. Enter pattern
4. Navigate through matches

---

## Command-Line Testing

### Interactive Python

```python
python3
>>> import re
>>> pattern = r'\d{3}-\d{3}-\d{4}'
>>> text = "Call 123-456-7890"
>>> re.search(pattern, text)
<re.Match object; span=(5, 17), match='123-456-7890'>
>>> re.findall(pattern, text)
['123-456-7890']
```

### Node.js REPL

```javascript
node
> const pattern = /\d{3}-\d{3}-\d{4}/;
> const text = "Call 123-456-7890";
> pattern.test(text)
true
> text.match(pattern)
[ '123-456-7890', index: 5, input: 'Call 123-456-7890', groups: undefined ]
```

### ripgrep Interactive

```bash
# Interactive search
rg "pattern" --interactive

# Test pattern on file
rg "pattern" file.txt

# Test with multiple files
rg "pattern" *.txt
```

---

## Mobile Apps

### iOS Apps

1. **RegEx** - Regex tester and reference
2. **Regex Tester** - Pattern testing app
3. **RegEx Lab** - Advanced regex testing

### Android Apps

1. **Regex Tester** - Test patterns on mobile
2. **RegEx Helper** - Reference and testing
3. **Regex Tools** - Pattern builder and tester

---

## Specialized Tools

### 1. Regex Crossword
**URL:** https://regexcrossword.com/

**Purpose:** Learn regex through puzzles

**Features:**
- Interactive crossword puzzles
- Progressive difficulty
- Pattern explanations
- Fun learning approach

---

### 2. Regex Golf
**URL:** https://alf.nu/RegexGolf

**Purpose:** Optimize regex patterns

**Features:**
- Challenge-based learning
- Pattern optimization
- Score tracking
- Competitive element

---

### 3. Regex Crossword (Alternative)
**URL:** https://regexcrossword.com/challenges/intermediate/puzzles/1

**Purpose:** Practice through challenges

---

## Testing Workflow Recommendations

### For Learning
1. Start with **Regex101** for explanations
2. Use **Debuggex** to visualize patterns
3. Practice with **RegexOne** tutorials
4. Test in **browser console** for quick checks

### For Development
1. Use **IDE plugins** for quick testing
2. Test in **language REPL** for accuracy
3. Use **Regex101** for complex debugging
4. Validate with **unit tests**

### For Production
1. Test with **real data samples**
2. Use **language-specific testers**
3. Check **performance** with large inputs
4. Validate **edge cases**

---

## Quick Testing Scripts

### Python Test Script

```python
#!/usr/bin/env python3
import re
import sys

def test_pattern(pattern, test_strings):
    compiled = re.compile(pattern)
    print(f"Pattern: {pattern}\n")
    for test in test_strings:
        match = compiled.search(test)
        result = "✓" if match else "✗"
        print(f"{result} {test}")
        if match:
            print(f"  Match: {match.group()}")
    print()

# Usage
test_pattern(r'\d{3}-\d{3}-\d{4}', [
    "Call 123-456-7890",
    "No phone here",
    "123-456-7890 is the number"
])
```

### JavaScript Test Script

```javascript
function testPattern(pattern, testStrings) {
    const regex = new RegExp(pattern);
    console.log(`Pattern: ${pattern}\n`);
    testStrings.forEach(test => {
        const match = regex.test(test);
        const result = match ? "✓" : "✗";
        console.log(`${result} ${test}`);
        if (match) {
            const fullMatch = test.match(regex);
            console.log(`  Match: ${fullMatch[0]}`);
        }
    });
    console.log();
}

// Usage
testPattern('\\d{3}-\\d{3}-\\d{4}', [
    "Call 123-456-7890",
    "No phone here",
    "123-456-7890 is the number"
]);
```

---

## Tips for Effective Testing

1. **Test with various inputs** - valid and invalid
2. **Check edge cases** - empty strings, boundaries
3. **Test performance** - large texts, complex patterns
4. **Verify across engines** - if supporting multiple languages
5. **Document test cases** - keep examples for future reference
6. **Use real data** - test with actual production-like data

---

## Recommended Setup

**For Beginners:**
- Regex101 (learning)
- Browser console (quick tests)
- RegexOne (tutorials)

**For Developers:**
- IDE plugin (VS Code Regex Previewer)
- Language REPL (Python/Node.js)
- Regex101 (debugging)

**For Advanced Users:**
- Debuggex (visualization)
- Command-line tools (ripgrep, grep)
- Custom test scripts

---

**Next:** Check [recommended-tools.md](recommended-tools.md) for more tool recommendations

