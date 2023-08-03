from graphiccalendar import GraphicCalendar
from kivy.app import App

class MainApp(App):
    def build(self):
        return GraphicCalendar(6, 2000, '#FFFFFF', '#0D5D4D', False)
    
MainApp().run()
