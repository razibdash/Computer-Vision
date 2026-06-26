import cv2;

## resize image

imge=cv2.imread('Resources/lambo.png')
crop_img=imge[0:200,200:500] # cropping image
cv2.imshow('original image',imge)
cv2.imshow('cropped image',crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
