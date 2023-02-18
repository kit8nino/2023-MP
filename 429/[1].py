# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

data = ("Voronin Michael Mikhailovich, 28 , 02, 2003") 
certificate = {
                "russian_language":4,
                "literature":5,
                "english_language":5,
                "algebra":4,
                "geometry":4,
                "informatics":5,
                "physics":5,
                "BPE":5,
                "biology":5,
                "chemistry":5,
                "ru_history":5,
                "general_history":5,
                "social_science":5,
                "geography":5,
                "fis_culture":5
                }
family_names = ["Oliver","Jack","homas","Jacob","Charley","Thomas","George","Jack","Jacob","Jack"]
kiwa_name = "crab(#12)"

#mean mark
sum_m=sum(certificate.values())
len_m=len(certificate)
avg_m=sum_m/len_m

#unique names
