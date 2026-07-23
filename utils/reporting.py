"""
Reporting Utilities
-------------------
Reusable functions for displaying analysis output
in a clean and consistent format.
Version: 1.0
"""

def print_section(title):
    """Print a major report section."""
    print("\n" + "=" * 60)
    print(title.upper())
    print("=" * 60)

def print_subsection(title):
    """Print a subsection heading."""
    print("\n" + title)
    print("-" * 40)

def print_business_insight(text):
    print()                      # Blank line before section
    print("Business Insight")
    print("-" * 40)
    print(text)
    print()                      # Optional blank line after section

def print_blank():
    """Print a blank line."""
    print()

def print_key_findings(text):
    """
    Print the Key Findings section.
    """

    print()
    print("Key Findings")
    print("-" * 40)
    print(text)

def print_recommendations(text):
    """
    Print the Strategic Recommendations section.
    """

    print()
    print("Strategic Recommendations")
    print("-" * 40)
    print(text)