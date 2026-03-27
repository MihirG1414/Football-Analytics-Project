from ultralytics import YOLO 

model = YOLO('models/best.pt')

results = model.predict(r"C:\Users\Win-10\Desktop\ASEP Project 1\input videos\test_video.mp4", save=True)

print(results[0])
print('=====================================')
for box in results[0].boxes:
    print(box)