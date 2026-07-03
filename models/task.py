class Task:

    def __init__(self, project_id, task_id , title, deadline, priority, status):
        self.task_id = task_id
        self.title = title
        self.deadline = deadline
        self.__priority = priority
        self.__status = status
        self.project_id = project_id

    def get_priority(self):
        return self.__priority
    
    def set_priority(self, priority):
        self.__priority = priority
        return "❯❯❯❯ Priority set successfully ✔.✦ ݁˖"
    
    def get_status(self):
        return self.__status
    
    def set_status(self, status):
        self.__status = status
        return "❯❯❯❯ Status set successfully ✔.✦ ݁˖"
    
    def calculate_score(self):
        pass

    def __str__(self):
        return (
            f"── .✦ task ID : {self.task_id}\n"
            f"── .✦ title : {self.title}\n"
            f"── .✦ deadline : {self.deadline}\n"
            f"── .✦ priority : {self.__priority}\n"
            f"── .✦ status : {self.__status}\n"
            f"── .✦ project ID : {self.project_id}"
        )
    
    def __repr__(self):
        return f"Task({self.project_id},{self.task_id},{self.title},{self.deadline},{self.__priority},{self.__status})"
