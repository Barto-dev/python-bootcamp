from random import choice

turtle_color_list = [
    "DarkOrchid",
    "MediumPurple",
    "Indigo",
    "MediumSlateBlue",
    "SlateBlue",
    "MediumOrchid",
    "BlueViolet",
    "DarkViolet",
    "DarkMagenta",
    "Purple",
    "MediumVioletRed",
    "DarkRed",
    "Red",
    "OrangeRed",
    "Orange",
    "DarkOrange",
    "Gold",
    "Yellow",
    "GreenYellow",
    "Chartreuse",
    "LawnGreen",
    "Lime",
    "LimeGreen",
    "PaleGreen",
    "SpringGreen",
    "MediumSpringGreen",
    "SeaGreen",
    "ForestGreen",
    "Green",
    "DarkGreen",
    "OliveDrab",
    "DarkOliveGreen",
    "DarkSeaGreen",
    "MediumAquamarine",
    "DarkCyan",
    "Teal",
    "Aqua",
    "Cyan",
    "LightCyan",
    "PaleTurquoise",
    "Aquamarine",
    "Turquoise",
    "MediumTurquoise",
    "DarkTurquoise",
    "CadetBlue",
    "SteelBlue",
    "LightSteelBlue",
    "PowderBlue",
    "LightBlue",
    "SkyBlue",
    "LightSkyBlue",
    "DeepSkyBlue",
    "DodgerBlue",
    "CornflowerBlue",
    "RoyalBlue",
    "Blue",
    "MediumBlue",
    "DarkBlue",
    "Navy",
    "MidnightBlue",
    "Black",
]


def random_rgb():
    r = choice(range(0, 256))
    g = choice(range(0, 256))
    b = choice(range(0, 256))
    rgb = (r, g, b)
    return rgb
