from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from plyer import filechooser
from kivy.properties import StringProperty

class HomeScreen(Screen):
    pass
class PictureScreen(Screen):
    pass
class MusicScreen(Screen):
    pass
class VideoScreen(Screen):
    pass


class ThykelPlay(MDApp):
    video_name = StringProperty()

    def build(self):
        self.sm = ScreenManager()

        self.home_page = HomeScreen()
        screen = Screen(name='home')
        screen.add_widget(self.home_page)
        self.sm.add_widget(screen)

        self.video_page = VideoScreen()
        screen = Screen(name='video')
        screen.add_widget(self.video_page)
        self.sm.add_widget(screen)

        return self.sm

    
    def choose_file(self):
        filechooser.open_file(on_selection=self.handle_selection)
    def handle_selection(self,selection):
        self.video_name = selection[0]
        print(self.video_name)
        self.change_screen('video')
    def change_screen(self,screen_name):
        self.sm.current = screen_name

    

if __name__ == "__main__":
    ThykelPlay().run()