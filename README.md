# ML_Loan_Approval_Framework

This project is a machine learning-based loan approval framework that can help financial institutions make smarter, data-driven decisions. It includes a full pipeline from data preprocessing and model training to real-time prediction using a Streamlit web application.

---

## 🚀 Features

- Preprocessing and feature engineering on loan application data  
- Class imbalance handling using SMOTE and class weights  
- Model comparison: Logistic Regression, Decision Tree, Random Forest, XGBoost  
- Model explainability with SHAP  
- Streamlit interface for live predictions  

---

## 📁 Project Structure

```
ML_Loan_Approval_Framework/
│
├── app/                    # Streamlit app for real-time predictions  
├── loan_approval_dataset/  # JSON version of the dataset  
├── model_files/            # Encoders, scalers, transformers 
├── Trained_models/         # Trained models 
├── style/                  # Styling for the Streamlit app  
├── requirements.txt        # Project dependencies  
├── README.md               # Project documentation  
└── *.ipynb                 # Jupyter notebooks (EDA, training, SHAP, etc.)
```

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GRozzah/ML_Loan-_Approval_Framework.git
   cd ML_Loan-_Approval_Framework
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Running the Streamlit App

To launch the interactive loan approval app:

```bash
streamlit run app/app.py
```

This will open the app in your default browser, where you can input new loan applications and receive predictions.

---

## 📊 Model Overview

- **Best Model:** Random Forest  
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score, ROC-AUC  
- **Model Explainability:** SHAP (SHapley Additive exPlanations) used to interpret model predictions and feature impact  

---

## 📈 Dataset Source

The dataset used in this project is from Kaggle:  
🔗 [Loan Approval Dataset by Rohit265](https://www.kaggle.com/datasets/rohit265/loan-approval-dataset)

---

## ⚠️ Notes

- Folders like `loan_approval_data/`, `model_files/`, and `Trained_models/` are excluded from version control via `.gitignore`.  
- You can replace the dataset or retrain the model with different parameters as needed.

---

## 📄 License

This project is licensed under the **MIT License**.

---

