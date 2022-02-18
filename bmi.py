# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 18:21:16 2022

@author: Ariki
"""

class BMI:
    
    def __init__(self,g,h,w):
        self.gender=g
        self.height=h
        self.weight=w
        self.bmi=self.bmi_calculate(self.weight,self.height)
        self.category,self.risk=self.category_risk(self.bmi)
        
        
    def bmi_calculate(self,w,h):
        return round(w/(h**2),2)
    
    def category_risk(self,bmi):
        if bmi<18.4:
            return 'Underweight','Malnutrition risk'
        elif bmi>18.4 and bmi<=24.9:
            return 'Normal weight','Low Risk'
        elif bmi>24.9 and bmi<=29.9:
            return 'Overweight','Enhanced risk'
        elif bmi>29.9 and bmi<=34.9:
            return 'Moderately obese','Medium risk'
        elif bmi>34.9 and bmi<=39.9:
            return 'Very severely obese','Very high risk'