import requests
from bs4 import BeautifulSoup

def scrape_walmart_product(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('h1')
        price = soup.find('[data-automation-id="product-price"]')
        return {
            'name': name.text.strip() if name else 'Unknown',
            'price': price.text.strip() if price else 'Unknown',
            'url': url,
            'source': 'walmart'
        }
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    test_url = 