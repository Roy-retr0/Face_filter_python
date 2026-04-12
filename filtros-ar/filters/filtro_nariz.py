
from filters.base_filters import BaseFilter
import cv2 as cv

class NoseDotFilter(BaseFilter):
    def apply(self, frame, landmarks):
        h, w, _  = frame.shape
        nose  = landmarks[4]
        x = int(nose.x * w)
        y = int(nose.y * h)
        frame  = cv.circle(frame, (x,y), 10, (0, 0, 255), -1)
        return frame
    
    
        






'''
import cv2
from .base_filters import BaseFilter

class FiltroNariz(BaseFilter):
    def apply(self, frame, landmarks):
        if landmarks and len(landmarks) > 0:
            nose_landmark = landmarks[0]
            h, w = frame.shape[:2]
            x = int(nose_landmark.x * w)
            y = int(nose_landmark.y * h)
            filter_type = "nose"  # Puedes cambiar este valor según el filtro deseado
            
            if filter_type == "nose":
                cv2.circle(frame, (x, y), 8, (50, 0, 50), -1)

'''                