#import PIL
from PIL import Image
import PIL.ImageOps
import PIL.ImageEnhance

img_dir = '/var/www/images/'


for i in range(1,8):
	img_tag = 'A4_'+str(i)+'_resizing'
	img_name = img_dir + img_tag + '.PNG'
	img = Image.open(img_name)
	convrt = PIL.ImageEnhance.Color(img)
	img = convrt.enhance(3.0)

	w = img.size[0]
	h = img.size[1]
	
	for j in range(0, 4):
		tmp = img.crop((0, j*(h/4), w, (j+1)*(h/4)))
		tmp = tmp.resize((w/2, h/8), Image.ANTIALIAS)
		#tmp = PIL.ImageOps.invert(tmp)
		
		if tmp.mode == 'RGBA':
			r,g,b,a = tmp.split()
			rgb_img = Image.merge('RGB', (r,g,b))

			tmp = PIL.ImageOps.invert(rgb_img)

			r2, g2, b2 = tmp.split()
			tmp = Image.merge('RGBA', (r2,g2,b2,a))

		else:
			tmp = PIL.ImageOps.invert(tmp)
		tmp_name = img_dir+'temp/'+img_tag.replace('resizing', 'inv')+'_'+str(j+1)+'.png'
		print(tmp_name)
		tmp.save(tmp_name)

