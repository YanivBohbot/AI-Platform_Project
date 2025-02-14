from fastapi import APIRouter , UploadFile, File
import pandas as pd 
import io 
from app.services.kafka_producer import send_message


router = APIRouter()  

@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    data = {"filesmname": file.filename,  "columns": list(df.columns)}
    
    send_message(data)
    
    return {"message": "File uploaded successfully"}    
    