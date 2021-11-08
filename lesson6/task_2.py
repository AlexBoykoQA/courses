def song_la_la_la(rows_count = 3, count = 3, end = 0):

    rows = []
    for i in range(0, rows_count):
        rows.append( "-".join(['la' for _ in range(0, count)]))

    return "\n".join(rows) + ("!" if end == 1 else ".")


song = song_la_la_la(6, 6, 1)

f = open('results.txt', 'w')
f.write(str(song) + '\n')
f.close()

f = open('results.txt')
for line in f.readlines():
    print(line)
f.close()


f = open("results.txt")
for line in f:
    print(line.rstrip() + "!")


with open('input.txt') as source, open('output.txt', 'w') as destination:
    for line in source:
        destination.write("Number: " + line)

try:
    f = open("input.txt")
    for line in f:
        print(line)
        modified_line = int(line.strip())
        print(modified_line)
except ValueError:
    print("Error")
else:
    print("I did it!")
finally:
    f.close()
