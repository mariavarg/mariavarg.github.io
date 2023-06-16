from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    # Get the uploaded image
    uploaded_image = request.files['image']
    image = Image.open(uploaded_image)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)

    # Choose a font and font size
    font = ImageFont.truetype('arial.ttf', 36)

    # Get the size of the text
    text = 'My Poster'
    text_width, text_height = draw.textsize(text, font)

    # Calculate the x and y coordinates for the text
    x = (image.width - text_width) / 2
    y = (image.height - text_height) / 2

    # Set the text color
    color = (0, 0, 0)

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=color)

    # Save the image
    image.save('static/poster.jpg')

    return 'Image processed successfully'

if __name__ == '__main__':
    app.run(debug=True)
