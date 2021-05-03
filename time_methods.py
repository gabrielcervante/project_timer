import re
from datetime import datetime
from datetime import timedelta
from csv_methods import Csv_Methods

class Time_Methods():

    #This funcion get the current timestamp
    def get_current_timestamp(self):
        now = datetime.now()
        current_timestamp = datetime.timestamp(now)
        
        return current_timestamp

    #This function calculate the worked time
    def calculate_work_time(self, project_name):
        csv_reader = Csv_Methods()
        get_last_work_time = csv_reader.read_csv_file(project_name)

        now = datetime.now()
        current_timestamp = datetime.timestamp(now)
        worked_time = current_timestamp - float(get_last_work_time[-1][0])
        timestamp_to_date = timedelta(seconds=worked_time)

        get_corret_time_format = re.search("(.*)\.", str(timestamp_to_date))

        return get_corret_time_format.group(1)

