from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^insertdata', views.insert_data ),
    url(r'^insertCourseData', views.insert_course_data ),
    url(r'^$', views.index , name='index'),
    url(r'^index', views.index , name='index'),
    url(r'^jobDataForm', views.job_data , name='job_data'),
    url(r'^course_content_form', views.course_data , name='course_data'),
    url(r'^selJobCategory', views.jobCategory_Select, name='jobCategory_Select'),
    url(r'^selectUni', views.university_Select, name='university_Select'),
    url(r'^similarity', views.similarity, name='similarity'),
    url(r'^showUni', views.showUni, name='showUni'),
    url(r'^uniDataShow', views.uniDataShow, name='uniDataShow'),
    url(r'^extractedKeywordJob', views.extractedKeywordJob, name='extractedKeywordJob'),
    url(r'^extractedKeywordUniversity', views.extractedKeywordUniversity, name='extractedKeywordUniversity'),
    url(r'^comparison', views.comparison , name='comparison'),




]