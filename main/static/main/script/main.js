
// $('video').addEventListener('canplay', function(e) {
//     this.volume = 0.4;
//     this.currentTime = 10;
//     this.play();
// });
$(document).ready(function () {
    // myWebRTC();
    // testWS();
    // testIMG();
    // testFetch('http://localhost:8090/test1.webm');
    modalVideo();
});


function getIMG(img_url, img_parent) {
    var xhr = new XMLHttpRequest;
    xhr.overrideMimeType('image/png');
    xhr.responseType = 'blob';
    i = new Image();
    img_parent.appendChild(i);
    xhr.onload = function () {
        i.src = window.URL.createObjectURL(xhr.response);
        getIMG();
        // setTimeout(getIMG,1000/24);
    };
    getIMG();
    function getIMG() {
        xhr.open('GET', img_url, true);
        xhr.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest');
        xhr.send();
    }

}

function testWS() {
    var ws = new WebSocket("ws://localhost:8000/test");
    ws.send('hello');
    ws.close();
}

function modalVideo() {
    var video_tr = document.body.querySelector('tbody').childNodes;
    for (var i = 0; i < video_tr.length; ++i) {
        video_tr[i].onclick = function () {
            var CameraName = this.querySelector('#CameraName').innerText;
            var CameraURL = this.querySelector('#CameraURL').innerText;
            var CameraID = this.querySelector('#CameraID').innerText;
            // var url = "http://localhost:8000/connect_cam_"+CameraID;
            var url = "http://localhost:8000/socket_cam_"+CameraID;
            var xhr = new XMLHttpRequest;
            xhr.onload = function () {
                getIMG(img_url, img_parent);
                console.log(xhr.response);
            };
            xhr.open('GET', url, true);
            // xhr.setRequestHeader('X-REQUESTED-WITH', 'XMLHttpRequest');
            xhr.send();
            var img_url = "http://localhost:8000/socket_cam_"+CameraID;
            var img_parent = document.body.querySelector('#img');
            document.body.querySelector('#CameraModalLabel').innerText = CameraName;
            $('#CameraModal').modal('show');
        }
    }
}

function myMSE () {
    var assetURL = 'http://localhost:8090/test1.webm';
    console.log(assetURL);
    var ms = new MediaSource;
    var video = document.querySelector('video');
    var mimeCodec = 'video/webm';
    video.src = URL.createObjectURL(ms);
    ms.addEventListener('sourceopen', function (e) {
        var mediaSource = this;
        console.log(mediaSource);
        var sourceBuffer = mediaSource.addSourceBuffer(mimeCodec);
        // sourceBuffer.appendStream(assetURL);
        fetchAB(assetURL, function (buf) {
            sourceBuffer.addEventListener('updateend', function () {
                mediaSource.endOfStream();
                video.play();
                console.log(mediaSource.readyState); // ended
            });
            sourceBuffer.appendBuffer(buf);
        });
    })
}

function fetchAB (url, cb) {
    console.log(url);
    var xhr = new XMLHttpRequest;
    xhr.open('GET', url, true);
    xhr.withCredentials = true;
    xhr.responseType = 'arraybuffer';
    xhr.onload = function () {
        console.log('h');
        console.log(xhr.response);
        cb(xhr.response);
    };
    xhr.send();
}


function testFetch (url) {
    console.log(url);
    var xhr = new XMLHttpRequest;
    xhr.open('GET', url, true);
    xhr.withCredentials = true;
    xhr.overrideMimeType('text/plain; charset=x-user-defined');
    xhr.responseType = 'arraybuffer';
    xhr.onload = function (aEvt) {
        console.log(xhr.response);
    };
    xhr.send();
}

function myWebRTC(){
    var UserMedia = navigator.mediaDevices.getUserMedia({ audio: true, video: true });
    UserMedia.then(function (mediaStream) {
        var video = document.querySelector('video');
        video.src = URL.createObjectURL(mediaStream);
    });
    UserMedia.catch(function(err) { console.log(err.name); });
}