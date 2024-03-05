"""Web Scraping Implementation With BeautifulSoup"""
import requests
from bs4 import BeautifulSoup


def event_handler(event):
    """Log events to a file."""
    with open("event_handler.txt", "w", encoding="utf-8") as file1:
        print("Event:", event, file=file1)


def scrape_website(url):
    """Scrape a website and log results or errors."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            elements = soup.find_all(class_='entry-title')
            with open("event_handler.txt", "w", encoding="utf-8") as file2:
                for item in elements:
                    print(item.a.text, file=file2)
        elif response.status_code == 400:
            event_handler("Error: Bad request")
        else:
            event_handler(f"Error: Failed request {response.status_code}")
    except requests.Timeout:
        event_handler("Error: Timeout occurred while accessing the website")
    except requests.RequestException as e:
        event_handler(f"Error: RequestException - {e}")


scrape_website("https://punchng.com/topics/politics/")
