class EmptyStrParametersError(Exception):
    pass
    
class InvalidPriorityError(Exception):
    pass 

class InvalidStatusError(Exception):
    pass

class InvalidUrgencyLevelError(Exception):
    pass

class InvalidMenuChoiceError(Exception):
    def __init__(self, menu_choice):
        super().__init__(f"⚠︎ Invalid Menu Choice: '{menu_choice}' is invalid !!! Menu choice must be a valid number.")


class DuplicateIDError(Exception):
    def __init__(self, id_value):
        super().__init__(f"⚠︎ ID '{id_value}' already exists !!!")

class TaskNotFoundError(Exception):
    def __init__(self, task_id):
        super().__init__(f"✘ Not Found Error : Task with ID '{task_id}' not found !")

class ProjectNotFoundError(Exception):
    def __init__(self, project_id):
        super().__init__(f"✘ Not Found Error : Project with ID '{project_id}' not found !")

