from flask import Flask, request, render_template
import pickle
import numpy as np
import cv2
import mediapipe as mp

app = Flask(__name__)

# Load model
model_dict = pickle.load(open('model.p', 'rb'))
model = model_dict['model']

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.5)

labels_dict = {
    0:'A',1:'B',2:'C',3:'J',4:'K',5:'S',6:'F',7:'O',
    8:'L',9:'R',10:'M',11:'N',12:'D',13:'E',
    14:'W',15:'V',16:'Y',17:'Z'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']

    file_bytes = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    data_aux = []
    x_ = []
    y_ = []

    prediction_text = "No hand detected"   # ✅ default

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                x_.append(lm.x)
                y_.append(lm.y)

            for lm in hand_landmarks.landmark:
                data_aux.append(lm.x - min(x_))
                data_aux.append(lm.y - min(y_))

        if len(data_aux) == 42:
            prediction = model.predict([np.asarray(data_aux)])
            prediction_text = labels_dict[int(prediction[0])]

    # ✅ THIS IS THE IMPORTANT LINE
    return render_template('index.html', prediction=prediction_text)
if __name__ == '__main__':
    app.run()