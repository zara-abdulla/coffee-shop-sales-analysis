# Coffee Shop Sales Analysis - End To End Project

An end-to-end data analysis project focused on coffee shop sales, combining sales data with external weather data to perform data analysis, visualization, machine learning forecasting, and present insights through an interactive Streamlit dashboard.


## Project Overview

This project aims to analyze coffee shop sales data and integrate external weather information via an API to build an interactive Streamlit dashboard. The goal is to understand overall sales patterns, customer behavior, and potential relationships between weather conditions and product demand.

The project also includes a simple machine learning model to forecast sales based on historical sales and weather data. The model’s primary goal is to provide insights on how weather impacts coffee shop sales.


## Project Workflow Diagram

Below is the workflow diagram illustrating the end-to-end process of the Coffee Shop Sales Analysis project, from data collection to dashboard deployment.

![](images/diagram_gif.gif)

## Project Workflow

### **Data Collection**

- **Coffee shop sales data** is loaded from a local Excel file into Python.

- **Weather data** is collected from an external API.



### **Exploratory Data Analysis & Visualization**

- Exploratory Data Analysis (EDA) is conducted to uncover patterns and trends.
- Data cleaning, preprocessing, and feature extraction are performed.
- Visualizations are created using **Matplotlib** and **Seaborn** to analyze:
  - Sales trends
  - Top-selling products
  - Store location performance

### **Data Storage (Python → Dockerized MySQL)**

- Cleaned and processed sales data is stored in a **Dockerized MySQL database**.
- Weather data fetched from the API is also stored in the same database.
- This setup ensures structured storage, reproducibility, and readiness for modeling.


### **Machine Learning**

- Sales and weather data are retrieved from MySQL.
- A simple machine learning model is built to forecast sales.
- The model helps explore the relationship between weather conditions and sales performance.

### **Streamlit Dashboard**

- All insights and results are presented in an interactive **Streamlit dashboard**

## Team Members


- [**Zahra Abdullayeva**](https://github.com/zara-abdulla) 

- [**Ziyafet Rzayeva**](https://github.com/Ziyafat98)

- [**Sevinc Qiyasova**](https://github.com/sevinc-giyasova) 