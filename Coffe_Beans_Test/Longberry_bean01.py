# import required libraries
import cv2
from matplotlib import pyplot as plt

# Read the input image
img = cv2.imread('_Sysroot\Longberry\lb_1600.jpg')

# calculate the histogram for Blue, green ,Red color channels
hist1 = cv2.calcHist([img],[0],None,[256],[0,256]) #blue
hist2 = cv2.calcHist([img],[1],None,[256],[0,256]) # green
hist3 = cv2.calcHist([img],[2],None,[256],[0,256]) # red

# plot the histogram
plt.subplot(3,1,1), plt.plot(hist1, color='b')
plt.subplot(3,1,2), plt.plot(hist2, color='g')
plt.subplot(3,1,3), plt.plot(hist2, color='r')

plt.show()