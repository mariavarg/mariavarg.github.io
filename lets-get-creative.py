 <py-script>
pip install Pillow==5.3.0

from PIL import Image, ImageDraw, ImageFont

<form>
  <label for="image">Choose an image:</label>
  <input type="file" id="image" accept="image/*">
  <br>
  <input type="button" value="Search Google for an Image" onclick="searchGoogle()">
</form>

# Open the image
image = Image.open('image.jpg')

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
image.save('poster.jpg')
