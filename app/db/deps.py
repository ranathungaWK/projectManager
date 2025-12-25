from app.db.session import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()  # you can also commit here if every endpoint should auto-commit
    except:
        db.rollback()
        raise
    finally:
        db.close()
