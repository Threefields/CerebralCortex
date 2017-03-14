from apiv1 import blueprint as apiv1
from flask import Flask

app = Flask(__name__)
app.register_blueprint(apiv1)

if __name__ == "__main__":
    app.run(debug=True)
