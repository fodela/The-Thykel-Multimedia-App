from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from plyer import filechooser
from kivy.properties import StringProperty,ListProperty
from kivy.core.audio import SoundLoader

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
    color_black =ListProperty((0,0,0,1))
    color_primary =ListProperty((1,0,1,1))

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

        self.music_page = MusicScreen()
        screen = Screen(name='music')
        screen.add_widget(self.music_page)
        self.sm.add_widget(screen)

        return self.sm

    def play_music(self):
        sound = SoundLoader.load('music.m4a')
        if sound:
            sound.volume = 1
            self.change_screen('music')
            print(sound.length)
            sound.play
            
    
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