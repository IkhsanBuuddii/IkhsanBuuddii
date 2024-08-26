import feedparser
import re

# Medium feed URL
MEDIUM_FEED_URL = "https://medium.com/feed/@ikhsan.budi.wicaksono"

# Fetch Medium RSS feed
feed = feedparser.parse(MEDIUM_FEED_URL)

# Function to extract image URL from content
def extract_image(content):
    img = re.search(r'<img[^>]+src="([^">]+)"', content)
    return img.group(1) if img else None

# Generate the README content
with open("README.md", "r") as file:
    readme = file.read()

start_tag = "<!-- BLOG-POST-LIST:START -->"
end_tag = "<!-- BLOG-POST-LIST:END -->"
before_start = readme.split(start_tag)[0]
after_end = readme.split(end_tag)[1]

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

new_content = start_tag + "\n" + "\n\n".join(posts) + "\n" + end_tag

with open("README.md", "w") as file:
    file.write(before_start + new_content + after_end)
