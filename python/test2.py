import cv2

cam = cv2.VideoCapture(0)
cam.open(0)

# max. 10 retries
for i in range (10):
    ret, img = cam.read()
    if ret:
        break
else:
    # capture failed even after 10 tries
    raise MyExceptiom("Video driver does not like me.")
