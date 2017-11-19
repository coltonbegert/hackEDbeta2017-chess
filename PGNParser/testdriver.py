from chessparser import PGNParser

gameSet = PGNParser("c:\\Users\\RyanH\Development\\hackEDbeta2017-chess\\Test Data\\lichess_db_standard_rated_2014-02.pgn")

write_file = "datums.csv"
with open(write_file, "w") as output:
    try:
        lineCount = 0
        lines = []
        while(True):
            datum = gameSet.parse_next_game()
            if not datum is None:
                lineCount += 1
                lines.append(repr(datum))
                if(lineCount >= 1000):
                    output.write("\n".join(lines))
                    lineCount = 0
                    lines = []
    except ValueError:
        output.write("\n".join(lines))
        print("Done maybe")
        