from flask import Flask, render_template, request
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

def process_image(image_file):
    # Code for processing the image (as shown in step 1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_image', methods=['POST'])
def process_image_route():
    # Get the uploaded image
    uploaded_image = request.files['image']

    # Process the image and get the path of the processed image
    output_image_path = process_image(uploaded_image)

    return output_image_path

if __name__ == '__main__':
    app.run(debug=True)

