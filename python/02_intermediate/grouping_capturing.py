#!/usr/bin/env python3
"""
Grouping and Capturing - Intermediate Examples

Demonstrates:
- Capturing groups ()
- Non-capturing groups (?:)
- Named groups (?P<name>)
- Group extraction
"""

import re


def example_basic_grouping():
    """Basic grouping"""
    print("=" * 60)
    print("Basic Grouping")
    print("=" * 60)
    
    pattern = r'(abc)+'
    test_cases = ["abc", "abcabc", "abcabcabc", "ab"]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        if match:
            print(f"✓ '{text}' -> Matched: {match.group()}")
        else:
            print(f"✗ '{text}'")
    print()


def example_extract_date_components():
    """Extract date components"""
    print("=" * 60)
    print("Extract Date Components")
    print("=" * 60)
    
    pattern = r'(\d{2})/(\d{2})/(\d{4})'
    text = "Date: 25/12/2023"
    
    match = re.search(pattern, text)
    if match:
        day = match.group(1)
        month = match.group(2)
        year = match.group(3)
        print(f"Pattern: {pattern}")
        print(f"Text: {text}")
        print(f"Day: {day}, Month: {month}, Year: {year}")
    print()


def example_named_groups():
    """Named groups"""
    print("=" * 60)
    print("Named Groups")
    print("=" * 60)
    
    pattern = r'(?P<day>\d{2})/(?P<month>\d{2})/(?P<year>\d{4})'
    text = "Date: 25/12/2023"
    
    match = re.search(pattern, text)
    if match:
        print(f"Pattern: {pattern}")
        print(f"Text: {text}")
        print(f"Day: {match.group('day')}")
        print(f"Month: {match.group('month')}")
        print(f"Year: {match.group('year')}")
    print()


def example_non_capturing_groups():
    """Non-capturing groups"""
    print("=" * 60)
    print("Non-Capturing Groups")
    print("=" * 60)
    
    # With capturing group
    pattern1 = r'(Mr|Mrs|Ms)\.\s+(\w+)'
    # With non-capturing group
    pattern2 = r'(?:Mr|Mrs|Ms)\.\s+(\w+)'
    
    text = "Mr. John Smith"
    
    match1 = re.search(pattern1, text)
    match2 = re.search(pattern2, text)
    
    print(f"Pattern (capturing): {pattern1}")
    if match1:
        print(f"  Groups: {match1.groups()}")
    
    print(f"\nPattern (non-capturing): {pattern2}")
    if match2:
        print(f"  Groups: {match2.groups()}")
    print()


def example_phone_format():
    """Phone format with groups"""
    print("=" * 60)
    print("Phone Format with Groups")
    print("=" * 60)
    
    pattern = r'(\d{3}-){2}\d{4}'
    test_cases = ["123-456-7890", "123-456"]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def example_alternation():
    """Alternation with groups"""
    print("=" * 60)
    print("Alternation with Groups")
    print("=" * 60)
    
    pattern = r'(cat|dog|bird)'
    text = "I have a cat and a dog"
    
    matches = re.findall(pattern, text)
    print(f"Pattern: {pattern}")
    print(f"Text: {text}")
    print(f"Matches: {matches}")
    print()


def example_file_extensions():
    """File extensions"""
    print("=" * 60)
    print("File Extensions")
    print("=" * 60)
    
    pattern = r'\.(jpg|jpeg|png|gif)$'
    test_cases = [".jpg", ".jpeg", ".png", ".gif", ".txt"]
    
    print(f"Pattern: {pattern}")
    for text in test_cases:
        match = re.search(pattern, text)
        result = "✓" if match else "✗"
        print(f"{result} '{text}'")
    print()


def example_extract_email_components():
    """Extract email components"""
    print("=" * 60)
    print("Extract Email Components")
    print("=" * 60)
    
    pattern = r'(\w+)@(\w+\.\w+)'
    text = "user@example.com"
    
    match = re.search(pattern, text)
    if match:
        local_part = match.group(1)
        domain = match.group(2)
        print(f"Pattern: {pattern}")
        print(f"Text: {text}")
        print(f"Local part: {local_part}")
        print(f"Domain: {domain}")
    print()


def main():
    """Run all grouping examples"""
    print("\n" + "=" * 60)
    print("GROUPING AND CAPTURING - PYTHON EXAMPLES")
    print("=" * 60 + "\n")
    
    example_basic_grouping()
    example_extract_date_components()
    example_named_groups()
    example_non_capturing_groups()
    example_phone_format()
    example_alternation()
    example_file_extensions()
    example_extract_email_components()
    
    print("=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

