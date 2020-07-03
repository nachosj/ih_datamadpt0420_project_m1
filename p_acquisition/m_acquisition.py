import pandas as pd
from sqlalchemy import create_engine
from datetime import date


list_countries= ['Austria','Belgium','Bulgaria','Croatia','Cyprus','Czechia','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Ireland','Italy','Latvia','Lithuania','Luxembourg','Malta','Netherlands','Poland','Portugal','Romania','Slovakia','Slovenia','Spain','Sweden','United Kingdom']


def validation_args(countryval):
    if countryval in list_countries:
        print(f'{countryval} is in the list')
    else:
        exit(f"{countryval} is not a valid country, try to use one of this list {list_countries}")



def get_main_table(path):
    print("getting the table with all the columns")
    engine = create_engine(f'{path}')
    df_raw = pd.read_sql_query(''' SELECT personal_info.uuid, age, gender, dem_has_children, age_group AS "Age Group", dem_education_level, dem_full_time_job, normalized_job_code as "Normalized Job Code", country_code as "Country code", rural, question_bbi_2016wave4_basicincome_awareness AS "question: BI awareness", question_bbi_2016wave4_basicincome_effect AS "question: BI effect",question_bbi_2016wave4_basicincome_argumentsfor AS "question: BI arguments for",question_bbi_2016wave4_basicincome_argumentsagainst AS "question: BI arguments against"
        FROM personal_info
        LEFT JOIN career_info ON personal_info.uuid = career_info.uuid
        LEFT JOIN country_info ON personal_info.uuid = country_info.uuid
        LEFT JOIN poll_info ON personal_info.uuid = poll_info.uuid
        ''', engine)
    print("saving a csv copy")
    df_raw.to_csv(f'data/raw/historical_data/{date.today()}-data.csv', index=False)
    selected_columns = ["uuid", "age", "Age Group", "gender", "Country code", "Normalized Job Code"]
    df_good = df_raw[selected_columns]
    print("creating the table with the selected columns")
    main_table = df_good
    return main_table











