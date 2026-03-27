## Personal Site

This repo holds the code that I use for my personal site. It is built with streamlit.

The goal of the site is to be a professional portfolio that showcases my projects and skills.

Streamlit is a python package that allows you to construct webapps entiarly with python. Streamlit community cloud allows you to host the app for free.

This project is built using:
- streamlit
- numpy
- pandas
- matplotlib
- plotly
- seaborn
- scikit-learn
- tensorflow
- keras

---

## Repo Structure
personal_site/
├── portfolio_app.py          # Main Streamlit app
├── requirements.txt          # Dependencies (for Streamlit Cloud)
├── assets/
│   ├── images/
│   │   ├── photo.jpg  # Your profile photo
│   │   └── images (maybe some of my photography)            
│   ├── reports/              # Project report PDFs
│   │   ├── cifar10_report.pdf
│   │   └── spark_report.pdf
│   ├── models/
│   │   └── # Any saved ML models
│   └── cv.pdf                # Downloadable CV
├── data/                     # Any small datasets for demos
└── README.md                 # Repo description (shows on GitHub)