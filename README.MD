# Lab: 27 - Django Models

Overview
The first words you see on the Django website are

Django makes it easier to build better Web apps more quickly and with less code.

The next quote you’ll see is

The web framework for perfectionists with deadlines.

In this class we’ll build out a small, but functional, multi page web site using Django.

We’ll get a feel for the “Django Way” and see the dramatic performance gains you can get with a mature, robust framework.


## steps 1:


1. create directory
2. poetry init -n
3. poetry add django
4. poetry add --dev black
5. poetry shell
6. `django-admin startproject <project_Name> .`  (start project)
7. `python manage.py runserver` (for run server)
8. `python manage.py migrate`  (sql lite )
9. `python manage.py startapp <app_Name>`
******************************

10. In setting in project file 
in `INSTALLED_APPS` : 
add 
 `app_name(folder).apps.className`

className -> in apps  folder, `app.py`. for example : `'moviesapp.apps.MoviesappConfig' `  

******************************


11. in same file Templates add this line: 

` 'DIRS': [os.path.join(BASE_DIR , 'templates')],` and create templates folder  with base,home , about


******************************

12. go to project file -> `urls.py` 

add : 

• `from django.urls import path, include.`

•in urlpatterns add path : 

`path ('', include('appName.urls'))` 
*******************************

13. go to views in app folder 

`from django.views.generic import TemplateView`

    class Home (TemplateView): 
        template_name="home.html"  

******************************

14. create `urls.py` in app folder 

import

   `from django.urls import path`

`from .views import HomeView , AboutView`

• create the paths and  call your classes

    urlpatterns = [
        path('', HomeView.as_view(), name='home'), 
        path('about', AboutView.as_view() , name='about' ),
    ]
******************************


15. in test file in app : 

• import  : 

    from django import urls

    from django.test import TestCase , SimpleTestCase

    from django.urls import reverse



  • create class and inherit (SimpleTestCase) 
  and  your tests as a method .

  • use `python manage.py test ` to run your cheak your tests.



## steps 2:

1. In `models.py` in apps folder 

• create your class and inherit it from (models.Model) 

• add your properties and type of data field.

example : 

```
class ModelName (models.Model): 
    name = models.CharField(max_length=64) 
                
    
    description =  models.TextField(max_length=200)

    def __str__ (self):
        return self.name
```
***********************************************
2. in terminal

`python manage.py makemigrations`
   then 

`python manage.py migrate ` to apply the migration

> this for scan `module.py` run as field in databases

*******************************
3. Create super_user 

`python manage.py createsuperuser`
follow the steps .. 

then go the /admin and add users with user name and pass etc
*****************************************
4. register your model in admin app
*******************************
```
from .models import moduleName(class)

admin.site.register(moduleName) 
```
*******************************

5. from browser go to /admin  and add some data .
will open to you the moduleName .. you can fill the input field.
*******************************
6. go to views.py in app .

import 

` from django.views.generic import TemplateView , ListView , DetailView`

`from .models import ModuleName`

add your class in views with renderd html page ,
you can use list views or detailView depends on your page.
for example : 

ListView : for showing a list

DetailView : for showing  Details
```
    class snackView (ListView): 
        template_name="snack_list.html"  
        model = Snack

```
****************************************
7.  go to urls.py and add your  paths 

import
```
from django.urls import path
from .views import  <your *classes* in  views>
```
add your urls 
```
urlpatterns=[
    path = ('' , classNameIn_Views.as_view(), name= "name")
]
```
if you wanna show details of renderd data use 
for example : 
`path ('book/<int:pk>') `



*******************************************
8. create your html pages that you wanna show the list inside it  .
loop inside object_list
```
{% for i in object_list %}
{{i.name }}
{% endfor %}

in detail page :  
href= "{% url 'detialPage' i.pk %}"{{i.name}}



I got help from HamzaQahoush thx for HamzaQahoush.



