from sqlalchemy import Integer , String , ForeignKey , DateTime , Enum, null
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from app.db.base import Base
import enum

from app.models import project

class TaskStatus(str , enum.Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100) , nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    status: Mapped[str] = mapped_column(
                          Enum(TaskStatus),
                          default=TaskStatus.TODO,
                          nullable=False)

    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"),nullable=False)
    owner_id: Mapped[int] = mapped_column(ForeignKey("users.id"),nullable=False)
    create_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now(),nullable=False)


