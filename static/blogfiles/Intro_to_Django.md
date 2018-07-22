# Intro to Django

Note: I did read *Two scoops of Django* which suggests you rework the standard directory folder thast *startproject* provides - too much rework for this project



## A point on the setup

Call me crazy, but after following the usual install of Django to my PC, I did the following:

* I did not use virtualenv or virtualenwrapper-win (AHH!)
* I always run the test site on default port 8000 (no idea why you wouldn't)
* I understand **Apps** as parts of the code you could envision being insetred into other projects
  * Project is just the default configuration of Django plus the apps



## Starting a project

After running the setup, the following are snapshots of the directories produced:

![initial_django_files](C:\Users\Craig\Django_blog\Pics\Project setup\initial_django_files.png)

![django_features](C:\Users\Craig\Django_blog\Pics\Project setup\django_features.png)

To note here:

- Project is called 'mysite'
- *manage.py* is the most important tool you will use to run the project, run the shell - it is the control centre
- *\__init__.py* is a flag used to ID the directories as Python *package* directories
- *wsgi.py* is a temporary database



# Django Views

Purpose:

* Deliver **web pages and other content**
* Responsible for <u>**2 things**</u>: returning an **HttpResponse** (which contains the *content for the requested page*)  or raising an **exception** (ie. 404)

<u>**Key concept**</u>:  the view can *read from a database*, use *templates*, generate a pdf, etc. - ***anything you want***. All Django wants is an **HttpResponse or exception**

* For example, you can do these manipulations - all you need is the *HttpResponse*:

  * ```python
    def results(request, question_id):
        response = "You're looking at the results of question %s."
        return HttpResponse(response % question_id)
    ```

### View setup

Views are functions embedded inside the `views.py` file

Take the following:

![initial_views](Pics/Project setup/initial_views.png)

What is happening here:

- `django.http` is a ***module*** (group of **classes**)

  - Note that in the backend of Django, the directory would look something like `$ django/http/...` - the **dot-format** links the directory, subdirectory, and the classes they contain via `__init__.py`

- `HttpResponse` is a **class object of type**

  - The class has a bunch of attributes
  - Takes the Http **request** (function argument) and returns an Http **response**
  - Necessary because we are ***building the server***, therefore we need to let the server know ***what to return when a given request is sent***

- `def index(request):`  is the new view (a.k.a function)

  - Consumes the request and **returns** an HttpResponse


Note that when a page is requested, Django creates and HttpRequest object that contains *metadata* about the request. Django then loads the appropriate view, passing the *HttpRequest as the first argument* in the view function (hence the `request` parameter). Each view is then responsible for returning an ***HttpResponse object***

### Basics of django.http

Classes part of django.http module

`HttpRequest`: created automatically 

`HttpResponse`: created by developer. Required for returning results when a view is called 

Both have attributes

### What is http

- **Communication language** for internet sites that defines how messages are *formatted and transmitted*

- An entered URL *sends HTTP command to the server* 

- If the request is bad, the server returns a 404 error - file not found

- **Request header**:

- - Text sent from <u>browser to server</u> with *details of the information it wants back*
  - Also contains the *capabilities of the request browser* so the server returns *compatible data*

- **Response header:**

- - Text info the <u>server sends back to browser</u>
  - Contains *date, size and type of file* that is being sent back
  - *Attached* to the actual file being returned


### Slightly more complex Views

![more_complex_view](Pics/Project setup/more_complex_view.png)

Note:

* In addition to `request`, there is **another argument** entered: `question_id`
  * This can then be used in the function body 
* `%s` is used as a **dynamic insert**

So where does the `question_id` argument come from?

​	**The url**:		![more_complex_view_url](Pics/Project setup/more_complex_view_url.png)

​	Note the grouping of `<question_id>` is then **used as the argument when the views** are called

#urls

Now that we have a view that we want users to see once they request the site, we need to make sure the site address exists. Cue the urls...

![inital_urls](Pics/Project setup/inital_urls.png)

Notice:

* The module `django.conf.urls`:
* The `.` which suggests the current directory
* The `urlpatterns`
  * The `url()` function takes a regex parameter, the view that is to run when said page is entered, and the name of the page (very helpful)

Also note there will be times when creating another app you **include their own urls file in the app directory** - this is useful for the 'plug and play' nature of apps. If you do this, you must include the `include()` function that tells Django to reference urls in another directory

![new_app_urls_file](Pics/Project setup/new_app_urls_file.png)

In the above app, there is an independent urls file that can be referenced in the project urls file as such:

![new_app_urls_include_function](Pics/Project setup/new_app_urls_include_function.png)

* Notice:
  * The `import include` class
  * The reference to `include('polls.urls')` when a certain link has been selected

#settings.py

Settings is where all of the back-end configuration is set up. If you have everything else set up properly and the site still isnt working, you probably haven't set up the settings correctly (ie. included your new app in the *apps* section of settings)

### Databases

Django starts off with a SQLite database. If you know you are going to use a database other than SQLite, edit the *database* section of the settings

I will not do this now

### Miscellaneous

* Update the timezone to your local timezone

### Installed Apps

In the `INSTALLED_APPS` section, you will find a list of all of the apps Django delivers out of the box, plus you can add the apps you create

### Migrations

Fancy word for updating tables. Everytime you make a change to the data collected (ie. adding a new model), you need to run the `makemigrations` and `migrate` tasks in the Python server



# Models

Simply put: the **database layout**, including metadata. This is how you would design and configure the *rows and columns* of the database

In other words, models contain the essential **fields and behaviors** regarding the data you're storing

Key point: **DRY (Dont Repeat Yourself)** - write a model once and refer to it in other places

![initial_model](Pics/Project setup/initial_model.png)

Note that:

* *Each model* is represented by a **class** that ***subclasses***  `django.db.models.Model` 
  * Each model has *class variables* which represent **database fields** in the model (**column headers** in the database)
    * *Each field* is represented by an instance of the **Field** class (ie. Charfield)
* The `'date published'` argument in the pub_date variable is termed the *human readable* name for the variable and acts as documentation
  * The variable name (pub_date) is called the *machine readable* name and is used by default if the human readable name is not provided
* The `ForeignKey` tells Django that each instance of Choice relates to Question
  * Django supports common database relationships: many-to-one, many-to-many, and one-to-one

Finally make sure you add the app that has the new model to the `INSTALLED APPS` section of settings.py and make the migrations

### Model attributes

Class attributes allow you to modify what is returned when pulling the class name

![model_attributes](Pics/Project setup/model_attributes.png)

Note the `self` argument - since the method is tied to the class, and each instance is therefore 'fed' to the function via `Question.\__str__(instance)` we must specify that `self` represents the instace that should be fed each time the method is called

* In the case above, when the instance is called, it will return the `question_text` variable as the name of the instance

* ```python
  >>> q.question_text = "What's up?"
  >>> q.save()

  # Make sure our __str__() addition worked.
  >>> Question.objects.all()
  <QuerySet [<Question: What's up?>]>
  ```

  * See how the instance `q` was assigned `question_text` variable. Therefore when all question objects are called, it returns the question text

Note that attributes/methods are not just restricted to fields.

![model_methods2](Pics/Project setup/model_methods2.png)

Note that methods still do functions and act as functions, as displayed with `def was_published_recently(self):`



### Django API

We have already seen this above, but as a recap here is what you do to **test your models** and ensure that **future database queries** work as expected

To run the API:

```python
python manage.py shell

#Must import the classes first
from .models import Question, Choice

#Make sure __str__() worked:
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>
 
#Use filters
>>> Question.objects.filter(question_text__startswith='What')
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
           
#Do cool tricks (important for database queries)
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>
```

Note:

* `.models` suggests you extract the models from the current directory (`.`) in a file named `models`
* `Question.objects.all()` pulls all of the object instances tied to the class Question
* The `__` is the notation for **filter**
* The values are not static - you can create new variables, then use these in the queries



###Django Admin

* Delivered backend that allows non-technical users to add/update new config instead of having to do this via python code
* Create an account via`python manage.py createsuperuser`
* Access via <http://127.0.0.1:8000/admin/>

![django_admin](Pics/Project setup/django_admin.png)

* Note the editable content (groups and users) are provided by `django.contrib.auth`

So where is the 'polls' app that was built before?

![django_admin_add_app](Pics/Project setup/django_admin_add_app.png)

* Note you must **tell the admin** that Question objects have an admin interface via the `admin.site.register(Question)`
* The result:
  * <img src="Pics/Project setup/django_admin_add_app2.png" width="500">
  * Questions class (meaning the polls app) has now been added to the admin site



#Templates

* Preferred way to edit how the page looks without amending the python code

***Should be noted here that <u>views</u> are the connection between models and templates - so whatever is on the views page is what gets displayed on the template***

What is the difference between the two pieces of code below:

<img src="C:\Users\Craig\Django_blog\Pics\Project setup\Templates\bad_example_of_complex_view.png" width="500">

And:

<img src="Pics/Project setup/Templates/good_example_of_complex_view.png" width="500">

The first code snippet is correct in that the view can do what we want (ie. list out the questions segregated by comma), but it is **hard-coded** into the view

The second code snippet is **preferred**:

* Create an html template that goes through each of the questions and lists it out with the question text
* Note the `<a href="/polls/{{ question.id }}">`: this creates a <u>***hyperlink***</u> to each question  

However, the reworked view is *complicated*.

### render() shortcut

<img src="C:\Users\Craig\Django_blog\Pics\Project setup\Views\render_shortcut.png" width="500">

Note:

* Render consumes:
  * The *request*
  * A template name
  * *Optional* but <u>***highly useful***</u> dictionary as its **context** - which in this case the context is the dictionary value of the line above it in the view function (`latest_question_list`), which is the questions ordered by their publication date
    * The render function looks at the view specified (`'polls/index.html'`) and looks where in the template the context should go (if you look at the template above, you will see reference to `latest_question_list`)

This is the same as the **HttpResponse**, and in fact it returns an **HttpResponse object**



### get_object_or_404()

Instead of using the try/unless Python approach, use can use this shortcut

<img src="C:\Users\Craig\Django_blog\Pics\Project setup\Views\get_object_or_404.png" width="500">

Note how the **variable** `question` is referring to `get_object_or_404()` function, and then the render function is calling the `question` variable

Note there is also ***`get_list_or_404()`*** function available



### Dot syntax

Given that above we just created a new variable called `question`, we should use the ***dot syntax*** going forward

<img src="C:\Users\Craig\Django_blog\Pics\Project setup\Templates\dot_syntax.png" width="500">

Note:

* `question.question_text` can now be used when being referenced in the `detail.html` view
  * `question`  is now an <u>***instance object***</u> of **class Question** because it is made by `question = get_object_or_404(Question, pk=question_id)`,
    * Therefore, we can call question and refer to the **class Question attributes**

#### This is really important

We need to understand here that through the `get_object_or_404()` function we created a <u>**new object of type Question**</u> called `question`

* Therefore given what we learned in the pre-read on Python fundamentals, the new object `question` can reference the Question class attributes