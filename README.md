# 📈 GNSS-Strain-Profile-Analysis-along-Transects

This repository contains the script **`Strain Profile Analysis along GPS Transects.py`**, a Python tool developed to analyze crustal deformation along tectonic transects using GPS datasets.  
The workflow is designed for applications in **active tectonics, fault kinematics, and seismic hazard analysis**.

---

## 🔎 Overview
The script computes **strain accumulation profiles** along user-defined transects based on GPS station displacements.  
It integrates **geospatial preprocessing, interpolation, and geophysical calculations** to quantify deformation across subduction zones and fault systems.

---

## ⚙️ Features
- Load GPS data from **CSV** or **shapefiles**.
- Define transects with start and end coordinates.
- Project station displacements onto transects.
- Compute:
  - Cumulative strain profiles.
  - Velocity gradients.
  - Convergence/extension rates.
- Output results as **plots** and **summary tables**.

---

## 📂 Input Data
- **GPS shapefiles** or CSV with:
  - Station ID
  - Latitude / Longitude
  - Horizontal displacement (E, N components)
  - Uncertainties (optional)

- **Transect definition**:
  - Start and end coordinates (lat/lon).
  - Transect width (optional).

---
## Output

<p align="center"> <img width="500" alt="GPS Strain Profile Example" src="https://github.com/user-attachments/assets/ed705d6e-1cff-4ace-9907-fb6e97a02cd0" /> </p>
## 🖥️ Usage
```bash
python3 "Strain Profile Analysis along GPS Transects.py"
