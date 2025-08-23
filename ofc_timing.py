class Company():
    def toMinutes(self, time):
        time_list = time.split(":")
        time = (int(time_list[0])*60) +int(time_list[1]) 
        return time
    def timeCalculation(self, emp_data):
        dic ={}
        clock_in_time = {}
        for emp_id, action, time in emp_data:
            time_in_minutes = self.toMinutes(time)
            if action == "in":
                clock_in_time[emp_id] = time_in_minutes
            else:
                if emp_id in clock_in_time:
                    dic[emp_id] = time_in_minutes - clock_in_time[emp_id]

        return dic



records = [
    (101, "in", "09:00"),
    (101, "out", "17:00"),
    (102, "in", "10:00"),
    (102, "out", "15:30"),
]

obj = Company()
print(obj.timeCalculation(records))
