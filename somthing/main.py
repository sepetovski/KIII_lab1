# Import required libraries
import requests
from bs4 import BeautifulSoup


# Function to scrape a website
def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract all paragraph elements
            paragraphs = soup.find_all('p')

            # Print each paragraph's text
            for i, p in enumerate(paragraphs, 1):
                print(f"Paragraph {i}: {p.get_text().strip()}")

        else:
            print(f"Failed to retrieve website. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Replace with the URL you want to scrape
    target_url = "https://example.com"
    print(f"Scraping: {target_url}\n")
    scrape_website(target_url)