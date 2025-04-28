# 🌍 Air Quality Predictor V1.0
[](https://www.python.org/)
🔬 **Analyze, visualize, and forecast air pollution (PM2.5) trends using real-world data.**
## 📑 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Technologies](#technologies)
- [Contributing](#contributing)
- [License](#license)

## 🏷️ Overview
Air pollution impacts millions across the globe. This project leverages **real-time data** from the [WAQI API](https://waqi.info/) to analyze, visualize, and predict PM2.5 air quality metrics using modern data science practices.
## ✨ Features
- 📲 **Live Data Collection**: Fetches air quality data (PM2.5, temperature, humidity) for any city
- 🧹 **Data Cleaning**: Handles missing values & normalizes features for robust analysis
- 📊 **Exploratory Data Analysis**: Intuitive plots to identify trends, outliers & distributions
- 🤖 **Machine Learning Model**: Linear regression-based PM2.5 prediction
- 📝 **Model Evaluation**: Key performance metrics and visual inspection
- 💾 **Model Saving**: Export your trained model for reuse
- 📒 **Easy-to-Read Notebooks**: All analyses clearly documented in Jupyter Notebooks

## 🗂️ Project Structure
```bash
📁 air-quality-analysis/
├── data_collection.py     # Fetches and stores live air quality data (WAQI API)
├── data_cleaning.py       # Cleans and preprocesses collected data
├── train_model.py         # Trains the machine learning model
├── eda.ipynb              # Jupyter Notebook for Exploratory Data Analysis
├── outputFiles/           # Stores intermediate data (CSV), models (pkl)
└── README.md              # Project documentation (this file!)
```
## ⚙️ Prerequisites
- Python 3.12+
- Get your **WAQI API Key** [here](https://aqicn.org/data-platform/token/)
- Recommended: `pip` package manager

## 🚀 Installation
1. **Clone the repository:**
```bash
   git clone https://github.com/yourusername/air-quality-analysis.git
   cd air-quality-analysis
```
2. **Install dependencies:**
``` bash
   pip install -r requirements.txt
```
3. **Configure your WAQI API key in :`data_collection.py`**
``` python
   API_KEY = "your_api_key_here"
```
4. **Ensure an output directory exists (if not, create one):**
``` bash
   mkdir outputFiles
```
## 🏃 Usage
**Step 1:** Collect live air quality data
``` bash
python data_collection.py
```
**Step 2:** Clean and preprocess gathered data
``` bash
python data_cleaning.py
```
**Step 3:** Explore your dataset visually
``` bash
jupyter notebook eda.ipynb
```
**Step 4:** Train and evaluate the predictive model
``` bash
python train_model.py
```
## 📈 Visualizations
- **Distributions**: Histogram of PM2.5 levels
- **Trends**: PM2.5 over time
- **Correlations**: Scatter plots (PM2.5 vs temp & humidity)
- **Outlier Detection**: Boxplots
- **Model Performance**: Actual vs Predicted PM2.5 plot

Example: 
## 🛠️ Technologies
- **Python**: Data analysis & ML scripting
- [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/): Data manipulation
- [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/): Visualization
- [scikit-learn](https://scikit-learn.org/): Machine learning
- [Requests](https://docs.python-requests.org/): API data fetching
- [Jupyter Notebook](https://jupyter.org/): Exploratory data analysis

## 🤝 Contributing
We ❤️ contributions!
1. Fork the repository
2. Create your branch (`git checkout -b feature/something`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/something`)
5. Open a Pull Request

## 📜 License
[MIT License](./LICENSE)
