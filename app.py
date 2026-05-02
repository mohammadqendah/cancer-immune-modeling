import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Tumor-Immune Dynamics", layout="wide")

st.title("Interactive ODE Dashboard: Tumor-Immune Dynamics")
st.markdown("**Mohammad Qendah** | Artificial Intelligence for Biomedicine and Healthcare")
st.markdown("---")

# --- SIDEBAR: INTERACTIVE CONTROLS ---
st.sidebar.header("Clinical Parameters")
st.sidebar.markdown("Adjust the sliders to simulate clinical scenarios live.")

# 1. T0 (To demonstrate the Late-Stage Paradox)
T0_exp = st.sidebar.slider("Initial Tumor Burden (Log10)", min_value=3, max_value=10, value=6, step=1)
T0 = 10**T0_exp

# 2. Immunosuppression (Bone Marrow Failure)
sigma_val = st.sidebar.number_input("Spontaneous Immune Production (sigma)", min_value=0.0, max_value=20000.0, value=13000.0, step=1000.0)

# 3. Tumor Antigenicity (Cold Tumor Evasion)
rho_exp = st.sidebar.slider("Immune Recruitment Rate (rho) [10^x]", min_value=-9, max_value=-5, value=-7)
rho_val = 10**rho_exp * 2.0  # Centers around 2.0e-7

# 4. Immunotherapy Drug (Kill Rate Multiplier)
k_mult = st.sidebar.slider("Immunotherapy Dose (k multiplier)", min_value=1, max_value=20, value=1, step=1)

# 5. Tumor Growth Kinetics (For Scenario 3: Indolent Tumor)
st.sidebar.markdown("---")
st.sidebar.markdown("**Tumor Kinetics**")
a = st.sidebar.slider("Tumor Growth Rate (a)", min_value=0.100, max_value=1.000, value=0.514, step=0.001, format="%.3f")
b = st.sidebar.slider("Capacity Factor (b)", min_value=0.0050, max_value=0.0500, value=0.0248, step=0.0001, format="%.4f")

# Baseline static parameters
delta = 0.0412
s_val = 1.0e-6
I0 = 1e5
days = 100
k_base = 3.23e-7
k_val = k_base * k_mult

# --- ODE SOLVER ---
def system(t, y):
    T = max(1.0, y[0]) # Floor at 1 cell
    I = max(1.0, y[1])
    dT = T * (a - b * np.log(T)) - k_val * T * I
    dI = sigma_val + (rho_val * T * I) / (1 + s_val * T) - delta * I
    return [dT, dI]

def tumor_only(t, y):
    T = max(1.0, y[0])
    return [T * (a - b * np.log(T))]

t_span = (0, days)
t_eval = np.linspace(0, days, 500)

sol = solve_ivp(system, t_span, [T0, I0], t_eval=t_eval, method='RK45')
sol_tumor = solve_ivp(tumor_only, t_span, [T0], t_eval=t_eval, method='RK45')

# --- DATA EXTRACTION ---
final_tumor = sol.y[0][-1]
peak_tumor = np.max(sol.y[0])
eliminated = np.any(sol.y[0] <= 1.0)

# --- TOP METRICS ROW ---
col1, col2, col3 = st.columns(3)
col1.metric("Current Patient Outcome", "CURED" if eliminated else "ESCAPE / DORMANT")
col2.metric("Peak Tumor Burden", f"{peak_tumor:.2e} cells")
col3.metric("Final Tumor Size", f"{final_tumor:.2e} cells")

# --- PLOTTING ---
fig, ax = plt.subplots(figsize=(12, 5))

# Control line
ax.plot(sol_tumor.t, sol_tumor.y[0], color='gray', linestyle=':', linewidth=2.5, alpha=0.7, label='Tumor (No Immune System)')

# Main lines
ax.plot(sol.t, sol.y[0], color='#e74c3c', linewidth=3, label='Tumor Cells')
ax.plot(sol.t, sol.y[1], color='#3498db', linestyle='--', linewidth=3, label='Immune Cells')

# Thresholds
ax.axhline(1e9, color='darkred', linestyle='--', alpha=0.4, label='Clinical Threshold ($10^9$)')
ax.axhline(1.0, color='forestgreen', linestyle='--', alpha=0.6, label='Elimination ($10^0$)')
ax.axhspan(1.0, 1e9, color='gold', alpha=0.05, label='Sub-clinical Zone')

ax.set_yscale('log')
ax.set_xlabel('Days', fontsize=12)
ax.set_ylabel('Cell Count', fontsize=12)
ax.legend(loc='center left', bbox_to_anchor=(1.02, 0.5))
plt.tight_layout()

# Render chart in Streamlit
st.pyplot(fig)