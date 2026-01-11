from app.db.session import engine
from app.db.base import Base
import app.db.models  # noqa

Base.metadata.create_all(bind=engine)
