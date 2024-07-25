import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Kenton.html'
position = 18  
repeat_times = 7  

def get_nth_link(url, position, ctx):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    return tags[position - 1].get('href', None) 
 
current_url = url
for i in range(repeat_times):
    next_url = get_nth_link(current_url, position, ctx)
    print("Retrieving:", next_url)
    current_url = next_url

last_name = current_url.split('_')[-1].split('.')[0]
print("Last name found:", last_name)


