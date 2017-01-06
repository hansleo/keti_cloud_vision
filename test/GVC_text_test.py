import sys
import os
import textindex

sys.path.insert(0, '/home/leo/cloud-vision/python/text')
img_dir = '/home/leo/cloud-vision/pics/'

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
	print('\nimage name: ', img)
	for img_idx in range(1, len(result[img])):
		print('\t', result[img][img_idx]['description'])


