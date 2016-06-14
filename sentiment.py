import requests
from bs4 import BeautifulSoup
import spiderAssist

spidy = spiderAssist()

class senti:

    def word_count(self,line):
        clean_list = []
        for word in line:
            symbols = "!@#$%^&*()_+={}[]:;\"',.<>?/"
            for i in range(0,len(symbols)):
                word = word.replace(symbols[i])
                if len(word)>3:
                    clean_list.append(word)

    def amazon_spider(self, max_pages):
        page = 1

        while page <= max_pages:
            url = 'https://www.amazon.com/Philips-SHP9500-Precision-Over-ear-Headphones/product-reviews/B00ENMK1DW/' \
                  'ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&showViewpoints=1&sortBy=helpful&pageNumber=' + str(page)
            source_code = requests.get(url)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text, "html.parser")
            for link in soup.find_all('a',
                                      {'class': 'a-size-base a-link-normal review-title a-color-base a-text-bold'}):
                href = r"http://www.amazon.com" + link.get('href')
                title = link.string
                print(title)
                print(href)
                self.amazon_spider2(href)
            page += 1