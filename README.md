# housing-mlops-deployment
# Housing Price Prediction Web App - MLOps Deployment

This repository contains the necessary files to deploy a web application that predicts housing prices using a pre-trained machine learning model.

## Repository Contents

- `Housing.csv`: The dataset used for reference and training.
- `model.pkl`: The pre-trained model file for predicting housing prices.
- `app.py`: A Python script that provides a web interface for making predictions using Gradio.
- `README.md`: This documentation file containing project details and instructions.

## Purpose

This project demonstrates an end-to-end MLOps pipeline for deploying a web application that predicts housing prices. The goal is to show how to integrate a pre-trained model into a user-friendly web interface using Gradio.

## Usage Instructions

1. **Clone the Repository:**

```bash
git clone https://github.com/<your-username>/housing-mlops-deployment.git
cd housing-mlops-deployment

2. **Install the Required Python Libraries**
Make sure you have Python installed on your system. Then install the required packages:
pip install gradio pandas scikit-learn joblib

3. **Run the Application**
Execute the deployment script:
python app.py

**Additional Notes**
Ensure that the model.pkl and Housing.csv are present in the repository root.

You may need to adjust the file paths if you reorganize the repository structure.

Enjoy using the housing price prediction app!
