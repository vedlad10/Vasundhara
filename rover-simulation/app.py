from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Vasundhara Rover Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    logger.info("✓ Vasundhara Rover Backend Started")
    logger.info("WebSocket: ws://localhost:8000/ml-inference")

@app.websocket("/ml-inference")
async def websocket_ml_inference(websocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            telemetry = json.loads(data)
            response = {
                'status': 'success',
                'movement': {'forward': 0, 'turn': 0, 'speed': 0.5},
                'confidence': 0.8,
                'reasoning': 'Rover AI Inference Ready'
            }
            await websocket.send_json(response)
    except Exception as e:
        logger.error(f"Error: {e}")

@app.get("/health")
async def health():
    return {'status': 'healthy'}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
