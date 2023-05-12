from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scripts.services import inventory_router

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
)

app.include_router(inventory_router)
