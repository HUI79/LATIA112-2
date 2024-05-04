# -*- coding: utf-8 -*-
"""HW2_request.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18BItnMXiKPzkHHKRwfDb8XWrbPEZhu5V
"""

# Commented out IPython magic to ensure Python compatibility.
# %%shell
# # Ubuntu no longer distributes chromium-browser outside of snap
# #
# # Proposed solution: https://askubuntu.com/questions/1204571/how-to-install-chromium-without-snap
# 
# # Add debian buster
# cat > /etc/apt/sources.list.d/debian.list <<'EOF'
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster.gpg] http://deb.debian.org/debian buster main
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-buster-updates.gpg] http://deb.debian.org/debian buster-updates main
# deb [arch=amd64 signed-by=/usr/share/keyrings/debian-security-buster.gpg] http://deb.debian.org/debian-security buster/updates main
# EOF
# 
# # Add keys
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DCC9EFBF77E11517
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 648ACFD622F3D138
# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 112695A0E562B32A
# 
# apt-key export 77E11517 | gpg --dearmour -o /usr/share/keyrings/debian-buster.gpg
# apt-key export 22F3D138 | gpg --dearmour -o /usr/share/keyrings/debian-buster-updates.gpg
# apt-key export E562B32A | gpg --dearmour -o /usr/share/keyrings/debian-security-buster.gpg
# 
# # Prefer debian repo for chromium* packages only
# # Note the double-blank lines between entries
# cat > /etc/apt/preferences.d/chromium.pref << 'EOF'
# Package: *
# Pin: release a=eoan
# Pin-Priority: 500
# 
# Package: *
# Pin: origin "deb.debian.org"
# Pin-Priority: 300
# 
# 
# Package: chromium*
# Pin: origin "deb.debian.org"
# Pin-Priority: 700
# EOF
# 
# # Install chromium and chromium-driver
# apt-get update
# apt-get install chromium chromium-driver
# 
# # Install selenium
# pip install selenium

!pip install selenium==4.3.0

pip install beautifulsoup4

# 引入所需套件
import requests
from bs4 import BeautifulSoup
import pandas as pd
from google.colab import files

# 定義要爬取的網址
url = 'https://travel.ettoday.net/category/%E9%9F%93%E5%9C%8B%E6%97%85%E9%81%8A/'

# 使用requests庫發送HTTP GET請求,獲取網頁內容
web = requests.get(url)

# 使用BeautifulSoup解析網頁內容
soup = BeautifulSoup(web.text, "html.parser")

# 尋找具有class名稱"part_pictxt_1"的元素
container = soup.find("div", class_="part_pictxt_1")

# 查找所有具有"a"標籤且屬性"itemprop"為"url"的元素
headline_a = container.find_all("a", itemprop="url")
# 查找所有具有"em"標籤且屬性"itemprop"為"datePublished"的元素
datePublished_em = container.find_all("em", itemprop="datePublished")

# 建立兩個空列表
headline=[]
datePublished=[]

#將每個元素h的text存至headline中，並列印
for h in headline_a:
    headline.append(h.string)
    print(h.string, "\n")

#將每個元素d的string存至datePublished中
for d in datePublished_em:
    datePublished.append(d.string)

#將兩個列表寫入DataFrame
df = pd.DataFrame({'日期':datePublished,'新聞標題':headline})
# 將DataFrame寫入CSV檔案
df.to_csv('travel_news.csv', index=False, encoding='utf-8-sig')
files.download('travel_news.csv')