# Simple Regex Examples

Practical examples to get you started with regex. Each example includes the pattern, explanation, and test cases.

## Example 1: Match a 3-Letter Word

### Pattern
```
\b[a-zA-Z]{3}\b
```

### Explanation
- `\b` - Word boundary (start of word)
- `[a-zA-Z]` - Any letter (lowercase or uppercase)
- `{3}` - Exactly 3 characters
- `\b` - Word boundary (end of word)

### Matches
- ✅ "cat"
- ✅ "dog"
- ✅ "The cat sat" → matches "The", "cat", "sat"
- ❌ "cats" (4 letters)
- ❌ "a" (1 letter)

### Code Examples

**Python:**
```python
import re

text = "The cat sat on the mat"
pattern = r'\b[a-zA-Z]{3}\b'
matches = re.findall(pattern, text)
print(matches)  # ['The', 'cat', 'sat', 'the', 'mat']
```

**JavaScript:**
```javascript
const text = "The cat sat on the mat";
const pattern = /\b[a-zA-Z]{3}\b/g;
const matches = text.match(pattern);
console.log(matches); // ['The', 'cat', 'sat', 'the', 'mat']
```

---

## Example 2: Match Only Digits

### Pattern
```
^\d+$
```

### Explanation
- `^` - Start of string
- `\d+` - One or more digits
- `$` - End of string

This ensures the entire string contains only digits.

### Matches
- ✅ "123"
- ✅ "0"
- ✅ "999999"
- ❌ "123abc" (contains letters)
- ❌ "12 34" (contains space)
- ❌ "12.34" (contains dot)

### Code Examples

**Python:**
```python
import re

def is_only_digits(text):
    pattern = r'^\d+$'
    return bool(re.match(pattern, text))

print(is_only_digits("123"))    # True
print(is_only_digits("123abc"))  # False
```

**JavaScript:**
```javascript
function isOnlyDigits(text) {
    const pattern = /^\d+$/;
    return pattern.test(text);
}

console.log(isOnlyDigits("123"));    // true
console.log(isOnlyDigits("123abc")); // false
```

---

## Example 3: Validate a Username

### Pattern
```
^[a-zA-Z0-9_]{3,16}$
```

### Explanation
- `^` - Start of string
- `[a-zA-Z0-9_]` - Letters, digits, or underscore
- `{3,16}` - Between 3 and 16 characters
- `$` - End of string

Common username rules: alphanumeric + underscore, 3-16 characters.

### Matches
- ✅ "john_doe"
- ✅ "user123"
- ✅ "admin"
- ❌ "ab" (too short)
- ❌ "this_username_is_too_long" (too long)
- ❌ "user-name" (contains hyphen)

### Code Examples

**Python:**
```python
import re

def validate_username(username):
    pattern = r'^[a-zA-Z0-9_]{3,16}$'
    return bool(re.match(pattern, username))

usernames = ["john_doe", "user123", "ab", "user-name"]
for username in usernames:
    print(f"{username}: {validate_username(username)}")
# Output:
# john_doe: True
# user123: True
# ab: False
# user-name: False
```

**JavaScript:**
```javascript
function validateUsername(username) {
    const pattern = /^[a-zA-Z0-9_]{3,16}$/;
    return pattern.test(username);
}

const usernames = ["john_doe", "user123", "ab", "user-name"];
usernames.forEach(username => {
    console.log(`${username}: ${validateUsername(username)}`);
});
```

---

## Example 4: Find Spaces and Tabs

### Pattern
```
[\s\t]+
```

### Explanation
- `[\s\t]` - Character class matching whitespace or tab
- `+` - One or more occurrences

Alternative: `\s+` (matches all whitespace including spaces, tabs, newlines)

### Matches
- ✅ "hello    world" → matches "    " (spaces)
- ✅ "hello\tworld" → matches "\t" (tab)
- ✅ "hello   \t  world" → matches "   \t  "
- ❌ "helloworld" (no whitespace)

### Code Examples

**Python:**
```python
import re

text = "hello    world\tand   more"
pattern = r'[\s\t]+'
matches = re.findall(pattern, text)
print(matches)  # ['    ', '\t', '   ']

# Replace multiple spaces with single space
cleaned = re.sub(pattern, ' ', text)
print(cleaned)  # "hello world and more"
```

**JavaScript:**
```javascript
const text = "hello    world\tand   more";
const pattern = /[\s\t]+/g;
const matches = text.match(pattern);
console.log(matches); // ['    ', '\t', '   ']

// Replace multiple spaces with single space
const cleaned = text.replace(pattern, ' ');
console.log(cleaned); // "hello world and more"
```

---

## Example 5: Match Words Starting with 'A'

### Pattern
```
\b[Aa]\w+
```

### Explanation
- `\b` - Word boundary
- `[Aa]` - Letter 'A' or 'a' (case-insensitive match)
- `\w+` - One or more word characters

### Matches
- ✅ "Apple"
- ✅ "apple"
- ✅ "application"
- ✅ "The Apple is red" → matches "Apple"
- ❌ "banana" (doesn't start with A)
- ❌ "a" (single letter, but `\w+` requires at least one more)

### Code Examples

**Python:**
```python
import re

text = "Apple and application are awesome"
pattern = r'\b[Aa]\w+'
matches = re.findall(pattern, text)
print(matches)  # ['Apple', 'application', 'are', 'awesome']

# Case-insensitive version
pattern_ci = r'\ba\w+'
matches_ci = re.findall(pattern_ci, text, re.IGNORECASE)
print(matches_ci)  # ['Apple', 'application', 'are', 'awesome']
```

**JavaScript:**
```javascript
const text = "Apple and application are awesome";
const pattern = /\b[Aa]\w+/g;
const matches = text.match(pattern);
console.log(matches); // ['Apple', 'application', 'are', 'awesome']

// Case-insensitive version
const patternCI = /\ba\w+/gi;
const matchesCI = text.match(patternCI);
console.log(matchesCI); // ['Apple', 'application', 'are', 'awesome']
```

---

## Example 6: Match Phone Number Format (Simple)

### Pattern
```
\d{3}-\d{3}-\d{4}
```

### Explanation
- `\d{3}` - Exactly 3 digits
- `-` - Literal hyphen
- `\d{3}` - Exactly 3 digits
- `-` - Literal hyphen
- `\d{4}` - Exactly 4 digits

Format: XXX-XXX-XXXX

### Matches
- ✅ "123-456-7890"
- ✅ "555-123-4567"
- ❌ "1234567890" (no hyphens)
- ❌ "12-34-5678" (wrong format)
- ❌ "123-456-789" (last part too short)

### Code Examples

**Python:**
```python
import re

def find_phone_numbers(text):
    pattern = r'\d{3}-\d{3}-\d{4}'
    return re.findall(pattern, text)

text = "Call me at 123-456-7890 or 555-123-4567"
numbers = find_phone_numbers(text)
print(numbers)  # ['123-456-7890', '555-123-4567']
```

**JavaScript:**
```javascript
function findPhoneNumbers(text) {
    const pattern = /\d{3}-\d{3}-\d{4}/g;
    return text.match(pattern);
}

const text = "Call me at 123-456-7890 or 555-123-4567";
const numbers = findPhoneNumbers(text);
console.log(numbers); // ['123-456-7890', '555-123-4567']
```

---

## Example 7: Match Email (Basic Pattern)

### Pattern
```
\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
```

### Explanation
- `\b` - Word boundary
- `[A-Za-z0-9._%+-]+` - One or more allowed characters before @
- `@` - Literal @ symbol
- `[A-Za-z0-9.-]+` - Domain name (letters, digits, dots, hyphens)
- `\.` - Literal dot
- `[A-Z|a-z]{2,}` - TLD (2+ letters)
- `\b` - Word boundary

**Note:** This is a simplified pattern. Real email validation is more complex.

### Matches
- ✅ "user@example.com"
- ✅ "john.doe@company.co.uk"
- ❌ "@example.com" (missing local part)
- ❌ "user@.com" (missing domain)
- ❌ "user@example" (missing TLD)

### Code Examples

**Python:**
```python
import re

def find_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

text = "Contact admin@example.com or support@company.org"
emails = find_emails(text)
print(emails)  # ['admin@example.com', 'support@company.org']
```

**JavaScript:**
```javascript
function findEmails(text) {
    const pattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g;
    return text.match(pattern);
}

const text = "Contact admin@example.com or support@company.org";
const emails = findEmails(text);
console.log(emails); // ['admin@example.com', 'support@company.org']
```

---

## Practice Tips

1. **Test each pattern** with different inputs
2. **Understand each part** of the pattern
3. **Try variations** - modify patterns to see what changes
4. **Use online tools** like regex101.com to visualize matches
5. **Read error messages** - they often point to syntax issues

---

**Next:** Try the [exercises-basic.md](exercises-basic.md) to practice!

