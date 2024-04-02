import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras.preprocessing.image import ImageDataGenerator




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