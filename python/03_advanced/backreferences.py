#!/usr/bin/env python3
"""
Backreferences - Advanced Examples

Demonstrates:
- Basic backreferences \1, \2
- Named group backreferences
- Practical applications
"""

import re


def example_repeated_words():
    """Find repeated words"""
    print("=" * 60)
    print("Example: Find Repeated Words")
    print("=" * 60)
    
    pattern = r'\b(\w+)\s+\1\b'
    text = "the the cat sat on the the mat"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Repeated words found: {matches}")
    
    # Find full matches
    for match in re.finditer(pattern, text):
        print(f"  Found: '{match.group()}'")
    print()


def example_html_tags():
    """Match HTML tags with backreferences"""
    print("=" * 60)
    print("Example: Match HTML Tags")
    print("=" * 60)
    
    pattern = r'<(\w+)>.*?</\1>'
    text = "<div>Hello</div> and <p>World</p>"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Tag names found: {matches}")
    
    # Find full matches
    for match in re.finditer(pattern, text):
        print(f"  Found: '{match.group()}'")
    print()


def example_named_group_backreference():
    """Named group backreferences"""
    print("=" * 60)
    print("Example: Named Group Backreferences")
    print("=" * 60)
    
    pattern = r'<(?P<tag>\w+)>.*?</(?P=tag)>'
    text = "<div>content</div>"
    
    match = re.search(pattern, text)
    if match:
        print(f"Pattern: {pattern}")
        print(f"Text: {text}")
        print(f"Tag name: {match.group('tag')}")
        print(f"Full match: {match.group()}")
    print()


def example_quoted_strings():
    """Match quoted strings with matching quotes"""
    print("=" * 60)
    print("Example: Quoted Strings with Matching Quotes")
    print("=" * 60)
    
    pattern = r'(["\'])(.*?)\1'
    test_cases = [
        '"hello"',
        "'world'",
        '"hello\'',
        "'test\""
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        if match:
            print(f"✓ '{text}' -> Content: '{match.group(2)}'")
        else:
            print(f"✗ '{text}'")
    print()


def example_phone_area_code_equals_exchange():
    """Phone number where area code equals exchange"""
    print("=" * 60)
    print("Example: Phone with Area Code = Exchange")
    print("=" * 60)
    
    pattern = r'(\d{3})-\1-\d{4}'
    test_cases = [
        "123-123-4567",
        "123-456-7890"
    ]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def example_repeated_sequences():
    """Find repeated sequences"""
    print("=" * 60)
    print("Example: Find Repeated Sequences")
    print("=" * 60)
    
    pattern = r'(.{2,})\1+'
    text = "ababab hellohello 123123123"
    
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    for match in re.finditer(pattern, text):
        sequence = match.group(1)
        print(f"  Found sequence '{sequence}' repeated")
    print()


def example_palindromic_words():
    """Find palindromic words (simplified)"""
    print("=" * 60)
    print("Example: Palindromic Words (Simplified)")
    print("=" * 60)
    
    # Words starting and ending with same letter
    pattern = r'\b([a-zA-Z])[a-zA-Z]*\1\b'
    text = "level radar hello test"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")
    
    # Full matches
    for match in re.finditer(pattern, text):
        print(f"  Found: '{match.group()}'")
    print()


def main():
    """Run all backreference examples"""
    print("\n" + "=" * 60)
    print("BACKREFERENCES - PYTHON EXAMPLES")
    print("=" * 60 + "\n")
    
    example_repeated_words()
    example_html_tags()
    example_named_group_backreference()
    example_quoted_strings()
    example_phone_area_code_equals_exchange()
    example_repeated_sequences()
    example_palindromic_words()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

