#bolsonaro 22

import os
from flask import Flask
from routes.home import home_route
from routes.user import user_route
from routes.admin import admin_route

app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(user_route, url_prefix='/user')
app.register_blueprint(admin_route)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)
