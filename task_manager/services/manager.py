from models import Project, Task, PersonalTask, TeamTask, UrgentTask
from exceptions import (TaskNotFoundError, ProjectNotFoundError, DuplicateIDError)



class TaskManager:
    
    def __init__(self):
        self.projects = []
        self.tasks = []


#project_management


    def add_project(self, project : Project):
        for p in self.projects:
            if p.project_id == project.project_id:
                raise DuplicateIDError(project.project_id)
        self.projects.append(project)

    def show_projects(self):
        if not self.projects:
            print("── .✦ No projects yet")
        else:
            for project in self.projects:
                print(project, "\n ----------------------------")

    def search_project(self, project_id):
        for project in self.projects:
            if project_id == project.project_id:
                return project
        raise ProjectNotFoundError(project_id)

    def edit_project(self, project_id, name, description = ""):
            project = self.search_project(project_id)
            project.name = name
            project.description = description
            return f"❯❯❯❯ Project with ID '{project_id}' successfully edited ✔.✦ ݁˖"
    
    def delete_project(self, project_id):
            project = self.search_project(project_id)
            self.projects.remove(project)
            self.tasks = [task for task in self.tasks if task.project_id != project_id]
            return f"❯❯❯❯ Project with ID '{project_id}' successfully deleted ✔.✦ ݁˖"
    
    def total_project_tasks(self, project_id):
            project = self.search_project(project_id)
            print(project.__len__())
    
#task_management


    def add_task(self, task):
        for t in self.tasks:
            if t.task_id == task.task_id:
                raise DuplicateIDError(task.task_id)
        self.tasks.append(task)
 
    def show_tasks(self):
        if not self.tasks:
            print("── .✦ No tasks yet")
        else:
            for task in self.tasks:
                print(task, "\n ----------------------------")
    
    def show_project_tasks(self, project_id):
        project = self.search_project(project_id)
        if not project.tasks:
            print("── .✦ No project tasks yet")
        for task in project.tasks:
            print(task, "\n ----------------------------")

    def search_task(self, task_id):
        for task in self.tasks:
            if task_id == task.task_id:
                return task
        raise TaskNotFoundError(task_id)
    
    def edit_task(self, task_id, title, deadline, priority):
            task = self.search_task(task_id)
            task.title = title
            task.deadline = deadline
            task.set_priority(priority)       
            return f"❯❯❯❯ Task with ID '{task_id}' successfully edited ✔.✦ ݁˖"
        
    def delete_task(self, task_id):
            task = self.search_task(task_id)
            self.tasks.remove(task)
            project_id = task.project_id
            project = self.search_project(project_id)
            project.tasks.remove(task)
            return f"❯❯❯❯ Task with ID '{task_id}' successfully deleted ✔.✦ ݁˖"
        
    def change_status(self, task_id):
            task = self.search_task(task_id)
            task.set_status("completed")
            return f"❯❯❯❯ Task status with ID '{task_id}' successfully changed(completed) ✔.✦ ݁˖" 
    
    def show_tasks_scores(self):
        if len(self.tasks) == 0:
             print("╰┈➤ˎˊ˗ score :")
             print("➤  there is no task yet.")
        for task in self.tasks:
            print(task.calculate_score(), "\n ----------------------------")