# Basic Regex Quiz

Test your understanding of basic regex concepts with these questions.

## Multiple Choice Questions

### Q1: What does the pattern `^hello$` match?

a) "hello" anywhere in the text  
b) "hello" at the start of the text  
c) "hello" at the end of the text  
d) "hello" as the entire string  

**Answer:** `d`

---

### Q2: What does `\d` match?

a) Any digit (0-9)  
b) Any non-digit  
c) Any character  
d) A literal 'd'  

**Answer:** `a`

---

### Q3: What does the pattern `colou?r` match?

a) Only "color"  
b) Only "colour"  
c) Both "color" and "colour"  
d) Neither  

**Answer:** `c`

---

### Q4: What does `[^0-9]` match?

a) Any digit  
b) Any non-digit  
c) Digits 0-9  
d) Nothing  

**Answer:** `b`

---

### Q5: What does `a+` match?

a) Zero or more 'a's  
b) One or more 'a's  
c) Exactly one 'a'  
d) Two or more 'a's  

**Answer:** `b`

---

### Q6: What does `\b` represent?

a) Backspace character  
b) Word boundary  
c) Beginning of string  
d) End of string  

**Answer:** `b`

---

### Q7: What does the pattern `^[A-Z]` match?

a) Any uppercase letter anywhere  
b) Uppercase letter at the start  
c) Any letter at the start  
d) Uppercase letter at the end  

**Answer:** `b`

---

### Q8: What does `.{3}` match?

a) Exactly 3 characters  
b) 3 or more characters  
c) Up to 3 characters  
d) Any 3-digit number  

**Answer:** `a`

---

### Q9: What does `[a-z]{2,4}` match?

a) 2 to 4 lowercase letters  
b) Exactly 2 or 4 letters  
c) At least 2 letters  
d) Up to 4 letters  

**Answer:** `a`

---

### Q10: What does `\.` match?

a) Any character  
b) A literal dot  
c) A newline  
d) Nothing  

**Answer:** `b`

---

## Identify the Output

### Q11: What will `re.findall(r'\d+', "I have 5 apples and 10 oranges")` return in Python?

a) `['5', '10']`  
b) `['5 apples', '10 oranges']`  
c) `['I have 5', 'and 10']`  
d) Error  

**Answer:** `a`

---

### Q12: What will `"hello world".match(/\b\w{5}\b/g)` return in JavaScript?

a) `['hello', 'world']`  
b) `['hello']`  
c) `['world']`  
d) `null`  

**Answer:** `a`

---

### Q13: What does `re.sub(r'\s+', ' ', "hello    world")` return in Python?

a) `"hello    world"`  
b) `"hello world"`  
c) `"helloworld"`  
d) Error  

**Answer:** `b`

---

## Fill in the Regex

### Q14: Complete the pattern to match a 3-digit number: `_____`

**Answer:** `\d{3}` or `[0-9]{3}`

---

### Q15: Complete the pattern to match words starting with 'h': `_____`

**Answer:** `\bh\w+` or `\b[hH]\w+` (case-insensitive)

---

### Q16: Complete the pattern to match the entire string as digits only: `_____`

**Answer:** `^\d+$`

---

### Q17: Complete the pattern to match "color" or "colour": `_____`

**Answer:** `colou?r`

---

### Q18: Complete the pattern to match any whitespace: `_____`

**Answer:** `\s+` or `\s`

---

## Pattern Matching

### Q19: Which strings match the pattern `^[A-Z][a-z]+$`?

a) "Hello"  
b) "HELLO"  
c) "hello"  
d) "H"  

**Answer:** `a` (must start with uppercase, followed by one or more lowercase)

---

### Q20: Which strings match the pattern `\d{2,4}`?

a) "1"  
b) "12"  
c) "1234"  
d) "12345"  

**Answer:** `b` and `c` (2 to 4 digits)

---

## True or False

### Q21: The pattern `.*` matches any string, including empty string.

**Answer:** `True`

---

### Q22: `[a-z]` matches both uppercase and lowercase letters.

**Answer:** `False` (only lowercase)

---

### Q23: `^` always matches the start of a line when using multiline flag.

**Answer:** `True`

---

### Q24: `\w` matches letters, digits, and underscores.

**Answer:** `True`

---

### Q25: The pattern `a*` will always match at least one 'a'.

**Answer:** `False` (`*` means zero or more)

---

## Practical Application

### Q26: Write a regex pattern to validate that a string contains only letters and spaces.

**Answer:** `^[A-Za-z\s]+$`

---

### Q27: Write a regex pattern to find all 4-letter words.

**Answer:** `\b\w{4}\b`

---

### Q28: Write a regex pattern to match phone numbers in format XXX-XXX-XXXX.

**Answer:** `\d{3}-\d{3}-\d{4}`

---

### Q29: Write a regex pattern to match strings that start with "http://" or "https://".

**Answer:** `^https?://`

---

### Q30: Write a regex pattern to remove all digits from a string (for replacement).

**Answer:** `\d+` or `\d`

---

## Scoring

- **25-30 correct**: Excellent! You've mastered the basics. Move to intermediate level.
- **18-24 correct**: Good understanding. Review weak areas and practice more.
- **12-17 correct**: Keep practicing. Re-read the basics and try more examples.
- **Below 12**: Review the basics section again. Focus on understanding each concept.

---

## Review Topics Based on Your Score

### If you struggled with:
- **Anchors (`^`, `$`)**: Review how they work with full string matching
- **Character classes (`[]`)**: Practice with different character sets
- **Quantifiers (`*`, `+`, `?`, `{}`)**: Understand the difference between them
- **Word boundaries (`\b`)**: Practice matching whole words vs. partial matches
- **Escaping (`\`)**: Remember to escape special characters

---

**Next Steps:**
- Review incorrect answers
- Re-read relevant sections in [introduction.md](introduction.md) and [syntax-cheatsheet.md](syntax-cheatsheet.md)
- Try more examples in [simple-examples.md](simple-examples.md)
- Practice with [exercises-basic.md](exercises-basic.md)
- Check solutions in [../solutions/basic-solutions.md](../solutions/basic-solutions.md)

**Ready for intermediate level?** → [../02-intermediate/character-classes.md](../02-intermediate/character-classes.md)

