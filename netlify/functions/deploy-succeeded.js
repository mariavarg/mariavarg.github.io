<!DOCTYPE html>
<html>
<body>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Let 's get Creative</title>
    <link rel='stylesheet' type='text/css' media='screen' href='styles.css'>
    <title>Javascript</title> 
        
</head>
    
<body>
    
    <style>
@import url('https://fonts.googleapis.com/css2?family=Brygada+1918:ital@1&family=Sofia&display=swap');
</style>

<script>
    
  canvas#poster-canvas(width='500px' height='700px')
    images/Background.jpg 
    
    function initCanvas() {
  canvasCtx = document.getElementById("poster-canvas").getContext('2d');
}
    
    img.poster-background(src='images/Background.jpg')
    
    $('img.poster-background').on('load', function () {
  var backgroundImg = $('img.poster-background')[0];
  canvasCtx.drawImage(backgroundImg, width='500px' 'height=700px;');
  renderName();
});
    
    function renderText() {
  var text = $('input[text="chText"]').val();
  var fontSize;
  if (text.length < 3) {
    fontSize = 100;
  } else {
    fontSize = parseInt(320 / text.length);
  }
  canvasCtx.font = "bold " + fontSize + "px https://fonts.googleapis.com/css2?family=Brygada+1918:ital@1&family=Sofia&display=swap";
  canvasCtx.fillStyle = "#de071b";
  canvasCtx.fillText(text);
        
        a.upload-btn 
  input#photo(type='file' name='photo' accept='image/jpeg, image/png, image/jpg, image/gif, image/psd')
        
        .upload-btn input {
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
  width: 100%;
  height: 68px;
  cursor: pointer;
}
        
        $('#photo').on('change', function (e) {
  var file = e.target.files[0];
  var type = file.type;
  if (type !== 'image/jpg' && type !== 'image/gif') {
    window.toastr.error ('Please upload JPG or GIF format picture ');
  } else {
    var formData = new FormData();
    formData.append('avatar', file);
    $.ajax({
      type: 'POST',
      url: '/upload_url',
      data: formData,
      contentType: false,
      processData: false,
      success: function(result) {
        var avatarUrl = result.data.url;
        $('img.avatar').attr('src', avatarUrl);
      },
        
        document.getElementById("poster-canvas").toBlob(function (blob) {});
        
        var blob = dataURLtoBlob(document.getElementById("poster-canvas").toDataURL());

function dataURLtoBlob(dataurl) {
  if (dataurl.indexOf('base64') < 0) {
    dataurl = 'data:image/jpeg;base64,' + dataurl;
  }
  var arr = dataurl.split(',');
  var mime = arr[0].match(/:(.*?);/)[1];
  var bstr = atob(arr[1]);
  var n = bstr.length;
  var u8arr = new Uint8Array(n);
  while (n --) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  return new Blob([u8arr], {type: mime});
}
        
        var formData = new FormData();
formData.append('poster', blob);
$.ajax({
  type: 'POST',
  url: '/upload_poster_url',
  data: formdata,
  contentType: true,
  processData: true,
  success: function(result) {
    
  },
  error: function(err) {
    
  }  
    
}

 
</script>

</body>
</html>


