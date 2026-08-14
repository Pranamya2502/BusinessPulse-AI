# BusinessPulse

## Business Analytics, Machine Learning & Sales Forecasting Platform

BusinessPulse is an end-to-end business analytics and data science platform designed to transform raw sales data into meaningful business insights.

The project combines data preprocessing, exploratory data analysis, PostgreSQL, SQL analytics, machine learning, time-series forecasting, and an interactive Streamlit dashboard into a single workflow.

---

## Project Overview

BusinessPulse helps analyze historical business data and answer questions such as:

- How are sales and profit performing?
- Which categories and regions generate the most revenue?
- Which products contribute most to sales?
- How does discounting affect profitability?
- What are the historical sales trends?
- What could future sales look like?
- What profit could be expected from a new order?

The complete workflow is:

Raw Sales Data
      ↓
Data Cleaning & Feature Engineering
      ↓
Processed Dataset
      ↓
Exploratory Data Analysis
      ↓
PostgreSQL & SQL Analytics
      ↓
Machine Learning
      ↓
Sales Forecasting
      ↓
Interactive Dashboard
      ↓
Business Insights

---

## Key Features

### Data Processing

- Data cleaning and validation
- Missing-value analysis
- Duplicate detection
- Date conversion
- Feature engineering
- Shipping duration calculation
- Profit margin calculation
- Sales and pricing features

### Business Analytics

- Total Sales
- Total Profit
- Total Orders
- Profit Margin
- Sales by Category
- Profit by Category
- Sales by Region
- Profit by Region
- Top 10 Products
- Profitable vs Loss-Making Order Lines
- Monthly Sales Trends

### Interactive Dashboard

The dashboard supports dynamic filtering by:

- Region
- Category
- Customer Segment
- Year

The selected filters dynamically update the historical business analytics.

### Machine Learning

A Random Forest regression model is used to estimate expected order profit based on sales, discount, product, customer, geographic, and operational features.

### Sales Forecasting

Historical monthly sales are analyzed using time-series forecasting to generate a six-month future sales forecast.

---

# Dashboard

BusinessPulse provides a centralized dashboard for monitoring business performance.

### Key Performance Indicators

- Total Sales
- Total Profit
- Total Orders
- Profit Margin

### Dashboard Analytics

- Sales by Category
- Monthly Sales Trend
- Profit by Category
- Sales by Region
- Profit by Region
- Top 10 Products
- Profitability Overview
- Six-Month Sales Forecast
- Interactive Profit Prediction


## Dashboard Preview



<img width="1661" height="754" alt="dashboard" src="https://github.com/user-attachments/assets/e1cc0050-b47c-4fdc-8136-bb01627c8e23" />




---

## Business Analytics

The dashboard allows users to explore business performance through interactive filters.

Available filters include:

Region
Category
Segment
Year

These filters update the relevant KPIs and visualizations without requiring the underlying analysis to be rewritten.

### Example Business Questions

- Which region generates the highest sales?
- Which category generates the highest profit?
- Which products contribute the most revenue?
- Which segments are most profitable?
- How does performance change across years?
- Where are loss-making transactions concentrated?


## Analytics Dashboard



<img width="1697" height="618" alt="analytics" src="https://github.com/user-attachments/assets/91ccc182-95f4-4e87-9924-951668d1bb0f" />




---

# Machine Learning

## Objective

The machine learning component predicts the expected profit of an order based on its business and operational characteristics.

### Model

Random Forest Regressor

### Features

The model uses:

- Sales
- Quantity
- Discount
- Shipping Days
- Average Selling Price
- Category
- Sub-Category
- Region
- Segment
- Ship Mode

### Machine Learning Workflow

Order Information
       ↓
Feature Selection
       ↓
Train / Test Split
       ↓
Categorical Encoding
       ↓
Random Forest Regression
       ↓
Model Evaluation
       ↓
Profit Prediction

The preprocessing and model are combined into a machine learning pipeline to ensure consistent transformation of numerical and categorical features.

The trained model is integrated into the Streamlit dashboard, allowing users to enter order information and receive an estimated profit.

---

## Profit Prediction



<img width="1659" height="695" alt="ml_prediction" src="https://github.com/user-attachments/assets/95b2af8a-6843-4864-b750-e873077d2d7d" />




---

# Sales Forecasting

The forecasting component uses historical monthly sales to estimate future sales performance.

### Forecasting Workflow

Historical Order Data
       ↓
Monthly Sales Aggregation
       ↓
Time-Series Dataset
       ↓
Train / Test Split
       ↓
Holt-Winters Exponential Smoothing
       ↓
Model Evaluation
       ↓
Six-Month Forecast

The forecast is generated from historical sales patterns and integrated into the BusinessPulse dashboard.

The generated forecast is stored in:

data/processed/sales_forecast.csv


## Sales Forecast



<img width="1642" height="782" alt="forecast" src="https://github.com/user-attachments/assets/a3e334cf-f547-4d01-9fac-614c0d37bb70" />




---

# Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the structure, distribution, relationships, and trends within the dataset.

The analysis includes:

- Dataset profiling
- Data quality checks
- Missing-value analysis
- Duplicate analysis
- Descriptive statistics
- KPI analysis
- Category analysis
- Regional analysis
- Monthly sales trends
- Monthly profit trends
- Sales vs Profit analysis
- Discount vs Profit analysis
- Correlation analysis
- Outlier analysis
- Business insight generation

The EDA workflow is available in:

notebooks/EDA.ipynb

---

# PostgreSQL & SQL Analytics

PostgreSQL is used as the relational database layer for storing and analyzing the processed business data.

### Database Workflow

Processed Dataset
       ↓
PostgreSQL
       ↓
SQL Queries
       ↓
Business Analysis
       ↓
Business Insights

SQL analysis includes:

- Regional performance
- Category performance
- Sub-category profitability
- Monthly sales analysis
- Customer analysis
- Product analysis
- Loss-making products
- Ranking analysis
- Conditional analysis
- Common Table Expressions
- CASE statements
- Window functions
- PARTITION BY
- Running totals

SQLAlchemy is used to establish the Python-to-PostgreSQL connection.

---

# Data Preprocessing

The preprocessing workflow includes:

1. Loading the raw Superstore dataset
2. Validating data types
3. Converting date fields
4. Checking missing values
5. Checking duplicate records
6. Validating numerical columns
7. Extracting year and month
8. Extracting quarters
9. Extracting day names
10. Identifying weekends
11. Calculating shipping duration
12. Calculating profit margin
13. Calculating average selling price

The processed dataset is stored at:

data/processed/cleaned_superstore.csv

---

# Technology Stack

## Programming

- Python

## Data Processing

- Pandas
- NumPy

## Data Visualization

- Matplotlib
- Plotly

## Database

- PostgreSQL
- SQLAlchemy
- pgAdmin

## Machine Learning

- Scikit-learn
- Random Forest Regression
- Joblib

## Forecasting

- Statsmodels
- Holt-Winters Exponential Smoothing

## Dashboard

- Streamlit
- Plotly

## Development & Version Control

- VS Code
- Git
- GitHub

---


# Installation

## 1. Clone the Repository

git clone https://github.com/Pranamya2502/BusinessPulse-AI.git

cd BusinessPulse-AI

## 2. Create a Virtual Environment

python -m venv venv

Activate the environment on Windows:

venv\Scripts\activate

## 3. Install Dependencies

pip install -r requirements.txt

---

# PostgreSQL Configuration

Make sure PostgreSQL is installed and running.

Create the required database:

businesspulse_db

Create a .env file in the project root:

DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/businesspulse_db

Replace the credentials with your local PostgreSQL configuration.

The .env file should never be committed to GitHub.

---

# Running the Dashboard

From the project root:

streamlit run app/app.py

The application will be available at:

http://localhost:8501

---

# Git Workflow

The project follows a feature-branch and Pull Request workflow.

main
  ↓
Create Feature Branch
  ↓
Develop Feature
  ↓
Commit Changes
  ↓
Push Feature Branch
  ↓
Create Pull Request
  ↓
Review
  ↓
Merge into main
  ↓
Pull Updated main

This workflow keeps the main branch stable while allowing individual features to be developed and reviewed independently.

---

# Security

The following files and directories are excluded from version control:

.env
venv/
__pycache__/
*.pyc
*.pkl
.ipynb_checkpoints/

This prevents sensitive credentials, local environments, temporary files, and generated model artifacts from being accidentally committed.

---

# Future Improvements

- Cloud deployment
- Automated data ingestion
- Real-time business data
- Cloud PostgreSQL integration
- Filter-aware forecasting
- Advanced anomaly detection
- Customer segmentation
- Advanced demand forecasting
- Automated business recommendations
- Authentication and role-based access
- Automated model retraining
- CI/CD pipeline

---

# Project Outcome

BusinessPulse demonstrates a complete end-to-end data science and business intelligence workflow.

Data Collection
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
PostgreSQL & SQL Analytics
      ↓
Machine Learning
      ↓
Sales Forecasting
      ↓
Interactive Dashboard
      ↓
Business Insights

The project brings together data processing, business analytics, database management, machine learning, forecasting, visualization, and application development into a single platform.

---

# Author

## Pranamya G

Computer Science (Data Science)

RNS Institute of Technology, Bengaluru
