from fastapi import FastAPI

app = FastAPI()

async def status():
    return {"status":200}
