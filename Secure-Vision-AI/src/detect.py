from ultralytics import YOLO
import cv2

MODEL_PATH = "models/best.pt"
CONFIDENCE_THRESHOLD = 0.55


def draw_alert(frame, label):
    """Display warning banner on detected frame."""
    cv2.rectangle(frame, (0, 0), (640, 40), (0, 0, 255), -1)
    cv2.putText(
        frame,
        f"ALERT: {label.upper()} DETECTED",
        (10, 27),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
    )


def run_detection(source=0):
    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print("Error: Unable to access camera.")
        return

    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame, verbose=False)

        alert = None

        for result in results:
            for box in result.boxes:
                confidence = float(box.conf[0])

                if confidence < CONFIDENCE_THRESHOLD:
                    continue

                class_id = int(box.cls[0])
                label = model.names[class_id]

                if label.lower() in ["gun", "knife", "weapon"]:
                    alert = label

        annotated_frame = results[0].plot()

        if alert:
            draw_alert(annotated_frame, alert)

        cv2.imshow("Secure Vision AI", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()