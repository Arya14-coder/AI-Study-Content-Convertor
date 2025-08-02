from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from summarize import summarize_text
from voice_note import text_to_speech, generate_voice_script 

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.get("/")
def hello():
    return {"message":"Welcome"}

@app.post("/summarize")
def summarize_endpoint(data: InputText):
    return {"summary": summarize_text(data.text)}

@app.post("/voice")
def voice_endpoint(data: InputText):
    voive_script = generate_voice_script(data.text)
    path=text_to_speech(voive_script)
    return {"voice_file_path": path}


