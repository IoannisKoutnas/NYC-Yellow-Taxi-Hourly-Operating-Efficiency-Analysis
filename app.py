import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="NYC Yellow Taxi Efficiency", page_icon="🚕", layout="wide")

st.title("🚕 NYC Yellow Taxi Hourly Operating Efficiency")
st.caption("John Koutnas - Junior Data Analyst")

hourly = pd.DataFrame({
    "pickup_hour": list(range(24)),
    "trips": [203243,145704,106468,75567,58953,72748,174484,299619,368535,360827,356337,370205,395539,398060,426430,445472,412945,461257,508267,468688,417339,403979,363462,276872],
    "trip_share_pct": [2.684493,1.924501,1.406261,0.998111,0.778669,0.960877,2.304636,3.957456,4.867719,4.765909,4.706604,4.889777,5.224396,5.257694,5.632413,5.883926,5.454299,6.092418,6.713340,6.190569,5.512337,5.335874,4.800713,3.657007],
    "median_duration_min": [9.916667,9.616667,9.316667,9.216667,9.55,7.866667,7.666667,9.316667,10.65,10.983333,10.8,10.766667,10.65,10.583333,10.7,10.683333,10.516667,10.733333,10.55,10.033333,9.983333,10.133333,10.216667,10.05],
    "median_rev_per_hour": [80.104265,80.608696,81.697417,83.799582,88.21978,95.414634,82.204724,71.958042,65.831202,65.429126,66.101695,65.344538,66.070234,66.540284,65.498652,65.049505,70.159091,69.333333,70.645161,74.328358,75.327731,76.338028,77.045455,79.0282],
    "median_rev_per_mile": [5.939394,5.89081,5.827815,5.605096,5.130435,5.470019,5.880952,6.636364,7.55,7.733333,7.535714,7.555556,7.462963,7.280702,7.291667,7.314286,7.608696,7.788079,7.787611,7.428571,6.767857,6.460177,6.277778,6.073026],
    "median_tip_ratio": [0.2104,0.210417,0.209259,0.18,0.074074,0.137778,0.166667,0.201538,0.208205,0.208,0.206522,0.205714,0.204923,0.204,0.202885,0.203077,0.208421,0.211852,0.215,0.216,0.21625,0.215758,0.214706,0.212093]
})

st.sidebar.header("Filters")
metric = st.sidebar.selectbox("Chart metric", ["trips", "median_duration_min", "median_rev_per_hour", "median_rev_per_mile", "median_tip_ratio"])
start_hour, end_hour = st.sidebar.slider("Pickup-hour range", 0, 23, (0, 23))
filtered = hourly[hourly.pickup_hour.between(start_hour, end_hour)]

labels = {
    "trips": "Trips",
    "median_duration_min": "Median duration (minutes)",
    "median_rev_per_hour": "Median revenue per hour ($)",
    "median_rev_per_mile": "Median revenue per mile ($)",
    "median_tip_ratio": "Median tip ratio"
}

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total trips", f"{hourly.trips.sum():,.0f}")
c2.metric("Mean revenue/hour", "$78.26")
c3.metric("Median revenue/hour", "$71.43")
c4.metric("Mean tip ratio", "15%")

st.subheader("Hourly operating profile")
chart = alt.Chart(filtered).mark_line(point=True).encode(
    x=alt.X("pickup_hour:O", title="Pickup hour"),
    y=alt.Y(f"{metric}:Q", title=labels[metric]),
    tooltip=[alt.Tooltip("pickup_hour:O", title="Hour"), alt.Tooltip(f"{metric}:Q", title=labels[metric], format=",.2f"), alt.Tooltip("trips:Q", format=",.0f")]
).properties(height=430)
st.altair_chart(chart, use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Trip volume by hour")
    st.bar_chart(hourly.set_index("pickup_hour")["trips"], height=350)
with right:
    st.subheader("Revenue efficiency")
    efficiency = hourly.set_index("pickup_hour")[["median_rev_per_hour", "median_rev_per_mile"]]
    st.line_chart(efficiency, height=350)

st.subheader("Key findings")
st.markdown("""
- The busiest period is **18:00**, with 508,267 trips and a 6.71% share of all trips.
- The highest median revenue per hour occurs at **05:00**, reaching $95.41, but that hour has relatively low demand.
- Median revenue per mile peaks at **17:00** at $7.79 and remains strong during the evening period.
- The lowest median tip ratio occurs at **04:00** at 7.4%; tip ratios are generally around 20–22% during busier daytime and evening hours.
""")

st.subheader("Hourly results")
display = filtered.copy()
display["median_tip_ratio"] = display["median_tip_ratio"] * 100
display = display.rename(columns={"median_tip_ratio": "median_tip_pct"})
st.dataframe(display, use_container_width=True, hide_index=True)

st.download_button("Download hourly results", display.to_csv(index=False), "hourly_taxi_efficiency.csv", "text/csv")
