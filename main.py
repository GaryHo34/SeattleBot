from fastapi import FastAPI

app = FastAPI()

@app.get("/{apple}")
async def root(apple):

    return {"message": apple}