
// $('video').addEventListener('canplay', function(e) {
//     this.volume = 0.4;
//     this.currentTime = 10;
//     this.play();
// });
$(document).ready(function () {
   $('tbody').children('tr').click(function () {
       var CameraName = $(this).children('#CameraName').text();
       var CameraURL = $(this).children('#CameraURL').text();
       $('#CameraModalLabel').text(CameraName);
       $('#CameraModalVideo').children('source').attr('src', CameraURL);
       document.getElementById("CameraModalVideo").play();
       $('#CameraModal').modal('show');
   })
});