from bs4 import BeautifulSoup

from bs4 import XMLParsedAsHTMLWarning
import warnings

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)




fp = open("joins.xml", "r", encoding="utf-8")
openFile = fp.read()
soup = BeautifulSoup(openFile, 'html.parser')

for data in soup.find_all('item'):
    print("title:", data.title.string)
    print("description:", data.description.string)
