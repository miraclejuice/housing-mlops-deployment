import gradio as gr
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load("model.pkl")

# Function to perform prediction
def predict_price(area, bedrooms, bathrooms):
    # Create a DataFrame for the input features
    input_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms]
    })
    # Predict housing price using the loaded model
    prediction = model.predict(input_data)
    # Return the predicted price
    return f"Predicted price: ${prediction[0]:,.2f}"

# Build the Gradio interface
# Input components for area, bedrooms, bathrooms; output is text.
interface = gr.Interface(
    fn=predict_price,
    inputs=[
        gr.Number(label="Area (sq ft)"),
        gr.Number(label="Bedrooms"),
        gr.Number(label="Bathrooms")
    ],
    outputs="text",
    title="Housing Price Prediction",
    description="Enter the details of the house to predict its price."
)

# Launch the web interface
if __name__ == "__main__":
    interface.launch()
