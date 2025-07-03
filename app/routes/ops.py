from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
import os

router = APIRouter()

# Dummy role check - simulate Ops User
def get_current_user():
    return {"username": "ops_user", "role": "ops"}

@router.post("/upload")
def upload_file(file: UploadFile = File(...), user: dict = Depends(get_current_user)):
    if user['role'] != "ops":
        raise HTTPException(status_code=403, detail="Only Ops User can upload files")
    
    if not file.filename.endswith((".pptx", ".docx", ".xlsx")):
        raise HTTPException(status_code=400, detail="Invalid file type")

    path = f"app/uploads/{file.filename}"
    with open(path, "wb") as f:
        f.write(file.file.read())
    
    return {"message": "File uploaded successfully", "filename": file.filename}
