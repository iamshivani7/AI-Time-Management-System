
# AI Time Management System

A machine learning project with a Streamlit dashboard for productivity analytics and employee attrition prediction.

## Application Preview

![Home Dashboard](home.png)

![AI Prediction](prediction.png)

**Live Demo:** [Open AI Time Management System](https://ai-time-management-system-ghyckmdcreywefimephe59.streamlit.app/)


## Features
- Interactive Streamlit dashboard
- Productivity analytics and visualizations
- Employee attrition prediction
- Comparison of machine learning models
- AI-driven insights and recommendations

## Technologies
Python, Streamlit, Pandas, Scikit-learn, XGBoost, Matplotlib


## System Architecture

```mermaid
flowchart TD
    A["IBM HR Dataset"] --> B["Data Preprocessing"]
    B --> C["Feature Scaling"]
    C --> D["Train-Test Split"]
    D --> E["Six ML Models"]
    E --> F["Model Evaluation"]
    F --> G["XGBoost Model"]
    G --> H["Streamlit Dashboard"]
    H --> I["Analytics and Predictions"]
```


## Project Structure
- `app.py` – Streamlit application
- `final.ipynb` – Google Colab notebook
- `requirements.txt` – Dependencies
- `model/` – Trained model files

## Dataset
IBM HR Employee Attrition Dataset

## Disclaimer
This project is an educational prototype.


## Screenshots

### Home
![Home Dashboard](home.png)

### AI Prediction
![AI Prediction](prediction.png)

