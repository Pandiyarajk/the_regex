# Intermediate Regex Quiz

Test your understanding of intermediate regex concepts.

## Multiple Choice Questions

### Q1: What does `[^0-9]` match?

a) Any digit  
b) Any non-digit  
c) Digits 0-9  
d) Nothing  

**Answer:** `b`

---

### Q2: What does `(\d{3})-(\d{3})-(\d{4})` capture for "123-456-7890"?

a) Three groups: "123", "456", "7890"  
b) One group: "123-456-7890"  
c) Four groups: "123", "-", "456", "-", "7890"  
d) Error  

**Answer:** `a`

---

### Q3: What does `(?:cat|dog)` do?

a) Matches "cat" or "dog" and captures it  
b) Matches "cat" or "dog" but doesn't capture  
c) Matches "catdog"  
d) Matches neither  

**Answer:** `b`

---

### Q4: What does `(?=\d)` represent?

a) Positive lookbehind  
b) Positive lookahead  
c) Negative lookahead  
d) Capturing group  

**Answer:** `b`

---

### Q5: What does `\b(\w+)\s+\1\b` match?

a) Any word  
b) A word followed by the same word  
c) Two different words  
d) Nothing  

**Answer:** `b`

---

### Q6: What does `[a-zA-Z0-9_]` match?

a) Same as `\w`  
b) Same as `\d`  
c) Same as `\s`  
d) Nothing  

**Answer:** `a`

---

### Q7: What does `(?<=@)[^.]+` extract?

a) Everything before @  
b) Domain name from email  
c) Everything after @  
d) Nothing  

**Answer:** `b`

---

### Q8: What does `(abc){2,3}` match?

a) "abc" 2 or 3 times  
b) "abcabc" or "abcabcabc"  
c) "ab" 2-3 times  
d) Both a and b  

**Answer:** `d`

---

### Q9: What does `(?!ing\b)\w+` match?

a) Words ending with "ing"  
b) Words not ending with "ing"  
c) Only "ing"  
d) Nothing  

**Answer:** `b`

---

### Q10: What does `[^aeiouAEIOU]` match?

a) Vowels  
b) Consonants  
c) Non-vowels  
d) Both b and c  

**Answer:** `d`

---

## Regex Correction Tasks

### Q11: Fix this pattern to match a 10-digit phone number: `\d{10}`

**Current issue:** Doesn't anchor to full string, so it matches 10 digits anywhere.

**Corrected pattern:** `^\d{10}$`

---

### Q12: Fix this pattern to extract domain from email: `@(.+)`

**Current issue:** Captures everything after @ including path if email is in URL.

**Corrected pattern:** `@([^\s]+)` or `@([^/\s]+)`

---

### Q13: Fix this pattern to match "color" or "colour": `colou?r`

**Current pattern is correct!** But if you want to be more explicit: `colou?r` or `colo(u|ur)r`

---

## Predict Matched Groups

### Q14: Pattern: `(\d{2})/(\d{2})/(\d{4})`  
Text: `"25/12/2023"`

What are the captured groups?

**Answer:**
- Group 1: "25"
- Group 2: "12"
- Group 3: "2023"

---

### Q15: Pattern: `(\w+)@(\w+\.\w+)`  
Text: `"user@example.com"`

What are the captured groups?

**Answer:**
- Group 1: "user"
- Group 2: "example.com"

---

### Q16: Pattern: `(?:Mr|Mrs|Ms)\.\s+(\w+)`  
Text: `"Mr. John"`

What is captured?

**Answer:**
- Group 1: "John" (title not captured due to non-capturing group)

---

## Write Complex Regex

### Q17: Write a pattern to validate password with:
- At least 8 characters
- Contains uppercase
- Contains lowercase  
- Contains digit

**Answer:** `^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$`

---

### Q18: Write a pattern to extract hashtags from text.

**Answer:** `#(\w+)`

---

### Q19: Write a pattern to find duplicate words (case-sensitive).

**Answer:** `\b(\w+)\s+\1\b`

---

### Q20: Write a pattern to extract domain from URL (http/https).

**Answer:** `https?://(?:www\.)?([^/]+)`

---

## Debug Faulty Patterns

### Q21: Pattern: `\d{3}-\d{3}-\d{4}`  
Issue: Matches "123-456-7890" in "abc123-456-7890xyz"

**Fix:** Add anchors: `^\d{3}-\d{3}-\d{4}$`

---

### Q22: Pattern: `[a-z]+`  
Issue: Matches partial words like "hello" in "Hello"

**Fix:** Add word boundaries: `\b[a-z]+\b` or use case-insensitive flag

---

### Q23: Pattern: `.*@.*\..*`  
Issue: Too permissive, matches invalid emails

**Fix:** More specific: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`

---

## Practical Application

### Q24: Write a regex to extract all prices in format $XX.XX from text.

**Answer:** `\$(\d+\.\d{2})`

---

### Q25: Write a regex to validate Indian phone number (10 digits, starts with 6-9).

**Answer:** `^[6-9]\d{9}$`

---

### Q26: Write a regex to find words that start and end with the same letter.

**Answer:** `\b([a-zA-Z])[a-zA-Z]*\1\b`

---

### Q27: Write a regex to extract time in format HH:MM:SS.

**Answer:** `(\d{2}):(\d{2}):(\d{2})`

---

### Q28: Write a regex to validate username: 3-20 chars, alphanumeric and underscore only.

**Answer:** `^[a-zA-Z0-9_]{3,20}$`

---

## Advanced Questions

### Q29: What does `(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}` do?

a) Matches password with all requirements  
b) Matches any 8+ character string  
c) Matches strings with digits, lowercase, uppercase  
d) Both a and c  

**Answer:** `d`

---

### Q30: Explain the difference between `(cat|dog)` and `(?:cat|dog)`.

**Answer:**  
- `(cat|dog)` - Capturing group, saves matched text  
- `(?:cat|dog)` - Non-capturing group, doesn't save matched text  
Both match "cat" or "dog", but only the first captures it.

---

## Scoring

- **25-30 correct**: Excellent! You've mastered intermediate concepts. Ready for advanced!
- **18-24 correct**: Good understanding. Review weak areas and practice more.
- **12-17 correct**: Keep practicing. Re-read intermediate sections.
- **Below 12**: Review intermediate concepts. Focus on grouping and lookarounds.

---

## Review Topics

### If you struggled with:
- **Character classes**: Practice with ranges and negation
- **Grouping**: Understand capturing vs non-capturing groups
- **Lookarounds**: Practice with positive/negative lookaheads
- **Backreferences**: Review how `\1`, `\2` work
- **Complex patterns**: Break down into smaller parts

---

**Next Steps:**
- Review incorrect answers
- Practice with [exercises-intermediate.md](exercises-intermediate.md)
- Check solutions in [../solutions/intermediate-solutions.md](../solutions/intermediate-solutions.md)
- Try more examples in [medium-examples.md](medium-examples.md)

**Ready for advanced level?** → [../03-advanced/backreferences.md](../03-advanced/backreferences.md)

