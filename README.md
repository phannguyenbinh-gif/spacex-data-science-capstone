# SpaceX Falcon 9 First-Stage Landing Prediction

Data Science Capstone project demonstrating an end-to-end workflow for predicting Falcon 9 first-stage landing success.

## Project structure

- `notebooks/` — completed-style notebooks for API collection, web scraping, EDA/SQL, visualization, Folium, and machine learning.
- `src/` — reusable Python modules for data preparation and modeling.
- `dashboard/` — Plotly Dash application.
- `data/` — sample project data used by the included scripts/notebooks.
- `docs/` — project report.
- `requirements.txt` — Python dependencies.

## Workflow

1. Collect Falcon 9 launch data from API/web sources.
2. Clean and wrangle the data.
3. Perform exploratory analysis with Pandas/SQL and visualization.
4. Explore launch sites with Folium.
5. Build an interactive Plotly Dash dashboard.
6. Train and compare classification models.

## Coursework results documented in the report

- Falcon 9 records after removing Falcon 1: **90**
- CCAFS SLC 40 launches in the SQL exercise: **55**
- Geosynchronous-orbit launches in the SQL exercise: **1**
- Successful drone-ship landings in the SQL exercise: **41**
- Modeling test sample: **18 records**
- Decision Tree first-run test accuracy referenced in coursework: **83.33%**

> Note: Results can vary with dataset version, random split, and notebook execution. Run the notebooks to reproduce results from your environment.

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
jupyter notebook
```

To run the dashboard:

```bash
python dashboard/app.py
```

## Final report

See `docs/Data_Science_Capstone_Project_Report_REVISED.pdf`.

## GitHub submission

After creating a GitHub repository, push this entire folder and replace the GitHub URL placeholder in the PDF/report with your actual repository URL.
