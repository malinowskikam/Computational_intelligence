from keras.preprocessing.image import ImageDataGenerator
from keras import layers, models
import data
import numpy as np

batch_size = 10

model = models.Sequential()

model.add(layers.Conv2D(32, (3, 3), input_shape=(data.data_dimensions[0], data.data_dimensions[1], 3)))
model.add(layers.Activation('relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

model.add(layers.Conv2D(32, (3, 3)))
model.add(layers.Activation('relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

model.add(layers.Conv2D(64, (3, 3)))
model.add(layers.Activation('relu'))
model.add(layers.MaxPooling2D(pool_size=(2, 2)))

model.add(layers.Flatten())
model.add(layers.Dense(64))
model.add(layers.Activation('relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(1))
model.add(layers.Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.summary()

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

val_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

train_generator = train_datagen.flow(np.array(data.train_data), data.train_classes, batch_size=batch_size)
validation_generator = val_datagen.flow(np.array(data.test_data), data.test_classes, batch_size=batch_size)

history = model.fit_generator(
    train_generator, 
    steps_per_epoch=len(data.train_data) // batch_size,
    epochs=30,
    validation_data=validation_generator,
    validation_steps=len(data.test_data) // batch_size
)

model.save_weights('tmp_model_weights.h5')
model.save('tmp_model.h5')