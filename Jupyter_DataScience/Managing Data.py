import csv

%precision 2

with open('mpg.csv') as csvfile:
    
    mpg = list(csv.DictReader(csvfile)) #Here use method DictReader with arg

print (mpg[:3])