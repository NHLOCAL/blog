# Workflow: Converting a NodeBB Post

This guide outlines the streamlined process for converting a NodeBB post into a blog post using the `nodebb_to_blog.py` script.

## The Process

When asked to convert a NodeBB link, follow these steps:

### 1. Fetch Original Post Date

First, determine the original date of the post.
- Extract the Topic ID (TID) from the URL (e.g., for `/topic/65404/...`, the TID is `65404`).
- Run the following command to get the date in `YYYY-MM-DD` format:

  ```bash
  python -c "import requests, datetime; api_url = 'https://mitmachim.top/api/topic/<TID>'; r = requests.get(api_url); d = r.json(); ts = int(d['posts'][0]['timestamp']); dt = datetime.datetime.fromtimestamp(ts / 1000); print(dt.strftime('%Y-%m-%d'))"
  ```

### 2. Gather Information for Saving

- **Preview Content:** Run the script in preview mode to get the original title and content, which will help in deciding the metadata.
  ```bash
  python nodebb_to_blog.py <URL>
  ```
- **Determine Metadata:** Based on the preview and examples in `drafts/posts_metadata.json`, decide on a final:
    - Title
    - URL Slug (the part after the date in the filename)
    - Description
    - Categories
    - Tags

### 3. Create the Blog Post

- **Construct the Command:** Combine the information from the previous steps into a single command.
    - Use the original date for the filename and the `--date` argument.
    - Use the chosen metadata for the other arguments.
- **Execute:**

  ```bash
  python nodebb_to_blog.py <URL> \
    -o "docs/_posts/YYYY-MM-DD-slug.md" \
    --date "YYYY-MM-DD" \
    -T "<Title>" \
    -d "<Description>" \
    -c <Category1> <Category2> \
    -t <Tag1> <Tag2>
  ```

### 4. Add a Featured Image (Optional)

This step should only be performed if the user explicitly requests to add a featured image.

- **Download Image:**
  ```bash
  python -c "import requests, os; url='<IMAGE_URL>'; dir_path=r'docs/assets/images/YYYY-MM-DD-slug'; file_path=os.path.join(dir_path, 'featured.webp'); os.makedirs(dir_path, exist_ok=True); r=requests.get(url); r.raise_for_status(); open(file_path, 'wb').write(r.content);"
  ```
- **Update Front Matter:** Add the `featured_image` field to the post's front matter.
  ```yaml
  featured_image: "/assets/images/YYYY-MM-DD-slug/featured.webp"
  ```

### 5. Final Review

As a final step, quickly read the generated Markdown file to ensure the formatting is correct and make any minor stylistic improvements if needed.