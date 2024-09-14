#Now lets install our libraries to the code. We are not going to use all of the widgets in these libraries so i will only import part of them
from pytube import YouTube
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.image import Image 
from kivy.uix.button import Button 
from kivymd.uix.list import OneLineListItem,MDList
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

import os as os

#First let’s create our window’s size . I will make it 720/600 . But you can do it however you want. You might need to do slight adjustments to the code tho…Also let’s make a class and create the app
Window.size = (720,600)
class Yt(App):

#Now we want to make a function. In this function we will have our widgets like buttons labels textinputs and images. Widgets have so many different attributes , so you can use different attributes or change the values of it.

	def build(self):
		self.icon = "Assets\\1077046.png"
		layout = MDRelativeLayout(md_bg_color = [0,1,1]) # using with RGB code 
   # size hint means that it makes the size of the widget according to the apps default resolution. Pos_hint makes the same thing with about widget placement.
  # you can use different images and icons just dont forget to enter their path correctly

		self.img = Image(source='Assets\download-removebg-preview.png',size_hint=(.5,.5),pos_hint={'center_x':0.5,'center_y':0.9}) 
		self.linkinput = TextInput(text="",pos_hint={'center_x':0.5,'center_y':0.65},size_hint=(1,None),height=48,font_size=29,foreground_color=(34/255,139/255,34/255),)
		self.label = Label(text="Enter the link of the video which you want to download to your device ", pos_hint = {"center_x":0.5,"center_y":0.75},size_hint=(.3,.3),font_size=20,color=(0,100/255,0))
		self.button = Button(text="Download",size_hint=(0.15,0.15),pos_hint = {"center_x":0.5,"center_y":0.50},background_color=(34/255,139/255,34/255)) 
        self.add_widget(self.label)
        layout.add_widget(self.img)
        layout.add_widget(self.linkinput)
        layout.add_widget(self.button)
        layout.add_widget(self.res_link_input)
        return layout
            
            #Now we have to get the value of the textinput and attach a function to our button. We want to button to download videos of the link we wrote to linkinput when it is pressed. We have to create another function to do that
            
            def OnClicked(self,button):
            input_value = self.linkinput.text #gets the value from the input 
            res_value = self.res_link_input.text # makes the linkinput value text 
            button.disabled = True # cannot press he button
            try:
                youtube_object = YouTube(input_value, use_oauth=True, allow_oauth_cache=True) # Creating the youtube obect
                youtube_object.streams.filter(res=f"{res_value}p").first().download()# filtering the resolution so we can download which resolution we want
                self.success = Label(text="Video has been downloaded succesfully  ", pos_hint = {"center_x":0.5,"center_y":0.3},size_hint=(.3,.3),font_size=20,color=(0,100/255,0))

                
            except :
                print("An error has occurred:" )
                
                #Now let’s make main function to run the app:
                
                if __name__ == '__main__':
    Yt().run()
    
