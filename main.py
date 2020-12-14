from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from plyer import filechooser
from kivy.properties import StringProperty,ListProperty,ObjectProperty,NumericProperty
from kivy.core.audio import SoundLoader
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.filechooser import FileChooserIconView
from kivy.clock import Clock

class HomeScreen(Screen):
    pass
class ImageScreen(Screen):
    pass
class MusicScreen(Screen):
    pass
class VideoScreen(Screen):
    pass
class MyToolbar(MDToolbar):
    pass


class ThykelPlay(MDApp):
    media_name = StringProperty()
    prev_dir = StringProperty('home/fodela/')
    media_playing = StringProperty()
    played = StringProperty('0')
    left_to_play = StringProperty('0')
    play_length = NumericProperty(0)
    color_black =ListProperty((0,0,0,1))
    color_primary =ListProperty((1,0,1,1))
    sound = ObjectProperty(SoundLoader.load('music.m4a'))

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

        self.image_page = ImageScreen()
        screen = Screen(name='image')
        screen.add_widget(self.image_page)
        self.sm.add_widget(screen)
        

        return self.sm
           
    def choose_file(self):
        filechooser.open_file(path=self.prev_dir,on_selection=self.handle_selection)
        # FileChooserIconView()

    def handle_selection(self,selection):
        self.media_name = selection[0]
        self.media_playing = self.media_name.split('/')[-1]
        self.prev_dir = '/'.join(self.media_name.split('/')[:-1])
        print(self.prev_dir)
            
    def change_screen(self,screen_name):
        self.sm.current = screen_name

    def play_music(self):
        self.prev_dir = '/home/fodela/Music/'
        self.choose_file()
        self.sound = SoundLoader.load(self.media_name)
        if self.sound:
            self.sound.volume = self.music_page.ids.vol.value
            self.change_screen('music')
            self.left_to_play = str(round(self.sound.length//60))+':'+str(round(self.sound.length%60))
            self.play_length = self.sound.length
            self.sound.play()
            self.played = str(self.sound.get_pos())
            self.music_page.ids.seeker.value = self.sound.get_pos()

            # def update_music_ui(self,**kwargs):
            #     self.left_to_play = str(round(self.sound.length//60))+':'+str(round(self.sound.length%60))
            #     self.play_length = self.sound.length
            #     self.played = str(self.sound.get_pos())
            # Clock.schedule_interval(update_music_ui(ThykelPlay()),1)
       
    def play_video(self):
        self.prev_dir = '/home/fodela/Downloads/Video/'
        self.choose_file()
        self.change_screen('video')

    def view_image(self):
        self.prev_dir = '/home/fodela/Downloads/Images/'
        self.choose_file()
        self.change_screen('image')

    def music_go_home(self):
        self.sound.stop()
        self.change_screen('home')

    # def update_music_ui(self):
    #     self.left_to_play = str(round(self.sound.length//60))+':'+str(round(self.sound.length%60))
    #     self.played = str(self.sound.get_pos())
    
if __name__ == "__main__":
    ThykelPlay().run()