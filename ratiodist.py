import numpy as np
import matplotlib.pyplot as plt

folders=['10-12-2017-bashyam_circle_ss_nagara', '18-12-17-garuda_mall(6am-10pm)', '18-12-2017-brv_jn(6am-10pm)', '20-12-17-bhashyam_crcl', '22-12-17-dickenson_road(6am-10pm)']
base_dir = "//mnt//c//Users//AdityaSinha//Desktop//FGImages"

data=list()
for i in folders:
	dir=base_dir+'//'+i+'//image_info.txt'
	fl= open(dir,'r')
	for line in fl:
		info=line.split()
		data.append(info[3])
	j=0
	for item in data:
		data[j]=round(float(item),3)
		j=j+1
	plt.hist(data)
	plt.title(i+'- histogram')
	plt.xlabel('Value')
	plt.ylabel('Frequency')
	plt.show()


