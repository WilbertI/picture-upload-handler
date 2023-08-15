from PIL import Image, ImageDraw

# Generates the watermark as a layer to be added over image.
def generate_layer(repeat = True, transparency = 75, offset = (0, 0), boundary = True):
    layer = Image.new('RGBA', (1000, 100), (255, 255, 255, 0)) #Add dimensions
    maxx, maxy = layer.size

    # Add boundary to watermark
    if boundary:
        d_boundary = ImageDraw.Draw(layer)
        d_boundary.line([(0,0), (maxx,0), (maxx, maxy), (0, maxy), (0,0)], fill=(0, 0, 0), width = 5)

    # Generate the Watermark
    #if mark is image
    #    mark = image
    # else # mark is text
    mark = Image.new('RGBA', (100, 100))
    d_mark = ImageDraw.Draw(mark)
    d_mark.text((10, 15), 'Artisan Market', fill = (0, 0, 0))

    drawn = layer.copy()
    drawn.alpha_composite(mark)
    # Repeat Watermark Across Image
    #for x,y in ?
    #    drawn.alpha_composite(i, dest = (x * size, y * size))

    return layer
