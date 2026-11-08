import csv

with open("csvtext.csv") as csvfile:
    csvreader = csv.reader(csvfile)

    for line in csvreader:
        print(line)


#to get 2nd in line another way is
with open("csvtext.csv") as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    for line in csvreader:
        print(line)



with open("csvtext.csv") as csvfile:
     csvreader = csv.reader(csvfile)

import csv

with open("csvtext.csv", 'w', newline='') as newfile:
    csvwriter = csv.writer(newfile, delimiter='\t')

    for line in csvreader:
        csvwriter.writerow(line)


with open("csvtext.csv") as csvfile:
    csvreader = csv.Dictreader(csvfile)

    for line in csvreader:
        print(line['email'])

#this code deletes email row
# with open('new_names.csv', 'w') as new_file:
#     fieldnames = ['first_name', 'last_name']
#
#     csv_writer = csv.DictWriter(
#         new_file,
#         fieldnames=fieldnames,
#         delimiter='\t'
#     )
#
#     csv_writer.writeheader()
#
#     for line in csv_reader:
#         del line['email']
#         csv_writer.writerow(line)





