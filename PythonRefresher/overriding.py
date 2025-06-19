class Skills():
    def __init__(self):
        pass
    def msg(self):
        print ("Mastering Software Fundamentals")

class HR():
    def __init__(self):
        super(HR, self).__init__()
    def msg(self):
        print ("Mastering Human Resources Fundamentals")

communication = HR()
communication.msg()  # Output: Mastering Human Resources Fundamentals
