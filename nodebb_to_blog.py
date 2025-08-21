#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import argparse
import os
from urllib.parse import urlparse, urljoin
from datetime import date
from bs4 import BeautifulSoup
from markdownify import markdownify as md

DESCRIPTION = """
NodeBB First Post to Blog Converter.

Accepts full topic URLs (.../topic/...) and short post URLs (.../post/...).

Modes:
1. Preview Mode: Run with only a URL to see the converted Markdown content.

2. Save Mode: Add save arguments (-o, -c, etc.) to generate a blog post file.
   - Downloads all images from the post into a specified image directory.
   - Renames images based on the output filename with a counter (e.g., my-post-1.jpg).
   - Allows overriding the post title with the --title/-T argument.
   - Allows specifying a custom image directory with --image-dir/-I.
   - Converts horizontal rules from '---' to '***' in the post body.
"""

# --- פונקציות עזר ---

def download_images_and_update_html(html_content, base_url, image_dir, image_base_name):
    if not html_content:
        return ""
    
    soup = BeautifulSoup(html_content, 'html.parser')
    os.makedirs(image_dir, exist_ok=True)
    
    img_tags = soup.find_all('img')
    print(f"Found {len(img_tags)} image(s) to process.")
    
    image_counter = 1
    
    for img_tag in img_tags:
        src = img_tag.get('src')
        if not src:
            continue

        absolute_url = urljoin(base_url, src)
        
        try:
            original_path = urlparse(absolute_url).path
            extension = os.path.splitext(original_path)[1] or '.jpg'

            new_filename = f"{image_base_name}-{image_counter}{extension}"
            local_path = os.path.join(image_dir, new_filename)

            print(f"Downloading image: {absolute_url} -> {local_path}")
            with requests.get(absolute_url, stream=True, timeout=20) as r:
                r.raise_for_status()
                with open(local_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            
            # הנתיב שייכתב ב-Markdown יהיה יחסי לקובץ
            relative_path = os.path.join(image_dir, new_filename).replace("", "/")
            if relative_path.startswith('docs/'):
                relative_path = '/' + relative_path[len('docs/'):]
            img_tag['src'] = relative_path
            img_tag['src'] = relative_path
            
            image_counter += 1

        except requests.exceptions.RequestException as e:
            print(f"Warning: Failed to download image {absolute_url}. Error: {e}")
        except Exception as e:
            print(f"Warning: An unexpected error occurred while processing image {absolute_url}. Error: {e}")

    return str(soup)

def resolve_url_if_needed(url):
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
        relative_path = response.text.strip('"')
        if relative_path and relative_path.startswith('/topic/'):
            resolved_url = urljoin(base_url, relative_path)
            print(f"Successfully resolved to: {resolved_url}")
            return resolved_url
        else:
            raise ValueError(f"API response did not return a valid topic path. Got: '{relative_path}'")
    except (requests.exceptions.RequestException, ValueError) as e:
        print(f"Error: Could not resolve short URL. {e}")
        exit(1)

def get_tid_and_base_url(thread_url):
    try:
        parsed_url = urlparse(thread_url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        match = re.search(r'/topic/(\d+)', parsed_url.path)
        if not match:
            raise ValueError("Could not find topic ID in URL.")
        return match.group(1), base_url
    except Exception as e:
        print(f"Error: Invalid URL format. {e}")
        exit(1)

def fetch_first_post(api_url):
    try:
        print(f"Fetching data from: {api_url}")
        response = requests.get(api_url, timeout=15)
        response.raise_for_status()
        data = response.json()
        if 'posts' not in data or not data['posts']:
            raise ValueError("API response contains no posts.")
        return data.get('title', 'Untitled'), data['posts'][0]
    except (requests.exceptions.RequestException, ValueError, KeyError) as e:
        print(f"Error: Failed to fetch or parse post data. {e}")
        exit(1)

def preprocess_html_and_convert_to_md(html_content):
    markdown_content = md(html_content, heading_style="ATX", code_style="FENCED")
    markdown_content = re.sub(r'^\s*---\s*$', '***', markdown_content, flags=re.MULTILINE)
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
    if categories_yaml: front_matter.append(f"categories:\n{categories_yaml}")
    if tags_yaml: front_matter.append(f"tags:\n{tags_yaml}")
    if args.description: front_matter.append(f"description: \"{args.description.replace('\"', '\\\"')}\"")
    if args.featured_image: front_matter.append(f"featured_image: \"{args.featured_image}\"")
    front_matter.append("---")
    return "\n".join(front_matter) + "\n\n" + markdown

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text).strip('-')
    return text

def main():
    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('url', help='The full topic or short post URL of the NodeBB thread.')
    parser.add_argument('--output', '-o', help='(Save Mode) Output filename for the Markdown file.')
    parser.add_argument('--title', '-T', help='(Save Mode) Override the original post title.')
    parser.add_argument('--image-dir', '-I', help='(Save Mode) Custom directory for downloaded images.')
    parser.add_argument('--categories', '-c', nargs='+', help='(Save Mode) A list of categories.')
    parser.add_argument('--tags', '-t', nargs='+', help='(Save Mode) A list of tags.')
    parser.add_argument('--description', '-d', help='(Save Mode) A short description.')
    parser.add_argument('--featured-image', '-i', help='(Save Mode) Path to a featured image.')
    
    args = parser.parse_args()

    topic_url = resolve_url_if_needed(args.url)
    tid, base_url = get_tid_and_base_url(topic_url)
    api_url = f"{base_url}/api/topic/{tid}"
    original_title, first_post = fetch_first_post(api_url)
    html_content = first_post.get('content', '')

    is_save_mode = any([args.output, args.categories, args.tags, args.description, args.featured_image, args.title, args.image_dir])

    if is_save_mode:
        print("\nSave mode activated. Processing for file output...")
        final_title = args.title or original_title
        output_filename = args.output or f"{date.today().strftime('%Y-%m-%d')}-{slugify(final_title)}.md"
        
        post_base_name = os.path.splitext(os.path.basename(output_filename))[0]
        # הגדרת תיקיית התמונות: מותאמת אישית או ברירת מחדל
        image_output_dir = args.image_dir or post_base_name
        
        processed_html = download_images_and_update_html(html_content, base_url, image_output_dir, post_base_name)
        
        markdown_content = preprocess_html_and_convert_to_md(processed_html)
        full_post_content = create_blog_post_content(final_title, markdown_content, args)

        try:
            with open(output_filename, 'w', encoding='utf-8') as f:
                f.write(full_post_content)
            print(f"\n[SUCCESS] Blog post saved to: {output_filename}")
            if os.path.exists(image_output_dir) and os.listdir(image_output_dir):
                 print(f"[INFO] Images renamed and saved in folder: {image_output_dir}/")
        except IOError as e:
            print(f"Error: Could not write to file '{output_filename}'. {e}")
            exit(1)
    else: # Preview mode
        print("\nPreview mode activated. Processing for console output...")
        
        soup = BeautifulSoup(html_content, 'html.parser')
        for img in soup.find_all('img'):
            src = img.get('src')
            if src:
                img['src'] = urljoin(base_url, src)
        
        markdown_content = preprocess_html_and_convert_to_md(str(soup))
        
        print("\n--- PREVIEW MODE ---")
        print("Displaying converted Markdown content. Image URLs are made absolute.\n")
        print("="*40)
        print(markdown_content)
        print("="*40)
        print("\nTo save this content and download images, re-run with save options (e.g., -o, -T, -I).")

if __name__ == '__main__':
    main()