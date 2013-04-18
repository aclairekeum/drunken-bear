from SimpleCV import * #import SimpleCV
cam = Camera()
prev = cam.getImage() #previous camera image
size = prev.size() #print size of previous image
print(size)
while True:
	#import pdb
	#pdb.set_trace()
	new = prev  #makes a red box for user to interface with
	new=new.getSkintoneMask(0) # make skin white, background black
	new=new.erode(6) #image processing 1
	new=new.dilate(3) #image processing 2
	blobs = new.findBlobsFromMask(new) # create green outlined blobs GUI layer
	new.dl().rectangle((400,0), (240,480), Color.RED) #add GUI layer
	cropped = new.crop(400,0,240,480) #crop what's in GUI box
	newblobs = cropped.findBlobs()
	print(newblobs)
	if newblobs:
		print(newblobs.coordinates)
		cropped.show() #display what's in box
	#blobs.show() #show blobs
	current = cam.getImage() #get new image
	prev = current #assign variable to reset loop
