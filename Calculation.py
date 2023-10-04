'''
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        main_layout = BoxLayout(orientation = 'vertical', padding = 10, spacing = 10)   # Расположение элементов
        self.solution = TextInput(multiline = False, readonly = False, halign = 'right', font_size = 55)     # Кнопка ввода
        # Добавляем текстовую кнопку 
        main_layout.add_widget(self.solution)

        # Добавляем кнопки команд
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]
        # Пробегаем по строкам
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint = {"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press = self.on_button_press)  # Позволяет привязать кнопку из списка вып. функции
                # Горизонтальное расположение кнопки
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        
        # Делаем кнопку ровняется
        equals_button = Button(text='=', pos_hint = {"center_x": 0.5, "center_y": 0.5})
        equals_button.bind(on_press = self.on_solution)
        main_layout.add_widget(equals_button)



        return main_layout

    # Функция для работы кнопок
    def on_button_press(self, instace):
        if instace.text == "C":
            self.solution.text = ''
        else:
            self.solution.text += instace.text

    # Функция для работы кнопок вычисления
    def on_solution(self, instance):
        if self.solution.text:
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = 'Error'


if __name__ == '__main__':
    MainApp().run()
'''
