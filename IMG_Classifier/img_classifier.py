import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras import models
from sklearn.metrics import confusion_matrix

from tensorflow import convert_to_tensor

from PIL import Image




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
    

    #Metodo getter para obtener las clases
    def get_classes(self):
        classes = os.listdir(self.data_path)
        return classes
    

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
        return train_generator, validation_generator, batch_size, classnames
    

    #Metodo para definir la CNN
    def define_cnn(self, train_generator):
        # Define a CNN classifier network
        # Define the model as a sequence of layers
        model = Sequential()
        # The input layer accepts an image and applies a convolution that uses 32 6x6 filters and a rectified linear unit activation function
        model.add(Conv2D(32, (6, 6), input_shape = train_generator.image_shape, activation = 'relu'))
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
        model.add(Dense(train_generator.num_classes, activation = 'softmax'))
        # With the layers defined, we can now compile the model for categorical (multi-class) classification
        model.compile(loss='categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])
        print(model.summary())
        return model


    #Metodo para entrenar el modelo
    def train_model(self, model, train_generator, validation_generator, batch_size):
        self.num_epochs = 5
        history = model.fit(
            train_generator,
            steps_per_epoch = train_generator.samples // batch_size,
            validation_data = validation_generator, 
            validation_steps = validation_generator.samples // batch_size,
            epochs = self.num_epochs)
        return history
    

    #Metodo para visualizar los resultados
    def plot_loss(self, history):
        epoch_nums = range(1, self.num_epochs + 1)
        training_loss = history.history["loss"]
        validation_loss = history.history["val_loss"]
        plt.plot(epoch_nums, training_loss)
        plt.plot(epoch_nums, validation_loss)
        plt.xlabel('epoch')
        plt.ylabel('loss')
        plt.legend(['training', 'validation'], loc='upper right')
        plt.show()

    
    #Obtenemos la matriz de confusion del modelo
    def get_model_performance(self, model, validation_generator, classnames):
        print("Generating predictions from validation data...")
        # Get the image and label arrays for the first batch of validation data
        x_test = validation_generator[0][0]
        y_test = validation_generator[0][1]
        # Use the model to predict the class
        class_probabilities = model.predict(x_test)
        # The model returns a probability value for each class
        # The one with the highest probability is the predicted class
        predictions = np.argmax(class_probabilities, axis=1)
        # The actual labels are hot encoded (e.g. [0 1 0], so get the one with the value 1
        true_labels = np.argmax(y_test, axis=1)
        # Plot the confusion matrix
        cm = confusion_matrix(true_labels, predictions)
        plt.imshow(cm, interpolation="nearest", cmap=plt.cm.Blues)
        plt.colorbar()
        tick_marks = np.arange(len(classnames))
        plt.xticks(tick_marks, classnames, rotation=85)
        plt.yticks(tick_marks, classnames)
        plt.xlabel("Predicted Shape")
        plt.ylabel("Actual Shape")
        plt.show()  
    

    #Guardamos el modelo
    def save_model(self, model, output_path):
        model.save(output_path)
        del model  # deletes the existing model variable
        print('Model saved as', output_path)
    

    #Metodo para predecir el equipo de los logos de test
    def predict(self, model_path, test_data_path, classes):
        #Definimos una funcion dentro del metodo para predecir la clase de una imagen
        def predict_image(classifier, image):
            # Convertir la imagen a modo RGB si tiene un canal alpha (transparencia)
            print(image.shape)
            if image.shape[2] == 4:  # Si la imagen tiene 4 canales (RGBA)
                image = image[:, :, :3]  # Eliminar el canal alpha
                print(image.shape)
            # The model expects a batch of images as input, so we'll create an array of 1 image
            imgfeatures = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])
            # We need to format the input to match the training data
            # The generator loaded the values as floating point numbers
            # and normalized the pixel values, so...
            imgfeatures = imgfeatures.astype('float32')
            print(imgfeatures.shape)
            imgfeatures /= 255
            # Use the model to predict the image class
            class_probabilities = classifier.predict(imgfeatures)
            # Find the class predictions with the highest predicted probability
            index = int(np.argmax(class_probabilities, axis=1)[0])
            return index
        
        model = models.load_model(model_path)

        #Mostramos las imagenes con las predicciones
        fig = plt.figure(figsize=(8, 12))
        i = 0
        for img_file in os.listdir(test_data_path):
            i += 1
            img_path = os.path.join(test_data_path, img_file)
            img = mpimg.imread(img_path)
            #Obtenemos la prediccion de la imagen
            index = predict_image(model, np.array(img))
            a = fig.add_subplot(1, len(classes), i)
            a.axis('off')
            imgplot = plt.imshow(img)
            a.set_title(classes[index])
        plt.show()
