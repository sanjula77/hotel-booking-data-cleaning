# 🧼 Data Cleaning Report: Hotel Booking Dataset

---

## 1. 📊 Original Dataset Statistics

- **Shape**: 119,390 rows × 32 columns
- **Missing Values**:
  - `company`: 94.3%
  - `agent`: 13.7%
  - `country`: 0.4%
  - `children`: 4 rows
- **Duplicates**: 31,994 exact duplicate rows
- **Zero Guests**: 180 rows with `adults + children + babies = 0`
- **Unclean Columns**: Separate date fields, inconsistent labels (`'Undefined'`)

---

## 2. 🛑 Issues Identified & Their Impact

| Issue                       | Impact on Analysis                           |
| --------------------------- | -------------------------------------------- |
| Missing values              | Leads to incorrect modeling/training         |
| Duplicates                  | Skews distributions and frequency counts     |
| Outliers (e.g., adr = 5400) | Affects mean/median and regression models    |
| Inconsistent categories     | Affects grouping/aggregation                 |
| Zero total guests           | Logically invalid rows                       |
| Separate date columns       | Harder to filter/sort by actual arrival date |

---

## 3. 🧠 Cleaning Strategies & Rationale

| Step                          | Strategy                                   | Rationale                               |
| ----------------------------- | ------------------------------------------ | --------------------------------------- |
| Missing `children`            | Fill with 0                                | Only 4 rows; assume MCAR                |
| Missing `country`             | Fill with mode (`'PRT'`)                   | Most common entry, low missing %        |
| Missing `agent` and `company` | Fill with 0                                | Assumed no agent/company involvement    |
| Duplicates                    | Removed exact duplicate rows               | 100% identical, unnecessary repetitions |
| `total_guests = 0`            | Rows removed                               | Invalid booking                         |
| Negative `adr`                | Removed                                    | Illogical ADR                           |
| Outliers (`adr`, `lead_time`) | Capped using IQR                           | Retain scale, reduce skew               |
| Date fields                   | Combined into single `arrival_date` column | Simplified date filtering               |
| Inconsistent labels           | Replaced `'Undefined'` with `'Other'`      | Better interpretation                   |

---

## 4. 📊 Expected Outcomes Summary Table

This section summarizes the key issues identified before cleaning and the improvements made after the data cleaning process.

| 🧩 **Aspect**         | 🔍 **Before Cleaning**                                                                 | ✅ **After Cleaning**                                               |
|-----------------------|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| **Missing Values**     | Present in ~4 columns:<br>• `children`<br>• `country`<br>• `agent`<br>• `company`       | All missing values imputed:<br>• Logic-based or statistical methods applied |
| **Duplicates**         | ~31,994 exact duplicate rows                                                           | All exact duplicates removed                                        |
| **Outliers**           | Extreme values in:<br>• `adr` (up to 5400)<br>• `lead_time` (up to 737)                | Outliers treated using:<br>• IQR capping<br>• Z-score analysis      |
| **Categorical Issues** | Inconsistent labels:<br>• `'Undefined'`<br>• Case variations and typos                 | All categories standardized:<br>• Replaced with `'Other'` or cleaned |
| **Invalid Rows**       | 180 bookings with `total_guests = 0` (illogical combinations)                          | All such rows removed                                               |
| **Date Columns**       | Arrival date split across:<br>• `year`, `month`, `day`                                 | Combined into single `arrival_date` column in datetime format       |
| **Overall Quality**    | Raw, inconsistent, and error-prone dataset                                             | Cleaned, structured, and analysis-ready dataset with ~118,000 rows  |

---


## 5. 📉 Final Dataset Statistics

- **Final Shape**: 87,210 rows × 35 columns (added `arrival_date` & `total_guests`)
- **Missing Values**: 0 (after imputation)
- **No duplicates**
- **No invalid numeric values**
- **No zero-guest records**

---

## 6. 🔍 Assumptions Made During Cleaning

- If `children` is missing → assume 0
- If `agent` or `company` is missing → assume booking was made directly
- ADR outliers above IQR bound were capped, not removed
- Bookings with total guests = 0 are considered invalid and were removed
- Replaced ambiguous values like `'Undefined'` with `'Other'` instead of dropping

---

✅ The dataset is now fully cleaned, structured, and ready for EDA, visualization, or modeling.
