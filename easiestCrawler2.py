# 웹 크롤링에 도움 줄 모듈 추가하기
import urllib.request
from bs4 import BeautifulSoup
import time

# 기사목록 가져오기
  # 크롤링 하고 싶은 URL을 넣자
  # 네이버 뉴스로 해보자
url ="https://news.naver.com" 

  # URL을 열면 나오는 홈페이지 내용
response = urllib.request.urlopen(url)

# html.parser를 이용해 기사를 끌어오자
soup = BeautifulSoup(response, "html.parser")
lists = soup.find_all("a", attrs={"class" : "nclicks(hom.headcont)" })

# 기사 하나씩 가져오자
for list in lists:
  # article = list.select(".newsnow_tx_inner a")
  # 제목
  print("제목 : ", list)
  # 기사 링크 가져와서
  url_article = list.attrs["href"]
  # 링크로 기사 열어보기
  response = urllib.request.urlopen(url_article)
  soup_article = BeautifulSoup(response, "html.parser")
  content = soup_article.select_one("#articleBodyContents")

  # 사람이 읽을 수 있게 가공합시다
  output = ""
  for item in content.contents:
    stripped = str(item).strip()
    if stripped == "":
      continue
    if stripped[0] not in ["<", "/"]:
      output += str(item).strip()
  output.replace("&apos;", "")
  print(output.replace("본문 내용TV플레이어", ""))

  # 5초 대기 -> 왜 대기할까요??
  time.sleep(5)