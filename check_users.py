from app import create_app, db
from app import Usuario

app = create_app()
with app.app_context():
    users = Usuario.query.all()
    print(f"Total users: {len(users)}")
    for u in users:
        print(f"User: {u.email}")
