chessboard = (function () {
    var chessboard = {};
    var board = null;
    chessboard.init = () => {
        board = ChessBoard('board', 'start');
        board.draggable = false;
    }

    chessboard.apply_state = (fen) => {
        let position = ChessBoard.fenToObj(fen);

        board.position(position, true);
    }
    return chessboard
})();

window.onload = function() {
    chessboard.init();
}

$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/test');
    socket.on('fen', function(msg) {
        $('#log').append('<p>Received: ' + msg.data + '</p>');
    });
    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
    $('form#broadcast').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
        return false;
    });
});