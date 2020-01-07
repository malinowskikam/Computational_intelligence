from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array, load_img
from keras import layers, models, optimizers
from keras import backend as K
import data
import numpy as np
import cv2

batch_size=20

model = models.load_model("tmp_model.h5")
model.load_weights("tmp_model_weights.h5")

val_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

validation_generator = val_datagen.flow(np.array(data.test_data), data.test_classes, batch_size=batch_size)

log = model.predict_generator(
    validation_generator,
    steps=len(data.test_data) // batch_size,
    verbose=1
)

j = 0
for i in range(len(data.test_data)):
    if round(log[i][0]) != data.test_classes[i]:
        cv2.imwrite("wrong_predicts\\wrong"+str(j)+".jpg",data.test_data[i])
        j += 1 

print(f"{len(data.test_data)-j}/{len(data.test_data)}")

log = model.evaluate_generator(
    validation_generator,
    steps=len(data.test_data) // batch_size,
    verbose=1
)

print(log)