from app import  app , logger

@app.get("/")
@logger.catch
def root():
    return {'hallo Fast Api'}