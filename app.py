import streamlit as st
# from modules.policy_analyzer import analyze_policy
from modules.scam_detector import detect_scam
from modules.risk_profiler import generate_risk_profile

st.set_page_config(layout="wide")
st.title("🛡️ FinGuardian – Your AI for Financial Protection")

tab1, tab2, tab3 = st.tabs(["📄 Policy Analyzer", "🚨 Scam Detector", "📊 Risk Profiler"])

with tab1:
    st.subheader("Upload Your Insurance Policy")
    file = st.file_uploader("Upload PDF", type="pdf")
    # if file:
    #     st.markdown(analyze_policy(file))
    pass

with tab2:
    st.subheader("Check for Financial Scam")
    message = st.text_area("Paste message here")
    if st.button("Check"):
        st.markdown(detect_scam(message))

with tab3:
    st.subheader("Financial Risk Estimator")
    age = st.slider("Age", 18, 75, 30)
    income = st.number_input("Annual Income (₹)", 100000)
    dependents = st.slider("Dependents", 0, 5, 1)
    loans = st.checkbox("Do you have outstanding loans?")
    if st.button("Analyze"):
        st.plotly_chart(generate_risk_profile(age, income, dependents, loans))
