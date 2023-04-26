import json
import os
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Sec-Fetch-Site': 'same-origin',
    'Accept-Language': 'zh-TW,zh-Hant;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Sec-Fetch-Mode': 'navigate',
    'Host': 'exam.naer.edu.tw',
    'Origin': 'https://exam.naer.edu.tw',
    'Referer': 'https://exam.naer.edu.tw/searchResult.php',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
}

total_pages = 4767
data_file = "./data.json"

if os.path.exists(data_file):
    with open(data_file, 'r', encoding='utf-8') as f:
        all_data = json.load(f)
    if all_data:
        last_record = all_data[-1]
        last_page = int(last_record['page'])
        start_page = last_page + 1
    else:
        start_page = 1
else:
    all_data = []
    start_page = 1

for page in tqdm(range(start_page, total_pages + 1)):
    data = {
        'page': page,
        'orderBy': 'lastest',
        'selCategory': '0',
        'selTech': '0',
        'chkClass[]': ['15', '16', '17'],
        'keyword': '',
        'selCountry': '',
        'selYear': '',
        'selTerm': '',
        'selType': '',
        'selPublisher': '',
    }

    response = requests.post('https://exam.naer.edu.tw/searchResult.php', headers=headers, data=data)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find_all('tr')
    for row in rows[1:]:
        try:
            cols = row.find_all('td')
            if len(cols) < 11:
                continue
            # Check if the "縣市" column contains invalid data
            city = cols[0].text.strip()
            if "回首頁" in city or "版權所有" in city:
                continue
            test_paper_link = cols[9].find('a')['href'] if cols[9].find('a') else None
            answer_paper_link = cols[10].find('a')['href'] if cols[10].find('a') else None
            if test_paper_link is None and answer_paper_link is None:
                continue
            record = {
                "縣市": cols[0].text.strip(),
                "學校名稱": cols[1].text.strip(),
                "年級": cols[2].text.strip(),
                "學年度": cols[3].text.strip(),
                "領域/群科": cols[4].text.strip(),
                "科目": cols[5].text.strip(),
                "種類": cols[6].text.strip(),
                "版本": cols[7].text.strip(),
                "點閱率": cols[8].text.strip(),
                "下載試卷": urljoin('https://exam.naer.edu.tw', test_paper_link),
                "下載答案": urljoin('https://exam.naer.edu.tw', answer_paper_link),
                "page": page,
            }
            all_data.append(record)
        except:
            pass

    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
