from django.urls import path
from django.contrib import admin

from ldtkc.views import auth_register,report,del_question,load_question,register_user,login_view,auth_logout,dashboard,test_dashboard,course_detail,user_test,take_test,submit_test,download_excel_data
urlpatterns =[
    path('',auth_register, name='home'),
    path('get_registered/', register_user, name='register_user'),
    path('online_test/', user_test, name='online_test'),
    # url(r'^populate/$', populate, name='online_test'),
    path('submit_test/<username>/', submit_test, name='submit_test'),
    path('test/<username>/testdashboard', test_dashboard, name='test_dashboard'),
    path('test/<username>/', take_test, name='take_test'),
    # re_path(r'^test/(?P<username>\w+)$', leadleap_test, name='leadleap_test'),
    path('report/<username>/', report, name='report'),
    path('generate_report/<username>', download_excel_data, name='get_excel'),
    path('login/', login_view, name='login'),
    path('logout/', auth_logout, name='logout'),
    path('<username>/dashboard/', dashboard, name='dashboard'),
    path('<username>/<course_title>/', course_detail, name='course_detail'),
    path('qloads/',load_question, name='load_question'),
    path('dload/', del_question, name='del_question'),

    # url(r'^(?P<username>\w+)/student_profile/$', student_profile, name='student_profile'),
    # url(r'^(?P<username>\w+)/edit_profile/$', edit_profile, name='edit_profile'),
    # url(r'^(?P<username>\w+)/edit_studentprofile/$', edit_studentprofile, name='edit_studentprofile'),
    ]
