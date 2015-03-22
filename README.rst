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



Usage: render_with & def_block and use_block
--------------------------------------------

This is sort of macro-like solution allowing you to define base
template that looks always the same, and fill just a "block" inside it
differently.

Assuming you have partial template person_wrapper.html::


  {% load goodies %}
  <div class="person-wrapper">
      <div class="first-name">{{ first_name }}</div>
      {% use_block "block" %}
  </div>


You can use it in following way::


  {% load goodies %}
  {% render_with "person_wrapper.html" first_name="First" last_name="Last" %}
      {% def_block "block" %}
      <div class="last-name">{{ last_name }}</div>
      {% end %}
  {% end %}


This invocation will substitude "{% use_block "block" %}" in
person_wrapper.html with the contents within "{% def_block .... %}"
and "{% end %}" insidee "render_with". So the outcome of above will be
more or less::


  <div class="person-wrapper">
      <div class="first-name">First</div>
      <div class="last-name">Last</div>
  </div>


Another example with tables, table.html::


  {% load goodies %}
  <table class="{{ opts.table_class }}">
      <thead>
          <tr>
              {% use_block "headers" %}
          </tr>
      </thead>
      <tbody>
          {% for row in object_list %}
          <tr>
              {% use_block "row" %}
          </tr>
          {% endfor %}
      </tbody>
  </table>


can be used in following way::

  {% render_with "table.html" object_list=people %}{% def_block "headers" %}
      <td>ID</td>
      <td>First name</td>
      <td>Last Name</td>
      <td>Age</td>
  {% end %}{% def_block "row" %}
      <td>{{ forloop.counter }}</td>
      <td>{{ row.first_name }}</td>
      <td>{{ row.last_name }}</td>
      <td>{{ row.age }}</td>
  {% end %}{% end %}


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
