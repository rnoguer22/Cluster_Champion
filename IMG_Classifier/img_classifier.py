import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense





class Img_Classifier:

    def __init__(self, data_path):
        self.data_path = data_path
    

    #Metodo para explorar los datos
    def data_exploration(self):
        classes = os.listdir(self.data_path)
        print(len(classes), 'classes:')
        print(classes)

        fig = plt.figure(figsize=(12, 12))
        i = 0
        for sub_dir in os.listdir(self.data_path):
            i += 1
            img_file = f'{sub_dir}.png'
            img_path = os.path.join(self.data_path, sub_dir, img_file)
            img = mpimg.imread(img_path)
            self.img_shape = np.array(img).shape
            a = fig.add_subplot(1, len(classes), i)
            a.axis('off')
            plt.imshow(img)
            a.set_title(img_file + ' : ' + str(self.img_shape)).set_rotation(90)
        plt.show()
    

    #Metodo para crear los data generators
    def create_data_generators(self):
        img_size = [self.img_shape[0], self.img_shape[1]]
        batch_size = 30
        print("Getting Data...")
        datagen = ImageDataGenerator(rescale=1./255, # normalize pixel values
                                    validation_split=0.3) # hold back 30% of the images for validation
        print("Preparing training dataset...")
        train_generator = datagen.flow_from_directory(
            self.data_path,
            target_size=img_size,
            batch_size=batch_size,
            class_mode='categorical',
            subset='training') # set as training data
        print("Preparing validation dataset...")
        validation_generator = datagen.flow_from_directory(
            self.data_path,
            target_size=img_size,
            batch_size=batch_size,
            class_mode='categorical',
            subset='validation') # set as validation data
        classnames = list(train_generator.class_indices.keys())
        print('Data generators ready')
        return train_generator, validation_generator, batch_size
    

    #Metodo para definir la CNN
    def define_cnn(self, train_generator):
        # Define a CNN classifier network
        # Define the model as a sequence of layers
        model = Sequential()
        # The input layer accepts an image and applies a convolution that uses 32 6x6 filters and a rectified linear unit activation function
        model.add(Conv2D(32, (6, 6), input_shape=train_generator.image_shape, activation='relu'))
        # Next we'll add a max pooling layer with a 2x2 patch
        model.add(MaxPooling2D(pool_size=(2,2)))
        # We can add as many layers as we think necessary - here we'll add another convolution and max pooling layer
        model.add(Conv2D(32, (6, 6), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # And another set
        model.add(Conv2D(32, (6, 6), activation='relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        # A dropout layer randomly drops some nodes to reduce inter-dependencies (which can cause over-fitting)
        model.add(Dropout(0.2))
        # Now we'll flatten the feature maps and generate an output layer with a predicted probability for each class
        model.add(Flatten())
        model.add(Dense(train_generator.num_classes, activation='softmax'))
        # With the layers defined, we can now compile the model for categorical (multi-class) classification
        model.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])
        print(model.summary())
        return model


    #Metodo para entrenar el modelo
    def train_model(self, model, train_generator, validation_generator, batch_size):
        num_epochs = 5
        history = model.fit(
            train_generator,
            steps_per_epoch = train_generator.samples // batch_size,
            validation_data = validation_generator, 
            validation_steps = validation_generator.samples // batch_size,
            epochs = num_epochs)