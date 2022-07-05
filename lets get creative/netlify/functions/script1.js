<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Let 's get Creative</title>
    <link rel='stylesheet' type='text/css' media='screen' href='lets get creative/css/styles.css'>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Sofia&display=swap');
        </style>
    </head>

<body>
         
            <script>
const quoteText = document.getElementById("quote__text");
const image_input = document.querySelector("#image_input");
var uploaded_image = "";

image_input.addEventListener("change", function() {
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    const uploaded_image = reader.result;
    document.querySelector("#display-image").style.backgroundImage = `url(${uploaded_image})`;
  });
  reader.readAsDataURL(this.files[0]);
});

</script>

</body>
</html>
