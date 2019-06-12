# Subify Issue Tracker
To fix bugs and add features to my growing sandwich filling website

[![This project uses Travis CI](https://travis-ci.org/jamesahorne/milestone-4.svg?branch=master)](https://travis-ci.org/jamesahorne/milestone-4)


## Technologies Used
Django Rest Framework - for rendering the chart.js data (?? is that right?)
Chart.js - for the data visualisation

### Features left to implement
For the first release of this website I kept users having to go to checkout and entering card details for adding bugs. The reason is so that only people with serious bugs will actually bother posting (and any user wanting to add loads as a joke would be deterred), but I may rethink a better way to do this. You must be logged into an account to post a bug as it is, so maybe that is enough.


## Credits
Got help from CI tutor for this line in settings.py
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
Ticket image from [here](https://www.vcw-wrestling.com/site/).

## Deployment
Commented out "import env" - explain
