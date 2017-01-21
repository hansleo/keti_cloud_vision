#!/usr/bin/python
#-*-coding:utf8-*-

import sys, os
sys.path.insert(0, '/home/leo/cloud-vision/python/text')
import textindex
import time
import picamera

pic = '/home/leo/camera/default.jpg'

if len(sys.argv) is 1:
	print '*****'
	print 'A picture has default file name in default path.'
	print ': /home/leo/camera/default.jpg'
	print '*****'

elif len(sys.argv) > 2:
	print 'Insert only the file name with directory where you want to save a picture in'
	print 'default : /home/leo/camera/default.jpg'

else:
	pic = sys.argv[1]



pi_cam =  picamera.PiCamera() 
pi_cam.hflip = True
pi_cam.capture(pic)
print '\n\nA picture was saved at '+pic+'\n\n'

vision_api = textindex.VisionApi()
result = vision_api.detect_text([pic])
for idx in range(1, len(result[pic])):
	print '\t'+result[pic][idx]['description']


