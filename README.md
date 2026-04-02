# 🛒 Shopping Mall Data Pipeline

A batch data pipeline that ingests transactional data from MySQL, transforms it using PySpark, and loads it into BigQuery for analytics.

---

## 🛠️ Tech Stack

- Python
- Pandas
- PySpark
- SQLAlchemy
- Google Cloud Storage
- BigQuery

---

## 🔄 Workflow

> <img width="1750" height="398" alt="image" src="https://github.com/user-attachments/assets/b7a24d3d-46d4-4122-b8b5-955f58ee6fc5" />


| Step | Description | Tools |
|------|-------------|-------|
| 1. Ingest | Extract all tables from MySQL, upload to GCS as Parquet | Python, SQLAlchemy, GCS |
| 2. Clean | Drop nulls, fix data types, remove duplicates | PySpark |
| 3. Transform | JOIN transaction + customer + product tables | PySpark SQL |
| 4. Load | Write processed data to BigQuery | BigQuery |

---

## 📊 Dataset

Shopping mall transactional dataset with 3 tables:

| Table | Description |
|-------|-------------|
| `transaction` | Sales transactions with TransactionNo, Date, Price, Quantity |
| `customer` | Customer information |
| `product` | Product catalog with category |

---

## 🔍 Data Cleaning

- Drop null values in key columns
- Fix data types (e.g. `CustomerNo` Double → String)
  ><img width="480" height="279" alt="image" src="https://github.com/user-attachments/assets/9791047e-7fac-48d9-a895-ccde24287d51" />

- Filter out invalid records (negative Quantity)
  > <img width="583" height="110" alt="image" src="https://github.com/user-attachments/assets/b64a1d8e-d6aa-4493-81a5-8fe37d60894c" />

---

## 📈 BigQuery Output

Final table contains joined data from all 3 sources:

| Column | Type | Source |
|--------|------|--------|
| TransactionNo | STRING | transaction |
| Date_time | TIMESTAMP | transaction |
| Quantity | INTEGER | transaction |
| Price | DOUBLE | transaction |
| CustomerNo | STRING | customer |
| CustomerName | STRING | customer |
| Country | STRING | customer |
| ProductNo | STRING | product |
| ProductName | STRING | product |
| Category | STRING | product |
| Total_Sales | DOUBLE | Price × Quantity (Feature Engineering)|

> <img width="1394" height="572" alt="image" src="https://github.com/user-attachments/assets/27f0d2cd-ad1e-41e3-8fbd-e12c591f773b" />


---

## 📝 What I Learned

- Building an end-to-end batch data pipeline on GCP
- Using PySpark for large-scale data transformation
- Managing GCS bucket structure (raw / clean / processed zones)
