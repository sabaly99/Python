import csv 


with open ('/home/sabaly/Documents/poiiihts.csv', 'r') as file:
    csv_reader = csv.reader(file)


    for line in csv_reader:
        print(line[3])