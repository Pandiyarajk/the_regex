# Project: Regex in JavaScript - Complete Guide

A comprehensive guide to using regex in JavaScript, including common patterns and best practices.

## JavaScript Regex Overview

JavaScript has built-in regex support. Two ways to create regex:

1. **Literal notation**: `/pattern/flags`
2. **Constructor**: `new RegExp('pattern', 'flags')`

## Common Methods

### String Methods

- `match()` - Returns matches array
- `matchAll()` - Returns iterator of all matches
- `search()` - Returns index of first match
- `replace()` - Replaces matches
- `split()` - Splits by pattern

### RegExp Methods

- `test()` - Returns true/false
- `exec()` - Returns match details (can be called repeatedly)

## Common Patterns and Examples

### 1. Basic Matching

```javascript
// Using test()
const text = "Hello, my phone number is 123-456-7890";
const pattern = /\d{3}-\d{3}-\d{4}/;
const found = pattern.test(text);
console.log(found); // true

// Using match()
const match = text.match(/\d{3}-\d{3}-\d{4}/);
console.log(match[0]); // "123-456-7890"
```

### 2. Finding All Matches

```javascript
const text = "Contact: email1@example.com or email2@test.org";
const pattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g;
const emails = text.match(pattern);
console.log(emails); // ['email1@example.com', 'email2@test.org']
```

### 3. Using Groups

```javascript
const text = "Date: 25/12/2023";
const pattern = /(\d{2})\/(\d{2})\/(\d{4})/;
const match = text.match(pattern);
if (match) {
    const day = match[1];      // "25"
    const month = match[2];    // "12"
    const year = match[3];      // "2023"
    console.log(`Day: ${day}, Month: ${month}, Year: ${year}`);
}
```

### 4. Named Groups (ES2018+)

```javascript
const text = "Date: 25/12/2023";
const pattern = /(?<day>\d{2})\/(?<month>\d{2})\/(?<year>\d{4})/;
const match = text.match(pattern);
if (match) {
    console.log(match.groups.day);    // "25"
    console.log(match.groups.month);   // "12"
    console.log(match.groups.year);    // "2023"
}
```

### 5. Substitution

```javascript
const text = "Phone: 123-456-7890";
const pattern = /\d{3}-\d{3}-\d{4}/;
const replacement = "XXX-XXX-XXXX";
const result = text.replace(pattern, replacement);
console.log(result); // "Phone: XXX-XXX-XXXX"

// Replace all occurrences
const text2 = "Call 123-456-7890 or 987-654-3210";
const result2 = text2.replace(/\d{3}-\d{3}-\d{4}/g, "XXX-XXX-XXXX");
console.log(result2); // "Call XXX-XXX-XXXX or XXX-XXX-XXXX"
```

### 6. Using matchAll() (ES2020+)

```javascript
const text = "Call 123-456-7890 or 987-654-3210";
const pattern = /\d{3}-\d{3}-\d{4}/g;
const matches = [...text.matchAll(pattern)];
matches.forEach(match => {
    console.log(match[0]); // "123-456-7890", then "987-654-3210"
});
```

### 7. Flags

```javascript
// Case-insensitive
const text = "Hello HELLO hello";
const pattern = /hello/gi;
const matches = text.match(pattern);
console.log(matches); // ['Hello', 'HELLO', 'hello']

// Multiline
const text2 = "Line 1\nLine 2\nLine 3";
const pattern2 = /^Line/gm;
const matches2 = text2.match(pattern2);
console.log(matches2); // ['Line', 'Line', 'Line']

// Global flag
const text3 = "test test test";
const pattern3 = /test/g;
const matches3 = text3.match(pattern3);
console.log(matches3); // ['test', 'test', 'test']
```

## Common Use Cases

### Email Validation

```javascript
function validateEmail(email) {
    const pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return pattern.test(email);
}

const emails = ["user@example.com", "invalid.email", "@example.com"];
emails.forEach(email => {
    console.log(`${email}: ${validateEmail(email)}`);
});
```

### Phone Number Extraction

```javascript
function extractPhoneNumbers(text) {
    const pattern = /\b\d{3}[-.]?\d{3}[-.]?\d{4}\b/g;
    return text.match(pattern) || [];
}

const text = "Call 123-456-7890 or 987.654.3210";
const numbers = extractPhoneNumbers(text);
console.log(numbers); // ['123-456-7890', '987.654.3210']
```

### URL Extraction

```javascript
function extractUrls(text) {
    const pattern = /https?:\/\/[^\s]+/g;
    return text.match(pattern) || [];
}

const text = "Visit https://example.com and http://test.org";
const urls = extractUrls(text);
console.log(urls); // ['https://example.com', 'http://test.org']
```

### Text Cleaning

```javascript
function cleanText(text) {
    // Remove extra spaces
    text = text.replace(/\s+/g, ' ');
    // Remove special characters (keep letters, digits, spaces)
    text = text.replace(/[^a-zA-Z0-9\s]/g, '');
    return text.trim();
}

const text = "Hello!!!   World@@@";
const cleaned = cleanText(text);
console.log(cleaned); // "Hello World"
```

### Form Validation

```javascript
function validateForm(formData) {
    const errors = {};
    
    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(formData.email)) {
        errors.email = "Invalid email format";
    }
    
    // Phone validation
    const phonePattern = /^\d{3}-\d{3}-\d{4}$/;
    if (!phonePattern.test(formData.phone)) {
        errors.phone = "Phone must be in format XXX-XXX-XXXX";
    }
    
    // Password validation (8+ chars, uppercase, lowercase, digit)
    const passwordPattern = /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$/;
    if (!passwordPattern.test(formData.password)) {
        errors.password = "Password must be 8+ chars with uppercase, lowercase, and digit";
    }
    
    return errors;
}
```

## Best Practices

### 1. Use Literal Notation When Possible

```javascript
// Good - literal notation
const pattern = /\d+/;

// Fine - constructor (useful for dynamic patterns)
const digitCount = 3;
const pattern2 = new RegExp(`\\d{${digitCount}}`);
```

### 2. Remember the Global Flag

```javascript
// Without 'g' - only first match
const text = "test test test";
const matches1 = text.match(/test/);
console.log(matches1); // ['test']

// With 'g' - all matches
const matches2 = text.match(/test/g);
console.log(matches2); // ['test', 'test', 'test']
```

### 3. Handle Null Results

```javascript
const text = "No numbers here";
const matches = text.match(/\d+/);
if (matches) {
    console.log(matches[0]);
} else {
    console.log("No match found");
}
```

### 4. Use test() for Simple Checks

```javascript
// Good - simple boolean check
const isValid = /\d+/.test(text);

// Less efficient - gets full match when not needed
const match = text.match(/\d+/);
const isValid2 = match !== null;
```

### 5. Be Careful with Greedy Matching

```javascript
// Greedy (matches too much)
const text = "<div>content</div><div>more</div>";
const match1 = text.match(/<div>.*<\/div>/);
console.log(match1[0]); // "<div>content</div><div>more</div>"

// Lazy (matches correctly)
const match2 = text.match(/<div>.*?<\/div>/);
console.log(match2[0]); // "<div>content</div>"
```

## Common Pitfalls

### 1. Forgetting Anchors

```javascript
// Without anchors - matches partial strings
const pattern = /\d{3}/;
pattern.test("abc123def"); // true

// With anchors - matches full string
const pattern2 = /^\d{3}$/;
pattern2.test("abc123def"); // false
```

### 2. Not Escaping Special Characters

```javascript
// Wrong - dot matches any character
const pattern = /example.com/;
pattern.test("exampleXcom"); // true

// Correct - escape dot
const pattern2 = /example\.com/;
pattern2.test("exampleXcom"); // false
```

### 3. Global Flag Side Effects

```javascript
const pattern = /\d+/g;
const text = "123 456";

pattern.test(text); // true
pattern.lastIndex;  // 3 (position after first match)

pattern.test(text); // true (continues from lastIndex)
pattern.lastIndex;  // 7

pattern.test(text); // false (no more matches)
pattern.lastIndex;  // 0 (reset)

// Reset manually if needed
pattern.lastIndex = 0;
```

## Performance Tips

1. **Compile patterns** for repeated use
2. **Use specific patterns** instead of `.*`
3. **Avoid catastrophic backtracking**
4. **Consider string methods** - sometimes faster than regex

## Browser Compatibility

- **Named groups**: ES2018+ (Chrome 64+, Firefox 78+, Safari 13.1+)
- **matchAll()**: ES2020+ (Chrome 73+, Firefox 67+, Safari 13+)
- **Lookbehind**: ES2018+ (Chrome 62+, Firefox 78+, Safari 16.4+)

## Resources

- [MDN Regex Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions)
- [Regex101 JavaScript tester](https://regex101.com/)
- Practice with exercises in this repository

---

**Congratulations!** You've completed the regex learning path. Practice with real-world projects and continue building your regex skills!

