from PIL import Image, ImageDraw

def generate_layer(repeat = True, transparency = 75, offset = (0, 0)):
    layer = Image.new('RGBA', (1000, 100), (255, 0, 255, 50)) #Add dimensions

    # Generate the Watermark
    i = Image.new('RGBA', (100, 100), (255, 255, 0, 50))
    d = ImageDraw.Draw(i)
    d.text((10, 15), 'Artisan Market', fill = (255, 255, 255, 255))
    d.text((10, 30), 'Two Ole Bs', fill = (0, 255, 0, 255))

    drawn = layer.copy()
    drawn.alpha_composite(i)
    drawn.alpha_composite(i, dest = (100, 0))
    drawn.alpha_composite(i, dest = (200, 0))
    #drawn = Image.alpha_composite(layer, i)

    # Debug
    layer.show() # Start of image
    i.show()
    #drawn.show() #Single Text Instance
    drawn.show() #Full Watermark

    return layer


# Text (Generated from Value) or Image (Provided)
# Repeat in Pattern or Single Instance
#
#
#
#
#
#
