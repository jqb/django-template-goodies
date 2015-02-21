django template goodies
=======================

A set of simple tools that will make your life easier in django templates.
Based on great django-classytags_ library.

.. _django-classytags: https://django-classy-tags.readthedocs.org/


Installation
------------

1) Install the package

::

   $> pip install django-template-goodies

1) put "template_goodies" into INSTALLED_APPS.



Usage: render_with
------------------

This is sort of macro-like solution allowing you to define base
template that looks always the same, and fill just a "block" inside it
differently.

Assuming you have partial template person_wrapper.html::

  <div class="person-wrapper">
      <div class="first-name">{{ first_name }}</div>
      {{ block }}
  </div>


You can use it in following way::

  {% load goodies %}

  {% render_with "person_wrapper.html" first_name="First" last_name="Last" %}
  <div class="last-name">{{ last_name }}</div>
  {% end %}


This invocation will substitude "{{ block }}" in person_wrapper.html
with the contents within "{% render_with .... %}" and "{% end %}". So
the outcome of above will be more or less::

  <div class="person-wrapper">
      <div class="first-name">First</div>
      <div class="last-name">Last</div>
  </div>



Usage: dict
-----------

Updates or creates dictionary inside template. You can use all kinds
of filters on variable if you need::

  {% load goodies %}

  {% dict opts name="first"|title %}
  {% dict opts last_name="last" value=opts.name %}

  {{ opts.first }} - {{ opts.last_name}} || {{ opts.value }}


The outcome will be more or less following::

  First - last || first



Requirements
------------

- django-classytags



Authors
-------

* Jakub Janoszek (kuba.janoszek@gmail.com)
