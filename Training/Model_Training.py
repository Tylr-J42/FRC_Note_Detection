import numpy as np
import os

from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

import tensorflow as tf

training_data = object_detector.DataLoader("~/Desktop/note detection frc 2024.v4i.tfrecord/train/note.tfrecord")
test_data = object_detector.DataLoader("~/Desktop/note detection frc 2024.v4i.tfrecord/test/note.tfrecord")
valid_data = object_detector.DataLoader("~/Desktop/note detection frc 2024.v4i.tfrecord/valid/note.tfrecord")

spec = model_spec.get('efficientdet_lite0')

model = object_detector.create(training_data, model_spec=spec, batch_size=4, train_whole_model=True, epochs=15, validation_data=valid_data)

model.evaluate(valid_data)
