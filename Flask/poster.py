from PIL import Image, ImageDraw, ImageFont

def process_image(image_file):
    # Open the image
    image = Image.open(image_file)

    # Create an ImageDraw object
    draw = ImageDraw.Draw(image)

    # Choose a font and font size
    font = ImageFont.truetype('ARIAL.TTF', 36)

    # Get the size of the text
    text = 'My Poster'
    text_width, text_height = draw.textsize(text, font=ARIAL.TTF)

    # Calculate the x and y coordinates for the text
    x = (image.width - text_width) / 2
    y = (image.height - text_height) / 2

    # Set the text color
    color = (0, 0, 0)

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=color)

    # Save the image
    output_image_path = 'static/poster.jpg'
    image.save(output_image_path)

    return output_image_path


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
      <a class="nav-link" href="Flask/poster.py">NEXT</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="page20.html">PREVIOUS</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="javascript:history.go(-1)">BACK</a>
    </li>
   </ul>

</nav>
        
        </body>

<audio controls autoplay>
  <source src="Metallica - Fade to Black (Official Video).m4a">

</audio>
