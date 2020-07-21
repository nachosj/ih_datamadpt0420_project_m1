import argparse
from p_acquisition import m_acquisition as mac
from p_wrangling import m_wrangling as mwr
from p_reporting import m_reporting as mre

def argument_parser():
    parser = argparse.ArgumentParser(description='Specify a path and url')
    parser.add_argument("-p", "--path", type=str, help="Specify a path and a file location", required=True, dest="path1")
    parser.add_argument("-c", "--country", type=str, help="Specify a country", dest="country1", default="")
    args = parser.parse_args()
    return args

def main(path,country):
    country_validation = mac.validation_args(country)
    database = mac.get_main_table(path)
    data_cleaned = mwr.wrangle_main(database)
    data_right= mwr.merge_tables(data_cleaned)
    data_output = mre.challenge1_final(data_right)
    data_top10 = mre.top10_topdf(data_output)
    data_country = mre.input_country(country,data_output)
    print(data_country.head())



if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments.path1,arguments.country1)



