from fastapi import APIRouter , UploadFile, File

import pandas as pd 
import io 

router = APIRouter()  

@router.post("/upload")
async def uploadFile(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    return {"filesmname": file.filename,  "columns": list(df.columns)}