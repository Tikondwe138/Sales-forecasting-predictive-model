# Sales Forecasting Predictive Model

A time series forecasting project using ARIMA and Prophet to predict future sales for Rab Processors Ltd, a leading food production and distribution company in Malawi. This model helps in production planning, inventory control, and sales strategy by offering reliable sales forecasts based on historical data.

---

## 📊 Project Overview

This project demonstrates how time series models can be applied to real business challenges. Rab Processors, which deals with essential commodities like maize flour, cooking oil, and soya pieces, required a system to:

- Predict future sales trends
- Optimize inventory and reduce waste
- Improve planning and minimize stockouts

Using historical sales data, we built forecasting pipelines with ARIMA and Facebook Prophet to generate month-by-month forecasts for each product line.

---

## 🧠 Business Case: Rab Processors Ltd

**Client:** Rab Processors Ltd  
**Sector:** FMCG / Agribusiness  
**Location:** Malawi

Rab Processors is a key supplier of processed foods in Malawi. With seasonal fluctuations and changing consumer demand, traditional forecasting methods led to:

- Overproduction and underproduction issues
- Inventory wastage
- Inaccurate procurement and logistics planning

This model solves those problems using data-driven forecasting techniques.

---

## 🔍 Features

- Data cleaning and transformation for time series modeling
- Trend and seasonality decomposition
- Sales forecasts using both ARIMA and Prophet
- Visualizations of actual vs forecasted sales
- Exportable reports and metrics (MAPE, RMSE)
- Optional Streamlit dashboard for business users

---

## 🧱 Project Structure

```

sales-forecasting-predictive-model/
│
├── data/                          # Raw and processed sales data
├── notebooks/
│   ├── 01\_data\_preparation.ipynb
│   └── 02\_modeling\_and\_forecast.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── forecasting\_arima.py
│   ├── forecasting\_prophet.py
│   └── evaluation.py
│
├── reports/                       # Forecast reports and visualizations
├── app/                           # Optional: Streamlit app for visualization
├── README.md
├── requirements.txt
└── main.py                        # Entry point script

````

---

## 🔧 Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/sales-forecasting-predictive-model.git
cd sales-forecasting-predictive-model
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the notebooks or main script:

```bash
python main.py
```

---

## 📈 Models Used

* **ARIMA** – Autoregressive model for stationary data series
* **Facebook Prophet** – Ideal for handling seasonality and trend shifts in business data

---

## 📊 Results

* MAPE (Mean Absolute Percentage Error): \~7–10% (depending on product)
* Prophet showed stronger performance for seasonal products
* Sales spikes in Q4 identified for cooking oil and maize flour
* Forecasting accuracy improved operational planning decisions

---

## 📌 Takeaways

* Forecasting is essential for inventory-heavy businesses
* ARIMA works best for stable products; Prophet handles complex patterns
* A forecasting model adds long-term value by reducing uncertainty

---

## ✅ Future Improvements

* Automate model retraining monthly
* Integrate with ERP systems for real-time decision support
* Deploy as a hosted dashboard for non-technical stakeholders

---

## 👨‍💼 Contact

**Author:** Mr. Kaonga
**Role:** Business Analyst | Data Enthusiast | Malawi
**LinkedIn:** \[Your LinkedIn Here]
**Portfolio:** \[Your Google Site Here]

---

## 📝 License

This project is licensed for educational and professional portfolio use.

```

---

Let me know when you're ready for:

- A **dashboard version** of this using Streamlit
- A **PDF version** of the case study for offline/print use
- Or, turning this into a **LinkedIn post** or **Google Sites** page layout

Ready when you are.
```
