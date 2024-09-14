from fastapi import FastAPI
from core.utils import json_to_dict_list, update_json_file
import os
from typing import Optional

# Получаем путь к директории текущего скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Переходим на уровень выше
parent_dir = os.path.dirname(script_dir)

# Получаем путь к JSON
path_to_json = os.path.join(parent_dir, 'tasks.json')

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Привет, это наши задания!"}

@app.get("/tasks")
def get_all_tasks():
    tasks = json_to_dict_list(path_to_json)
    return tasks

@app.get("/tasks/{id}")
def get_all_tasks_id(id: int):
    tasks = json_to_dict_list(path_to_json)
    return_list = []
    for task in tasks:
        if task["id"] == id:
            return_list.append(task)
    return return_list

@app.post("/task")
def add_task(task: dict):
    current_tasks = json_to_dict_list(path_to_json)
    # task["id"] = f"task{len(current_tasks)}"
    current_tasks.append(task)
    update_json_file(path_to_json, current_tasks)
    return {"message": "Задача успешно добавлена", "task": task}

@app.delete("/task/{task_id}")
def delete_task(id: int):
    current_tasks = json_to_dict_list(path_to_json)
    updated_tasks = [task for task in current_tasks if task["id"] != id]
    if not updated_tasks:
        Exception(status_code=404, detail="Задача не найдена")
    update_json_file(path_to_json, updated_tasks)
    return {"message": "Задача успешно удалена"}




