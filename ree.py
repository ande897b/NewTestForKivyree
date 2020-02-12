import kivy
from kivy.uix.label import Label


class MyApp():
    def build (self):
        return Label(test="Testmofo")

if __name__ == "__main__":
    MyApp().Run()