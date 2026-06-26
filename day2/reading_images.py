import cv2;

# Read an image
# img = cv2.imread('Resources/lena.png')
# print(img)
# cv2.imshow('Output', img)
# cv2.waitKey(0)

# reading video
# video = cv2.VideoCapture('Resources/elon.mp4')
# while True:
#     success, img = video.read()
#     cv2.imshow('Video', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# reading webcam
capture=cv2.VideoCapture(0)
capture.set(3,640) # width
capture.set(4,480) # height

while True:
    success, img = capture.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break