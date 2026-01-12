from sqlalchemy.orm import Session

from app.db.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_in: UserCreate) -> User:
    hashed_password = hash_password(user_in.password)

    user = User(
        email=user_in.email,
        hashed_password=hashed_password,
        role_id=1,  # default role (we'll formalize roles later)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
