#############################
# Data Visualisation - HS17
# University of Zurich
# Exercise 02
# Nik Zaugg
# 12-716-734
#############################

Versions:
    python: 3.6.2
    bokeh: 0.12.10
    tornado: 4.4.2

How to run:
    -   make sure you are using python module Tornado 4.4.2 for a bokeh server (4.5.2 still not properly working with bokeh https://github.com/bokeh/bokeh/issues/6152)
    -   run conda install tornado=4.4.2 to downgrade (current version is most likely on 4.5.2)
    -   run bokeh server:
            - In Anaconda-CLI: run 'bokeh serve --show dashboard-serve.py'
                OR 
            - Other CLI: run 'python -m bokeh serve --show .\dashboard-serve.py'

            --> this will open the dashboard in a browser-tab

Alternative:
    -   Project folder contains file 'dashboard.py' which uses CustomJS to update data of the images.
        As all data needs to be loaded beforehand, the resulting dashboard.html is ~75MB.
        - Run 'dashboard.py' to generate 'dashboard.html'
          => Salt & Pepper percentages available only between 0% and 50% with 10% steps
