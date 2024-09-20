import os
from app import db, User, app

def setup_database():
    password = os.getenv("ADMIN_PASSWORD")
    if not password:
        raise ValueError("A senha do administrador não foi fornecida na variável de ambiente 'ADMIN_PASSWORD'.")
    
    with app.app_context():
        # Cria todas as tabelas no banco de dados
        db.create_all()

        # Verifica se o usuário 'admin' já existe
        existing_user = User.query.filter_by(username="admin").first()
        if not existing_user:
            admin_user = User(username="admin", password=password)
            db.session.add(admin_user)
            db.session.commit()
            print(f"User 'admin' created with id: {admin_user.id}")
        else:
            print("User 'admin' already exists.")

if __name__ == "__main__":
    setup_database()
