from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import winsound
from kivy.config import Config

Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')
Config.set('graphics', 'resizable', '0')

s = []

class MainApp(App):
    def build(self):
        main_layout = FloatLayout()

        box_layout = BoxLayout(orientation='vertical',
                               size_hint = (1, 0.5),
                               pos_hint = {'x': 0, 'y': 0.5})

        restart_button = Button(text='Restart Sound Track',
                                background_color=[1, 0, 1, 1],
                                italic = True,
                                bold = True,
                                font_size = 30)

        restart_button.bind(on_press = restart_solution)
        box_layout.add_widget(restart_button)

        start_button = Button(text='Start Sound Track',
                              background_color=[1, 1, 0, 1],
                              italic = True,
                              bold = True,
                              font_size = 30)

        start_button.bind(on_press = start_solution)
        box_layout.add_widget(start_button)

        main_layout.add_widget(box_layout)

        grid_layout = GridLayout(rows = 1,
                                 size_hint = (1, 0.5))

        buttons = ['90', '100', '110', '120', '130', '200', '300', '400', '500', '600',
                   '700', '800', '900', '1000', '25000']
        color_switch = 0

        for i in buttons:
            if color_switch == 0:
                color = [0, 0.5, 0.5, 1]
                color_switch = 1
            else:
                color = [0.1, 0.5, 0.8, 1]
                color_switch = 0

            button = Button(text = str(i), background_color = color,
                            italic = True, font_size = 15)
            button.bind(on_press = sound_solution)
            grid_layout.add_widget(button)

        main_layout.add_widget(grid_layout)

        return main_layout
    # Создаем функцию, которая будет отвечать за обнуление трека
def restart_solution(instance):
    global s
    s = []

    #Далее создаем функцию, которая будет воспроизводить весь записанный трек
def start_solution(instance):
    for i in s:
        winsound.Beep(int(i), 300)

   #последняя функция, которая будет отвечать за воспроизведение звука нажатой клавиши и записи его в переменную s
def sound_solution(instance):
    winsound.Beep(int(instance.text), 300)
    s.append(instance.text)

if __name__ == '__main__':
    MainApp().run()