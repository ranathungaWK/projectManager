from fastapi import APIRouter, HTTPException , status , Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User as UserModel
from app.schemas.user import User , UserCreate , UserLogin
from app.utils.security import hash_password , verify_password
from app.api.deps import get_current_user
from app.utils.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup", response_model=User , status_code=status.HTTP_201_CREATED)
def signup(user: UserCreate , db:Session = Depends(get_db)) -> User:
    """create a new user"""

    existing_user = db.query(UserModel).filter(
        (UserModel.username == user.username) | (UserModel.email == user.email)).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username or email already exists")  

    new_user = UserModel(
        username=user.username,
        email=user.email,
        password=hash_password(user.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login", status_code=status.HTTP_200_OK)
def login(user: UserLogin, db: Session = Depends(get_db)) -> dict:
    """Login user"""
    
    found_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    
    if not found_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not verify_password(user.password, found_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect password")
    
    access_token = create_access_token(data={"sub":str(found_user.id)})

    return {"access_token": access_token, "token_type": "bearer"}
