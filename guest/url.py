from django.urls import path
from guest import views

urlpatterns = [
path('login/',views.login, name='login'),
path('loginaction/',views.loginaction, name='loginaction'),
path('',views.guestindex, name='guestindex'),
path('studentregistration/',views.studentregistration, name='studentregistration'),
path('studentregistrationaction/',views.studentregistrationaction, name='studentregistrationaction'),
path('studentregistrationview/',views.studentregistrationview, name='studentregistrationview'),
path('staffdetails/',views.staffdetails, name='staffdetails'),
path('staffdetailsaction/',views.staffdetailsaction, name='staffdetailsaction'),
path('staffdetailsview/',views.staffdetailsview, name='staffdetailsview'),
# path('adminindex',views.adminindex, name='adminindex'),
path('coursedetails/',views.coursedetails_view, name='coursedetails'), 
path('coursedetailsaction/',views.coursedetailsaction, name='coursedetailsaction'),
path('coursedetailsview/',views.coursedetailsview, name='coursedetailsview'),
path('coursedetailsedit/<int:id>/', views.coursedetailsedit, name='coursedetailsedit'),
path('coursedetailsdelete/<int:id>/',views.coursedetailsdelete,name='coursedetailsdelete'),
path('subjectdetails/',views.subjectdetails, name='subjectdetails'),
path('subjectdetailsaction/',views.subjectdetailsaction, name='subjectdetailsaction'),
path('subjectdetailsview/',views.subjectdetailsview, name='subjectdetailsview'),
path('subjectdetailsedit/<int:id>/', views.subjectdetailsedit, name='subjectdetailsedit'),
path('subjectdetailsdelete/<int:id>/',views.subjectdetailsdelete,name='subjectdetailsdelete'),
path('enrolleddetails/',views.enrolleddetails, name='enrolleddetails'), 
path('enrolleddetailsaction/<int:id>',views.enrolleddetailsaction, name='enrolleddetailsaction'),
path('enrolleddetailsview/',views.enrolleddetailsview, name='enrolleddetailsview'),
path('cusindex/',views.cusindex, name='cusindex'),
path('getsubjectview/<int:id>',views.getsubjectview, name='getsubjectview'),
path('subjectviewmore/<int:id>',views.subjectviewmore, name='subjectviewmore'),
path('addtoenrolled/<int:id>',views.addtoenrolled, name='addtoenrolled'),
path('addtoenrollment/<int:id>',views.addtoenrollment, name='addtoenrollment'),






 
]