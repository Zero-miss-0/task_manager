def completed_tasks(tasks):
        completed = [task for task in tasks if task.get_status() == "completed"]
        if not completed:
            return f"➤  there is no completed task."
        return (f"➤  number of completed tasks : ""\n ----------------------------\n".join(str(task) for task in completed))


def pending_tasks(tasks):
        pending = [task for task in tasks if task.get_status() == "pending"]
        if not pending:
             return f"➤  there is no pending task."
        return (f"➤  number of pending tasks : ""\n ----------------------------\n".join(str(task) for task in pending))


def total_tasks(tasks):
    return f"➤  total tasks : {len(tasks)}"


def project_progress(tasks):
    if len(tasks) == 0:
        return "➤  project progress : 0 %"
    else:
        total = len(tasks)
        completed = len([task for task in tasks if task.get_status() == "completed"])
        progress = (completed / total) * 100
        return f"➤  project progress : {progress}"
    
def sorted_by_priority(tasks):
    sorted_tasks = sorted(tasks, key=lambda task: task.get_priority(), reverse=True)
    print("➤  sorted tasks:")
    for task in sorted_tasks:
        print(task, "\n ----------------------------")
    if len(tasks) == 0:
        print("➤  there is no task yet.")
    

