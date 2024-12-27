from fastapi import FastAPI
from routes import api_router
from logging_config import logger

app = FastAPI()

app.include_router(api_router)

from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("Api started")
@app.get("/", response_description="Start")
async def hello():
    return "Hello!"

#@app("shutdown")
#async def shutdown_remove_db():
#    if os.environ["API_TEST"]:
#        drop_database()