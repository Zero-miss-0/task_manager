from models.project import Project
from models.personal_task import PersonalTask
from models.team_task import TeamTask
from models.urgent_task import UrgentTask
from services.manager import TaskManager
from services.reports import completed_tasks, pending_tasks, total_tasks, project_progress, sorted_by_priority
from utils.validators import (validate_str_parameters, validate_priority, 
                              validate_status, validate_urgency_level, )
from exceptions.custom_errors import (
    InvalidMenuChoiceError,
    InvalidUrgencyLevelError,
    TaskNotFoundError,
    ProjectNotFoundError,
    InvalidPriorityError,
    InvalidStatusError,
    EmptyStrParametersError, 
    DuplicateIDError)



def print_menu():
    print("""
╔══════════════════════════════════════╗
║    << Task & Project Manager >>      ║
╠══════════════════════════════════════╣
║  Project Management :                ║
║   1. Add Project                     ║
║   2. Show Projects                   ║
║   3. Edit Project                    ║
║   4. Delete Project                  ║
╠══════════════════════════════════════╣
║  Task Management :                   ║
║   5. Add Task                        ║
║   6. Show All Tasks                  ║
║   7. Show Project Tasks              ║
║   8. Search Task                     ║
║   9. Edit Task                       ║
║  10. Delete Task                     ║
║  11. Change Task Status              ║
╠══════════════════════════════════════╣
║  Reports :                           ║
║  12. Completed Tasks                 ║
║  13. Pending Tasks                   ║
║  14. Total Task Count                ║
║  15. Tasks Per Project               ║
║  16. Project Progress (%)            ║
║  17. Sort Tasks by Priority          ║
║  18. Show Scores                     ║
╠══════════════════════════════════════╣
║   0. Exit                            ║
╚══════════════════════════════════════╝""")


manager = TaskManager()

def get_int(prompt):
    raw = input(prompt).strip()
    if not raw.lstrip("-").isdigit():
        raise ValueError(f"⚠︎ Invalid Input : '{raw}' is not a number !!! Enter a number.")
    return int(raw)


#  Project handlers


def handle_add_project():
    try:
        project_id = get_int(".project ID:")
        name = validate_str_parameters(input("..Name:"))
        description = input("...Description:")
        project = Project(project_id, name, description)
        manager.add_project(project)
        print(f"❯❯❯❯ project with ID '{project_id}' added ✔.✦ ݁˖")
    except (EmptyStrParametersError, ValueError, AttributeError, DuplicateIDError) as e:
        print(e)
    
def handle_show_projects():
    manager.show_projects()

def handle_edit_project():
    try:
        project_id = get_int(".project ID:")
        manager.search_project(project_id)
        name = validate_str_parameters(input("..New name:"))
        description = input("...New description:")
        print(manager.edit_project(project_id, name, description))
    except (EmptyStrParametersError, ValueError, AttributeError, ProjectNotFoundError) as e:
        print(e)

def handle_delete_project():
    try:
        project_id = get_int("project ID:")
        manager.search_project(project_id)
        print(manager.delete_project(project_id))
    except ProjectNotFoundError as e:
        print(e)


#  Task helpers


def pick_task_type():
    print("Task type:\n  1. Personal\n  2. Team\n  3. Urgent")
    menu_choice = get_int("────────── Choice: ")
    if menu_choice not in (1, 2, 3):
        raise InvalidMenuChoiceError(menu_choice)
    return menu_choice

def build_task(project_id, task_id, title, deadline, priority, status):
        task_type = pick_task_type()
        if task_type == 1:
            owner_name = validate_str_parameters(input(".......Owner name: ")).strip()
            return PersonalTask(owner_name, project_id, task_id, title, deadline, priority, status)
        elif task_type == 2:
            team_size = get_int(".......Team size: ")
            return TeamTask(team_size, project_id, task_id, title, deadline, priority, status)
        else:
            urgency_level = validate_urgency_level(input(".......Urgency level: "))
            return UrgentTask(urgency_level, project_id, task_id, title, deadline, priority, status)


#Task handlers


def handle_add_task():
    try:
        project_id = get_int(".project ID:")
        project = manager.search_project(project_id)
        task_id = get_int("..Task ID:")
        title = validate_str_parameters(input("...Title:"))
        deadline = get_int("....Deadline:")
        priority = validate_priority(input(".....Priority:"))
        status = validate_status(input("......Status(pending or completed):"))
        task = build_task(project_id, task_id, title, deadline, priority, status)
        manager.add_task(task)
        project.tasks.append(task)
        print(f"❯❯❯❯ Task with Project ID '{project_id}' added ✔.✦ ݁˖")
    except (InvalidPriorityError, InvalidStatusError, 
            EmptyStrParametersError, ValueError, AttributeError, TypeError, 
            ProjectNotFoundError, InvalidMenuChoiceError, 
            DuplicateIDError, InvalidUrgencyLevelError) as e:
        print(e)

def handle_show_tasks():
    manager.show_tasks()

def handle_show_project_tasks():
    try:
        project_id = get_int("project ID:")
        manager.show_project_tasks(project_id)
    except (ProjectNotFoundError, ValueError) as e:
        print(e)

def handle_search_task():
    try:
        task_id = get_int("Task ID:")
        print(manager.search_task(task_id))
    except (TaskNotFoundError, ValueError) as e:
        print(e)

def handle_edit_task():
    try:
        task_id = get_int("Task ID:")
        manager.search_task(task_id)
        title = validate_str_parameters(input("New Title:"))
        deadline = get_int("New Deadline:")
        priority = validate_priority(input("New Priority:"))
        print(manager.edit_task(task_id, title, deadline, priority))        
    except (TaskNotFoundError, ValueError, TypeError, AttributeError, InvalidPriorityError, EmptyStrParametersError) as e:
        print(e)

def handle_delete_task():
    try:
        task_id = get_int("Task ID:")
        print(manager.delete_task(task_id))
    except (TaskNotFoundError, ValueError) as e:
        print(e)
    
def handle_change_status():
    try:
        task_id = get_int("Task ID:")
        print(manager.change_status(task_id))
    except (TaskNotFoundError, ValueError) as e:
        print(e)


#Report handlers


def handle_completed_tasks():
    tasks = manager.tasks
    print(completed_tasks(tasks))

def handle_pending_tasks():
    tasks = manager.tasks
    print(pending_tasks(tasks))

def handle_total_tasks():
    tasks = manager.tasks
    print(total_tasks(tasks))

def handle_total_project_tasks():
    try:
        project_id = get_int("project ID:")
        manager.search_project(project_id)
        manager.total_project_tasks(project_id)
    except (ProjectNotFoundError, ValueError) as e:
        print(e)

def handle_project_progress():
    tasks = manager.tasks
    print(project_progress(tasks))

def handle_sorted_by_priority():
    tasks = manager.tasks
    sorted_by_priority(tasks)

def handle_show_tasks_scores():
    manager.show_tasks_scores()



#  Main loop


def main():
    print("Welcome to the Task & Project Manager!")
    while True:
        print_menu()
        try:
            choice = get_int("────────── Enter choice: ")
            if choice == 0:
                print("Thank you for using task and project management ♡︎ \n Have a wonderful time!")
                break
            if choice == 1:
                handle_add_project()
            elif choice == 2:
                handle_show_projects()
            elif choice == 3:
                handle_edit_project()
            elif choice == 4:
                handle_delete_project()
            elif choice == 5:
                handle_add_task()
            elif choice == 6:
                handle_show_tasks()
            elif choice == 7:
                handle_show_project_tasks()
            elif choice == 8:
                handle_search_task()
            elif choice == 9:
                handle_edit_task()
            elif choice == 10:
                handle_delete_task()
            elif choice == 11:
                handle_change_status()
            elif choice == 12:
                handle_completed_tasks()
            elif choice == 13:
                handle_pending_tasks()
            elif choice == 14:
                handle_total_tasks()
            elif choice == 15:
                handle_total_project_tasks()
            elif choice == 16:
                handle_project_progress()
            elif choice == 17:
                handle_sorted_by_priority()
            elif choice == 18:
                handle_show_tasks_scores()
        except (InvalidMenuChoiceError, ValueError) as e:
            print(e)
        finally:
            print(input("\nPress Enter to continue..."))



if __name__ == "__main__":
    main()
