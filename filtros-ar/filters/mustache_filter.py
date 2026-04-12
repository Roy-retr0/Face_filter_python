'''

from .base_filters import BaseFilter
import cv2

class MustacheFilter(BaseFilter):
    def __init__(self, image_path):
        super().__init__()
        self.overlay_rgba = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        
        if self.overlay_rgba is None:
            raise ValueError(f"No se pudo cargar la imagen: {image_path}")
        
        self.overlay_rgba = cv2.cvtColor(self.overlay_rgba, cv2.COLOR_BGRA2RGBA)
        
        self.width = self.overlay_rgba.shape[1]
        self.offset_x = 0
        self.offset_y = 0
    
    def apply(self, frame, landmarks):
        h,w = image_shape[:2]
        x = int(landmarck.x*w)
        y = int(landmark.y*h)
        return x,y
    
    def apply(self, frame, landmarks)
        nose = landmarks[0].landmark[1]
        xnose, ynose = self.landmarck_xtoy(nose,frame.shape)
        ph, ow = self.overlay_rgba.shape[:2]
        scale = self.object_width[:2]
        
        
        new_oh = int(oh*scale)
        new_ = int(ow*scale)

        reazised = cv.resize(self.overlay_rgba, (new_ow, new_oh), interpolation=cv2.INTER_AREA)
        x = xnose - new_ow // 2 + self.offset_x
        y = ynose - new_oh // 2 + self.offset_y

        return
    
    def overlay_rgba_on_bgr(self, frame, overlay_rgba, x, y):
        h, w = frame.shape[:2]
        oh, ow = rgba.shape[:2]

        z1 = max(0, x)
        y1 = max(0, y)


        x2 = min(w, x + ow)
        y2 = min(h, y + oh)

        crop = rgba[(y1-y2):(y2-y1)]

        roi = frame(y1:y2, x2:x1)

        alpha = crop[..., 3:4] / 255.0
        blended = alpha * crop[..., :3] + (1 - alpha) * roi
        rgb = blended.astype(np.uint8)
        frame[y1:y2, x1:x2] = rgb
        return frame    
    '''
    