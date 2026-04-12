# import numpy
# import mediapipe

import cv2 as cv

from camera_manager import CameraManager
from face_detector import FaceDetector
from filters.base_filters import BaseFilter
from filters.filtro_nariz import NoseDotFilter
from filters.filtro_bigote import Mustache

camera = CameraManager()
detector = FaceDetector()
nose = NoseDotFilter()
mostacho = Mustache()

# Iniciamos el programa

while True:
    frame = camera.get_frame()
    frame = detector.detect(frame)   # primero procesas
    if detector.results.multi_face_landmarks:
        frame = nose.apply(frame, detector.results.multi_face_landmarks[0].landmark)
        frame = mostacho.apply(frame, detector.results.multi_face_landmarks[0].landmark)
    cv.imshow("Camera", frame)       # luego muestras UNA sola vez
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()


'''
while True:
    frame = camera.get_frame()
    cv.imshow("Camera: ",frame)
    
    if cv.waitKey(1) & 0xff == ord('q'):
        break
    
    frame = detector.detect(frame)
    cv.imshow("Camera", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
'''



'''
import cv2
import mediapipe
from camera_manager import CameraManager
from face_detector import FaceDetector
from filters.filtro_nariz import FiltroNariz

cam = CameraManager(camera_index=0)
detector = FaceDetector(is_static=False, max_num_faces=1, use_landmarks=True, min_confidence_detection=0.5, min_confidence_tracking=0.5)

try:
    while True:
        frame = cam.get_frame()
        output_frame, landmarks = detector.detect(frame)
        cv2.imshow("Mallas", output_frame)
        
        key = cv2.waitKey(1)
        if key != -1 and chr(key) == 'q':
            break

finally:
    cam.release()
'''