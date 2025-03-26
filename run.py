import werkzeug.security
werkzeug.security.safe_str_cmp = lambda a, b: a == b

from app import create_app, db
from app.models import initialize_database
from app.routes import add_test_data  # Updated import

app = create_app()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        initialize_database(app)
        add_test_data(app)
    app.run(debug=True)