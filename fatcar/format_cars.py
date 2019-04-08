import csv

car_names = []
with open("csv_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    for item in reader:
        car_names.append("{} {}".format(item[1].title(), item[2].title()))


# get rid of duplicates
car_names = list(set(car_names))

print(car_names)

