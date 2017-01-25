#!/usr/bin/python
#-*-coding:utf8-*-

# Import modules for CGI handling 
import os, sys, json
sys.path.insert(0, '/home/leo/cloud-vision/python/text/')
import cloud_api

img_dir = '/var/www/images/'


def targeting():
	imgs = list()
	for root, dirs, files in os.walk(img_dir):
		for img in files:
			imgs.append(img_dir+img)
	return imgs


def extract_texts(target):
	target.sort()
	texts = list()
	img_list = list()
	result = dict()

	vision_api = textindex.VisionApi()
	for start in range(0, len(target)-(len(target)%5)+1, 5):
		end = start + 5
		if end >= len(target): end = len(target)
		api_json = vision_api.detect_text(target[start:end])
		for img in target[start:end]:
			for img_idx in range(1, len(api_json[img])):
				Json = api_json[img][img_idx]['description'].encode('utf8')
				texts.append(Json.decode('utf-8'))
			result[img.replace(img_dir,'')] = texts
			texts = []
	return result



result = extract_texts(targeting())
with open('result.txt', 'w') as outfile:
	json.dump(result, outfile)
os.chmod('result.txt', 0755)
