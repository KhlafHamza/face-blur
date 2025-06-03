 # face-blur
🕵️‍♂️ Face Blur with Oval Mask using Python & OpenCV
This project will automatically detect faces in your image and apply a natural blur in an oval shape over each face.

📥 Step 1 – Install Python (Very Important)
🔗 Download Python:
👉 Go to: https://www.python.org/downloads

✅ During installation:
Choose Python version 3.12 or lower (⚠️ Don't use Python 3.13).

Check the box ✅ "Add Python to PATH"

Click Install Now


🧱 Step 2 – Install Required Libraries
📌 Open your terminal or command prompt:
On Windows: Press Windows + R, type cmd, press Enter.

On macOS/Linux: Use the built-in terminal.

📦 Run these commands:
bash
pip install opencv-python numpy
This will install:

opencv-python: for face detection and image processing.

numpy: for working with image data.

🖼️ Step 3 – Add Your Image
Put your image file (example: myphoto.jpeg) in the same folder as the Python script.

🧠 Step 4 – Run the Code
🖥️ In your terminal, go to the folder:
Example:

bash
cd Desktop/face_blur_project
Then run:

bash

python blur_faces.py
✅ If everything works, you’ll see:

✅ Blurred image saved to output_oval_blur.jpg
🛠️ Step 5 – Use Your Own Image
Place your image (e.g., myphoto.jpeg) in the same folder.

Open blur_faces.py in any code editor.

Change this line:

python

blur_faces_oval('nmtcv2.jpeg', 'output_oval_blur.jpg')
to:

python

blur_faces_oval('myphoto.jpeg', 'myphoto_blurred.jpg')
Save and re-run:

bash

python blur_faces.py
✅ Files You Should Have

📁 face_blur_project/
├── blur_faces.py
├── nmtcv2.jpeg      ← your input image
└── output_oval_blur.jpg  ← the result
