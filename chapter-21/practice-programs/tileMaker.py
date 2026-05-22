from PIL import Image

def make_tile(image, num_horizonal, num_vertical):
    image_input = Image.open(image)
    image_width, image_height = image_input.size

    tiled_image = Image.new('RGBA', (image_width*num_horizonal, image_height*num_vertical), 'white')

    for left in range(0, image_width*num_horizonal, image_width):
        for top in range(0, image_height*num_vertical, image_height):
            print(left, top)
            tiled_image.paste(image_input, (left, top))

    return tiled_image

cat_image = make_tile('zophie.png', 6, 10)

cat_image.save('tiled_zophie.png')
