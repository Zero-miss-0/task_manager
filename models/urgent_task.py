from .task import Task

class UrgentTask(Task):
    
    def __init__(self, urgency_level, project_id, task_id, title, deadline, priority, status):
        super().__init__(project_id, task_id, title, deadline, priority, status)
        self.urgency_level = urgency_level

    def calculate_score(self):
        return f"╰┈➤ˎˊ˗ task '{self.task_id}'score : {self.get_priority() * self.urgency_level * 5}"
    
    def __str__(self):
        return (
            f"── .✦ urgency level : {self.urgency_level}\n" + 
            super().__str__()
            )
    
    def __repr__(self):
        return f"UrgentTask({self.urgency_level},{self.task_id},{self.title},{self.deadline},{self.get_priority()},{self.get_status()},{self.project_id})"