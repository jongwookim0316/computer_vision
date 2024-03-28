import cv2 as cv
import sys


# 영상에 도형을 그리고 글씨 쓰기 1
img = cv.imread("./image/apples.jpg")

if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

cv.rectangle(img, (290,780), (620,950), (0,0,255), 2)
cv.putText(img, "apple", (290,770), cv.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2)

cv.imshow("Draw", img)

cv.waitKey()
cv.destroyAllWindows()


