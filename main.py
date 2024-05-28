import datetime
import random
import requests
import time
import pprint
import json
from bs4 import BeautifulSoup
from urllib.parse import quote
import requests
import re
import urllib.parse
from urllib.parse import urlencode, urljoin


def build_url(base_url, params):
    # 파라미터를 쿼리 문자열로 변환
    query_string = urlencode(params)

    # base_url과 쿼리 문자열을 합쳐서 완전한 URL을 생성
    full_url = urljoin(base_url, '?' + query_string)

    return full_url
def GetRequest(url):
    # url = 'https://search.shopping.naver.com/catalog/33155226620?cat_id=50000440&frm=NVSCPRO&query=%EC%88%98%EB%B6%84%ED%81%AC%EB%A6%BC&NaPm=ct%3Dluur56q0%7Cci%3De22b37d1cb8c166b047e7a332421ef6e45d937a1%7Ctr%3Dsls%7Csn%3D95694%7Chk%3De721c75e7a562db1ce6ec2370f6bdcd33941a68f'
    # url='https://ip.oxylabs.io/headers'
    # Proxy configuration with login and password
    proxy_host = 'gw.dataimpulse.com'
    proxy_port = 823
    # proxy_login = '8370b4580cf4cb6a2555'
    # proxy_password = 'dafeda6cabefb166'
    proxy_login="82c087469cb5881bf886"
    proxy_password="f3329ab92a350588"
    proxy = f'http://{proxy_login}:{proxy_password}@{proxy_host}:{proxy_port}'
    proxies = {
        'http': proxy,
        'https': proxy
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        # 'cookie': 'NNB=HK6BYGF5VMLGM; SHP_BUCKET_ID=3; nid_inf=558720006; NID_AUT=fAFrTdmV+d1CAui+kz2pojA33LDB/dxfffVl3PYmV8OpkY9zOGr68DZlEns9IUfe; NID_JKL=aqpXBjPTJUH3HDVb5cXHih5mk36gUHPGcQvEz4AYayw=; NID_SES=AAABfIG5+Plp5I3iztQ9KDO0UdrxRKBlzckV7AE/vmDhf2DhHpoM0/OkWeat8zLn79ObLmU97iOW8c/NLuWJ25dMakpphdxaJqlx0wWqOJ/K/Q/CN0KgyVohGNrSYP7IrDqGg1u+jaTK+2O+u6AZldyknkU88E6CesrK7v7nRyH4CcHiAcNBykcMhqDzmhL2UWpAhlOr/TB68Qc7Q3Uemq0RTsfnZBls0zW2M5XEPvKngcszjVpYyKms2y65LADV05N0xYl6r8iwGF6KQu/ieci2mBXERbaJ1lF3BdhobNcSYNM3CO0eMNu88yIOROCzPayEUR/Z1Zq3ib6gVOBBI8/OIq/Cm2750uP8DkrnHDXFSX95wMYGVj98iBTNRTNbA1CxIw3fb9MC142Ya6PnmxpTCfXgajdDMWWrLVPkumyxJn063H9Gdn9B0HZl378cBDVWoLslKnoS8vawrh3e8JrK8hODrtTnwFUHh0hFmxN2k5WOBKGMwkVJ6mn74LfIuoncDw==; _naver_usersession_=AEGI/PyIZehWBCdvQErP54Wy; page_uid=imN0dsqo15wssmjaldZssssstXC-334879; sus_val=lgzT2KRVqobvVruKYLc7ADBv; ncpa=5594875|db8084eb2149553f99c78b4f24cd93b0c7271477|luuiyeu8|s_11525ff4ab978|102514c347554322fc8133a8634cc3887f037680:95694|luuiyjgw|8782c22e22bacc8f66cb6d6e2589fa5e38f5a87c|95694|e1642e50ae60b023a79f9faf8be875ff9ec351ff; spage_uid=imN0dsqo15wssmjaldZssssstXC-334879',
        # 'referer': 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%88%98%EB%B6%84%ED%81%AC%EB%A6%BC',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.106", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.106"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-ch-ua-wow64': '?0',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',

    }
    cookies={"NNB": "RFE6UGY6GILWM"}

    response = requests.get(url, proxies=proxies, headers=headers, cookies=cookies)


    return response
def find_option_combinations2(data, key):
    # key를 찾았을 경우 반환
    if isinstance(data, dict):
        if key in data:
            return data[key]
        else:
            # dictionary 내부를 재귀적으로 탐색
            for value in data.values():
                result = find_option_combinations(value, key)
                if result is not None:
                    return result
    elif isinstance(data, list):
        # list 내부의 각 아이템을 재귀적으로 탐색
        for item in data:
            result = find_option_combinations(item, key)
            if result is not None:
                return result

def find_option_combinations(data, key):
    # key를 찾았을 경우 반환
    if isinstance(data, dict):
        if key in data:
            return data[key]
        else:
            # dictionary 내부를 재귀적으로 탐색
            for value in data.values():
                result = find_option_combinations(value, key)
                if result is not None:
                    return result
    elif isinstance(data, list):
        # list 내부의 각 아이템을 재귀적으로 탐색
        for item in data:
            result = find_option_combinations(item, key)
            if result is not None:
                return result
def extract_numbers_from_url2(url):
    # commonPrdTotCnt 뒤에 있는 숫자를 찾는 정규 표현식
    common_prd_tot_cnt_pattern = r"commonPrdTotCnt=(\d+)"
    # prdMoreStartShowCnt 뒤에 있는 숫자를 찾는 정규 표현식
    prd_more_start_show_cnt_pattern = r"prdMoreStartShowCnt=(\d+)"

    # commonPrdTotCnt 값 추출
    common_prd_tot_cnt = re.search(common_prd_tot_cnt_pattern, url)
    common_prd_tot_cnt_value = int(common_prd_tot_cnt.group(1)) if common_prd_tot_cnt else None

    # prdMoreStartShowCnt 값 추출
    prd_more_start_show_cnt = re.search(prd_more_start_show_cnt_pattern, url)
    prd_more_start_show_cnt_value = int(prd_more_start_show_cnt.group(1)) if prd_more_start_show_cnt else None

    return common_prd_tot_cnt_value, prd_more_start_show_cnt_value
def filter_products_by_platform(data_list, platform):
    # 결과를 저장할 빈 리스트 생성
    filtered_products = []

    # 데이터 리스트를 순회하면서 platform 값이 입력 값 또는 '전체'인 경우 필터링
    for product in data_list:
        if product['platform'] == platform or product['platform'] == '전체':
            filtered_products.append(product)

    return filtered_products

def GetSearchS2B(supabaseData,priceRatio):
    dataList=[]
    pageCount=0
    keyword=supabaseData['name']
    while True:
        print("S2B★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            'WMONID': 'VY6ZPxFLel8',
            '_fwb': '1530Wq4aF57AOLc7E2TEvKp.1712495137147',
            '_gid': 'GA1.2.104889499.1712495137',
            # 'itemBannerID': '202401107889413:2023111422279:í”„ë¡œë³´ í…Œí\x81¬ë‹‰ ì½”ë”©ë¡œë´‡ ë\xa0ˆë²¨1 í‚¤íŠ¸:2024/01/10/202401107889413_1704850062495.jpg:120000&',
            's2bncustomer': 'kMfLmT2TgPqGQ2DdlLyJMlKJqJcTJGfPCvn3Mq4pNjVcgmBnhqSq!1437451093!-1263246214',
            'itemID': '202401107889413A',
            # '_gat_gtag_UA_173155725_2': '1',
            # '_ga_7N9G9N6N6X': 'GS1.1.1712586324.5.1.1712588227.56.0.0',
            # '_ga': 'GA1.1.1879214181.1712495137',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'WMONID=VY6ZPxFLel8; _fwb=1530Wq4aF57AOLc7E2TEvKp.1712495137147; _gid=GA1.2.104889499.1712495137; itemBannerID=202401107889413:2023111422279:í”„ë¡œë³´ í…Œí\x81¬ë‹‰ ì½”ë”©ë¡œë´‡ ë\xa0ˆë²¨1 í‚¤íŠ¸:2024/01/10/202401107889413_1704850062495.jpg:120000&; s2bncustomer=kMfLmT2TgPqGQ2DdlLyJMlKJqJcTJGfPCvn3Mq4pNjVcgmBnhqSq!1437451093!-1263246214; itemID=202401107889413A; _gat_gtag_UA_173155725_2=1; _ga_7N9G9N6N6X=GS1.1.1712586324.5.1.1712588227.56.0.0; _ga=GA1.1.1879214181.1712495137',
            'Origin': 'https://www.s2b.kr',
            'Referer': 'https://www.s2b.kr/S2BNCustomer/S2B/scrweb/remu/rema/searchengine/s2bCustomerSearch.jsp',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        text=supabaseData['name']
        encoded_text = urllib.parse.quote(text, encoding='cp949')
        # print("encoded_text:",encoded_text,"/ encoded_text_TYPE:",type(encoded_text))
        # data = 'actionType=MAIN_SEARCH&searchField=ALL&startIndex=&viewCount=50&viewType=LIST&sortField=RANK&priceMin=0&priceMax=0&priceMinSet=0&priceMaxSet=0&categoryLevel1Code=&categoryLevel2Code=&categoryLevel3Code=&categoryLevel3Name=&areaCode=&localAreaCode=&categoryWinStatus=none&companyCodeParam=&priceNewSet=true&publicPurchaseCode=&f_edufine_code=&submit_yn=Y&defaultView=&defaultCount=&CERT_CODE_YN=&etCategoryLevel1Code=&etCategoryLevel2Code=&etCategoryLevel3Code=&searchQuery=%C7%C1%B7%CE%BA%B8+%C5%D7%C5%A9%B4%D0&locationGbn=all&f_category_code1=1%C2%F7%C4%AB%C5%D7%B0%ED%B8%AE&f_category_code2=&f_category_code3=&searchRequery=&recategory=ALL&CERT_CODE=&CERT_CODE_OR=&CERT_CODE_AND=&CERT_CHECK=&CERT_CODE_119=&CERT_CODE_161=&CERT_CODE_162=&CERT_CODE_163=&kcMall='
        data = 'actionType=MAIN_SEARCH&searchField=ALL&startIndex={}&viewCount=50&viewType=LIST&sortField=RANK&priceMin=0&priceMax=0&priceMinSet=0&priceMaxSet=0&categoryLevel1Code=&categoryLevel2Code=&categoryLevel3Code=&categoryLevel3Name=&areaCode=&localAreaCode=&categoryWinStatus=none&companyCodeParam=&priceNewSet=true&publicPurchaseCode=&f_edufine_code=&submit_yn=Y&defaultView=&defaultCount=&CERT_CODE_YN=&etCategoryLevel1Code=&etCategoryLevel2Code=&etCategoryLevel3Code=&searchQuery={}&locationGbn=all&f_category_code1=1%C2%F7%C4%AB%C5%D7%B0%ED%B8%AE&f_category_code2=&f_category_code3=&searchRequery=&recategory=ALL&CERT_CODE=&CERT_CODE_OR=&CERT_CODE_AND=&CERT_CHECK=&CERT_CODE_119=&CERT_CODE_161=&CERT_CODE_162=&CERT_CODE_163=&kcMall='.format(pageCount*50,encoded_text,)

        # print("dataList:",dataList,"/ dataList_TYPE:",type(dataList))
        response = requests.post(
            'https://www.s2b.kr/S2BNCustomer/S2B/scrweb/remu/rema/searchengine/s2bCustomerSearch.jsp',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        soup=BeautifulSoup(response.text,'html.parser')
        # print(soup.prettify())
        items=soup.find_all("td",attrs={'style':'padding-right:7px;'})
        if len(items)==0:
            break
        prices=soup.find_all("td",attrs={'class':'lt_mulpumprice'})
        for index,item in enumerate(items):
            try:
                title=item.find("a").get_text()
            except:
                title=""
            print("title:",title)
            try:
                url=item.find("a")['href']
                extracted_number = re.findall(r'\d+', url)[0]
                url=extracted_number
            except:
                url=""
            print("url:",url)
            try:
                price=int(prices[index].find('li').get_text().replace("원","").replace(",",""))
            except:
                price=""
            print("price:",price)
            data={'title':title,'realPrice':price,'url':url,'priceHigh':supabaseData['priceHigh'],'priceLow':supabaseData['priceLow'],'platform':'S2B','url':url,'salesInfo':'','inputKeyword':supabaseData['name']}
            if float(priceRatio)*supabaseData['priceLow']<price<supabaseData['priceLow']:
                dataList.append(data)
        pageCount+=1
        print("===============pageCount:{}============".format(pageCount))
        time.sleep(random.randint(5,10)*0.1)
    with open('dataList_S2B.json', 'w',encoding='utf-8-sig') as f:
        json.dump(dataList, f, indent=2,ensure_ascii=False)
    return dataList
def GetLotteOn(supabaseData,priceRatio):
    pageCount=1
    dataList=[]
    keyword=supabaseData['name']
    while True:
        print("롯데온★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            'infw_mdia_cd': 'PC',
            'ch_mem_no': '285068555mn7SW65f2ce593a',
            'ch_no': '100995',
            'ch_dtl_no': '1025316',
            'ch_csf_cd': 'PA',
            'ch_typ_cd': 'PA07',
            'pcs_grp': '',
            'site_no': '1',
            'mall_no': '1',
            'infw_mall_no': '1',
            'crss_rte_nm': 'LO',
            'crss_ntm': '1',
            'fnl_crss_rte_nm': '',
            'at_check': 'true',
            'AMCVS_443A1C095C0A82400A495E92%40AdobeOrg': '1',
            '_gcl_au': '1.1.1251061932.1712762507',
            'AMCV_443A1C095C0A82400A495E92%40AdobeOrg': '1176715910%7CMCIDTS%7C19824%7CMCMID%7C72523635356235877200189499512793502995%7CMCAAMLH-1713367306%7C11%7CMCAAMB-1713367306%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C857883598%7CMCOPTOUT-1712769706s%7CNONE%7CvVersion%7C5.4.0',
            '_fbp': 'fb.1.1712762506848.1943539184',
            '_ga': 'GA1.1.2021012175.1712762507',
            '__rtbh.lid': '%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22Gc4V180EBeyPr98WtjQW%22%7D',
            '__rtbh.uid': '%7B%22eventType%22%3A%22uid%22%7D',
            'econAnalyticsSession': 'e034bc77-2035-4ef3-b602-46e2c98f903e',
            'econAnalyticsLtSession': '59fb42cf-4a4e-44e9-9247-02bccc8656f3',
            '_wp_uid': '2-9242275ca3b6eb4fd71e9a43f1adef5a-s1712217785.665417|windows_10|chrome-1m59n96',
            '_dd_s': 'rum=0&expire=1712763512807',
            'pv_count_session': '6',
            'mbox': 'session#0778712c8f104f9d901962775fe68a51#1712764475|PC#0778712c8f104f9d901962775fe68a51.32_0#1776007415',
            '_ga_4D4NCCP4FX': 'GS1.1.1712762507.1.1.1712762614.17.0.0',
            'cto_bundle': 'IK2O1V9Ud0Z0cDJ4dmdlQiUyQm5QbiUyRnglMkI1RyUyRmJhNThqSmZvYzBmeXp3MjZac2E1UElzNjVNMVZhRXFIa25JSjhpNklHSGVOQ1YzJTJCME9iZzZoYiUyQmkwWmF1ckdmUmlJUk5udU5VT2dvRlJIbEZhQkxlcXAyZHJPNzM2VWwxa1c2M3dFc2xxQXRvWmYlMkJGTk5mU3puMHdJdTdxYWNQdyUzRCUzRA',
            'on_lrtm': '658C174175A42EE7A489B836583EB9126470658C16CFBD38E1762382290B9BAA9E3847F2786CC74A',
            'econAnalyticsSeq': '16',
            'econAnalyticsLastActivity': '1712762706950',
        }

        headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': 'infw_mdia_cd=PC; ch_mem_no=285068555mn7SW65f2ce593a; ch_no=100995; ch_dtl_no=1025316; ch_csf_cd=PA; ch_typ_cd=PA07; pcs_grp=; site_no=1; mall_no=1; infw_mall_no=1; crss_rte_nm=LO; crss_ntm=1; fnl_crss_rte_nm=; at_check=true; AMCVS_443A1C095C0A82400A495E92%40AdobeOrg=1; _gcl_au=1.1.1251061932.1712762507; AMCV_443A1C095C0A82400A495E92%40AdobeOrg=1176715910%7CMCIDTS%7C19824%7CMCMID%7C72523635356235877200189499512793502995%7CMCAAMLH-1713367306%7C11%7CMCAAMB-1713367306%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C857883598%7CMCOPTOUT-1712769706s%7CNONE%7CvVersion%7C5.4.0; _fbp=fb.1.1712762506848.1943539184; _ga=GA1.1.2021012175.1712762507; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22Gc4V180EBeyPr98WtjQW%22%7D; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%7D; econAnalyticsSession=e034bc77-2035-4ef3-b602-46e2c98f903e; econAnalyticsLtSession=59fb42cf-4a4e-44e9-9247-02bccc8656f3; _wp_uid=2-9242275ca3b6eb4fd71e9a43f1adef5a-s1712217785.665417|windows_10|chrome-1m59n96; _dd_s=rum=0&expire=1712763512807; pv_count_session=6; mbox=session#0778712c8f104f9d901962775fe68a51#1712764475|PC#0778712c8f104f9d901962775fe68a51.32_0#1776007415; _ga_4D4NCCP4FX=GS1.1.1712762507.1.1.1712762614.17.0.0; cto_bundle=IK2O1V9Ud0Z0cDJ4dmdlQiUyQm5QbiUyRnglMkI1RyUyRmJhNThqSmZvYzBmeXp3MjZac2E1UElzNjVNMVZhRXFIa25JSjhpNklHSGVOQ1YzJTJCME9iZzZoYiUyQmkwWmF1ckdmUmlJUk5udU5VT2dvRlJIbEZhQkxlcXAyZHJPNzM2VWwxa1c2M3dFc2xxQXRvWmYlMkJGTk5mU3puMHdJdTdxYWNQdyUzRCUzRA; on_lrtm=658C174175A42EE7A489B836583EB9126470658C16CFBD38E1762382290B9BAA9E3847F2786CC74A; econAnalyticsSeq=16; econAnalyticsLastActivity=1712762706950',
            'referer': 'https://www.lotteon.com/search/search/search.ecn?render=search&platform=pc&q=%EC%88%98%EB%B6%84%ED%81%AC%EB%A6%BC&mallId=1',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        }

        name = supabaseData['name']

        response = requests.get(
            'https://www.lotteon.com/search/search/search.ecn?&u2={}&u3=60&u9=initialData&render=qapi&platform=pc&collection_id=9&q={}&mallId=1&u39=10'.format( 60*(pageCount-1),quote(name)),
            cookies=cookies,
            headers=headers,
        )
        try:
            results=json.loads(response.text)['itemList']
            print(results)
        except:
            print("자료없음")
            time.sleep(random.randint(10, 15) * 0.1)
            return []
        if len(results)==0:
            print("마지막페이지:",pageCount-1)
            break
        for result in results:
            try:
                title=result['productName']
            except:
                title=""
            print("title:",title)
            try:
                price=result['data']['final_price']
            except:
                price=""
            print("price:",price)
            try:
                url=result['productLink']
            except:
                url=""
            print("url:",url)
            if float(priceRatio)*supabaseData['priceLow']<price<supabaseData['priceLow']:
                print("찾았다!")
                #===========판매자정보가져오기
                cookies = {
                    'infw_mdia_cd': 'PC',
                    'ch_mem_no': '285068555mn7SW65f2ce593a',
                    'ch_no': '100995',
                    'ch_dtl_no': '1025316',
                    'ch_csf_cd': 'PA',
                    'ch_typ_cd': 'PA07',
                    'pcs_grp': '',
                    'site_no': '1',
                    'mall_no': '1',
                    'infw_mall_no': '1',
                    'crss_rte_nm': 'LO',
                    'crss_ntm': '1',
                    'fnl_crss_rte_nm': '',
                    'at_check': 'true',
                    'AMCVS_443A1C095C0A82400A495E92%40AdobeOrg': '1',
                    '_gcl_au': '1.1.1251061932.1712762507',
                    'AMCV_443A1C095C0A82400A495E92%40AdobeOrg': '1176715910%7CMCIDTS%7C19824%7CMCMID%7C72523635356235877200189499512793502995%7CMCAAMLH-1713367306%7C11%7CMCAAMB-1713367306%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C857883598%7CMCOPTOUT-1712769706s%7CNONE%7CvVersion%7C5.4.0',
                    '_fbp': 'fb.1.1712762506848.1943539184',
                    '_ga': 'GA1.1.2021012175.1712762507',
                    '_wp_uid': '2-9242275ca3b6eb4fd71e9a43f1adef5a-s1712217785.665417|windows_10|chrome-1m59n96',
                    'mbox': 'session#0778712c8f104f9d901962775fe68a51#1712765556|PC#0778712c8f104f9d901962775fe68a51.32_0#1776008496',
                    'cto_bundle': 'DJbky19Ud0Z0cDJ4dmdlQiUyQm5QbiUyRnglMkI1RyUyRlhaSHRjcE8xaWlONDNZNTdlbGN2Z2VvYkRaSktsTXhuJTJGbWhHT0RsSmZaOWFRNmJ0Q3RPV3l5N0E5N1VPekhTWUdDeTdmYUtadGl5eSUyQlVpbVFCWldkUHBnaTJKb21RZllodVVuRXduTEFWeDFlJTJGUENqMmJ6UFhRamcyYjF3TlVDdyUzRCUzRA',
                    '_ga_4D4NCCP4FX': 'GS1.1.1712762507.1.1.1712763704.49.0.0',
                    'on_lrtm': 'C31F055969658A0D856481617631E5586987C31F04D7A1C9992DB4EB01332002C7CB00AD12ABD976',
                }
                headers = {
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                    # 'cookie': 'infw_mdia_cd=PC; ch_mem_no=285068555mn7SW65f2ce593a; ch_no=100995; ch_dtl_no=1025316; ch_csf_cd=PA; ch_typ_cd=PA07; pcs_grp=; site_no=1; mall_no=1; infw_mall_no=1; crss_rte_nm=LO; crss_ntm=1; fnl_crss_rte_nm=; at_check=true; AMCVS_443A1C095C0A82400A495E92%40AdobeOrg=1; _gcl_au=1.1.1251061932.1712762507; AMCV_443A1C095C0A82400A495E92%40AdobeOrg=1176715910%7CMCIDTS%7C19824%7CMCMID%7C72523635356235877200189499512793502995%7CMCAAMLH-1713367306%7C11%7CMCAAMB-1713367306%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCCIDH%7C857883598%7CMCOPTOUT-1712769706s%7CNONE%7CvVersion%7C5.4.0; _fbp=fb.1.1712762506848.1943539184; _ga=GA1.1.2021012175.1712762507; _wp_uid=2-9242275ca3b6eb4fd71e9a43f1adef5a-s1712217785.665417|windows_10|chrome-1m59n96; mbox=session#0778712c8f104f9d901962775fe68a51#1712765556|PC#0778712c8f104f9d901962775fe68a51.32_0#1776008496; cto_bundle=DJbky19Ud0Z0cDJ4dmdlQiUyQm5QbiUyRnglMkI1RyUyRlhaSHRjcE8xaWlONDNZNTdlbGN2Z2VvYkRaSktsTXhuJTJGbWhHT0RsSmZaOWFRNmJ0Q3RPV3l5N0E5N1VPekhTWUdDeTdmYUtadGl5eSUyQlVpbVFCWldkUHBnaTJKb21RZllodVVuRXduTEFWeDFlJTJGUENqMmJ6UFhRamcyYjF3TlVDdyUzRCUzRA; _ga_4D4NCCP4FX=GS1.1.1712762507.1.1.1712763704.49.0.0; on_lrtm=C31F055969658A0D856481617631E5586987C31F04D7A1C9992DB4EB01332002C7CB00AD12ABD976',
                    'origin': 'https://www.lotteon.com',
                    'referer': 'https://www.lotteon.com/',
                    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
                }

                # 정규식 패턴: 'sitmNo=' 뒤부터 '&' 사이의 값을 찾음
                pattern = r'sitmNo=([^&]+)'
                # 정규식 검색
                match = re.search(pattern, url)
                if match:
                    sitmNo = match.group(1)  # 첫 번째 그룹(괄호 안)의 값을 가져옴
                    print("sitmNo:",sitmNo,"/ sitmNo_TYPE:",type(sitmNo))
                    params = {
                        'sitmNo': sitmNo,
                        # 'mall_no': '1',
                        # 'dp_infw_cd': 'SCH스카이킥 어린이 축구드론',
                        # 'areaCode': 'SCH',
                        # 'isNotContainOptMapping': 'true',
                    }

                    response = requests.get(
                        'https://pbf.lotteon.com/product/v2/detail/search/base/sitm/{}'.format(sitmNo),
                        params=params,
                        cookies=cookies,
                        headers=headers,
                    )
                    sellerInfo = json.loads(response.text)
                    # pprint.pprint(sellerInfo)
                    companyName = find_option_combinations(sellerInfo, 'sellerNm')
                    sellerName = find_option_combinations(sellerInfo, 'rprrNm')
                    phoneNo = find_option_combinations(sellerInfo, 'sellerPhone')
                    address = find_option_combinations(sellerInfo, 'stnmZipAddr') + " " + find_option_combinations(
                        sellerInfo, 'stnmDtlAddr')
                    totalInfo = companyName + "," + sellerName + "," + phoneNo + "," + address
                    data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                            'priceLow': supabaseData['priceLow'], 'platform': '롯데ON', 'url': url,
                            'salesInfo': totalInfo,
                            'inputKeyword': supabaseData['name']}
                else:
                    print("No match found")
                    data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                            'priceLow': supabaseData['priceLow'], 'platform': '롯데ON', 'url': url,
                            'salesInfo': "",
                            'inputKeyword': supabaseData['name']}
                

                dataList.append(data)
                time.sleep(random.randint(10, 15) * 0.1)
        pageCount+=1
        time.sleep(random.randint(10,15)*0.1)
    with open('dataList_LotteON.json', 'w',encoding='utf-8-sig') as f:
        json.dump(dataList, f, indent=2,ensure_ascii=False)
    return dataList

def extract_numbers_from_url(url):
    # '/stores/'와 '?' 사이의 숫자 추출
    store_number = re.search(r'/stores/(\d+)', url)
    if store_number:
        store_number = store_number.group(1)

    # 'pdpPrdNo=' 뒤의 숫자 추출
    product_number = re.search(r'pdpPrdNo=(\d+)', url)
    if product_number:
        product_number = product_number.group(1)

    return store_number, product_number

def GetArticles11(inputData,priceRatio):
    keyword=inputData['name']
    pageCount=1
    dataList=[]

    cookies = {
        'PCID': '17131880148467103680616',
        'XSRF-TOKEN': '6fbff414-35ec-a07b-0a71-5b5a30a84c96',
        'TT': 'CONN_IP_LOC%7CDOM',
        'AUID': 'AUID_QkK9WFZudXCfwu0fSk8prQ',
        '_gid': 'GA1.3.1825982365.1713188015',
        'PCID_FRV': 'true',
        'DMP_UID': '(DMPC)418d70b5-c38b-4f1d-baa5-4e8a4f3d1d0d',
        '_fbp': 'fb.2.1713188102727.1994465894',
        'RCPD': '7004310526',
        '_gcl_au': '1.1.1503612310.1713188015.662043767.1713247834.1713250599',
        'Pointory': 'ON_3',
        'XSITE': '1001652917',
        'PARTNER_CD': '1020',
        'TP': 'scrnChk%7CY%23CO_BSNS_NM%7CDefault%23EX_BH%7Cj%2FMnG78%2FkJ7DxBb4pdwYgw%3D%3D%23PARTNER_REFERER%7Chttps%3A%2F%2Fwww.google.com%2F',
        'XSITE_DETAIL': '453021863',
        '_gcl_aw': 'GCL.1713253085.EAIaIQobChMIy46Aip3GhQMVoNgWBR0UFAT8EAAYASAAEgKaE_D_BwE',
        '_gac_UA-68494772-1': '1.1713253085.EAIaIQobChMIy46Aip3GhQMVoNgWBR0UFAT8EAAYASAAEgKaE_D_BwE',
        'RAKE_SID': '17132530852205463714446',
        'RAKE_SID_XSITE': '17132530852205463714446',
        '_ga': 'GA1.3.785674265.1713188015',
        'appVCA': '""',
        '_ga_6VBF5N51X2': 'GS1.1.1713252859.8.1.1713253177.60.0.0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Cookie': 'PCID=17131880148467103680616; XSRF-TOKEN=6fbff414-35ec-a07b-0a71-5b5a30a84c96; TT=CONN_IP_LOC%7CDOM; AUID=AUID_QkK9WFZudXCfwu0fSk8prQ; _gid=GA1.3.1825982365.1713188015; PCID_FRV=true; DMP_UID=(DMPC)418d70b5-c38b-4f1d-baa5-4e8a4f3d1d0d; _fbp=fb.2.1713188102727.1994465894; RCPD=7004310526; _gcl_au=1.1.1503612310.1713188015.662043767.1713247834.1713250599; Pointory=ON_3; XSITE=1001652917; PARTNER_CD=1020; TP=scrnChk%7CY%23CO_BSNS_NM%7CDefault%23EX_BH%7Cj%2FMnG78%2FkJ7DxBb4pdwYgw%3D%3D%23PARTNER_REFERER%7Chttps%3A%2F%2Fwww.google.com%2F; XSITE_DETAIL=453021863; _gcl_aw=GCL.1713253085.EAIaIQobChMIy46Aip3GhQMVoNgWBR0UFAT8EAAYASAAEgKaE_D_BwE; _gac_UA-68494772-1=1.1713253085.EAIaIQobChMIy46Aip3GhQMVoNgWBR0UFAT8EAAYASAAEgKaE_D_BwE; RAKE_SID=17132530852205463714446; RAKE_SID_XSITE=17132530852205463714446; _ga=GA1.3.785674265.1713188015; appVCA=""; _ga_6VBF5N51X2=GS1.1.1713252859.8.1.1713253177.60.0.0',
        'Origin': 'https://search.11st.co.kr',
        'Referer': 'https://search.11st.co.kr/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'kwd': keyword,
        'tabId': 'TOTAL_SEARCH',
        # '_': '1713253177872',
    }

    response = requests.get('https://apis.11st.co.kr/search/api/tab', params=params, cookies=cookies, headers=headers)
    results = json.loads(response.text)
    # pprint.pprint(results)
    try:
        urlInfo = find_option_combinations(results, 'moreButton')['moreUrl']
    except:
        print("상품아예없음1")
        return []
    print("urlInfo:", urlInfo, "/ urlInfo_TYPE:", type(urlInfo))
    common_prd_tot_cnt_value, prd_more_start_show_cnt_value = extract_numbers_from_url2(urlInfo)
    print(common_prd_tot_cnt_value)
    print(prd_more_start_show_cnt_value)
    if common_prd_tot_cnt_value==None:
        print("상품아예없음1")
        return []
    prevCheckList=['111']
    while True:
        print("11번가★★★키워드는:{}".format(keyword))
        print("pageCount:",pageCount,"/ pageCount_TYPE:",type(pageCount))

        cookies = {
            'PCID': '17131880148467103680616',
            'XSRF-TOKEN': '6fbff414-35ec-a07b-0a71-5b5a30a84c96',
            'TT': 'CONN_IP_LOC%7CDOM',
            'AUID': 'AUID_QkK9WFZudXCfwu0fSk8prQ',
            '_gid': 'GA1.3.1825982365.1713188015',
            'PCID_FRV': 'true',
            'DMP_UID': '(DMPC)418d70b5-c38b-4f1d-baa5-4e8a4f3d1d0d',
            '_fbp': 'fb.2.1713188102727.1994465894',
            'RAKE_SID': '17132478342975330935780',
            'RAKE_SID_XSITE': '17132478342975330935780',
            'Pointory': 'ON_3',
            'XSITE': '1001652962',
            'PARTNER_CD': '1020',
            'TP': 'scrnChk%7CY%23CO_BSNS_NM%7CDefault%23EX_BH%7Cj%2FMnG78%2FkJ6CnMaPRtyeRw%3D%3D%23PARTNER_REFERER%7Chttps%3A%2F%2Fwww.google.com%2F',
            'XSITE_DETAIL': '453043861',
            '_gcl_aw': 'GCL.1713248383.CjwKCAjwoPOwBhAeEiwAJuXRhxN5E0BsOCDnZKQ7qIs5HGrQVioVBmNSHGH6Qw4DiwLyFOgIuRGNXxoCJSIQAvD_BwE',
            '_gac_UA-68494772-1': '1.1713248383.CjwKCAjwoPOwBhAeEiwAJuXRhxN5E0BsOCDnZKQ7qIs5HGrQVioVBmNSHGH6Qw4DiwLyFOgIuRGNXxoCJSIQAvD_BwE',
            '_gcl_au': '1.1.1503612310.1713188015.662043767.1713247834.1713248744',
            'appVCA': '""',
            '_ga': 'GA1.1.785674265.1713188015',
            '_ga_6VBF5N51X2': 'GS1.1.1713247833.7.1.1713249139.30.0.0',
            'RCPD': '6990282561',
        }

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'PCID=17131880148467103680616; XSRF-TOKEN=6fbff414-35ec-a07b-0a71-5b5a30a84c96; TT=CONN_IP_LOC%7CDOM; AUID=AUID_QkK9WFZudXCfwu0fSk8prQ; _gid=GA1.3.1825982365.1713188015; PCID_FRV=true; DMP_UID=(DMPC)418d70b5-c38b-4f1d-baa5-4e8a4f3d1d0d; _fbp=fb.2.1713188102727.1994465894; RAKE_SID=17132478342975330935780; RAKE_SID_XSITE=17132478342975330935780; Pointory=ON_3; XSITE=1001652962; PARTNER_CD=1020; TP=scrnChk%7CY%23CO_BSNS_NM%7CDefault%23EX_BH%7Cj%2FMnG78%2FkJ6CnMaPRtyeRw%3D%3D%23PARTNER_REFERER%7Chttps%3A%2F%2Fwww.google.com%2F; XSITE_DETAIL=453043861; _gcl_aw=GCL.1713248383.CjwKCAjwoPOwBhAeEiwAJuXRhxN5E0BsOCDnZKQ7qIs5HGrQVioVBmNSHGH6Qw4DiwLyFOgIuRGNXxoCJSIQAvD_BwE; _gac_UA-68494772-1=1.1713248383.CjwKCAjwoPOwBhAeEiwAJuXRhxN5E0BsOCDnZKQ7qIs5HGrQVioVBmNSHGH6Qw4DiwLyFOgIuRGNXxoCJSIQAvD_BwE; _gcl_au=1.1.1503612310.1713188015.662043767.1713247834.1713248744; appVCA=""; _ga=GA1.1.785674265.1713188015; _ga_6VBF5N51X2=GS1.1.1713247833.7.1.1713249139.30.0.0; RCPD=6990282561',
            'Origin': 'https://search.11st.co.kr',
            'Referer': 'https://search.11st.co.kr/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        totalUrl = 'https://apis.11st.co.kr/search/api/tab/total-search/more/common?kwd={}&tabId=TOTAL_SEARCH&&commonPrdTotCnt={}&pageNo={}&prdMoreStartShowCnt={}'.format(
            keyword, common_prd_tot_cnt_value, pageCount, prd_more_start_show_cnt_value)
        print("totalUrl:",totalUrl,"/ totalUrl_TYPE:",type(totalUrl))
        response = requests.get(
            # 'https://apis.11st.co.kr/search/api/tab/total-search/more/common?kwd=%EC%8A%A4%EC%B9%B4%EC%9D%B4%ED%82%A5&tabId=TOTAL_SEARCH&_=1713248744268&commonPrdTotCnt=108&pageNo=3&prdMoreStartShowCnt=60&dupCheckPrdNos=6822376260,4196378376,3505209770,7011517539,6270846456,4847982875,3505146723&_1713249910600',
            totalUrl,
            cookies=cookies,
            headers=headers,
        )
        try:
            results = json.loads(response.text)['items']
        except:
            print("상품페이지없음")
            break
        with open('results.json', 'w',encoding='utf-8-sig') as f:
            json.dump(results, f, indent=2,ensure_ascii=False)


        checkList=[]
        for target in results:
            # print("target:",target,"/ target_TYPE:",type(target))
            title=target.get('title',"")
            checkList.append(title)
            # print("title:",title,"/ title_TYPE:",type(title))
            url=target.get('sellerUrl',"")
            # print("url:",url,"/ url_TYPE:",type(url))
            storeNo,productNo=extract_numbers_from_url(url)
            # print("storeNo:",storeNo,"/ storeNo_TYPE:",type(storeNo))
            # print("productNo:",productNo,"/ productNo_TYPE:",type(productNo))
            price=target.get('finalPrc',"")
            # print("price:",price,"/ price_TYPE:",type(price))

            if float(priceRatio)*supabaseData['priceLow']<price<supabaseData['priceLow'] and storeNo!=None:
                sellerInfo=GetDetails11(storeNo,productNo)
                time.sleep(random.randint(10, 20) * 0.1)
                data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '11번가', 'url': url, 'salesInfo': sellerInfo,
                        'inputKeyword': supabaseData['name']}
                print("data:",data,"/ data_TYPE:",type(data))
                dataList.append(data)
        if ",".join(checkList)==",".join(prevCheckList):
          print("더없음")
          break
        prevCheckList=checkList.copy()
        pageCount+=1
        time.sleep(random.randint(10,20)*0.1)
        print("======================")
    return dataList

def GetDetails11(storeNo,productNo):
    cookies = {
        'Pointory': 'ON_3',
        'XSITE': '1001652962',
        'PARTNER_CD': '1020',
        'XSITE_DETAIL': '453043861',
        'PCID': '17131880148467103680616',
        'XSRF-TOKEN': '6fbff414-35ec-a07b-0a71-5b5a30a84c96',
        'TT': 'CONN_IP_LOC%7CDOM',
        'TP': 'CO_BSNS_NM%7CDefault%23EX_BH%7Cj%2FMnG78%2FkJ54zSto9Lvigg%3D%3D%23PARTNER_REFERER%7Chttps%3A%2F%2Fwww.google.co.kr%2F%23scrnChk%7CY',
        'AUID': 'AUID_QkK9WFZudXCfwu0fSk8prQ',
        '_gcl_aw': 'GCL.1713188015.CjwKCAjwoPOwBhAeEiwAJuXRhyDJBHBmHjM5NUU8SMSRuCjXifW0UPgbmdlqN6cHCuXrExgsP9JU9hoCOXwQAvD_BwE',
        '_gcl_au': '1.1.1503612310.1713188015',
        '_gid': 'GA1.3.1825982365.1713188015',
        '_gac_UA-68494772-1': '1.1713188015.CjwKCAjwoPOwBhAeEiwAJuXRhyDJBHBmHjM5NUU8SMSRuCjXifW0UPgbmdlqN6cHCuXrExgsP9JU9hoCOXwQAvD_BwE',
        'PCID_FRV': 'true',
        'RAKE_SID': '17131880155132948325794',
        'RAKE_SID_XSITE': '17131880155132948325794',
        'DMP_UID': '(DMPC)418d70b5-c38b-4f1d-baa5-4e8a4f3d1d0d',
        '_fbp': 'fb.2.1713188102727.1994465894',
        'RCPD': '6835418518',
        'appVCA': '""',
        '_ga': 'GA1.3.785674265.1713188015',
        '_ga_6VBF5N51X2': 'GS1.1.1713188015.1.1.1713188741.14.0.0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Cookie': 'Pointory=ON_3; XSITE=1001652962; PARTNER_CD=1020; XSITE_DETAIL=453043861; PCID=17131880148467103680616; XSRF-TOKEN=6fbff414-35ec-a07b-0a71-5b5a30a84c96; TT=CONN_IP_LOC%7CDOM; TP=CO_BSNS_NM%7CDefault%23EX_BH%7Cj%2FMnG78%2FkJ54zSto9Lvigg%3D%3D%23PARTNER_REFERER%7Chttps%3A%2F%2Fwww.google.co.kr%2F%23scrnChk%7CY; AUID=AUID_QkK9WFZudXCfwu0fSk8prQ; _gcl_aw=GCL.1713188015.CjwKCAjwoPOwBhAeEiwAJuXRhyDJBHBmHjM5NUU8SMSRuCjXifW0UPgbmdlqN6cHCuXrExgsP9JU9hoCOXwQAvD_BwE; _gcl_au=1.1.1503612310.1713188015; _gid=GA1.3.1825982365.1713188015; _gac_UA-68494772-1=1.1713188015.CjwKCAjwoPOwBhAeEiwAJuXRhyDJBHBmHjM5NUU8SMSRuCjXifW0UPgbmdlqN6cHCuXrExgsP9JU9hoCOXwQAvD_BwE; PCID_FRV=true; RAKE_SID=17131880155132948325794; RAKE_SID_XSITE=17131880155132948325794; DMP_UID=(DMPC)418d70b5-c38b-4f1d-baa5-4e8a4f3d1d0d; _fbp=fb.2.1713188102727.1994465894; RCPD=6835418518; appVCA=""; _ga=GA1.3.785674265.1713188015; _ga_6VBF5N51X2=GS1.1.1713188015.1.1.1713188741.14.0.0',
        'Origin': 'https://search.11st.co.kr',
        'Referer': 'https://search.11st.co.kr/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    url='https://shop.11st.co.kr/stores/{}?pdpPrdNo={}'.format(storeNo,productNo)
    while True:
        try:
            res=requests.get(url,headers=headers,cookies=cookies)
            break
        except:
            print("11번가 응답없음")
    # print(res.text)
    soup=BeautifulSoup(res.text,'lxml')
    table=soup.find("dl",attrs={'class':'store_info_detail'})
    infos=table.find_all('dd')
    dataList=[]
    for index,info in enumerate(infos):
        data=info.get_text().replace(" ","").replace("\n","").replace("\t","").strip()
        dataList.append(data)
    dataString=",".join(dataList)
    # print("dataString:",dataString,"/ dataString_TYPE:",type(dataString))
    return dataString
def GetMaru(supabaseData,priceRatio):
    pageCount=1
    dataList=[]
    keyword=supabaseData['name']
    while True:
        print("마루★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            'ec_category': 'category_no%3D172%26category_name%3D%25EC%25A0%2584%25EC%25B2%25B4%25EC%2583%2581%25ED%2592%2588',
            'ECSESSID': '8db1837d94991de2a5cadd55c4474fc2',
            'basketcount_1': '0',
            'atl_epcheck': '1',
            'atl_option': '1%2C1%2CH',
            'fb_external_id': '0153238020fa83c054392d07b595c9a64de3790272c44056f287c72c06b1717b',
            '_fwb': '183L6Zd3ZlzolRJo7mV3N3F.1713408583575',
            'ec_ipad_device': 'F',
            'isviewtype': 'pc',
            'CFAE_CID': 'CFAE_CID.maruhanmall_1.2XNYA0F.1713408584197',
            'CFAE_CUK1Y': 'CFAE_CUK1Y.maruhanmall_1.2XNYA0F.1713408584197',
            'CFAE_CUK45': 'CFAE_CUK45.maruhanmall_1.2XNYA0F.1713408584197',
            'CVID': 'CVID.5c53464150545e54525c586e06.1713408584197',
            'CVID_Y': 'CVID_Y.5c53464150545e54525c586e06.1713408584197',
            'CUK45': 'cuk45_maruhanmall_8db1837d94991de2a5cadd55c4474fc2',
            'CUK2Y': 'cuk2y_maruhanmall_8db1837d94991de2a5cadd55c4474fc2',
            'CID': 'CIDRe8773a6093353b7f5964449c45b6eadf',
            'CIDRe8773a6093353b7f5964449c45b6eadf': '7914383b5105e1f428a5c1c78caa5f1a%3A%3A%3A%3A%3A%3Ahttps%3A%2F%2Fwww.google.co.kr%2F%3A%3A%EA%B5%AC%EA%B8%80%3A%3A1%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%2F%3A%3A1713408583%3A%3A%3A%3Appdp%3A%3A1713408583%3A%3A%3A%3A%3A%3A%3A%3A',
            '_ga': 'GA1.2.1739008184.1713408584',
            '_gid': 'GA1.2.94293648.1713408584',
            'view_product_map': 'a%3A1%3A%7Bi%3A1%3Ba%3A1%3A%7Bi%3A0%3Bi%3A496%3B%7D%7D',
            'recent_plist': '496',
            '_gat_UA-216495125-1': '1',
            'wcs_bt': 's_462f70e42f12:1713408693',
            'fb_event_id': 'event_id.maruhanmall.1.43BSCAQI8WSMVEOXGXUK7CZAB101XMY',
            'vt': '1713408693',
            'CFAE_LC': 'CFAE_LC.maruhanmall_1.A1X9HY5.1713408693705',
            '_ga_XJ6PBK8WLN': 'GS1.2.1713408584.1.1.1713408693.0.0.0',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': 'ec_category=category_no%3D172%26category_name%3D%25EC%25A0%2584%25EC%25B2%25B4%25EC%2583%2581%25ED%2592%2588; ECSESSID=8db1837d94991de2a5cadd55c4474fc2; basketcount_1=0; atl_epcheck=1; atl_option=1%2C1%2CH; fb_external_id=0153238020fa83c054392d07b595c9a64de3790272c44056f287c72c06b1717b; _fwb=183L6Zd3ZlzolRJo7mV3N3F.1713408583575; ec_ipad_device=F; isviewtype=pc; CFAE_CID=CFAE_CID.maruhanmall_1.2XNYA0F.1713408584197; CFAE_CUK1Y=CFAE_CUK1Y.maruhanmall_1.2XNYA0F.1713408584197; CFAE_CUK45=CFAE_CUK45.maruhanmall_1.2XNYA0F.1713408584197; CVID=CVID.5c53464150545e54525c586e06.1713408584197; CVID_Y=CVID_Y.5c53464150545e54525c586e06.1713408584197; CUK45=cuk45_maruhanmall_8db1837d94991de2a5cadd55c4474fc2; CUK2Y=cuk2y_maruhanmall_8db1837d94991de2a5cadd55c4474fc2; CID=CIDRe8773a6093353b7f5964449c45b6eadf; CIDRe8773a6093353b7f5964449c45b6eadf=7914383b5105e1f428a5c1c78caa5f1a%3A%3A%3A%3A%3A%3Ahttps%3A%2F%2Fwww.google.co.kr%2F%3A%3A%EA%B5%AC%EA%B8%80%3A%3A1%3A%3A%3A%3A%3A%3A%3A%3A%3A%3A%2F%3A%3A1713408583%3A%3A%3A%3Appdp%3A%3A1713408583%3A%3A%3A%3A%3A%3A%3A%3A; _ga=GA1.2.1739008184.1713408584; _gid=GA1.2.94293648.1713408584; view_product_map=a%3A1%3A%7Bi%3A1%3Ba%3A1%3A%7Bi%3A0%3Bi%3A496%3B%7D%7D; recent_plist=496; _gat_UA-216495125-1=1; wcs_bt=s_462f70e42f12:1713408693; fb_event_id=event_id.maruhanmall.1.43BSCAQI8WSMVEOXGXUK7CZAB101XMY; vt=1713408693; CFAE_LC=CFAE_LC.maruhanmall_1.A1X9HY5.1713408693705; _ga_XJ6PBK8WLN=GS1.2.1713408584.1.1.1713408693.0.0.0',
            'priority': 'u=0, i',
            'referer': 'https://maruhanmall.com/product/search.html?banner_action=&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }

        params = {
            'banner_action': '',
            'keyword': supabaseData['name'],
            'page': pageCount,
        }
        response = requests.get('https://maruhanmall.com/product/search.html', params=params, cookies=cookies,
                                headers=headers)
        soup=BeautifulSoup(response.text,'lxml')
        # print(soup.prettify())
        table=soup.find("ul",attrs={'class':'prdList grid5'})
        if table==None:
            print("더없음")
            break
        items=table.find_all('li',attrs={'class':'item xans-record-'})
        for item in items:
            try:
                url='https://maruhanmall.com/'+item.find('a')['href']
            except:
                url=""

            print("url:",url)
            try:
                productName=item.find('p',attrs={'class':'name'}).get_text().replace("\n","").replace("상품명 :","").strip()
            except:
                productName=""
            print("productName:",productName)
            try:
                price=item.find('ul',attrs={'class':'xans-element- xans-search xans-search-listitem spec'}).get_text().replace(",","").replace("원","").replace("판매가 :","").strip()
                regex=re.compile('\d+')
                price=int(regex.findall(price)[0])

            except:
                price=999999999999
            print("price:",price)
            if float(priceRatio)*supabaseData['priceLow']<price<supabaseData['priceLow']:
                data = {'title': productName, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '마루한몰', 'url': url, 'salesInfo': "",
                        'inputKeyword': supabaseData['name']}
                print("data:",data,"/ data_TYPE:",type(data))
                dataList.append(data)
        pageCount+=1
        time.sleep(1)
    return dataList

def GetTeacherMall(supabaseData,priceRatio):
    pageCount=1
    dataList=[]
    keyword=supabaseData['name']
    endFlag=False
    while True:

        print("티처몰★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            'mobileapp': 'N',
            'shopteachervillecokr_firstmall': '3d35de176c2511b7ce7158222f5c747f99cfddb9',
            'shopReferer': 'https%3A%2F%2Fwww.google.co.kr%2F',
            'refererDomain': 'google.co.kr',
            'marketplace': 'google',
            'mobileapp': 'N',
            'shopteachervillecokrvisitorInfo_0001': 'a%3A2%3A%7Bs%3A4%3A%22date%22%3Bs%3A10%3A%222024-04-22%22%3Bs%3A7%3A%22referer%22%3Bs%3A25%3A%22https%3A%2F%2Fwww.google.co.kr%2F%22%3B%7D',
            '_gcl_au': '1.1.828327163.1713794744',
            '_fbp': 'fb.2.1713794743654.1897083673',
            '_fwb': '148tTOHwMIAhCR9NSWhHFuL.1713794743856',
            '_clck': '1bvp4so%7C2%7Cfl5%7C0%7C1573',
            'CART_ID': '3d35de176c2511b7ce7158222f5c747f99cfddb9',
            'mi_ticker_id': 'pp1bgDi_616afeef37d1e0',
            '_mi_board_statue': '0',
            'pop_main_cookie_142': 'view',
            'searchKeyword': 'a%3A1%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A7%3A%22keyword%22%3Bs%3A12%3A%22%EC%9E%90%EC%84%9D%EB%B3%B4%EB%93%9C%22%3Bs%3A4%3A%22time%22%3Bs%3A19%3A%222024-04-22+23%3A05%3A48%22%3B%7D%7D',
            '_ga': 'GA1.1.1052549675.1713794750',
            'wcs_bt': 's_4ab8832a3007:1713794750',
            '_ga_KH5XEFNW3Z': 'GS1.1.1713794749.1.0.1713794750.59.0.0',
            '_clsk': 'xuhdyq%7C1713794751099%7C2%7C1%7Ca.clarity.ms%2Fcollect',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'mobileapp=N; shopteachervillecokr_firstmall=3d35de176c2511b7ce7158222f5c747f99cfddb9; shopReferer=https%3A%2F%2Fwww.google.co.kr%2F; refererDomain=google.co.kr; marketplace=google; mobileapp=N; shopteachervillecokrvisitorInfo_0001=a%3A2%3A%7Bs%3A4%3A%22date%22%3Bs%3A10%3A%222024-04-22%22%3Bs%3A7%3A%22referer%22%3Bs%3A25%3A%22https%3A%2F%2Fwww.google.co.kr%2F%22%3B%7D; _gcl_au=1.1.828327163.1713794744; _fbp=fb.2.1713794743654.1897083673; _fwb=148tTOHwMIAhCR9NSWhHFuL.1713794743856; _clck=1bvp4so%7C2%7Cfl5%7C0%7C1573; CART_ID=3d35de176c2511b7ce7158222f5c747f99cfddb9; mi_ticker_id=pp1bgDi_616afeef37d1e0; _mi_board_statue=0; pop_main_cookie_142=view; searchKeyword=a%3A1%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A7%3A%22keyword%22%3Bs%3A12%3A%22%EC%9E%90%EC%84%9D%EB%B3%B4%EB%93%9C%22%3Bs%3A4%3A%22time%22%3Bs%3A19%3A%222024-04-22+23%3A05%3A48%22%3B%7D%7D; _ga=GA1.1.1052549675.1713794750; wcs_bt=s_4ab8832a3007:1713794750; _ga_KH5XEFNW3Z=GS1.1.1713794749.1.0.1713794750.59.0.0; _clsk=xuhdyq%7C1713794751099%7C2%7C1%7Ca.clarity.ms%2Fcollect',
            'Referer': 'https://shop.teacherville.co.kr/goods/search?keyword_log_flag=Y&search_text=%EC%9E%90%EC%84%9D%EB%B3%B4%EB%93%9C',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'page': pageCount,
            'search_text': supabaseData['name'],
            'popup': '',
            'iframe': '',
            'old_search_text': supabaseData['name'],
            'category1': '',
            'old_category1': '',
            # 'totalcount': '111',
        }

        response = requests.get('https://shop.teacherville.co.kr/goods/search', params=params, cookies=cookies,
                                headers=headers)
        soup=BeautifulSoup(response.text,'lxml')
        items=soup.find_all('li',attrs={'class':'goodsDisplayWrap'})
        
        if len(items)==0:
            print("더 없음")
            break
        for item in items:

            try:
                # url='https://shop.teacherville.co.kr/goods/view?no='+item.find('a')['onclick']
                url=item.find('a')['onclick']
                regex=re.compile('\d+')
                result=regex.findall(url)[0]
                url='https://shop.teacherville.co.kr/goods/view?no='+result
            except:
                url=""
            if url=="":
                print("다찾음")
                endFlag=True
                break
            print("url:",url)
            try:
                productName=item.find('span').get_text()
            except:
                productName=""
            print("productName:",productName)
            try:
                price=item.find('span',attrs={'style':'color:#ff2100;font-weight:bold;text-decoration:none;'}).get_text().replace(",","")
                regex=re.compile('\d+')
                price=int(regex.findall(price)[0])
            except:
                price=999999999999
            print("price:",price)
            if float(priceRatio)*supabaseData['priceLow']<price<supabaseData['priceLow']:
                data = {'title': productName, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '티처몰', 'url': url, 'salesInfo': "",
                        'inputKeyword': supabaseData['name']}
                print("data:",data,"/ data_TYPE:",type(data))
                dataList.append(data)
        if endFlag==True:
            break
        print("============================")
        pageCount+=1
        time.sleep(1)
    return dataList
def GetArticlesIcecreamMall(inputData,priceRatio):
    keyword = inputData['name']
    pageCount = 1
    dataList = []
    while True:
        print("아이스크림몰★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            'WMONID': 'gzb8FkJA0ro',
            '_firstmall': 'qnr5qttbcumdmiaen3sjig2i1sqorf71',
            'MALL_CODE': '0001',
            'marketplace': 'direct',
            'i-screammallcokrvisitorInfo': 'a%3A3%3A%7Bs%3A9%3A%22mall_code%22%3Bs%3A4%3A%220001%22%3Bs%3A4%3A%22date%22%3Bs%3A10%3A%222024-04-25%22%3Bs%3A7%3A%22referer%22%3BN%3B%7D',
            '_gid': 'GA1.3.1969522420.1714017570',
            '_fwb': '1242vg3klaHWapBQH05vcTd.1714017569889',
            'today_view': 'a%3A1%3A%7Bi%3A0%3Bi%3A980511%3B%7D',
            'wcs_bt': 's_5967a8bb59a:1714017799',
            '_ga_54D4SXDVJD': 'GS1.1.1714017569.1.1.1714017799.60.0.0',
            '_ga': 'GA1.3.1426996756.1714017569',
            '_gat_gtag_UA_99932460_1': '1',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'WMONID=gzb8FkJA0ro; _firstmall=qnr5qttbcumdmiaen3sjig2i1sqorf71; MALL_CODE=0001; marketplace=direct; i-screammallcokrvisitorInfo=a%3A3%3A%7Bs%3A9%3A%22mall_code%22%3Bs%3A4%3A%220001%22%3Bs%3A4%3A%22date%22%3Bs%3A10%3A%222024-04-25%22%3Bs%3A7%3A%22referer%22%3BN%3B%7D; _gid=GA1.3.1969522420.1714017570; _fwb=1242vg3klaHWapBQH05vcTd.1714017569889; today_view=a%3A1%3A%7Bi%3A0%3Bi%3A980511%3B%7D; wcs_bt=s_5967a8bb59a:1714017799; _ga_54D4SXDVJD=GS1.1.1714017569.1.1.1714017799.60.0.0; _ga=GA1.3.1426996756.1714017569; _gat_gtag_UA_99932460_1=1',
            'Referer': 'https://i-screammall.co.kr/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'page': pageCount,
            'search_text': keyword,
            'popup': '',
            'iframe': '',
            'category1': '',
        }

        response = requests.get('https://i-screammall.co.kr/goods/search', params=params, cookies=cookies,
                                headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        itemGroup = soup.find("div", attrs={'class': 'md_products_wrap'})
        isItemGroup=len(soup.find_all("div", attrs={'class': 'md_products_wrap'}))>=1
        print("isItemGroup:",isItemGroup,"/ isItemGroup_TYPE:",type(isItemGroup))
        if isItemGroup==False:
            print("상품없음1")
            break
        items = itemGroup.find_all('li')
        if len(items)==0:
            print("상품없음2")
            break
        checkList=[]
        for index,item in enumerate(items):
            try:
                url = "https://i-screammall.co.kr" + item.find("a")['href']
            except:
                print("상품없음")
                continue
            if url == "https://i-screammall.co.kr#":
                continue
            print("url:", url, "/ url_TYPE:", type(url))
            title = item.find("span", attrs={'class': 'goods_name slidegoods_name'}).get_text().strip()
            print("title:", title, "/ title_TYPE:", type(title))
            price = item.find('span', attrs={'class': 'sale_price slidegood_price'}).get_text().replace(",","").replace("원","")
            regex = re.compile("\d+")
            price = int(regex.findall(price)[-1])
            print("price:", price, "/ price_TYPE:", type(price))
            checkList.append(title)
            if float(priceRatio) * supabaseData['priceLow'] < price < supabaseData['priceLow']:
                sellerInfo = GetDetailsIcecreamMall(url)
                time.sleep(random.randint(10, 20) * 0.1)
                data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '아이스크림몰', 'url': url, 'salesInfo': sellerInfo,
                        'inputKeyword': supabaseData['name']}
                print("data:", data, "/ data_TYPE:", type(data))
                dataList.append(data)
                time.sleep(random.randint(10, 20) * 0.1)
        if len(checkList)==0:
            print("상품없음3")
            break


        pageCount += 1
        time.sleep(random.randint(10, 20) * 0.1)
        print("======================")
    return dataList
def GetDetailsIcecreamMall(url):
    cookies = {
        'WMONID': 'gzb8FkJA0ro',
        '_firstmall': 'qnr5qttbcumdmiaen3sjig2i1sqorf71',
        'MALL_CODE': '0001',
        'marketplace': 'direct',
        'i-screammallcokrvisitorInfo': 'a%3A3%3A%7Bs%3A9%3A%22mall_code%22%3Bs%3A4%3A%220001%22%3Bs%3A4%3A%22date%22%3Bs%3A10%3A%222024-04-25%22%3Bs%3A7%3A%22referer%22%3BN%3B%7D',
        '_gid': 'GA1.3.1969522420.1714017570',
        '_fwb': '1242vg3klaHWapBQH05vcTd.1714017569889',
        'today_view': 'a%3A2%3A%7Bi%3A0%3Bi%3A980511%3Bi%3A1%3Bi%3A258913%3B%7D',
        'wcs_bt': 's_5967a8bb59a:1714026299',
        '_ga_54D4SXDVJD': 'GS1.1.1714026296.2.1.1714026300.56.0.0',
        '_ga': 'GA1.3.1426996756.1714017569',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'WMONID=gzb8FkJA0ro; _firstmall=qnr5qttbcumdmiaen3sjig2i1sqorf71; MALL_CODE=0001; marketplace=direct; i-screammallcokrvisitorInfo=a%3A3%3A%7Bs%3A9%3A%22mall_code%22%3Bs%3A4%3A%220001%22%3Bs%3A4%3A%22date%22%3Bs%3A10%3A%222024-04-25%22%3Bs%3A7%3A%22referer%22%3BN%3B%7D; _gid=GA1.3.1969522420.1714017570; _fwb=1242vg3klaHWapBQH05vcTd.1714017569889; today_view=a%3A2%3A%7Bi%3A0%3Bi%3A980511%3Bi%3A1%3Bi%3A258913%3B%7D; wcs_bt=s_5967a8bb59a:1714026299; _ga_54D4SXDVJD=GS1.1.1714026296.2.1.1714026300.56.0.0; _ga=GA1.3.1426996756.1714017569',
        'Referer': 'https://i-screammall.co.kr/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'no': '258913',
    }

    response = requests.get(url, params=params, cookies=cookies, headers=headers)
    soup=BeautifulSoup(response.text,'lxml')
    table=soup.find_all("table",attrs={'class':'bbslist_table_style bbslist_table_style2'})[-1]
    rows=table.find_all("tr")
    sellerInfoList=[]
    for row in rows:
        try:
            rowName=row.find("th")
            rowValue=row.find("td")
            if rowName.find("상호")>=0:
                sellerInfoList.append(rowValue)
            if rowName.find("소재지")>=0:
                sellerInfoList.append(rowValue)
            if rowName.find("사업자번호")>=0:
                sellerInfoList.append(rowValue)
        except:
            print("지나감")
    sellerInfo=",".join(sellerInfoList)

    return sellerInfo
def GetArticlesIschoolShop(supabaseData,priceRatio):
    keyword = supabaseData['name']
    pageCount = 1
    dataList = []
    while True:
        print("아이스쿨샵★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            'GD5SESSID': 'hg744mivkfvq8brpadj0n8gqi7paglngs1uk2irmf9nurn31mv5q272ml9h7cbeh06q23l8f9ps8n5ndv8oslolhek4ajq468s5bd50',
            '_fwb': '250G5mVIEUtWr01XgrGZDsb.1714113181170',
            'popupCode_layer_19': 'true',
            'todayGoodsNo': '%5B%221000004410%22%5D',
            'recentKeyword': '%5B%22%5Cucf54%5Cub529%5E%7C%5E2024.04.26%22%2C%22%5Cub4dc%5Cub860%5E%7C%5E2024.04.26%22%2C%22%5Cuc2a4%5Cuce74%5Cuc774%5Cud0a5%5E%7C%5E2024.04.26%22%2C%22%5Cub9d0%5Cub791%5Cucf54%5Cub529%5E%7C%5E2024.04.26%22%5D',
            'wcs_bt': 's_419fddbe88af:1714113332',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'GD5SESSID=hg744mivkfvq8brpadj0n8gqi7paglngs1uk2irmf9nurn31mv5q272ml9h7cbeh06q23l8f9ps8n5ndv8oslolhek4ajq468s5bd50; _fwb=250G5mVIEUtWr01XgrGZDsb.1714113181170; popupCode_layer_19=true; todayGoodsNo=%5B%221000004410%22%5D; recentKeyword=%5B%22%5Cucf54%5Cub529%5E%7C%5E2024.04.26%22%2C%22%5Cub4dc%5Cub860%5E%7C%5E2024.04.26%22%2C%22%5Cuc2a4%5Cuce74%5Cuc774%5Cud0a5%5E%7C%5E2024.04.26%22%2C%22%5Cub9d0%5Cub791%5Cucf54%5Cub529%5E%7C%5E2024.04.26%22%5D; wcs_bt=s_419fddbe88af:1714113332',
            'Referer': 'http://ischoolshop.co.kr/goods/goods_search.php?reSearchKeyword%5B%5D=%EB%93%9C%EB%A1%A0&reSearchKey%5B%5D=all&sort=&pageNum=20&key=goodsNm&keyword=%EC%BD%94%EB%94%A9&cateGoods%5B%5D=&cateGoods%5B%5D=&cateGoods%5B%5D=&cateGoods%5B%5D=&goodsPrice%5B%5D=&goodsPrice%5B%5D=',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }

        params = {
            'page': pageCount,
            'reSearchKeyword[]': keyword,
            'reSearchKey[]': 'all',
            'sort': '',
            'pageNum': '20',
            'key': 'goodsNm',
            'keyword': keyword,
            'cateGoods[]': [
                '',
                '',
                '',
                '',
            ],
            'goodsPrice[]': [
                '',
                '',
            ],
        }
        try:
            response = requests.get(
                'http://ischoolshop.co.kr/goods/goods_search.php',
                params=params,
                cookies=cookies,
                headers=headers,
                verify=False,
            )
        except:
            print("페이지없음")
            break

        soup = BeautifulSoup(response.text, 'lxml')
        print(soup.prettify())
        itemGroup = soup.find("div", attrs={'class': 'goods_list_cont'})
        items = itemGroup.find_all('li')
        if len(items) == 0:
            print("상품없음2")
            break
        checkList = []
        for index, item in enumerate(items):
            try:
                url = "https://ischoolshop.co.kr" + item.find("a")['href']
            except:
                print("상품없음")
                continue
            print("url:", url, "/ url_TYPE:", type(url))
            title = item.find("strong", attrs={'class': 'item_name'}).get_text().strip()
            print("title:", title, "/ title_TYPE:", type(title))
            price = item.find('strong', attrs={'class': 'item_price'}).get_text().replace(",", "").replace("원","")
            regex = re.compile("\d+")
            price = int(regex.findall(price)[-1])
            print("price:", price, "/ price_TYPE:", type(price))
            checkList.append(title)
            if float(priceRatio) * supabaseData['priceLow'] < price < supabaseData['priceLow']:
                time.sleep(random.randint(10, 20) * 0.1)
                data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '아이스쿨샵', 'url': url, 'salesInfo': "",
                        'inputKeyword': supabaseData['name']}
                print("data:", data, "/ data_TYPE:", type(data))
                dataList.append(data)
                time.sleep(random.randint(10, 20) * 0.1)
        if len(checkList) == 0:
            print("상품없음3")
            break

        pageCount += 1
        time.sleep(random.randint(10, 20) * 0.1)
        print("======================")
    return dataList
def GetSearchPopcone(supabaseData,priceRatio):
    keyword = supabaseData['name']
    pageCount = 1
    dataList = []
    while True:
        print("팝콘★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            'GD5SESSID': 'jbma5a1fl139jk04860mlgfr9atjcnn13um8dv692oqomo1nekrt95jur32jl2d6i21j7pdl7eqgs749ncgmt2g1mto0morg96gvb60',
            '_fwb': '246ooYNETet6dwNQB66wNLO.1714544649572',
            'recentKeywordMobile': '%5B%22%5Cub9d0%5Cub791%5Cucf54%5Cub529%5E%7C%5E2024.05.01%22%5D',
            'wcs_bt': 's_17c4c8aac4fd:1714544673',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': 'GD5SESSID=jbma5a1fl139jk04860mlgfr9atjcnn13um8dv692oqomo1nekrt95jur32jl2d6i21j7pdl7eqgs749ncgmt2g1mto0morg96gvb60; _fwb=246ooYNETet6dwNQB66wNLO.1714544649572; recentKeywordMobile=%5B%22%5Cub9d0%5Cub791%5Cucf54%5Cub529%5E%7C%5E2024.05.01%22%5D; wcs_bt=s_17c4c8aac4fd:1714544673',
            'priority': 'u=0, i',
            'referer': 'https://m.popcone.co.kr/goods/goods_search.php?keyword=%EB%A7%90%EB%9E%91%EC%BD%94%EB%94%A9',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }

        params = {
            'mode': 'get_search_list',
            'keyword': keyword,
            'displayType': '01',
            'page': pageCount,
            'sort': '',
        }


        try:
            response = requests.get('https://m.popcone.co.kr/goods/goods_search.php', params=params, cookies=cookies,
                                    headers=headers)
        except:
            print("페이지없음")
            break

        soup = BeautifulSoup(response.text, 'lxml')
        print(soup.prettify())
        # itemGroup = soup.find("ul", attrs={'class': 'goods_product_list'})
        items = soup.find_all('li',attrs={'class':'goods_prd_item2 list_num_2'})
        if len(items) == 0:
            print("상품없음2")
            break
        checkList = []
        for index, item in enumerate(items):
            try:
                url = "https://m.popcone.co.kr/" + item.find("a")['href']
            except:
                print("상품없음")
                continue
            print("url:", url, "/ url_TYPE:", type(url))
            title = item.find("li", attrs={'class': 'prd_name'}).get_text().strip()
            print("title:", title, "/ title_TYPE:", type(title))
            price = item.find('span', attrs={'class': 'c_price'}).get_text().replace(",", "").replace("원", "")
            regex = re.compile("\d+")
            price = int(regex.findall(price)[-1])
            print("price:", price, "/ price_TYPE:", type(price))
            checkList.append(title)
            if float(priceRatio) * supabaseData['priceLow'] < price < supabaseData['priceLow']:
                data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '팝콘에듀', 'url': url, 'salesInfo': "",
                        'inputKeyword': supabaseData['name']}
                print("data:", data, "/ data_TYPE:", type(data))
                dataList.append(data)
        if len(checkList) == 0:
            print("상품없음3")
            break

        pageCount += 1
        time.sleep(random.randint(10, 20) * 0.1)
        print("======================")
    return dataList
def GetSearchGmarket(supabaseData,priceRatio):
    keyword = supabaseData['name']
    pageCount = 1
    dataList = []
    prevCheckList = ['11']
    while True:
        print("지마켓★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        import requests

        cookies = {
            'cguid': '11714535924876009952000000',
            'pguid': '21714535924876009952010000',
            'sguid': '31714535924876009952200000',
            '_ga': 'GA1.1.1079676716.1714535926',
            '6361c5a58da80370cd396c77654e6153': 'db823101c3cd8771e2d508ba3bbcaaf7',
            'charset': 'enUS',
            'shipnation': 'KR',
            '_fbp': 'fb.2.1714535932408.1996552083',
            'WingFlag': 'R',
            'jaehuid': '200011415',
            'kwid': 'Cj0KCQjw0MexBhD3ARIsAEI3WHILO2fb_ybQmX_b6kuIO9WueUrQvnpT6h1w-oWni3VGoJLLWng__bwaAo5uEALw_wcB',
            'lnd_kwd': 'undefined',
            '9b5ac327653ddb71c4abb11d9b645ca3': 'e3ef247aabdb3fa8f8e9bb129696f273',
            'user%5Finfo': 'isNego=N',
            'Sif': 'ef8567df923705cef3692c0b87d2dbe2',
            'gmktloadingtimecheck': 'N',
            'Pif': 'E9F8C5476690D6E17BFF5A32D38D4947E4FE37D1DA7AC012C0A5847EC4922429B44DE7EB1C4DAF8F56AB6C2C3916B9B9',
            'BASKET%5FCALLBACK%5FSTAT': 'F',
            'ASPSESSIONIDSQRASARC': 'BFCIAECBIDEDKFONANKMPNCB',
            'PCUID': '17145499416612791860207',
            'bm_mi': '2541CBAE52621DD2A42F465E144F1BA5~YAAQVaUrF+cWsCiPAQAAkP4jMxctnPLA6Jvb8hO9eVCT+U4m7Ai5t35NREZOIxyzssuMFfRUlovV1Tr9P0ZiMdamdQKbTNbk3ZG2TVwCGuTufblYbB6zIFVe/Z+oN44/Q8H19cl2jcuwm1Kub+ckPvXPqvz23YQjoXCBK9KluntQvsiDoE9Kik3IPIzOyWFms1S4iTRktLghCN4sG5vQvdP1/YxkHoHA35JUEj7vOJy3+EN9PsIkLkjLzY5h67JQb/zo19elGeJnzy6GtCrweF/NV6o/qSJ4sIqgplNhPquVI3K5pWu9beUEj+6IQEYC2g4WHCwb75sqhmqZbbrMb5c=~1',
            'giftAniShowed': '%5B%221478154564%22%2C%223139865443%22%2C%222337367942%22%5D',
            'bm_sv': '7DF1D5CB9B8504325FDA39C600CA8F14~YAAQVaUrFyEXsCiPAQAA8gAkMxeFQ5YPjYLNd/ZH4/Onz6GhqT9GH/8B3nDEoU9SxIBY0uGeNzhPLaijyeGGHQm7ZU978f6mJoORb7q5eaoMmOl9NGKZdBmnhFY3WUHt/FhbAQ9OOGuE6bIw1Gd1z90BntQF1rrGjLX79APNR4JtnDBjakKsG8vhmu7q7uhqdKk4FMnlhkGLEGqsY1Dr7wmbBUS7mcGZ+BpodP7Mx6OXRrRET616596UQMCUsA6CHi4s~1',
            'ak_bmsc': '8986C00C89C6DB78CFDCC9F6CC23D443~000000000000000000000000000000~YAAQVaUrFzMXsCiPAQAA+gEkMxdmbuSkImbRb1RM2jW/W4ZP5H72HbTW3nGpeaX9Tj2hAyCT2FhCXchT+NqaTdN4e4JhdwUwwElBwGSIeLJPnfYtzVQngN9RfAb6fFIaWiJletN6gQ4uVgDxwtvTMI4luK8fymQeCQeGzR86lEuFzaGbQHb2XfAUSiNaQV5fRbO315ulYlyhMw+m30vEm0MdSkU6jHp2AikQvYfswJ7/D+OLJdotCPh6yxUajW/BPRs2rCK1GXhdHZ9KblsWCVaX/PdXaw5OFWpIaSr0VlJ31/YtARnXmzqtRNeDjspyAuyC+Th/Q02+gQrVD4AACjsIzsDupHejQYGT9FuVxMfuW76iUOIrY1RmLfh0yHS1H/zK12CJc/0KmHbwYnXOo/oyLkuvzV/TytluvMbhe1NB9syfdNvRMOuP8JOcWePaDd1rXluED2cUzFT/FOlEdLSv3BxGyo/tBtnFsY/HtjXbjbeD09WVbpps9oDxcFns3Pe4',
            'ssguid': '317145499413540020222000003',
            '5b5a8868cb3cb2da80cdab9359fc0332': '403179ee86b4d89dee5247564f8d1652',
            'cto_bundle': 'fO2Yu19NZ3d3TDNmOGpvMyUyQiUyQnRqTGJieHZpMW5pd1Y2ejN6TlBxRFlWUkhqRmFWaDNrc2dybjJrYTBQQTVsSHZ2ZXczZ2ZFelBsM3AxUDJSV2JVVUhuM3clMkJIaWdJc3dBRTZmTkl2STAzcFd5QkVmN3QlMkJGbWRwZlFCZGo3ZXBTbXVKaW1Tc21XUmMzUEJkNTlWUWR2NmxOS0RCRkVtTE9GbXFmTmhDNHYzdWszTE9WcVhyZ1duU3FkbnFwakQ5eDJiVmVud1dqSkhyNlNmOFdzamxxOEF4QWIzZ0ElM0QlM0Q',
            '_ga_1BYVQK09SB': 'GS1.1.1714549914.2.1.1714550964.3.0.0',
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'cguid=11714535924876009952000000; pguid=21714535924876009952010000; sguid=31714535924876009952200000; _ga=GA1.1.1079676716.1714535926; 6361c5a58da80370cd396c77654e6153=db823101c3cd8771e2d508ba3bbcaaf7; charset=enUS; shipnation=KR; _fbp=fb.2.1714535932408.1996552083; WingFlag=R; jaehuid=200011415; kwid=Cj0KCQjw0MexBhD3ARIsAEI3WHILO2fb_ybQmX_b6kuIO9WueUrQvnpT6h1w-oWni3VGoJLLWng__bwaAo5uEALw_wcB; lnd_kwd=undefined; 9b5ac327653ddb71c4abb11d9b645ca3=e3ef247aabdb3fa8f8e9bb129696f273; user%5Finfo=isNego=N; Sif=ef8567df923705cef3692c0b87d2dbe2; gmktloadingtimecheck=N; Pif=E9F8C5476690D6E17BFF5A32D38D4947E4FE37D1DA7AC012C0A5847EC4922429B44DE7EB1C4DAF8F56AB6C2C3916B9B9; BASKET%5FCALLBACK%5FSTAT=F; ASPSESSIONIDSQRASARC=BFCIAECBIDEDKFONANKMPNCB; PCUID=17145499416612791860207; bm_mi=2541CBAE52621DD2A42F465E144F1BA5~YAAQVaUrF+cWsCiPAQAAkP4jMxctnPLA6Jvb8hO9eVCT+U4m7Ai5t35NREZOIxyzssuMFfRUlovV1Tr9P0ZiMdamdQKbTNbk3ZG2TVwCGuTufblYbB6zIFVe/Z+oN44/Q8H19cl2jcuwm1Kub+ckPvXPqvz23YQjoXCBK9KluntQvsiDoE9Kik3IPIzOyWFms1S4iTRktLghCN4sG5vQvdP1/YxkHoHA35JUEj7vOJy3+EN9PsIkLkjLzY5h67JQb/zo19elGeJnzy6GtCrweF/NV6o/qSJ4sIqgplNhPquVI3K5pWu9beUEj+6IQEYC2g4WHCwb75sqhmqZbbrMb5c=~1; giftAniShowed=%5B%221478154564%22%2C%223139865443%22%2C%222337367942%22%5D; bm_sv=7DF1D5CB9B8504325FDA39C600CA8F14~YAAQVaUrFyEXsCiPAQAA8gAkMxeFQ5YPjYLNd/ZH4/Onz6GhqT9GH/8B3nDEoU9SxIBY0uGeNzhPLaijyeGGHQm7ZU978f6mJoORb7q5eaoMmOl9NGKZdBmnhFY3WUHt/FhbAQ9OOGuE6bIw1Gd1z90BntQF1rrGjLX79APNR4JtnDBjakKsG8vhmu7q7uhqdKk4FMnlhkGLEGqsY1Dr7wmbBUS7mcGZ+BpodP7Mx6OXRrRET616596UQMCUsA6CHi4s~1; ak_bmsc=8986C00C89C6DB78CFDCC9F6CC23D443~000000000000000000000000000000~YAAQVaUrFzMXsCiPAQAA+gEkMxdmbuSkImbRb1RM2jW/W4ZP5H72HbTW3nGpeaX9Tj2hAyCT2FhCXchT+NqaTdN4e4JhdwUwwElBwGSIeLJPnfYtzVQngN9RfAb6fFIaWiJletN6gQ4uVgDxwtvTMI4luK8fymQeCQeGzR86lEuFzaGbQHb2XfAUSiNaQV5fRbO315ulYlyhMw+m30vEm0MdSkU6jHp2AikQvYfswJ7/D+OLJdotCPh6yxUajW/BPRs2rCK1GXhdHZ9KblsWCVaX/PdXaw5OFWpIaSr0VlJ31/YtARnXmzqtRNeDjspyAuyC+Th/Q02+gQrVD4AACjsIzsDupHejQYGT9FuVxMfuW76iUOIrY1RmLfh0yHS1H/zK12CJc/0KmHbwYnXOo/oyLkuvzV/TytluvMbhe1NB9syfdNvRMOuP8JOcWePaDd1rXluED2cUzFT/FOlEdLSv3BxGyo/tBtnFsY/HtjXbjbeD09WVbpps9oDxcFns3Pe4; ssguid=317145499413540020222000003; 5b5a8868cb3cb2da80cdab9359fc0332=403179ee86b4d89dee5247564f8d1652; cto_bundle=fO2Yu19NZ3d3TDNmOGpvMyUyQiUyQnRqTGJieHZpMW5pd1Y2ejN6TlBxRFlWUkhqRmFWaDNrc2dybjJrYTBQQTVsSHZ2ZXczZ2ZFelBsM3AxUDJSV2JVVUhuM3clMkJIaWdJc3dBRTZmTkl2STAzcFd5QkVmN3QlMkJGbWRwZlFCZGo3ZXBTbXVKaW1Tc21XUmMzUEJkNTlWUWR2NmxOS0RCRkVtTE9GbXFmTmhDNHYzdWszTE9WcVhyZ1duU3FkbnFwakQ5eDJiVmVud1dqSkhyNlNmOFdzamxxOEF4QWIzZ0ElM0QlM0Q; _ga_1BYVQK09SB=GS1.1.1714549914.2.1.1714550964.3.0.0',
            'Referer': 'https://www.gmarket.co.kr/n/search?keyword=%EC%8A%A4%EC%B9%B4%EC%9D%B4%ED%82%A5',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        try:
            response = requests.get(
                'https://www.gmarket.co.kr/n/search?keyword={}&k=1&p={}'.format(keyword,pageCount),
                cookies=cookies,
                headers=headers,
            )
        except:
            print("페이지없음")
            break
        if response.text.find("검색 결과가 없습니다")>=0:
            print("검색 결과 없어서 다른거 추천됨")
            break
        soup = BeautifulSoup(response.text, 'lxml')
        # print(soup.prettify())
        # itemGroup = soup.find("ul", attrs={'class': 'goods_product_list'})
        items = soup.find_all('div', attrs={'class': 'box__component box__component-itemcard box__component-itemcard--general'})
        if len(items) == 0:
            print("상품없음2")
            break

        checkList = []
        for index, item in enumerate(items):

            try:
                url = item.find("a",attrs={'class':'link__item'})['href']
            except:
                print("상품없음")
                continue
            print("url:", url, "/ url_TYPE:", type(url))
            title = item.find("span", attrs={'class': 'text__item'}).get_text().strip()
            print("title:", title, "/ title_TYPE:", type(title))
            price = item.find('strong', attrs={'class': 'text text__value'}).get_text().replace(",", "").replace("원", "")
            regex = re.compile("\d+")
            price = int(regex.findall(price)[-1])
            print("price:", price, "/ price_TYPE:", type(price))
            checkList.append(title)
            if float(priceRatio) * supabaseData['priceLow'] < price < supabaseData['priceLow']:
                data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '지마켓', 'url': url, 'salesInfo': "",
                        'inputKeyword': supabaseData['name']}
                print("data:", data, "/ data_TYPE:", type(data))
                dataList.append(data)
        # print("checkList:",checkList,"/ checkList_TYPE:",type(checkList))
        # print("prevCheckList:",prevCheckList,"/ prevCheckList_TYPE:",type(prevCheckList))
        if len(checkList) == 0 or ",".join(checkList)==",".join(prevCheckList):
            print("상품없음3")
            break
        prevCheckList=checkList.copy()
        pageCount += 1
        time.sleep(random.randint(10, 20) * 0.1)
        print("======================")
    return dataList
def GetSearchAuction(supabaseData,priceRatio):
    keyword = supabaseData['name']
    pageCount = 1
    dataList = []
    prevCheckList = ['11']
    while True:
        print("옥션★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            # 'cguid': '11714664268670009321000000',
            # '_ga': 'GA1.1.1696239146.1714664271',
            # 'pcid': '1714664276133',
            # 'pguid': '21714664275373003961010000',
            # 'APAC': 'kid=&acdt=240503&lgdt=&tmcnt=1&lmcnt=0&lpdt1=240503&lpdt2=240502',
            # '_fbp': 'fb.2.1714664292986.1281782545',
            # 'sguid': '31714703896103007071200000',
            # 'cto_bundle': 'SPkpJ19HY3hvSHh6eDJHdzAlMkJYJTJGV3lUWTgxRTBFaHRtejdCYTNBWDdwMGtEQ2xmaDE1Ym0xMFhhMyUyRjlXa0lTb3lkSnFnRFdLWGZNdDdrUkUlMkZod2lUJTJCSFR3cnU2TVIxRlF6bklNQ0JmM3RWVlIzUWNVajZPVUMxJTJCT1YzYkxlbUk0VEZZY2twb0pSanl3MVg4VmRiVGtmTiUyRmtqa3BnUU93Umd4ZW9JQVRrSUFqRiUyRjd0NTV6enJnVzFTN3FuRUdudVFHT202bkZaSHlYcEx5MHVjOGR1ajY2dHQ4QSUzRCUzRA',
            # 'ssguid': '317147079218930018312000005',
            # '_ga_ZZV2J6NHR2': 'GS1.1.1714707914.3.1.1714707944.30.0.0',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'cguid=11714664268670009321000000; _ga=GA1.1.1696239146.1714664271; pcid=1714664276133; pguid=21714664275373003961010000; APAC=kid=&acdt=240503&lgdt=&tmcnt=1&lmcnt=0&lpdt1=240503&lpdt2=240502; _fbp=fb.2.1714664292986.1281782545; sguid=31714703896103007071200000; cto_bundle=SPkpJ19HY3hvSHh6eDJHdzAlMkJYJTJGV3lUWTgxRTBFaHRtejdCYTNBWDdwMGtEQ2xmaDE1Ym0xMFhhMyUyRjlXa0lTb3lkSnFnRFdLWGZNdDdrUkUlMkZod2lUJTJCSFR3cnU2TVIxRlF6bklNQ0JmM3RWVlIzUWNVajZPVUMxJTJCT1YzYkxlbUk0VEZZY2twb0pSanl3MVg4VmRiVGtmTiUyRmtqa3BnUU93Umd4ZW9JQVRrSUFqRiUyRjd0NTV6enJnVzFTN3FuRUdudVFHT202bkZaSHlYcEx5MHVjOGR1ajY2dHQ4QSUzRCUzRA; ssguid=317147079218930018312000005; _ga_ZZV2J6NHR2=GS1.1.1714707914.3.1.1714707944.30.0.0',
            'Referer': 'https://browse.auction.co.kr/search?keyword=%EC%8A%A4%EC%B9%B4%EC%9D%B4+%EC%BD%A9%EC%BD%A9&itemno=&nickname=&encKeyword=%25EC%258A%25A4%25EC%25B9%25B4%25EC%259D%25B4%2520%25EC%25BD%25A9%25EC%25BD%25A9&arraycategory=&frm=&dom=auction&isSuggestion=No&retry=',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        try:
            response = requests.get(
                'https://browse.auction.co.kr/search?keyword={}&itemno=&nickname=&arraycategory=&frm=&dom=auction&isSuggestion=No&retry=&k=34&p={}'.format(keyword,pageCount),
                cookies=cookies,
                headers=headers,
            )
        except:
            print("페이지없음")
            break

        soup = BeautifulSoup(response.text, 'lxml')
        # print(soup.prettify())
        # itemGroup = soup.find("ul", attrs={'class': 'goods_product_list'})
        items = soup.find_all('div',attrs={'class':'component component--item_card type--general'})
        if len(items) == 0:
            print("상품없음2")
            break

        checkList = []
        for index, item in enumerate(items):
            try:
                url = item.find('div',attrs={'class':'section--itemcard_info'}).find("a",attrs={'target':'_blank'})['href']
            except:
                print("상품없음")
                continue
            print("url:", url, "/ url_TYPE:", type(url))
            title = item.find("span", attrs={'class': 'text--title'}).get_text().strip()
            print("title:", title, "/ title_TYPE:", type(title))
            try:
                price = item.find('strong', attrs={'class': 'text__price-seller'}).get_text().replace(",", "").replace(
                    "원", "")
            except:
                try:
                    price = item.find('strong', attrs={'class': 'text--price_seller'}).get_text().replace(",","").replace("원", "")
                except:
                    price='9999999999'
            checkList.append(title)
            regex = re.compile("\d+")
            price = int(regex.findall(price)[-1])
            print("price:", price, "/ price_TYPE:", type(price))
            checkList.append(title)
            if float(priceRatio) * supabaseData['priceLow'] < price < supabaseData['priceLow']:
                data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '옥션', 'url': url, 'salesInfo': "",
                        'inputKeyword': supabaseData['name']}
                print("data:", data, "/ data_TYPE:", type(data))
                dataList.append(data)
        if len(checkList) == 0 or ",".join(checkList)==",".join(prevCheckList):
            print("상품없음3")
            break
        prevCheckList=checkList.copy()
        pageCount += 1
        time.sleep(random.randint(20, 30) * 0.1)
        print("======================")
    return dataList
def GetSearchInterpark(supabaseData,priceRatio):
    keyword = supabaseData['name']
    pageCount = 1
    dataList = []
    prevCheckList = ['11']
    while True:
        print("인터파크★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            'pcid': '171454737392763070',
            '_ga_E2Q3PB7X43': 'GS1.1.1714547374.1.0.1714547374.0.0.0',
            '_trs_id': 'eY2770350%3F525770',
            'OAX': '3mozz2Y6DScAAV8Q',
            'WMONID': 'PwMufH8p9DU',
            '_trs_sid': 'G%5B646041436450%5Bg%5B0552172%3D707552',
            '_trs_flow': '',
            '_gid': 'GA1.2.660166378.1715080489',
            '_gat_UA-93889457-1': '1',
            '_ga': 'GA1.2.1435135503.1714547375',
            'ab.storage.deviceId.5def1864-09a6-498b-812e-c060d6dd41a7': '%7B%22g%22%3A%2216002e26-672c-209e-18b1-c0d3b412c797%22%2C%22c%22%3A1715080497447%2C%22l%22%3A1715080497447%7D',
            'ab.storage.sessionId.5def1864-09a6-498b-812e-c060d6dd41a7': '%7B%22g%22%3A%22223b1f47-99ec-41d5-3b36-89013e46ad39%22%2C%22e%22%3A1715082302642%2C%22c%22%3A1715080497446%2C%22l%22%3A1715080502642%7D',
            '_ga_4SKTL7E8Q8': 'GS1.1.1715080489.1.1.1715080508.41.0.0',
            'q_smsCertYN': 'N',
            '_SHOP_PC_ID': '20240507201508259723635',
            '_gat_UA-250333866-1': '1',
            '_fbp': 'fb.1.1715080509363.1790636552',
            'appier_utmz': '%7B%7D',
            '_atrk_siteuid': 'l9HxwyMc8kcmoMta',
            '_atrk_ssid': 'Nr4dOTGsvIdiMrMF4H9DWc',
            'appier_pv_counteref9110b85e056ec': '0',
            'appier_page_isView_ef9110b85e056ec': '4106d2d71a8c7f30bdc21904782e077646d1d5cb465918fb151a5d89af9314a9',
            'appier_pv_counter54ffdf3b09506ec': '0',
            'appier_page_isView_54ffdf3b09506ec': '4106d2d71a8c7f30bdc21904782e077646d1d5cb465918fb151a5d89af9314a9',
            '_atrk_sessidx': '2',
            'JSESSIONID': 'D4FDFC59F2D63A313C52E6E76D8BA79E.node1',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'pcid=171454737392763070; _ga_E2Q3PB7X43=GS1.1.1714547374.1.0.1714547374.0.0.0; _trs_id=eY2770350%3F525770; OAX=3mozz2Y6DScAAV8Q; WMONID=PwMufH8p9DU; _trs_sid=G%5B646041436450%5Bg%5B0552172%3D707552; _trs_flow=; _gid=GA1.2.660166378.1715080489; _gat_UA-93889457-1=1; _ga=GA1.2.1435135503.1714547375; ab.storage.deviceId.5def1864-09a6-498b-812e-c060d6dd41a7=%7B%22g%22%3A%2216002e26-672c-209e-18b1-c0d3b412c797%22%2C%22c%22%3A1715080497447%2C%22l%22%3A1715080497447%7D; ab.storage.sessionId.5def1864-09a6-498b-812e-c060d6dd41a7=%7B%22g%22%3A%22223b1f47-99ec-41d5-3b36-89013e46ad39%22%2C%22e%22%3A1715082302642%2C%22c%22%3A1715080497446%2C%22l%22%3A1715080502642%7D; _ga_4SKTL7E8Q8=GS1.1.1715080489.1.1.1715080508.41.0.0; q_smsCertYN=N; _SHOP_PC_ID=20240507201508259723635; _gat_UA-250333866-1=1; _fbp=fb.1.1715080509363.1790636552; appier_utmz=%7B%7D; _atrk_siteuid=l9HxwyMc8kcmoMta; _atrk_ssid=Nr4dOTGsvIdiMrMF4H9DWc; appier_pv_counteref9110b85e056ec=0; appier_page_isView_ef9110b85e056ec=4106d2d71a8c7f30bdc21904782e077646d1d5cb465918fb151a5d89af9314a9; appier_pv_counter54ffdf3b09506ec=0; appier_page_isView_54ffdf3b09506ec=4106d2d71a8c7f30bdc21904782e077646d1d5cb465918fb151a5d89af9314a9; _atrk_sessidx=2; JSESSIONID=D4FDFC59F2D63A313C52E6E76D8BA79E.node1',
            'Referer': 'https://m.shop.interpark.com/',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
        }

        params = {
            'keyword': keyword,
            'page': pageCount,
            'rows': '20',
            'sort': 'recommend',
            'brand': '',
            'minPrice': '0',
            'maxPrice': '999999999',
            'deliveryYn': '',
            'todayDelvYn': '',
            'cardDiscountYn': '',
            'ssdealYn': '',
            'abroadBsYn': '',
            'inweekYn': '',
            'reqType': 'shopMobile',
            'nc1': '',
            'os': 'Android',
            # 'callback': '__jp14',
            # '_': '1715080528904',
        }


        try:
            response = requests.get(
                'https://shopapi.interpark.com/niSearch/shopMobile/listPrdChoiceAndNormal.json',
                params=params,
                cookies=cookies,
                headers=headers,
            )
        except:
            print("페이지없음")
            break

        items = json.loads(response.text)['data']['listChoiceAndNormal']
        if len(items) == 0:
            print("상품없음2")
            break

        checkList = []
        for index, item in enumerate(items):
            try:
                url = "https://m.shop.interpark.com/product/{}/0000100000?pay_disp_no=".format(item['prdNo'])
            except:
                print("상품없음")
                continue
            print("url:", url, "/ url_TYPE:", type(url))
            title = item.get('name',"")
            print("title:", title, "/ title_TYPE:", type(title))
            try:
                price = int(item.get('final_sell_price',""))
            except:
                price=9999999999
            checkList.append(title)
            if float(priceRatio) * supabaseData['priceLow'] < price < supabaseData['priceLow']:
                sellerName,ceoName,phoneNumber,addr=GetDetailsInterpark(item['prdNo'])
                data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '인터파크', 'url': url, 'salesInfo': sellerName+","+ceoName+","+phoneNumber+","+addr,
                        'inputKeyword': supabaseData['name']}
                print("data:", data, "/ data_TYPE:", type(data))
                dataList.append(data)
                time.sleep(1)
        if len(checkList) == 0 or ",".join(checkList) == ",".join(prevCheckList):
            print("상품없음3")
            break
        prevCheckList = checkList.copy()
        pageCount += 1
        time.sleep(random.randint(20, 30) * 0.1)
        print("======================")
    return dataList
def GetSearchWemakeprice(supabaseData,priceRatio):
    keyword = supabaseData['name']
    pageCount = 1
    dataList = []
    prevCheckList = ['11']
    while True:
        print("위메프★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            # 'wmp-auk': '06a0b63f-4a46-4831-a8aa-3026-d8ebb6c7f746',
            # 'wmp_pcstamp': '1715083500709014015',
            # 'WemepAffiliate': '%7B%22channelId%22%3A1000057%2C%22expirationDate%22%3A%222024-05-08T21%3A05%3A00.185%22%7D',
            # 'rp': 'http%3A%2F%2Ffront.wemakeprice.com%2Fmain%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3Dnull%26utm_term%3D%25EC%259C%2584%25EB%25A9%2594%25ED%2594%2584%26utm_content%3Dwemake%26gad_source%3D1%26gclid%3DCjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE',
            # 'WemepEdgeUtmTerm': '%EC%9C%84%EB%A9%94%ED%94%84',
            # '_fbp': 'fb.1.1715083500855.841822278',
            # '__utma': '122159757.901157887.1715083501.1715083501.1715083501.1',
            # '__utmc': '122159757',
            # '__utmz': '122159757.1715083501.1.1.utmcsr=google|utmgclid=CjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE|utmccn=null|utmcmd=cpc|utmctr=ìœ„ë©”í”„|utmcct=wemake',
            # '__utmt': '1',
            # '_gid': 'GA1.2.1895161050.1715083502',
            # '_gac_UA-18774526-1': '1.1715083502.CjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE',
            # '_gat_UA-18774526-1': '1',
            # 'wmp_mweb_cinfo': 'WMW%09mm%09m%09%5B%5D%090%2C0%090%7C0%7C0%7C',
            # 'wmp_basic_info': 'a%3A2%3A%7Bs%3A12%3A%22cart_session%22%3Bs%3A32%3A%22f9d73add353d39776abd1815cf5f9d07%22%3Bs%3A11%3A%22IsNotWmpApp%22%3Bs%3A1%3A%221%22%3B%7D',
            # '__utmb': '122159757.4.10.1715083501',
            # 'wlogFunnel': 'WMP-MWEB-001-0-V',
            # '_ga_C3QBWSBLPT': 'GS1.1.1715083501.1.1.1715083525.36.0.0',
            # '_ga': 'GA1.2.518513905.1715083502',
            # '_ga_0CD35LTKXG': 'GS1.2.1715083502.1.1.1715083525.37.0.0',
            # 'SCOUTER': 'z1rb0klr38bdtt',
        }

        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'wmp-auk=06a0b63f-4a46-4831-a8aa-3026-d8ebb6c7f746; wmp_pcstamp=1715083500709014015; WemepAffiliate=%7B%22channelId%22%3A1000057%2C%22expirationDate%22%3A%222024-05-08T21%3A05%3A00.185%22%7D; rp=http%3A%2F%2Ffront.wemakeprice.com%2Fmain%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3Dnull%26utm_term%3D%25EC%259C%2584%25EB%25A9%2594%25ED%2594%2584%26utm_content%3Dwemake%26gad_source%3D1%26gclid%3DCjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE; WemepEdgeUtmTerm=%EC%9C%84%EB%A9%94%ED%94%84; _fbp=fb.1.1715083500855.841822278; __utma=122159757.901157887.1715083501.1715083501.1715083501.1; __utmc=122159757; __utmz=122159757.1715083501.1.1.utmcsr=google|utmgclid=CjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE|utmccn=null|utmcmd=cpc|utmctr=ìœ„ë©”í”„|utmcct=wemake; __utmt=1; _gid=GA1.2.1895161050.1715083502; _gac_UA-18774526-1=1.1715083502.CjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE; _gat_UA-18774526-1=1; wmp_mweb_cinfo=WMW%09mm%09m%09%5B%5D%090%2C0%090%7C0%7C0%7C; wmp_basic_info=a%3A2%3A%7Bs%3A12%3A%22cart_session%22%3Bs%3A32%3A%22f9d73add353d39776abd1815cf5f9d07%22%3Bs%3A11%3A%22IsNotWmpApp%22%3Bs%3A1%3A%221%22%3B%7D; __utmb=122159757.4.10.1715083501; wlogFunnel=WMP-MWEB-001-0-V; _ga_C3QBWSBLPT=GS1.1.1715083501.1.1.1715083525.36.0.0; _ga=GA1.2.518513905.1715083502; _ga_0CD35LTKXG=GS1.2.1715083502.1.1.1715083525.37.0.0; SCOUTER=z1rb0klr38bdtt',
            'Origin': 'https://mw.wd.wemakeprice.com',
            'Referer': 'https://mw.wd.wemakeprice.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'x-session-id': '3b1e1856c28445cfa785c0f29683b094',
        }

        params = {
            # '_service': '5',
            # 'isRec': '1',
            'keyword': keyword,
            'os': 'mweb',
            'page': pageCount,
            'perPage': '20',
            'tab': 'main',
        }




        try:
            response = requests.get(
                'https://mw.wemakeprice.com/api/wmpsearch/api/aggregate/wmp-search/search.json',
                params=params,
                cookies=cookies,
                headers=headers,
            )
        except:
            print("페이지없음")
            break

        items = json.loads(response.text)['data']['deals']
        if len(items) == 0:
            print("상품없음2")
            break

        checkList = []
        for index, item in enumerate(items):
            try:
                url = "https://mw.wemakeprice.com/product/{}".format(item['link']['value'])
            except:
                print("상품없음")
                continue
            print("url:", url, "/ url_TYPE:", type(url))
            title = item.get('dispNm',"")
            print("title:", title, "/ title_TYPE:", type(title))
            try:
                price = int(item.get('discountPrice',""))
            except:
                price=9999999999
            checkList.append(title)
            if float(priceRatio) * supabaseData['priceLow'] < price < supabaseData['priceLow']:
                partnerNm, partnerOwner, infoCenter, partnerOwnerEmail, addr=GetDetailsWemakeprice(item['link']['value'])
                data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '위메프', 'url': url, 'salesInfo': partnerNm+","+partnerOwner+","+infoCenter+","+partnerOwnerEmail+","+addr,
                        'inputKeyword': supabaseData['name']}
                print("data:", data, "/ data_TYPE:", type(data))
                dataList.append(data)
                time.sleep(1)
        if len(checkList) == 0 or ",".join(checkList) == ",".join(prevCheckList):
            print("상품없음3")
            break
        prevCheckList = checkList.copy()
        pageCount += 1
        time.sleep(random.randint(20, 30) * 0.1)
        print("======================")
    return dataList
def GetSearchSSG(supabaseData,priceRatio):
    keyword = supabaseData['name']
    pageCount = 1
    dataList = []
    prevCheckList = ['11']
    while True:
        print("신세계★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            'PCID': '17139199268943125027912',
            'ab.storage.userId.4a23e2c2-9255-4dd0-97c0-64c0e4036eb5': '%7B%22g%22%3A%2217139199268943125027912%22%2C%22c%22%3A1713919927246%2C%22l%22%3A1713919927248%7D',
            'ab.storage.deviceId.4a23e2c2-9255-4dd0-97c0-64c0e4036eb5': '%7B%22g%22%3A%2241b36c0a-e87e-6853-46d4-55de13d41f7a%22%2C%22c%22%3A1713919927249%2C%22l%22%3A1713919927249%7D',
            'RC_RESOLUTION': '1920*1080',
            'RC_COLOR': '24',
            '_gcl_au': '1.1.1445904301.1713919927',
            '_fbp': 'fb.1.1713919927430.518883918',
            'mbr_test_type': 'A',
            'emf.723.euuid.v5': 'e4b5e673-mc4c-4cca-s4ef-3ac07dc676cd',
            'tk_id': 'd0df54d2-fc64-4b80-b056-9d58bac38993',
            'a1_gid': '3mozz2YoV7cAB1G6',
            '_ga': 'GA1.1.743789127.1713919928',
            'au_ip': '222.106.51.207.91412',
            'au_id': 'e81928fc096e70cda416e918f0b02d2f542b5',
            'uni_merge': '1',
            'analytics_sp': 'N',
            'target_sp': 'N',
            'prevBinding': '218B7A02CFD464A304F052718ACAA8748FEA30D3C6D367EDBF634135468B4C10',
            '_wp_uid': '1-3d209e007e89826e73becd6ed9193ded-s1714697573.191811|windows_10|chrome-3c7qfc',
            '_atrk_siteuid': 'UWZDOJHVhcuSnZGh',
            'emf.32.euuid.v5': 'e59aa13b-m447-49b0-s762-18ad8c36afc2',
            'CHECKED': 'b2bc6bfa0dd611efb3e30050568ceda46921434772645259',
            'ab.storage.sessionId.4a23e2c2-9255-4dd0-97c0-64c0e4036eb5': '%7B%22g%22%3A%22f711c5bc-4f12-8c26-3d13-eb0a3741b48a%22%2C%22e%22%3A1715241932012%2C%22c%22%3A1715240132013%2C%22l%22%3A1715240132013%7D',
            'PT': 'FST_PURCH_TGT_YN%3DN%26MOLLYS_SALESTR_NO%3D2449%26SHPP_LOC_SEQ%3D5878678%26EM_DUAL_SALE_STR_NO%3D0000%26EM_HOLY_SHPP_SALESTR_NO%3D2449%26TR_CLST_SALE_STR_NO%3D2570%26EM_CLST_SALE_STR_NO%3D2569%26CART_NM%3D%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%26EM_SALE_STR_NM%3D%EB%B4%89%EC%84%A0%EC%A0%90%26EM_PICKU_STR_YN%3DN%26EM_SALE_STR_CENTER_YN%3DN%26GM_SALE_STR_NO%3D0000%26GM_SALE_STR_NM%3D-%26EM_SALE_STR_NO%3D2137%26TR_SALE_STR_NM%3DTRADERS+%EC%9B%94%EA%B3%84%EC%A0%90%26SHPPLOC_MOD_KEY%3D5878678%26TR_SALE_STR_NO%3D2491%26TR_RSVT_SHPP_PSBL_YN%3DN%26SHPPLOC_MOD_NM%3DMY%EB%B0%B0%EC%86%A1%EC%A7%80%26TR_HOLY_SHPP_SALESTR_NO%3D2491%26SHIP_ZIP_CD%3D61455%26GM_SALE_STR_YN%3DN%26SHPPLOC_MOD%3DMY%26EM_RSVT_SHPP_PSBL_YN%3DY',
            'FSID': 'sdfak3662y1f5rn6vg03',
            'where': 'SE%3DY%26CHNL_ID%3D0000015208%26CK_WHERE%3Ddirect_ssg%26et%3D1715601459071',
            'CKWHERE': 'direct_ssg',
            'TS01e49c73': '010874cb80abec6c7e4c635b11f05d41adb7564b6413ad2cd9f3c421c3d44cad28a3edf8a1d677e406433582cd298e4d4246adfaea',
            'TS0197eadc': '010874cb80abec6c7e4c635b11f05d41adb7564b6413ad2cd9f3c421c3d44cad28a3edf8a1d677e406433582cd298e4d4246adfaea',
            'SSGDOMAIN': 'www',
            'CSTALK_POPUP_OPEN': 'null',
            'a1_sgid': '3mozz2YoV7cAB1G61715601466891',
            'cto_bundle': 'bnuZaF8zVnNHNVAlMkZSSFUxRlFES3VOTU1RbTFXUFdaek5acktycWlvSCUyRk96Qjg4RTB5NTh2YTVpbEVpYnJ3enlFd3NLWGUlMkI2Q2ZwbGcydDZKMW13a2JGMXEyajg3JTJCUG1MQmpTMjR6Z2lFZVAzdW9SYk5UNExCVklSd0hlNEklMkJuNjk3MnIxSGYyT0EzZFhRd0ROdHJjSUdjZlFoVUV1OUV3V0pDZ2twOFphT0N0SyUyQjhPd2tOZHc0VlVwNmRXcjhIejlnNUNoQmZOV05FRiUyRkN6d0s0eG8xZmlxUlU0Z1VTeDRRRWpMUmNxT1NhNTIlMkZIYjU3VmVRRzNYUGhTMXl6bmRYeWJCdGpYcWZLc01JM1RFMHNCclJCNVBLTiUyRnBJOFY1RDEwbTVCM2k3VzRXdm05Y2pRZkY4czdTYVRHUWFSWDlZZzB3Zg',
            'JSESSIONID': 'E259E4554F9FD4185AAEB92EC9037CA5.ssgmall6202',
            'FSID1': 'sdfamtn6vg05m084r5b1',
            '_ga_E0P8DK53C8': 'GS1.1.1715601467.25.1.1715601568.27.0.0',
            '_dd_s': 'rum=0&expire=1715602489762',
        }

        headers = {
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'PCID=17139199268943125027912; ab.storage.userId.4a23e2c2-9255-4dd0-97c0-64c0e4036eb5=%7B%22g%22%3A%2217139199268943125027912%22%2C%22c%22%3A1713919927246%2C%22l%22%3A1713919927248%7D; ab.storage.deviceId.4a23e2c2-9255-4dd0-97c0-64c0e4036eb5=%7B%22g%22%3A%2241b36c0a-e87e-6853-46d4-55de13d41f7a%22%2C%22c%22%3A1713919927249%2C%22l%22%3A1713919927249%7D; RC_RESOLUTION=1920*1080; RC_COLOR=24; _gcl_au=1.1.1445904301.1713919927; _fbp=fb.1.1713919927430.518883918; mbr_test_type=A; emf.723.euuid.v5=e4b5e673-mc4c-4cca-s4ef-3ac07dc676cd; tk_id=d0df54d2-fc64-4b80-b056-9d58bac38993; a1_gid=3mozz2YoV7cAB1G6; _ga=GA1.1.743789127.1713919928; au_ip=222.106.51.207.91412; au_id=e81928fc096e70cda416e918f0b02d2f542b5; uni_merge=1; analytics_sp=N; target_sp=N; prevBinding=218B7A02CFD464A304F052718ACAA8748FEA30D3C6D367EDBF634135468B4C10; _wp_uid=1-3d209e007e89826e73becd6ed9193ded-s1714697573.191811|windows_10|chrome-3c7qfc; _atrk_siteuid=UWZDOJHVhcuSnZGh; emf.32.euuid.v5=e59aa13b-m447-49b0-s762-18ad8c36afc2; CHECKED=b2bc6bfa0dd611efb3e30050568ceda46921434772645259; ab.storage.sessionId.4a23e2c2-9255-4dd0-97c0-64c0e4036eb5=%7B%22g%22%3A%22f711c5bc-4f12-8c26-3d13-eb0a3741b48a%22%2C%22e%22%3A1715241932012%2C%22c%22%3A1715240132013%2C%22l%22%3A1715240132013%7D; PT=FST_PURCH_TGT_YN%3DN%26MOLLYS_SALESTR_NO%3D2449%26SHPP_LOC_SEQ%3D5878678%26EM_DUAL_SALE_STR_NO%3D0000%26EM_HOLY_SHPP_SALESTR_NO%3D2449%26TR_CLST_SALE_STR_NO%3D2570%26EM_CLST_SALE_STR_NO%3D2569%26CART_NM%3D%EC%9E%A5%EB%B0%94%EA%B5%AC%EB%8B%88%26EM_SALE_STR_NM%3D%EB%B4%89%EC%84%A0%EC%A0%90%26EM_PICKU_STR_YN%3DN%26EM_SALE_STR_CENTER_YN%3DN%26GM_SALE_STR_NO%3D0000%26GM_SALE_STR_NM%3D-%26EM_SALE_STR_NO%3D2137%26TR_SALE_STR_NM%3DTRADERS+%EC%9B%94%EA%B3%84%EC%A0%90%26SHPPLOC_MOD_KEY%3D5878678%26TR_SALE_STR_NO%3D2491%26TR_RSVT_SHPP_PSBL_YN%3DN%26SHPPLOC_MOD_NM%3DMY%EB%B0%B0%EC%86%A1%EC%A7%80%26TR_HOLY_SHPP_SALESTR_NO%3D2491%26SHIP_ZIP_CD%3D61455%26GM_SALE_STR_YN%3DN%26SHPPLOC_MOD%3DMY%26EM_RSVT_SHPP_PSBL_YN%3DY; FSID=sdfak3662y1f5rn6vg03; where=SE%3DY%26CHNL_ID%3D0000015208%26CK_WHERE%3Ddirect_ssg%26et%3D1715601459071; CKWHERE=direct_ssg; TS01e49c73=010874cb80abec6c7e4c635b11f05d41adb7564b6413ad2cd9f3c421c3d44cad28a3edf8a1d677e406433582cd298e4d4246adfaea; TS0197eadc=010874cb80abec6c7e4c635b11f05d41adb7564b6413ad2cd9f3c421c3d44cad28a3edf8a1d677e406433582cd298e4d4246adfaea; SSGDOMAIN=www; CSTALK_POPUP_OPEN=null; a1_sgid=3mozz2YoV7cAB1G61715601466891; cto_bundle=bnuZaF8zVnNHNVAlMkZSSFUxRlFES3VOTU1RbTFXUFdaek5acktycWlvSCUyRk96Qjg4RTB5NTh2YTVpbEVpYnJ3enlFd3NLWGUlMkI2Q2ZwbGcydDZKMW13a2JGMXEyajg3JTJCUG1MQmpTMjR6Z2lFZVAzdW9SYk5UNExCVklSd0hlNEklMkJuNjk3MnIxSGYyT0EzZFhRd0ROdHJjSUdjZlFoVUV1OUV3V0pDZ2twOFphT0N0SyUyQjhPd2tOZHc0VlVwNmRXcjhIejlnNUNoQmZOV05FRiUyRkN6d0s0eG8xZmlxUlU0Z1VTeDRRRWpMUmNxT1NhNTIlMkZIYjU3VmVRRzNYUGhTMXl6bmRYeWJCdGpYcWZLc01JM1RFMHNCclJCNVBLTiUyRnBJOFY1RDEwbTVCM2k3VzRXdm05Y2pRZkY4czdTYVRHUWFSWDlZZzB3Zg; JSESSIONID=E259E4554F9FD4185AAEB92EC9037CA5.ssgmall6202; FSID1=sdfamtn6vg05m084r5b1; _ga_E0P8DK53C8=GS1.1.1715601467.25.1.1715601568.27.0.0; _dd_s=rum=0&expire=1715602489762',
            'Referer': 'https://www.ssg.com/search.ssg?target=all&query=%EC%BD%94%EB%94%A9%20%EB%A1%9C%EB%B4%87&page=2',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'target': 'item',
            'query': keyword,
            'page': pageCount,
            'count': '100',

            # '_': '1715601556955',
        }


        try:
            response = requests.get('https://www.ssg.com/search/jsonSearch.ssg', params=params, cookies=cookies,
                                    headers=headers)
        except:
            print("페이지없음")
            break

        soup = BeautifulSoup(response.text, 'lxml')

        table = soup.find("ul", attrs={'id': 'idProductImg'})
        isItem=len(soup.find_all("ul", attrs={'id': 'idProductImg'}))
        if isItem==0:
            print("상품없음")
            break
        items = table.find_all('li')


        if len(items) == 0:
            print("상품없음2")
            break

        checkList = []
        for index, item in enumerate(items):
            try:
                url = 'https://www.ssg.com'+item.find("a",attrs={'class':'clickable'})['href']
            except:
                print("상품없음")
                continue
            print("url:", url, "/ url_TYPE:", type(url))
            title = item.find('em',attrs={'class':'tx_ko'}).get_text()
            print("title:", title, "/ title_TYPE:", type(title))
            try:
                price = int(item.find('em',attrs={'class':'ssg_price'}).get_text().replace(",","").replace("원",""))
            except:
                price=9999999999
            print("price:",price,"/ price_TYPE:",type(price))
            checkList.append(title)
            if float(priceRatio) * supabaseData['priceLow'] < price < supabaseData['priceLow']:
                data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': 'SSG', 'url': url, 'salesInfo': "",
                        'inputKeyword': supabaseData['name']}
                print("data:", data, "/ data_TYPE:", type(data))
                dataList.append(data)
                time.sleep(1)
        if len(checkList) == 0 or ",".join(checkList) == ",".join(prevCheckList):
            print("상품없음3")
            break
        prevCheckList = checkList.copy()
        pageCount += 1
        time.sleep(random.randint(20, 30) * 0.1)
        print("======================")
    return dataList
def GetSearchCoupang(supabaseData,priceRatio):
    keyword = supabaseData['name']
    pageCount = 1
    dataList = []
    prevCheckList = ['11']
    while True:
        print("쿠팡★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        # cookies = {
        #     'PCID': '16062593661524224436363',
        #     'x-coupang-accept-language': 'ko-KR',
        #     'x-coupang-target-market': 'KR',
        #     '_fbp': 'fb.1.1713884027605.708116537',
        #     'sc_vid': 'A00888095',
        #     'sc_lid': 'fuzzily',
        #     'sc_uid': 'KvKg6pnd13CrWErdKstYJ35NvCUsTqEyzRooDbFfaO7ibQEIFGwlZadlrrBfvg==',
        #     'sid': '9986eba6b55b4da3b6b858a9fa4d87bb32be3b5e',
        #     'gd1': 'Y',
        #     'trac_src': '0',
        #     'trac_spec': '0',
        #     'trac_addtag': '0',
        #     'trac_ctag': '""',
        #     'trac_lptag': '""',
        #     'trac_itime': '""',
        #     'trac_sid': '""',
        #     'trac_appver': '""',
        #     'APPVER': '',
        #     '_gcl_au': '1.1.852457399.1715578916',
        #     'lastCheckoutId': '1715591726276',
        #     'overrideAbTestGroup': '%5B%5D',
        #     'MARKETID': '16062593661524224436363',
        #     'bm_sz': '5106C4984D7A69B5A2F911E6E39F6E99~YAAQrXpGaCgHdGOPAQAAuwQFchf+swtbgiiHT5M9XQHUymY3xaPNG3yRKGMDjQOypqPYHZr5yqifYkUDFLdvQFOI2joE/d4bzzTiwhf1ulMMBkWSNGFxdrgq8Ng10u0GTgCP5BA1dvlFqT1vvp1XAqP9vVawp8YoouOjEMM4x2OLCqqaQ1n7LXnj5igNxE9DkojZ67tabJ4ya514Ce3JZTdwd6Mvj9SaHj9tJKbQvyDSeEBpspv3QKwdcPAYqcsivf++QYejxhWsbMduNI2T+rerMuLMkYre/DS2rZqA2SY4fIy/sdcmnecvd4fvNEfHSmBIpf0pQNmKMmJjgRZXFGrUMAkxgygw1NTm4sAZ905doAA6Q2OPPfO6q/sPPgGHB97WWSNI4t0xJdvy3zH5bvM0Jse2mPgX1tQEiXiLDWKESGJVwV+WizGZqVRvFkd6bRDj/HtPaCcLfSXz/OrFJ4aBbsN/OEV3M/ioE9eY9w8kwYpGYU8y3+vU8alNicphLnl0vmjX~3229241~3289400',
        #     # 'ak_bmsc': '0F4E18EA63C84884AC1EDE17D16B17B9~000000000000000000000000000000~YAAQrXpGaMMHdGOPAQAABwgFchfWLq3d8UbvvjA+UoUP0sCPAXww6jDLARM0gSxDwl6aE+uREQ/HVa1BqhjcwSzo48/SzJXtLCr/RrbraYB1XdaGaasJpLjJXzuo4zBChJadMhOzqrAk+21k64WjjclPPWbSEJa1O3klsETL6AZDCXStMDrPs5EwXQbSniJUKmN+0bfSqGQkWgYIy4zIZQj+2W6c6qHFu6BJXB2siX9YyV9/UyUsz4oy08vhlwTr7aNEK7PI1zL49KCnIAZ0t6oTfo+HZ7eySyo1WWKFLVebrwSx1Trv0mYgrPYMQppeMO+iBExcfqyteH/vzAH38qdwXrDYaqMwPsdl8p7jBwK/F57aE8vbda5gu5udfQyjduV2N7IqNuxJ0BuFpJKDm1O6dDaP8NGMiJGmtXYGbW7OXGH/HPKpMFhRss3R9oZ/wmYM7x39zV1N5Y7oMqc=',
        #     'searchKeyword': 'ssd%7C%EB%B3%B5%ED%95%A9%EA%B8%B0%7C%ED%94%84%EB%A1%9C%EB%B3%B4',
        #     'searchKeywordType': '%7B%22ssd%22%3A0%7D%7C%7B%22%EB%B3%B5%ED%95%A9%EA%B8%B0%22%3A0%7D%7C%7B%22%ED%94%84%EB%A1%9C%EB%B3%B4%22%3A0%7D',
        #     'baby-isWide': 'wide',
        #     'cto_bundle': 'NTIwBV91dXlKWTJQanB2TWFpTVBTQkRwbW42VXM4UzhJMGRLOSUyQktkc2s2OXpCellmbyUyRkhnYkJQU0tnRlZNcWJ6dHBnUGFRMUMlMkZ6Q01FZVNyNUhrSlNiZW12RXlTNUd3TTVSOW14SGk0cldZeVF6TFB2RnAzUXpIemlWRXRJWjcyekU1ZkI5TTloN2pXUkJzNHZnZlJzVXVVT29BOVlFZkxHekRMdDJoVWM0eTN6Z05LeEFrS0NUSDFoVjRJYnptZm1ESTJmaTYxVkNrYkxMZW80QVRYWmZUeHNqNkpNSVclMkZOMWNBN01aYlBjcFBDS04xeGZVamNEZm16JTJCNFV5RmJPcHdlaQ',
        #     '_abck': '54D3ED80A2F55A6CD4261FC6C32AB3E2~0~YAAQrXpGaLogdGOPAQAAb7IFcgse6BlZNXQABUNY1beN5gHvMgxZ9GQbdOhYS6MeCMgIIcHPtBz2iHx0eL+9YQxTBmxv0QnJDKbzpzJfGNMJ1k5N5vKYvl2RpQdS8J78f01rAbeDmtEK9h/8Fvi+dqYlrXZSAprqQVAHhyy/qrjmTEz1/7Hww8ej+YdQzU5E8Cp56jAT31nsaAICiT1dXO52uNzaJsalVYTCqujeiRyQcjtImJI5dN2ooZHUmJRJmvUhgsNqZfw33wKqqVYMVRjD+BzX7nV2eeHblU+u1+zSNH347Ki0BAkfJuliy02zKsNGzUCRuAT0vGuoMhTvzaAV0X7KaJ1BE6Sfa6NUIDCxYzSy3HpTb2ie+LzYglco4JFtC2xX3/LCV9kQLA==~-1~-1~-1',
        #     'bm_sv': '4A33E1877F45458AE1352E5FB51DA623~YAAQrXpGaLsgdGOPAQAAb7IFchfAAJWokzXr3eo0DyYG1md/pFRDakwqdap98YDgbhsAFMHrtkqvU8cNxk1J6gRMW/NbDv4bE/9FAobR7HhwQtHDiiM8FxSsTUMcpdKSb2gCcp2mJoobEbJp/QRAyZwC/DrXH1KV1xOnPnJMMH4u4K2uVUWz4kAvBY6X86+YVQKRAn+28xEdQb6rZLWYHK+LNqaEnMUhUa8kN9UiN1uYW5z7g6gcYyON8PKSxkaZHuk=~1',
        # }
        cookies = {
            'PCID': '16062593661524224436363',
            'x-coupang-accept-language': 'ko-KR',
            'x-coupang-target-market': 'KR',
            '_fbp': 'fb.1.1713884027605.708116537',
            'sc_vid': 'A00888095',
            'sc_lid': 'fuzzily',
            'sc_uid': 'KvKg6pnd13CrWErdKstYJ35NvCUsTqEyzRooDbFfaO7ibQEIFGwlZadlrrBfvg==',
            'sid': '9986eba6b55b4da3b6b858a9fa4d87bb32be3b5e',
            'gd1': 'Y',
            '_gcl_au': '1.1.852457399.1715578916',
            'overrideAbTestGroup': '%5B%5D',
            'MARKETID': '16062593661524224436363',
            # 'ak_bmsc': 'EE568EEDB700FA38798324250BB36A72~000000000000000000000000000000~YAAQdwI1F0KNB4SPAQAAhw6MhBeDFHWOKPQkigTNSAeKqe+2SMclSmaql8CfvCYDw6ZVgjDXuv2/iMhb1tSeByR/Fqy3m4/2zWPSa6zBcIVMDMBQeTUj8nBThXbQg1I5WZelVriNqjizNb2YVgq7yEwxv0m4id/OBReCcney/yODRack+5OCkZ+CcEPNlgUOPR6vH5I9r8zTj68ynuXuIZef0kGgk5WmP43Ydd/itjP2VxtDHHzGa9Nkmxy4Pw9ybvBFXf9Y36aypxyCkqlZuSBB2u/cxIIJjUaPTct2Pcd7Soch0CkkP6/HkyZJI7/cFgt0rTP+YLrIhIKobQXJEjJ9Om2e6YWXeOZzL4Y9QYOoGRg5D2p5OTX47iyl7DIZITzQfk4BgFofNkd5mWyryGbIPJODerd3thPYne/aJIl1IMJsQf51HPMxQy+4LEg/wB2G6E2J5x4mh+oSEXE=',
            'searchKeyword': 'ssd%7C%EB%B3%B5%ED%95%A9%EA%B8%B0%7C%ED%94%84%EB%A1%9C%EB%B3%B4%7C%EC%8A%A4%EC%B9%B4%EC%9D%B4%ED%82%A5%20%EC%96%B4%EB%A6%B0%EC%9D%B4%20%EC%B6%95%EA%B5%AC%EB%93%9C%EB%A1%A0%7C%EB%A0%88%EA%B3%A0%7C%EB%B0%94%EC%9D%B4%EB%A1%9C%EB%B4%87%20%EC%BD%94%EB%94%A9%EB%93%9C%EB%A1%A0',
            'searchKeywordType': '%7B%22ssd%22%3A0%7D%7C%7B%22%EB%B3%B5%ED%95%A9%EA%B8%B0%22%3A0%7D%7C%7B%22%ED%94%84%EB%A1%9C%EB%B3%B4%22%3A0%7D%7C%7B%22%EC%8A%A4%EC%B9%B4%EC%9D%B4%ED%82%A5%20%EC%96%B4%EB%A6%B0%EC%9D%B4%20%EC%B6%95%EA%B5%AC%EB%93%9C%EB%A1%A0%22%3A0%7D%7C%7B%22%EB%A0%88%EA%B3%A0%22%3A0%7D%7C%7B%22%EB%B0%94%EC%9D%B4%EB%A1%9C%EB%B4%87%20%EC%BD%94%EB%94%A9%EB%93%9C%EB%A1%A0%22%3A0%7D',
            '_abck': '54D3ED80A2F55A6CD4261FC6C32AB3E2~0~YAAQRCPJF5T42HyPAQAAJwGRhAv6VxI8AAdQFrJJVxLHBQpwcdPwlZMiODTgz//NdSvZLxXhuYH50YnxqWmD8U984iozapNmppja+9LRXx1HAr6eP9NhOmvkcDFFn2MLr7OOruGdi/bv0e6NTFiEGhBV0L6BaXDVSV/FyXW/Zj3aN0m0uUcK0fvN00WUnsmTiAzco+6FDBd7SJsHlNqPyUIoJ/Oe8os2Tq0ePwHag2LCRGTqvJc8MPPqBZpC2iDEj1IdGqYCmpvSz7Z9+SuNanA+vRD4rfsyy6+GH2A7u+/sBam9lkQn63NdrXr6g5NjIV1el4QCeNkOPIg2uSCXA7d5IXfCP6IGf03D1E9hDJRS0RcvO8bDUWvANf8aPflISq6x7c/CBIuL5wtcoQm0yLUfXyydhNrggusVbQWTcujmz8GpLO7D~-1~||0||~-1',
            'bm_sz': '7EEDF1CF73B22DE23AA626253437B60E~YAAQRCPJF1f72HyPAQAAQAmRhBd6SSmiZUuWQOkt5qz2z6RtzEBKvzHVufu+3TbIqtfyzGMQ+9DLytwOOVOeCGvVelXn0C8bPS1ZFwqMd+tZcEy57u+UBupmZzNjhNpi198zJVftfVH5O1FqTl0d6X3B7rcQdw4pPGC7CFqO3bF0COUTT/X8L73T7j20FLXxqT330BVWT3JQ61QYSOziDGSqZdpbXaX4VLk2cjd8QxriUJ7KMqwLJkW17g9OT3l23K55nb/GLc70wXSE5zp1oNC9Ad1LDABW80LrtQ6vjFP9Rl6O1fvr5BRMKizd9B+X5bRIVCX04yoqlBcCxXVeRGO2HdSlHj8LojoYZS+SN0lCeRZdWvqBKpTd+RujM1FW+JQVTYK6vFmlj4qc6dp0qwLsr7mtBIyI00suGIc=~3687984~4342323',
            'cto_bundle': 'dCXra191dXlKWTJQanB2TWFpTVBTQkRwbW43NCUyRjVhNDNha04lMkZjYmJucVBydnBIZFBXZWtkOTN4dTE0NSUyQmhGNjNQSXNUbVVqbmJxbkhzT2VyUVJSRW9OMUN6Umo4d0VCYWZlZU44bEREeGxPQXZPRktweHZSVVpWSGtvR0dNcXZoeTZwZ3Q3S2JQWUpnTmtQbzlTRTBhRzZuRVFwMlB0dUtYb285NlMlMkJMM2JjMEVhWVNCUlhPUW1GbXM1VkloZkpnRWQlMkZDQUQ1ZTlKeiUyQnJyMUhXOXNjUWRJMjhoc3QxcFpYYkpudGNVU28walRaczFHVEVodGU2cUwlMkZ2RmpIeFY2cWpOWXU',
            'baby-isWide': 'wide',
            'bm_sv': 'F906B9D299FCC245760EAF9E8FA9CE1C~YAAQRCPJFxT92HyPAQAA+Q2RhBe3BerHQ+5yF161JXs1fbWgmznzcd+I+VcBCq8X/uIDxIaXBy4jalZVt5M2gso1w37GvHucFRPxc0fTDYhK4i3zE6wb0dQw5zcx73M1eCq71dB5zzaV7haenUAzuVQII9WIssxFQrYG1+uxvJcfUimRpwZ3fVqrViJUu+QCHvHcOP15/7MdxGgBfcrDTDZaBga7cMqpvKfP1znQ19EYhKeq4jPOYRtK36eyc21EUpw=~1',
        }

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': 'PCID=16062593661524224436363; x-coupang-accept-language=ko-KR; x-coupang-target-market=KR; _fbp=fb.1.1713884027605.708116537; sc_vid=A00888095; sc_lid=fuzzily; sc_uid=KvKg6pnd13CrWErdKstYJ35NvCUsTqEyzRooDbFfaO7ibQEIFGwlZadlrrBfvg==; sid=9986eba6b55b4da3b6b858a9fa4d87bb32be3b5e; gd1=Y; trac_src=0; trac_spec=0; trac_addtag=0; trac_ctag=""; trac_lptag=""; trac_itime=""; trac_sid=""; trac_appver=""; APPVER=; _gcl_au=1.1.852457399.1715578916; lastCheckoutId=1715591726276; overrideAbTestGroup=%5B%5D; MARKETID=16062593661524224436363; bm_sz=5106C4984D7A69B5A2F911E6E39F6E99~YAAQrXpGaCgHdGOPAQAAuwQFchf+swtbgiiHT5M9XQHUymY3xaPNG3yRKGMDjQOypqPYHZr5yqifYkUDFLdvQFOI2joE/d4bzzTiwhf1ulMMBkWSNGFxdrgq8Ng10u0GTgCP5BA1dvlFqT1vvp1XAqP9vVawp8YoouOjEMM4x2OLCqqaQ1n7LXnj5igNxE9DkojZ67tabJ4ya514Ce3JZTdwd6Mvj9SaHj9tJKbQvyDSeEBpspv3QKwdcPAYqcsivf++QYejxhWsbMduNI2T+rerMuLMkYre/DS2rZqA2SY4fIy/sdcmnecvd4fvNEfHSmBIpf0pQNmKMmJjgRZXFGrUMAkxgygw1NTm4sAZ905doAA6Q2OPPfO6q/sPPgGHB97WWSNI4t0xJdvy3zH5bvM0Jse2mPgX1tQEiXiLDWKESGJVwV+WizGZqVRvFkd6bRDj/HtPaCcLfSXz/OrFJ4aBbsN/OEV3M/ioE9eY9w8kwYpGYU8y3+vU8alNicphLnl0vmjX~3229241~3289400; ak_bmsc=0F4E18EA63C84884AC1EDE17D16B17B9~000000000000000000000000000000~YAAQrXpGaMMHdGOPAQAABwgFchfWLq3d8UbvvjA+UoUP0sCPAXww6jDLARM0gSxDwl6aE+uREQ/HVa1BqhjcwSzo48/SzJXtLCr/RrbraYB1XdaGaasJpLjJXzuo4zBChJadMhOzqrAk+21k64WjjclPPWbSEJa1O3klsETL6AZDCXStMDrPs5EwXQbSniJUKmN+0bfSqGQkWgYIy4zIZQj+2W6c6qHFu6BJXB2siX9YyV9/UyUsz4oy08vhlwTr7aNEK7PI1zL49KCnIAZ0t6oTfo+HZ7eySyo1WWKFLVebrwSx1Trv0mYgrPYMQppeMO+iBExcfqyteH/vzAH38qdwXrDYaqMwPsdl8p7jBwK/F57aE8vbda5gu5udfQyjduV2N7IqNuxJ0BuFpJKDm1O6dDaP8NGMiJGmtXYGbW7OXGH/HPKpMFhRss3R9oZ/wmYM7x39zV1N5Y7oMqc=; searchKeyword=ssd%7C%EB%B3%B5%ED%95%A9%EA%B8%B0%7C%ED%94%84%EB%A1%9C%EB%B3%B4; searchKeywordType=%7B%22ssd%22%3A0%7D%7C%7B%22%EB%B3%B5%ED%95%A9%EA%B8%B0%22%3A0%7D%7C%7B%22%ED%94%84%EB%A1%9C%EB%B3%B4%22%3A0%7D; baby-isWide=wide; cto_bundle=NTIwBV91dXlKWTJQanB2TWFpTVBTQkRwbW42VXM4UzhJMGRLOSUyQktkc2s2OXpCellmbyUyRkhnYkJQU0tnRlZNcWJ6dHBnUGFRMUMlMkZ6Q01FZVNyNUhrSlNiZW12RXlTNUd3TTVSOW14SGk0cldZeVF6TFB2RnAzUXpIemlWRXRJWjcyekU1ZkI5TTloN2pXUkJzNHZnZlJzVXVVT29BOVlFZkxHekRMdDJoVWM0eTN6Z05LeEFrS0NUSDFoVjRJYnptZm1ESTJmaTYxVkNrYkxMZW80QVRYWmZUeHNqNkpNSVclMkZOMWNBN01aYlBjcFBDS04xeGZVamNEZm16JTJCNFV5RmJPcHdlaQ; _abck=54D3ED80A2F55A6CD4261FC6C32AB3E2~0~YAAQrXpGaLogdGOPAQAAb7IFcgse6BlZNXQABUNY1beN5gHvMgxZ9GQbdOhYS6MeCMgIIcHPtBz2iHx0eL+9YQxTBmxv0QnJDKbzpzJfGNMJ1k5N5vKYvl2RpQdS8J78f01rAbeDmtEK9h/8Fvi+dqYlrXZSAprqQVAHhyy/qrjmTEz1/7Hww8ej+YdQzU5E8Cp56jAT31nsaAICiT1dXO52uNzaJsalVYTCqujeiRyQcjtImJI5dN2ooZHUmJRJmvUhgsNqZfw33wKqqVYMVRjD+BzX7nV2eeHblU+u1+zSNH347Ki0BAkfJuliy02zKsNGzUCRuAT0vGuoMhTvzaAV0X7KaJ1BE6Sfa6NUIDCxYzSy3HpTb2ie+LzYglco4JFtC2xX3/LCV9kQLA==~-1~-1~-1; bm_sv=4A33E1877F45458AE1352E5FB51DA623~YAAQrXpGaLsgdGOPAQAAb7IFchfAAJWokzXr3eo0DyYG1md/pFRDakwqdap98YDgbhsAFMHrtkqvU8cNxk1J6gRMW/NbDv4bE/9FAobR7HhwQtHDiiM8FxSsTUMcpdKSb2gCcp2mJoobEbJp/QRAyZwC/DrXH1KV1xOnPnJMMH4u4K2uVUWz4kAvBY6X86+YVQKRAn+28xEdQb6rZLWYHK+LNqaEnMUhUa8kN9UiN1uYW5z7g6gcYyON8PKSxkaZHuk=~1',
            'priority': 'u=0, i',
            'referer': 'https://www.coupang.com/np/search?q=%ED%94%84%EB%A1%9C%EB%B3%B4&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=72&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=13&rocketAll=false&searchIndexingToken=1=9&backgroundColor=',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }

        params = {
            'q': keyword,
            'channel': 'user',
            'component': '',
            'eventCategory': 'SRP',
            'trcid': '',
            'traid': '',
            'sorter': 'scoreDesc',
            'minPrice': '',
            'maxPrice': '',
            'priceRange': '',
            'filterType': '',
            'listSize': '72',
            'filter': '',
            'isPriceRange': 'false',
            'brand': '',
            'offerCondition': '',
            'rating': '0',
            'page': pageCount,
            'rocketAll': 'false',
            'searchIndexingToken': '',
            'backgroundColor': '',
        }
        print("요청시작")

        baseUrl='https://www.coupang.com/np/search'
        fullUrl=build_url(baseUrl,params)
        try:
            # response = requests.get(fullUrl,
            #                         # cookies=cookies,
            #                         headers=headers,
            #                         )
            response=GetRequest(fullUrl)
            print("요청성공")
        except:
            print("페이지없음")
            break

        soup = BeautifulSoup(response.text, 'lxml')

        table = soup.find("ul", attrs={'id': 'productList'})
        isItem=len(soup.find_all("ul", attrs={'id': 'productList'}))
        if isItem==0:
            print("상품없음11")
            break
        items = table.find_all('li')


        if len(items) == 0:
            print("상품없음2")
            break

        checkList = []
        for index, item in enumerate(items):
            try:
                url = 'https://www.coupang.com'+item.find("a",attrs={'target':'_blank'})['href']
            except:
                print("상품없음")
                continue
            print("url:", url, "/ url_TYPE:", type(url))
            title = item.find('div',attrs={'class':'name'}).get_text()
            print("title:", title, "/ title_TYPE:", type(title))
            try:
                price = int(item.find('strong',attrs={'class':'price-value'}).get_text().replace(",","").replace("원",""))
            except:
                price=9999999999
            print("price:",price,"/ price_TYPE:",type(price))
            checkList.append(title)
            if float(priceRatio) * supabaseData['priceLow'] < price < supabaseData['priceLow']:
                try:
                    vendorName, repPersonName, repPhoneNum, repAddress, repEmail=GetDetailsCoupang(url)
                except:
                    vendorName=""
                    repPersonName = ""
                    repPhoneNum=""
                    repAddress=""
                    repEmail=""
                data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                        'priceLow': supabaseData['priceLow'], 'platform': '쿠팡', 'url': url, 'salesInfo': vendorName+","+repPersonName+","+repPhoneNum+","+repAddress+","+repEmail,
                        'inputKeyword': supabaseData['name']}
                print("data:", data, "/ data_TYPE:", type(data))
                dataList.append(data)
                time.sleep(1)
        if len(checkList) == 0 or ",".join(checkList) == ",".join(prevCheckList):
            print("상품없음3")
            break
        prevCheckList = checkList.copy()
        pageCount += 1
        time.sleep(random.randint(20, 30) * 0.1)
        print("======================")
    return dataList
def GetSearchNaverSmartstore(supabaseData,priceRatio):
    keyword = supabaseData['name']
    pageCount = 1
    dataList = []
    prevCheckList = ['11']
    while True:
        print("네이버쇼핑★★★키워드는:{}".format(keyword))
        print("pageCount:", pageCount, "/ pageCount_TYPE:", type(pageCount))
        cookies = {
            'NNB': 'WA6OT6AVLITWM',
            '_ga': 'GA1.1.121891294.1713878001',
            '_ga_451MFZ9CFM': 'GS1.1.1713878001.1.1.1713878022.0.0.0',
            'ASID': 'de6a33cf0000018f0b81b0b40000004c',
            'NFS': '2',
            'SHP_BUCKET_ID': '3',
            '_fwb': '104oWuwoA1OxFwDMQiNpNJm.1715861604891',
            'ncpa': '402990|03c455ddfab878be5f934e94478b98984c922fbc|lw9cula0|s_47130c01b681|dd64292a199f9eac9aeb624a64da287f0ba1de58:198995|431cb9d23edcf31d637a29e495ecdf41f6bc0bdf|lw9cup4w|s_36b9975a9d38|6efae9b238b21aa980d48945424a7d5ab2442863:54191|6a3a31c5ad7cdfeb38f63d64acdaf57a35882964|lw9cuvb4|s_cdad0ee04b2|b720607dbdb8aa0ec273923396546bc588e60660:9382964|beabe527648d43971e6ccf76f3c215e2160bc899|lw9cuz60|s_1922660954ce6|51f2cc085c6525a17b8976887b69e51cfd39fba7:313503|lw9dc9uo|6127faad4112206f04ca607611f708d11b5122c2|s_469290831878637971|680a3471fae95cd22df27389b51597d93ca15b2c:745802|lw9dchkg|5d0c8dc44aea45d7f43d7506ac6b5fad6db633ae|s_2665d723ab8fd|e7dd86a45ec2edc1d606c37fba7fa3728fad2f49:153376|lw9dcm74|9214c05f0b5d1a8fc3a6b0c3f8018236662906e1|s_107e2382464a|e57a17f78d56d9efc494888204e25ea9f32b9e3c:853405|lw9dlurc|c0658b1caf826c71c015fb155b34ace4a5df23f7|s_26d31bfafa072|aeb3550d2519646f174aadd49c71fecaf690cad4:95694|lw9ek0p4|860070711cab0c8f03468a84a5e3d2f832e79b36|95694|43951ae30e1e756903faf6e688625064470a2f59:122785|lw9ek5bs|00cc3861fa24bad9cd396dc719a98affd7a0d965|s_1ff44278576b|2407bd5a95724165f92b2eae6476d99caa961c65',
            'CBI_SES': 'F1VxhM8i7fEOvVFBI7lADWX91wbnwcuXuCE4eHiSijpCxyW1ziiOXoeUaaBVG6LpaFKigCFwoMm12H/4rFos/BRnEbVNmPOpFUHmQKP5y7nYRt36Wai+33R3GGGYul8lZfVTsaUjzvrzRWBaPOp8bliclW8TG07k5c8YMsCV48TL0Xoo82vqymL9A+EsQxhQnV/es2pj0xkuthHafrii9KNgcd+uGciJtUDQLZPBxIXO7ZvwoaMELJD193QtvjBYkkUzpMvefGmGgodjaWw9yj5BlS4E9QkYT+DS/AoyzeuroKNs5FmUV3vFfhID776gnAi/CsuTMRUxummmWaXmKmmeraou/2aMqD3zqohbMvdMxfziR39oZL0IeWw4XcdtLnXdVRgvgiU5FQBorUAPXOhXoY2650NbhArfNGFyPoZ1GCzyat80p9oTM0LUw+RxZVM/6bmmdK+U5NgvgSXJr3Xkqk27WHIyxR0qunPUAXI=',
            'CBI_CHK': '"r5V0mf9uRUZHZ/vmLGy3ez7f4/k4aqWXL5o03eN68fr4senxX6NGEnbCzsijj2KG9raPGFvh6mxGKdqEGYA1jKUwghn+t+LaaKRo6p413KKjt+0rLE/lP3CQR7OqFrRjDTNYspJMnjVztln4eK7FWWZcNOGnpPw59xlH71bJONc="',
            'nid_inf': '1103175498',
            'NID_AUT': 'VUVJgd/JSN8vR/SDPAvn7L2YcbCEgfP9T5wCP1xLbCTn30FhWVyE11yBzT01rlOc',
            'NID_JKL': 'H8Y0sZs0ciFihxoRLV3J4f+gxFsy2MHpyO57KcL9F1k=',
            '_naver_usersession_': 'h6S/lqYWKhLFDaGT75jU3TBL',
            'page_uid': 'iCkB1spzL8wss4ZNq6ossssst2K-226936',
            'spage_uid': 'iCkB1spzL8wss4ZNq6ossssst2K-226936',
            'NID_SES': 'AAABkULGHas3VwY3+HE63IK+Ale5r2nUH3eOtWdyo4hQ/Q4Wl0zY42vs4Wp2g4conwumq0skqnX4NdkG7/ZA5R838G9mBa+y/rO9PqFYp6bf/CWRbctSNJyBM+6mwT0JILEZjwJovF4DajTOf63TKrVjOvWz6wY8cGR5k3+x3Y9GpwSG6/C/Yly+eEeRKJ1QequUlD60PSoHMpLF3aBq/oDOOxE97fzc+pIembYn25FQ9T+E+NC8P2Hi9SCEv9M8VC+aOQc4HKKHrwqR1QgXUEruqmMkSHVjJPrAgzVw9WTp6e/4wiD9jqSfINzdXcHIJBPlrogXxCb63tSwd6cHctgE5nE9Z8ZL0hShyjmeIAEhEbZiXeF8vU96MK8pyqmbjYqr4ruwjtmVT9Em3fccHNzrHJ1l7C6pehPZZ2BPMPOHHwFnOTETEPWonZL0shDuPAObZ4mgdujNjjuuebrfjCFU6iISXDcAIi46g1dvn/IvxuBkLBoswgFdlAMNF3Hz4txwvSQnxG/1AT055x1IhQPL7TZuQFHpH8xgkNNyf+tdmhhH',
            'BUC': 'A7CKXktn5MESWrAPd6Ct_vuSqCeloTKFJTDGQF10qQI=',
        }
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            # 'cookie': 'NNB=WA6OT6AVLITWM; _ga=GA1.1.121891294.1713878001; _ga_451MFZ9CFM=GS1.1.1713878001.1.1.1713878022.0.0.0; ASID=de6a33cf0000018f0b81b0b40000004c; NFS=2; SHP_BUCKET_ID=3; CBI_SES=CBspH5w4Jk1t8k/Q41oN3cPBzcn13vvIJ1f/AYfhSuswcKIdmiQLtsbbGk68UWXT9ANhsPG2O48r/mC5532SGfF917wjM/Y0Zns09OdH6M2zxQ5/lJETXWwOw1YQppoisnVbzCDcscef+bpg6dq/aKndl9kQxFteLuafTmolT6cKsGoxJsJgEJKSP5RVP8BHbo+eS+MGmxb7B3Ik1aD/pHYzOMXkvYCuaVDNlm3LzrgL8/d6x+egURqV58G5Q/m7snDru4weNz3CfB/7zZ8bgicAfUDCmbpSEXNcjd17Jz5LVwzTAxhAAEzbno2JcSROrq6h8EdD9JuvkeL9h8CXOwldGckG+5Gb2vFi3iQBloW10UgYcAfqjZDtmdUVnnTQnjobfnlHusu6GwK9UBtszOg2VJRlljJcNs+5JOw0UcpIRTxAuAIpyZOu0JtUYLHePlogz2rtKnySi1OSY2j9RbiSWISnveWStUVAXDDVNjc=; ncpa=1137650|lw97owv4|7dc80820cc50f0e25ad24b7ac6df2438ca240571|s_1fedda0421a9e|cb22023f673b75bbcf200e8a84700b2b4ee0fdd4; _fwb=104oWuwoA1OxFwDMQiNpNJm.1715861604891; page_uid=iCU9TlqVN8VssEh4tu4ssssst1d-246488; CBI_CHK="r5V0mf9uRUZHZ/vmLGy3ez7f4/k4aqWXL5o03eN68fr4senxX6NGEnbCzsijj2KG9raPGFvh6mxGKdqEGYA1jKUwghn+t+LaaKRo6p413KKjt+0rLE/lP3CQR7OqFrRjFdrXbikh1W8/eg2eQrJNECbCCdn1+N5ee8lN7CvVeyg="; nid_inf=649203180; NID_AUT=bJ4bB0FYCgEoeRfM04x+6WsEjQsPU6kz4gbUdKVF4bTV1OrTDGzWZXoD/mRmh/Ph; NID_JKL=cg183Ds1uUpoYRcBd9RXdvCz9Of2f2xxMb1n1Bd95Zk=; NID_SES=AAABf/GPFOCZEJcUgJ+CctTLY52NUzDG+BfuOXvoY5xWyUiyu+NI04O+oL4FxwtrhdK4AY96jFIUjlY5iZU2QxQpk8YtpuYN9ojC830sFDHDdrY1Zf+TqWLarCiNCkof4mXy48Qxha+51/NEtQQYZg1A8Adf+TjZmeArXeJqlg7xPel60qEwEiOCqPk6+UL0yZa19dYMz3XgqRuh2WG8D30fXR7DpK0C3WSS6ciOPQY8dmJTHzW6dpssua6TAw08D+6VdiOfO0CJ0fV/xkPIm963UyUwAtFJgzm2SHvUO8VzZ3i5uv2MsCQMN3+408kcU4PzuOsS85BwMsYUNMWF7iUg4AEx6v72aafLDTfDhzqAO441hSnqkBn7UPIbIumCjoW6UhG/vVnhz9XfcgIh5RvDOZmRUUvcM1DjztigJiZi4/ZmfJAdatRnb4CVSJKda8t9O/rS/5doDhkHB5/b25Qc39Lg15nW4ZWZgbNHv46oNRLKGo5v+IgvQTxVIFHA9gk27w==; spage_uid=iCU9TlqVN8VssEh4tu4ssssst1d-246488; BUC=zHma7ei2exsTx7h9cgF6UYupWccV54s_Q2BNfIJvvT4=',
            'priority': 'u=0, i',
            'referer': 'https://shopping.naver.com/home?dtm_source=naver_pcbs&dtm_medium=mktatrb_etc&dtm_campaign=2402-shopping-001&pcode=naver_pcbs&campaign_id=2402-shopping-001&channel_id=naver_pcbs',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-arch': '"x86"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-form-factors': '"Desktop"',
            'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.208", "Google Chrome";v="124.0.6367.208", "Not-A.Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-ch-ua-wow64': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }

        params = {
            'exagency': 'true',
            'exrental': 'true',
            'exused': 'true',
            'pagingIndex': pageCount,
            'pagingSize': '80',
            'productSet': 'total',
            'query': keyword,
            'sort': 'rel',
            'timestamp': '',
            'viewType': 'list',
        }
        try:
            response = requests.get('https://search.shopping.naver.com/search/all', params=params, cookies=cookies,
                                    headers=headers)
        except:
            print("페이지없음")
            break

        soup = BeautifulSoup(response.text, 'lxml')

        table = soup.find("ul", attrs={'id': 'productList'})
        try:
          target = soup.find("script", attrs={'id': '__NEXT_DATA__'}).get_text()
        except:
          print("script더없음")
          break
        results = json.loads(target)
        items = find_option_combinations(results, 'list')
        print("script가져오기완료")
        if len(items) == 0:
            print("상품없음2")
            break

        checkList = []
        
        for index, item in enumerate(items):
            isAd = item['item'].get("adId", "")
            if isAd == "":
                title = item['item'].get('productName', "")
                print("title:", title, "/ title_TYPE:", type(title))
                checkList.append(title)
                try:
                    price = int(item['item'].get('mobilePrice', ""))
                except:
                    price=99999999999
                print("price:", price, "/ price_TYPE:", type(price))
                url = item['item'].get('mallProductUrl', "")
                print("url:", url, "/ url_TYPE:", type(url))
                if url == "":
                    print("카탈로그")
                    mallList = item['item']['lowMallList']
                    crUrl=item['item']['crUrl']
                    for mall in mallList:
                        chnlType=mall.get('chnlType',"")
                        if chnlType=="STOREFARM":
                            try:
                                eachPrice = int(mall['price'])
                            except:
                                eachPrice=999999999
                            print("eachPrice:",eachPrice,"/ eachPrice_TYPE:",type(eachPrice))
                            try:
                                mallName=mall['name']
                            except:
                                mallName="없음"
                            print("mallName:",mallName,"/ mallName_TYPE:",type(mallName))
                            if float(priceRatio) * supabaseData['priceLow'] < eachPrice < supabaseData['priceLow']:
                                data = {'title': title, 'realPrice': eachPrice, 'url': crUrl,
                                        'priceHigh': supabaseData['priceHigh'],
                                        'priceLow': supabaseData['priceLow'], 'platform': '네이버쇼핑',
                                        'salesInfo': "",
                                        'inputKeyword': supabaseData['name'],'additionalInfo':'카탈로그,'+mallName}
                                print("data:", data, "/ data_TYPE:", type(data))
                                dataList.append(data)
                                time.sleep(1)

                else:
                    print("일반상품")
                    if float(priceRatio) * supabaseData['priceLow'] < price < supabaseData['priceLow'] and url.find('smartstore')>=0:

                        data = {'title': title, 'realPrice': price, 'url': url, 'priceHigh': supabaseData['priceHigh'],
                                'priceLow': supabaseData['priceLow'], 'platform': '네이버쇼핑', 'url': url, 'salesInfo': "",
                                'inputKeyword': supabaseData['name'],'additionalInfo':'일반상품'}
                        print("data:", data, "/ data_TYPE:", type(data))
                        dataList.append(data)
                        time.sleep(1)
        if ",".join(checkList) ==",".join(prevCheckList):
            print("상품더없음")
            break
        
        
        with open("smartstore.json","w",encoding="utf-8") as file:
            json.dump(dataList,file,ensure_ascii=False,indent=2)
        
        prevCheckList=checkList.copy()
         
        pageCount += 1
        time.sleep(random.randint(20, 30) * 0.1)
        print("======================")
    return dataList

def GetDetailsCoupang(productId):
    cookies = {
        'PCID': '16062593661524224436363',
        'x-coupang-accept-language': 'ko-KR',
        'x-coupang-target-market': 'KR',
        # '_fbp': 'fb.1.1713884027605.708116537',
        # 'sc_vid': 'A00888095',
        # 'sc_lid': 'fuzzily',
        # 'sc_uid': 'KvKg6pnd13CrWErdKstYJ35NvCUsTqEyzRooDbFfaO7ibQEIFGwlZadlrrBfvg==',
        # 'sid': '9986eba6b55b4da3b6b858a9fa4d87bb32be3b5e',
        # 'gd1': 'Y',
        # 'trac_src': '0',
        # 'trac_spec': '0',
        # 'trac_addtag': '0',
        # 'trac_ctag': '""',
        # 'trac_lptag': '""',
        # 'trac_itime': '""',
        # 'trac_sid': '""',
        # 'trac_appver': '""',
        # 'APPVER': '',
        # '_gcl_au': '1.1.852457399.1715578916',
        # 'lastCheckoutId': '1715591726276',
        'MARKETID': '16062593661524224436363',
        'bm_sz': '5106C4984D7A69B5A2F911E6E39F6E99~YAAQrXpGaCgHdGOPAQAAuwQFchf+swtbgiiHT5M9XQHUymY3xaPNG3yRKGMDjQOypqPYHZr5yqifYkUDFLdvQFOI2joE/d4bzzTiwhf1ulMMBkWSNGFxdrgq8Ng10u0GTgCP5BA1dvlFqT1vvp1XAqP9vVawp8YoouOjEMM4x2OLCqqaQ1n7LXnj5igNxE9DkojZ67tabJ4ya514Ce3JZTdwd6Mvj9SaHj9tJKbQvyDSeEBpspv3QKwdcPAYqcsivf++QYejxhWsbMduNI2T+rerMuLMkYre/DS2rZqA2SY4fIy/sdcmnecvd4fvNEfHSmBIpf0pQNmKMmJjgRZXFGrUMAkxgygw1NTm4sAZ905doAA6Q2OPPfO6q/sPPgGHB97WWSNI4t0xJdvy3zH5bvM0Jse2mPgX1tQEiXiLDWKESGJVwV+WizGZqVRvFkd6bRDj/HtPaCcLfSXz/OrFJ4aBbsN/OEV3M/ioE9eY9w8kwYpGYU8y3+vU8alNicphLnl0vmjX~3229241~3289400',
        # # 'ak_bmsc': '0F4E18EA63C84884AC1EDE17D16B17B9~000000000000000000000000000000~YAAQrXpGaMMHdGOPAQAABwgFchfWLq3d8UbvvjA+UoUP0sCPAXww6jDLARM0gSxDwl6aE+uREQ/HVa1BqhjcwSzo48/SzJXtLCr/RrbraYB1XdaGaasJpLjJXzuo4zBChJadMhOzqrAk+21k64WjjclPPWbSEJa1O3klsETL6AZDCXStMDrPs5EwXQbSniJUKmN+0bfSqGQkWgYIy4zIZQj+2W6c6qHFu6BJXB2siX9YyV9/UyUsz4oy08vhlwTr7aNEK7PI1zL49KCnIAZ0t6oTfo+HZ7eySyo1WWKFLVebrwSx1Trv0mYgrPYMQppeMO+iBExcfqyteH/vzAH38qdwXrDYaqMwPsdl8p7jBwK/F57aE8vbda5gu5udfQyjduV2N7IqNuxJ0BuFpJKDm1O6dDaP8NGMiJGmtXYGbW7OXGH/HPKpMFhRss3R9oZ/wmYM7x39zV1N5Y7oMqc=',
        # 'searchKeyword': 'ssd%7C%EB%B3%B5%ED%95%A9%EA%B8%B0%7C%ED%94%84%EB%A1%9C%EB%B3%B4%7C%EC%8A%A4%EC%B9%B4%EC%9D%B4%ED%82%A5%20%EC%96%B4%EB%A6%B0%EC%9D%B4%20%EC%B6%95%EA%B5%AC%EB%93%9C%EB%A1%A0',
        # 'searchKeywordType': '%7B%22ssd%22%3A0%7D%7C%7B%22%EB%B3%B5%ED%95%A9%EA%B8%B0%22%3A0%7D%7C%7B%22%ED%94%84%EB%A1%9C%EB%B3%B4%22%3A0%7D%7C%7B%22%EC%8A%A4%EC%B9%B4%EC%9D%B4%ED%82%A5%20%EC%96%B4%EB%A6%B0%EC%9D%B4%20%EC%B6%95%EA%B5%AC%EB%93%9C%EB%A1%A0%22%3A0%7D',
        # 'overrideAbTestGroup': '%5B%5D',
        'cto_bundle': 'oM8Ibl91dXlKWTJQanB2TWFpTVBTQkRwbW4yNUZIMCUyRlBPQ2NPcHhvc1ElMkZRdkNNek9HODJjb0dYeG1rUVBob3FRbEpzdG9Na3RjUU9UeWh5a3NZQW4lMkYwWUlmVHRVQkRJVzMwRTNUbDhvNyUyRkk3NWgwJTJCSUtpcG9aaU1nQjltYUZqbiUyQk9ta0h3bjhVVjQ0d0Y3dDltN2Zydms1TWhzVVUwakNxWVBCSmlnSW9OQTZVMmlGam5LNWU2dUdDNlU4RDVVYVV5UlZHWVY4UXY5cSUyRkVRUTJwZ2lnSm9xRmVOZ250OUp4YXdsbyUyRkE1S1hCdG1vZHNzSjZNNVJreVJyUFJORG9zYWRPWg',
        'baby-isWide': 'wide',
        '_abck': '54D3ED80A2F55A6CD4261FC6C32AB3E2~0~YAAQl+PfratVvE+PAQAAXxIqcgvKisMVmiRuHquygU6XDO+ABs67k/J9CNnQ1FxCGYW2U3s9bytaHJztZd4gbu5BaCLEXT/yQMjrftF93OPSgtpCl3qTQNjpNf1/i+qXrXf0IIMYiZI415MlNPI6sHIgsoFP01AxOwURq//AyTKPj9rhtj7e5DgsgRQKDXpqQAFzl+HodlMcbwY3jRUAfOO19wgmbmT8QDIFQmeaaNkPtXHhXnF5WZsJpWOMVHS2jhMM5m9CAqCp8Mz86kf8X1lZfB1L4QUC9+fbZVCk64rajaE/cLIL9pqGGChkb9nbScY5kEsnHrATFTUbmg5i5N5yCnRbxvh0nhkowBGnL77n4BHLd2RfYe6s4ssD8OCafSVN5ocYMxe0aR4jTQ==~-1~-1~-1',
        'bm_sv': '4A33E1877F45458AE1352E5FB51DA623~YAAQl+PfraxVvE+PAQAAXxIqchfIR/5HNZP9z8rM+SY6dkFYvucherFE4BLox6IJ+GT140oRvPjYLviwex9hoVXhsAloe1srfZAUs3f8pKTbChWG75rYYk5ZIgkfOcM9JCQEU7QEo79JeDDlNPRnkoo1rsgJ0PnbOU9lHMnrKRPVzVw7g2gAFGC+yysySz8sZE4SGWz9DnByGTUipF+3AssGXAHod7cVUSltax4iapSCHg0XNwQpjjSst5tbKKGKxSM=~1',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'PCID=16062593661524224436363; x-coupang-accept-language=ko-KR; x-coupang-target-market=KR; _fbp=fb.1.1713884027605.708116537; sc_vid=A00888095; sc_lid=fuzzily; sc_uid=KvKg6pnd13CrWErdKstYJ35NvCUsTqEyzRooDbFfaO7ibQEIFGwlZadlrrBfvg==; sid=9986eba6b55b4da3b6b858a9fa4d87bb32be3b5e; gd1=Y; trac_src=0; trac_spec=0; trac_addtag=0; trac_ctag=""; trac_lptag=""; trac_itime=""; trac_sid=""; trac_appver=""; APPVER=; _gcl_au=1.1.852457399.1715578916; lastCheckoutId=1715591726276; MARKETID=16062593661524224436363; bm_sz=5106C4984D7A69B5A2F911E6E39F6E99~YAAQrXpGaCgHdGOPAQAAuwQFchf+swtbgiiHT5M9XQHUymY3xaPNG3yRKGMDjQOypqPYHZr5yqifYkUDFLdvQFOI2joE/d4bzzTiwhf1ulMMBkWSNGFxdrgq8Ng10u0GTgCP5BA1dvlFqT1vvp1XAqP9vVawp8YoouOjEMM4x2OLCqqaQ1n7LXnj5igNxE9DkojZ67tabJ4ya514Ce3JZTdwd6Mvj9SaHj9tJKbQvyDSeEBpspv3QKwdcPAYqcsivf++QYejxhWsbMduNI2T+rerMuLMkYre/DS2rZqA2SY4fIy/sdcmnecvd4fvNEfHSmBIpf0pQNmKMmJjgRZXFGrUMAkxgygw1NTm4sAZ905doAA6Q2OPPfO6q/sPPgGHB97WWSNI4t0xJdvy3zH5bvM0Jse2mPgX1tQEiXiLDWKESGJVwV+WizGZqVRvFkd6bRDj/HtPaCcLfSXz/OrFJ4aBbsN/OEV3M/ioE9eY9w8kwYpGYU8y3+vU8alNicphLnl0vmjX~3229241~3289400; ak_bmsc=0F4E18EA63C84884AC1EDE17D16B17B9~000000000000000000000000000000~YAAQrXpGaMMHdGOPAQAABwgFchfWLq3d8UbvvjA+UoUP0sCPAXww6jDLARM0gSxDwl6aE+uREQ/HVa1BqhjcwSzo48/SzJXtLCr/RrbraYB1XdaGaasJpLjJXzuo4zBChJadMhOzqrAk+21k64WjjclPPWbSEJa1O3klsETL6AZDCXStMDrPs5EwXQbSniJUKmN+0bfSqGQkWgYIy4zIZQj+2W6c6qHFu6BJXB2siX9YyV9/UyUsz4oy08vhlwTr7aNEK7PI1zL49KCnIAZ0t6oTfo+HZ7eySyo1WWKFLVebrwSx1Trv0mYgrPYMQppeMO+iBExcfqyteH/vzAH38qdwXrDYaqMwPsdl8p7jBwK/F57aE8vbda5gu5udfQyjduV2N7IqNuxJ0BuFpJKDm1O6dDaP8NGMiJGmtXYGbW7OXGH/HPKpMFhRss3R9oZ/wmYM7x39zV1N5Y7oMqc=; searchKeyword=ssd%7C%EB%B3%B5%ED%95%A9%EA%B8%B0%7C%ED%94%84%EB%A1%9C%EB%B3%B4%7C%EC%8A%A4%EC%B9%B4%EC%9D%B4%ED%82%A5%20%EC%96%B4%EB%A6%B0%EC%9D%B4%20%EC%B6%95%EA%B5%AC%EB%93%9C%EB%A1%A0; searchKeywordType=%7B%22ssd%22%3A0%7D%7C%7B%22%EB%B3%B5%ED%95%A9%EA%B8%B0%22%3A0%7D%7C%7B%22%ED%94%84%EB%A1%9C%EB%B3%B4%22%3A0%7D%7C%7B%22%EC%8A%A4%EC%B9%B4%EC%9D%B4%ED%82%A5%20%EC%96%B4%EB%A6%B0%EC%9D%B4%20%EC%B6%95%EA%B5%AC%EB%93%9C%EB%A1%A0%22%3A0%7D; overrideAbTestGroup=%5B%5D; cto_bundle=oM8Ibl91dXlKWTJQanB2TWFpTVBTQkRwbW4yNUZIMCUyRlBPQ2NPcHhvc1ElMkZRdkNNek9HODJjb0dYeG1rUVBob3FRbEpzdG9Na3RjUU9UeWh5a3NZQW4lMkYwWUlmVHRVQkRJVzMwRTNUbDhvNyUyRkk3NWgwJTJCSUtpcG9aaU1nQjltYUZqbiUyQk9ta0h3bjhVVjQ0d0Y3dDltN2Zydms1TWhzVVUwakNxWVBCSmlnSW9OQTZVMmlGam5LNWU2dUdDNlU4RDVVYVV5UlZHWVY4UXY5cSUyRkVRUTJwZ2lnSm9xRmVOZ250OUp4YXdsbyUyRkE1S1hCdG1vZHNzSjZNNVJreVJyUFJORG9zYWRPWg; baby-isWide=wide; _abck=54D3ED80A2F55A6CD4261FC6C32AB3E2~0~YAAQl+PfratVvE+PAQAAXxIqcgvKisMVmiRuHquygU6XDO+ABs67k/J9CNnQ1FxCGYW2U3s9bytaHJztZd4gbu5BaCLEXT/yQMjrftF93OPSgtpCl3qTQNjpNf1/i+qXrXf0IIMYiZI415MlNPI6sHIgsoFP01AxOwURq//AyTKPj9rhtj7e5DgsgRQKDXpqQAFzl+HodlMcbwY3jRUAfOO19wgmbmT8QDIFQmeaaNkPtXHhXnF5WZsJpWOMVHS2jhMM5m9CAqCp8Mz86kf8X1lZfB1L4QUC9+fbZVCk64rajaE/cLIL9pqGGChkb9nbScY5kEsnHrATFTUbmg5i5N5yCnRbxvh0nhkowBGnL77n4BHLd2RfYe6s4ssD8OCafSVN5ocYMxe0aR4jTQ==~-1~-1~-1; bm_sv=4A33E1877F45458AE1352E5FB51DA623~YAAQl+PfraxVvE+PAQAAXxIqchfIR/5HNZP9z8rM+SY6dkFYvucherFE4BLox6IJ+GT140oRvPjYLviwex9hoVXhsAloe1srfZAUs3f8pKTbChWG75rYYk5ZIgkfOcM9JCQEU7QEo79JeDDlNPRnkoo1rsgJ0PnbOU9lHMnrKRPVzVw7g2gAFGC+yysySz8sZE4SGWz9DnByGTUipF+3AssGXAHod7cVUSltax4iapSCHg0XNwQpjjSst5tbKKGKxSM=~1',
        'priority': 'u=1, i',
        'referer': 'https://www.coupang.com/vp/products/8034880219?itemId=22477471991&vendorItemId=89520061049&q=%ED%94%84%EB%A1%9C%EB%B3%B4&itemsCount=72&searchId=4a201bad160e4e66b7008244721705a3&rank=415&isAddedCart=',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-requested-with': '',
    }
    # 정규 표현식 패턴
    pattern = r"products/(\d+)"
    # 패턴 매칭
    productsNo = re.findall(pattern, productId)[0]

    # 정규 표현식 패턴
    pattern = r"itemId=(\d+)"
    # 패턴 매칭
    itemNo = re.findall(pattern, productId)[0]

    # 정규 표현식 패턴
    pattern = r"vendorItemId=(\d+)"
    # 패턴 매칭
    vendorItemNo = re.findall(pattern, productId)[0]


    fullUrl='https://www.coupang.com/vp/products/{}/items/{}/vendoritems/{}'.format(productsNo,itemNo,vendorItemNo)
    # response = requests.get(
    #     fullUrl,
    #     cookies=cookies,
    #     headers=headers,
    # )
    coupangDetail=GetRequest(fullUrl)
    # print(coupangDetail.text)
    coupangDict=json.loads(coupangDetail.text)
    print("디테일정보보여주기")

    vendorName=find_option_combinations(coupangDict,'vendorName')
    if vendorName==None:
        vendorName=""

    repPersonName=find_option_combinations(coupangDict,'repPersonName')
    if repPersonName==None:
        repPersonName=""
    repPhoneNum = find_option_combinations(coupangDict, 'repPhoneNum')
    if repPhoneNum==None:
        repPhoneNum=""
    repAddress=find_option_combinations(coupangDict,'repAddress')
    if repAddress==None:
        repAddress=""
    repEmail=find_option_combinations(coupangDict,'repEmail')
    if repEmail==None:
        repEmail=""
    print("쿠팡디테일정보가져오기완료")
    return vendorName,repPersonName,repPhoneNum,repAddress,repEmail
def GetDetailsWemakeprice(productId):
    def extract_partner_name(json_string):
        # Regular expression to extract the value associated with "partnerNm" key
        pattern = r'"partnerNm":"(.*?)"'
        match = re.search(pattern, json_string)
        partnerNm = match.group(1) if match else ""

        pattern = r'"partnerOwner":"(.*?)"'
        match = re.search(pattern, json_string)
        partnerOwner = match.group(1) if match else ""

        pattern = r'"infoCenter":"(.*?)"'
        match = re.search(pattern, json_string)
        infoCenter = match.group(1) if match else ""

        pattern = r'"partnerOwnerEmail":"(.*?)"'
        match = re.search(pattern, json_string)
        partnerOwnerEmail = match.group(1) if match else ""

        pattern = r'"addr":"(.*?)"'
        match = re.search(pattern, json_string)
        addr = match.group(1) if match else ""
        return partnerNm, partnerOwner, infoCenter, partnerOwnerEmail, addr
    cookies = {
        # 'wmp-auk': '06a0b63f-4a46-4831-a8aa-3026-d8ebb6c7f746',
        # 'wmp_pcstamp': '1715083500709014015',
        # 'WemepAffiliate': '%7B%22channelId%22%3A1000057%2C%22expirationDate%22%3A%222024-05-08T21%3A05%3A00.185%22%7D',
        # 'rp': 'http%3A%2F%2Ffront.wemakeprice.com%2Fmain%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3Dnull%26utm_term%3D%25EC%259C%2584%25EB%25A9%2594%25ED%2594%2584%26utm_content%3Dwemake%26gad_source%3D1%26gclid%3DCjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE',
        # 'WemepEdgeUtmTerm': '%EC%9C%84%EB%A9%94%ED%94%84',
        # '_fbp': 'fb.1.1715083500855.841822278',
        # '__utma': '122159757.901157887.1715083501.1715083501.1715083501.1',
        # '__utmc': '122159757',
        # '__utmz': '122159757.1715083501.1.1.utmcsr=google|utmgclid=CjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE|utmccn=null|utmcmd=cpc|utmctr=ìœ„ë©”í”„|utmcct=wemake',
        # '_gid': 'GA1.2.1895161050.1715083502',
        # '_gac_UA-18774526-1': '1.1715083502.CjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE',
        # 'SCOUTER': 'z1rb0klr38bdtt',
        # '__utmt': '1',
        # 'wmp_basic_info': 'a%3A3%3A%7Bs%3A12%3A%22cart_session%22%3Bs%3A32%3A%22f9d73add353d39776abd1815cf5f9d07%22%3Bs%3A11%3A%22IsNotWmpApp%22%3Bs%3A1%3A%221%22%3Bs%3A8%3A%22cart_qty%22%3Bi%3A0%3B%7D',
        # 'cart_noti_date': '20240507',
        # 'fb_autologin': '1',
        # '_gat_UA-18774526-1': '1',
        # 'WemepEdgeToastBannerToday': '1',
        # 'cto_bundle': '9l1abl9ibVY0TkpwZ0o4bmJsc3h4WGRqWVNSRHJqaHI3UTJhSkNEeEdsQ0JDdmI2OUFEJTJCeUpGa2dSZExkQ0dScFA1ekNzR3Z5YldJNWxrcnk1cDJlQm41TCUyRkk0aVNqVUdqN0hyMmF5ZzNXR1NHOThwcUk1JTJCVFNSd0NTWTVSTU9oNDVLQTFvT2JzR3NheXd2WmZiWlJaVnhkcjVES3lMYVNKbGRXM3BHMmVUbmRSZWpEamRaQmowTSUyRkMzUEpiZlVCOFFjOFpuNXNuR2ZvTVU2QnBHMHhkQ0Z6OTlDMHJiVGMxbUt5amtLNUhOVmc2TnZGNnRLTzJoeGY5RXhKRkJGOWpYVGEzTmFQSEs0cnExU2xGTzRNR1Jqa3FRJTNEJTNE',
        # '__utmb': '122159757.13.10.1715083501',
        # 'wlogFunnel': 'WMP-MWEB-001-0-V',
        # '_ga': 'GA1.2.518513905.1715083502',
        # '_ga_0CD35LTKXG': 'GS1.2.1715083502.1.1.1715084284.20.0.0',
        # '_ga_C3QBWSBLPT': 'GS1.1.1715083501.1.1.1715084284.20.0.0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Cookie': 'wmp-auk=06a0b63f-4a46-4831-a8aa-3026-d8ebb6c7f746; wmp_pcstamp=1715083500709014015; WemepAffiliate=%7B%22channelId%22%3A1000057%2C%22expirationDate%22%3A%222024-05-08T21%3A05%3A00.185%22%7D; rp=http%3A%2F%2Ffront.wemakeprice.com%2Fmain%3Futm_source%3Dgoogle%26utm_medium%3Dcpc%26utm_campaign%3Dnull%26utm_term%3D%25EC%259C%2584%25EB%25A9%2594%25ED%2594%2584%26utm_content%3Dwemake%26gad_source%3D1%26gclid%3DCjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE; WemepEdgeUtmTerm=%EC%9C%84%EB%A9%94%ED%94%84; _fbp=fb.1.1715083500855.841822278; __utma=122159757.901157887.1715083501.1715083501.1715083501.1; __utmc=122159757; __utmz=122159757.1715083501.1.1.utmcsr=google|utmgclid=CjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE|utmccn=null|utmcmd=cpc|utmctr=ìœ„ë©”í”„|utmcct=wemake; _gid=GA1.2.1895161050.1715083502; _gac_UA-18774526-1=1.1715083502.CjwKCAjwouexBhAuEiwAtW_Zx1DPofoLbrHY0uos8qybvjgewyAlk4olCrT3dlF1BBXI-8DnOWJqoBoCRq8QAvD_BwE; SCOUTER=z1rb0klr38bdtt; __utmt=1; wmp_basic_info=a%3A3%3A%7Bs%3A12%3A%22cart_session%22%3Bs%3A32%3A%22f9d73add353d39776abd1815cf5f9d07%22%3Bs%3A11%3A%22IsNotWmpApp%22%3Bs%3A1%3A%221%22%3Bs%3A8%3A%22cart_qty%22%3Bi%3A0%3B%7D; cart_noti_date=20240507; fb_autologin=1; _gat_UA-18774526-1=1; WemepEdgeToastBannerToday=1; cto_bundle=9l1abl9ibVY0TkpwZ0o4bmJsc3h4WGRqWVNSRHJqaHI3UTJhSkNEeEdsQ0JDdmI2OUFEJTJCeUpGa2dSZExkQ0dScFA1ekNzR3Z5YldJNWxrcnk1cDJlQm41TCUyRkk0aVNqVUdqN0hyMmF5ZzNXR1NHOThwcUk1JTJCVFNSd0NTWTVSTU9oNDVLQTFvT2JzR3NheXd2WmZiWlJaVnhkcjVES3lMYVNKbGRXM3BHMmVUbmRSZWpEamRaQmowTSUyRkMzUEpiZlVCOFFjOFpuNXNuR2ZvTVU2QnBHMHhkQ0Z6OTlDMHJiVGMxbUt5amtLNUhOVmc2TnZGNnRLTzJoeGY5RXhKRkJGOWpYVGEzTmFQSEs0cnExU2xGTzRNR1Jqa3FRJTNEJTNE; __utmb=122159757.13.10.1715083501; wlogFunnel=WMP-MWEB-001-0-V; _ga=GA1.2.518513905.1715083502; _ga_0CD35LTKXG=GS1.2.1715083502.1.1.1715084284.20.0.0; _ga_C3QBWSBLPT=GS1.1.1715083501.1.1.1715084284.20.0.0',
        'Referer': 'https://mw.wd.wemakeprice.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    response = requests.get('https://mw.wemakeprice.com/product/{}'.format(productId), cookies=cookies, headers=headers)

    partnerNm, partnerOwner, infoCenter, partnerOwnerEmail, addr = extract_partner_name(response.text)
    return partnerNm, partnerOwner, infoCenter, partnerOwnerEmail, addr
def GetDetailsInterpark(productId):
    cookies = {
        'pcid': '171454737392763070',
        '_trs_id': 'eY2770350%3F525770',
        'OAX': '3mozz2Y6DScAAV8Q',
        '_gid': 'GA1.2.660166378.1715080489',
        '_ga_4SKTL7E8Q8': 'GS1.1.1715080489.1.1.1715080508.41.0.0',
        '_SHOP_PC_ID': '20240507201508259723635',
        '_fbp': 'fb.1.1715080509363.1790636552',
        '_atrk_siteuid': 'l9HxwyMc8kcmoMta',
        '_gcl_au': '1.1.4177499.1715080750',
        '_fwb': '30TNqYf0lrhhv2oNIVyhj0.1715080750668',
        'ab.storage.deviceId.50122e68-98a7-46cd-bc57-88ed9744d020': '%7B%22g%22%3A%2243d99538-dc22-83cb-e277-48fb7822908c%22%2C%22c%22%3A1715080772504%2C%22l%22%3A1715080772504%7D',
        'shopFirstPrdEvent': '14162767708',
        'shopTwicePrdEvent': '10454711775',
        'shopThirdPrdEvent': '10454711775',
        'preferCategories': '%5B%22001100%22%2C%22001841%22%2C%22001841%22%2C%22001841%22%2C%22001140%22%5D',
        '_ga_E2Q3PB7X43': 'GS1.1.1715081274.2.0.1715081274.0.0.0',
        '_ga': 'GA1.2.1435135503.1714547375',
        'ippcd': '000000',
        'org_ippcd': '000000',
        'q_interparkstamp': '0176472256320677380517104001967285',
        'q_iaf': 'sG3p7pPV695phvOCK5LAvUm84%2B8bJ7QQPp%2FLyrcNaxeh2aN6LPvKraib%2Fl7dJnZL',
        'q_smsCertYN': 'N',
        'cto_bundle': 'zlpAB18zcWxyZiUyQnpsVnVaM0laRkdDbXNZbUVMaXN6VU1RWUtVS25WM3ZDVkJGT29EZFBzJTJCcmVVUnJYUkxrRHMwMFFZN0JadmhicmtvbkJmODZzUDhtMkM5YkdEcjJOajFyOGNaVUd3dlJyWVF4RTBmdG1FdiUyQkRnQm1YRFpKRmR4TDlpWngwVmclMkZkVkxQT1JYSlI2UXNMclhRcXhMcXJjY3VHTGNoS3Z5SnJPUFhoU1BNRWpnWVQxN2lxaXFmQnEwQmZObkNJTkNJMGg0WG5ldUhBRjAyWDlCWUtiM0U1NFVhSkxBJTJCcjUyemF1ZnBtc1g5eWNScW1QemJOWnFXZkNDS3lKaVFjRmpuVkNWUzFPMzhjeGE2Y1NYaUElM0QlM0Q',
        'appier_utmz': '%7B%22csr%22%3A%22m.shop.interpark.com%22%2C%22timestamp%22%3A1715081274%2C%22lcsr%22%3A%22m.shop.interpark.com%22%7D',
        'appier_page_isView_ef9110b85e056ec': '56dafc1e3862388c4f1d2ff7863534b948923879bc17f38631e84cd35de22de6',
        'appier_pv_counter54ffdf3b09506ec': '6',
        'appier_page_isView_54ffdf3b09506ec': '56dafc1e3862388c4f1d2ff7863534b948923879bc17f38631e84cd35de22de6',
        'appier_pv_counteref9110b85e056ec': '16',
        'ab.storage.sessionId.50122e68-98a7-46cd-bc57-88ed9744d020': '%7B%22g%22%3A%226cfb06a5-9553-aaa9-f837-8c0330a932bb%22%2C%22e%22%3A1715085998105%2C%22c%22%3A1715084198097%2C%22l%22%3A1715084198105%7D',
        'wcs_bt': 's_1ff66f16bd3a:1715084198',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'pcid=171454737392763070; _trs_id=eY2770350%3F525770; OAX=3mozz2Y6DScAAV8Q; _gid=GA1.2.660166378.1715080489; _ga_4SKTL7E8Q8=GS1.1.1715080489.1.1.1715080508.41.0.0; _SHOP_PC_ID=20240507201508259723635; _fbp=fb.1.1715080509363.1790636552; _atrk_siteuid=l9HxwyMc8kcmoMta; _gcl_au=1.1.4177499.1715080750; _fwb=30TNqYf0lrhhv2oNIVyhj0.1715080750668; ab.storage.deviceId.50122e68-98a7-46cd-bc57-88ed9744d020=%7B%22g%22%3A%2243d99538-dc22-83cb-e277-48fb7822908c%22%2C%22c%22%3A1715080772504%2C%22l%22%3A1715080772504%7D; shopFirstPrdEvent=14162767708; shopTwicePrdEvent=10454711775; shopThirdPrdEvent=10454711775; preferCategories=%5B%22001100%22%2C%22001841%22%2C%22001841%22%2C%22001841%22%2C%22001140%22%5D; _ga_E2Q3PB7X43=GS1.1.1715081274.2.0.1715081274.0.0.0; _ga=GA1.2.1435135503.1714547375; ippcd=000000; org_ippcd=000000; q_interparkstamp=0176472256320677380517104001967285; q_iaf=sG3p7pPV695phvOCK5LAvUm84%2B8bJ7QQPp%2FLyrcNaxeh2aN6LPvKraib%2Fl7dJnZL; q_smsCertYN=N; cto_bundle=zlpAB18zcWxyZiUyQnpsVnVaM0laRkdDbXNZbUVMaXN6VU1RWUtVS25WM3ZDVkJGT29EZFBzJTJCcmVVUnJYUkxrRHMwMFFZN0JadmhicmtvbkJmODZzUDhtMkM5YkdEcjJOajFyOGNaVUd3dlJyWVF4RTBmdG1FdiUyQkRnQm1YRFpKRmR4TDlpWngwVmclMkZkVkxQT1JYSlI2UXNMclhRcXhMcXJjY3VHTGNoS3Z5SnJPUFhoU1BNRWpnWVQxN2lxaXFmQnEwQmZObkNJTkNJMGg0WG5ldUhBRjAyWDlCWUtiM0U1NFVhSkxBJTJCcjUyemF1ZnBtc1g5eWNScW1QemJOWnFXZkNDS3lKaVFjRmpuVkNWUzFPMzhjeGE2Y1NYaUElM0QlM0Q; appier_utmz=%7B%22csr%22%3A%22m.shop.interpark.com%22%2C%22timestamp%22%3A1715081274%2C%22lcsr%22%3A%22m.shop.interpark.com%22%7D; appier_page_isView_ef9110b85e056ec=56dafc1e3862388c4f1d2ff7863534b948923879bc17f38631e84cd35de22de6; appier_pv_counter54ffdf3b09506ec=6; appier_page_isView_54ffdf3b09506ec=56dafc1e3862388c4f1d2ff7863534b948923879bc17f38631e84cd35de22de6; appier_pv_counteref9110b85e056ec=16; ab.storage.sessionId.50122e68-98a7-46cd-bc57-88ed9744d020=%7B%22g%22%3A%226cfb06a5-9553-aaa9-f837-8c0330a932bb%22%2C%22e%22%3A1715085998105%2C%22c%22%3A1715084198097%2C%22l%22%3A1715084198105%7D; wcs_bt=s_1ff66f16bd3a:1715084198',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
    }

    params = {
        'pay_disp_no': '',
    }

    response = requests.get(
        'https://m.shop.interpark.com/product/10223806578/0000100000',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    soup = BeautifulSoup(response.text, 'lxml')
    table = soup.find("div", attrs={'class': 'detailContentWrap'})
    rows = table.find_all('tr')
    sellerName=""
    ceoName=""
    phoneNumber=""
    addr=""
    for row in rows:
        rowName = row.find('th').get_text()
        print("rowName:", rowName, "/ rowName_TYPE:", type(rowName))
        if rowName.find("판매자") >= 0:
            sellerName = row.find('td').get_text()
        if rowName.find("대표자") >= 0:
            ceoName = row.find('td').get_text()
        if rowName.find("연락처") >= 0:
            phoneNumber = row.find('td').get_text()
        if rowName.find("소재지") >= 0:
            addr = row.find('td').get_text()
    return sellerName,ceoName,phoneNumber,addr

# 첫 번째 플래그를 True로 설정
firstFlag=False
while True:
    # Supabase 프로젝트 URL과 공개 API 키를 사용하여 클라이언트 초기화
    url: str = "https://ugxegrmjeuijmoxxcoon.supabase.co"
    key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVneGVncm1qZXVpam1veHhjb29uIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI0OTUyMDEsImV4cCI6MjAyODA3MTIwMX0.kUL6j2s_nIINFdwgnNRX4TJL7cQesN_2DeeKQue3hYE"
    headers = {
        "apikey": key,
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{url}/rest/v1/keywords", headers=headers)
    if response.status_code == 200:
        data = response.json()
        supabaseDatas = [{"name": item["name"], "priceHigh": item["priceHigh"], "priceLow": item["priceLow"],
                          'platform': item['platform']} for item in data]
    else:
        print(f"Error {response.status_code}: {response.text}")
        supabaseDatas = []
    # print("supabaseDatas:",supabaseDatas,"/ supabaseDatas_TYPE:",type(supabaseDatas))
    # 'constant' 테이블에서 모든 레코드 조회
    constants = []
    while True:
        response = requests.get(f"{url}/rest/v1/constant", headers=headers)
        if response.status_code == 200:
            constants = response.json()
            print("가져오기성공1")
            break
        else:
            print(f"가져오기실패: {response.status_code} - {response.text}")
        time.sleep(1)
    print("constants:",constants,"/ constants_TYPE:",type(constants))
    # 기본 가격 비율과 시작 시간을 설정
    priceRatio=0.8
    startTime=3
    # `constant` 테이블의 값을 기반으로 가격 비율과 시작 시간 업데이트
    for constant in constants:
        if constant['category']=="priceRatio":
            priceRatio=constant['value']
        if constant['category']=="startTime":
            startTime = int(constant['value'])

    # 총 리스트 초기화
    entireList=[]
    # 현재 시간 체크
    timeNow=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    timeCheck = datetime.datetime.now().strftime("%H%M")
    print("현재시간은:{}/timeCheck:{}/{}".format(timeNow,timeCheck,startTime*100))
    # 시작 시간 또는 첫 번째 플래그가 True일 때 작업 시작
    if int(timeCheck)==startTime*100 or firstFlag==True:
        print("작업시작")
        # Supabase 데이터에 따라 플랫폼별로 데이터 수집
        for index,supabaseData in enumerate(supabaseDatas):
          totalList=[]
          print("{}/{}번째 확인중...{}".format(index+1,len(supabaseDatas),supabaseData['name']))            
          try:
              if supabaseData['platform']=="S2B" or supabaseData['platform']=="전체":
                  dataList=GetSearchS2B(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in S2B: {e}")

          try:
              if supabaseData['platform'] == "롯데온" or supabaseData['platform'] == "전체":
                  dataList=GetLotteOn(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 롯데온: {e}")

          try:
              if supabaseData['platform'] == "11번가" or supabaseData['platform'] == "전체":
                  dataList=GetArticles11(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 11번가: {e}")

          try:
              if supabaseData['platform'] == "마루한몰" or supabaseData['platform'] == "전체":
                  dataList=GetMaru(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 마루한몰: {e}")

          try:
              if supabaseData['platform'] == "티처몰" or supabaseData['platform'] == "전체":
                  dataList = GetTeacherMall(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 티처몰: {e}")

          try:
              if supabaseData['platform'] == "아이스크림몰" or supabaseData['platform'] == "전체":
                  dataList=GetArticlesIcecreamMall(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 아이스크림몰: {e}")

          try:
              if supabaseData['platform'] == "아이스쿨샵" or supabaseData['platform'] == "전체":
                  dataList=GetArticlesIschoolShop(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 아이스쿨샵: {e}")

          try:
              if supabaseData['platform']=="팝콘에듀" or supabaseData['platform']=="전체":
                  dataList=GetSearchPopcone(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 팝콘에듀: {e}")

          try:
              if supabaseData['platform']=="지마켓" or supabaseData['platform']=="전체":
                  dataList=GetSearchGmarket(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 지마켓: {e}")

          try:
              if supabaseData['platform']=="옥션" or supabaseData['platform']=="전체":
                  dataList=GetSearchAuction(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 옥션: {e}")

          try:
              if supabaseData['platform']=="인터파크" or supabaseData['platform']=="전체":
                  dataList=GetSearchInterpark(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 인터파크: {e}")

          try:
              if supabaseData['platform']=="위메프" or supabaseData['platform']=="전체":
                  dataList=GetSearchWemakeprice(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 위메프: {e}")

          try:
              if supabaseData['platform']=="SSG" or supabaseData['platform']=="전체":
                  dataList=GetSearchSSG(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in SSG: {e}")

          try:
              if supabaseData['platform']=="쿠팡" or supabaseData['platform']=="전체":
                  dataList=GetSearchCoupang(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 쿠팡: {e}")

          try:
              if supabaseData['platform']=="네이버쇼핑" or supabaseData['platform']=="전체":
                  dataList=GetSearchNaverSmartstore(supabaseData,priceRatio)
                  totalList.extend(dataList)
          except Exception as e:
              print(f"Error in 네이버쇼핑: {e}")          
          # 중복 제거를 위해 totalList를 set으로 변환 후 다시 list로 변환
          totalList = list({frozenset(item.items()): item for item in totalList}.values())
          
          # 데이터 삽입
          for index, data in enumerate(totalList):
              timeCreated = datetime.datetime.now().strftime("%Y%m%d %H:%M:%S")
              data.update({'created_at': timeCreated})
              try:
                  response = requests.post(f"{url}/rest/v1/products", headers=headers, json=data)
                  if response.status_code == 201:
                      print(f"Inserted: {data}")
                  else:
                      print(f"Error {response.status_code}: {response.text}")
              except Exception as e:
                  print(f"에러발생: {e}")
              time.sleep(0.2)
          # 수집된 데이터를 JSON 파일로 저장
          entireList.extend(totalList)
        with open('entireList.json', 'w',encoding='utf-8-sig') as f:
            json.dump(entireList, f, indent=2,ensure_ascii=False)
            
        
        # 첫 번째 플래그를 False로 설정
        firstFlag=False

    # 10초 동안 대기
    time.sleep(10)



  
  



