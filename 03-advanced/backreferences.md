# Backreferences

Backreferences allow you to refer to previously captured groups within the same regex pattern. They're powerful for matching repeated patterns and validating structured data.

## What Are Backreferences?

A backreference matches the same text that was matched by a capturing group earlier in the pattern.

### Syntax

- `\1` - Reference to group 1
- `\2` - Reference to group 2
- `\3` - Reference to group 3
- And so on...

**Note:** In some engines (like JavaScript), you might use `$1`, `$2` in replacement strings, but `\1`, `\2` in the pattern itself.

## Basic Backreferences

### Example 1: Repeated Words

```
\b(\w+)\s+\1\b
```

**Explanation:**
- `\b` - Word boundary
- `(\w+)` - Capture word (group 1)
- `\s+` - One or more spaces
- `\1` - Same text as group 1
- `\b` - Word boundary

**Matches:**
- ✅ "the the cat" → Matches "the the"
- ✅ "hello hello world" → Matches "hello hello"
- ❌ "the cat sat" → No match

### Code Examples

**Python:**
```python
import re

pattern = r'\b(\w+)\s+\1\b'
text = "the the cat sat on the the mat"
matches = re.findall(pattern, text)
print(matches)  # ['the', 'the']

# To find the actual matches
for match in re.finditer(pattern, text):
    print(match.group())  # "the the", "the the"
```

**JavaScript:**
```javascript
const pattern = /\b(\w+)\s+\1\b/g;
const text = "the the cat sat on the the mat";
const matches = text.match(pattern);
console.log(matches); // ['the the', 'the the']
```

## Multiple Backreferences

You can use multiple backreferences in a single pattern.

### Example: Matching HTML Tags

```
<(\w+)>.*?</\1>
```

**Explanation:**
- `<(\w+)>` - Opening tag, captures tag name (group 1)
- `.*?` - Lazy match for content
- `</\1>` - Closing tag, matches same tag name as group 1

**Matches:**
- ✅ "<div>content</div>"
- ✅ "<p>text</p>"
- ❌ "<div>content</span>" (mismatched tags)

### Code Example

**Python:**
```python
import re

pattern = r'<(\w+)>.*?</\1>'
text = "<div>Hello</div> and <p>World</p>"
matches = re.findall(pattern, text)
print(matches)  # ['div', 'p']

# To get full matches
for match in re.finditer(pattern, text):
    print(match.group())  # "<div>Hello</div>", "<p>World</p>"
```

## Named Group Backreferences

### Python: Named Groups

```
(?P<tag>\w+).*?(?P=tag)
```

**Explanation:**
- `(?P<tag>\w+)` - Named capturing group
- `.*?` - Content
- `(?P=tag)` - Backreference to named group

### JavaScript: Named Groups

```
(?<tag>\w+).*?\k<tag>
```

**Explanation:**
- `(?<tag>\w+)` - Named capturing group
- `.*?` - Content
- `\k<tag>` - Backreference to named group

### Code Examples

**Python:**
```python
import re

pattern = r'<(?P<tag>\w+)>.*?</(?P=tag)>'
text = "<div>content</div>"
match = re.search(pattern, text)
if match:
    print(match.group('tag'))  # "div"
```

**JavaScript:**
```javascript
const pattern = /<(?<tag>\w+)>.*?<\/\k<tag>>/;
const text = "<div>content</div>";
const match = text.match(pattern);
if (match) {
    console.log(match.groups.tag); // "div"
}
```

## Practical Examples

### Example 1: Find Repeated Patterns

```
(\d{3})-(\d{3})-(\d{4})
```

Find phone numbers where area code equals exchange:

```
(\d{3})-(\1)-\d{4}
```

**Matches:**
- ✅ "123-123-4567" (area code = exchange)
- ❌ "123-456-7890" (different)

### Example 2: Validate Quoted Strings

```
(["'])(.*?)\1
```

**Explanation:**
- `(["'])` - Capture quote character (single or double)
- `(.*?)` - Capture content (lazy)
- `\1` - Match same quote character

**Matches:**
- ✅ `"hello"`
- ✅ `'world'`
- ❌ `"hello'` (mismatched quotes)

### Example 3: Find Palindromic Words

```
\b(\w)(\w)\w*\2\1\b
```

**Explanation:**
- `\b` - Word boundary
- `(\w)(\w)` - Capture first two letters
- `\w*` - Zero or more letters
- `\2\1` - Reverse of first two letters

**Matches:**
- ✅ "level" (l-e-v-e-l)
- ✅ "radar" (r-a-d-a-r)
- ❌ "hello" (not palindrome)

### Example 4: Extract Key-Value Pairs

```
(\w+)=(\w+)
```

Find repeated key-value pairs:

```
(\w+)=(\w+).*?\1=\2
```

**Matches:**
- ✅ "name=John ... name=John" (same key-value repeated)
- ❌ "name=John ... name=Jane" (different values)

## Advanced Patterns

### Example: Matching Balanced Parentheses (Limited)

```
\(([^()]+|\([^()]*\))*\)
```

This is a simplified version. Full balanced matching requires recursion (not supported in all engines).

### Example: Find Repeated Substrings

```
(.+)\1+
```

**Explanation:**
- `(.+)` - Capture one or more characters
- `\1+` - Same substring repeated one or more times

**Matches:**
- ✅ "ababab" (matches "ab" repeated)
- ✅ "hellohello" (matches "hello" repeated)

## Common Use Cases

### 1. Finding Typos (Repeated Characters)

```
(.)\1{2,}
```

Finds characters repeated 3+ times:
- "helllo" → Matches "lll"
- "cooool" → Matches "oooo"

### 2. Validating Format Consistency

```
^(\d{3})-\1-\d{4}$
```

Phone number where area code = exchange:
- ✅ "123-123-4567"
- ❌ "123-456-7890"

### 3. Extracting Paired Delimiters

```
\[([^\]]+)\]
```

Matches content in square brackets:
- "[text]" → Captures "text"

With backreference for matching brackets:
```
\[([^\]]+)\]
```

## Limitations

### 1. Not All Engines Support

Some basic regex engines don't support backreferences. Check your engine's documentation.

### 2. Performance

Backreferences can be slow, especially with complex patterns and long text.

### 3. Complexity

Patterns with backreferences can be hard to read and maintain.

## Tips and Best Practices

1. **Use named groups** for clarity when possible
2. **Test thoroughly** - backreferences can behave unexpectedly
3. **Consider alternatives** - sometimes simpler patterns work better
4. **Document complex patterns** - explain what each group captures
5. **Be aware of engine differences** - syntax varies

## Exercises

Try these:

1. Find words where first and last letters are the same: `_____`
2. Match HTML tags with same opening/closing tag: `_____`
3. Find repeated 3-digit sequences: `_____`
4. Match quoted strings with matching quotes: `_____`
5. Find phone numbers where area code = last 3 digits: `_____`

---

**Next:** [greedy-vs-lazy.md](greedy-vs-lazy.md) to understand matching behavior!

