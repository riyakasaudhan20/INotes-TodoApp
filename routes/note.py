from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity,notesEntity
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note=APIRouter()
templates = Jinja2Templates(directory="templates")


@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # docs=conn.notes.notes.find_one({})
    # print(docs)
    docs=conn.notes.notes.find({})
    newDocs=[]
    for doc in docs:
      newDocs.append({
          "id":doc["_id"],
          "title":doc["title"],
          "desc":doc["desc"],
          "important":doc["important"],
      })
    
    return templates.TemplateResponse("index.html", {"request": request,"newDocs":newDocs}) 


@note.post("/")
async def add_note(request:Request):
           form=await request.form()
        #    print(form)
           formDict=dict(form)
           formDict["important"] = True if formDict.get("important") == "on" else False  # type: ignore
           note=conn.notes.notes.insert_one(formDict)
           return {"Success":True}