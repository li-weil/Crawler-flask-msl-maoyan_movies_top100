import time
from bs4 import BeautifulSoup
import requests
import hashlib  
import pandas as pd


def main():

    dic = {
        "电影名称" : [],
        "主演" : [],
        "上映时间" : [],
        "猫眼链接（详情页）" : [],
        "评分" : [],
    }

    for page in range(0, 10):

        time.sleep(1)
        print('------------------------' + str(page) + '-------------------------')
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
            "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        cookies = {
            "__mta": "249855929.1755955651989.1756002426781.1756002441204.17",
            "uuid_n_v": "v1",
            "uuid": "E9782AF0802411F094F10D3D92218602F6CFCA754D3F4744A98D9B9A6CC14D4B",
            "_csrf": "80ac2e9e545e36ceb2218e31d396a2746509260302fb4917144d2a53db67cce2",
            "_lxsdk_cuid": "198d71ce3c1c8-063d0badc58af38-26011051-100200-198d71ce3c1c8",
            "_ga": "GA1.1.1861917512.1755955652",
            "Hm_lvt_e0bacf12e04a7bd88ddbd9c74ef2b533": "1755955652",
            "HMACCOUNT": "5132E831BD6484DE",
            "WEBDFPID": "z977xw5uu30x5w6zzy0w4y21u67xu9yw801w28w8zz1979580w7z0wu0-1756042066840-1755955664552MWYMYQQfd79fef3d01d5e9aadc18ccd4d0c95073586",
            "utm_source_rg": "AM%25dcZ909f%25289",
            "token": "AgEHH4miE8YQK_iTt5YgAephuhurjOvmDMLBIzFw-ofZzSoC-4OoWj0UNAAW6KKXpxKquITkHvFJpAAAAAAwLAAALlbMnSWew6L34WGxVQAj91x7JHfaNKQN0pJNAGXys0warq1mZRMhRgncU7gsIVJ-",
            "uid": "4618773806",
            "uid.sig": "sthWWSsWEknK5SXCau4qCNMe2V0",
            "_lxsdk": "E9782AF0802411F094F10D3D92218602F6CFCA754D3F4744A98D9B9A6CC14D4B",
            "global-guide-isclose": "true",
            "_ga_WN80P4PSY7": "GS2.1.s1756002084$o3$g1$t1756002440$j8$l0$h0",
            "Hm_lpvt_e0bacf12e04a7bd88ddbd9c74ef2b533": "1756002441",
            "_lxsdk_s": "198d9e165eb-177-18c-084%7C4618773806%7C11"
        }
        url = "https://www.maoyan.com/board/4"
        params = {
            "offset": f"{page*10}"
        }
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        response.encoding = 'utf-8'
        # with open('测试题目/maoyan.html', 'w', encoding='utf-8') as f:
        #     f.write(response.text)
        # print(response)

        soup = BeautifulSoup(response.text, 'html.parser')
        dl = soup.find('dl', class_='board-wrapper')
        # print(dl)
        if dl: # 检查dl是否成功找到了元素
            dd = dl.find_all('dd')
            for item in dd:
                name = item.find('a')['title']
                id_movie = item.find('a')['data-val'].split(':')[-1].replace('}', '')
                star = item.find('p', class_='star').text.strip()
                releasetime = item.find('p', class_='releasetime').text.strip()
                score = item.find('p', class_='score').find('i', class_='integer').text.strip() + item.find('p', class_='score').find('i', class_='fraction').text.strip()

                url_movie = f"https://www.maoyan.com/films/{id_movie}"

                dic["电影名称"].append(name)
                dic["主演"].append(star.replace('主演：',''))
                dic["上映时间"].append(releasetime.replace("上映时间：", ''))
                dic["猫眼链接（详情页）"].append(url_movie)
                dic["评分"].append(score)
        else:
            print("未找到 class 为 'board-wrapper' 的 dl 元素。") 

    df = pd.DataFrame(dic)
    df.to_excel('maoyan.xlsx', sheet_name="猫眼电影数据", index = False)


def te():
    print(time.time())
    sign = "1737109328989"
    sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
    print(sign)     

if __name__ == '__main__':
    main()
    # te()


