from kivy.lang import Builder
from kivy.graphics import Color, Line
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout

from wopeditor.widgets.drawingarea import DrawingArea


Builder.load_string('''
<NewDrawingScreen>:
    name: "newdrawing"

    GridLayout:
        cols: 1
        padding: [10, 10]

        Header:
            id: header
            title: "new symbol drawing"
            on_press_back: app.goto_symbol(back_from=root.name)

        BoxLayout:
            Sidebar:
                id: sidebar
                SideButton:
                    text: "clear"
                    on_press: root.ids['drawing_area'].clear()
                SideButton:
                    text: "save"
                    on_press: app.save_drawing()
                FloatLayout:
                    #Filler

            DrawingArea:
                id: drawing_area
''')


class NewDrawingScreen(Screen):
    def update(self):
        self.ids['drawing_area'].clear()
