import requests

# Masukkan User ID Medium Anda
USER_ID = "your_user_id"

def get_latest_posts():
    response = requests.get(f"https://api.medium.com/v1/users/{USER_ID}/publications")
    response.raise_for_status()
    publications = response.json()
    
    publication_id = publications['data'][0]['id']
    posts_response = requests.get(f"https://api.medium.com/v1/publications/{publication_id}/posts")
    posts_response.raise_for_status()
    posts = posts_response.json()
    
    latest_posts = posts['data'][:3]  # Ambil 3 posting terbaru
    return [(post['title'], post['url']) for post in latest_posts]

if __name__ == "__main__":
    posts = get_latest_posts()
    for title, url in posts:
        print(f"- [{title}]({url})")
