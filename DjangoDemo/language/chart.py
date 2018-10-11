#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Gaivin Wang 
@license: Apache Licence  
@contact: gaivin@outlook.com
@site:  
@software: PyCharm 
@file: chart.py 
@time: 10/10/2018 4:14 PM 
"""

from pyecharts import Bar, Line, WordCloud
import pandas as pd
import random, os.path as path

DATA_PATH = path.join(path.dirname(__file__), "data")


def history_chart():
    BOTTOM = 1
    TOP = 200
    XAXIS_COUNT = 10
    XAXIS_INTERVAL = ((TOP - BOTTOM) // XAXIS_COUNT) - 1
    chart = Line(title="Python History Ratings", subtitle="Source: www.tiobe.com",
                 title_color="DarkSlateGray", background_color="Azure",
                 width=1000, height=500, page_title="Python Ratings History")

    chart.use_theme('walden')

    df = pd.read_csv(path.join(DATA_PATH, "pythonratehistory.csv"), sep=",")
    TOP = len(df.Python)
    values = list(df.Python[BOTTOM:TOP])
    title = list(df.Date[BOTTOM:TOP])
    chart.add(name="Rating", x_axis=title, y_axis=values, yaxis_name="Rating (%)",
              xaxis_name="Date",
              # xaxis_interval=XAXIS_INTERVAL,
              # is_label_show=True,
              # label_formatter="{a}%",
              is_legend_show=False,
              is_smooth=True,
              is_symbol_show=False,
              line_width=4,
              mark_point=['max'],
              mark_point_symbolsize=60,
              mark_line=["max", "min"],
              is_datazoom_show=True,
              is_visualmap=True,
              visual_range=[0, 8])
    return chart


def language_rank_chart():
    TOP = 10
    AXIS_LABEL_TEXT_COLOR = "BLACK"
    bar = Bar(title="Program Language Ratings for September 2018", subtitle="Source: www.tiobe.com",
              title_color="DarkSlateGray", background_color="Azure", width=1000, height=500,
              page_title="Program Language Ratings"
              )

    # bar.use_theme('walden')
    df = pd.read_csv(path.join(DATA_PATH, "program_language_rank.csv"), sep=",", usecols=[2, 3])
    values = [float(x.replace("%", "")) for x in df.Ratings[0:TOP]]
    title = list(df.ProgrammingLanguage[0:TOP])
    bar.add(name="Rating", x_axis=title, y_axis=values, is_label_show=True,
            yaxis_name="Rating (%)", yaxis_label_textcolor=AXIS_LABEL_TEXT_COLOR,
            xaxis_name="Program Language", xaxis_interval=0, xaxis_label_textcolor=AXIS_LABEL_TEXT_COLOR,
            label_formatter="{c}%", is_legend_show=False,
            label_text_color=AXIS_LABEL_TEXT_COLOR,
            mark_point=[{"coord": [2, 3], "name": "3rd"}, {"coord": [1, 2], "name": "2nd"},
                        {"coord": [0, 1], "name": "1st"}],
            mark_point_symbolsize=80,
            mark_point_textcolor="SteelBlue",
            )
    return bar


def world_cloud_chart():
    CAT1 = 1000
    CAT2 = 800
    OFFSET = 20
    item_dict = {
        # "Python": CAT1 + random.randrange(-OFFSET, OFFSET),
        # "Anywhere": CAT1 + random.randrange(-OFFSET, OFFSET),
        "Web Apps": CAT1 + random.randrange(-OFFSET, OFFSET),
        "Files": CAT1 + random.randrange(-OFFSET, OFFSET),
        "Consoles": CAT1 + random.randrange(-OFFSET, OFFSET),
        "Databases": CAT1 + random.randrange(-OFFSET, OFFSET),
        "Scheduled Tasks": CAT1 + random.randrange(-OFFSET, OFFSET),
        "Easy Deploy": CAT2 + random.randrange(-OFFSET, OFFSET),
        "Develop Anywhere": CAT2 + random.randrange(-OFFSET, OFFSET),
        "Amazing Support": CAT2 + random.randrange(-OFFSET, OFFSET),
        "Teach & Learn": CAT2 + random.randrange(-OFFSET, OFFSET), }
    name_list = item_dict.keys()
    value_list = item_dict.values()
    wordcloud = WordCloud(title="Python Anywhere Features and Advantages", width=1000, height=500,
                          page_title="Python anywhere Word Cloud")
    wordcloud.add("", name_list, value_list, word_size_range=[30, 60])
    return wordcloud
