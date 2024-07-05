from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button


class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        self.camera = Camera(play=True)
        layout.add_widget(self.camera)

        button = Button(text='Сделать фото', size_hint=(1, 0.1))
        button.bind(on_press=self.take_photo)
        layout.add_widget(button)

        return layout

    def take_photo(self, instance):
        self.camera.export_to_png("photo.png")
        print("Фото сохранено как photo.png")


if __name__ == '__main__':
    CameraApp().run()