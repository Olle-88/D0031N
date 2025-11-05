from flask import Flask, render_template
from services import epok_service, studentits_service, ladok_service

app = Flask(__name__)

# Registrera REST-tjänster (BluePrints)
app.register_blueprint(epok_service.bp)
app.register_blueprint(studentits_service.bp)
app.register_blueprint(ladok_service.bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
