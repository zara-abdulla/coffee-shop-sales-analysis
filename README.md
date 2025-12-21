# Coffee Shop Sales Analysis - End To End Project

End-to-end Coffee Shop Sales Analysis project integrating CSV sales data and weather API data into SQL, followed by data cleaning, EDA, visualization, ML forecasting, and a final interactive Streamlit dashboard.


## Project Overview

This project aims to analyze coffee shop sales data and integrate external weather information via an API to build an interactive Streamlit dashboard. The goal is to understand overall sales patterns, customer behavior, and potential relationships between weather conditions and product demand.

The project also includes a simple machine learning model to forecast sales based on historical sales and weather data. The model’s primary goal is to provide insights on how weather impacts coffee shop sales.

## Project Workflow Diagram

Below is the workflow diagram illustrating the end-to-end process of the Coffee Shop Sales Analysis project, from data collection to dashboard deployment:

![](diagram/workflow_diagram.png)

## Project Workflow

**Data Collection & Storage**

Coffee shop sales data is loaded from a local CSV file into an SQL database.

Weather data is collected from an external API and stored in the same SQL database.

SQL → Python Processing

Data is retrieved from SQL into Python.

Initial data preprocessing is performed:

- Data cleaning

- Type conversions

- Handling missing values

Exploratory Data Analysis (EDA) is conducted to uncover patterns and trends.

Visualizations are created using Matplotlib and Seaborn to illustrate sales patterns, top products, and location performance.

**Machine Learning**

A simple model is built to forecast sales based on historical and weather data.

The model helps explore the relationship between weather conditions and sales performance.

**Streamlit Dashboard**

All insights and results are presented in an interactive Streamlit dashboard.

Users can explore sales trends by category, time, store location, and see potential impacts of weather on sales.

## Team Members

**This project will be carried out by**:

- [**Zahra Abdullayeva**](https://github.com/zara-abdulla) 
- [**Sevinc Qiyasova**](https://github.com/sevinc-giyasova) 
- [**Ziyafet Rzayeva**](https://github.com/Ziyafat98)
