import arcade
from arcade import Window

# 1 создаем поле
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "starwars"

LASER_SPEED=5
class Lazer(arcade.Sprite):
    def __init__(self):
        super().__init__('laser.png')
        self.center_x=window.falcon.center_x

        self.bottom=window.falcon.top

        self.change_y=LASER_SPEED

        self.laser_sound=arcade.load_sound("laser.wav")

    def update(self):
        self.center_y += self.change_y
        if self.center_y >=SCREEN_HEIGHT:
            self.kill()




class Falcon(arcade.Sprite):
    def __init__(self):
        super().__init__('falcon.png', 0.3)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = 100

    def update(self):
        self.center_x += self.change_y



class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('background.jpg')
        self.falcon = Falcon()
        # cкрыть мышку
        self.set_mouse_visible(False)

        self.lasers = arcade.SpriteList()




    def setup(self): pass

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.bg)
        self.falcon.draw()
        self.lasers.draw()

    def update(self, delta_time: float):
        self.falcon.update()
        self.lasers.update()



    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.falcon.center_x=x


    def on_mouse_press(self,x,y,button,modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            laser=Lazer()
            self.lasers.append(laser)

            arcade.play_sound(sound=laser.laser_sound,volume=0.2)

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run()
