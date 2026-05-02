# 🦠 Mathematical Modeling of Tumor-Immune Dynamics: A Melanoma Case Study

## 📌 Overview
This repository contains an *in-silico* mathematical model of the dynamic competition between a growing Melanoma tumor and the cell-mediated immune response. Built as a population dynamics problem, the simulation uses Ordinary Differential Equations (ODEs) to identify the specific biological thresholds where the immune system successfully clears a tumor versus where the tumor escapes immune control.

Alongside the core computational notebook, this project features a **Live Interactive Dashboard** built with Streamlit, allowing users to dynamically adjust biological parameters (like tumor growth rate and immune exhaustion limits) to see real-time clinical outcomes.

## 🔬 Mathematical Approach
* **Tumor Growth:** Modeled using Gompertzian kinetics to represent spatial and nutrient-limited carrying capacity.
* **Immune Predation:** Modeled using Mass-Action kinetics to simulate clonal expansion and cell-to-cell predation, modified with Michaelis-Menten saturation to simulate T-cell exhaustion.
* **Numerical Solver:** Utilizes the Runge-Kutta (RK45) algorithm via `scipy.integrate.solve_ivp` to handle highly non-linear interactions without the compounding instability typical of Euler methods.
* **Dimensional Analysis:** Parameters adapted from de Pillis et al. (2005) were mathematically scaled from fractional normalizations to absolute raw cell counts to provide clinically tangible simulations.

## 📊 Key Scenarios Simulated
The `notebooks/Modeling Project.ipynb` notebook and the `app.py` dashboard act as an *in-silico* clinical trial, testing 6 distinct hypotheses:
1. Baseline Immunoclearance (Healthy Patient)
2. Systemic Immunosuppression
3. Indolent/Slow-Growing Tumors
4. Late-Stage Diagnosis (Immune Exhaustion)
5. Immunotherapy Rescue (Boosting Kill Rate)
6. Immune Evasion ("Cold" Tumors)

## 🚀 How to Run Locally

**1. Clone the repository:**
```bash
git clone [https://github.com/mohammadqendah/cancer-immune-modeling.git](https://github.com/mohammadqendah/cancer-immune-modeling.git)
cd cancer-immune-modeling

2. Install required libraries:
pip install -r requirements.txt

3. Launch the Interactive Dashboard:
streamlit run app.py
