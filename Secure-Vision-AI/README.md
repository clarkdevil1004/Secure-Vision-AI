# Secure Vision AI

Real-time Smart Surveillance with Context-Aware Weapon Detection

## Project Overview

Secure Vision AI is our final-year B.E. Computer Engineering project that detects weapons and suspicious activities from CCTV footage using deep learning.

The main challenge was reducing false alarms. A kitchen knife being used to cut vegetables should not raise the same alert as a knife held in an aggressive posture. To improve detection quality, we prepared a custom dataset containing both safe and threatening knife positions together with normal indoor scenes. This helped reduce false positives during testing.

## Problem Statement

Manual CCTV monitoring is difficult to perform continuously. The objective was to automatically identify dangerous situations and assist security personnel with real-time alerts.

## Features

- Real-time CCTV/Webcam monitoring
- Context-aware weapon detection
- Custom trained YOLOv8 model
- Bounding boxes with confidence score
- Reduced false positives using negative samples

## Tech Stack

Python • YOLOv8 • OpenCV • NumPy • Pandas

## My Contribution

- Collected and cleaned the weapon dataset
- Annotated knife and weapon images
- Added safe vs aggressive knife samples
- Trained and evaluated the YOLO model
- Integrated live webcam detection

## Repository Structure

```text
src/
dataset/
models/
screenshots/
docs/
```

## Note

The dataset and trained weights are intentionally excluded because of their large size.
