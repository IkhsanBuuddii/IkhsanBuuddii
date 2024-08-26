README_FILE = "README.md"
POSTS_FILE = "scripts/posts.txt"

def update_readme():
    with open(POSTS_FILE, "r") as f:
        posts = f.read()

    with open(README_FILE, "r") as f:
        readme_content = f.read()

    new_content = readme_content.replace("<!-- START_MEDIUM_POSTS -->", "<!-- START_MEDIUM_POSTS -->\n" + posts)
    
    with open(README_FILE, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
