from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from plyer import filechooser
from kivy.properties import StringProperty,ListProperty,ObjectProperty,NumericProperty
from kivy.core.audio import SoundLoader
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDIconButton
from kivy.uix.filechooser import FileChooserIconView
from kivy.clock import Clock
from kivymd.uix.list import TwoLineIconListItem,IconLeftWidget
from kivy.uix.image import Image
import os



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
class MusicButton(MDIconButton):
    pass


class ThykelPlay(MDApp):
    media_name = StringProperty()
    prev_dir = StringProperty('home/fodela/Downloads')
    media_playing = StringProperty()
    played = StringProperty('0')
    player_state_icon = StringProperty('pause')
    player_state = StringProperty('playing')
    left_to_play = StringProperty('0')
    play_length = NumericProperty(0)
    color_black =ListProperty((0,0,0,1))
    color_white =ListProperty((1,1,1,1))
    color_white_transparent = ListProperty((1,1,1,.5))
    color_primary =ListProperty((1,0,1,1))
    sound = ObjectProperty(SoundLoader.load('music.m4a'))
    recently_played = ListProperty()
    recent_set = ObjectProperty()
    recent_set = set()
    pic_index = NumericProperty(0)
    image_lst = ListProperty()
    current_img = StringProperty()
    vid_played = StringProperty('0:00')
    vid_left_to_play = StringProperty('0:00')
    vid_player_state = StringProperty('playing')
    vid_player_state_icon = StringProperty('pause')

    def __init__(self,*args, **kwargs):
        super().__init__()
        self.icon = '/home/fodela/Prpngoject/Python Projects/Kivy Projects/The-Thykel-Multimedia-App/images/multimedia_icon.'

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
        # self.prev_dir = '/'.join(self.media_name.split('/')[:-1])
            
    def change_screen(self,screen_name):
        self.sm.current = screen_name

    def play_music(self):
        self.prev_dir = '/home/fodela/Music/'
        try:
            self.choose_file()
            self.sound = SoundLoader.load(self.media_name)
            if self.sound:
                self.sound.volume = self.music_page.ids.vol.value
                self.change_screen('music')
                self.left_to_play = str(round(self.sound.length//60))+':'+str(round(self.sound.length%60))
                self.play_length = self.sound.length
                self.sound.play()
                self.played = str(self.sound.get_pos())
                self.recent_set.add(self.media_name)
                self.recently_played = [i for i in self.recent_set]


                Clock.schedule_interval(self.update_music_ui,1)
                
        except Exception as e:
            print(e)

    def music_pause_play_n_stop(self):
        if self.player_state == 'playing':
            self.music_page.ids.seeker.value = self.sound.get_pos()
            self.sound.stop()
            self.player_state_icon = 'play'
            self.player_state = 'paused'
             
        elif self.player_state == 'paused':
            # self.sound.seek(self.paused_at)
            self.sound.play()
            self.player_state_icon = 'pause'
            self.player_state = 'playing'
        elif self.player_state == 'stoped':
            self.sound.play()
            self.player_state_icon = 'pause'
            self.player_state = 'playing'
            
    def music_stop(self):
        self.sound.stop()
        self.player_state_icon = 'play'
        self.player_state = 'stoped'
        self.music_page.ids.seeker.value = 0
     
    def play_video(self):
        self.prev_dir = '/home/fodela/Downloads/Video/'
        self.choose_file()
        self.left_to_play = str(round(self.sound.length//60))+':'+str(round(self.sound.length%60))
        self.change_screen('video')

        Clock.schedule_interval(self.update_vid_ui,1)

    def view_image(self):
        self.prev_dir = '/home/fodela/Downloads/Images/'
        self.choose_file()
        # self.current_img = self.media_name
        self.change_screen('image')

    def music_go_home(self):
        self.sound.stop()
        self.change_screen('home')

    def update_music_ui(self,*args):
        self.music_page.ids.seeker.value = self.sound.get_pos()
        self.played = f"{int(self.sound.get_pos()//60)}:{int(self.sound.get_pos()%60)}"

    def update_vid_ui(self,*args):
        self.video_page.ids.vid_seeker.value = self.video_page.ids.vid.position
        self.vid_played = f"{int(self.video_page.ids.vid.position//60)}:{int(self.video_page.ids.vid.position%60)}"
        self.vid_left_to_play = f"{int(self.video_page.ids.vid.duration//60)}:{int(self.video_page.ids.vid.duration%60)}"
    
    def get_files(self,dir):
        # fileNames = os.listdir('/home/fodela/Downloads/Images/')
        # for fileName in fileNames:
        #     print(fileName)
            # print(os.path.abspath(os.path.join(dir,fileName)))
    
        try:
            for r in self.recently_played:
                self.music_page.ids.recents.add_widget(TwoLineIconListItem(text = r.split('/')[-1][:-4],
                secondary_text= 'Scholaurenstein',
                theme_text_color= 'Custom',
                text_color= self.color_primary,
                secondary_theme_text_color= 'Custom',
                secondary_text_color= self.color_white_transparent,
                # IconLeftWidget=
                #         {'icon': 'play',
                #         'theme_text_color': "Custom",
                #         'text_color': self.color_white}
                ))
            
        except Exception as e:
            print(e)

    def vid_pause_play_n_stop(self):
        if self.vid_player_state == 'playing':
            self.music_page.ids.seeker.value = self.sound.get_pos()
            self.video_page.ids.vid.state = 'pause'
            self.vid_player_state_icon = 'play'
            self.vid_player_state = 'paused'
             
        elif self.vid_player_state == 'paused':
            # self.sound.seek(self.paused_at)
            self.video_page.ids.vid.state = 'play'
            self.vid_player_state_icon = 'pause'
            self.vid_player_state = 'playing'

        # elif self.vid_player_state == 'stoped':
        #     self.sound.play()
        #     self.vid_player_state_icon = 'pause'
        #     self.vid_player_state = 'playing'
    # def get_imgs(self):
    #     fileNames = os.listdir(self.prev_dir)
    #     self.image_lst = [f"{self.prev_dir}/{f} " for f in fileNames]
    #     print(len(self.image_lst))

    # def next_img(self):
        # try:
        #     print(self.current_img)
        #     self.get_imgs()
        #     if self.pic_index < len(self.image_lst):
        #         self.current_img = str(self.image_lst[self.pic_index])
        #         self.pic_index +=1
        #         print('fired')
        # except Exception as err:
        #     print(err)

    def seek_video(self):
        self.video_page.ids.vid.seek((self.video_page.ids.vid_seeker.value/self.video_page.ids.vid.duration))
        
if __name__ == "__main__":
    ThykelPlay().run()