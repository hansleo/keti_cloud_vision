#!/usr/bin/python3

# Import modules for CGI handling
import time, datetime
import os, sys

#api path
sys.path.insert(0, '/home/leo/cloud-vision/python/text')
#image path
img_dir = '/var/www/images/'

#make a image-file list
def find_images(img_dir):
	imgs= list()
	for root, dirs, files in os.walk(img_dir):
		for img in files:
			if img.lower().find('.jpg') > -1 or img.lower().find('.png') > -1:
				imgs.append(img_dir + img)
	return imgs


print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Image_list</title>")
print("</head>")
print("<body>")
print('<form method="POST" action="/cgi-bin/textindexing.py" target="_blank">')

idx = 0
imgs = find_images(img_dir)
imgs.sort()
print('<table align="left">')
print('<tr>')
#amke radio buttons for image-files to extract texts
for img in imgs:
	idx += 1
	item = img.split('/')[-1]
	print('<td>')
	print('<input type="checkbox" name="%s" value="on" /> %s' % (item, item.split('.')[0]))
	print('</td>')
	if idx % 5 == 0:
		print('</tr><tr>')
print("</tr>")
print('<tr><td><input type="submit" value="Get Texts"  /></td></tr>')
print('</table>')
print("</form>")
print("</body>")
print("</html>")
