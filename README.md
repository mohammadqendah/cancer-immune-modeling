# 🦠 Mathematical Modeling of Tumor-Immune Dynamics: A Melanoma Case Study

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![SciPy](https://img.shields.io/badge/SciPy-RK45-orange.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626.svg)

## 📌 Overview
This repository contains an in-silico mathematical model of the dynamic competition between a growing **Melanoma** tumor and the cell-mediated immune response. Built as a population dynamics problem, the simulation uses Ordinary Differential Equations (ODEs) to identify the specific biological thresholds where the immune system successfully clears a tumor versus where the tumor escapes immune control.

## 🔬 Mathematical Approach
* **Tumor Growth:** Modeled using **Gompertzian kinetics** to represent spatial and nutrient-limited carrying capacity.
* **Immune Predation:** Modeled using **Mass-Action kinetics** to simulate clonal expansion and cell-to-cell predation.
* **Numerical Solver:** Utilizes the **Runge-Kutta (RK45)** algorithm via `scipy.integrate.solve_ivp` to handle the highly non-linear interactions without the instability typical of Euler methods.
* **Dimensional Analysis:** Parameters adapted from de Pillis et al. (2005) were mathematically scaled from fractional normalizations to absolute raw cell counts to provide clinically tangible simulations.

## 📊 Key Scenarios Simulated
The `notebooks/tumor_immune_dynamics.ipynb` notebook acts as an in-silico clinical trial, testing 6 distinct hypotheses:
1. Baseline Immunoclearance (Healthy Patient)
2. Systemic Immunosuppression
3. Indolent/Slow-Growing Tumors
4. Late-Stage Diagnosis (Immune Exhaustion)
5. Immunotherapy Rescue (Boosting $k$)
6. Immune Evasion ("Cold" Tumors)

*(Optional: Add a screenshot of your Pandas table or your best chart here using `![Simulation Results](images/baseline_clearance.png)`)*

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone [https://github.com/YourUsername/tumor-immune-modeling.git](https://github.com/YourUsername/tumor-immune-modeling.git)
