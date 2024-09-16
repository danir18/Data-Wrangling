import csv

def main():
    with open("census_headers(in).csv") as file:
        reader = csv.DictReader(file)
        with open('census_cleansed.csv','w',newline='') as output:
            writer = csv.DictWriter(output, fieldnames=reader.fieldnames)
            writer.writeheader()

        
            for row in reader:
                locality = row["locality"]
                locality = locality.replace("Rural", "").replace("Municipality", "")
                row["locality"] = locality
                writer.writerow(row)
                



main()