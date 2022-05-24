def on_button_pressed_a():
    colorbit_51bit.show_color(colorbit.rgb(TCS34725.get_sensor_data(RGB.RED),
            TCS34725.get_sensor_data(RGB.GREEN),
            TCS34725.get_sensor_data(RGB.BLUE)))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    colorbit_51bit.clear()
input.on_button_pressed(Button.B, on_button_pressed_b)

colorbit_51bit: colorbit.Strip = None
TCS34725.start(TCS34725_ATIME.TIME_2_4_MS, TCS34725_AGAIN.GAIN_1X)
colorbit_51bit = colorbit.init_color_bit(DigitalPin.P2, BitColorMode.RGB)
colorbit_51bit.set_brightness(64)
colorbit_51bit.show_color_icon(ColorIcon.YES, colorbit.colors(BitColors.INDIGO))
basic.pause(500)
colorbit_51bit.clear()
colorbit_51bit.show()