from fastapi import FastAPI, Form, HTTPException, Request, Path, Query
from fastapi.responses import *
from fastapi.templating import Jinja2Templates
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
import mysql.connector

app=FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(SessionMiddleware, secret_key="your_secret_key")  # secret_key 用於加密 session

templates = Jinja2Templates(directory="templates")

@app.post("/signup")
async def signup(
    name: str = Form(...),
    username: str = Form(...),
    password: str = Form(...)
):    
    con = mysql.connector.connect(
    user="root",
    password="123456",
    host="localhost",
    database="website"
    )
    cursor = con.cursor()
    cursor.execute("SELECT member.username FROM member WHERE username = %s", (username,))
    data = cursor.fetchone()
    if data is None: # 如果帳號(username)不存在於member資料表, 就執行新增
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        values = (name, username, password)
        cursor.execute(sql, values)
        con.commit() # 確定執行
        con.close()
    else:
        con.close()
        return RedirectResponse("/error?message=帳號已存在，無法註冊", status_code=302)
    return RedirectResponse("/", status_code=302)

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/signin")
async def signin(request: Request, username: str = Form(...), password: str = Form(...)):
    con = mysql.connector.connect(
    user="root",
    password="123456",
    host="localhost",
    database="website"
    )
    # print("資料庫連線成功,登入成功")
    cursor = con.cursor()
    cursor.execute("SELECT id, name, username FROM member WHERE username= %s AND password = %s", (username, password))
    data = cursor.fetchone()
    
    if data:
        request.session["member_id"] = data[0] #儲存登入狀態到session
        request.session["name"] = data[1]
        request.session["username"] = data[2]
        con.close()
        return RedirectResponse("/member", status_code=302)
    else:
        con.close()
        return RedirectResponse("/error?message=帳號或密碼輸入錯誤", status_code=302)
    
@app.get("/member")
async def member(request: Request):
    member_id = request.session.get("member_id")
    print(type(member_id))
    name = request.session.get("name")
    username = request.session.get("username")
    if not username:  # 如果沒有登入，導回登入頁面
        return RedirectResponse("/", status_code=302)
    
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor = con.cursor()
    cursor.execute("SELECT message.id, member.username, message.content, message.member_id FROM member INNER JOIN message ON member.id = message.member_id ORDER BY message.id DESC")
    messages = cursor.fetchall()
    # print(messages)
    con.close()
    return templates.TemplateResponse("signin-success.html", 
    {"request": request, "name": name, "messages": messages, "member_id": member_id})

@app.get("/signout")
async def logout(request: Request):
    request.session.clear()  # 清除 session
    return RedirectResponse("/", status_code=302)

@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, message: str = "發生錯誤"):
    return templates.TemplateResponse("signin-fail.html", {"request": request, "message":message})

@app.post("/createMessage")
async def createMessage(request: Request, content: str = Form(...)):
    member_id = request.session.get("member_id")
    if not member_id:
        return RedirectResponse("/", status_code=302) # 如果沒登入，導回首頁
    
    con = mysql.connector.connect(
    user="root",
    password="123456",
    host="localhost",
    database="website"
    )
    cursor = con.cursor()
    
    sql = "INSERT INTO message (member_id, content) VALUES (%s, %s)"
    cursor.execute(sql, (member_id, content))
    con.commit()
    con.close()
    return RedirectResponse("/member", status_code=302) # 重新導向回會員頁面，讓使用者看到最新留言

@app.post("/deleteMessage")
async def delete_message(request: Request, message_id: int = Form(...)):
    member_id = request.session.get("member_id")
    if not member_id:  # 未登入則導回首頁
        return RedirectResponse("/", status_code=302)
    
    con = mysql.connector.connect(
        user="root",
        password="123456",
        host="localhost",
        database="website"
    )
    cursor = con.cursor()
    
    # 確保該訊息是當前登入者的
    cursor.execute("SELECT id FROM message WHERE id = %s AND member_id = %s", (message_id, member_id))
    message = cursor.fetchone()

    if message:
        cursor.execute("DELETE FROM message WHERE id = %s", (message_id,))
        con.commit()

    con.close()
    return RedirectResponse("/member", status_code=302)