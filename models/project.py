class Project:
    
    def __init__(self, project_id, name, description = ""):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.tasks = []

    def __len__(self):
        return f"➤  number of tasks in project with ID {self.project_id} : {len(self.tasks)}"    
    
    def __str__(self):
        return (
                f"── .✦ project ID : {self.project_id}\n"
                f"── .✦ name : {self.name}\n"
                f"── .✦ description : {self.description}")
        
    def __repr__(self):
        return f"Project({self.project_id},{self.name},{self.description})"
