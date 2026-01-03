from fastapi import FastAPI
import pyshorteners

shortener = pyshorteners.Shortener()

app = FastAPI()

def url_shortener(url: str) -> str:
    shortened_url = shortener.tinyurl.short(url)
    return shortened_url

@app.get("/shorturl")
async def get_short_url(url: str):
    short_url = url_shortener(url)
    return {"short_url": short_url}
