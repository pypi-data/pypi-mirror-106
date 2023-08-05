import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# set the sf account name
sf_account = 'ra45066.eu-west-1'
from toolkit_w.snowflake.snowflakeq import Snowflakeq
SQ = Snowflakeq()

from toolkit_w.tellme import Tellme
class Tellme:
    """ Module for internal analytics - different plots and exploratory data analysis"""

    def getAvgBorders(self, data, max_date, min_date):
        """    """

        data['Avg_Days_section'] = pd.cut(x=data['avg_days_between_purchases'],
                                        bins=[-1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 1000],
                                        labels=['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80',
                                                '80-90', '90+'])

        dat = data.groupby('Avg_Days_section').agg({'customerid':'count'})


        return dat








