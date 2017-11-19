from chessparser import PGNParser

b = PGNParser("c:\\Users\\RyanH\Development\\hackEDbeta2017-chess\\Test Data\\lichess_db_standard_rated_2017-10.pgn")

datums = []

while(True):
    datum = b.parse_next_game()
    if not datum is None:
        datums.append(datum)