import cv2 as cv
import sys

# 마우스 드래그로 도형크기 조절하기
img = cv.imread("./image/soccer.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

def draw(event, x ,y, flags, param):
    global ix,iy
 
    if event == cv.EVENT_LBUTTONDOWN:
          ix,iy=x,y

    elif event == cv.EVENT_RBUTTONDOWN:
          cv.rectangle(img, (ix,iy), (x,y), (0,0,255), 2)

    cv.imshow("Drawing", img)

cv.namedWindow("Drawing")
cv.imshow("Drawing", img)

cv.setMouseCallback("Drawing", draw)

while(True):
    if cv.waitKey(1)==ord("q"):
        cv.destroyAllWindows()
        break