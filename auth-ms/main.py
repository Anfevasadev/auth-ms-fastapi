# auth-ms/main.py
from fastapi import FastAPI
from interfaces.api.v1.user import router as user_router
from interfaces.api.v1.auth import router as auth_router
from fastapi.responses import JSONResponse

app = FastAPI()

app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(user_router, prefix="/api/v1/users")


@app.exception_handler(404)
async def not_found_handler(request, exc):
    return JSONResponse(status_code=404, content={"message": "Not Found"})
