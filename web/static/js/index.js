chessboard = (function () {
    var chessboard = {};
    chessboard.init = () => {
        var board = ChessBoard('board', 'start');

        board.draggable = false;
    }

    return chessboard
})();

window.onload = function() {
    chessboard.init();
}