from PIL import Image
import urllib, cStringIO
import random
import sys


class ImageEd(object):
   	def __init__(self, argv):
        	parts = {}

        	for i in range(1,len(argv),2):
            		parts[sys.argv[i]] = sys.argv[i+1]
        
        	if '-f' in parts.keys():
            		self.input_file = parts['-f']
            		self.save_file = self.input_file 
            		self.img = Image.open(self.input_file)

        	if '-u' in parts.keys():
            		self.input_url = parts['-u']
            		p = self.input_url.split('/')
            		self.save_file = p[len(p)-1]
            		self.img =  Image.open(cStringIO.StringIO(urllib.urlopen(self.input_url).read()))

        	if '-s' in parts.keys():
            		self.save_file = parts['-s']
            		self.save = True
        	else:
            		self.save = False

        	if '-show' in parts.keys():
            		self.show = parts['-show']
            		if self.show == "1" or self.show == "True":
                		self.show = True
            		else:
            			self.show = False
            
        	self.width = self.img.size[0]
        	self.height = self.img.size[1]

        	if self.save:
            		self.img.save(self.save_file)

        	if self.show:
            		self.img.show()

    	def glass_effect(self, img = None , distance = 5):
        	if img == None:
            		img = self.img
        	nums = [x for x in range(i-distance, i+distance) if x >=0]
        	choice = random.choice(nums)
        	for x in range(distance, self.width-distance):
            		for y in range(-distance, self.height-distance):
                		for i in range(-distance, distance):
                    			for j in range(-distance, distance):
                        			pix = img.getpixel((x+i, y+j))
                        			r = choice[0]
                        			g = choice[1]
                        			b = choice[2]
                		img.putpixel((x,y),(r,g,b))
        	return self.img       

                
    	def flip(self, img=None):
        	if img == None:
            		img = self.img
        	for x in range(self.width):
            		for y in range(self.height):
                		pixel = self.height - y
                		y = pixel
        	return self.img          
                
    	def posterize(self, img=None, snapVal = 50):
        	if img == None:
            		img = self.img
        	for x in range(self.width):
            		for y in range(self.height):
                		rgb = img.getpixel((x,y))
                		r = rgb[0]
                		g = rgb[1]
                		b = rgb[2]
                
                		r = snap_color(r, snapVal)
                		g = snap_color(g, snapVal)
                		b = snap_color(b, snapVal)
                
                	img.putpixel((x,y), rgb)            
        	return self.img 
    
    	def snap_color(self,color,snap_val):
        	color = int(color)
        	m = color % snap_val
        	if m < (snap_val // 2):
            		color -= m
        	else:
            		color += (snap_val - m)
        	return int(color)    
    
    	def blur(self, img=None, blur_power = 5):
        	if img == None:
            	img = self.img
        	r = 0
        	g = 0
        	b = 0
        	d = 2*blur_power * 2*blur_power
        	for w in range(blur_power, self.width-blur_power):
            		for x in range(blur_power, self.height-blur_power):
                		for y in range(-blur_power, blur_power):
                    			for z in range(-blur_power, blur_power):
                        			pix = imgNew.getpixel((w+y, x+z))
                        			r += pix[0]
                        			g += pix[1]
                        			b += pix[2]
                		imgNew.putpixel((w,x), (int(r/d), int(g/d), int(b/d)))
                		r = 0
                		g = 0
                		b = 0        
        	return self.img       
                        

	def solarize(self, img=None, intensity = 150):
        	if img == None:
            	img = self.img
        	for x in range(self.width):
		    	for y in range(self.height):
                		tot = img.getpixel((x,y))
                		r = tot[0]
                		g = tot[1]
                		b = tot[2]
			
			    	if r < intensity:
				    	r = intensity - r
			    	else:
				    	r = r + intensity
			    	if g < intensity:
				    	g = intensity - g
			    	else:
				    	g = g + intensity
			    	if b < intensity:
				    	b = intensity - b
			    	else:
				    	b = b + intensity
                    
                		img.putpixel((x, y), (tot))
        	return self.img
    
   

    """
    Warhole Effect code cited from
    http://stackoverflow.com/questions/2337110/jython-image-manipulation
    """       
    
    	def warholeEffect(self, img = None):
        	if img == None:
            		img = self.img
        	imgEdge=makeEmptyPicture(getWidth(img),getHeight(img))
        	for x in range (0, getWidth(img)-1):
            		for y in range (0, getHeight(img)-1):
                	here=getPixel(imgEdge,x,y)
                	down = getPixel(img,x,y+1)
                	right = getPixel(img, x+1,y)
                	hereL=(getRed(here)+getGreen(here)+getBlue(here))/3
                	downL=(getRed(down)+getGreen(down)+getBlue(down))/3
                	rightL=(getRed(right)+getGreen(right)+getBlue(right))/3
                	if abs (hereL-downL)>100 and abs(hereL-rightL)>100:
                    		setColor(here,black)
                	if abs (hereL-downL)<=100 or abs(hereL-rightL)<=100:
                    		setColor(here,white)
        	img = Warholize(imgEdge)
        	return self.img  
    
	def Warholize(imgEdge):
        	w= getWidth(imgEdge)
        	h= getHeight(imgEdge)
        	imgNew= makeEmptyPicture(w, h)
        	for x in range(0,w/2):
            		for y in range (0,h/2):
                		px=getPixel(imgEdge,x,y)
                		r=getRed(px)
                		pxNew=getPixel(imgNew,x,y)
                		if r >0:
                    			setColor(pxNew,blue)
                		else:
                    			setColor(pxNew,yellow)
        	for x in range (w/2,w):
            		for y in range (h/2,h):
                		px=getPixel(imgEdge,x,y)
                		r=getRed(px)
                		pxNew=getPixel(imgNew,x,y)
                		if r >0:
                    			setColor(pxNew,yellow)
                		else:
                    			setColor(pxNew,blue)

        	for x in range(0,w/2):
            		for y in range (h/2,h):
                		px=getPixel(imgEdge,x,y)
                		r=getRed(px)
                		pxNew=getPixel(imgNew,x,y)
                		if r >0:
                    			setColor(pxNew,green)
                		else:
                    			setColor(pxNew,red)
            
		for x in range (w/2,w):
        		for y in range (0,h/2):
                		px=getPixel(imgEdge,x,y)
                		r=getRed(px)
                		pxNew=getPixel(imgNew,x,y)
                		if r >0:
                    			setColor(pxNew,red)
                		else:
                    			setColor(pxNew,green)
        	return imgNew       
