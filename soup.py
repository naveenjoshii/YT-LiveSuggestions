import requests
from bs4 import BeautifulSoup
import re
import wikipedia
search = "Machine"
results = 1000 # valid options 10, 20, 30, 40, 50, and 100

page = requests.get(f"https://www.google.com/search?q={search}&num={results}")
soup = BeautifulSoup(page.content, "html5lib")
res = []
links = soup.findAll("a")
for link in links :
    link_href = link.get('href')
    if "url?q=" in link_href and not "webcache" in link_href:
        val = link.get('href').split("?q=")[1].split("&sa=U")[0]
        res.append(val)
result = ""
try:
    result = wikipedia.summary(search, sentences = 2)
    print(result)
except:
    print("No results found in wikipedia! ")















# import requests
# from fake_useragent import UserAgent
# from bs4 import BeautifulSoup
#
# ua = UserAgent()
# query = 'Deep Learning'
# number_result = 5
# google_url = "https://www.google.com/search?q=" + query + "&num=" + str(number_result)
# response = requests.get(google_url, {"User-Agent": ua.random})
# soup = BeautifulSoup(response.text, "html.parser")
#
# result_div = soup.find_all('div', attrs = {'class': 'ZINbbc'})
#
# links = []
# titles = []
# descriptions = []
# for r in result_div:
#     # Checks if each element is present, else, raise exception
#     try:
#         link = r.find('a', href = True)
#         title = r.find('div', attrs={'class':'vvjwJb'}).get_text()
#         description = r.find('div', attrs={'class':'s3v9rd'}).get_text()
#
#         # Check to make sure everything is present before appending
#         if link != '' and title != '' and description != '':
#             links.append(link['href'])
#             titles.append(title)
#             descriptions.append(description)
#     # Next loop if one element is not present
#     except:
#         continue
# import re
#
# to_remove = []
# clean_links = []
# for i, l in enumerate(links):
#     clean = re.search('\/url\?q\=(.*)\&sa',l)
#
#     # Anything that doesn't fit the above pattern will be removed
#     if clean is None:
#         to_remove.append(i)
#         continue
#     clean_links.append(clean.group(1))
#
# # Remove the corresponding titles & descriptions
# for x in to_remove:
#     del titles[x]
#     del descriptions[x]
#
# for i in range(len(titles)):
#     print(titles[i])
#     print(descriptions[i])
#     print(clean_links[i])
#     print("===============")
