import feedparser
import re

# Medium feed URL
MEDIUM_FEED_URL = "https://medium.com/feed/@ikhsan.budi.wicaksono"

# Files
README_FILE = "README.md"

# Fetch Medium RSS feed
feed = feedparser.parse(MEDIUM_FEED_URL)

# Function to extract image URL from content
def extract_image(content):
    img = re.search(r'<img[^>]+src="([^">]+)"', content)
    return img.group(1) if img else None

# Generate the README content
def generate_medium_posts():
    posts = []
    for entry in feed.entries[:5]:  # Change this number to limit posts
        title = entry.title
        url = entry.link
        img_url = extract_image(entry.content[0].value) if 'content' in entry else None
        if img_url:
            post = f'<a href="{url}" target="_blank"><img src="{img_url}" alt="{title}" width="300"/></a>\n\n[{title}]({url})'
        else:
            post = f'[{title}]({url})'
        posts.append(post)
    return "\n\n".join(posts)

def update_readme():
    new_posts = generate_medium_posts()

    with open(README_FILE, "r") as f:
        readme_content = f.read()

    start_tag = "<!-- BLOG-POST-LIST:START -->"
    end_tag = "<!-- BLOG-POST-LIST:END -->"

    new_content = readme_content.split(start_tag)[0] + start_tag + "\n" + new_posts + "\n" + end_tag + readme_content.split(end_tag)[1]
    
    with open(README_FILE, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
