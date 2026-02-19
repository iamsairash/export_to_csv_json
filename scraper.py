import requests
from bs4 import BeautifulSoup

URL = "https://web-scraping.dev/products"

def scrape_products():
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status # raise error if status is 404, 500 etc
    except requests.exceptions.ConnectionError:
        print("ERROR: No Internet Connection.")
        return 
    except requests.exceptions.ConnectTimeout:
        print("ERROR: Website is taking too long to load.")
        return
    except requests.exceptions.HTTPError as e:
        print("ERROR: HTTP error")
        
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup)
    
    # find all the cards
    product_cards = soup.find_all("div", class_="product")
    # print(product_cards)
    
    if not product_cards:
        print("WARNING: no product found. website structure may have changed")
        return []
    
    products = []
    for card in product_cards:
        try:
            # extract name
            name_tag = card.find("h3", class_="mb-0")
            name = name_tag.find("a").text.strip() if name_tag else "N/A"

            # extract description
            desc_tag = card.find("div", class_="short-description")
            desc = desc_tag.text.strip() if desc_tag else "N/A"
            
            # extract price
            price_tag = card.find("div", class_="price")
            price_text = price_tag.text.strip() if price_tag else "0"
            
            price = float(price_text)
            
            # build dictionary for this product. 
            product = {
                "name": name,
                "description": desc,
                "price": price
            }
            products.append(product)
            
        except Exception as e:
            print(f"WARNING: product skipped due to error. {e}")
            continue
    # print(products) 
    print(f"SUCCESS: Scraped {len(products)} products.")
    return products
            

# scrape_products()