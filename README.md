# Django Weird Calcu

A reusable Django app that implements a simple 
calculator returning the answer as an image.

## Installation

You can install this package directly from the Git 
repository in editable mode (for development) or as 
a regular package.

Installation in editable mode (for development):

``` bash
$ pip install -e git+https://github.com/fe7h/Django-Weird-Calcu.git#egg=django-weird-calcu
```

Add `weird_calcu` to your `INSTALLED_APPS`:

``` python
INSTALLED_APPS = [
    ...,
    'weird_calcu',
]
``` 

Add the `weird_calcu` URLs to your `urls.py`:

``` python
urlpatterns = patterns[
    ...,
    path('weird_calcu/', include('weird_calcu.urls')),
]
``` 

Connect static files:

Make sure that static files are configured in the project 
and add paths to the application's static resources.

## Usage

Include apps tags at the beginning of your template:
```html
{% load weird_calcu_tags %}
```
Then use in your template code the tag for calcu form 
`{% weird_calcu_form %}` and the tag for the answer field `{% weird_calcu_answer %}`.
