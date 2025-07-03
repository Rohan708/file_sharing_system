from fastapi import APIRouter, HTTPException
from app.utils import encrypt_data, decrypt_data
from fastapi import Request
from fastapi.responses import FileResponse
from app.schemas import UserSchema, LoginSchema
import os

router = APIRouter()
FILES_DIR = "app/uploads"
users = {}  # In-memory user storage for demo

@router.post("/signup")
def signup(user: UserSchema):
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.username] = {"email": user.email, "verified": False}
    encrypted_url = encrypt_data(user.username)
    return {"encrypted_url": encrypted_url}

@router.get("/verify-email")
def verify_email(token: str):
    try:
        username = decrypt_data(token)
        users[username]["verified"] = True
        return {"message": "Email verified successfully"}
    except:
        raise HTTPException(status_code=400, detail="Invalid token")


@router.post("/login")
def login(data: LoginSchema):
    user = users.get(data.username)
    if not user or not user["verified"]:
        raise HTTPException(status_code=403, detail="Email not verified or invalid user")
    return {"message": f"Welcome {data.username}"}

@router.get("/list-files")
def list_files():
    return {"files": os.listdir(FILES_DIR)}



@router.get("/download-file/{filename}")
def download_file(filename: str, request: Request):
    path = os.path.join(FILES_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="File not found")

    encrypted_link = encrypt_data(filename)
    full_url = str(request.base_url) + f"client/secure-download?token={encrypted_link}"
    
    return {"download-url": full_url, "message": "success"}


@router.get("/secure-download/{token}")
def secure_download(token: str):
    try:
        filename = decrypt_data(token)
        path = os.path.join(FILES_DIR, filename)
        if not os.path.exists(path):
            raise HTTPException(status_code=404, detail="File not found")
        return {"message": f"File ready for download: {filename}"}
    except:
        raise HTTPException(status_code=400, detail="Invalid token")

@router.get("/secure-download")
def secure_download(token: str):
    try:
        filename = decrypt_data(token)
        path = os.path.join(FILES_DIR, filename)

        if not os.path.exists(path):
            raise HTTPException(status_code=404, detail="File not found")

        return FileResponse(
            path,
            media_type="application/octet-stream",
            filename=filename
        )
    except:
        raise HTTPException(status_code=400, detail="Invalid token")