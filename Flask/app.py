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

<!DOCTYPE html>

<meta name="viewport" content="width=device-width-10, initial-scale=1.0">
<html lang="en">
    <head>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
        <link href="styles1.css" rel="stylesheet">
        <meta name="google-site-verification" content="lx9Buu8regrl5IfmZntGJ-oDlfmAMPucGl-y4_8W9RE" />
        <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest"> </script>
        <!-- Make sure your page supports utf-8 characterset. -->

      <style>
.content {
  max-width: 500px;
  margin: auto;
}</style>
            
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
    <div class="content">
<!-- Page content -->
      
    <body>

 <nav class="navbar navbar-expand-bg bg-dark navbar-dark">
<ul class="navbar-nav">
    <li class="nav-item">
      <a class="nav-link" href="index.html">HOME!</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="contactme.html">CONTACT</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="about.html">ABOUT</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="about.html">NEXT</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="Iphigeneia.html">PREVIOUS</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="javascript:history.go(-1)">BACK</a>
    </li>
   </ul>

</nav>
        
        </body>

</html>
