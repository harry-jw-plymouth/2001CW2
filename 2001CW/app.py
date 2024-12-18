# app.py 

from flask import render_template
#import connexion
import config
from models import Trail

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    trails = Trail.query.all()
    return render_template("home.html" , trails=trails)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)