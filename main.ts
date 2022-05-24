input.onButtonPressed(Button.A, function () {
    colorbit_51bit.showColor(colorbit.rgb(TCS34725.getSensorData(RGB.RED), TCS34725.getSensorData(RGB.GREEN), TCS34725.getSensorData(RGB.BLUE)))
})
input.onButtonPressed(Button.B, function () {
    colorbit_51bit.clear()
})
let colorbit_51bit: colorbit.Strip = null
TCS34725.start(TCS34725_ATIME.TIME_2_4_MS, TCS34725_AGAIN.GAIN_1X)
colorbit_51bit = colorbit.initColorBit(DigitalPin.P2, BitColorMode.RGB)
colorbit_51bit.setBrightness(64)
colorbit_51bit.showColorIcon(ColorIcon.Yes, colorbit.colors(BitColors.Indigo))
basic.pause(500)
colorbit_51bit.clear()
colorbit_51bit.show()
