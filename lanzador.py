class Lanzador:
    def lanzar_winrate(self):
        from UEFA_Winrate.winrate import Winrate
        print('Calculando probabilidad de éxito para cada equipo...')
        winrate = Winrate('./UEFA_Predictions/csv')
        combined_df = winrate.combine_data()
        df_prob = winrate.calculate_prob(combined_df, './UEFA_Winrate/csv/winrate.csv')
        winrate.plot_prob('./UEFA_Winrate/img/winrate.png', df_prob)

    

    def lanzar_img_classifier(self):
        from IMG_Classifier.img_classifier import Img_Classifier
        print('Clasificando imagenes...')
        img_classifier = Img_Classifier('./Web_Scrapping/Logos_img')
        img_classifier.data_exploration()
        train_generator, validation_generator, batch_size, classnames = img_classifier.create_data_generators()
        model = img_classifier.define_cnn(train_generator)
        history = img_classifier.train_model(model, train_generator, validation_generator, batch_size)
        img_classifier.plot_loss(history)
        img_classifier.get_model_performance(model, validation_generator, classnames)
        img_classifier.save_model(model, './IMG_Classifier/model.h5')
        classes = img_classifier.get_classes()
        img_classifier.predict('./IMG_Classifier/model.h5', './Web_Scrapping/test', classes)