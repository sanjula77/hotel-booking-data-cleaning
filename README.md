# 🏨 Hotel Booking Data Cleaning & Feature Engineering Project

This project demonstrates a complete workflow for cleaning, preprocessing, feature engineering, and evaluating the quality of a hotel booking dataset. It follows industry-standard best practices to build a **reusable data pipeline**, assess and **improve data quality**, and prepare a final dataset for analysis or machine learning.

---

## 📦 Project Structure

```
project-root/
│
├── data/
│   ├── hotel_bookings.csv              # Original dataset
│   └── hotel_booking_cleaned.csv       # Cleaned final dataset
│
├── scripts/
│   ├── pipeline_functions.py           # Modular cleaning pipeline
│   ├── test_pipline_cleaned.csv        # Test output (optional)
│   └── __pycache__/                    # Python cache files
│       └── pipeline_functions.cpython-37.pyc
│
├── notebooks/
│   └── data_cleaning.ipynb             # Interactive Jupyter notebook
│
├── reports/
│   ├── data_cleaning_report.md         # Data cleaning summary report
│   └── Data_Dictionary.md              # Data dictionary for all columns
│
└── README.md                           # Project documentation
```

---

## 🎯 Objectives

- Clean raw hotel booking data (handle missing values, duplicates, outliers)
- Standardize inconsistent formats (dates, categories)
- Engineer useful features (e.g., stay length, total revenue, loyalty)
- Build a **reusable and scalable cleaning pipeline**
- Evaluate and visualize data quality before and after cleaning
- Document the cleaning process and final dataset

---

## 🧼 Cleaning Workflow

**Phase 1: Data Exploration**

- Inspect structure, types, and missingness
- Identify invalid values and column types

**Phase 2: Data Cleaning**

- Impute missing values (`children`, `agent`, `country`, `company`)
- Remove duplicates and impossible guest counts
- Detect and cap outliers (`adr`, `lead_time`)
- Fix inconsistencies in date and category fields

**Phase 3: Feature Engineering**

- Create new features: `stay_length`, `total_guests`, `is_weekend_arrival`, `season`, `total_revenue`, `lead_time_category`, `loyal_and_stable`

**Phase 4: Pipeline & Automation**

- Modularize steps in `pipeline_functions.py`
- Run the entire pipeline with `clean_dataset(df)`
- Validate integrity with built-in checks

---

## 📊 Data Quality Dashboard

Visual comparison of key metrics **before and after cleaning**:

| Metric            | Before    | After      |
| ----------------- | --------- | ---------- |
| % Missing Columns | ✔️        | ✅ 0       |
| Duplicate Rows    | ❌ 31,994 | ✅ 0       |
| Zero Guest Rows   | ❌ 180    | ✅ 0       |
| ADR Outliers      | ❌ 3,793  | ✅ Reduced |

![Dashboard Preview](reports/comparison_dashboard.png)

---

## 📈 Key Features Engineered

| Feature Name         | Description                          |
| -------------------- | ------------------------------------ |
| `stay_length`        | Total nights stayed                  |
| `total_guests`       | Adults + Children + Babies           |
| `total_revenue`      | Revenue = `adr × stay_length`        |
| `is_weekend_arrival` | Arrival on Saturday or Sunday        |
| `season`             | Winter, Spring, Summer, Autumn       |
| `loyal_and_stable`   | Repeat guest with no booking changes |

---

## 🚀 Usage

### 1. Load and Clean Data

```python
from scripts.pipeline_functions import load_data, clean_dataset

df_raw = load_data("data/hotel_bookings.csv")
df_cleaned = clean_dataset(df_raw)
df_cleaned.to_csv("data/hotel_booking_cleaned.csv", index=False)
```

### 2. Run Quality Metrics

```python
from scripts.pipeline_functions import generate_quality_metrics

generate_quality_metrics(df_raw, name="Raw Dataset")
generate_quality_metrics(df_cleaned, name="Cleaned Dataset")
```

---

## 📚 Data Dictionary

See `reports/Data_Dictionary.md` for a full description of all columns.

| Column        | Type   | Description                      |
| ------------- | ------ | -------------------------------- |
| hotel         | object | City Hotel / Resort Hotel        |
| lead_time     | int    | Days between booking and arrival |
| adr           | float  | Average daily rate               |
| children      | int    | Number of children in booking    |
| total_guests  | int    | Total number of guests           |
| stay_length   | int    | Total nights stayed              |
| season        | object | Booking season                   |
| total_revenue | float  | Estimated total booking revenue  |

---

## 🛠️ Tools Used

- Python (pandas, NumPy)
- Matplotlib / Seaborn / Plotly
- Jupyter Notebook
- Custom pipeline in `.py` module
- Versioned with Git

---

## 🧠 Assumptions Made

- Missing `children` = 0 (MCAR)
- Missing `country` filled with mode (MAR)
- Missing `agent`, `company` = 0 → No agent/company involved (MAR)
- Guest counts (adults, children, babies) cannot all be zero

---

## 📤 Output

- Cleaned CSV: `data/hotel_booking_cleaned.csv`
- Automated report: `reports/data_cleaning_report.md`
- Data dictionary: `reports/Data_Dictionary.md`
- Dashboard: `reports/comparison_dashboard.png`

---

## 👨‍💻 Author

Gihan Sanjula — IT Undergraduate at Horizon Campus  
Learning modern data cleaning & analysis best practices

---

## 📄 License

This project is licensed under the MIT License.

---

## ✅ Next Steps

Would you like to:

- Generate the `data_cleaning_report.md` for the `/reports` folder?
- Finalize a `Data_Dictionary.md` file?
- Organize and push this to GitHub with commit suggestions?

Let me know and I’ll help you wrap everything up cleanly 🚀
