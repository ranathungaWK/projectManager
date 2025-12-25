from sqlalchemy import String , ForeignKey , DateTime , Integer
from sqlalchemy.orm import Mapped , mapped_column
from app.db.base import Base 
import enum
from sqlalchemy import Enum
from sqlalchemy.sql import func

class ProjectStatus(enum.Enum) :
    ongoing = "ongoing"
    paused = "paused"
    ended = "ended"

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer , primary_key=True)
    name:Mapped[str] = mapped_column(String(255),nullable=False)
    description:Mapped[str] = mapped_column(String(255),nullable=False)
    status:Mapped[ProjectStatus] = mapped_column(Enum(ProjectStatus),nullable=False , default=ProjectStatus.ongoing) 

    owner_id:Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    create_at:Mapped[DateTime] = mapped_column(DateTime,server_default=func.now(), nullable=False)

    class Config:
        from_attributes = True


