import numpy as np
import cv2
import os

fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()

def processImages(dir):
	pw_dir=os.getcwd()
	save_dir=pw_dir+'\\TrafficVideos'
	if not os.path.exists(save_dir):
		os.makedirs(save_dir)
	file=open(save_dir+'\\image_info.txt','w')
	num_Imgs=len(os.listdir(dir))
	print(num_Imgs)
	img_list=list()
	for i in range(0,num_Imgs):
		l=str(i)
		while(len(l)<10):
			l='0'+l
		img_list.append(l)
		print(dir+'\\\\'+img_list[i]+'.png')
		frame=cv2.imread(dir+'\\\\'+img_list[i]+'.png')
		fgmask=fgbg.apply(frame)
		#cv2.imshow('Frame',frame)
		#cv2.waitKey(0)
		#cv2.imshow('Mask',fgmask)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
		fg_pix,bg_pix,fgbg_ratio=imageData(frame,fgmask)
		#saveImage(save_dir,img_list[i],frame,fgmask)
		file.write(img_list[i]+' '+str(fg_pix)+' '+str(bg_pix)+' '+str(fgbg_ratio)+'\n')
	file.close()
		
def imageData(img,mask):
	fg_pix=np.sum(mask==255)
	bg_pix=np.sum(mask==0)
	fgbg_ratio= fg_pix/(fg_pix+bg_pix)
	return(fg_pix,bg_pix,fgbg_ratio)

def saveImage(save_dir,img_name,img,mask):
	fg_img=np.zeros(img.shape)
	fg_img[:,:,0]=np.multiply(img[:,:,0],mask)
	fg_img[:,:,1]=np.multiply(img[:,:,1],mask)
	fg_img[:,:,2]=np.multiply(img[:,:,2],mask)
	cv2.imwrite(save_dir+'\\'+img_name+'_fg_img.jpg',fg_img)
	cv2.imwrite(save_dir+'\\'+img_name+'_mask.jpg',mask)
	
dir= input("Enter directory address for input images:")
processImages(dir)		
