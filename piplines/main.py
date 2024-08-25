import tensorflow as tf
from Camera_Stream import PiVid

stream = PiVid((1536, 864))

while True:
    frame = stream.read()