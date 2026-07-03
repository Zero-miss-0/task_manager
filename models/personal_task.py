from .task import Task

class PersonalTask(Task):
    
    def __init__(self,owner_name, project_id, task_id, title, deadline, priority, status):
        super().__init__(project_id, task_id, title, deadline, priority, status)
        self.owner_name = owner_name

    def calculate_score(self):
        return f"╰┈➤ˎˊ˗ task '{self.task_id}' score : {self.get_priority() * 10}"
    
    def __str__(self):
        return (
            f"── .✦ owner name : {self.owner_name}\n" +
            super().__str__()
            )
    
    def __repr__(self):
        return f"PersonalTask({self.owner_name},{self.task_id},{self.title},{self.deadline},{self.get_priority()},{self.get_status()},{self.project_id})"