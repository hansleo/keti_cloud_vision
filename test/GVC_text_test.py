#Author: Lee, HANDONG(hansleo)

import sys
sys.path.insert(0, '/directory/of/cloud-vision/python/text')
import os
import textindex


img_dir = '/directory/of/images/'

def find_images(img_dir):
	imgs= list()
	for root, dirs, files in os.walk(img_dir):
		for img in files:
			imgs.append(img_dir + img)
	return imgs

imgs = find_images(img_dir)
vision_api = textindex.VisionApi()
result = vision_api.detect_text(imgs)
for img in imgs:
	print('\nimage: ', img)
	for img_idx in range(1, len(result[img])):
		print('\t', result[img][img_idx]['description'])


