#bolsonaro 22

from flask import Flask
from routes.home import home_route
from routes.user import user_route
from routes.admin import admin_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(user_route, url_prefix='/user')
app.register_blueprint(admin_route)

app.run(debug=True)