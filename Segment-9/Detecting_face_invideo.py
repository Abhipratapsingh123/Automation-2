import cv2

# Open the video file
video = cv2.VideoCapture("Segment-9/video.mp4")
success, frame = video.read()

# Check if the video was opened successfu lly
if not success:
    print("Error: Could not open video file.")
else:
    # Get the dimensions of the frame
    height = frame.shape[0]
    width = frame.shape[1]

    # Load the cascade for face detection
    face_cascade = cv2.CascadeClassifier('Segment-8/faces.xml')

    # Initialize the VideoWriter to save the output video
    fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
    output = cv2.VideoWriter('output.avi', fourcc, 30, (width, height))

    count = 0
    while success:
        # Convert the frame to grayscale (required for face detection)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=4)

        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4)

        # Write the frame with detected faces to the output video
        output.write(frame)

        # Read the next frame from the video
        success, frame = video.read()
        count += 1
        print(f"Processed frame {count}")

    # Release the VideoWriter and the VideoCapture objects
    output.release()
    video.release()
    print("Processing complete and output video saved.")
