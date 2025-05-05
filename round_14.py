
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Brush Wear Rate Dashboard", layout="wide")

def calculate_hours_safe(current, rate):
    return [(c - 35) / r if pd.notna(c) and r and r > 0 and c > 35 else 0 for c, r in zip(current, rate)]

# Sample mock data for demonstration
upper_current = [40, 36, 38, 42, 30, 60, 45]
avg_rate_upper = [0.01, 0.02, 0.015, 0.025, 0.005, 0.03, 0.02]

hour_upper = calculate_hours_safe(upper_current, avg_rate_upper)
color_upper = ['black' if h < 500 else 'red' for h in hour_upper]

# Plotting
fig, ax = plt.subplots()
bars = ax.bar(range(len(hour_upper)), hour_upper, color=color_upper)
ax.set_title("Remaining Hours - Upper")
ax.set_ylabel("Hours")
ax.set_xticks(range(len(hour_upper)))
ax.set_xticklabels([str(i + 1) for i in range(len(hour_upper))])
for bar, val in zip(bars, hour_upper):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 10, f"{int(val)}", ha='center', fontsize=8)

st.pyplot(fig)
