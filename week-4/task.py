from fastapi import FastAPI, Form, Path, Query
from fastapi import Request
from fastapi.responses import *
from fastapi.templating import Jinja2Templates
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware

app=FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")  # secret_key 用於加密 session

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signin")
async def signin(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == "test" and password == "test":
        request.session["username"] = username #儲存登入狀態到session
        return RedirectResponse("/member", status_code=302)
    elif username == "" or password == "":
        return RedirectResponse("/error?message=Please enter username and password", status_code=302)
    else:
        return RedirectResponse("/error?message=帳號或密碼輸入錯誤", status_code=302)

@app.get("/member")
async def member(request: Request):
    username = request.session.get("username")
    if not username:  # 如果沒有登入，導回登入頁面
        return RedirectResponse("/", status_code=302)
    return templates.TemplateResponse("signin-success.html", {"request": request, "username": username})

@app.get("/signout")
async def logout(request: Request):
    request.session.clear()  # 清除 session
    return RedirectResponse("/", status_code=302)

@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, message: str = "發生錯誤"):
    return templates.TemplateResponse("signin-fail.html", {"request": request, "message":message})

@app.get("/square")
def square(num, request: Request):
    num = int(num)
    num = num**2
    return templates.TemplateResponse("square.html", {"request": request, "num":num})