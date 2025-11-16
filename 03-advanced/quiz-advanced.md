# Advanced Regex Quiz

Test your mastery of advanced regex concepts.

## Multiple Choice Questions

### Q1: What does `\1` refer to in a regex pattern?

a) First character  
b) First capturing group  
c) First match  
d) Beginning of string  

**Answer:** `b`

---

### Q2: What is the difference between `.*` and `.*?`?

a) `.*` is greedy, `.*?` is lazy  
b) `.*` is lazy, `.*?` is greedy  
c) They're the same  
d) `.*?` doesn't exist  

**Answer:** `a`

---

### Q3: What does `(?:pattern)` create?

a) Capturing group  
b) Non-capturing group  
c) Named group  
d) Lookahead  

**Answer:** `b`

---

### Q4: What does `(?=pattern)` represent?

a) Positive lookbehind  
b) Positive lookahead  
c) Negative lookahead  
d) Capturing group  

**Answer:** `b`

---

### Q5: What does `(?<=pattern)` represent?

a) Positive lookbehind  
b) Positive lookahead  
c) Negative lookbehind  
d) Capturing group  

**Answer:** `a`

---

### Q6: What does `\b(\w+)\s+\1\b` match?

a) Any word  
b) Repeated word  
c) Two different words  
d) Nothing  

**Answer:** `b`

---

### Q7: Which is more efficient: `".*?"` or `"[^"]*"`?

a) `".*?"`  
b) `"[^"]*"`  
c) They're the same  
d) Depends on text  

**Answer:** `b` (negated character class avoids backtracking)

---

### Q8: What does `(?P<name>pattern)` create in Python?

a) Non-capturing group  
b) Named capturing group  
c) Lookahead  
d) Backreference  

**Answer:** `b`

---

### Q9: Can regex match truly nested structures like HTML?

a) Yes, always  
b) No, never  
c) Limited support in some engines  
d) Only with special flags  

**Answer:** `c` (limited - recursion not supported in all engines)

---

### Q10: What does `(?!pattern)` represent?

a) Positive lookahead  
b) Negative lookahead  
c) Positive lookbehind  
d) Negative lookbehind  

**Answer:** `b`

---

## Write Complex Regex

### Q11: Write a pattern to validate password with uppercase, lowercase, digit, and special char.

**Answer:** `^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$`

---

### Q12: Write a pattern to extract domain from email using lookbehind.

**Answer:** `(?<=@)[^.]+` or `(?<=@)[^.\s]+`

---

### Q13: Write a pattern to find HTML tags with matching opening/closing tags.

**Answer:** `<(\w+)>.*?</\1>` or `<(\w+)[^>]*>.*?</\1>`

---

### Q14: Write a pattern to match quoted strings with matching quotes.

**Answer:** `(["'])(.*?)\1`

---

### Q15: Write a pattern to find repeated 3-character sequences.

**Answer:** `(.{3})\1+`

---

## Debug Faulty Patterns

### Q16: Pattern: `.*` on text `"<div>content</div>"`  
Issue: Matches too much

**Fix:** Use lazy: `.*?` or better: `[^<]+`

---

### Q17: Pattern: `(\w+)\s+\1`  
Issue: Matches partial words

**Fix:** Add word boundaries: `\b(\w+)\s+\1\b`

---

### Q18: Pattern: `(?<=@).+`  
Issue: Matches everything after @ including path

**Fix:** `(?<=@)[^/\s]+` or `(?<=@)[^.]+`

---

## Predict Output

### Q19: Pattern: `\b(\w)(\w)\w*\2\1\b`  
Text: `"level radar test"`

What matches?

**Answer:** "level", "radar" (palindromic words)

---

### Q20: Pattern: `<(\w+)>.*?</\1>`  
Text: `"<div>Hello</div><span>World</span>"`

What are the captured groups?

**Answer:** Group 1: "div" (from first match), Group 1: "span" (from second match)

---

### Q21: Pattern: `(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}`  
Text: `"Password123"`

Does it match?

**Answer:** Yes (has digit, lowercase, uppercase, 8+ chars)

---

## Advanced Concepts

### Q22: Explain catastrophic backtracking.

**Answer:** When a regex pattern causes exponential time complexity due to excessive backtracking, often with nested quantifiers like `(a+)+`.

---

### Q23: What's the difference between `(?P<name>pattern)` and `(?<name>pattern)`?

**Answer:**  
- `(?P<name>pattern)` - Python syntax for named groups
- `(?<name>pattern)` - JavaScript/PCRE syntax for named groups

---

### Q24: Can you use backreferences in lookarounds?

**Answer:** Generally no in most engines. Lookarounds are evaluated independently.

---

### Q25: What's a better alternative to `.*?` for matching until a character?

**Answer:** Negated character class: `[^x]*` (more efficient, avoids backtracking)

---

## Practical Application

### Q26: Write regex to extract IP:Port combinations.

**Answer:** `(\d{1,3}(?:\.\d{1,3}){3}):(\d{1,5})`

---

### Q27: Write regex to find words where first and last letters match.

**Answer:** `\b([a-zA-Z])\w*\1\b`

---

### Q28: Write regex to validate phone where area code = exchange.

**Answer:** `^(\d{3})-\1-\d{4}$`

---

### Q29: Write regex to extract key-value pairs from `key="value"`.

**Answer:** `(\w+)="([^"]*)"`

---

### Q30: Write regex to match balanced parentheses (2 levels).

**Answer:** `\(([^()]+|\([^()]*\))*\)`

---

## Scoring

- **25-30 correct**: Master level! You understand advanced regex concepts deeply.
- **18-24 correct**: Excellent! Minor gaps, keep practicing.
- **12-17 correct**: Good understanding. Review advanced topics.
- **Below 12**: Review advanced concepts. Focus on backreferences and lookarounds.

---

## Review Topics

### If you struggled with:
- **Backreferences**: Practice with repeated patterns
- **Greedy vs Lazy**: Understand when to use each
- **Lookarounds**: Practice positive/negative lookaheads/behinds
- **Complex patterns**: Break down into smaller parts
- **Performance**: Learn about backtracking and alternatives

---

**Next Steps:**
- Review incorrect answers
- Practice with [exercises-advanced.md](exercises-advanced.md)
- Check solutions in [../solutions/advanced-solutions.md](../solutions/advanced-solutions.md)
- Try real-world projects in [../04-real-world-projects/](../04-real-world-projects/)

**Ready for real-world projects?** → [../04-real-world-projects/project-email-validator.md](../04-real-world-projects/project-email-validator.md)

