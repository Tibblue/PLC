import csv


csv_file = open("./datasets/Manga.csv")
csv_reader = csv.reader(csv_file, delimiter=',')


for row in csv_reader:
        string = row[1] + ',' + row[2] + ',' + row[13] + ',' + row[18] + ',' + row[19] + ',' + row[23] + ',' + row[26] 
        print(string)