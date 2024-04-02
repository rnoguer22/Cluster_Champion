import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg



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
            img_shape = np.array(img).shape
            a = fig.add_subplot(1, len(classes), i)
            a.axis('off')
            plt.imshow(img)
            a.set_title(img_file + ' : ' + str(img_shape)).set_rotation(90)
        plt.show()