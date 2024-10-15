import random

def generate_bright_random_color():
    # Generate a random hue (0-360)
    hue = random.randint(0, 360)
    # Set saturation and lightness for bright colors
    saturation = random.uniform(0.7, 1)  # High saturation
    lightness = random.uniform(0.5, 0.7)  # Medium lightness
    return f'hsl({hue}, {saturation * 100}%, {lightness * 100}%)'
