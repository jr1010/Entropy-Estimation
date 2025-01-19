# Estimating Distillable Entanglement in Bipartite Pure States

## Overview

This repository provides tools and resources for estimating the distillable entanglement in bipartite pure quantum states. Distillable entanglement quantifies the amount of pure entanglement that can be extracted from a quantum state using local operations and classical communication (LOCC).

## Contents

- **Bandits.ipynb**: A Jupyter Notebook exploring the application of multi-armed bandit algorithms in the context of entanglement estimation.
- **Distillable_Entanglement_Estimation.ipynb**: A Jupyter Notebook detailing methods and algorithms for estimating distillable entanglement in bipartite pure states.
- **Qubit-Qutrit.ipynb**: A Jupyter Notebook focusing on the estimation of distillable entanglement in qubit-qutrit systems.
- **utils.py**: A Python script containing utility functions to support the computations and visualizations in the notebooks.
- **requirements.txt**: A file listing the Python dependencies required to run the notebooks and scripts.

## Getting Started

To utilize the resources in this repository, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/jr1010/Entropy_Estimation.git
   cd Entropy_Estimation
   ```

2. **Set up a virtual environment** (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**:

   ```bash
   jupyter notebook
   ```

5. **Open and run the desired notebook**:

   Navigate to the notebook of interest (e.g., `Distillable_Entanglement_Estimation.ipynb`) and execute the cells to explore the content.

## Usage

Each notebook is designed to be self-explanatory, with code cells and accompanying descriptions. The `utils.py` script provides auxiliary functions that are imported and used within the notebooks.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For any questions or issues, please open an issue in this repository.
