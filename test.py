# __author__ = 'traitravinh'
import urllib, urllib2, re, os, sys, requests
from bs4 import BeautifulSoup
import httplib

homelink = 'http://xemphimso.com/'
logo = 'http://xemphimso.com/img/LogoNoel.png'
searchlink = 'http://xemphimso.com/tim-kiem/'

def GetContent(url):
    req = urllib2.Request(url)
    req.add_unredirected_header('User-agent','Mozilla/5.0')
    try:
        response = urllib2.urlopen(req).read()
    except urllib2.HTTPError, e:
        response = e.getcode()
    return response


def index(url):
    soup = BeautifulSoup(GetContent(url),"html.parser")
    for item in BeautifulSoup(str(soup('ul',{'class':'cfv'})[0]),"html.parser")('li'):
        isoup = BeautifulSoup(str(item),"html.parser")
        ititle = isoup('a')[0]['title']
        ilink = isoup('a')[0]['href']
        img = isoup('img')[0]['src']
        print "get file for ", ititle
        video(ilink)
     
def video(url):
    html = GetContent(url) 
    tempLink = re.compile('<a class="btn-watch" href="(.+?)"').findall(html)
    verify = "javascript:alert"
    confirm = [x for x in tempLink if verify in x] 
    if len(confirm) == 0:
     link = GetContent(tempLink[0])
     vlinks = re.compile('</script><script type="text/javascript" src="(.+?)"></script>').findall(link)
     subvlinks = GetContent(vlinks[0])
     if subvlinks != 404:
       filelink = re.compile('"file":"(.+?),"label"').findall(subvlinks)
       print len(filelink)
       print filelink
       #if len(filelink)==0:
       # filelink = re.compile('"file":"(.+?)","').findall(subvlinks)

       if len(filelink)>=1:
          flinks = filelink[len(filelink)-1].replace('\\','').strip('"')
       else:
          flinks = filelink[0].replace('\\','').strip('"')

       print flinks 

url = "http://xemphimso.com/xem-phim-chieu-rap.html"
index(url)
