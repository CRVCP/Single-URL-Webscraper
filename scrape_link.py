import sys                    # For command-line argument handling
import requests               # For sending HTTP requests
from bs4 import BeautifulSoup # For parsing HTML content

def scrape_quotes(url):
    try:
        # Send HTTP GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all quote blocks on the page
        quotes = soup.find_all('div', class_='quote')

        # Loop through each quote block and extract information
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()               # Get the quote text
            author = quote.find('small', class_='author').get_text()         # Get the author's name
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]  # Get all associated tags

            # Print the extracted information
            print(f'Quote: {text}')
            print(f'Author: {author}')
            print(f'Tags: {", ".join(tags)}\n')

    except requests.exceptions.RequestException as e:
        # Handle any request-related errors (e.g., connection issues)
        print(f"Error fetching {url}:\n{e}")

# Entry point when script is run directly
if __name__ == "__main__":
    # Ensure a URL is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python scrape_quotes.py <URL>")
    else:
        scrape_quotes(sys.argv[1])  # Call the scraper function with the given URL

