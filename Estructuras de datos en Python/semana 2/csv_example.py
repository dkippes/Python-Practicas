import csv

#leer un archivo csv
with open('home/aolmedo/coursera/python', 'r') as a_file:
    reader = csv.reader(csvfile)
    for row in reader:
        print(', '.join(row))

#escribir un archivo csv
with open('home/aolmedo/coursera/python', 'a') as a_file:
    write = csv.writer(csvfile)
    writer.writerow(['Pedro', 'Gont', '432556345', 'pgont@gmail.com'])