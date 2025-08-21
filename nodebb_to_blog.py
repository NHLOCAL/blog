#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import argparse
from urllib.parse import urlparse, urljoin
from datetime import date
from bs4 import BeautifulSoup
from markdownify import markdownify as md

DESCRIPTION = """
NodeBB First Post to Blog Converter.

Accepts both full topic URLs (.../topic/123/...) and short post URLs (.../post/456).
If a short URL is provided, it will be automatically resolved to its full topic URL.

Modes:
1. Preview: python nodebb_to_blog.py <URL>
2. Save:     python nodebb_to_blog.py <URL> -o post.md -c Category -t Tag
"""

# --- פונקציות עזר ---

def resolve_url_if_needed(url):
    """
    Checks if the URL is a short post URL. If so, resolves it to the full topic URL.
    Otherwise, returns the original URL.
    """
    parsed_url = urlparse(url)
    
    if '/post/' not in parsed_url.path:
        return url

    print(f"Short URL detected: {url}")
    print("Resolving to the full topic URL...")

    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    match = re.search(r'/post/(\d+)', parsed_url.path)
    
    if not match:
        print(f"Error: Could not extract Post ID from short URL: {url}")
        exit(1)
        
    pid = match.group(1)
    api_url = f"{base_url}/api/post/{pid}"

    try:
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        
        # --- התיקון כאן ---
        # ה-API מחזיר טקסט פשוט, לא JSON. נקרא אותו עם .text
        relative_path = response.text
        
        # התשובה עשויה להגיע עם מרכאות מסביב, ננקה אותן
        relative_path = relative_path.strip('"')

        # נוודא שהנתיב שקיבלנו נראה תקין
        if relative_path and relative_path.startswith('/topic/'):
            resolved_url = urljoin(base_url, relative_path)
            print(f"Successfully resolved to: {resolved_url}")
            return resolved_url
        else:
            raise ValueError(f"API response for the post did not return a valid topic path. Got: '{relative_path}'")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: API request to resolve short URL failed. {e}")
        exit(1)
    except ValueError as e:
        print(f"Error: Could not process API response for the post. {e}")
        exit(1)


def get_tid_and_base_url(thread_url):
    try:
        parsed_url = urlparse(thread_url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        match = re.search(r'/topic/(\d+)', parsed_url.path)
        if not match:
            raise ValueError("Could not find topic ID (TID) in the URL. Ensure the URL is a valid topic URL.")
            
        tid = match.group(1)
        return tid, base_url
    except Exception as e:
        print(f"Error: Invalid URL format provided. {e}")
        exit(1)

def fetch_first_post(api_url):
    try:
        print(f"Fetching data from: {api_url}")
        response = requests.get(api_url, timeout=15)
        response.raise_for_status()
        
        data = response.json()
        
        if 'posts' not in data or not data['posts']:
            raise ValueError("API response does not contain any posts.")
            
        first_post = data['posts'][0]
        thread_title = data.get('title', 'Untitled Thread')
        
        print("Successfully fetched thread data.")
        return thread_title, first_post
        
    except requests.exceptions.RequestException as e:
        print(f"Error: Network or API request failed. {e}")
        exit(1)
    except (ValueError, KeyError) as e:
        print(f"Error: Could not parse API response. {e}")
        exit(1)

def preprocess_html_and_convert_to_md(html_content, base_url):
    if not html_content:
        return ""

    soup = BeautifulSoup(html_content, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src')
        if src and not src.startswith(('http://', 'https://', 'data:')):
            img['src'] = urljoin(base_url, src)
    
    processed_html = str(soup)
    markdown_content = md(processed_html, heading_style="ATX", code_style="FENCED")
    cleaned_markdown = re.sub(r'> @\S+\s+כתב\s+ב[^:]+:\s*', '> ', markdown_content, flags=re.MULTILINE)

    return cleaned_markdown.strip()

def create_blog_post_content(title, markdown, args):
    post_date = date.today().strftime('%Y-%m-%d')
    categories_yaml = '\n'.join([f"- {c}" for c in args.categories]) if args.categories else ''
    tags_yaml = '\n'.join([f"- {t}" for t in args.tags]) if args.tags else ''
    
    front_matter = [
        "---",
        f"title: \"{title.replace('\"', '\\\"')}\"",
        "layout: post",
        f"date: '{post_date}'"
    ]
    
    if categories_yaml:
        front_matter.append(f"categories:\n{categories_yaml}")
    if tags_yaml:
        front_matter.append(f"tags:\n{tags_yaml}")
    if args.description:
        front_matter.append(f"description: \"{args.description.replace('\"', '\\\"')}\"")
    if args.featured_image:
        front_matter.append(f"featured_image: \"{args.featured_image}\"")
        
    front_matter.append("---")
    
    return "\n".join(front_matter) + "\n\n" + markdown

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text).strip('-')
    return text

def main():
    parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument('url', help='The full topic or short post URL of the NodeBB thread.')
    parser.add_argument('--output', '-o', help='(Save Mode) Output filename for the Markdown file.')
    parser.add_argument('--categories', '-c', nargs='+', help='(Save Mode) A list of categories.')
    parser.add_argument('--tags', '-t', nargs='+', help='(Save Mode) A list of tags.')
    parser.add_argument('--description', '-d', help='(Save Mode) A short description.')
    parser.add_argument('--featured-image', '-i', help='(Save Mode) Path to a featured image.')
    
    args = parser.parse_args()

    topic_url = resolve_url_if_needed(args.url)
    
    tid, base_url = get_tid_and_base_url(topic_url)
    api_url = f"{base_url}/api/topic/{tid}"
    title, first_post = fetch_first_post(api_url)
    html_content = first_post.get('content', '')
    
    print("Processing post content...")
    markdown_content = preprocess_html_and_convert_to_md(html_content, base_url)
    print("Content processed successfully.\n")

    is_save_mode = any([
        args.output,
        args.categories,
        args.tags,
        args.description,
        args.featured_image
    ])

    if is_save_mode:
        print("Save mode activated. Generating blog post file...")
        full_post_content = create_blog_post_content(title, markdown_content, args)

        output_filename = args.output
        if not output_filename:
            output_filename = f"{date.today().strftime('%Y-%m-%d')}-{slugify(title)}.md"

        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(full_post_content)
            print(f"Success! Blog post saved to: {output_filename}")
        except IOError as e:
            print(f"Error: Could not write to file '{output_filename}'. {e}")
            exit(1)
    else:
        print("--- PREVIEW MODE ---")
        print("Displaying converted Markdown content. No file will be saved.\n")
        print("="*40)
        print(markdown_content)
        print("="*40)
        print("\nTo save this content to a file with front matter,")
        print("re-run the script with save options (e.g., -o, -c, -t).")
        print("Use --help for more details.")


if __name__ == '__main__':
    main()