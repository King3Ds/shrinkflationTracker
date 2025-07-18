import requests
from bs4 import BeautifulSoup

def scrape_walmart_product(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('h1')
        price = (soup.find('span', {'itemprop': 'price'}) or
                soup.find('[data-automation-id="product-price"]') or 
                soup.find('.price-current') or
                soup.find('[data-testid="price"]') or
                soup.find('.price'))
        return {
            'name': name.text.strip() if name else 'Unknown',
            'price': price.text.strip() if price else 'Unknown',
            'url': url,
            'source': 'walmart'
        }
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    test_url = "https://www.walmart.com/ip/OREO-Chocolate-Sandwich-Cookies-13-29-oz/1052966595?classType=VARIANT&from=/search"
    result = scrape_walmart_product(test_url)
    print(result)