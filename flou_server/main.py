from fastapi import FastAPI
from flou_server import modules

app = FastAPI(title="Flou")

# app.mount("/client", modules.client_app)
app.mount("/api", modules.web_app)
# app.mount("/internal", modules.internal_app)
