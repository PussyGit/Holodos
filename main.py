from kivy.app import App
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix import slider
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.slider import Slider
from kivy.core.window import Window
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import ButtonBehavior


Window.size = (500, 800)
Builder.load_file('my.kv')

matrix = [
    [70, 2.09, 3.79, 6.89],
    [80, 1.6, 2.9, 5.28],
    [90, 1.26, 2.3, 4.17],
    [100, 1.02, 1.86, 3.38],
    [110, 0.85, 1.54, 2.79],
    [120, 0.71, 1.29, 2.35],
    [130, 0.61, 1.1, 2],
    [140, 0.52, 0.95, 1.72],
    [150, 0.45, 0.83, 1.5],
    [160, 0.4, 0.73, 1.32],
    [170, 0.35, 0.64, 1.17],
    [180, 0.32, 0.57, 1.04]
]

r12_matrix = [
    [70, 2.09, 3.79, 6.89],
    [80, 1.6, 2.9, 5.28],
    [90, 1.26, 2.3, 4.17],
    [100, 1.02, 1.86, 3.38],
    [110, 0.85, 1.54, 2.79],
    [120, 0.71, 1.29, 2.35],
    [130, 0.61, 1.1, 2],
    [140, 0.52, 0.95, 1.72],
    [150, 0.45, 0.83, 1.5],
    [160, 0.4, 0.73, 1.32],
    [170, 0.35, 0.64, 1.17],
    [180, 0.32, 0.57, 1.04]
]

r134_matrix = [
    [70, 2.76, 5.02, 9.11,],
    [80, 2.11, 3.84, 6.98,],
    [90, 1.67, 3.04, 5.51,],
    [100, 1.35, 2.46, 4.47,],
    [110, 1.12, 2.03, 3.69,],
    [120, 0.94, 1.71, 3.1,],
    [130, 0.8, 1.46, 2.64,],
    [140, 0.69, 1.26, 2.28,],
    [150, 0.6, 1.09, 1.99,],
    [160, 0.53, 0.96, 1.75,],
    [170, 0.47, 0.85, 1.55,],
    [180, 0.42, 0.76, 1.38,]
]

r600_matrix = [
    [70, 2.26, 4.11, 7.47],
    [80, 1.79, 3.26, 5.92],
    [90, 1.46, 2.65, 4.81],
    [100, 1.21, 2.19, 3.99],
    [110, 1.02, 1.85, 3.36],
    [120, 0.87, 1.58, 2.86],
    [130, 0.75, 1.36, 2.47],
    [140, 0.65, 1.19, 2.16],
    [150, 0.57, 1.04, 1.9],
    [160, 0.51, 0.93, 1.68],
    [170, 0.45, 0.83, 1.5],
    [180, 0.41, 0.74, 1.35]
]


class MyLayout(Widget):
    def __init__(self):
        super().__init__()

    def on_pressed_freon(self, value):
        if value == 'R12':
            matrix = r12_matrix
        if value == 'R134':
            matrix = r134_matrix
        if value == 'R600':
            matrix = r600_matrix
        else:
            pass #сообщение об ошибке с просьбой выбрать фреон

        choosed_compressor = self.ids.slider.value
        for i in range(len(matrix) - 1):
            if matrix[i][0] == choosed_compressor:
                self.ids.result.text = str(matrix[i][1])

    def slider_move(self, value):
        choosed_compressor = self.ids.slider.value
        for i in range(len(matrix) - 1):
            if matrix[i][0] == choosed_compressor:
                self.ids.result.text = str(matrix[i][1])

    def on_pressed_pipe(self, value):
        choosed_compressor = self.ids.slider.value
        for i in range(len(matrix) - 1):
            if matrix[i][0] == choosed_compressor:
                self.ids.result.text = str(matrix[i][value])


class HolodosApp(App):
    def build(self):
        Window.clearcolor = (69/255, 73/255, 78/255)
        return MyLayout()


if __name__ == "__main__":
    HolodosApp().run()

