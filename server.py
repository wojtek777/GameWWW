from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

with open("game.html") as file:
    html_content = file.read()

print(html_content)

@app.get('/')
async def root():
    return {"message": "Welcome to my home"} 


@app.get('/game/')
async def get_game():
    return HTMLResponse(content=html_content, status_code=200)
