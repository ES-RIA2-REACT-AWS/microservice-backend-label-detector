from fastapi import FastAPI
from controllers.label_detector_controller import router as label_detector_router
from handlers.label_detector_handler import add_label_detector_handlers


app = FastAPI()
add_label_detector_handlers(app)

app.include_router(label_detector_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3000)
