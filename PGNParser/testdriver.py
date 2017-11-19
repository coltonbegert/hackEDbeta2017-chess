from chessparser import PGNParser

b = PGNParser("c:\\Users\\RyanH\\Development\\hackEDbeta2017-chess\\Test Data\\ficsgamesdb_2016_blitz2000_nomovetimes_1509742.pgn")
datum = b.parse_next_game()