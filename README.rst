#DASHA MAIL
===============

This SDK allows communicate with Dasha Mail API. 

Requirements
------------

#. Python 3.8 or higher
#. pip


Instalation
------------

.. code-block:: bash
    
    pip install dasha_mail

Usage
-----

You have two ways, how you can use this module, but they both have to be configured. How to do this:

.. code-block:: python

    from dasha_mail import Configuration

    Configuration.configure('your api key')

First
~~~~~

Import API client class:

.. code-block:: python

    from dasha_mail import DashaApiClient

    client = DashaApiClient()

    client.send_request('method', **params)

Such code return JSON-object with data. 

Second
~~~~~~

On this way you can use class for work with Dasha Mail entities like Lists, Campaign and etc. 

.. code-block:: python

    from dasha_mail import Lists

    list = Lists()
    list.get()

Methods of classes have required and optional arguments. Required 


