
import mediapipe as mp
import cv2 as cv

class FaceDetector():
    def __init__(self, static_mode=False, num_max_faces=2, landmarks=True,
    min_detection = 0.4, min_tracking = 0.6):
    
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            static_image_mode=static_mode,
            max_num_faces=num_max_faces,
            refine_landmarks=landmarks,
            min_detection_confidence=min_detection,
            min_tracking_confidence=min_tracking
        )

        self.mp_drawing = mp.solutions.drawing_utils

    def detect(self, frame):
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        self.results = self.face_mesh.process(rgb_frame)
        if self.results.multi_face_landmarks:
            for face_landmarks in self.results.multi_face_landmarks:
                self.mp_drawing.draw_landmarks(
                    frame,
                    face_landmarks,    
                self.mp_face_mesh.FACEMESH_CONTOURS,
                landmark_drawing_spec=self.mp_drawing.DrawingSpec(color=(0,255,0), thickness=1),
                connection_drawing_spec=self.mp_drawing.DrawingSpec(color=(0,255,0), thickness=1)
                )
        return frame
        
        
        



                

'''
import mediapipe as mp
import cv2 as cv


class FaceDetector:
        def __init__(self, is_static: bool, max_num_faces: int, use_landmarks: bool, 
                     min_confidence_detection: float, min_confidence_tracking: float):
            """
            Inicializa el detector de caras.
            
            Args:
                is_static: True para imágenes estáticas, False para video
                max_num_faces: Número máximo de caras a detectar
                use_landmarks: Si se deben detectar los puntos de referencia (landmarks)
                min_confidence_detection: Confianza mínima para la detección
                min_confidence_tracking: Confianza mínima para el seguimiento
            """
            self.is_static = is_static
            self.max_num_faces = max_num_faces
            self.use_landmarks = use_landmarks
            self.min_confidence_detection = min_confidence_detection
            self.min_confidence_tracking = min_confidence_tracking        
            # Módulo de FaceMesh
            self.face_mesh_module = mp.solutions.face_mesh
            
            # Crear detector FaceMesh
            self.face_mesh = self.face_mesh_module.FaceMesh(
                static_image_mode=self.is_static,
                max_num_faces=self.max_num_faces,
                refine_landmarks=self.use_landmarks,
                min_detection_confidence=self.min_confidence_detection,
                min_tracking_confidence=self.min_confidence_tracking
            )
            
            # Módulo para dibujar
            self.drawing_utils = mp.solutions.drawing_utils

        def detect (self, image):
          
            # Convertir BGR a RGB
            rgb_image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
                
            # Ejecutar FaceMesh
            results = self.face_mesh.process(rgb_image)
                
            # Retornar las mallas detectadas
            return results.multi_face_landmarks
        
        def draw_faces(self, image):
            # Detectar caras en la imagen
            face_landmarks = self.detect(image)
            
            # Si se detectan caras, dibujar las mallas
            if face_landmarks:
                for landmarks in face_landmarks:
                    self.drawing_utils.draw_landmarks(
                        image=image,
                        landmark_list=landmarks,
                        connections=self.face_mesh_module.FACEMESH_TESSELATION,
                        landmark_drawing_spec=None,
                        connection_drawing_spec=self.drawing_utils.DrawingSpec(thickness=1, circle_radius=1)
                    )
            return image
        
        def landmarks_xy(self, image, landmarks):
            image_height, image_width, _ = image.shape
            coordinates = []
            for landmark in landmarks.landmark:
                x = int(landmark.x * image_width)
                y = int(landmark.y * image_height)
                coordinates.append((x, y))
            return coordinates
'''         