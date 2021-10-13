import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    cv2.imshow(u'Capture', frame)
    key = cv2.waitKey(1)
    if key & 0xff == ord('q') or key == 27:
        print(frame.shape, ret)
        break

cap.release()
cv2.destroyAllWindows()

'''
1、cap = cv2.VideoCapture(0)
VideoCapture()中参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频，
如cap = cv2.VideoCapture("…/test.avi")

2、ret,frame = cap.read()
cap.read()按帧读取视频，ret,frame是获cap.read()方法的两个返回值。其中ret是布尔值，
如果读取帧是正确的则返回True，如果文件读取到结尾，它的返回值就为False。frame就是每一帧的图像，是个三维矩阵。

3、cv2.waitKey(1)，waitKey（）方法本身表示等待键盘输入，
参数是1，表示延时1ms切换到下一帧图像，对于视频而言；
参数为0，如cv2.waitKey(0)只显示当前帧图像，相当于视频暂停,；
参数过大如cv2.waitKey(1000)，会因为延时过久而卡顿感觉到卡顿。
c得到的是键盘输入的ASCII码，esc键对应的ASCII码是27，即当按esc键是if条件句成立

4、调用release()释放摄像头，调用destroyAllWindows()关闭所有图像窗口。

5、cv.waitKey(delay) : 
可以用 cv.waitKey(delay) 函数延迟窗口显示时间。其中参数dealy表示要延迟的毫秒数。
由于操作系统是多线程执行，所以严格来说dealy表示最少延迟多少毫秒。
delay 默认值为 0，当 dealy <=0 时，表示永久延迟，直到键盘按下任意键。该函数会返回按键的  ASCII 值，
如果在dealy值期间一直没有按，则返回 -1。

6、& 0xff ：
在某些系统中，返回的键盘值可能不是ASCII编码的，所以通过与运算只取字符最后一个字节。

7.ord('a')
返回a的ASCII或者Unicode编码
'''
