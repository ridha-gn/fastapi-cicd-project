from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

app = FastAPI(title="To-Do API", version="1.0.0")

# In-memory storage (for demo purposes)
tasks_db = []

class Task(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    completed: bool = False

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI To-Do API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": "2024-01-01T00:00:00Z"}

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: str):
    task = next((task for task in tasks_db if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", response_model=Task)
async def create_task(task: TaskCreate):
    task_id = str(uuid.uuid4())
    new_task = Task(
        id=task_id,
        title=task.title,
        description=task.description
    )
    tasks_db.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, task_update: TaskCreate):
    task_index = next((index for index, task in enumerate(tasks_db) if task.id == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db[task_index].title = task_update.title
    tasks_db[task_index].description = task_update.description
    return tasks_db[task_index]

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    task_index = next((index for index, task in enumerate(tasks_db) if task.id == task_id), None)
    if task_index is None:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db.pop(task_index)
    return {"message": "Task deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
