
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import mainthread

import threading
import socket



# Виджет с указанием параметров
KV = """
MyBL: 
        orientation: "vertical"
        size_hint: (0.95, 0.95)                      
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        Label: 
                font_size: "15sp"
                multiline: True
                text_size: self.width*0.98, None
                size_hint_x: 1.0
                size_hint_y: None
                height: self.texture_size[1] + 15
                text: root.data_label
                markup: True

        TextInput:
                id: Inp
                multiline: False
                padding_y: (5,5)
                size_hint: (1, 0.5)

        Button:
                text: "Поиск по названию"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback()
        Button:
                text: "Поиск по описанию"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback2()
        Button:
                text: "Случайный"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback3()
        Button:
                text: "Отправить"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1,0.5)
                on_press: root.callback4()
"""

# Будет опр весь функционал нашего приложения
class MyBL(BoxLayout):
    data_label = StringProperty("Треугольник!")

    # Сделать сервер общедоступным
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        SERVER = "10.8.0.6"
        PORT = 1488

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((SERVER, PORT))
        self.client.sendall(bytes("979879789", 'UTF-8'))

        threading.Thread(target=self.get_data).start()

    def callback(self):
        print("Поиск по названию")
        self.client.sendall(bytes("Поиск по названию", 'UTF-8'))
    
    def callback2(self):
        print("Поиск по описанию")
        self.client.sendall(bytes("Поиск по описанию", 'UTF-8'))

    def callback3(self):
        print("Случайный")
        self.client.sendall(bytes("Случайный", 'UTF-8'))

    def callback4(self):
        print("Отправить")
    
    def get_data(self):
        while App.get_running_app().running:
            In_data = self.client_recv(4096)
            print("ОТ сервера: ", In_data.decode())
            KKK = In_data.decode()
            ZZZ = str(KKK)
            lines = ZZZ.split('\n')
            print(lines)
            if '\t\t\t\t\t' in lines:
                lines[4] = "=========="
            for ggg in lines:
                if ggg.startswith("https://"):
                    ggg = '[color=#00FFCE]' + ggg + '[/color]'
                self.set_data_label(ggg)


    @mainthread
    def set_data_label(self, data):
        self.data_label += str(data) + "\n"
    



# отвечает за запуска и отрицовку приложения
class MyApp(App):
    running = True
    def build(self):
        return Builder.load_string(KV)
    def on_stop(self):
        self.running = False


MyApp().run()





