#!/usr/bin/env python3
"""
Script to find markdown files where the title metadata differs from the first heading.
"""

import os
import re
import yaml
from pathlib import Path
from typing import Optional, Tuple, List


def extract_frontmatter_and_content(file_path: str) -> Tuple[Optional[dict], str]:
    """
    Extract YAML frontmatter and markdown content from a file.
    
    Returns:
        Tuple of (frontmatter_dict, content_without_frontmatter)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Try with different encoding
        try:
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None, ""
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None, ""
    
    # Check if file starts with frontmatter
    if not content.startswith('---'):
        return None, content
    
    # Find the end of frontmatter
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None, content
    
    frontmatter_text = parts[1].strip()
    markdown_content = parts[2].strip()
    
    # Parse YAML frontmatter
    try:
        frontmatter = yaml.safe_load(frontmatter_text)
        return frontmatter, markdown_content
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {file_path}: {e}")
        return None, markdown_content


def extract_first_heading(content: str) -> Optional[str]:
    """
    Extract the first heading (# heading) from markdown content.
    
    Returns:
        The first heading text without the # symbol, or None if no heading found.
    """
    lines = content.split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('# '):
            # Extract heading text, removing the # and any trailing whitespace
            heading = line[2:].strip()
            return heading
    
    return None


def normalize_text(text: str) -> str:
    """
    Normalize text for comparison by removing extra whitespace and converting to lowercase.
    """
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text.strip().lower())


def find_title_mismatches(root_dir: str) -> List[dict]:
    """
    Find all markdown files where title metadata differs from first heading.
    
    Returns:
        List of dictionaries with file info and mismatch details.
    """
    mismatches = []
    root_path = Path(root_dir)
    
    # Find all .md files recursively
    md_files = list(root_path.rglob('*.md'))
    
    print(f"Found {len(md_files)} markdown files to analyze...")
    
    for md_file in md_files:
        file_path = str(md_file)
        relative_path = md_file.relative_to(root_path)
        
        # Extract frontmatter and content
        frontmatter, content = extract_frontmatter_and_content(file_path)
        
        # Skip files without frontmatter
        if not frontmatter:
            continue
            
        # Get title from frontmatter
        title_metadata = frontmatter.get('title')
        if not title_metadata:
            continue
            
        # Get first heading from content
        first_heading = extract_first_heading(content)
        if not first_heading:
            continue
            
        # Skip if heading is a template variable that will render as the title
        if first_heading.strip() in ['{{ page.title}}', '{{ page.title }}', '{{page.title}}', '{{page.title }}']:
            continue
        
        # Compare normalized versions
        normalized_title = normalize_text(str(title_metadata))
        normalized_heading = normalize_text(first_heading)
        
        if normalized_title != normalized_heading:
            mismatches.append({
                'file': str(relative_path),
                'title_metadata': title_metadata,
                'first_heading': first_heading,
                'normalized_title': normalized_title,
                'normalized_heading': normalized_heading
            })
    
    return mismatches


def main():
    """Main function to run the analysis."""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("Analyzing markdown files for title/heading mismatches...")
    print(f"Root directory: {root_dir}")
    print("-" * 60)
    
    mismatches = find_title_mismatches(root_dir)
    
    if not mismatches:
        print("✅ No mismatches found! All files have consistent titles and headings.")
        return
    
    print(f"Found {len(mismatches)} files with title/heading mismatches:")
    print()
    
    for i, mismatch in enumerate(mismatches, 1):
        print(f"{i:2d}. {mismatch['file']}")
        print(f"     Title metadata: '{mismatch['title_metadata']}'")
        print(f"     First heading:  '{mismatch['first_heading']}'")
        print()
    
    print("-" * 60)
    print(f"Total mismatches: {len(mismatches)}")
    
    # Also save to a file for easier review
    with open('title_mismatch_report.txt', 'w', encoding='utf-8') as f:
        f.write("Title/Heading Mismatch Report\n")
        f.write("=" * 40 + "\n\n")
        
        for i, mismatch in enumerate(mismatches, 1):
            f.write(f"{i:2d}. {mismatch['file']}\n")
            f.write(f"     Title metadata: '{mismatch['title_metadata']}'\n")
            f.write(f"     First heading:  '{mismatch['first_heading']}'\n\n")
        
        f.write(f"Total mismatches: {len(mismatches)}\n")
    
    print(f"Report also saved to: title_mismatch_report.txt")


if __name__ == "__main__":
    main()
