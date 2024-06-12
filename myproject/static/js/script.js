let timer;
let running = false;
let time = 0;

function updateTime() {
    let hours = Math.floor(time / 3600);
    let minutes = Math.floor((time % 3600) / 60);
    let seconds = time % 60;
    document.getElementById('timer').innerText = 
        (hours < 10 ? "0" + hours : hours) + ":" + 
        (minutes < 10 ? "0" + minutes : minutes) + ":" + 
        (seconds < 10 ? "0" + seconds : seconds);
}

document.getElementById('start').addEventListener('click', function() {
    if (!running) {
        running = true;
        timer = setInterval(function() {
            time++;
            updateTime();
        }, 1000);
    }
});

document.getElementById('pause').addEventListener('click', function() {
    if (running) {
        running = false;
        clearInterval(timer);
    }
});

document.getElementById('reset').addEventListener('click', function() {
    running = false;
    clearInterval(timer);
    time = 0;
    updateTime();
});

$('#gifModal').on('show.bs.modal', function (event) {
    let button = $(event.relatedTarget);
    let gifUrl = button.data('gif');
    let modal = $(this);
    modal.find('.modal-body img').attr('src', gifUrl);
});
