# Data jobs Project README 

**by Nacho Sánchez Jurado**

![](surprise/gif_simpsons.gif)

## **Overview**

The main goal of this project was to try to understand how the data jobs are distributed in the European countries according to different variables as gender, age, etc. 

HOW? Creating a Python script  with the following requirements:

* Pandas
* SqlAlchemy
* Requests
* BeaufifulSoup
* MatplotLib



## **Data Sources**

The data come from 3 main sources:

- [an internal Database](http://www.potacho.com/files/ironhack/raw_data_project_m1.db): Connected through SqlAlchemy. You must download and you will need later indicate the path were it's located.
- [Open Skills Project API](http://dataatwork.org/data/): Using Requests library for Python
- [Eurostat website](https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes): Scrapped with BeautifulSoup

The dataset from the internal Database has to be cleaned up a with the intent of making it more appropriate and valuable 

## **Installation instructions**

```
conda install pandas
conda install sqlalchemy
conda install requests
conda install Matplotlib
pip instal BeaufifulSoup
```

## **Project Structure**
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── requeriments.txt
    ├── README.md
    ├── main_script.py  
    ├── p_acquisition
    │── p_analysis
    │── p_reporting
    │── p_wrangling
    └── data
        ├── raw
        ├── processed
        └── results
```


## **How to use it**
The main script is set up with two arguments:

- *path*: you need to provide the url where you have the internal database (it’s mandatory)

- *country*: you can specify this argument if you want to see the results for just one country, otherwise it's going to show the data of all the countries








