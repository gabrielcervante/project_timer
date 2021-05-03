import sys
import getopt
from csv_methods import Csv_Methods
from time_methods import Time_Methods

csv_methods = Csv_Methods()
time_methods = Time_Methods()

#Gets all the arguments less the first that is the file name
argv = sys.argv[1:]

#Getopt needed variabel that get args and see if it is a known argument
options, args = getopt.getopt(argv, "n:t:p:r:")

#For loop to say what to do when each argument is called
for option, arg in options:
    if option in ['-n']:
        csv_methods.write_new_csv_file(arg, time_methods.get_current_timestamp())
    elif option in ['-t']:
        print(arg + ":" + " " + time_methods.calculate_work_time(arg))
    elif option in ['-p']:
        csv_methods.add_pause(arg, time_methods.get_current_timestamp())
    elif option in ['-r']:
        csv_methods.add_work(arg, time_methods.get_current_timestamp())
