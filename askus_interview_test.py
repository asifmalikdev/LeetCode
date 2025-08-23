'''A company wants to track when employees clock in and clock out. 
Write a Python function that takes a list of tuples (employee_id, action, time) 
where action is "in" or "out", and returns the total hours each employee worked in a day.'''
class Company:
    def to_minutes(self, t: str) -> int:
        h, m = map(int, t.split(":"))
        return h * 60 + m

    def timeCalculation(self, emp_data):
        dic = {}
        clock_in_time = {}

        for emp_id, action, time in emp_data:
            time_in_minutes = self.to_minutes(time)

            if action == "in":
                clock_in_time[emp_id] = time_in_minutes
            elif action == "out":
                if emp_id in clock_in_time:
                    worked = time_in_minutes - clock_in_time[emp_id]
                    dic[emp_id] = dic.get(emp_id, 0) + worked
                    del clock_in_time[emp_id]
                    
        return {emp: round(total / 60, 2) for emp, total in dic.items()}


records = [
    (101, "in", "09:00"),
    (101, "out", "17:00"),
    (102, "in", "10:00"),
    (102, "out", "15:30"),
]

obj = Company()
print(obj.timeCalculation(records))
