with open("lesson3-exampletext.txt", "r") as sample_file:
# file öffnen, "r" = read modus ("w" = write)
# = einfachste variante files auszulesen
    content = sample_file.read()
    print(content)
# print(content) = der gesamte content auf einmal (ein string)

with open("lesson3-exampletext.txt", "r") as sample_file_two:
    content_two = sample_file_two.read().splitlines()

    for line in content_two:
        print(line)
        # unterschied vorschleife geht content_two variable durch, zeilenweise (liste von strings)

with open("lesson3-exampletext2.txt", "w") as sample_write: # "w" = write
    sample_write.write("Hallo, das ist ein Test!!!!")
