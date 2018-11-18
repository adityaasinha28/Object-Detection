import cv2
import numpy as np
import os

#path='C:\\Users\\AdityaSinha\\Desktop\\TrafficVideos\\YOLOoutput\\vid1\\0000000000.png'

def processImages(dir):
	num=len(os.listdir(dir))
	save_path=dir+'\\image_data.txt'
	save_dir=dir+'\\bbArea'
	if not os.path.exists(save_dir):
		os.makedirs(save_dir)
	file=open(save_path,'w')
	for i in range (0,num):
		l=str(i)
		while(len(l)<10):
			l='0'+l
		path=dir+'\\'+l+'.png'
		im=cv2.imread(path,1)

		h,w=im.shape[:2]
		frame = np.zeros(im.shape[:2],np.uint8)
		mask=np.zeros((h+2,w+2),np.uint8)
		for i in range(0,im.shape[0]):
			for j in range(0, im.shape[1]):
				if( im[i,j,0]==255 and im[i,j,1]==0 and im[i,j,2]==255):
					frame[i,j]=255
				else:
					frame[i,j]=0
		temp=frame.copy()

		cv2.floodFill(temp,mask,(0,0),255)
		temp_inv=cv2.bitwise_not(temp)
		im_out=frame | temp_inv
		fgpix=np.sum(im_out==255)
		bgpix=np.sum(im_out==0)
		rtio=fgpix/(fgpix+bgpix)
		file.write(l+' '+str(fgpix)+' '+str(bgpix)+' '+str(rtio)+'\n')
		cv2.imwrite(save_dir+'\\'+l+'.png',im_out)
		print(l)
#		cv2.imshow('frame',im_out)
#		cv2.imshow('image',im)
#		cv2.waitKey(0)
#		cv2.destroyAllWindows()
	file.close()


dir =input("Enter directory address for input images: ")
processImages(dir)
