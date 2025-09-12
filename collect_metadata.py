import os
import yaml
import json
from pathlib import Path

def collect_metadata(directory, output_file, fields, sort_key='file'):
    """
    Collects specified metadata from YAML front matter in markdown files
    in a given directory and saves it to a JSON file.
    """
    all_metadata = []
    dir_path = Path(directory)

    for md_file in dir_path.glob('*.md'):
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            parts = content.split('---')
            if len(parts) >= 3:
                front_matter_raw = parts[1]
                front_matter = yaml.safe_load(front_matter_raw)
                
                data = {'file': str(md_file.name)}
                for field, default in fields.items():
                    data[field] = front_matter.get(field, default)
                
                all_metadata.append(data)
        except Exception as e:
            print(f"Error processing file {md_file}: {e}")

    # Sort the metadata
    if all_metadata:
        all_metadata.sort(key=lambda x: x.get(sort_key, ''), reverse=True)

    try:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(all_metadata, f, ensure_ascii=False, indent=4)
        
        print(f"Successfully collected metadata from {directory} and saved to {output_file}")
    except Exception as e:
        print(f"Error writing to output file {output_file}: {e}")

if __name__ == '__main__':
    # Define fields for posts
    post_fields = {
        'title': None,
        'description': None,
        'tags': [],
        'categories': []
    }
    
    # Collect metadata for posts
    posts_dir = 'C:/Users/me/Documents/GitHub/blog/docs/_posts'
    posts_output_file = 'C:/Users/me/Documents/GitHub/blog/drafts/posts_metadata.json'
    collect_metadata(posts_dir, posts_output_file, post_fields)

    # Define fields for quotes
    quote_fields = {
        'author': None,
        'source': None,
        'tags': []
    }

    # Collect metadata for quotes
    quotes_dir = 'C:/Users/me/Documents/GitHub/blog/docs/_quotes'
    quotes_output_file = 'C:/Users/me/Documents/GitHub/blog/drafts/quotes_metadata.json'
    collect_metadata(quotes_dir, quotes_output_file, quote_fields)