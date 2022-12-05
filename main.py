Pedestrian_Red = 0
Secondary_Red_Light = 0
Main_Red_light = 0
Main_Yellow_light = 0
Main_Green_light = 0
pedestrian_control = 0
Pedestrian_Green = 0
Secondary_Yellow_Light = 0
Secondary_Green_Light = 0
def all_traffic_lights_system():
    global Pedestrian_Red, Secondary_Red_Light, Main_Red_light, Main_Yellow_light, Main_Green_light, pedestrian_control, Pedestrian_Green, Secondary_Yellow_Light, Secondary_Green_Light
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
    # If B button is pressed, the pedestrian_control variable will get a value of one. This will then be recognized by the IF section and the code will divert to and run the line of code inside the IF section
    if pedestrian_control == 1:
        pedestrian_control = 0
        basic.pause(1000)
        Pedestrian_Red = 0
        basic.pause(1000)
        Pedestrian_Green = 1
        music.play_tone(698, music.beat(BeatFraction.BREVE))
        music.play_tone(698, music.beat(BeatFraction.BREVE))
        music.play_tone(698, music.beat(BeatFraction.BREVE))
        music.play_tone(698, music.beat(BeatFraction.BREVE))
        music.play_tone(698, music.beat(BeatFraction.BREVE))
        for index in range(20):
            Pedestrian_Green = 1
            music.play_tone(698, music.beat(BeatFraction.EIGHTH))
            basic.pause(100)
            Pedestrian_Green = 0
            music.play_tone(698, music.beat(BeatFraction.EIGHTH))
            basic.pause(100)
        music.stop_melody(MelodyStopOptions.ALL)
        Pedestrian_Red = 1
        Pedestrian_Green = 0
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
    # If B button is pressed, the pedestrian_control variable will get a value of one. This will then be recognized by the IF section and the code will divert to and run the line of code inside the IF section
    if pedestrian_control == 1:
        pedestrian_control = 0
        basic.pause(1000)
        Pedestrian_Red = 0
        basic.pause(1000)
        Pedestrian_Green = 1
        music.play_tone(698, music.beat(BeatFraction.BREVE))
        music.play_tone(698, music.beat(BeatFraction.BREVE))
        music.play_tone(698, music.beat(BeatFraction.BREVE))
        music.play_tone(698, music.beat(BeatFraction.BREVE))
        music.play_tone(698, music.beat(BeatFraction.BREVE))
        for index2 in range(20):
            Pedestrian_Green = 1
            music.play_tone(698, music.beat(BeatFraction.EIGHTH))
            basic.pause(100)
            Pedestrian_Green = 0
            music.play_tone(698, music.beat(BeatFraction.EIGHTH))
            basic.pause(100)
        music.stop_melody(MelodyStopOptions.ALL)
        Pedestrian_Red = 1
        Pedestrian_Green = 0
    basic.pause(2000)
# Adds a number to the control variable which allows the IF sections to check if this is true. If it's true, Traffic lights remain red, and the pedestrian light sequence is initiated. When this is done, this variable is turned back down to null, and the main traffic lights resume their job.
# If this variable isn't enabled, then the IF sections are skipped
# 

def on_button_pressed_b():
    global pedestrian_control
    pedestrian_control = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

# Converts Pin numbers into recognizable names
def write_pins_to_names():
    led.enable(False)
    pins.digital_write_pin(DigitalPin.P16, Main_Red_light)
    pins.digital_write_pin(DigitalPin.P15, Main_Yellow_light)
    pins.digital_write_pin(DigitalPin.P14, Main_Green_light)
    pins.digital_write_pin(DigitalPin.P6, Secondary_Red_Light)
    pins.digital_write_pin(DigitalPin.P5, Secondary_Yellow_Light)
    pins.digital_write_pin(DigitalPin.P4, Secondary_Green_Light)
    pins.digital_write_pin(DigitalPin.P2, Pedestrian_Red)
    pins.digital_write_pin(DigitalPin.P1, Pedestrian_Green)
# Converts Pin numbers into recognizable names

def on_forever():
    write_pins_to_names()
basic.forever(on_forever)

# Main Chain of Code - Controls both the traffic lights and the Pedestrian lights

def on_forever2():
    all_traffic_lights_system()
basic.forever(on_forever2)
