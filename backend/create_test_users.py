from backend.database import SessionLocal, Base, engine
from backend.models.user import User
from backend.auth.password_utils import hash_password

# Ensure tables exist
Base.metadata.create_all(bind=engine)

db = SessionLocal()

users = [
    {
        "email": "admin@example.com",
        "password": "admin123",
        "role": "admin",
    },
    {
        "email": "manager@example.com",
        "password": "manager123",
        "role": "manager",
    },
    {
        "email": "analyst@example.com",
        "password": "analyst123",
        "role": "analyst",
    },
]

for u in users:
    existing = db.query(User).filter(User.email == u["email"]).first()
    if not existing:
        user = User(
            email=u["email"],
            hashed_password=hash_password(u["password"]),
            role=u["role"],
        )
        db.add(user)

db.commit()
db.close()

print("✅ Test users created successfully")
