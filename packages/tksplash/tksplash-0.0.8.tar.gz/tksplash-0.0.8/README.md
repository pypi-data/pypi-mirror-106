The tksplash module can be used to make splash screens for all of your GUIs which you make using tkinter

To use this assing the `Tksplash` class to a variable:

``splash = tksplash.Tksplash()``

and then you can fill in the arguments

it takes 5 arguments where only one is required and other are optional

`window`

the one above is the required value

`destroy_time, font_style,text_colour',font_size`

and the these are the optional values

____

**Note**->the `text_colour` can also be written as `#RRGGBB`

**Note**->The value of `time_after_which_it_should_destroy` should be entered in millisecond(ms), (1 s = 1000ms)

An example using all the arguments:

```
import tksplash
import tkinter

win = tkinter.Tk()
splash = tksplash.Tksplash(win, 3000, "Lucida Grande", "white")
splash.add_splash_text("hello", 500, 500)
win.mainloop()
```

_____
These are some examples on how to use this module :

```
import tksplash
import tkinter

win = tkinter.Tk()
splash = tksplash.Tksplash(win)
splash.add_splash_text("hello", 500, 500)
win.mainloop()
````

______________
the `add_splash_text()` takes in exactly 3 arguments

`text, width, height`

___
`text`--> the text you want to display

`widht`--> the width of the window

`height`--> the height of the window

_________________________

Adding an image in the splash screen

`splash.add_image("some.jpg", 100, 100, 250, 350)`

The `add_image()` function takes in `5` arguments

`img, img_x, img_y, place_x, place_y`

these are the required values 👆👆
___
`img`--> the image you want to project on the splash screen

`img_x`--> the width of the image

`img_y`--> the height of the image

`place_x`--> the x value where you want to place the image

`place_y`--> the y value where you want to place the image
_________________________

Adding image as well as text use `add_image_text()` function

It takes in these values

`text, width, height, img, img_x, img_y, place_x, place_y,`

____

To add a gif use `add_gif()`

And it takes in 3 arguments

`gif,place_x,place_y`
___

To add a gif and text use `add_gif_text()`

And it takes in 6 arguments

`text, width ,height,gif,place_x,place_y`





