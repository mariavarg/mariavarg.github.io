from flask import Flask, render_template
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_image')
def process_image():
    image_file = 'Flask/static/images/Desdemona by mariavarg.png'

    # Open the image
    image = Image.open(image_file)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)

    # Choose a font and font size
    font = ImageFont.truetype('ARIAL.TTF', 36)

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
    output_image_path = 'static/poster.png'
    image.save(output_image_path)

    return render_template('result.html', image_path=output_image_path)

if __name__ == '__main__':
    app.run()

