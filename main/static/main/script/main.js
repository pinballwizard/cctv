
// $('video').addEventListener('canplay', function(e) {
//     this.volume = 0.4;
//     this.currentTime = 10;
//     this.play();
// });
$(document).ready(function () {
    myWebRTC();
    $('tbody').children('tr').click(function () {

        var CameraName = $(this).children('#CameraName').text();
        var CameraURL = $(this).children('#CameraURL').text();
        $('#CameraModalLabel').text(CameraName);
        $('#CameraModalVideo').children('source').attr('src', CameraURL);
        document.getElementById("CameraModalVideo").play();
        $('#CameraModal').modal('show');
    })
});

function myWebRTC(){
    var UserMedia = navigator.mediaDevices.getUserMedia({ audio: true, video: true });
    UserMedia.then(function (mediaStream) {
        var video = document.querySelector('video');
        video.src = URL.createObjectURL(mediaStream);
    });
    UserMedia.catch(function(err) { console.log(err.name); });
}