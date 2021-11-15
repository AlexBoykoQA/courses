
def song_la_la_la(rows_count = 3, count = 3, end = 0):

    rows = []
    for i in range(0, rows_count):
        rows.append( "-".join(['la' for _ in range(0, count)]))

    return "\n".join(rows) + ("!" if end == 1 else ".")

song = song_la_la_la(6, 6 ,1)

#f = open('results.txt')
#f.write(str(song) + '\n')

#for line in f:
    #print(line.rstrip() + "!")

#print("test", "test", file=f)


