import urllib.request
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_2053737.html'

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

spans = soup.find_all('span')

numbers = [int(span.text) for span in spans]
total_sum = sum(numbers)

print("The sum of all numbers is:", total_sum)