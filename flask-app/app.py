from venv import create
from application import app
from create import Dbbuild

if __name__ == "__main__":
    Dbbuild()
    app.run(debug=True, host='0.0.0.0', port=5000)