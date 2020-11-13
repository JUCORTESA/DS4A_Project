![](https://teate.co/wp-content/themes/teatetheme/images/logo.png) ![](https://raw.githubusercontent.com/Mrjarkos/DS4A_Project/tree/main/assets/img/ds4A-logo.png?raw=true)


# Teaté Colombia S.A.S
## Demand Forecast Per Manufacture
This is the repository for the Data Science For All Final Project
## Instructions: 
First clone this repository:
```
git clone https://github.com/Mrjarkos/DS4A_Project.git
```
In order to run the app locally, you need to install all the Python libraries needed:

```
pip install -r requirements.txt
```
Finally run the application by running:
```
python3 index.py
```
### Business Problem
The neighborhood shops are one of the most important sales channels in Colombia for fast-moving consumer goods, representing more than 50% of the total sales. 
Moreover, four out of five Colombian households buy their basic foods from these types of stores due to their offer of low prices and convenient products. 
However, these small businesses are highly inefficientthese businesses and their suppliers need tools that allow them to achieve greater efficiency in their operations. 
One of such tools is to have an accurate sales forecast that can help both the neighborhood shops and the product manufacturers optimize their supply chains and provide the required products at the right moment. 
This would allow them to achieve greater service levels and minimize their losses.

## Code Structure

```
plotly-dash-multipage-template
│   index.py
|   app.py
|   data.py
|   auth.py
│
└───apps
│   │   About.py
|   |   Forecast.py
|   |   Geolocation.py
|   |   Home.py
|   |   Product.py
|   |   Store.py
|   |   Template.py
│   
└───models
    └───Geolocation
        └───geojson_data
|   |   |   |   Comunas_cali.geojson
|   |   |   |   Comunas_medellin.geojson
        └───Maps
|   |   |   |   Map.html
|   |   |   Store_Geo.csv
│   
└───scripts
│   │   utils.py
│   
└───assets
    └───css
    └───img
    └───js
```
### Application Overview
*FORECAST*  
![](https://raw.githubusercontent.com/Mrjarkos/DS4A_Project/tree/main/assets/img/forecast.png?raw=true)

*STORE ANALYSIS*  
![](https://raw.githubusercontent.com/Mrjarkos/DS4A_Project/tree/main/assets/img/store.png?raw=true)

*PRODUCT ANALYSIS*  
![](https://raw.githubusercontent.com/Mrjarkos/DS4A_Project/tree/main/assets/img/product.png?raw=true)
