# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:24:00 2022

@author: Ariki
"""
import orjson
import json
from bmi import BMI

if __name__=="__main__":
    f=open('bmi_data.json')
    bmi_collection=[]    
    data=json.load(f)
    for record in data:
        bmi_collection.append(BMI(record['Gender'],record['HeightCm']/100,record['WeightKg']))
    count=0
    for bmidetail in bmi_collection:
        print('Gender:{}, Height:{} m, Weight:{} kg, BMI:{}, Category:{}, Risk:{}'.format(bmidetail.gender,bmidetail.height,bmidetail.weight,bmidetail.bmi,bmidetail.category,bmidetail.risk))
        if bmidetail.category=='Overweight':
            count=count+1
    print('Total number of overweight persons {}'.format(count))

    f.close()
    
