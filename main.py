from kivy.app import App
from kivy.graphics import Rectangle, Color, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.clock import Clock
import requests
import random





class Interface(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)



    def calc(self,widget):
        self.ids.fjal.text=self.ids.fjal.text + widget.text

    def erase(self):
        self.ids.fjal.text=""

    def eval1(self):
        self.ids.fjal.text=str(eval(self.ids.fjal.text))












class prov(App):
    pass

prov().run()