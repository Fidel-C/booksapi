import uvicorn






if __name__=="__main__":
    uvicorn.run("apps.app:app",reload=True)