from fastapi import FastAPI, requests, HTTPException
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse
from typing import Optional

app = FastAPI()

@app.get("/hello")
def read_hello(name: Optional[str] = None, is_teacher: Optional[bool] = None):
    if name is None and is_teacher is None:
        # No query parameters → return the default message
        return JSONResponse(content={"message": "Hello world"}, status_code=200)


    # Assign default values if some parameters are missing
    if name is None:
        name = "Non fourni"
    if is_teacher is None:
        is_teacher = False

    # Otherwise, handle like before
    if is_teacher:
        message = f"Hello Teacher {name} !"
    else:
        message = f"Hello {name} !"

    return JSONResponse(content={"message": message}, status_code=200)


@app.get("/top-secret")
def top_secret(request: Request):
    # Get the "Authorization" header from the request
    auth_header = request.headers.get("Authorization")

    # Check the header value
    if auth_header != "david-secret-key":
        # If incorrect or missing, return 403 Forbidden with the wrong key
        return JSONResponse(
            content={"error": "Forbidden", "provided_key": auth_header},
            status_code=403
        )

    # If correct, return a welcome message
    return JSONResponse(
        content={"message": "Welcome to the secret area!"},
        status_code=200
    )


# Define the expected body using Pydantic
class SecretCodeRequest(BaseModel):
    secret_code: int

@app.post("/welcome")
def welcome(request_data: SecretCodeRequest):
    secret_code = request_data.secret_code

    # Check if secret_code is exactly 4 digits
    if secret_code < 1000 or secret_code > 9999:
        raise HTTPException(
            status_code=400,
            detail="Invalid code: The secret code must be a 4-digit number."
        )

    # If OK, return success message
    return JSONResponse(content={"message": "Access Granted! Secret code accepted."}, status_code=200)
