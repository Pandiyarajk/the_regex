# Intermediate Regex Exercises

Practice intermediate concepts: character classes, grouping, quantifiers, and lookarounds.

## Exercise 1: Validate Strong Password

Write a regex pattern to validate a strong password with these requirements:
- At least 8 characters long
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character (!@#$%^&*)

**Test Cases:**
```
"Password123!"     → Should match
"password123!"     → Should NOT match (no uppercase)
"PASSWORD123!"    → Should NOT match (no lowercase)
"Password!"        → Should NOT match (no digit)
"Password123"      → Should NOT match (no special char)
"Pass123!"         → Should NOT match (too short)
```

**Your Pattern:**
```
```

---

## Exercise 2: Extract Hashtags

Write a regex pattern to extract all hashtags from text. A hashtag:
- Starts with `#`
- Followed by word characters (letters, digits, underscore)
- Can appear anywhere in text

**Test Cases:**
```
"Check out #regex and #coding!"     → Should extract: "regex", "coding"
"#python #javascript #webdev"       → Should extract: "python", "javascript", "webdev"
"#123abc #test-case"                → Should extract: "123abc" (not "test-case" - hyphen not allowed)
"No hashtags here"                  → Should extract nothing
```

**Your Pattern:**
```
```

---

## Exercise 3: Extract Price Values

Write a regex pattern to extract price values in formats:
- $100
- $99.99
- $1,234.56 (with thousands separator)

**Requirements:**
- Dollar sign prefix
- Optional thousands separators (commas)
- Optional decimal part (.XX)

**Test Cases:**
```
"Price is $100"                    → Should extract: "$100"
"Costs $99.99 each"                → Should extract: "$99.99"
"Total: $1,234.56"                 → Should extract: "$1,234.56"
"Free item"                        → Should extract nothing
"$100.5"                           → Should extract: "$100.5"
```

**Your Pattern:**
```
```

---

## Exercise 4: Match All Capitalized Words

Write a regex pattern to find all words that:
- Start with an uppercase letter
- Followed by one or more lowercase letters
- Are complete words (word boundaries)

**Test Cases:**
```
"Hello World from Python"          → Should match: "Hello", "World", "Python"
"HELLO world"                      → Should match: "world" only
"iPhone and iPad"                  → Should match nothing (start with lowercase)
"The Quick Brown Fox"              → Should match: "The", "Quick", "Brown", "Fox"
```

**Your Pattern:**
```
```

---

## Exercise 5: Extract Domain from URLs

Write a regex pattern to extract the domain name from various URL formats:
- http://example.com
- https://www.example.com
- https://subdomain.example.com/path
- ftp://files.example.org

**Requirements:**
- Extract only the domain part (with subdomain if present)
- Should work with different protocols

**Test Cases:**
```
"http://example.com"                → Should extract: "example.com"
"https://www.google.com/search"     → Should extract: "www.google.com"
"ftp://files.example.org"           → Should extract: "files.example.org"
"https://sub.domain.example.com"    → Should extract: "sub.domain.example.com"
```

**Your Pattern:**
```
```

---

## Exercise 6: Parse Log Entry

Write a regex pattern to parse a log entry in format:
`[TIMESTAMP] LEVEL: MESSAGE`

Example: `[2023-12-25 10:30:45] ERROR: Database connection failed`

**Requirements:**
- Extract timestamp (date and time)
- Extract log level (INFO, ERROR, WARN, DEBUG)
- Extract message (rest of the line)

**Test Cases:**
```
"[2023-12-25 10:30:45] ERROR: Database connection failed"
→ Should extract:
  - Timestamp: "2023-12-25 10:30:45"
  - Level: "ERROR"
  - Message: "Database connection failed"

"[2023-01-01 00:00:00] INFO: Server started"
→ Should extract:
  - Timestamp: "2023-01-01 00:00:00"
  - Level: "INFO"
  - Message: "Server started"
```

**Your Pattern:**
```
```

---

## Exercise 7: Validate Credit Card Format

Write a regex pattern to validate credit card numbers in format:
- XXXX-XXXX-XXXX-XXXX (16 digits with hyphens)
- XXXX XXXX XXXX XXXX (16 digits with spaces)
- XXXXXXXXXXXXXXXX (16 digits, no separators)

**Requirements:**
- Exactly 16 digits
- Optional separators: hyphens or spaces
- Must be consistent (all hyphens or all spaces or none)

**Test Cases:**
```
"1234-5678-9012-3456"     → Should match
"1234 5678 9012 3456"     → Should match
"1234567890123456"        → Should match
"1234-5678 9012-3456"     → Should NOT match (inconsistent)
"1234-5678-9012"          → Should NOT match (too short)
"1234-5678-9012-34567"    → Should NOT match (too long)
```

**Your Pattern:**
```
```

---

## Exercise 8: Extract Email Local Part and Domain

Write a regex pattern to extract both the local part (before @) and domain (after @) from email addresses.

**Requirements:**
- Capture local part in group 1
- Capture domain in group 2
- Handle common email formats

**Test Cases:**
```
"user@example.com"
→ Should capture:
  - Group 1: "user"
  - Group 2: "example.com"

"john.doe@company.co.uk"
→ Should capture:
  - Group 1: "john.doe"
  - Group 2: "company.co.uk"

"user+tag@subdomain.example.org"
→ Should capture:
  - Group 1: "user+tag"
  - Group 2: "subdomain.example.org"
```

**Your Pattern:**
```
```

---

## Exercise 9: Find Repeated Phrases

Write a regex pattern to find phrases that appear twice in a row (with punctuation/space between).

**Requirements:**
- Match the same phrase repeated
- Can have spaces/punctuation between
- Case-sensitive

**Test Cases:**
```
"hello hello world"           → Should match: "hello hello"
"test, test, and more"        → Should match: "test, test"
"the the cat sat"             → Should match: "the the"
"Hello hello"                 → Should NOT match (different case)
```

**Your Pattern:**
```
```

---

## Exercise 10: Extract Time in 12-Hour Format

Write a regex pattern to extract time in 12-hour format:
- HH:MM AM/PM
- Examples: "09:30 AM", "11:45 PM", "12:00 AM"

**Requirements:**
- Extract hour, minute, and AM/PM
- Hour: 01-12
- Minute: 00-59
- AM or PM (case-insensitive)

**Test Cases:**
```
"Meeting at 09:30 AM"         → Should extract: "09:30 AM"
"Lunch at 12:00 PM"           → Should extract: "12:00 PM"
"Midnight is 12:00 AM"        → Should extract: "12:00 AM"
"Invalid: 13:00 PM"           → Should NOT match (invalid hour)
"Invalid: 09:60 AM"           → Should NOT match (invalid minute)
```

**Your Pattern:**
```
```

---

## Challenge Exercise: Validate Complex Password

Write a regex pattern that uses lookaheads to validate a password with ALL of these requirements:
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character from: !@#$%^&*
- No spaces allowed

**Hint:** Use multiple positive lookaheads.

**Test Cases:**
```
"Password123!"        → Should match
"password123!"        → Should NOT match (no uppercase)
"PASSWORD123!"        → Should NOT match (no lowercase)
"Password!"           → Should NOT match (no digit)
"Password123"         → Should NOT match (no special char)
"Pass word123!"       → Should NOT match (contains space)
```

**Your Pattern:**
```
```

---

## Tips for Solving

1. **Break down requirements** - List each requirement separately
2. **Use lookaheads** - For complex validation with multiple conditions
3. **Test incrementally** - Build pattern piece by piece
4. **Consider edge cases** - Empty strings, boundaries, special characters
5. **Use groups strategically** - Capture only what you need
6. **Check your engine** - Some features vary by language

---

## Checking Your Answers

After attempting all exercises, check your solutions in [../solutions/intermediate-solutions.md](../solutions/intermediate-solutions.md).

**Remember:** Focus on understanding why patterns work. There are often multiple valid solutions!

---

**Ready for the quiz?** → [quiz-intermediate.md](quiz-intermediate.md)

