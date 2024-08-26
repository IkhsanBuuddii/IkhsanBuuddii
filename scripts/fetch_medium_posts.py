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

# Generate the posts content
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

# Save posts to `posts.txt`
with open("scripts/posts.txt", "w") as file:
    file.write("\n\n".join(posts))
