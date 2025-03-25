# Quarter-1-Project

Food safety is important for both customers and restaurant owners. This project predicts restaurant inspection grades to help people choose safe places to eat and guide restaurants in improving their health standards. By analyzing which factors lead to better grades, the model identifies key areas that impact food safety. With foodborne illnesses being a major concern, this project provides a clear and data driven way to assess restaurant safety, helping to protect public health and build trust in the food industry.

## Dataset  
We use the **NYC Restaurant Inspection Results** dataset from Kaggle:  
[NYC Restaurant Inspection Results](https://www.kaggle.com/datasets)  

## Process  
1. **Preprocessing**  
   - Clean and format the data  
   - Handle missing values  
   - Perform feature engineering  

2. **Attribute Selection**  
   - Use methods like CorrelationAttributeEval and ReliefF to select important features  

3. **Classifier Models**  
   - Train and evaluate models such as Naive Bayes and RandomForest to classify restaurant grades  

## How to Run  
1. **Download the Dataset**  
   - Get the dataset from Kaggle and place it in the project directory  

2. **Run Preprocessing**  
   ```bash
   python preprocessing.py
   ```
3. Download WEKA and follow the WEKA process instructions in the report
