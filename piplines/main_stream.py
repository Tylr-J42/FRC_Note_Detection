from Camera_Stream import Picam2Vid
import Note_Obj_Inference

camera = Picam2Vid((1536, 864))

while True:
    camera.update()
    frame = camera.read()
    inference = Note_Obj_Inference.tflite_detect_images("~", frame)
