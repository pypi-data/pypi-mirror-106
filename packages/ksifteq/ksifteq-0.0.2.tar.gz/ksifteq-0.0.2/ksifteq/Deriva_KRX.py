"""
:Author: Meenmo Kang
:Date: 2021. 5. 21.
"""
import pandas as pd

from pymongo  import MongoClient
from datetime import datetime
from datetime import date, timedelta


class Data:
    def __init__(self, prod, start_date, end_date=None):
        self.df = None
        self.db = MongoClient("mongodb+srv://public:02455@cluster0.e4c3g.mongodb.net/KSIF?retryWrites=true&w=majority")['Deriva_KRX']
        self.prod = prod
        self.date = date
        self.date1 = datetime.strptime(start_date, "%Y%m%d")            
        self.date2 = datetime.strptime(end_date, "%Y%m%d") if end_date != None else self.date1
        self.data()

    def data(self):
        collection = self.db[self.prod]
        delta = timedelta(days=1)
        df = pd.DataFrame()
        while self.date1 <= self.date2:
            _date = datetime.strftime(self.date1, "%Y%m%d")
            query = list(collection.find({'_id':_date}))
            if query != []:
                for i, _class in enumerate(query[0]['class']):
                    _dict = {**_class['종목개요'], **_class['거래정보']}
                    del _dict['종목명']
                    _df   = pd.DataFrame(_dict, index=[self.date1])
                    df    = pd.concat([df, _df], axis=0)

            self.date1 += delta

        self.df = df