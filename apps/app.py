from fastapi import FastAPI
import sys

from routers.book_router import router as books_router





app = FastAPI(title="Books API")


@app.get("/")
async def index():
    return {"Hello": "world"}


app.include_router(prefix="", router=books_router)





# A workaround that prevents terminal from frezing on shutdown
def receive_signal(Signalno, frame):
    print("Received", Signalno)
    sys.exit()

@app.on_event("startup")
async def start_event():
    import signal

    signal.signal(signal.SIGINT, receive_signal)
