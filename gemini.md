# Workflow: Convert URL to Blog Post

This guide outlines the process for converting a post from a URL into a blog post using the `nodebb_to_blog.py` script.

## Process Overview

When asked to convert a link to a post, follow these steps:

### 1. Gather Information

- **Get Post Date:** The script automatically detects the publication date from the post's metadata. The `--date` flag can be used to override this.

- **Preview Content:** Get the title and content to determine the final metadata. The preview will also show the automatically detected date.
  ```bash
  python nodebb_to_blog.py <URL>
  ```

- **Define Metadata:** Based on the preview, decide on the final:
    - Title
    - URL Slug (for the filename)
    - Description
    - Categories
    - Tags

### 2. Create the Blog Post

- **Execute Script:** Use the collected information to run the script. The date will be set automatically unless you override it with `--date`.
  ```bash
  python nodebb_to_blog.py <URL> \
    -o "docs/_posts/YYYY-MM-DD-slug.md" \
    -T "<Title>" \
    -d "<Description>" \
    -c <Category1> <Category2> \
    -t <Tag1> <Tag2>
  ```


### 3. Add Featured Image

- **Auto-detect Image:** If the preview shows an image at the beginning of the post, use its URL to set it as a featured image. This should be done automatically.
- **Download Image:**
  ```bash
  python -c "import requests, os; url='<IMAGE_URL>'; dir_path=r'docs/assets/images/YYYY-MM-DD-slug'; file_path=os.path.join(dir_path, 'featured.webp'); os.makedirs(dir_path, exist_ok=True); r=requests.get(url); r.raise_for_status(); open(file_path, 'wb').write(r.content);"
  ```
- **Update Front Matter:** Add the `featured_image` field to the post's front matter.
  ```yaml
  featured_image: "/assets/images/YYYY-MM-DD-slug/featured.webp"
  ```

### 4. Final Review

Quickly read the generated Markdown file to check formatting and make minor improvements if needed.