import json

class Task:
    #title-a short description of the task
    #description - detailed description of the task
    #status - bool if task is complete or not

    def __init__(self, title, description=None, status=False):
        self.title=title
        self.description=description
        self.status=status

    def mark_complete(self):
        self.status=True

    def __str__(self):
        if self.status:
            return f"{self.title} is complete. Keep up the good work."

class ToDoList:

    def add_task(self, task):
        try:
            with open('todos.txt', 'r') as file:
                todos=json.load(file)
        except FileNotFoundError:
            todos=[]

        todos.append({'title':task.title, 'description':task.description, 'status':task.status})

        with open('todos.txt', 'w') as file:
            json.dump(todos, file, indent=2)


    def remove_task(self,task):
        try:
            with open('todos.txt', 'r') as file:
                todos=json.load(file)
        except FileNotFoundError:
            todos=[]

        tasks_to_keep=[]
        for t in todos:
            if t['title'] !=task.title:
                tasks_to_keep.append(t)

        with open('todos.txt', 'w') as file:
            json.dump(todos, file, indent=2)

    def mark_complete(self,task):
        try:
            with open('todos.txt', 'r') as file:
                todos=json.load(file)
        except FileNotFoundError:
            todos=[]


        for t in todos:
            if t['title'] == task.title:
                t['status']=True

        with open('todos.txt', 'w') as file:
            json.dump(todos, file, indent=2)

    def display_task(self):
        try:
            with open('todos.txt', 'r') as file:
                todos=json.load(file)
        except FileNotFoundError:
            todos=[]

        for t in todos:
            status='Complete' if t['status'] else 'Incomplete'
            print (f"Title: {t['title']}\nDescription: {t['description']}\nStatus: {t['status']}\n")

    def get_pending(self):
        try:
            with open('todos.txt', 'r') as file:
                todos=json.load(file)
        except FileNotFoundError:
            todos=[]

        pending_tasks=[]

        for t in todos:
            if not t['status']:
                pending_tasks.append(t)

        if not pending_tasks:
            print("You have no task to complete.")

        for t in pending_tasks:
            print(f"Title: {t['title']}\nDescription: {t['description']}\nStatus: {t['status']}\n")

    def get_completed_tasks(self):
        try:
            with open('todos.txt', 'r') as file:
                todos = json.load(file)
        except FileNotFoundError:
            todos = []

        completed_tasks = []

        for t in todos:
            if t['status']:
                completed_tasks.append(t)

        if not completed_tasks:
            print("You have not completed any tasks yet, get on it..")
            return

        for t in completed_tasks:
            print(f"Title: {t['title']}\nDescription: {t['description']}\nStatus: Complete\n")


todo_list=ToDoList()
task1=Task('Upload to Git', 'Upload the project to my GitHub')
todo_list.add_task(task1)

todo_list.get_pending()

todo_list.mark_complete(task1)
todo_list.get_pending()