#Teachable Machine에서 이미지 학습시킴.
#이미지 프로젝트 -> 표준 이미지모델 -> 사진 업로드(학습시킬 사진) -> 모델 학습시키기 -> 모델 내보내기 ->
#다되면 Tensorflow선택 후 Keras를 체크한 뒤 모델 다운로드를 누릅니다. 예제코드도 아래에 알려준다. 그대로 사용하자.
#다운받은 알집파일을 작업중인 폴더에 넣고 압축을 푼다.\
#pip install tensorflow.keras, 
from keras.models import load_model   # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

IMAGE_PATH = r"40 Python works\3. Project\9. Distinguish apples from oranges with artificial intelligence\orange picture\orange22.jpg"

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model(r"40 Python works\3. Project\9. Distinguish apples from oranges with artificial intelligence\converted_keras\keras_Model.h5", compile=False)

# Load the labels
class_names = open(r"40 Python works\3. Project\9. Distinguish apples from oranges with artificial intelligence\converted_keras\labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
image = Image.open(IMAGE_PATH).convert("RGB")

# resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# turn the image into a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Predicts the model
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("Class:", class_name[2:], end="")
print("Confidence Score:", confidence_score)