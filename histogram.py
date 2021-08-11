import requests
import datetime
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

furl = "http://cse.knu.ac.kr/06_sub/02_sub.html?page=%d&key=&keyfield=&category=&bbs_code=Site_BBS_25"
soup = BeautifulSoup(requests.get(furl % 1).content, "html.parser")
pages = soup.find_all("a", class_="paging-arrow")[-1]["href"]
pages = int(pages[6:pages.find("&")])

print("Number of pages: %d" % pages)
print("Crawling...")

freq = {}
for i in range(1, pages + 1):
    soup = BeautifulSoup(requests.get(furl % i).content, "html.parser")
    for row in soup.find_all("tr"):
        if row.find_all("th"):
            continue

        date = row.find_all("td")[3].get_text()
        dow = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")
        freq[dow] = freq.setdefault(dow, 0) + 1

plt.bar(*zip(*freq.items()))
plt.show()
