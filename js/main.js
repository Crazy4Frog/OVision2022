let container = document.querySelector('div#interactive')
let canvas = document.querySelector('canvas');
let video = document.querySelector('video');
let ctx = canvas.getContext('2d');
let isCanvasResized = false
new ResizeSensor(container, Program)

if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({video: true}).then(function (stream) {
        video.srcObject = stream;
    }).catch(function (error) {
        console.log("Something went wrong!");
    })
} else {
    console.log("getUserMedia not supported!")
}
function resizeCanvas() {
    canvas.width = container.offsetWidth;
    canvas.height = container.offsetHeight;
    isCanvasResized = true;
}
function drawRectangle(point1, point3, color){
    ctx.beginPath()
    ctx.strokeStyle = color;
    ctx.moveTo(point1.x, point1.y);
    ctx.lineTo(point3.x, point1.y);
    ctx.lineTo(point3.x, point3.y);
    ctx.lineTo(point1.x, point3.y);
    ctx.lineTo(point1.x, point1.y);
    ctx.stroke();
}
function Program(){
    resizeCanvas();
    // drawRectangle({x: 50, y: 30}, {x: 400, y: 200}, 'red')
}
