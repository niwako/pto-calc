import streamlit as st
import pto

st.write("# PTO Calculator")

as_of = st.date_input("Expected balance as of")

current_pto = st.number_input("Current PTO balance in hours", value=0)

pto_days = st.slider("PTO days per year", 1, 50, 15, 1)
daily_accrual_rate = pto_days * 8 / 365

total_pto = pto.calculate(as_of, current_pto, daily_accrual_rate)
st.metric(f"Expected total PTO hours on {as_of}", f"{total_pto: .2f}")
