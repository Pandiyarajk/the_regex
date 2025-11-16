# Advanced Regex Exercises

Challenge yourself with these advanced exercises combining multiple regex concepts.

## Exercise 1: Parse JSON-like Logs

Write a regex pattern to parse log entries in JSON-like format:
`{"key": "value", "key2": "value2"}`

**Requirements:**
- Extract key-value pairs
- Handle string values only (simplified)
- Keys and values are in double quotes

**Test Cases:**
```
'{"level": "ERROR", "message": "Failed"}'
→ Should extract:
  - level: "ERROR"
  - message: "Failed"

'{"timestamp": "2023-12-25", "user": "john"}'
→ Should extract:
  - timestamp: "2023-12-25"
  - user: "john"
```

**Your Pattern:**
```
```

---

## Exercise 2: Match Nested Parentheses (2 Levels)

Write a regex pattern to match content in parentheses, handling one level of nesting.

**Requirements:**
- Match outer parentheses
- Handle nested parentheses inside
- Extract the content

**Test Cases:**
```
"outer (inner (nested) more) text"
→ Should match: "inner (nested) more"

"(simple)"
→ Should match: "simple"

"(level1 (level2) end)"
→ Should match: "level1 (level2) end"
```

**Your Pattern:**
```
```

---

## Exercise 3: Extract IP + Port Combinations

Write a regex pattern to extract IP addresses with port numbers.

**Requirements:**
- IP format: XXX.XXX.XXX.XXX (simplified validation)
- Port: 1-65535
- Format: IP:PORT

**Test Cases:**
```
"Server at 192.168.1.1:8080"
→ Should extract: IP="192.168.1.1", Port="8080"

"Connect to 10.0.0.1:443 and 172.16.0.1:80"
→ Should extract:
  - IP="10.0.0.1", Port="443"
  - IP="172.16.0.1", Port="80"
```

**Your Pattern:**
```
```

---

## Exercise 4: Find Repeated Substrings

Write a regex pattern to find substrings that are repeated 2+ times consecutively.

**Requirements:**
- Find the base substring
- Must repeat at least twice
- Substring length: 2+ characters

**Test Cases:**
```
"ababab"        → Should find: "ab" (repeated 3 times)
"hellohello"    → Should find: "hello" (repeated 2 times)
"123123123"     → Should find: "123" (repeated 3 times)
"abcdef"        → Should find nothing
```

**Your Pattern:**
```
```

---

## Exercise 5: Validate Complex Password

Write a regex pattern using lookaheads to validate a password with ALL requirements:
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character (!@#$%^&*)
- No spaces
- No character repeated 3+ times consecutively

**Test Cases:**
```
"Password123!"     → Should match
"Pass123!"         → Should NOT match (too short)
"password123!"     → Should NOT match (no uppercase)
"PASS123!"         → Should NOT match (no lowercase)
"Password!"        → Should NOT match (no digit)
"Pass 123!"        → Should NOT match (contains space)
"Paass123!"        → Should NOT match (repeated 'a')
```

**Your Pattern:**
```
```

---

## Exercise 6: Extract HTML Tag Attributes

Write a regex pattern to extract attribute-value pairs from HTML tags.

**Requirements:**
- Extract attribute name and value
- Handle: `attr="value"` and `attr='value'`
- Extract from tags like: `<div class="container" id="main">`

**Test Cases:**
```
'<div class="container" id="main">'
→ Should extract:
  - class="container"
  - id="main"

'<a href="/page" title=\'Link\'>'
→ Should extract:
  - href="/page"
  - title='Link'
```

**Your Pattern:**
```
```

---

## Exercise 7: Match Balanced Quotes

Write a regex pattern to match text between matching quote characters.

**Requirements:**
- Match content between single or double quotes
- Quotes must match (single with single, double with double)
- Extract the content

**Test Cases:**
```
'He said "hello" and left'
→ Should match: "hello"

"She said 'hi' to me"
→ Should match: 'hi'

'Mixed "quotes' and 'more"'
→ Should match: "quotes", 'more'
```

**Your Pattern:**
```
```

---

## Exercise 8: Extract URLs with Components

Write a regex pattern to extract URL components:
- Protocol (http/https)
- Domain
- Path (optional)
- Query string (optional)

**Test Cases:**
```
"https://www.example.com/path?param=value"
→ Should extract:
  - Protocol: "https"
  - Domain: "www.example.com"
  - Path: "/path"
  - Query: "?param=value"

"http://example.com"
→ Should extract:
  - Protocol: "http"
  - Domain: "example.com"
  - Path: (none)
  - Query: (none)
```

**Your Pattern:**
```
```

---

## Exercise 9: Find Palindromic Words

Write a regex pattern to find words that are palindromes (read same forwards and backwards).

**Requirements:**
- Word must be 3+ characters
- Must be a complete word (word boundaries)
- Case-sensitive

**Test Cases:**
```
"level radar hello"
→ Should match: "level", "radar"

"a bb ccc dddd"
→ Should match: "bb", "ccc", "dddd"

"Hello" (capitalized)
→ Should NOT match (case-sensitive)
```

**Your Pattern:**
```
```

---

## Exercise 10: Parse Apache Log Entry

Write a regex pattern to parse Apache log entries in Common Log Format:
`IP - - [timestamp] "method path protocol" status size`

Example: `127.0.0.1 - - [25/Dec/2023:10:30:45 +0000] "GET /page HTTP/1.1" 200 1234`

**Requirements:**
- Extract IP address
- Extract timestamp
- Extract HTTP method
- Extract path
- Extract status code
- Extract response size

**Test Cases:**
```
'127.0.0.1 - - [25/Dec/2023:10:30:45 +0000] "GET /page HTTP/1.1" 200 1234'
→ Should extract:
  - IP: "127.0.0.1"
  - Timestamp: "25/Dec/2023:10:30:45 +0000"
  - Method: "GET"
  - Path: "/page"
  - Status: "200"
  - Size: "1234"
```

**Your Pattern:**
```
```

---

## Challenge Exercise: Regex for CSV Parsing (Simplified)

Write a regex pattern to parse CSV lines, handling:
- Basic fields: `field1,field2,field3`
- Quoted fields: `"field,with,commas","another"`
- Escaped quotes: `"field""with""quotes"`

**Note:** This is simplified. Real CSV parsing needs proper handling of edge cases.

**Test Cases:**
```
"name,age,city"
→ Should extract: ["name", "age", "city"]

'"John Doe",25,"New York, NY"'
→ Should extract: ["John Doe", "25", "New York, NY"]

'"Say ""hello""",test'
→ Should extract: ['Say "hello"', "test"]
```

**Your Pattern:**
```
```

---

## Tips for Advanced Exercises

1. **Combine concepts** - Use lookarounds, backreferences, groups together
2. **Test incrementally** - Build pattern piece by piece
3. **Consider limitations** - Some problems need parsers, not just regex
4. **Use named groups** - Makes extraction clearer
5. **Document your pattern** - Explain complex parts
6. **Test edge cases** - Empty strings, special characters, boundaries
7. **Performance** - Complex patterns can be slow on large text

---

## Checking Your Answers

After attempting all exercises, check your solutions in [../solutions/advanced-solutions.md](../solutions/advanced-solutions.md).

**Remember:** Some problems are better solved with parsers. Regex has limitations - know when to use alternatives!

---

**Ready for the quiz?** → [quiz-advanced.md](quiz-advanced.md)

