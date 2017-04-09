from random import randint
""" PIL :
from PIL import Image
im = Image.open('gdtst.jpg')
# im = Image.open('tst.png')
data = list(im.getdata())
"""
img = open("tst.pbm")
type = img.readline()
ln = img.readline()
lg = img.readline()
format = img.readline()
if (type != "P6") or (format != "255"):
	print("mauvais format d'image")
data = []
for i in range(int(ln)*int(lg)):
	tmp_data = img.readline()
	tmp = (tmp_data[0:2], tmp_data[4:6], tmp_data[8:10])
	data.append(tmp)
print(data)
def noir_blanc() :
	global data
	for i in range(len(data)):
		p = data[i]
		r = int((p[0]+p[1]+p[2])/3)
		p = (r, r, r)
		data[i] = p
def negatif() :
	global data
	for i in range(len(data)):
		p = data[i]
		p = (255-p[0], 255-p[1], 255-p[2])
		data[i] = p
def seuil() :
	global data
	for i in range(len(data)):
		p=data[i]
		r = int((p[0]+p[1]+p[2])/3)
		if r < 128:
			data[i] = (0, 0, 0)
		else :
			data[i] = (255, 255, 255)
def bruit_L(valeur):
	global data
	for i in range(len(data)):
		p = data[i]
		r = randint(-1,1)*255
		pxl = []
		for k in range(0,3):
			j = int(p[k]+r*(int(valeur)/100))
			if j > 255:
				pxl.append(255)
			elif j < 0 :
				pxl.append(0)
			else:
				pxl.append(j)
		p = (pxl[0], pxl[1], pxl[2])
		data[i]=p
def bruit_C(valeur):
	global data
	for i in range(len(data)):
		p=data[i]
		r=randint(0,2)
		pxl = [0]*3
		for k in range(0,3):
			if k == r:
				j = int(p[k]+255*(valeur/100))
				if j > 255:
					pxl[k] = 255
				else:
					pxl[k]=j
			else:
				j = int(p[k]-255*(valeur/100))
				if j < 0:
					pxl[k] = 0
				else:
					pxl[k] = j
		p = (pxl[0], pxl[1], pxl[2])
		data[i] = p
valeur = int(input("?"))
bruit_C(valeur)
# print(data)
im.putdata(data)
# im.save("final.png", "PNG")
im.show()
os.system("pause")
