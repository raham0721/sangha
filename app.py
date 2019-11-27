import requests

from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"
}

for idx in range(1, 10):
    #link_1 url = "https://www.coupang.com/np/categories/187371?listSize=60&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page="+str(idx)+"&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=saleCountDesc&filter=&component=187271&rating=0"
    url = "https://www.coupang.com/np/campaigns/2893?listSize=60&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page="+str(idx)+"&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=saleCountDesc&filter=&rating=1"
    
    print(url)
    result = requests.get(url, headers=headers)
    soup_obj = BeautifulSoup(result.content, "html.parser")

    div = soup_obj.findAll("div", {"class": "name"})
    lis = soup_obj.find("ul", {"id": "productList"}).findAll("li")

    for li in lis:
        product = li.find("div", {"class": "name"})
        price = li.find("em", {"class": "sale"}).find(
            "strong", {"class": "price-value"}
        )
        
       
        star_cnt = li.find("em",{"class":"rating"})
        
        #print("상품명: " + product.text.strip() + " / " + "상품가격: " + price.text.strip())
        print("상품명: " + product.text.strip() + " / " + "상품가격: " + price.text.strip()+ " / " + "별점" + star_cnt.text.strip())
       
       #별점은 첫 링크의 크롤링에서는 첫 페이지 상품들에 별점이 매겨져 있어서 정상적으로 작동하지만,
       #별점이 매겨지지 않은 상품이 존재할 때 에러가 생겨서 별점이 1점이상 매겨진 항목으로 크롤링 했습니다.
       
       
       #===============================#
       
