from bs4 import BeautifulSoup
import requests


# Step 1: Get the page content
content = requests.get(url="https://en.wikipedia.org/wiki/Mathematics").text
# print(content)

# Step 2: Extracting the data
soup = BeautifulSoup(content, 'html.parser')
# result = soup.select("li[id^='cite_note']")
paragraphs = soup.select('p')
# print(result)

# Step 3: Saving the data
# with open('citations.txt', 'w') as file:
#     for i in result:
#         file.write(i.get_text() + "\n")

with open('paragraphs.txt', 'w') as file:
    for para in paragraphs[:5]:  # Only the first 5 paragraphs
        para_text = para.get_text()
        file.write(para_text + '\n')
