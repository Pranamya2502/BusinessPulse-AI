import streamlit as st
import pandas as pd
import plotly.express as px
import joblib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="BusinessPulse",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM PROFESSIONAL LIGHT UI
# =========================================================

st.markdown(
    """
    <style>

    /* Main application background */
    .stApp {
        background-color: #F4F8FB;
        color: #172B4D;
    }

    /* Main content */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* Main title */
    h1 {
        color: #123B5D;
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    /* Section headings */
    h2, h3 {
        color: #1E5A88;
        font-weight: 600;
    }

    /* Caption */
    .stCaption {
        color: #607589;
    }

    /* KPI cards */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #D9E5EC;
        border-radius: 10px;
        padding: 18px;
        box-shadow: 0px 2px 8px rgba(30, 90, 136, 0.08);
    }

    [data-testid="stMetricLabel"] {
        color: #607589;
        font-weight: 500;
    }

    [data-testid="stMetricValue"] {
        color: #123B5D;
        font-weight: 700;
    }

    /* Select boxes */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF;
        border-color: #C9D9E3;
    }

    /* Buttons */
    .stButton > button {
        background-color: #1E5A88;
        color: white;
        border-radius: 7px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #17496F;
        color: white;
    }

    /* Divider */
    hr {
        border-color: #D9E5EC;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv(
    "data/processed/cleaned_superstore.csv"
)

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="mixed"
)


# =========================================================
# LOAD FORECAST
# =========================================================

forecast = pd.read_csv(
    "data/processed/sales_forecast.csv"
)

forecast["Forecast Month"] = pd.to_datetime(
    forecast["Forecast Month"]
)


# =========================================================
# LOAD ML MODEL
# =========================================================

model = joblib.load(
    "models/profit_prediction_model.pkl"
)


# =========================================================
# HEADER
# =========================================================

st.title("BusinessPulse")

st.caption(
    "Business Analytics & Sales Intelligence Platform"
)

st.divider()


# =========================================================
# FILTERS
# =========================================================

st.subheader("Business Performance")


regions = sorted(
    df["Region"].dropna().unique()
)

categories = sorted(
    df["Category"].dropna().unique()
)

segments = sorted(
    df["Segment"].dropna().unique()
)

years = sorted(
    df["Order Date"].dt.year.unique()
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    selected_region = st.selectbox(
        "Region",
        ["All Regions"] + regions
    )


with col2:

    selected_category = st.selectbox(
        "Category",
        ["All Categories"] + categories
    )


with col3:

    selected_segment = st.selectbox(
        "Segment",
        ["All Segments"] + segments
    )


with col4:

    selected_year = st.selectbox(
        "Year",
        ["All Years"] + years
    )


# =========================================================
# APPLY FILTERS
# =========================================================

filtered_df = df.copy()


if selected_region != "All Regions":

    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]


if selected_category != "All Categories":

    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]


if selected_segment != "All Segments":

    filtered_df = filtered_df[
        filtered_df["Segment"] == selected_segment
    ]


if selected_year != "All Years":

    filtered_df = filtered_df[
        filtered_df["Order Date"].dt.year == selected_year
    ]


# =========================================================
# KPI CALCULATIONS
# =========================================================

total_sales = filtered_df["Sales"].sum()

total_profit = filtered_df["Profit"].sum()

total_orders = filtered_df["Order ID"].nunique()

total_quantity = filtered_df["Quantity"].sum()


if total_sales != 0:

    profit_margin = (
        total_profit / total_sales
    ) * 100

else:

    profit_margin = 0


# =========================================================
# KPI CARDS
# =========================================================

st.subheader("Key Performance Indicators")


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Sales",
        f"${total_sales:,.0f}"
    )


with col2:

    st.metric(
        "Total Profit",
        f"${total_profit:,.0f}"
    )


with col3:

    st.metric(
        "Total Orders",
        f"{total_orders:,}"
    )


with col4:

    st.metric(
        "Profit Margin",
        f"{profit_margin:.2f}%"
    )


st.divider()


# =========================================================
# SALES BY CATEGORY
# =========================================================

st.subheader("Sales Analysis")


category_sales = (
    filtered_df
    .groupby("Category")["Sales"]
    .sum()
    .reset_index()
)


fig_category = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    title="Sales by Category",
    color="Category",
    color_discrete_sequence=[
        "#1E5A88",
        "#2A9D8F",
        "#5B8DB8"
    ]
)


fig_category.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="#F4F8FB",
    font=dict(color="#172B4D"),
    showlegend=False
)


st.plotly_chart(
    fig_category,
    width="stretch"
)


# =========================================================
# MONTHLY SALES
# =========================================================

monthly_sales = (
    filtered_df
    .groupby(
        pd.Grouper(
            key="Order Date",
            freq="MS"
        )
    )["Sales"]
    .sum()
    .reset_index()
)


fig_monthly = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="Monthly Sales Trend",
    markers=True
)


fig_monthly.update_traces(
    line=dict(
        color="#1E5A88",
        width=3
    ),
    marker=dict(
        size=6
    )
)


fig_monthly.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="#F4F8FB",
    font=dict(color="#172B4D")
)


st.plotly_chart(
    fig_monthly,
    width="stretch"
)


# =========================================================
# CATEGORY + REGION ANALYSIS
# =========================================================

col1, col2 = st.columns(2)


# -----------------------------
# PROFIT BY CATEGORY
# -----------------------------

with col1:

    category_profit = (
        filtered_df
        .groupby("Category")["Profit"]
        .sum()
        .reset_index()
    )


    fig_profit_category = px.bar(
        category_profit,
        x="Category",
        y="Profit",
        title="Profit by Category",
        color="Category",
        color_discrete_sequence=[
            "#2A9D8F",
            "#3AAFA9",
            "#78C6C0"
        ]
    )


    fig_profit_category.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#F4F8FB",
        font=dict(color="#172B4D"),
        showlegend=False
    )


    st.plotly_chart(
        fig_profit_category,
        width="stretch"
    )


# -----------------------------
# SALES BY REGION
# -----------------------------

with col2:

    region_sales = (
        filtered_df
        .groupby("Region")["Sales"]
        .sum()
        .reset_index()
    )


    fig_region_sales = px.bar(
        region_sales,
        x="Region",
        y="Sales",
        title="Sales by Region",
        color="Region",
        color_discrete_sequence=[
            "#1E5A88",
            "#3D7EA6",
            "#6A9FC0",
            "#91B8CF"
        ]
    )


    fig_region_sales.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#F4F8FB",
        font=dict(color="#172B4D"),
        showlegend=False
    )


    st.plotly_chart(
        fig_region_sales,
        width="stretch"
    )


# =========================================================
# PROFIT BY REGION
# =========================================================

region_profit = (
    filtered_df
    .groupby("Region")["Profit"]
    .sum()
    .reset_index()
)


fig_region_profit = px.bar(
    region_profit,
    x="Region",
    y="Profit",
    title="Profit by Region",
    color="Region",
    color_discrete_sequence=[
        "#2A9D8F",
        "#4AAE9F",
        "#73BFB2",
        "#9BD2C8"
    ]
)


fig_region_profit.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="#F4F8FB",
    font=dict(color="#172B4D"),
    showlegend=False
)


st.plotly_chart(
    fig_region_profit,
    width="stretch"
)


# =========================================================
# TOP 10 PRODUCTS
# =========================================================

st.subheader("Top 10 Products by Sales")


top_products = (
    filtered_df
    .groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)


top_products = top_products.sort_values(
    "Sales",
    ascending=True
)


fig_products = px.bar(
    top_products,
    x="Sales",
    y="Product Name",
    orientation="h",
    title="Top 10 Products by Sales"
)


fig_products.update_traces(
    marker_color="#1E5A88"
)


fig_products.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="#F4F8FB",
    font=dict(color="#172B4D")
)


st.plotly_chart(
    fig_products,
    width="stretch"
)


# =========================================================
# PROFITABLE VS LOSS-MAKING ORDER LINES
# =========================================================

st.subheader("Profitability Overview")


profitable_orders = (
    filtered_df["Profit"] >= 0
).sum()


loss_orders = (
    filtered_df["Profit"] < 0
).sum()


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Profitable Order Lines",
        f"{profitable_orders:,}"
    )


with col2:

    st.metric(
        "Loss-Making Order Lines",
        f"{loss_orders:,}"
    )


# =========================================================
# SALES FORECAST
# =========================================================

st.divider()

st.subheader("Sales Forecast")

st.caption(
    "Projected sales for the next six months based on historical sales patterns."
)


fig_forecast = px.line(
    forecast,
    x="Forecast Month",
    y="Forecast Sales",
    title="Next 6 Months Sales Forecast",
    markers=True
)


fig_forecast.update_traces(
    line=dict(
        color="#2A9D8F",
        width=3
    ),
    marker=dict(
        size=7
    )
)


fig_forecast.update_layout(
    plot_bgcolor="white",
    paper_bgcolor="#F4F8FB",
    font=dict(color="#172B4D")
)


st.plotly_chart(
    fig_forecast,
    width="stretch"
)


# =========================================================
# ML PROFIT PREDICTION
# =========================================================

st.divider()

st.subheader("Profit Prediction")

st.caption(
    "Estimate expected profit for a new order using the trained machine learning model."
)


col1, col2, col3 = st.columns(3)


# -----------------------------
# NUMERICAL INPUTS
# -----------------------------

with col1:

    prediction_sales = st.number_input(
        "Sales",
        min_value=0.0,
        value=500.0,
        step=50.0
    )


    prediction_quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=2,
        step=1
    )


    prediction_discount = st.slider(
        "Discount",
        min_value=0.0,
        max_value=1.0,
        value=0.10,
        step=0.05
    )


# -----------------------------
# PRODUCT INPUTS
# -----------------------------

with col2:

    prediction_category = st.selectbox(
        "Category",
        sorted(
            df["Category"].dropna().unique()
        )
    )


    prediction_subcategory = st.selectbox(
        "Sub-Category",
        sorted(
            df["Sub-Category"].dropna().unique()
        )
    )


    prediction_region = st.selectbox(
        "Region",
        sorted(
            df["Region"].dropna().unique()
        )
    )


# -----------------------------
# CUSTOMER / SHIPPING INPUTS
# -----------------------------

with col3:

    prediction_segment = st.selectbox(
        "Segment",
        sorted(
            df["Segment"].dropna().unique()
        )
    )


    prediction_ship_mode = st.selectbox(
        "Ship Mode",
        sorted(
            df["Ship Mode"].dropna().unique()
        )
    )


    prediction_shipping = st.number_input(
        "Shipping Days",
        min_value=0,
        value=3,
        step=1
    )


prediction_price = st.number_input(
    "Average Selling Price",
    min_value=0.0,
    value=250.0,
    step=25.0
)


# =========================================================
# PREDICT BUTTON
# =========================================================

if st.button(
    "Predict Profit",
    type="primary"
):

    prediction_data = pd.DataFrame({
        "Sales": [prediction_sales],
        "Quantity": [prediction_quantity],
        "Discount": [prediction_discount],
        "Shipping Days": [prediction_shipping],
        "Average Selling Price": [prediction_price],
        "Category": [prediction_category],
        "Sub-Category": [prediction_subcategory],
        "Region": [prediction_region],
        "Segment": [prediction_segment],
        "Ship Mode": [prediction_ship_mode]
    })


    predicted_profit = model.predict(
        prediction_data
    )[0]


    st.success(
        f"Estimated Profit: ${predicted_profit:,.2f}"
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "BusinessPulse | Business Analytics, Machine Learning & Sales Forecasting"
)