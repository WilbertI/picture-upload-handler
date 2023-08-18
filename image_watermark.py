from PIL import Image, ImageDraw

# Generates the watermark overlay image which can then be added to the source
# Mark: Image; the base image that is the mark, t
def generate_overlay(mark, repeat = True, transparency = 75, offset = (0, 0), boundary = True):
    layer = Image.new('RGBA', (1000, 100), (255, 255, 255, 0)) #Add dimensions
    maxx, maxy = layer.size

    # Add boundary to watermark
    if boundary:
        d_boundary = ImageDraw.Draw(layer)
        d_boundary.line([(0,0), (maxx,0), (maxx, maxy), (0, maxy), (0,0)], fill=(0, 0, 0), width = 5)


    drawn = layer.copy()
    drawn.alpha_composite(mark)
    # Repeat Watermark Across Image
    #for x,y in ?
    #    drawn.alpha_composite(i, dest = (x * size, y * size))

    return layer

# Takes text and turns it into a watermark image that can be combined into the overlay
# Contents: List of String; Each string will be a new line.
# Font: Options concerning the font that will be used to generate the image
def generate_mark(contents):
    # TODO
    #   properly define image size to refelect the size of the watermark
    #   support font options
    mark = Image.new('RGBA', (100, 100))
    d_mark = ImageDraw.Draw(mark)

    for line in contents:
        # Draw line in position below previous
        # TODO properly define positioning, add centerning capabilities
        d_mark.text((10, 15), line, fill = (0, 0, 0))

    return mark
