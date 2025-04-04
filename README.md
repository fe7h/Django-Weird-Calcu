# Django Weird Calcu

A reusable Django app that implements a simple 
calculator returning the answer as an image.

## Installation

## Usage

Include apps tags at the beginning of your template:
```html
{% load weird_calcu_tags %}
```
Then use in your template code the tag for calcu form 
`{% weird_calcu_form %}` and the tag for the answer field `{% weird_calcu_answer %}`.
