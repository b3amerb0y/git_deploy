from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    nombre = "Estudiante"
    return f"<h1>Bienvenido al portal universitario, {nombre}!</h1>"
    
@app.route("/api/status")
def status():
    return {"status": "ok", "entorno": "contenedor-docker", "version": "1.1.0"}

@app.route("/api/status/ok")
def status():
    return {"status": "ok", "version": "1.1.1"}

print("status: ok")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
