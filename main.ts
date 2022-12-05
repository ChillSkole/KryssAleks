let Pedestrian_Red = 0
let Secondary_Red_Light = 0
let Main_Red_light = 0
let Main_Yellow_light = 0
let Main_Green_light = 0
let pedestrian_control = 0
let Pedestrian_Green = 0
let Secondary_Yellow_Light = 0
let Secondary_Green_Light = 0
function all_traffic_lights_system () {
    Pedestrian_Red = 1
    Secondary_Red_Light = 1
    Main_Red_light = 1
    Main_Yellow_light = 0
    Main_Green_light = 0
    basic.pause(1000)
    Main_Red_light = 1
    Main_Yellow_light = 1
    Main_Green_light = 0
    basic.pause(2500)
    Main_Red_light = 0
    Main_Yellow_light = 0
    Main_Green_light = 1
    basic.pause(5000)
    Main_Red_light = 0
    Main_Yellow_light = 1
    Main_Green_light = 0
    basic.pause(2000)
    Main_Red_light = 1
    Main_Yellow_light = 0
    Main_Green_light = 0
    // If B button is pressed, the pedestrian_control variable will get a value of one. This will then be recognized by the IF section and the code will divert to and run the line of code inside the IF section
    if (pedestrian_control == 1) {
        pedestrian_control = 0
        basic.pause(1000)
        Pedestrian_Red = 0
        basic.pause(1000)
        Pedestrian_Green = 1
        for (let index = 0; index < 40; index++) {
            music.playTone(698, music.beat(BeatFraction.Eighth))
            basic.pause(50)
        }
        for (let index = 0; index < 17; index++) {
            Pedestrian_Green = 1
            music.playTone(698, music.beat(BeatFraction.Quarter))
            basic.pause(100)
            Pedestrian_Green = 0
            music.playTone(698, music.beat(BeatFraction.Quarter))
            basic.pause(100)
        }
        Pedestrian_Red = 1
        Pedestrian_Green = 0
    }
    basic.pause(2500)
    Secondary_Red_Light = 1
    Secondary_Yellow_Light = 1
    Secondary_Green_Light = 0
    basic.pause(2000)
    Secondary_Red_Light = 0
    Secondary_Yellow_Light = 0
    Secondary_Green_Light = 1
    basic.pause(5000)
    Secondary_Red_Light = 0
    Secondary_Yellow_Light = 1
    Secondary_Green_Light = 0
    basic.pause(2000)
    Secondary_Red_Light = 1
    Secondary_Yellow_Light = 0
    Secondary_Green_Light = 0
    // If B button is pressed, the pedestrian_control variable will get a value of one. This will then be recognized by the IF section and the code will divert to and run the line of code inside the IF section
    if (pedestrian_control == 1) {
        pedestrian_control = 0
        basic.pause(1000)
        Pedestrian_Red = 0
        basic.pause(1000)
        Pedestrian_Green = 1
        for (let index = 0; index < 40; index++) {
            music.playTone(698, music.beat(BeatFraction.Eighth))
            basic.pause(50)
        }
        for (let index = 0; index < 17; index++) {
            Pedestrian_Green = 1
            music.playTone(698, music.beat(BeatFraction.Quarter))
            basic.pause(100)
            Pedestrian_Green = 0
            music.playTone(698, music.beat(BeatFraction.Quarter))
            basic.pause(100)
        }
        Pedestrian_Red = 1
        Pedestrian_Green = 0
    }
    basic.pause(2000)
}
// Adds a number to the control variable which allows the IF sections to check if this is true. If it's true, Traffic lights remain red, and the pedestrian light sequence is initiated. When this is done, this variable is turned back down to null, and the main traffic lights resume their job.
// If this variable isn't enabled, then the IF sections are skipped
// 
input.onButtonPressed(Button.B, function () {
    pedestrian_control = 1
})
// Converts Pin numbers into recognizable names
function write_pins_to_names () {
    led.enable(false)
    pins.digitalWritePin(DigitalPin.P16, Main_Red_light)
    pins.digitalWritePin(DigitalPin.P15, Main_Yellow_light)
    pins.digitalWritePin(DigitalPin.P14, Main_Green_light)
    pins.digitalWritePin(DigitalPin.P6, Secondary_Red_Light)
    pins.digitalWritePin(DigitalPin.P5, Secondary_Yellow_Light)
    pins.digitalWritePin(DigitalPin.P4, Secondary_Green_Light)
    pins.digitalWritePin(DigitalPin.P2, Pedestrian_Red)
    pins.digitalWritePin(DigitalPin.P1, Pedestrian_Green)
}
// Converts Pin numbers into recognizable names
basic.forever(function () {
    write_pins_to_names()
})
// Main Chain of Code - Controls both the traffic lights and the Pedestrian lights
basic.forever(function () {
    all_traffic_lights_system()
})
