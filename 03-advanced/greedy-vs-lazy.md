# Greedy vs Lazy Matching

Understanding the difference between greedy and lazy quantifiers is crucial for writing correct regex patterns.

## What is Greedy Matching?

**Greedy quantifiers** match as much as possible while still allowing the overall pattern to match.

### Greedy Quantifiers

- `*` - Zero or more (greedy)
- `+` - One or more (greedy)
- `?` - Zero or one (greedy)
- `{n}` - Exactly n
- `{n,}` - n or more (greedy)
- `{n,m}` - Between n and m (greedy)

### Example: Greedy Matching

**Pattern:** `.*`

**Text:** `"Hello <div>content</div> World"`

**Match:** `"Hello <div>content</div> World"` (matches everything)

The `.*` is greedy - it matches as much as possible.

## What is Lazy Matching?

**Lazy (non-greedy) quantifiers** match as little as possible while still allowing the overall pattern to match.

### Lazy Quantifiers

- `*?` - Zero or more (lazy)
- `+?` - One or more (lazy)
- `??` - Zero or one (lazy)
- `{n,}?` - n or more (lazy)
- `{n,m}?` - Between n and m (lazy)

### Example: Lazy Matching

**Pattern:** `.*?`

**Text:** `"Hello <div>content</div> World"`

**Match:** `""` (empty string - matches as little as possible)

But with context:

**Pattern:** `<.*?>`

**Text:** `"Hello <div>content</div> World"`

**Match:** `"<div>"` (matches minimal - just the tag)

## Side-by-Side Comparison

### Example 1: Extracting HTML Tags

**Text:** `"<div>content</div> and <span>more</span>"`

#### Greedy: `<.*>`

```
Match: "<div>content</div> and <span>more</span>"
```

Matches from first `<` to last `>` - too much!

#### Lazy: `<.*?>`

```
Matches: "<div>", "</div>", "<span>", "</span>"
```

Matches each tag individually - correct!

### Code Examples

**Python:**
```python
import re

text = "<div>content</div> and <span>more</span>"

# Greedy
greedy_pattern = r'<.*>'
greedy_match = re.search(greedy_pattern, text)
print(greedy_match.group())  # "<div>content</div> and <span>more</span>"

# Lazy
lazy_pattern = r'<.*?>'
lazy_matches = re.findall(lazy_pattern, text)
print(lazy_matches)  # ['<div>', '</div>', '<span>', '</span>']
```

**JavaScript:**
```javascript
const text = "<div>content</div> and <span>more</span>";

// Greedy
const greedyPattern = /<.*>/;
const greedyMatch = text.match(greedyPattern);
console.log(greedyMatch[0]); // "<div>content</div> and <span>more</span>"

// Lazy
const lazyPattern = /<.*?>/g;
const lazyMatches = text.match(lazyPattern);
console.log(lazyMatches); // ['<div>', '</div>', '<span>', '</span>']
```

## Practical Examples

### Example 1: Extracting Content Between Tags

**Text:** `"<div>Hello</div><div>World</div>"`

#### Greedy: `<div>.*</div>`

```
Match: "<div>Hello</div><div>World</div>"
```

Matches everything from first `<div>` to last `</div>`.

#### Lazy: `<div>.*?</div>`

```
Matches: "<div>Hello</div>", "<div>World</div>"
```

Matches each div separately.

### Example 2: Extracting Quoted Text

**Text:** `'He said "hello" and "world"'`

#### Greedy: `".*"`

```
Match: "hello" and "world"
```

Matches from first quote to last quote.

#### Lazy: `".*?"`

```
Matches: "hello", "world"
```

Matches each quoted string separately.

### Example 3: Matching Numbers

**Text:** `"123 456 789"`

#### Greedy: `\d+`

```
Matches: "123", "456", "789"
```

With `findall()`, each number is matched separately (greedy within each match).

#### Lazy: `\d+?`

```
Matches: "1", "2", "3", "4", "5", "6", "7", "8", "9"
```

Matches minimal - each digit separately.

## When to Use Greedy

Use greedy matching when you want to:
- Match as much as possible
- Extract the longest possible match
- Match until a specific boundary

### Example: Extract Everything Until End

```
^.*$
```

Matches the entire string (greedy is appropriate here).

### Example: Match Until Specific Character

```
[^,]+
```

Matches one or more non-comma characters (greedy - matches until comma).

## When to Use Lazy

Use lazy matching when you want to:
- Match the shortest possible string
- Extract multiple separate matches
- Avoid matching too much

### Example: Extract Multiple Tags

```
<.*?>
```

Matches each HTML tag separately.

### Example: Extract Quoted Strings

```
"[^"]*"
```

Or with lazy:

```
".*?"
```

Both work, but `"[^"]*"` is more efficient (doesn't backtrack).

## Performance Considerations

### Greedy Can Be Slow

Greedy quantifiers can cause **catastrophic backtracking** with certain patterns:

```
(a+)+b
```

On text like "aaaaac", this can be very slow.

### Lazy Can Also Be Slow

Lazy quantifiers backtrack too, which can be slow:

```
.*?b
```

On text without 'b', this checks every position.

### Better Alternatives

Sometimes, negated character classes are more efficient:

```
<[^>]+>        # Better than <.*?>
"[^"]*"        # Better than ".*?"
```

## Common Patterns

### Extract Content Between Delimiters

**Greedy (wrong):**
```
<tag>.*</tag>
```

**Lazy (better):**
```
<tag>.*?</tag>
```

**Best (most efficient):**
```
<tag>[^<]*</tag>
```

### Match Until Character

**Greedy:**
```
[^,]+
```

Matches until comma (efficient).

**Lazy:**
```
.*?,
```

Matches until comma (less efficient due to backtracking).

## Tips and Best Practices

1. **Use lazy** when extracting multiple separate items
2. **Use greedy** when matching until a boundary
3. **Prefer negated classes** (`[^x]+`) over lazy (`.*?`) when possible
4. **Test with edge cases** - empty strings, no matches, etc.
5. **Consider performance** - lazy can be slower than negated classes
6. **Document your choice** - explain why greedy or lazy

## Exercises

Try these:

1. Extract all HTML tags from text: `_____`
2. Extract quoted strings (each separately): `_____`
3. Match content between parentheses: `_____`
4. Extract email addresses from text: `_____`
5. Match numbers with optional decimals: `_____`

---

**Next:** [complex-examples.md](complex-examples.md) for advanced patterns!

