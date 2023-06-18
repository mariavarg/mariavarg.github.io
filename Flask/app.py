from PIL import Image, ImageDraw, ImageFont

def process_image(image_file):
    # Open the image
    image = Image.open(image_file)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)

    # Choose a font and font size
    font = ImageFont.truetype('arial.ttf', 36)

    # Get the size of the text
    text = 'My Poster'
    text_width, text_height = draw.textsize(text, font=font)

    # Calculate the x and y coordinates for the text
    x = (image.width - text_width) / 2
    y = (image.height - text_height) / 2

    # Set the text color
    color = (0, 0, 0)

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=color)

    # Save the image
    output_image_path = '/workspaces/75952007/Flask/static/images/poster.jpg'
    image.save(output_image_path)

    return output_image_path
