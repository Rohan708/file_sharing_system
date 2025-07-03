from fastapi import FastAPI
from app.routes import ops, client
import os

app = FastAPI(title="Secure File Sharing System")

# Include Routes
app.include_router(ops.router, prefix="/ops", tags=["Ops User"])
app.include_router(client.router, prefix="/client", tags=["Client User"])

# Ensure uploads folder exists
if not os.path.exists("app/uploads"):
    os.makedirs("app/uploads")
