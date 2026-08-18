# SpaceX Falcon 9 Data Science Capstone

Public submission repository for the IBM Applied Data Science Capstone.

**Repository URL:** https://github.com/phannguyenbinh-gif/spacex-data-science-capstone

## Completed project artifacts

| Area | File |
|---|---|
| API data collection | `1-Spacex-data-collection-api.ipynb` |
| Web scraping | `2-Webscraping.ipynb` |
| Data wrangling | `3-Spacex-Data-Wrangling.ipynb` |
| EDA with SQL | `4-EDA-with-SQL.ipynb` |
| EDA with visualization | `5-EDA-with-Visualization.ipynb` |
| Folium map | `6-Folium-Launch-Site-Location.ipynb` |
| Predictive classification | `7-SpaceX-Machine-Learning-Prediction.ipynb` |
| Plotly Dash | `spacex_dash_app.py` |
| Reusable Python | `src/` |
| Data | `data/` |
| Final presentation | `SpaceX_Capstone_Final_Presentation_UPDATED.pdf` |

## Project objective
Predict whether the Falcon 9 first stage lands successfully using launch, payload, orbit and site information. The workflow covers collection, wrangling, EDA, SQL, visualization, geospatial analysis, interactive dashboarding, classification and evaluation.

## Run
```bash
pip install -r requirements.txt
jupyter notebook
python spacex_dash_app.py
```

> The included CSV is a self-contained demonstration dataset so the repository can execute without depending on a live API. The notebooks also document the original API/web-scraping methodology.
