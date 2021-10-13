import cv2
import numpy as np

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    # 对图像进行翻转
    (h, w) = image.shape[:2]
    (cX, cY) = (w / 2, h / 2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

cascPath = r'D:\Python_project\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
cap = cv2.VideoCapture(0)



while (True):
    ret, img = cap.read()
    image = rotate_bound(img, 90)
    faces = faceCascade.detectMultiScale(image, 1.2, 4, cv2.CASCADE_SCALE_IMAGE, (20, 20))
    for (x, y, w, h) in faces:
        img = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow('Detect faces', image)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q') or key == 27:
        break

cv2.destroyAllWindows()
cap.release()

'''
A.faceCascade.detectMultiScale()
1.image表示的是要检测的输入图像
2.objects表示检测到的人脸目标序列
3.scaleFactor表示每次图像尺寸减小的比例
4.minNeighbors表示每一个目标至少要被检测到3次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸),
5.minSize为目标的最小尺寸
6.maxSize为目标的最大尺寸
适当调整4,5,6两个参数可以用来排除检测结果中的干扰项。

B.cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)画出矩行
参数解释
第一个参数：img是原图
第二个参数：（x，y）是矩阵的左上点坐标
第三个参数：（x+w，y+h）是矩阵的右下点坐标
第四个参数：（0,255,0）是画线对应的rgb颜色
第五个参数：2是所画的线的宽度,-1表示填满矩形

C.img.shape[0]、[1]、[2]到底代表什么
img.shape[ : 2] 表示取彩色图片的长、宽。
img.shape[ : 3] 则表示取彩色图片的长、宽、通道。

关于img.shape[0]、[1]、[2]
img.shape[0]：图像的垂直尺寸（高度）
img.shape[1]：图像的水平尺寸（宽度）
img.shape[2]：图像的通道数

在矩阵中，[0]就表示行数，[1]则表示列数。
'''
