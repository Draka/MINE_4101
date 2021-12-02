#!/usr/bin/env python
# coding: utf-8
import sys
import pickle

filename = 'derrumbe_final.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Ejemplos
# [7.0,2551.3591,7.0,12.0,0.209492,5.959947],
# [15.0,3435.0000,7.0,68.0,0.065119,8.412902],
# [16.0,2390.5293,7.0,12.0,0.223671,17.925686]
# Distancia_Fallas;DTM;Slope;TPI;Rugosidad;Distancia_Fallas DTM;Distancia_Fallas NDVI;Distancia_Fallas TPI;Distancia_Fallas Rugosidad;Distancia_Vias^2;Distancia_Vias DTM;Distancia_Vias NDVI;Distancia_Vias TPI;DTM^2;DTM TPI;NDVI^2;NDVI Slope;Slope^2;Cob_13;Cob_8;Cob_12;Geol_5;Geol_2;Geom_27;UGS_4
# 0 3.6286209 -1.2752151 -0.8258867 1.0126883 2.0018942 -4.627272 2.8179684 3.6746619 7.2641153 0.30656675 0.70606714 -0.4299887 -0.56071 1.6261737 -1.2913954 0.6030996 -0.6413794 0.6820889 0 0 0 0 0 0 1
# 1 3.6241398 -1.2663954 -0.792244 1.178476 2.0018942 -4.5895944 2.8144884 4.2709618 7.2551446 0.3113051 0.70658183 -0.43329895 -0.6575274 1.6037574 -1.4924166 0.6030996 -0.6152527 0.62765056 0 0 0 0 0 0 1
# 2 3.619664 -1.2642161 -1.1156818 1.1866806 2.0018942 -4.5760374 2.8657699 4.295385 7.2461843 0.31607985 0.71075463 -0.44511423 -0.66716343 1.5982423 -1.5002207 0.62682474 -0.88331056 1.2447459 0 0 0 0 0 0 1
# 3 3.632452 -1.2880936 -0.17128628 0.8119943 2.0018942 -4.678938 2.8094773 2.9495304 7.271785 0.29673904 0.701673 -0.4213209 -0.4423238 1.659185 -1.0459247 0.59820676 -0.13247937 0.029338991 0 0 0 0 0 0 1
# 4 3.627955 -1.2813088 -0.05523705 0.9100577 2.0018942 -4.6485305 2.8059993 3.3016484 7.262782 0.3012884 0.7033071 -0.42453828 -0.49952835 1.6417521 -1.166065 0.59820676 -0.04272245 0.0030511317 0 0 0 0 0 0 1
# 5 3.6234643 -1.2747239 -0.14824453 1.01918 2.0018942 -4.6189165 2.813964 3.6929626 7.2537923 0.30580127 0.7049134 -0.42945153 -0.56359947 1.624921 -1.2991731 0.6030996 -0.11512594 0.021976441 0 0 0 0 0 0 1

# 3.6286209 -1.2752151 -0.8258867 1.0126883 2.0018942 -4.627272 2.8179684 3.6746619 7.2641153 0.30656675 0.70606714 -0.4299887 -0.56071 1.6261737 -1.2913954 0.6030996 -0.6413794 0.6820889 0 0 0 0 0 0 1

#print(sys.argv)

X_train = [
  float(sys.argv[1]),
  float(sys.argv[2]),
  float(sys.argv[3]),
  float(sys.argv[4]),
  float(sys.argv[5]),
  float(sys.argv[6]),
  float(sys.argv[7]),
  float(sys.argv[8]),
  float(sys.argv[9]),
  float(sys.argv[10]),
  float(sys.argv[11]),
  float(sys.argv[12]),
  float(sys.argv[13]),
  float(sys.argv[14]),
  float(sys.argv[15]),
  float(sys.argv[16]),
  float(sys.argv[17]),
  float(sys.argv[18]),
  0,
  0,
  0,
  0,
  0,
  0,
  1
  ]
result = loaded_model.predict([X_train])
print(result[0] * 100)



