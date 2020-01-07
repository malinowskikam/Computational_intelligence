from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array, load_img
from keras import layers, models, optimizers
from keras import backend as K
import data
import numpy as np

batch_size=16

model = models.load_model("tmp_model.h5")
model.load_weights("tmp_model_weights.h5")

model.summary()

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

print(len(log))
print(len(data.test_data))
