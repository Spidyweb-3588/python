import requests  # Python 프로그래밍 언어용 HTTP 라이브러리
from bs4 import BeautifulSoup # HTML과 XML 문서를 파싱하기위한 파이썬 패키지
import re

def word_4xr():
    url = "https://www.4xr.co.kr/ranking/goods_list.php?cate=01"
    response = requests.get(url)
    response.raise_for_status()
    soup =BeautifulSoup(response.text, "lxml")

    rank100_4XR = soup.select(".base_slider_list .product .infor_box .p_conts")
    rank100_4XR_list = [i.text for i in rank100_4XR]
    rank100_4XR_list = [x.replace("\r","").replace("\n","").replace("\t","").replace("(","").replace(")","") for x in rank100_4XR_list]
    rank100_4XR_word_list = [y for x in rank100_4XR_list for y in x.split(" ")]
    return rank100_4XR_word_list

def word_musinsa():
    url = "https://www.musinsa.com/ranking/best?" \
           "period=now&age=ALL&mainCategory=&subCategory=&leafCategory=&price=&golf=false&" \
           "kids=false&newProduct=false&exclusive=false&discount=false&soldOut=false&page=1&" \
           "viewType=small&priceMin=&priceMax="
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    rank100_musinsa = soup.select(".article_info p.list_info a")
    rank100_musinsa_list = [i.text for i in rank100_musinsa]
    rank100_musinsa_list =\
    [x.replace("\r","").replace("\n","").replace("\t","").replace("(","").replace(")","") for x in rank100_musinsa_list]
    rank100_musinsa_word_list =\
    [y.replace(" ","") for x in rank100_musinsa_list for y in x.split(" ") if y != ""]
    print(rank100_musinsa_word_list)
    return rank100_musinsa_word_list

def word_boom_style():
    url = "http://www.jogunshop.com/shop/shopbrand.html?xcode=071&type=P"
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, "lxml")

    rank100_boom_style_all = soup.select(".item-wrap  .item-cont  .item-list .prd-name a")
    rank100_boom_style_font = soup.select(".item-wrap  .item-cont  .item-list .prd-name a font")
    if rank100_boom_style_font[0].text in rank100_boom_style_all[0].text:
        print(rank100_boom_style_all[0].text.replace(rank100_boom_style_font[0].text,""))

    """rank100_boom_style_list = [i.text[0] for i in rank100_boom_style]
    print(rank100_boom_style_list)

    rank100_boom_style_list = [i.text for i in rank100_boom_style]
    rank100_boom_style_list =\
    [x.replace("\r","").replace("\n","").replace("\t","").replace("(","").replace(")","") for x in rank100_boom_style_list]

    rank100_boom_style_list_word_list =\
    [y.replace(" ","") for x in rank100_boom_style_list for y in x.split(" ") if y != ""]"""

    #print(rank100_boom_style_list)
    #return rank100_boom_style_list_word_list

if __name__=="__main__":
    word_musinsa()
    word_boom_style()

#rank100_boom_style =
