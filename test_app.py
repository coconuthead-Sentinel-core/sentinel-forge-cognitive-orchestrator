from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def demo_endpoint():
    return "ok"

print("App created with route")
