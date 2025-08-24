from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def root():
    return "Hola Mundo desde Flask 🚀, Proyecto final Electiva 2 (Adrian Hendrix Mat:20231352)"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Render inyecta PORT
    app.run(host="0.0.0.0", port=port)
