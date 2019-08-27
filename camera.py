import cv2

class Cam:
    def __init__(self):
        # 設定影像的尺寸大小
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    def opencam(self,save):
        ret, frame = self.cap.read()
        if save: 
           cv2.imwrite('./Audience.jpg', frame)
        self.cap.release()
        cv2.destroyAllWindows()
        return frame
    def showcam(self):
        aud = cv2.imread('./Audience.jpg')
        cv2.imshow('My audience', aud)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        