from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('mainScreen.kv')
class FirstScreen(Screen):
    def get_image_link(self):
        query = self.manager.current_screen.ids.user_input.text
        page = wikipedia.page(query)
        link_image = page.images[0]
        return link_image
    def download_image(self):
        req = requests.get(self.get_image_link())
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        return imagepath
    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()
class RootWidget(ScreenManager):
    pass
class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()