# 📈 GNSS-Strain-Profile-Analysis-along-Transects

This script performs **strain parameter analysis** (dilation, rotation, and maximum shear) along predefined GPS transects.  
It is designed to integrate results from **SSPX (Allmendinger et al.2009)** with geographic transects, allowing the visualization of how strain evolves along active tectonic profiles.  


---

## 🔎 Overview
Projects GPS strain results from SSPX onto user-defined transects (shapefiles).  
- Computes **cumulative distance along transects** (in kilometers).  
- Visualizes strain parameters as scatter plots with **polynomial trend lines**.  
- Facilitates **tectonic interpretation of crustal deformation** across subduction zones and fault systems.  

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
1. **Strain data (SSPX outputs)**  
   - Text files (`.txt`) exported from SSPX (Allmendinger).  
   - Contain point-based strain parameters: *dilation, rotation, maxShear*.  

2. **Transects (Shapefiles)**  
   - Linear features (`.shp`) representing transects or profiles.  
   - One transect = one profile line.  

Each GPS/strain point is automatically projected onto its closest transect. Its position is converted into **cumulative distance along the profile (km)** for analysis.


---
## Example Output

<p align="center"> <img width="500" alt="GPS Strain Profile Example" src="https://github.com/user-attachments/assets/ed705d6e-1cff-4ace-9907-fb6e97a02cd0" /> </p>
## 🖥️ Usage

Example of strain variation along a transect with polynomial fit.

## 🔬 Applications

Identifying strain gradients across active faults and subduction interfaces.

Linking GPS-derived strain fields to tectonic segmentation.

Comparing SSPX strain models with geologic/geomorphic features.

Supporting earthquake hazard assessments with deformation profiles.

##📜 Reference

Allmendinger, R. W., Cardozo, N., & Fisher, D. (2012). Structural Geology Algorithms: Vectors & Tensors.

SSPX software – widely used for structural analysis of strain parameters.

## 📜 License

This tool is released under the MIT License.
© 2025 Hernán Porras Espinoza.


