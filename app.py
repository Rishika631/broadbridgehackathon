import streamlit as st
import cv2
from model import ImageToWordModel

# Load the trained model
model = ImageToWordModel(model_path="path/to/model")

# Define Streamlit app
def main():
    st.title("Handwriting Recognition")
    st.write("Upload an image and get the predicted text.")

    # Upload image file
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image file
        image = cv2.imdecode(np.fromstring(uploaded_file.read(), np.uint8), 1)

        # Display the uploaded image
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform prediction
        prediction_text = model.predict(image)

        # Display the predicted text
        st.subheader("Predicted Text:")
        st.write(prediction_text)

# Run the Streamlit app
if __name__ == "__main__":
    main()
