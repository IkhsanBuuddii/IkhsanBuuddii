import requests
from bs4 import BeautifulSoup

MEDIUM_PROFILE_URL = "https://medium.com/@ikhsan.budi.wicaksono"

def get_latest_posts():
    response = requests.get(MEDIUM_PROFILE_URL)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('div', class_='postArticle')
    
    latest_posts = []
    for article in articles[:3]:  # Ambil 3 posting terbaru
        title = article.find('h3')
        title = title.get_text() if title else "No title"
        link = article.find('a', {'data-action': 'open-post'})
        link = link['href'] if link else "#"
        latest_posts.append((title, link))
    
    return latest_posts

if __name__ == "__main__":
    posts = get_latest_posts()
    with open("scripts/posts.txt", "w") as file:
        for title, url in posts:
            file.write(f"- [{title}]({url})\n")
