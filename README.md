# 🌱 CoalZero: Measuring Today, Planning Net-Zero
Data-driven platform to measure coal mine emissions and simulate pathways to carbon neutrality

## Overview
CoalZero is a web-based carbon footprint and carbon neutrality planning tool designed specifically for coal mining operations in India.

## Problem Statement
India's coal mining sector is critical for energy security but contributes significantly to greenhouse gas emissions. Mine operators need simple digital tools to:
- Quantify total carbon emissions
- Understand emission sources
- Evaluate mitigation strategies
- Plan realistic pathways toward carbon neutrality

## Solution
CoalZero provides:
- **Emission Estimation** from diesel, electricity, excavation, and transportation
- **Carbon Sink Calculation** from existing plantations
- **Gap Analysis** between emissions and absorption
- **Simulation-Based Planning** for neutrality pathways
- **Clear Data Visualization** for decision-making

## Technology Stack
- **Python 3.8+**
- **Streamlit** - Web application framework
- **Matplotlib** - Data visualization
- **NumPy** - Numerical computations
- **Pandas** - Data handling

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps
1. Clone the repository
```bash
git clone <repository-url>
cd CoalZero-AAAG
```

2. Install dependencies
```bash
pip3 install -r requirements.txt
```

3. Run the application
```bash
streamlit run app.py
```

4. Open browser at `http://localhost:8501`

## Project Structure
```
CoalZero-AAAG/
│
├── app.py                      # Main Streamlit application
├── utils/
│   ├── emission_factors.py    # Emission constants
│   ├── emissions.py            # Emission calculations
│   ├── sinks.py                # Carbon sink estimation
│   └── simulations.py          # Scenario simulations
├── visuals/
│   └── plots.py                # Matplotlib charts
├── requirements.txt
└── README.md
```

## Features

### 1. Emission Estimation
- Diesel combustion emissions
- Electricity consumption emissions
- Coal excavation emissions
- Transportation emissions
- Per-capita emission metrics

### 2. Carbon Sink Assessment
- Plantation area-based absorption
- Tree count-based absorption
- Total absorption capacity

### 3. Gap Analysis
- Emissions vs absorption comparison
- Carbon neutral status
- Land requirement calculation

### 4. Neutrality Pathways (Simulations)
- **Fleet Electrification:** Reduce diesel emissions
- **Renewable Energy:** Switch to solar/wind power
- **Afforestation:** Increase carbon sinks
- **Carbon Credits:** Cost estimation for offsetting

## Usage Guide

1. **Enter Operational Data** in the sidebar
2. **View Current Status** in the main dashboard
3. **Adjust Simulation Sliders** to explore strategies
4. **Compare Scenarios** to find optimal pathway
5. **Review Detailed Breakdown** for insights

## Emission Factors Used
- Diesel: 2.68 kg CO₂/litre
- Electricity (grid): 0.82 kg CO₂/kWh
- Coal excavation: 0.15 kg CO₂/tonne
- Transportation: 0.062 kg CO₂/tonne-km

## Carbon Absorption Rates
- Forest: 10,000 kg CO₂/hectare/year
- Tree: 22 kg CO₂/tree/year

## Team
- **Project Name:** CoalZero
- **Team Code:** AAAG
- **Hackathon:** Electrothon 24Hrs Hackathon organised by EEESOC, BIT Mesra

## License
This project is developed for educational and hackathon purposes.

## Contact
For queries, reach out to the project team (AAAG).



