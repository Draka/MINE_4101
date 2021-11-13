#!/usr/bin/env python
# coding: utf-8
import sys
import pickle

filename = 'derrumbe.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Ejemplos
# [7.0,2551.3591,7.0,12.0,0.209492,5.959947],
# [15.0,3435.0000,7.0,68.0,0.065119,8.412902],
# [16.0,2390.5293,7.0,12.0,0.223671,17.925686]


X_train = [float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5]),float(sys.argv[6])]
result = loaded_model.predict([X_train])
print(result[0] * 100)



