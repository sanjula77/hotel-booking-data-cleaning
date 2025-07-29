import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

def load_data(path):
    """Load dataset from CSV file"""
    try:
        df = pd.read_csv(path)
        print(f"✅ Data loaded successfully from {path}")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None
    
def handle_missing_values(df):
    """Fill missing values with appropriate defaults."""
    df['children'].fillna(0, inplace=True)
    df['country'].fillna(df['country'].mode()[0], inplace=True)
    df['agent'].fillna(0, inplace=True)
    df['company'].fillna(0, inplace=True)
    return df

def fix_inconsistencies(df):
    """Standardize values and fix logical issues."""
    # Replace 'Undefined' with 'Other'
    for col in ['meal', 'distribution_channel']:
        df[col] = df[col].replace('Undefined', 'Other')

    # Remove rows where total guests is 0
    df['total_guests'] = df['adults'] + df['children'] + df['babies']
    df = df[df['total_guests'] > 0]

    # Convert arrival date fields
    df['arrival_date'] = pd.to_datetime(df['arrival_date_year'].astype(str) + '-' +
                                        df['arrival_date_month'] + '-' +
                                        df['arrival_date_day_of_month'].astype(str),
                                        errors='coerce')
    return df

def remove_duplicates(df):
    """Drop exact duplicates."""
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"🧹 Removed {before - after} duplicate rows.")
    return df

def detect_outliers(df, col):
    """Detect outliers using IQR."""
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower) | (df[col] > upper)]
    print(f"📈 {col}: {len(outliers)} outliers detected.")
    return outliers

def engineer_features(df):
    """Add engineered features for modeling."""
    df['arrival_month'] = df['arrival_date'].dt.month
    df['arrival_dayofweek'] = df['arrival_date'].dt.dayofweek
    df['is_weekend_arrival'] = df['arrival_dayofweek'].isin([5, 6])
    df['season'] = df['arrival_month'].apply(lambda m: (
        'Winter' if m in [12, 1, 2] else
        'Spring' if m in [3, 4, 5] else
        'Summer' if m in [6, 7, 8] else 'Autumn'
    ))
    df['stay_length'] = df['stays_in_week_nights'] + df['stays_in_weekend_nights']
    df['is_long_stay'] = df['stay_length'] > 7
    df['total_revenue'] = df['adr'] * df['stay_length']
    df['has_special_requests'] = df['total_of_special_requests'] > 0
    df['lead_time_category'] = df['lead_time'].apply(lambda x: (
        'Short' if x <= 7 else 'Medium' if x <= 30 else 'Long'
    ))
    df['loyal_and_stable'] = (df['is_repeated_guest'] == 1) & (df['booking_changes'] == 0)
    return df

def validate_data(df):
    """Run integrity checks."""
    errors = 0

    # Check guests
    if (df['total_guests'] <= 0).any():
        print("❌ Error: Found 0-guest bookings.")
        errors += 1

    # Check ADR
    if (df['adr'] < 0).any():
        print("❌ Error: Found negative ADR values.")
        errors += 1

    # Check arrival_date
    if df['arrival_date'].isna().sum() > 0:
        print("❌ Warning: Missing arrival_date values.")

    if errors == 0:
        print("✅ Data validation passed.")
    return df

def clean_dataset(df):
    """Run full cleaning pipeline in order."""
    df = handle_missing_values(df)
    df = fix_inconsistencies(df)
    df = remove_duplicates(df)
    df = engineer_features(df)
    df = validate_data(df)
    return df
