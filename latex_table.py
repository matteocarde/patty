import csv


def main():
    file = "experiments/results.csv"

    f = open(file, "r")
    csvString = f.read()
    f.close()

    csvReader = csv.reader(csvString)




if __name__ == '__main__':
    main()
