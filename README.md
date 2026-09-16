# NYC Yellow Taxi — Hourly Operating Efficiency Analysis

Analysis of 7.7 million NYC yellow taxi trips to identify operational inefficiencies and revenue optimization opportunities, using trip-level data from the NYC Taxi & Limousine Commission (TLC).

## Objective

Identify when driver time is being converted into earnings efficiently, and when high trip volume masks poor productivity. The analysis moves past raw trip counts to measure revenue per hour, revenue per mile, and trip duration, then translates the findings into operational recommendations for drivers, fleet operators, and regulators.

## Data Source

New York City Taxi & Limousine Commission (TLC) — Yellow Taxi Trip Records, January 2019.
Public dataset available at: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

## Methodology

1. Data validation and schema inspection
2. Rule-based data cleaning (physical and economic plausibility constraints on duration, distance, fare, and speed)
3. Feature engineering (trip duration, implied speed, revenue per hour, revenue per mile, tip ratio)
4. Hourly aggregation using median-based, outlier-resistant statistics
5. Diagnostic analysis of demand versus efficiency by pickup hour
6. Operational recommendations for drivers, fleet operators, and regulators

## Key Findings

- Trip volume and driver profitability are not the same thing. The busiest hours are not the most productive.
- The highest median revenue per hour occurs at 05:00 ($95.41/hr), despite this hour accounting for under 1% of daily trip volume.
- Midday hours (11:00–14:00) generate the highest trip volume but the lowest revenue per hour (as low as $65.05/hr), driven by congestion and longer trip durations.
- Revenue per mile stays comparatively stable across the day, indicating that lost driver income is a function of time lost to traffic, not distance-based pricing.

## Tech Stack

- Python (Pandas, NumPy) — data cleaning, validation, feature engineering
- Jupyter Notebook — exploratory analysis and documentation
- Streamlit, Altair — interactive dashboard
- Power BI, Excel — supplementary dashboard design and validation

## Author

Ioannis Koutnas
LinkedIn: https://www.linkedin.com/in/ioanniskoutnas/
Portfolio: https://johnkoutnas-portfolio.netlify.app
