# Spam Detection using Machine Learning

## Overview
This project focuses on detecting spam messages using multiple machine learning models. The dataset is vectorized using **TF-IDF** (Term Frequency-Inverse Document Frequency), and classification is performed using the following models:
- **Logistic Regression**
- **Random Forest Classifier**
- **K-Nearest Neighbors (KNN)**

Additionally, exploratory data analysis (EDA) is conducted to understand the distribution of spam and ham messages.

## Dataset
The dataset used in this project contains labeled SMS messages categorized as **spam** or **ham** (not spam). The data is preprocessed and converted into numerical representations using **TF-IDF vectorization**.

## Installation
To run this project, install the required dependencies using the following command:
```bash
pip install -r requirements.txt
```

## Usage
Run the `spam_detection.py` script to train and evaluate the models:
```bash
python spam_detection.py
```

## Model Performance
| Model                 | Accuracy |
|----------------------|----------|
| Logistic Regression  | ~96.6%   |
| Random Forest       | ~98.3%   |
| K-Nearest Neighbors | ~92.0%   |

The **Random Forest** model achieved the highest accuracy but showed signs of **overfitting**.

## Potential Improvements
- **Hyperparameter tuning** using GridSearchCV
- **Class imbalance handling** using SMOTE
- **Feature engineering** (e.g., Word2Vec, BERT embeddings)
- **Deep Learning approaches** (e.g., LSTM, Transformer-based models)

## License
This project is open-source and available under the **MIT License**.

## Contributing
Feel free to open an issue or submit a pull request if you want to improve this project.

---

🚀 **Happy Coding!**


