# Data Cleaning Report: Hotel Booking Dataset

**Date:** 2024-07-29

**Author:** Gemini

---

## Executive Summary

This report details the cleaning process for the hotel booking dataset. The original dataset contained 119,390 rows and 32 columns, with significant issues including missing values, duplicate records, and inconsistencies. The cleaning process addressed these issues, resulting in a final dataset of 87,210 rows and 35 columns, ready for analysis.

---

## 1. Initial Dataset Profile

- **Dimensions:** 119,390 rows, 32 columns
- **Key Issues:**
    - **Missing Data:**
        - `company`: 94.3%
        - `agent`: 13.7%
        - `country`: 0.4%
        - `children`: 4 rows
    - **Duplicate Records:** 31,994 duplicate rows
    - **Invalid Data:** 180 rows with zero guests
    - **Inconsistent Formatting:** Date information split across multiple columns, use of 'Undefined' label.

---

## 2. Identified Data Quality Issues and Impacts

| Issue                       | Impact on Analysis                                       |
| --------------------------- | -------------------------------------------------------- |
| **Missing Values**          | Can lead to biased or incorrect models.                  |
| **Duplicate Records**       | Skews distributions and inflates sample size.            |
| **Outliers**                | Can distort statistical measures and model performance.  |
| **Inconsistent Categories** | Hinders accurate grouping and aggregation.               |
| **Zero Guests**             | Represents logically impossible or invalid bookings.     |
| **Separate Date Columns**   | Complicates time-based analysis and filtering.           |

---

## 3. Cleaning Methodology

| Step                          | Action                                       | Rationale                                                 |
| ----------------------------- | -------------------------------------------- | --------------------------------------------------------- |
| **Handle Missing `children`** | Filled with 0.                               | Minimal number of missing rows; assumed to be zero.       |
| **Handle Missing `country`**  | Filled with the mode ('PRT').                | Most frequent value, minimal data loss.                   |
| **Handle Missing `agent`/`company`** | Filled with 0.                            | Assumed direct bookings with no agent or company.         |
| **Remove Duplicates**         | Deleted all exact duplicate rows.            | Redundant and unnecessary information.                    |
| **Remove Invalid Bookings**   | Deleted rows where `total_guests` was 0.     | These bookings are not valid.                             |
| **Correct `adr`**             | Removed rows with negative `adr`.            | Average Daily Rate cannot be negative.                    |
| **Cap Outliers**              | Capped `adr` and `lead_time` using the IQR.  | Reduces skew while retaining data.                        |
| **Combine Date Fields**       | Merged into a single `arrival_date` column.  | Simplifies date-based operations.                         |
| **Standardize Labels**        | Replaced 'Undefined' with 'Other'.           | Improves clarity and consistency.                         |

---

## 4. Comparison: Before and After Cleaning

| Aspect             | Before Cleaning                               | After Cleaning                                  |
| ------------------ | --------------------------------------------- | ----------------------------------------------- |
| **Missing Values** | Present in `children`, `country`, `agent`, `company`. | All missing values handled.                     |
| **Duplicates**     | 31,994 duplicate records.                     | All duplicates removed.                         |
| **Outliers**       | Extreme values in `adr` and `lead_time`.      | Outliers capped using the IQR method.           |
| **Inconsistencies**| 'Undefined' labels, separate date columns.    | Standardized labels, single `arrival_date` column. |
| **Invalid Rows**   | 180 rows with zero guests.                    | All invalid rows removed.                       |
| **Date Columns**   | `year`, `month`, `day` columns.               | Single `arrival_date` (datetime object).        |
| **Final Shape**    | 119,390 rows, 32 columns                      | 87,210 rows, 35 columns                         |

---

## 5. Final Dataset Statistics

- **Shape:** 87,210 rows, 35 columns (including `arrival_date` and `total_guests`)
- **Missing Values:** 0
- **Duplicates:** 0
- **Invalid Numeric Values:** 0
- **Zero-Guest Records:** 0

---

## 6. Assumptions

- Missing `children` values imply zero children.
- Missing `agent` or `company` values imply a direct booking.
- Outliers in `adr` were capped rather than removed to preserve data.
- Bookings with zero guests are invalid.
- 'Undefined' values were categorized as 'Other'.

---

## Conclusion

The dataset is now clean, consistent, and ready for exploratory data analysis, visualization, and predictive modeling.