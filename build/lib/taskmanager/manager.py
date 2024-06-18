from taskmanager.database import SessionLocal
from taskmanager.models import Category, Task

class TaskManager:
    def __init__(self):
        self.db = SessionLocal()

    def create_category(self, name):
        category = Category(name=name)
        self.db.add(category)
        self.db.commit()
        return category

    def list_categories(self):
        return self.db.query(Category).all()

    def create_task(self, description, category_id):
        task = Task(description=description, category_id=category_id)
        self.db.add(task)
        self.db.commit()
        return task

    def list_tasks(self, category_id=None):
        if category_id:
            return self.db.query(Task).filter_by(category_id=category_id).all()
        return self.db.query(Task).all()

    def delete_task(self, task_id):
        task = self.db.query(Task).get(task_id)
        if task:
            self.db.delete(task)
            self.db.commit()
