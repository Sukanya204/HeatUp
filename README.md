# HeatUp - A Calorie Burnt Prediction App

HeatUp is a lightweight web application designed to estimate the number of calories burned during various physical activities. By inputting specific parameters, users can gain insights into their energy expenditure, aiding in fitness tracking and goal setting.

## Features

✅ User-Friendly Interface: Simple and intuitive design for easy navigation.  
✅Calorie Estimation: Predicts calories burned based on user inputs.  
✅ Interactive Notebook: Includes `Calorie.ipynb` (Jupyter Notebook) for data exploration and model insights.    

## Installation

You can install HeatUp directly from GitHub:

### 1. Clone the repository
```bash
git clone https://github.com/Sukanya204/HeatUp.git
cd HeatUp
```
### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv\Scripts\activate(For Windows)
source venv/bin/activate(For Mac)
```
### 3. Install Dependencies
```bash
pip install -r requirement.txt
```
### 4. Run the Application
```bash
streamlit run app.py
```

## Usage
After launching the app, open the provided local URL in your browser (typically `http://localhost:8501`). Enter your details (e.g., weight, activity type, duration) to view calorie burn estimates.
