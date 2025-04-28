import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse
from dotenv import load_dotenv
import requests

load_dotenv()

app = FastAPI()

CLIENT_ID = os.getenv("LINKEDIN_CLIENT_ID")
CLIENT_SECRET = os.getenv("LINKEDIN_CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

@app.get("/api/hello")
def read_root():
    return {"message": "Hello, world from Backend!"}

@app.get("/api/auth/linkedin")
def linkedin_auth():
    auth_url = (
        "https://www.linkedin.com/oauth/v2/authorization"
        f"?response_type=code&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}&scope=r_liteprofile%20r_emailaddress%20w_member_social"
    )
    return RedirectResponse(auth_url)

@app.get("/auth/linkedin/callback")
def linkedin_callback(request: Request):
    code = request.query_params.get("code")
    token_resp = requests.post(
        "https://www.linkedin.com/oauth/v2/accessToken",
        data={
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    ).json()
    return JSONResponse(token_resp)
