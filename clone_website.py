from urllib import response
import urllib.request

c = open("clone.html", 'w' )
def clone(url):
    response = urllib.request.urlopen(url)
    html = response.read()
    html = html.decode()
    print(html , file=c )

clone("https://www.geeksforgeeks.org/python-programming-language/")