# Basic Regex Exercises

Practice your regex skills with these exercises. Try to solve them yourself before checking the solutions!

## Exercise 1: Match Numbers

Write a regex pattern that matches:
- Any sequence of digits
- At least one digit
- Can appear anywhere in the text

**Test Cases:**
```
"Price is 123 dollars"     → Should match "123"
"I have 5 apples"          → Should match "5"
"Version 2.0.1"            → Should match "2", "0", "1"
"No numbers here"          → Should match nothing
```

**Your Pattern:**
```
```

---

## Exercise 2: Detect Mobile Number

Write a regex pattern to match a 10-digit mobile number.

**Requirements:**
- Exactly 10 digits
- Can have optional formatting: spaces, hyphens, or parentheses
- Examples: "1234567890", "123-456-7890", "(123) 456-7890", "123 456 7890"

**Test Cases:**
```
"1234567890"              → Should match
"123-456-7890"            → Should match
"(123) 456-7890"          → Should match
"123 456 7890"            → Should match
"12-345-6789"             → Should NOT match (9 digits)
"12345678901"             → Should NOT match (11 digits)
```

**Your Pattern:**
```
```

---

## Exercise 3: Find All Words Starting with 'A'

Write a regex pattern that finds all words starting with the letter 'A' (case-insensitive).

**Requirements:**
- Match whole words only
- Case-insensitive (matches both "Apple" and "apple")
- At least 2 characters long

**Test Cases:**
```
"Apple and application are awesome"  → Should match: "Apple", "application", "are", "awesome"
"An apple a day"                     → Should match: "An", "apple", "a"
"Banana is yellow"                   → Should match nothing
```

**Your Pattern:**
```
```

---

## Exercise 4: Match Valid PIN Code

Write a regex pattern to validate a 4-digit or 6-digit PIN code.

**Requirements:**
- Either exactly 4 digits OR exactly 6 digits
- Only digits allowed
- Entire string must match (use anchors)

**Test Cases:**
```
"1234"      → Should match (4 digits)
"123456"    → Should match (6 digits)
"12345"     → Should NOT match (5 digits)
"1234a"     → Should NOT match (contains letter)
"12 34"     → Should NOT match (contains space)
```

**Your Pattern:**
```
```

---

## Exercise 5: Extract Domain Names

Write a regex pattern to extract domain names from URLs.

**Requirements:**
- Match domain part (without protocol and path)
- Examples: "example.com", "subdomain.example.com"
- Should work with: "http://example.com", "https://www.example.com/path"

**Test Cases:**
```
"http://example.com"              → Should extract "example.com"
"https://www.google.com/search"   → Should extract "www.google.com"
"ftp://files.example.org"         → Should extract "files.example.org"
"example.com"                     → Should extract "example.com"
```

**Your Pattern:**
```
```

---

## Exercise 6: Match Time Format (HH:MM)

Write a regex pattern to match time in 24-hour format (HH:MM).

**Requirements:**
- Hours: 00-23
- Minutes: 00-59
- Format: HH:MM

**Test Cases:**
```
"09:30"     → Should match
"23:59"     → Should match
"00:00"     → Should match
"24:00"     → Should NOT match (invalid hour)
"12:60"     → Should NOT match (invalid minute)
"9:30"      → Should NOT match (missing leading zero)
```

**Your Pattern:**
```
```

---

## Exercise 7: Find Repeated Words

Write a regex pattern to find words that appear twice in a row (with space between).

**Requirements:**
- Match the pattern: word space word
- Case-sensitive
- Example: "the the", "hello hello"

**Test Cases:**
```
"the the cat"           → Should match "the the"
"hello hello world"     → Should match "hello hello"
"the cat sat"           → Should NOT match
"Hello hello"           → Should NOT match (different case)
```

**Your Pattern:**
```
```

---

## Exercise 8: Validate Username (Stricter)

Write a regex pattern to validate usernames with stricter rules.

**Requirements:**
- Must start with a letter
- Can contain letters, digits, and underscores
- Length: 5-20 characters
- Cannot end with underscore

**Test Cases:**
```
"john_doe"      → Should match
"user123"       → Should match
"admin"         → Should NOT match (too short)
"123user"       → Should NOT match (starts with digit)
"user_"         → Should NOT match (ends with underscore)
"user-name"     → Should NOT match (contains hyphen)
```

**Your Pattern:**
```
```

---

## Exercise 9: Match IP Address (Simple)

Write a regex pattern to match IPv4 addresses (simplified version).

**Requirements:**
- Format: XXX.XXX.XXX.XXX
- Each segment: 0-255 (simplified: 0-999 for now)
- Example: "192.168.1.1"

**Test Cases:**
```
"192.168.1.1"       → Should match
"10.0.0.1"          → Should match
"256.1.1.1"         → Should match (simplified version)
"192.168.1"         → Should NOT match (incomplete)
"192.168.1.1.1"     → Should NOT match (too many segments)
```

**Your Pattern:**
```
```

---

## Exercise 10: Remove Extra Spaces

Write a regex pattern to identify multiple consecutive spaces (to be replaced with single space).

**Requirements:**
- Match 2 or more consecutive spaces
- Should match tabs as spaces too

**Test Cases:**
```
"hello    world"        → Should match "    "
"text   with   spaces"  → Should match "   " and "   "
"normal text"           → Should NOT match
```

**Your Pattern:**
```
```

---

## Challenge Exercise: Extract Dates

Write a regex pattern to extract dates in format DD/MM/YYYY or DD-MM-YYYY.

**Requirements:**
- Day: 01-31
- Month: 01-12
- Year: 1900-2099 (simplified)
- Separator: `/` or `-`

**Test Cases:**
```
"Date: 25/12/2023"      → Should match "25/12/2023"
"Born on 01-01-2000"    → Should match "01-01-2000"
"Invalid: 32/01/2023"   → Should match "32/01/2023" (validation comes later)
"12/25/2023"            → Should match "12/25/2023"
```

**Your Pattern:**
```
```

---

## Tips for Solving

1. **Break down the problem** into smaller parts
2. **Start simple** - match the basic pattern first
3. **Add constraints** gradually (anchors, character classes, etc.)
4. **Test incrementally** - verify each part works
5. **Use online tools** to visualize and debug
6. **Read the requirements carefully** - note all constraints

---

## Checking Your Answers

After attempting all exercises, check your solutions in [../solutions/basic-solutions.md](../solutions/basic-solutions.md).

**Remember:** There are often multiple correct solutions. Focus on understanding why your pattern works (or doesn't work)!

---

**Ready for the quiz?** → [quiz-basic.md](quiz-basic.md)

