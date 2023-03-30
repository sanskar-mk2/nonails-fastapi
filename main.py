from fastapi import FastAPI, UploadFile
from lead_test_avg import get_mean
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def status() -> dict:
    return {"status": "operational"}


@app.post("/")
def get_mean_from_file(image: UploadFile) -> dict:
    return {"mean": get_mean(image.file)}
