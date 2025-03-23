#!/usr/bin/python3
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
import cv2
from ultralytics import YOLO
import math
import os

class KivyCamera(Image):
    def __init__(self, capture, fps, **kwargs):
        super(KivyCamera, self).__init__(**kwargs)
        self.capture = capture
        Clock.schedule_interval(self.update, 1.0 / fps)

    def update(self, dt):
        faceCascade = cv2.CascadeClassifier("/home/su3dotcom/haarcascade_frontalface_alt.xml")  # added

        ret, frame = self.capture.read()
        if ret:
            path = os.path.join("haarcascade_frontalface_alt.xml")
            face_classifier = cv2.CascadeClassifier(path)
            frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # added
            faces = faceCascade.detectMultiScale(frameGray, 1.1, 4)  # added

            for (x, y, w, h) in faces:  # added
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # added

            # convert it to texture
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            image_texture = Texture.create(
            size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture

        else:
            #start web-cam
            cap = cv2.VideoCapture(0)
            cap.set(3, 640)
            cap.set(4, 480)
            #initiate model
            model = YOLO("yolo-Weights/yolov8n.pt")
            # object classes
        classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "cat",
              "dog", "horse", "sheep", "cow", "goat"
              ]

        while True:
            success, img = cap.read()
            results = model(img, stream=True)

            # coordinates
        for r in results:
            boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence match --->",confidence)

            # class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

            cv2.imshow('Webcam', img)
            if cv2.waitKey(1) == ord('q'):
                break
                cap.release()
                cv2.destroyAllWindows()


class CamApp(App):
    def build(self):
        self.capture = cv2.VideoCapture(0)
        self.my_camera = KivyCamera(capture=self.capture, fps=30)
        return self.my_camera

    def on_stop(self):
        #without this, app will not exit even if the window is closed
        self.capture.release()


if __name__ == '__main__':
    CamApp().run()