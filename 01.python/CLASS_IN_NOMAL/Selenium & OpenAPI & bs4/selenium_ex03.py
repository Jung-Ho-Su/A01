from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time

def CoffeeBean_store(result):
    CoffeeBean_URL = "http://www.coffeebeankorea.com/store/store.asp"
    wd = webdriver.Chrome()
    for i in range(409, 0, -1):
        wd.get(CoffeeBean_URL)
        time.sleep(1)
        try:
            wd.execute_script("storePop2(%d)"% i)
            time.sleep(1)
            html = wd.page_source
            soupCB =  BeautifulSoup(html, "html.parser")
            store_name_h2 = soupCB.select("div.store_txt > h2")
            store_name = store_name_h2[0].string
            store_info = soupCB.select("div.store_txt > table.store_table > tbody > tr  > td")
            store_address_list = list(store_info[2])
            store_address = store_address_list[0]
            store_phone = store_info[3].string
            result.append([store_name] + [store_phone] + [store_address])
            print(i, [store_name] + [store_phone] + [store_address])
        except:
            continue

    return

def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)

    CB_tbl = pd.DataFrame(result, columns=('store', 'address', 'phone'))
    CB_tbl.to_csv('CoffeeBean.csv', encoding='utf8', mode='W', index=False)

if __name__ == '__main__':
    main()

