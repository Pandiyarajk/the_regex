#!/usr/bin/env python3
"""
Greedy vs Lazy Matching - Advanced Examples

Demonstrates:
- Greedy quantifiers (*, +, ?)
- Lazy quantifiers (*?, +?, ??)
- When to use each
"""

import re


def example_greedy_matching():
    """Greedy matching"""
    print("=" * 60)
    print("Greedy Matching")
    print("=" * 60)
    
    text = "<div>content</div><div>more</div>"
    
    # Greedy - matches too much
    pattern_greedy = r'<div>.*</div>'
    match_greedy = re.search(pattern_greedy, text)
    
    print(f"Text: {text}")
    print(f"\nGreedy pattern: {pattern_greedy}")
    if match_greedy:
        print(f"Match: '{match_greedy.group()}'")
        print("  (Matches from first <div> to last </div>)")
    print()


def example_lazy_matching():
    """Lazy matching"""
    print("=" * 60)
    print("Lazy Matching")
    print("=" * 60)
    
    text = "<div>content</div><div>more</div>"
    
    # Lazy - matches correctly
    pattern_lazy = r'<div>.*?</div>'
    matches_lazy = re.findall(pattern_lazy, text)
    
    print(f"Text: {text}")
    print(f"\nLazy pattern: {pattern_lazy}")
    print(f"Matches: {matches_lazy}")
    print("  (Matches each div separately)")
    print()


def example_extract_quoted_strings():
    """Extract quoted strings"""
    print("=" * 60)
    print("Extract Quoted Strings")
    print("=" * 60)
    
    text = 'He said "hello" and "world"'
    
    # Greedy - matches too much
    pattern_greedy = r'".*"'
    match_greedy = re.search(pattern_greedy, text)
    
    # Lazy - matches correctly
    pattern_lazy = r'".*?"'
    matches_lazy = re.findall(pattern_lazy, text)
    
    print(f"Text: {text}")
    print(f"\nGreedy pattern: {pattern_greedy}")
    if match_greedy:
        print(f"Match: '{match_greedy.group()}'")
        print("  (Matches from first quote to last quote)")
    
    print(f"\nLazy pattern: {pattern_lazy}")
    print(f"Matches: {matches_lazy}")
    print("  (Matches each quoted string separately)")
    print()


def example_better_alternative():
    """Better alternative: negated character class"""
    print("=" * 60)
    print("Better Alternative: Negated Character Class")
    print("=" * 60)
    
    text = "<div>content</div><div>more</div>"
    
    # Most efficient - negated character class
    pattern_efficient = r'<div>[^<]+</div>'
    matches = re.findall(pattern_efficient, text)
    
    print(f"Text: {text}")
    print(f"\nEfficient pattern: {pattern_efficient}")
    print(f"Matches: {matches}")
    print("  (More efficient than lazy matching)")
    print()


def example_numbers_lazy():
    """Numbers with lazy matching"""
    print("=" * 60)
    print("Numbers: Greedy vs Lazy")
    print("=" * 60)
    
    text = "123 456 789"
    
    # Greedy
    pattern_greedy = r'\d+'
    matches_greedy = re.findall(pattern_greedy, text)
    
    # Lazy
    pattern_lazy = r'\d+?'
    matches_lazy = re.findall(pattern_lazy, text)
    
    print(f"Text: {text}")
    print(f"\nGreedy pattern: {pattern_greedy}")
    print(f"Matches: {matches_greedy}")
    
    print(f"\nLazy pattern: {pattern_lazy}")
    print(f"Matches: {matches_lazy}")
    print("  (Matches each digit separately - usually not what you want)")
    print()


def example_match_until_character():
    """Match until specific character"""
    print("=" * 60)
    print("Match Until Character")
    print("=" * 60)
    
    text = "name=value,age=25,city=NYC"
    
    # Efficient - negated character class
    pattern1 = r'[^,]+'
    matches1 = re.findall(pattern1, text)
    
    # Less efficient - lazy
    pattern2 = r'.*?,'
    matches2 = re.findall(pattern2, text)
    
    print(f"Text: {text}")
    print(f"\nEfficient (negated class): {pattern1}")
    print(f"Matches: {matches1}")
    
    print(f"\nLazy: {pattern2}")
    print(f"Matches: {matches2}")
    print()


def main():
    """Run all greedy/lazy examples"""
    print("\n" + "=" * 60)
    print("GREEDY VS LAZY MATCHING - PYTHON EXAMPLES")
    print("=" * 60 + "\n")
    
    example_greedy_matching()
    example_lazy_matching()
    example_extract_quoted_strings()
    example_better_alternative()
    example_numbers_lazy()
    example_match_until_character()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)
    print("\nTips:")
    print("- Use lazy (*?) when extracting multiple separate items")
    print("- Use greedy (*) when matching until a boundary")
    print("- Prefer negated classes ([^x]+) over lazy when possible")


if __name__ == "__main__":
    main()

