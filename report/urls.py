# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:yhq

from django.conf.urls import url

from . import views

app_name = 'report'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<questionnaire_id>\d+)/get_report/$', views.get_report, name="get_report"),
    url(r'^user_get_report/$', views.user_get_report, name="user_get_report"),
    # 用户获取所有报告
    url(r'^user_get_all_report/$', views.user_get_all_report, name="user_get_all_report"),
    # 用户获取指定报告
    url(r'^user_get_specific_report/$', views.user_get_specific_report, name="user_get_specific_report"),
    # word 服务获取生成报告模板所需信息
    url(r'^send_report_data/$', views.send_report_data, name="send_report_data"),
    url(r'^admin_get_report/$', views.admin_get_report, name="admin_get_report"),
    # 管理员获取所有用户报告
    url(r'^admin_get_all_report/$', views.admin_get_all_report, name="admin_get_all_report"),
    # 管理员获取指定用户报告
    url(r'^admin_get_specific_report/$', views.admin_get_specific_report, name="admin_get_specific_report"),

]