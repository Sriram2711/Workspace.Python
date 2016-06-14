import requests
from bs4 import BeautifulSoup

def amazon_spider(max_pages):
    page = 1
    while page >= max_pages:
        url = 'https://www.amazon.com/Philips-SHP9500-Precision-Over-ear-Headphones/product-reviews/B00ENMK1DW/' \
              'ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&showViewpoints=1&sortBy=helpful&pageNumber=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in soup.find_all('a',{'class':'a-size-base a-link-normal review-title a-color-base a-text-bold'}):
            href = r"http://www.amazon.com" + link.get('href')
            title = link.string
            print(title)
            print(href)
            amazon_spider2(href)
        page += 1

def amazon_spider2(url2):
    source_code = requests.get(url2)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for review_link in soup.find_all('div', {'class': 'reviewText'}):
        (review) = review_link.get_text(' ', strip=True)
        print(review)

amazon_spider(1)




