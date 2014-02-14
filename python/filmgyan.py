# required 
import urllib
import urllib2
import re

# test-link [reset this as your target directory]
main_url = 'http://filmygyan.in/tamannah-bhatia-spotted-sizzling-hot-at-tv-channel-launch/'

# page source data of test-link page
data = urllib2.urlopen(main_url).read()

# to extract data inside <div class="counter">......</div>
start = data.find('<div class="counter">')
last  = data.find('</div>',start)
inner = data[start+len('<div class="counter">'):last]
# variable 'inner' is inside data of that 'div'
# in this case it is, 'Picture 1 of 20'

# for extracting, total number of pictures
total = re.findall(r'\d+',inner)[1]
# here, it will return 20

# now, they have picture in a 'div' tag, with class attr as 'pic'(see page source)
first = data.find('<div class="pic">')
end   = data.find('</div>',first)
text  = data[first+len('<div class="pic">'):end]


f_imgsrc = text.find('"')
l_imgsrc = text.find('"',f_imgsrc+1)
img_src  = text[f_imgsrc+1:l_imgsrc]

# counting variables
number = 1
remain = int(total)-number

while remain>=0:
        first = data.find('<div class="pic">')
        end   = data.find('</div>',first)
        text  = data[first+len('<div class="pic">'):end]

        f_imgsrc = text.find('"')
        l_imgsrc = text.find('"',f_imgsrc+1)
        img_src  = text[f_imgsrc+1:l_imgsrc]
        # img_src contains img-src value

        # downlading image
        urllib.urlretrieve(img_src,'image_%d.jpg'%number)
        print 'downloaded...image %d, there are %d more ' %(number, remain)

        # redirecting to new page because, when you click 'next' button,
        # it opens a new page and then performs the same as we have done.
        # and searching the next page's link the 'div' tag with class attr as 'next'

        f_source = data.find('<div class="next">')
        l_source = data.find('</div>',f_source)
        t_source = data[f_source+len('<div class="next">'):l_source]


        f_data = t_source.find('href="')
        l_data = t_source.find('"',f_data+6)

        # link for the new page (new_url)

        new_url = t_source[f_data+len('href="'):l_data]

        # page source data of the new page

        data = urllib2.urlopen(new_url).read()

        # updating counter variables
        number = number+1
        remain = remain-1