import re
import urllib2
import urllib

# add the main desired link here
_url_ = 'http://listcovery.com/funny-look-alikes-40-pics/'

def foo(url,page):
    if(page==1): 
        pass
    else: 
        url = url + str(page) + '/'

    data = urllib2.urlopen(url).read()

    start = data.find('<div class="post-content">')
    last  = data.find('</div>',start)  
    inner = data[start+len('<div class="counter">'):last]
    total = re.findall(r'\d+',inner)[1]

    src = inner.find('src') 
    img_s = inner.find('"',src) + 1
    img_e = inner.find('"',img_s)
    img_src = inner[img_s:img_e]

    # downlading image
    urllib.urlretrieve(img_src,'image_%d.jpg'%(page))
    print 'downloading image number %d' %(page)


data = urllib2.urlopen(_url_).read()

start = data.find('<div class="post-content">')
last  = data.find('</div>',start)
inner = data[start+len('<div class="counter">'):last]
total = re.findall(r'\d+',inner)[2]

#print total

for i in range(1,int(total)+1):
    foo(_url_,i)
    i = i+1