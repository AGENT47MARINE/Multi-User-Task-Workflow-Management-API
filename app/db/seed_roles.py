from app.db.session import SessionLocal
from app.db.models.role import Role


def seed_roles():
    db = SessionLocal()

    existing = db.query(Role).filter(Role.id == 1).first()
    if existing:
        print("Roles already seeded.")
        return

    user_role = Role(id=1, name="user")

    db.add(user_role)
    db.commit()

    print("Default role seeded successfully.")


if __name__ == "__main__":
    seed_roles()
