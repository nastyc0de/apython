from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

Builder.load_file('frontend.kv')

class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.cameraButton.text = 'Stop Camera'
        self.ids.camera.texture = self.ids.camera._camera.texture
    def stop(self):
        self.ids.camera.play = False
        self.ids.cameraButton.text = 'Start Camera'
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filename = f'files/{current_time}.png'
        self.ids.camera.export_to_png(self.filename)
        self.manager.current = 'imageScreen'
        self.manager.current_screen.ids.img.source = self.filename
class ImageScreen(Screen):
    def create_link(self):
        filepath = App.get_running_app().root.ids.cameraScreen.filename
        print(filepath)
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()