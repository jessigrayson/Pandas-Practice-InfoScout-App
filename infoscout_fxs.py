import pandas as pd
from functools import reduce

"""
#################################
Initially, I had read the file before listing the functions, but
that would have required changing the parameters on the given functions
like this:

    def retailer_affinity(focus_brand, df):
                                       ^^
So I read the csv file in each function so as to not alter the functions as assigned.

##################################
df = pd.read_csv('trips_gdrive.csv',
                 parse_dates=[1],
                 index_col=0,
                 converters={'Item Dollars': lambda s: float(s.replace('$', ''))},
                 infer_datetime_format=True)

df["Total"] = df['Item Dollars'] * df['Item Units']
# add column with total dollars based on number of units
##################################
"""


def retailer_affinity(focus_brand):
    """Returns name of retailer relative to other brands"""
    # Depending on the company, this docstring can become more or less specific such as
    # the datatype of the function's parameter is defined to be a string
    # or examples of input and output, etc.

    df = pd.read_csv('trips_gdrive.csv',
                     parse_dates=[1],
                     index_col=0,
                     converters={'Item Dollars': lambda s: float(s.replace('$', ''))},
                     infer_datetime_format=True)

    df["Total"] = df['Item Dollars'] * df['Item Units']
    # add column with total dollars based on number of units

    df = df.drop(columns=['User ID'])

    total_sales_by_retailer = df.groupby(df.Retailer).sum()

    df = df[df['Parent Brand'] == focus_brand]

    focus_brand_sales_by_retailer = df.groupby(df.Retailer).sum()

    focus_brand_sales_by_retailer['Percent of Sales'] = focus_brand_sales_by_retailer['Total'] / total_sales_by_retailer['Total']

    return focus_brand_sales_by_retailer['Percent of Sales'].idxmax()


def count_hhs(brand=None, retailer=None, start_date=None, end_date=None):
    """Returns number of households based on specified parameters"""

    df = pd.read_csv('trips_gdrive.csv',
                     parse_dates=[1],
                     index_col=0,
                     converters={'Item Dollars':
                                 lambda s: float(s.replace('$', ''))},
                     infer_datetime_format=True)

    mergelst = []

    if brand:
        b_df = df[df['Parent Brand'] == brand]
        mergelst.append(b_df)

    if retailer:
        r_df = df[df['Retailer'] == retailer]
        mergelst.append(r_df)

    if start_date:
        # start_date string recognized, inferred as datetime - no strtime needed
        # start_dt = datetime.strptime(start_date, '%Y-%M-%D')

        s_df = df[df['Date'] >= start_date]
        mergelst.append(s_df)

    if end_date:
        # end_date string recognized, inferred as datetime - no strptime needed
        # end_dt = datetime.strptime(end_date, '%Y-%m-%d')

        e_df = df[df['Date'] <= end_date]
        mergelst.append(e_df)

    if brand is None and retailer is None and start_date is None and end_date is None:

        return 0

    mrg = reduce(lambda left, right: pd.merge(left, right, how='inner'), mergelst)

    return mrg['User ID'].nunique()


def top_buying_brand():
    """Returns Parent Brand with top buying rate (dollars spend per household)"""

    df = pd.read_csv('trips_gdrive.csv',
                     parse_dates=[1],
                     index_col=0,
                     converters={'Item Dollars': lambda s: float(s.replace('$', ''))},
                     infer_datetime_format=True)

    df["Total"] = df['Item Dollars'] * df['Item Units']
    # add column with total dollars based on number of units

    brands = []

    for brand in df["Parent Brand"].unique():
        brands.append(brand)

    total_sales_by_brand = df.groupby('Parent Brand')["Total"].sum()

    total_sales_by_brand = df.groupby(['Parent Brand'])["Total"].sum()

    brand_buying_rates = []

    for item in brands:
        item_buying_rate = total_sales_by_brand[item]/count_hhs(brand=item)
        brand_buying_rates.append((item_buying_rate, item))

    # I believe that this function and for loops can be significantly optimized
    # (with more time) as I understand that there are many other features of
    # pandas that I am still in the process of learning. This solution is a
    # a bit clunky...

    return max(brand_buying_rates)[1]


def print_greeting():
    """Prints the Introductory Greeting"""

    print("Please select a report to run:")
    print("A: Retailer Affinity by Brand")
    print("B: Count of Households defined by: brand, retailer, start date, or end date")
    print("C: Top Buying Rate by brand")
    print("Q: Exit program")


def get_report():
    """R

    [month, day, year]
    """
    option = input(">> Report: ")

    if option == "A" or option == "B" or option == "C":
        if option == "A":
            focus_brand = input("Enter brand name (case/character sensitive): ")
            print("Strongest Retailer Affinity: {} \n".format(retailer_affinity(focus_brand)))

        elif option == "B":

            print("Please specify all or none of the following:")
            print("Brand  | Retailer | Start Date | End Date")

            brand = eval(input("Enter brand name (case/character sensitive) or type 'None': "))
            retailer = input("Enter retailer name (case/character sensitive) or type 'None': ")
            start_date = eval(input("Enter Start Date in YYYY-MM-DD format or type 'None': "))
            end_date = eval(input("Enter Start Date in YYYY-MM-DD format or type 'None': "))

            print("Number of Households: {}".format(count_hhs(brand, retailer, start_date, end_date)))

        elif option == "C":
            print("The brand with the top buying rate: {}".format(top_buying_brand()))

    if option == "Q":
        exit()


def ask_to_continue():
    """Ask user to continue"""

    playing = input("Would you like to run another report? Y/N: ")

    if playing == "N":
        return False

    return True


def run_program():
    """Runs program for InfoScout Exercise"""

    print_greeting()

    playing = True

    while playing:

        get_report()

        playing = ask_to_continue()

if __name__ == "__main__":
    run_program()
