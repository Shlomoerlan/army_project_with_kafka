from app.db.database_psql import init_db
from app.routes.get_data import app


if __name__ == '__main__':
    init_db()
    app.run()