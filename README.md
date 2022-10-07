# Introduction
The use of machine learning has increased significantly in the past few years. The utilization of machine learning to automate simple routine activities is one of the biggest accomplishments of machine learning. With the current long periods of shortage of water, the conservation of water is the need of the hour. The idea that in the future, everyone will have to grow their own food in their own backyards or gardens is not very surprising. The number of these ‘urban farmers’ is increasing every day. However, most residents and gardeners are not equipped with the knowledge regarding the healthy growth of any plant and end up over-watering or under-watering their house plants. Over-watering any plant can cause salt accumulation and loss of nutrients which cause the plant to ultimately wither or catch water-borne diseases. The proposed system addresses this problem with Wi-Fi communication and machine learning. A flowering plant called Vinca has been selected for the experimentation and system development procedures. The soil moisture values of the previous day are measured with the help of a soil-moisture sensor which is then transmitted wirelessly to a regression model used for the prediction of the water to be put in the plant on the current day. The model also takes the temperature and humidity values along with the soil moisture values and makes a prediction based on the three input values, called features. The prediction of the water amount is then sent to an automated watering system which waters the plant accordingly. This prediction system is suitable for most potted plants which are found in apartments and houses and can be used for the prediction of the correct amount of water so that water is preserved along with the health of the plant. It is a modern tool for any urban farmer. 

## Problem Statement
Plants need water, soil and nutrients to grow. Providing vinca plant less will result in death of the plant. Providing excess water will result in waterlogging and growth of algae which is not healthy for the plant. There is a need to provide the correct amount water for good health of the plant. Amount of water plant needs depends on soil moisture, atmospheric humidity, atmospheric temperature and few other factors. Considering these factors as input to our system, we have to design a system that gives the amount of water to be added in the plant that day. The system trains on a data sets and observes the trends on how these factors affect the water output and based on that it provides the value of water to be added.

## Block Diagram
<img width="476" alt="image" src="https://user-images.githubusercontent.com/32329699/194554970-8daa9ec3-c841-46c0-b7a6-fb46b1591d28.png">

## Installation
VS Code
Python
Flask
Node JS
Arduino IDE

Please clone the repository - https://github.com/zainabk1997/BE_Project and run the files to find the output on console

## Files

data_base.csv   - contains all the data manually collected over 4 months for the vinca plant - temperature, soil moisture, atmospheric humidity
backend.py      - contains code for all the data obtained from the soil moisture sensor and subsequent water required based on various regression o/p to the  watering system
linreg_cross.py - contains regression code for water o/p prediction using linear regression
knnreg.py       - contains code for k-nearest neighbours for water o/p prediction
svreg_cross.py  - contains code for support vector predictions
Mainscript.py   - contains consolidated code for all files involved from plotting to automated watering of the plant
plantcrudop     - contains frontend code in flask

## Troubleshooting
Please contact - khokawala.z@northeastern.edu

## Credits
Zainab Khokawala
1513088
