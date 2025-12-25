from fastapi import APIRouter, Depends, HTTPException , status
from sqlalchemy.orm import Session 
from app.db.session import get_db
from app.models.project import Project 
from app.schemas.project import ProjectCreate , Project as ProjectModel
from app.models.user import User 
from app.api.deps import get_current_user
from app.schemas.project import ProjectStatusUpdate



router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/create", response_model=ProjectModel, status_code=status.HTTP_201_CREATED)
def create_project(project: ProjectCreate , db:Session = Depends(get_db) , current_user:User = Depends(get_current_user))-> ProjectModel:
    """create a new project"""
    
    new_project = Project(
        name=project.name,
        description=project.description,
        owner_id=current_user.id,
        status = project.status if hasattr(project, "status") else "ongoing")

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project

@router.get("/list" , response_model=list[ProjectModel])
def list_projects(db:Session = Depends(get_db) , current_user:User = Depends(get_current_user)):
    """list all projects"""
    return db.query(Project).filter(Project.owner_id == current_user.id).all()



@router.patch("/{project_id}/status")
def update_project_status(
    project_id: int,
    payload: ProjectStatusUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Update the status of a project."""
    project = (
        db.query(Project)
        .filter(
            Project.id == project_id,
            Project.owner_id == current_user.id
        )
        .first()
    )

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    project.status = payload.status
    db.commit()

    return {"message": "Status updated", "status": project.status}

