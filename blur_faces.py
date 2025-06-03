import cv2
import numpy as np

def blur_faces_circular(image_path, output_path):
    # Load the image
    image = cv2.imread(image_path)

    if image is None:
        print("❌ Failed to load image. Check the file name and path.")
        return

    # Load the pre-trained face detector
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Blur each face with a circular mask
    for (x, y, w, h) in faces:
        # Get the region of interest (face)
        face_roi = image[y:y+h, x:x+w]

        # Create a circular mask
        mask = np.zeros((h, w), dtype=np.uint8)
        center = (w // 2, h // 2)
        radius = min(w, h) // 2
        cv2.circle(mask, center, radius, 255, -1)

        # Blur the entire face ROI
        blurred_face = cv2.GaussianBlur(face_roi, (99, 99), 30)

        # Combine blurred and original using mask
        for c in range(3):  # For each color channel
            face_roi[:, :, c] = np.where(mask == 255, blurred_face[:, :, c], face_roi[:, :, c])

        # Place modified face ROI back in image
        image[y:y+h, x:x+w] = face_roi

    # Save the result
    cv2.imwrite(output_path, image)
    print(f"✅ Blurred image saved to {output_path}")

# Run the function
blur_faces_circular('nmtcv2.jpeg', 'output_blurred.jpg')
