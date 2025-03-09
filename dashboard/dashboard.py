import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Set page configuration
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# Title
st.title("🚲 Bike Sharing Analysis Dashboard")

# Load data
@st.cache_data
def load_data():
    try:
        # Get the parent directory path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        data_dir = os.path.join(parent_dir, 'data')
        
        # Load the CSV files
        day_df = pd.read_csv(os.path.join(data_dir, 'day.csv'))
        hour_df = pd.read_csv(os.path.join(data_dir, 'hour.csv'))
        
        # Convert date columns
        day_df['dteday'] = pd.to_datetime(day_df['dteday'])
        hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
        
        return day_df, hour_df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None

day_df, hour_df = load_data()

if day_df is not None and hour_df is not None:
    # Sidebar filters
    st.sidebar.header("📊 Filters")
    
    # Date range filter
    st.sidebar.subheader("Date Range")
    date_range = st.sidebar.date_input(
        "Select Date Range",
        [day_df['dteday'].min(), day_df['dteday'].max()],
        min_value=day_df['dteday'].min(),
        max_value=day_df['dteday'].max()
    )
    
    # Season filter
    season_labels = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    selected_seasons = st.sidebar.multiselect(
        "Select Seasons",
        options=list(season_labels.values()),
        default=list(season_labels.values())
    )
    
    # Weather filter
    weather_labels = {
        1: 'Clear',
        2: 'Mist/Cloudy',
        3: 'Light Rain/Snow',
        4: 'Heavy Rain/Snow'
    }
    selected_weather = st.sidebar.multiselect(
        "Select Weather Conditions",
        options=list(weather_labels.values()),
        default=list(weather_labels.values())
    )
    
    # Day type filter
    day_type_labels = {0: 'Weekend/Holiday', 1: 'Working Day'}
    selected_day_types = st.sidebar.multiselect(
        "Select Day Types",
        options=list(day_type_labels.values()),
        default=list(day_type_labels.values())
    )

    # Filter the dataframes
    # Convert labels back to numeric values for filtering
    season_nums = [k for k, v in season_labels.items() if v in selected_seasons]
    weather_nums = [k for k, v in weather_labels.items() if v in selected_weather]
    day_type_nums = [k for k, v in day_type_labels.items() if v in selected_day_types]
    
    # Apply filters
    mask = (
        (day_df['dteday'].dt.date >= date_range[0]) &
        (day_df['dteday'].dt.date <= date_range[1]) &
        (day_df['season'].isin(season_nums)) &
        (day_df['weathersit'].isin(weather_nums)) &
        (day_df['workingday'].isin(day_type_nums))
    )
    filtered_day_df = day_df[mask]
    
    # Filter hour_df based on the same date range and conditions
    hour_mask = (
        (hour_df['dteday'].dt.date >= date_range[0]) &
        (hour_df['dteday'].dt.date <= date_range[1]) &
        (hour_df['season'].isin(season_nums)) &
        (hour_df['weathersit'].isin(weather_nums)) &
        (hour_df['workingday'].isin(day_type_nums))
    )
    filtered_hour_df = hour_df[hour_mask]

    st.markdown("---")

    # Main KPIs
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_rentals = filtered_day_df['cnt'].sum()
        st.metric("Total Bike Rentals", f"{total_rentals:,}")

    with col2:
        avg_daily_rentals = int(filtered_day_df['cnt'].mean())
        st.metric("Average Daily Rentals", f"{avg_daily_rentals:,}")

    with col3:
        max_daily_rentals = filtered_day_df['cnt'].max()
        st.metric("Max Daily Rentals", f"{max_daily_rentals:,}")

    with col4:
        total_days = len(filtered_day_df)
        st.metric("Total Days Analyzed", f"{total_days:,}")

    # Daily Trends
    st.subheader("Daily Rental Trends")
    fig_daily = px.line(filtered_day_df, x='dteday', y='cnt', 
                    title='Daily Bike Rental Trends')
    fig_daily.update_layout(xaxis_title="Date", yaxis_title="Number of Rentals")
    st.plotly_chart(fig_daily, use_container_width=True)

    # Create two columns for charts
    col1, col2 = st.columns(2)

    with col1:
        # Weather Analysis
        st.subheader("Weather Impact on Rentals")
        weather_impact = filtered_day_df.groupby('weathersit')['cnt'].mean().round()
        weather_df = pd.DataFrame({
            'Weather': [weather_labels.get(i, f'Weather {i}') for i in weather_impact.index],
            'Average Rentals': weather_impact.values
        })
        fig_weather = px.bar(weather_df, x='Weather', y='Average Rentals',
                            title='Average Rentals by Weather Condition')
        st.plotly_chart(fig_weather, use_container_width=True)

    with col2:
        # Hourly Pattern
        st.subheader("Hourly Rental Pattern")
        hourly_pattern = filtered_hour_df.groupby('hr')['cnt'].mean()
        fig_hourly = px.line(hourly_pattern, title='Average Hourly Rental Pattern')
        fig_hourly.update_layout(xaxis_title="Hour of Day", yaxis_title="Average Rentals")
        st.plotly_chart(fig_hourly, use_container_width=True)

    # Create two more columns for additional charts
    col1, col2 = st.columns(2)

    with col1:
        # Seasonal Analysis
        st.subheader("Seasonal Analysis")
        filtered_day_df['season_name'] = filtered_day_df['season'].map(season_labels)
        seasonal_avg = filtered_day_df.groupby('season_name')['cnt'].mean()
        seasonal_avg = seasonal_avg.reindex(['Spring', 'Summer', 'Fall', 'Winter'])
        fig_seasonal = px.bar(seasonal_avg, title='Average Rentals by Season')
        fig_seasonal.update_layout(xaxis_title="Season", yaxis_title="Average Rentals")
        st.plotly_chart(fig_seasonal, use_container_width=True)

    with col2:
        # Working Day Analysis
        st.subheader("Working Day vs Weekend")
        workday_avg = filtered_day_df.groupby('workingday')['cnt'].mean()
        workday_df = pd.DataFrame({
            'Day Type': ['Weekend/Holiday', 'Working Day'],
            'Average Rentals': workday_avg.values
        })
        fig_workday = px.bar(workday_df, x='Day Type', y='Average Rentals',
                            title='Average Rentals: Working Days vs Weekends')
        st.plotly_chart(fig_workday, use_container_width=True)

    # Data Tables
    st.markdown("---")
    st.subheader("Raw Data")
    tab1, tab2 = st.tabs(["Daily Data", "Hourly Data"])

    with tab1:
        st.dataframe(filtered_day_df)

    with tab2:
        st.dataframe(filtered_hour_df)
else:
    st.error("Failed to load the data. Please check if the CSV files are in the correct location.")