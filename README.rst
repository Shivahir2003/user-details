============
get-user-data
============

this is a Django app to conduct web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "get_data" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "get_data",
    ]

2. Include the polls URLconf in your project urls.py like this::

    path("get_data/", include("get_data.urls")),

3. Run ``python manage.py migrate`` to create the models.

4. Start the development server and visit the admin to create a poll.

5. Visit the ``/get_data/`` URL to participate in the poll.