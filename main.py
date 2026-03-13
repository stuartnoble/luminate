
# Rainbow

def on_button_pressed_a():
    global LEDs
    haloDisplay.clear()
    LEDs = 1
    #haloDisplay.show_rainbow(1, 360)
    
    while LEDs == 1:
        for x in range(359):
            ledRange = haloDisplay.range(0, 1)
            ledRange.set_zip_led_color(x, kitronik_halo_hd.colors(x))
            ledRange.set_brightness(randint(0, 255))

        #haloDisplay.rotate(1)
        #basic.pause(100)
        basic.pause(500)
        haloDisplay.show()
input.on_button_pressed(Button.A, on_button_pressed_a)

# Green

def on_button_pressed_ab():
    global LEDs
    LEDs = 3
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# Red

def on_button_pressed_b():
    global LEDs
    LEDs = 2
input.on_button_pressed(Button.B, on_button_pressed_b)

# Blue

def on_gesture_shake():
    global LEDs
    LEDs = 4
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# Yellow

def on_logo_pressed():
    global LEDs
    LEDs = 5
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

LEDs = 0
haloDisplay: kitronik_halo_hd.ZIPHaloHd = None
radio.set_group(1)
haloDisplay = kitronik_halo_hd.create_zip_halo_display(60)
haloDisplay.set_brightness(50)

def on_forever():
    basic.show_string("Stuart")
basic.forever(on_forever)
