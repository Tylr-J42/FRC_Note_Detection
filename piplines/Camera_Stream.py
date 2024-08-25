from picamera2 import Picamera2
from libcamera import Transform

# class for allocating a thread to only updating the camera stream,
# the other thread is used for detection processing
class PiVid:

    def __init__(self, camera_res):
        # RPi camera recording setup with threading crap.
        #  For specs - https://www.raspberrypi.com/documentation/accessories/camera.html
        self.camera = Picamera2()
        self.resolution = camera_res
        config = self.camera.create_video_configuration(main={"format": "XRGB8888", "size": self.resolution}, transform=Transform(hflip=True))
        #config = self.camera.create_video_configuration(raw={"size":camera_res})
        self.camera.configure(config)
        #self.camera.set_controls({"FrameRate": 120})
        self.frame = None
        self.stopped = False
        self.camera.start()

    # output the frame we want
    def read(self):
        if self.stopped:
            self.camera.stop()
            return
        self.frame=self.camera.capture_array('main')
        return self.frame
        #print("debug threading")        

    def stop(self):
        self.stopped = True