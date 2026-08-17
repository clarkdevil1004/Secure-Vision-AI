from ultralytics import YOLO


DATA_CONFIG = "dataset/data.yaml"
MODEL = "yolov8n.pt"

EPOCHS = 65
IMAGE_SIZE = 640
BATCH_SIZE = 16


def train_model():
    model = YOLO(MODEL)

    model.train(
        data=DATA_CONFIG,
        epochs=EPOCHS,
        imgsz=IMAGE_SIZE,
        batch=BATCH_SIZE,
        workers=2,
        patience=15,
        project="runs/train",
        name="secure_vision_ai",
    )

    print("\nTraining completed successfully.")
    print("Best model saved inside runs/train/secure_vision_ai/")


if __name__ == "__main__":
    train_model()
