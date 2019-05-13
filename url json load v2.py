#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 16:41:18 2018

@author: caser
"""

#1 import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
#import urllib 
import requests

##check json content
#url_all_radios='http://www.radio-browser.info/webservice/json/stations' #define site for all radio stations
#response_all_radios = requests.get(url_all_radios) #check url
#cont = json.loads(response_all_radios.content) #download json content as a trial
#
##real download to df
#df_all_radios=pd.read_json(url_all_radios, orient='records')
#df_tag_list=pd.read_json('http://www.radio-browser.info/webservice/json/tags', orient='records')
#
##sort df2
#df_tag_list.sort_values(by=['stationcount'],ascending=False,na_position='last',inplace=True) 
#df_tag_list.reset_index(inplace=True,drop=True) #reset index
#
##save data for future use
#df_all_radios.to_csv('all_radios.csv')
#df_tag_list.to_csv('tags_list.csv')
df1=pd.read_csv('all_radios.csv')

#define genres
genre_list=['alternative rock', 'classic rock', 'indie rock', 'progressive rock', 'blues rock', 'classical', 'death metal', 'downtempo', 'dubstep', 'edm', 'metalcore', 'progressive rock', 'smooth jazz', 'news','business']

#create rating by combining clicks * votes
quantile_clickcount = df1['clickcount'].quantile(.8)
quantile_votes = df1['votes'].quantile(.8)
df1['rating'] = (df1['clickcount']/quantile_clickcount)  + (3*df1['votes']/quantile_votes)

#sort by rating
df1.sort_values(by=['rating'],ascending=False,na_position='last',inplace=True) #sort by rating
df1.reset_index(inplace=True,drop=True) #reset index

#def funct for tag filtering
def genre_filter(x):
    df_tag=df1.loc[df1['tags'].str.contains(x, na=False),['url','tags','name','rating','country','homepage','votes','clickcount']]
    df_tag.to_csv(str('Genre ' + x + '.csv'))
    return

#apply filter function to all genre list
for i in genre_list:
    genre_filter(i)


