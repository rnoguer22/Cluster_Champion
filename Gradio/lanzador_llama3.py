from Gradio.llama3 import Gradio_GUI

class LanzadorLlama3():
    def lanzar_gradio_gui(self):
        gradio_gui = Gradio_GUI('./UEFA_Predictions/csv')
        gradio_gui.launch_gradio_gui()