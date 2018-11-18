import os
import subprocess
import cv2

testpath='/data2/SampleImages'

total=len(os.listdir(testpath))
print total
file=open('/home/adityaasinha28/VidSlices/areainfo.txt','w')
for i in range(0,total):    
	l=str(i)
	while(len(l)<10):
		l='0'+l
	print('Current: '+l+'/'+str(total)) 
	im_no=l
	im=cv2.imread(testpath+'/'+im_no+'.png')
	x,y=im.shape[:2]
	cmd='./darknet detect cfg/yolov3.cfg yolov3.weights '+testpath+'/'+im_no+'.png > outfile.txt'
	os.system(cmd)
	fp=open('/home/adityaasinha28/yolofortraffic/darknet/outfile.txt','r')
	sum=0
	for line in fp:
		if (line.find('Objects') != -1):
			objects_str=line.split(':')
			print('objects: '+objects_str[1])
		if (line.find('BBox_data') != -1):
			splt=line.split(' ')
			sum=sum+x*y*float(splt[3])*float(splt[4])
	file.write(str(sum)+'\n')
	print(sum)		
	fp.close()
file.close()
