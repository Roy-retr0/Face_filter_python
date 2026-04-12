import cv2 as cv

class CameraManager():
    def __init__(self):
        self.cap = cv.VideoCapture(0)
    
    def get_frame(self):
        ret,frame = self.cap.read()
        if not ret:
            return None
        return cv.flip(frame,1)

    def release(self):
        self.cap.release()
        cv.destroyAllWindows()
         



'''class CameraManager():
    def __init__(self, camera_index=0):
        self.cap = cv.VideoCapture(camera_index)
    def get_frame(self):
        ret, frame = (self.cap.read())
        if not ret:
            False, Exception("Could not read frame from camera")
        return(frame)
    def release(self):
        self.cap.release
        cv.destroyAllWindows()'''