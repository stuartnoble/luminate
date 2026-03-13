//  Rainbow
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    let ledRange: kitronik_halo_hd.ZIPHaloHd;
    
    haloDisplay.clear()
    LEDs = 1
    // haloDisplay.show_rainbow(1, 360)
    while (LEDs == 1) {
        for (let x = 0; x < 359; x++) {
            ledRange = haloDisplay.range(0, 1)
            ledRange.setZipLedColor(x, kitronik_halo_hd.colors(x))
            ledRange.setBrightness(randint(0, 255))
        }
        // haloDisplay.rotate(1)
        // basic.pause(100)
        basic.pause(500)
        haloDisplay.show()
    }
})
//  Green
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    LEDs = 3
})
//  Red
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    LEDs = 2
})
//  Blue
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    LEDs = 4
})
//  Yellow
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    LEDs = 5
})
let LEDs = 0
let haloDisplay : kitronik_halo_hd.ZIPHaloHd = null
radio.setGroup(1)
haloDisplay = kitronik_halo_hd.createZIPHaloDisplay(60)
haloDisplay.setBrightness(50)
basic.forever(function on_forever() {
    basic.showString("Stuart")
})
