✅ Full Testing Workflow After Running Uvicorn
bash
Copy
Edit
python -m uvicorn app.main:app --reload
Once server starts, follow these steps:

1️⃣ Client Signup
Go to http://127.0.0.1:8000/docs

Find /client/signup

Click Try it out

Request Body Example:

json
Copy
Edit
{
  "username": "testuser",
  "email": "test@example.com"
}
Click Execute

Copy the "encrypted_url" from the response (remove any spaces!)

2️⃣ Email Verification
Find /client/verify-email

Click Try it out

Paste the token (from "encrypted_url")

Example:

Copy
Edit
gAAAAABk........
Click Execute

You should get:

json
Copy
Edit
{ "message": "Email verified successfully" }
3️⃣ Client Login
Find /client/login

Click Try it out

Provide:

json
Copy
Edit
{
  "username": "testuser"
}
Click Execute

You should see "Welcome testuser"

4️⃣ Ops User Upload File
Find /ops/upload

Click Try it out

Select a file (.docx, .xlsx, .pptx)

Click Execute

You should see "File uploaded successfully"

5️⃣ List Files as Client
Find /client/list-files

Click Execute

You will see:

json
Copy
Edit
{ "files": ["example.docx"] }
6️⃣ Generate Secure Download Link
Find /client/download-file/{filename}

Click Try it out

Provide filename from the list (e.g., example.docx)

Click Execute

Copy the "download-link" value

7️⃣ Secure File Download
✔️ Recommended safer version:

Find /client/secure-download

Click Try it out

Paste only the token part from "download-link"

Example:

Copy
Edit
gAAAAABk.....
Click Execute

You get:

json
Copy
Edit
{ "message": "File ready for download: example.docx" }
➡️ Currently shows confirmation only — want real file download? Let me know.