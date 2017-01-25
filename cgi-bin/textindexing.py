#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import json
import os, sys
#sys.path.insert(0, '/home/leo/cloud-vision/python/text/')
#import textindex


img_dir = '/var/www/images/'
form = cgi.FieldStorage() 

def check_items(img_dir):
	imgs = list()
	target = list()
	for root, dirs, files in os.walk(img_dir):
		for img in files:
			imgs.append(img)

	for img in imgs:
		item = img
		if form.getvalue(item):
			target.append(item)
	
	if target == []:
		target = ['upside_2.jpg','tight_1.jpg']
	
	print('<p>selected images : %s</p>'%(target))
	return target

def extract_texts(target):
	text = list()
	img_list = list()
	result = dict()
	print('<p>extracting images : %s</p>'%(target))

	for item in target:
		img = img_dir+item
		img_url = open(img, 'rb').read().encode('base64').replace('\n', '')
		img_tag = '<img src="data:image/jpeg;base64,{0}" alt="" />'.format(img_url)
		
		#print(img_tag)
		img_list.append(img)
	
	print('<p> %s </p>'%(img_list))
	vision_api = textindex.VisionApi()
	api_json = vision_api.detect_text(img_list)
	for img in img_list:
		print('<p> %s </p>'%(img))
		img_url = open(img, 'rb').read().encode('base64').replace('\n', '')
		img_tag = '<img src="data:image/jpeg;base64,{0}" alt="" />'.format(img_url)
		print(img_tag)
		for img_idx in range(1, len(api_json[img])):
			text.append(api_json[img][img_idx]['description'])
		result[img] = text
		text = []
	return result

def from_json(imgs):
	json_data = open('/var/www/cgi-bin/result.txt').read()
	texts = json.loads(json_data)
	print('<table align="left" valign="top" cellpadding="10">')
	for img in imgs:
		print('<tr><td align="center" colspan="2"><h3><br/>%s</h3></td></tr>'% (img))
		img_url = open(img_dir+img, 'rb').read().encode('base64').replace('\n', '')
		img_tag = '<td align="center"><img src="data:image/jpeg;base64,{0}" alt="" style="max-width:auto; height:50%;"/></td>'.format(img_url)
		print(img_tag)
		text = texts[img]
		print('<td>')
		for word in text:
			print(' %s<br/>' %(word))
		print('</td>')
	print('</table>')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Extract Text</title>")
print("</head>")
print("<body>")
print("<h1>Extracting TEXT</h1>")

imgs = check_items(img_dir)
from_json(imgs)
'''
texts = extract_texts(imgs)

for key, val in texts.items():
	print('<p>%s</p>' % key)
	for text in val: 
		print('<p>\t%s</p>' % text)
'''
print("</body>")
print("</html>")
