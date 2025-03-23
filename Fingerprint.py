#!/usr/bin/python3
from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import requests
import time

class Application(App):

    def build(self):
        root_layout = BoxLayout()
        label = TextInput()
        root_layout.ids['content'] = label
        root_layout.add_widget(label)
        return root_layout

    def request_callback(self, req, result):
        print(f'HttpStatus: {req.resp_status}')
        print(f'Response Headers: {req.resp_headers}')
        print(f'Response: {result}')

        self.root.ids.content.text += f'HttpStatus: {req.resp_status}\n\n'
        self.root.ids.content.text += f'Response Headers: {req.resp_headers}\n\n'
        self.root.ids.content.text += f'Response: {result}\n'
        self.root.ids.content.cursor = 0, 0

    def on_start(self, delay=0.5):
        time.sleep(delay)
        UrlRequest('https://www.babcock.co.za', self.request_callback, timeout=3, debug=True)

Application().run()