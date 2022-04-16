if(navigator.webkitGetUserMedia!=null) {
    var options = {
        video:true,
        audio:true
    };

    // запрашиваем доступ к веб-камере
    navigator.webkitGetUserMedia(options,
        function(stream) {
            // получаем тег video
            var video = document.querySelector('video');
            // включаем поток в магический URL
            video.src = window.webkitURL.createObjectURL(stream);
        },
        function(e) {
            console.log("error happened");
        }
    );
}