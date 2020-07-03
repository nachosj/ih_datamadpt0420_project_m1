import pandas as pd
import requests
from bs4 import BeautifulSoup



def wrangle_main(maintable):
    print(f"cleaning the columns of the {maintable}")
    maintable["age"].replace('\s\w*\s\w*',"",regex=True, inplace = True)
    maintable["age"] = maintable["age"].apply(lambda x: 2016-int(x) if len(x)>2 else x)
    maintable['Normalized Job Code'].fillna('no_full_time_job',inplace=True)
    maintable["gender"].replace(to_replace= ['male','Fem','FeMale','female'], value = ['Male', 'Female','Female','Female'],inplace=True)
    maintable["Age Group"].replace(to_replace = ['juvenile'], value = ['14_25'],inplace=True)
    maintable["Age Group"].replace(to_replace = ['40_65', '26_39', '14_25'], value = ['40 to 65 years', '26 to 39 years', '14 to 25 years'],inplace=True)
    wr_main_table = maintable
    print(f"{maintable} is now cleaned and renamed as {wr_main_table}")
    return wr_main_table


URL = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
API_URL = 'http://api.dataatwork.org/v1/jobs/'


def scraping(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'lxml')
    countries = soup.find_all('td')
    print(f"scrapping this {url}")
    list_countries = list(filter(None,[i.text.strip().replace('\n','').replace('(','').replace(')','') for i in countries]))
    countries_refactored = [list_countries[x:x + 2] for x in range(0, len(list_countries), 2)]
    df_countries = pd.DataFrame(countries_refactored, columns=["Country", "Country code"])
    df_countries.replace(to_replace=["EL", "UK"], value=["GR", "GB"], inplace=True)
    print(f"creating a table with the countries and the country codes")
    df_countries.to_csv(f'data/raw/countries-to-remove.csv', index=False)
    return df_countries


def api_connection(apiurl,df):
    '''
    p = vlc.MediaPlayer("surprise/surprise.mp3")
    p.play()   # Where magic happens...
    print(f"connecting to this {apiurl}")
    unique_jobcodes = df["Normalized Job Code"].unique()[1:]
    job_names = [requests.get(f'{apiurl}' + job).json() for job in unique_jobcodes]
    df_jobnames = pd.DataFrame(job_names).rename(columns={'uuid': 'Normalized Job Code', 'title': 'Job Title'})
    print(f"the connection was successfully accomplished, now I will save a copy just in case...")
    df_jobnames.to_csv(f'data/raw/jobnames-to-remove.csv', index=False)
    p.stop()  # Where magic ends...
    '''
    df_jobnames = pd.read_csv('data/raw/jobnames-to-remove.csv')  # FAKE API CONNECTION
    return df_jobnames



def merge_tables(df1):
    df2 = scraping(URL)
    df3 = api_connection(API_URL,df1)
    df_first_merge=pd.merge(df1,df2,on="Country code",how="inner")
    df_merged=pd.merge(df_first_merge,df3,on="Normalized Job Code")
    print(f"merging the main table with the scraped data and the API data")
    return df_merged


