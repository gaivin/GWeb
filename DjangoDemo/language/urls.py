#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: Gaivin Wang 
@license: Apache Licence  
@contact: gaivin@outlook.com
@site:  
@software: PyCharm 
@file: urls.py 
@time: 10/10/2018 3:17 PM 
"""

from django.conf.urls import url
from django.conf.urls.static import static
from DjangoDemo import settings
from language.views import history_view, rank_view, feature_cloud_view
urlpatterns = [
    url('^history', history_view),
    url('^rank', rank_view),
    url('^feature_cloud', feature_cloud_view),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
