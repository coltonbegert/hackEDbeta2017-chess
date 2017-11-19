from chessparser import PGNParser

gameSet = PGNParser("c:\\Users\\RyanH\Development\\hackEDbeta2017-chess\\Test Data\\lichess_db_standard_rated_2017-10.pgn")

write_file = "datums.csv"
with open(write_file, "w") as output:
    try:
        while(True):
            datum = gameSet.parse_next_game()
            if not datum is None:
                output.write(repr(datum) + "\n")
    except ValueError:
        print("Done maybe")
        