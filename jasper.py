from SimpleCV import * #import SimpleCV

cam = Camera()
prev = cam.getImage() #previous camera image
size = prev.size() #print size of previous image
print(size)
while True:
  cropped = prev  #makes a red box for user to interface with
	cropped=cropped.getSkintoneMask(0) # make skin white, background black
	cropped=cropped.erode(6) #fuzzy
	cropped=cropped.dilate(3) #fuzzy
	cropped.dl().rectangle((400,0), (240,480), Color.RED) #GUI
	blobs = cropped.findBlobsFromMask(cropped) # of the fuzzy picture, make blobs
	blobs.show() #show blobs
	current = cam.getImage()
	fs = current.findMotion(prev, method="LK")
	if fs: #if there's motion
		print "motion found"
	prev = current
