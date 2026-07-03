from .task import Task

class TeamTask(Task):
    
    def __init__(self, team_size, project_id, task_id, title, deadline, priority, status):
        super().__init__(project_id, task_id, title, deadline, priority, status)
        self.team_size = team_size

    def calculate_score(self):
        return f"╰┈➤ˎˊ˗ task '{self.task_id}'score : {self.get_priority() * self.team_size}"
    
    def __str__(self):
        return (
            f"── .✦ team size : {self.team_size}\n" + 
            super().__str__()
            )
    
    def __repr__(self):
        return f"TeamTask({self.team_size},{self.task_id},{self.title},{self.deadline},{self.get_priority()},{self.get_status()},{self.project_id})"