# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:14:54 2022

@author: HP
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


cultivated_area_in_ha_season_A_20 = pd.read_csv('D:\\DATA\\Admin_boundaries-2012\\Agriculture_data\\2020\\Season_A_Cultivated_Area_by_crop_type_per_district_in_ha_2020.csv')
cultivated_area_in_ha_season_B_20 = pd.read_csv('D:\\DATA\\Admin_boundaries-2012\\Agriculture_data\\2020\\Season_B_Cultivated_Area_by_crop_type_per_district_in_ha_2020.csv')
cultivated_area_in_ha_season_C_20 = pd.read_csv('D:\\DATA\\Admin_boundaries-2012\\Agriculture_data\\2020\\Season_C_Cultivated_Area_by_crop_type_per_district_in_ha_2020.csv')

Harvested_area_in_ha_season_A_20 = pd.read_csv('D:\\DATA\\Admin_boundaries-2012\\Agriculture_data\\2020\\Season_A_Harvested_Area_by_crop_type_per_district_in_ha_2020.csv')
Harvested_area_in_ha_season_B_20 = pd.read_csv('D:\\DATA\\Admin_boundaries-2012\\Agriculture_data\\2020\\Season_B_Harvested_Area_by_crop_type_per_district_in_ha_2020.csv')
Harvested_area_in_ha_season_C_20 = pd.read_csv('D:\\DATA\\Admin_boundaries-2012\\Agriculture_data\\2020\\Season_C_Harvested_Area_by_crop_type_per_district_in_ha_2020.csv')

#Cultivated_Areas_Season_A_2020_in_ha = cultivated_area_in_ha_season_A_20.set_index(' District ') 
cultivated_area_season_A = cultivated_area_in_ha_season_A_20.rename(columns={" District ":"District", "Total developped land": "Developped land"})
#Renaming the column name to District so that it may take the same format as cultivated area. for Season A
dropping_some_columns = Harvested_area_in_ha_season_A_20.drop(columns = ['Cereals ','Tubers and Roots', 'Legumes and Pulses','Vegetables and Fruits'])
#renamed_column_in_Harvested_Area_Season_A_20 = dropping_some_columns.set_index('District name')
Harvested_area_season_A = dropping_some_columns.rename(columns={"District name": "District","vegetables":"Vegetables","Fodder crops":"Fodder Crops"})
"""
Changing the data types of Cultivated area season A from object to integer.
"""
cultivated_area_season_A['Sorghum'].astype(int)
cultivated_area_season_A['Paddy rice'].astype(int)
cultivated_area_season_A['Wheat'].astype(int)
cultivated_area_season_A['Other cereals'].astype(int)
cultivated_area_season_A['Cassava'].astype(int)
cultivated_area_season_A['Sweet potato'].astype(int)
cultivated_area_season_A['Irish potato'].astype(int)
cultivated_area_season_A['Yarms & Taro'].astype(int)
cultivated_area_season_A['Bananas'].astype(int)
cultivated_area_season_A['Cooking banana'].astype(int)
cultivated_area_season_A['Dessert banana'].astype(int)
cultivated_area_season_A['Banana for beer'].astype(int)
cultivated_area_season_A['Beans'].astype(int)
cultivated_area_season_A['Bush bean'].astype(int)
cultivated_area_season_A['Climbing bean'].astype(int)
cultivated_area_season_A['Pea'].astype(int)
cultivated_area_season_A['Groundnut'].astype(int)
cultivated_area_season_A['Soybean'].astype(int)
cultivated_area_season_A['Vegetables'].astype(int)
cultivated_area_season_A['Fruits'].astype(int)
cultivated_area_season_A['Fodder Crops'].astype(int)
cultivated_area_season_A['Other crops'].astype(int)
cultivated_area_season_A['Developped land'].astype(int)

#Trying to plot
#fig, ax = plt.subplots(figsize=(15,6))
#compare_axis = ax.bar(cultivated_area_season_A['District'], cultivated_area_season_A['Sorghum'],width=0.9, bottom=None,color='Brown')
#ax.set_xlabel('Districts', color='Brown')
#ax.set_ylabel('Cultivated Area in ha')
#ax.set_title('Cultivated Area in Season A for Sorghum')
#ax.annotate(cultivated_area_season_A['Sorghum'])
#labels = ax.get_xticklabels()
#plt.setp(labels, rotation=45, color='red', horizontalalignment='right')
#ax.legend()

"""
Changing the data types of harvested area season A from object to integer.
"""
Harvested_area_season_A['Sorghum'].astype(int)
Harvested_area_season_A['Paddy rice'].astype(int)
Harvested_area_season_A['Wheat'].astype(int)
Harvested_area_season_A['Other cereals'].astype(int)
Harvested_area_season_A['Cassava'].astype(int)
Harvested_area_season_A['Sweet potato'].astype(int)
Harvested_area_season_A['Irish potato'].astype(int)
Harvested_area_season_A['Yarms & Taro'].astype(int)
Harvested_area_season_A['Bananas'].astype(int)
Harvested_area_season_A['Cooking banana'].astype(int)
Harvested_area_season_A['Dessert banana'].astype(int)
Harvested_area_season_A['Banana for beer'].astype(int)
Harvested_area_season_A['Beans'].astype(int)
Harvested_area_season_A['Bush bean'].astype(int)
Harvested_area_season_A['Climbing bean'].astype(int)
Harvested_area_season_A['Pea'].astype(int)
Harvested_area_season_A['Groundnut'].astype(int)
Harvested_area_season_A['Soybean'].astype(int)
Harvested_area_season_A['Vegetables'].astype(int)
Harvested_area_season_A['Fruits'].astype(int)
Harvested_area_season_A['Fodder Crops'].astype(int)
Harvested_area_season_A['Other crops'].astype(int)
Harvested_area_season_A['Developped land'].astype(int)

#Trying another plot
labels = cultivated_area_season_A['District']
cultivated = cultivated_area_season_A['Sorghum']
harvested = Harvested_area_season_A['Sorghum']

x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars


fig, ax = plt.subplots(figsize=(25,13))
rects1 = ax.bar(x- width/2, cultivated, width, label='Cultivated Area in Ha')
rects2 = ax.bar(x+ width/2, harvested, width, label='Harvested Area in Ha')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cultivated Area in Ha')
ax.set_title('Cultivated Area in Season A for Sorghum')
ax.set_xticks(x, labels,rotation=45, color='red', horizontalalignment='right')
ax.legend()

ax.bar_label(rects1, padding=3,rotation=90)
ax.bar_label(rects2, padding=3, rotation=90)

#fig.tight_layout()

plt.show()

"""
Comparing cultivated area with the harvested area in season A, 2020
"""
compare_A = cultivated_area_season_A.compare(Harvested_area_season_A, align_axis=1, keep_shape=True, keep_equal=True)
#plot_result = compare_A.plot()
#set_index_compare_A = compare_A.set_index('District')

"""
#Comparing crops from cultivated to harvested in season A
"""
comparing_sorghum_2020 = cultivated_area_season_A['Sorghum'].compare(Harvested_area_season_A['Sorghum'])
comparing_paddy_rice_2020 = cultivated_area_season_A['Paddy rice'].compare(Harvested_area_season_A['Paddy rice'])
comparing_Wheat_2020 = cultivated_area_season_A['Wheat'].compare(Harvested_area_season_A['Wheat'])
comparing_Other_cereals_2020 = cultivated_area_season_A['Other cereals'].compare(Harvested_area_season_A['Other cereals'])
comparing_Sweet_potato_2020 = cultivated_area_season_A['Sweet potato'].compare(Harvested_area_season_A['Sweet potato'])
comparing_Irish_potato_2020 = cultivated_area_season_A['Irish potato'].compare(Harvested_area_season_A['Irish potato'])
comparing_Yarms_and_Taro_2020 = cultivated_area_season_A['Yarms & Taro'].compare(Harvested_area_season_A['Yarms & Taro'])
comparing_Bananas_2020 = cultivated_area_season_A['Bananas'].compare(Harvested_area_season_A['Bananas'])
comparing_Cooking_banana_2020 = cultivated_area_season_A['Cooking banana'].compare(Harvested_area_season_A['Cooking banana'])
comparing_Dessert_banana_2020 = cultivated_area_season_A['Dessert banana'].compare(Harvested_area_season_A['Dessert banana'])
comparing_Banana_for_beer_2020 = cultivated_area_season_A['Banana for beer'].compare(Harvested_area_season_A['Banana for beer'])
comparing_Beans_2020 = cultivated_area_season_A['Beans'].compare(Harvested_area_season_A['Beans'])
comparing_Bush_bean_2020 = cultivated_area_season_A['Bush bean'].compare(Harvested_area_season_A['Bush bean'])
comparing_Climbing_bean_2020 = cultivated_area_season_A['Climbing bean'].compare(Harvested_area_season_A['Climbing bean'])
comparing_Pea_2020 = cultivated_area_season_A['Pea'].compare(Harvested_area_season_A['Pea'])
comparing_Groundnut_2020 = cultivated_area_season_A['Groundnut'].compare(Harvested_area_season_A['Groundnut'])
comparing_Soybean_2020 = cultivated_area_season_A['Soybean'].compare(Harvested_area_season_A['Soybean'])
comparing_vegetables_2020 = cultivated_area_season_A['Vegetables'].compare(Harvested_area_season_A['Vegetables'])
comparing_Fruits_2020 = cultivated_area_season_A['Fruits'].compare(Harvested_area_season_A['Fruits'])
comparing_Fodder_crops_2020 = cultivated_area_season_A['Fodder Crops'].compare(Harvested_area_season_A['Fodder Crops'])
comparing_Other_crops_2020 = cultivated_area_season_A['Other crops'].compare(Harvested_area_season_A['Other crops'])
comparing_Developped_land_2020 = cultivated_area_season_A['Developped land'].compare(Harvested_area_season_A['Developped land'])


"""
Making adjustments on data of cultivated area season B
"""
renaming_columns_cultivated_area_in_ha_season_B_2020 = cultivated_area_in_ha_season_B_20.rename(columns={" District ":"District","Taro & Yams":"Yarms & Taro","for beer":"Banana for beer","Fodder Crops":"Fodder crops","Vegetables":"vegetables","Total developped land":"Developped land"})

"""
Renaming the unnamed column in harvested area season B to have same format with the cultivated area season B
"""
renamed_column_in_Harvested_Area_Season_B_20 = Harvested_area_in_ha_season_B_20.rename(columns={"Unnamed: 0": "District"})

"""
Dropping some columns in the harvested file in order to polish and have same format with the cultivated. Season B
"""
Dropping_columns_in_harvested_Areas_Season_B_20= renamed_column_in_Harvested_Area_Season_B_20.drop(columns = ['Bananas','Beans'])

"""
Change data types for bush bean and pea from rultivated area season B
"""
renaming_columns_cultivated_area_in_ha_season_B_2020['Bush bean'].astype(int)
renaming_columns_cultivated_area_in_ha_season_B_2020['Pea'].astype(int)

"""
Comparing cultivated area with the harvested area in season B, 2020
"""
#compare_B = renaming_columns_cultivated_area_in_ha_season_B_2020.compare(Dropping_columns_in_harvested_Areas_Season_B_20, align_axis=1, keep_shape=True, keep_equal=True)
#set_index_compare_B = compare_B.set_index('District')

"""
Comparing crops from cultivated to harvested in season B
"""
comparing_sorghum_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Sorghum'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Sorghum'])
comparing_paddy_rice_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Paddy rice'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Paddy rice'])
comparing_Wheat_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Wheat'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Wheat'])
comparing_Other_cereals_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Other cereals'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Other cereals'])
comparing_Sweet_potato_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Sweet potato'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Sweet potato'])
comparing_Irish_potato_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Irish potato'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Irish potato'])
comparing_Yarms_and_Taro_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Yarms & Taro'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Yarms & Taro'])
#comparing_Bananas_2020 = renaming_columns_cultivated_area_in_ha_season_B_2020['Bananas'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Bananas'])
comparing_Cooking_banana_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Cooking banana'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Cooking banana'])
comparing_Dessert_banana_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Dessert banana'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Dessert banana'])
comparing_Banana_for_beer_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Banana for beer'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Banana for beer'])
#comparing_Beans_2020 = renaming_columns_cultivated_area_in_ha_season_B_2020['Beans'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Beans'])
comparing_Bush_bean_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Bush bean'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Bush bean'])
comparing_Climbing_bean_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Climbing bean'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Climbing bean'])
comparing_Pea_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Pea'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Pea'])
comparing_Groundnut_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Groundnut'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Groundnut'])
comparing_Soybean_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Soybean'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Soybean'])
comparing_vegetables_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['vegetables'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['vegetables'])
comparing_Fruits_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Fruits'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Fruits'])
comparing_Fodder_crops_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Fodder crops'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Fodder crops'])
comparing_Other_crops_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Other crops'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Other crops'])
comparing_Developped_land_2020_B = renaming_columns_cultivated_area_in_ha_season_B_2020['Developped land'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Developped land'])


#Trying another plot
labels = cultivated_area_season_A['District']
cultivated = renaming_columns_cultivated_area_in_ha_season_B_2020['Sorghum']
harvested = Dropping_columns_in_harvested_Areas_Season_B_20['Sorghum']

x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars


fig, ax = plt.subplots(figsize=(24,14.3))
rects1 = ax.bar(x- width/2, cultivated, width, label='Cultivated Area in Ha')
rects2 = ax.bar(x+ width/2, harvested, width, label='Harvested Area in Ha')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cultivated Area in Ha')
ax.set_title('Cultivated Area in Season A for Sorghum')
ax.set_xticks(x, labels,rotation=45, color='red', horizontalalignment='right')
ax.legend()

ax.bar_label(rects1, padding=3,rotation=90)
ax.bar_label(rects2, padding=3, rotation=90)

#fig.tight_layout()

plt.show()
"""
Renaming one column for both cultivated area and harvested area in season C to have the meaning.
"""
renamed_column_in_cultivated_Area_Season_C_20 = cultivated_area_in_ha_season_C_20.rename(columns={"District/Crop": "District"})
renamed_column_in_Harvested_Area_Season_C_20 = Harvested_area_in_ha_season_C_20.rename(columns={"District/Crop": "District"})

"""
Changing the data types of Cultivated area season C from object to integer.
"""
renamed_column_in_cultivated_Area_Season_C_20['Sweet potato'].astype(int)
renamed_column_in_cultivated_Area_Season_C_20['Irish potato'].astype(int)
renamed_column_in_cultivated_Area_Season_C_20['Yarms & Taro'].astype(int)
renamed_column_in_cultivated_Area_Season_C_20['Beans'].astype(int)
renamed_column_in_cultivated_Area_Season_C_20['Bush bean'].astype(int)
renamed_column_in_cultivated_Area_Season_C_20['Climbing bean'].astype(int)
renamed_column_in_cultivated_Area_Season_C_20['Pea'].astype(int)
renamed_column_in_cultivated_Area_Season_C_20['Soybean'].astype(int)
renamed_column_in_cultivated_Area_Season_C_20['vegetables'].astype(int)
renamed_column_in_cultivated_Area_Season_C_20['Developed land'].astype(int)

"""
Changing the data types of harvested area season C from object to integer.
"""

renamed_column_in_Harvested_Area_Season_C_20['Sweet potato'].astype(int)
renamed_column_in_Harvested_Area_Season_C_20['Irish potato'].astype(int)
renamed_column_in_Harvested_Area_Season_C_20['Yarms & Taro'].astype(int)
renamed_column_in_Harvested_Area_Season_C_20['Beans'].astype(int)
renamed_column_in_Harvested_Area_Season_C_20['Bush bean'].astype(int)
renamed_column_in_Harvested_Area_Season_C_20['Climbing bean'].astype(int)
renamed_column_in_Harvested_Area_Season_C_20['Pea'].astype(int)
renamed_column_in_Harvested_Area_Season_C_20['Soybean'].astype(int)
renamed_column_in_Harvested_Area_Season_C_20['vegetables'].astype(int)
renamed_column_in_Harvested_Area_Season_C_20['Developed land'].astype(int)

"""
Comparing cultivated area with the harvested area in season C, 2020
"""

#compare_C = renamed_column_in_cultivated_Area_Season_C_20.compare(renamed_column_in_Harvested_Area_Season_C_20, align_axis=1, keep_shape=True, keep_equal=True)
#set_index_compare_C = compare_C.set_index('District')

#Comparing crops from cultivated to harvested in season C
#comparing_sorghum_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Sorghum'].compare(renamed_column_in_Harvested_Area_Season_C_20['Sorghum'])
#comparing_paddy_rice_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Paddy rice'].compare(renamed_column_in_Harvested_Area_Season_C_20['Paddy rice'])
#comparing_Wheat_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Wheat'].compare(renamed_column_in_Harvested_Area_Season_C_20['Wheat'])
#comparing_Other_cereals_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Other cereals'].compare(renamed_column_in_Harvested_Area_Season_C_20['Other cereals'])
comparing_Sweet_potato_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Sweet potato'].compare(renamed_column_in_Harvested_Area_Season_C_20['Sweet potato'])
comparing_Irish_potato_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Irish potato'].compare(renamed_column_in_Harvested_Area_Season_C_20['Irish potato'])
comparing_Yarms_and_Taro_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Yarms & Taro'].compare(renamed_column_in_Harvested_Area_Season_C_20['Yarms & Taro'])
#comparing_Bananas_2020 = renaming_columns_cultivated_area_in_ha_season_B_2020['Bananas'].compare(Dropping_columns_in_harvested_Areas_Season_B_20['Bananas'])
#comparing_Cooking_banana_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Cooking banana'].compare(renamed_column_in_Harvested_Area_Season_C_20['Cooking banana'])
#comparing_Dessert_banana_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Dessert banana'].compare(renamed_column_in_Harvested_Area_Season_C_20['Dessert banana'])
#comparing_Banana_for_beer_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Banana for beer'].compare(renamed_column_in_Harvested_Area_Season_C_20['Banana for beer'])
comparing_Beans_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Beans'].compare(renamed_column_in_Harvested_Area_Season_C_20['Beans'])
comparing_Bush_bean_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Bush bean'].compare(renamed_column_in_Harvested_Area_Season_C_20['Bush bean'])
comparing_Climbing_bean_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Climbing bean'].compare(renamed_column_in_Harvested_Area_Season_C_20['Climbing bean'])
comparing_Pea_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Pea'].compare(renamed_column_in_Harvested_Area_Season_C_20['Pea'])
#comparing_Groundnut_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Groundnut'].compare(renamed_column_in_Harvested_Area_Season_C_20['Groundnut'])
comparing_Soybean_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Soybean'].compare(renamed_column_in_Harvested_Area_Season_C_20['Soybean'])
comparing_vegetables_2020_C = renamed_column_in_cultivated_Area_Season_C_20['vegetables'].compare(renamed_column_in_Harvested_Area_Season_C_20['vegetables'])
#comparing_Fruits_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Fruits'].compare(renamed_column_in_Harvested_Area_Season_C_20['Fruits'])
#comparing_Fodder_crops_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Fodder crops'].compare(renamed_column_in_Harvested_Area_Season_C_20['Fodder crops'])
#comparing_Other_crops_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Other crops'].compare(renamed_column_in_Harvested_Area_Season_C_20['Other crops'])
comparing_Developped_land_2020_C = renamed_column_in_cultivated_Area_Season_C_20['Developed land'].compare(renamed_column_in_Harvested_Area_Season_C_20['Developed land'])

#Trying another plot
labels = cultivated_area_season_A['District']
cultivated = renamed_column_in_cultivated_Area_Season_C_20['Sweet potato']
harvested = renamed_column_in_Harvested_Area_Season_C_20['Sweet potato']

x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars


fig, ax = plt.subplots(figsize=(24,14.3))
rects1 = ax.bar(x- width/2, cultivated, width, label='Cultivated Area in Ha')
rects2 = ax.bar(x+ width/2, harvested, width, label='Harvested Area in Ha')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Cultivated Area in Ha')
ax.set_title('Cultivated Area in Season A for Sorghum')
ax.set_xticks(x, labels,rotation=45, color='red', horizontalalignment='right')
ax.legend()

ax.bar_label(rects1, padding=3,rotation=90)
ax.bar_label(rects2, padding=3, rotation=90)

#fig.tight_layout()

plt.show()
