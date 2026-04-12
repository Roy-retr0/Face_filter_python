from filters.base_filters import BaseFilter
import cv2 as cv

class Mustache(BaseFilter):
    def __init__(self):
        self.bigote = cv.imread("assets/Mostacho.png", cv.IMREAD_UNCHANGED)

    def apply(self, frame, landmarks):    
        h, w, _ = frame.shape
        labio = landmarks[13]
        boca_l = landmarks[61]
        boca_r = landmarks[291]

        ancho_bigote = int(abs(boca_r.x - boca_l.x) * w * 1.5)
        alto_bigote = int(self.bigote.shape[0] * ancho_bigote / self.bigote.shape[1])
        x = int(labio.x * w)
        y = int(labio.y * h) - 70
        bigote_redim = cv.resize(self.bigote, (ancho_bigote, alto_bigote))
        bgr = bigote_redim[:, :, :3]
        alpha = bigote_redim[:, :, 3]

        y1 = y
        y2 = y + alto_bigote
        x1 = x - ancho_bigote // 2
        x2 = x + ancho_bigote // 2

        region = frame[y1:y2, x1:x2]
        bgr = cv.resize(bgr, (x2-x1, y2-y1))
        alpha = cv.resize(alpha, (x2-x1, y2-y1))
        alpha_norm = alpha / 255.0
        region[:] = (bgr * alpha_norm[:,:,None] + region * (1 - alpha_norm[:,:,None]))
        return frame