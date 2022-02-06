import cv2
import matplotlib.pyplot as plt
import numpy as np

imgs = [] 
for i in range(1,300):
    try:
        path = f'8주차_10주차_11주차_12주차_merged_page-{i:04d}.jpg'
        imgfile = cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_COLOR)
        
        #imgfile = cv2.imread()
        imgfile = 255 - imgfile
        imgs.append(imgfile) 
        
    except:
        break

cnt = 40
for img in imgs: 
    for i in range(1125):
        for j in range(2000):
            a = np.where((img[i,j]>150) & (img[i,j]<220))
            if len(a[0])==3:
                img[i,j] = np.array([255,255,255])
    cnt += 1
    cv2.imwrite(f'inversion{cnt:04d}.jpg', img)
            

        
        
#plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.xticks([])
#plt.yticks([])
#plt.show()



#cv2.waitKey(0)
#cv2.destroyAllWindows()
