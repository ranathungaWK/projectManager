from fastapi import APIRouter , Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.deps import get_db
from app.models.project import Project
from app.models.task import Task
from app.models.user import User
from app.schemas.report import ProjectProgressReport, TaskStatusSummary, userOverviewReport

router = APIRouter(prefix="/reports" , tags=["Reports"])


@router.get("/project/{project_id}" , response_model=ProjectProgressReport)
def get_project_progress(project_id:int, db:Session = Depends(get_db) , current_user:User = Depends(get_current_user)) ->ProjectProgressReport :
    """get project progress report"""

    project = db.query(Project).filter(Project.id == project_id , Project.owner_id == current_user.id).first()

    total = db.query(Task).filter(Task.project_id == project_id).count()

    done = db.query(Task).filter(Task.project_id == project_id , Task.status == "DONE").count()

    pending = total - done 
    progress = (done / total*100) if total > 0 else 0.0
    projectProgressReport = {"project_id": project.id,
                            "project_name": project.name,
                            "total_tasks": total,
                            "completed_tasks": done,
                            "pending_tasks": pending,
                            "progress_percent": round(progress,2)}

    return projectProgressReport


@router.get("/project/{project_id}/tasks" , response_model=TaskStatusSummary)
def get_task_status_summary(project_id:int , db:Session = Depends(get_db),current_user:User = Depends(get_current_user))->TaskStatusSummary:
    """get task status summary"""

    taskStatusCount = db.query(Task.status ,func.count(Task.id)).filter(Task.owner_id == current_user.id , Task.project_id == project_id).group_by(Task.status).all()
    print(taskStatusCount)
    summary_ = {"TODO":0 , "IN_PROGRESS":0 , "DONE":0}
    for status , count in taskStatusCount:
        summary_[status] = count

    
    summary = {
            "todo": summary_["TODO"],
            "in_progress": summary_["IN_PROGRESS"],
            "done": summary_["DONE"],
            }

    return summary


@router.get("/overview" , response_model=userOverviewReport)
def get_user_overview(db: Session = Depends(get_db),current_user:User = Depends(get_current_user)) -> userOverviewReport:
    """get user overview report"""

    total_projects = db.query(Project).filter(Project.owner_id == current_user.id).count()
    total_tasks = db.query(Task).join(Project).filter(Project.owner_id == current_user.id).count()
    completed_tasks = db.query(Task).join(Project).filter(Project.owner_id == current_user.id , Task.status == "DONE").count()

    userOverviewReport = {
                "total_projects": total_projects,
                "total_tasks": total_tasks,
                "completed_tasks": completed_tasks
                }

    return userOverviewReport

















