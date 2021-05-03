import csv

class Csv_Methods():

    #Function to create new csv file to store user project times
    def write_new_csv_file(self, project_name, start_time):
        with open(project_name + '.csv', 'w', newline='') as csv_file:
            fieldnames = ['work', 'pause']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerow({'work': start_time})

    #Function to add a new time to csv file
    def add_work(self, project_name, new_time):
        with open(project_name + ".csv", 'a', newline='') as csv_file:
            fieldnames = ['work', 'pause']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'work': new_time})

    #Function to add a new pause to csv file
    def add_pause(self, project_name, pause):
        with open(project_name + ".csv", 'a', newline='') as csv_file:
            fieldnames = ['work', 'pause']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writerow({'pause': pause})

    #Function to read the csv file and get put it in a list
    def read_csv_file(self, project_name):
        with open(project_name + '.csv', newline='') as csv_file:
            reader = csv.reader(csv_file)
            data = list(reader)
            return data
