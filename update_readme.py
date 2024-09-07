import re

README_FILE = "README.md"
POSTS_FILE = "scripts/posts.txt"

def update_readme():
    with open(POSTS_FILE, "r") as f:
        posts = f.read()

    with open(README_FILE, "r") as f:
        readme_content = f.read()

    # Gunakan regex untuk mengganti konten di antara START dan END
    new_content = re.sub(
        r"<!-- START_MEDIUM_POSTS -->(.*?)<!-- END_MEDIUM_POSTS -->", 
        f"<!-- START_MEDIUM_POSTS -->\n{posts}\n<!-- END_MEDIUM_POSTS -->", 
        readme_content, 
        flags=re.DOTALL
    )
    
    with open(README_FILE, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
