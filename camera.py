import cv2

class Cam:
    def __init__(self):
        # 設定影像的尺寸大小
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
    def opencam(self):
        ret, frame = self.cap.read()
        self.cap.release()
        cv2.destroyAllWindows()
        return frame
        
  # 設定影像的尺寸大小
  

  