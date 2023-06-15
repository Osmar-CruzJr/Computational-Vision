import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('_Sysroot\Premium\P_1600.jpg')
cv.imshow('Premium', img)

color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])

plt.title('Colour Histogram of a Premium Bean')
plt.xlabel('Colour Values')
plt.ylabel('# of pixels')
plt.show()