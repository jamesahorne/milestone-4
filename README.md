# Subify Issue Tracker
This project is for Milestone 4 of Code Institutes Full Stack Development Diploma, and uses Python, Django and PostgreSQL in the backend and HTML, CSS, Bootstrap and JavaScript in the frontend.
Subify Issue Tracker is a response to the growing popularity of Subify, the growing sandwich filling site. The developer decided a separate site was needed, dedicated to reporting and tracking bugs and a platform for users to ask for more features to be added to the main site.
[![This project uses Travis CI](https://travis-ci.org/jamesahorne/milestone-4.svg?branch=master)](https://travis-ci.org/jamesahorne/milestone-4)

## Please note
I started the project with different project requirements and was advised by a Code Institute tutor to submit the project based on the older project requirements. For reference, the older project requirements can be found [here](https://github.com/jamesahorne/milestone_4/blob/master/project_requirements.md).

## UX
### User Stories
- As a user wanting to buy a product, on the home page I click the Buy A Ticket button which takes me to the Buy Tickets page. This can also be achieved via the Buy Tickets link in the navigation bar. I select the product I would like to buy, which takes me to the Cart page. I click through to the Checkout page, fill out the payment details and pay.
- As a user wanting to post a feature, after buying a product as above, I select Feature and fill out the ticket form with correct details and submit.
- As a user wanting to upvote a feature, after buying a product as above, I select Upvote and choose a feature to upvote and click the upvote button attached to that feature.
- As a user wanting to post a bug, after selecting Bug on the Buy Tickets page, I fill out the ticket form with the correct details and submit.
- As a user wanting to upvote a bug, I go into the full detail page for the bug and click the upvote button.
- As a user wanting to delete a product from the cart, on the Cart page I click the delete button.
- As a user wanting to view the Data page, I click on the Data link in the navigation bar.
- As a user wanting to see all tickets, I click on the All Tickets link in the navigation bar.
- As a user wanting to see the full details of a ticket, on the All Tickets page I click the See More button.
- As a user wanting to edit a ticket, on the full details of the ticket I click the Edit button, and then fill out and submit the form on the Edit Ticket page with correct details.
- As a user wanting to search for a ticket, I type part of the ticket name into the search box in the navigation bar and click the Search button.
- As a user wanting to log in, I click on the Log In link in the navigation bar and enter the correct details into the Log In page form.
- As a user wanting to log out, I click on the Log Out link in the navigation bar.
- As a user wanting to register, I click on the Register link in the navigation bar and enter the correct details into the Register page form.
- As a user wanting to view their profile, I click on the Profile link in the navigation bar.
- As a user wanting to reset their password, on either the Log In page or Profile page, I click the Reset My Password link and follow the instructions.

### Mock Ups
I created mock ups for small, medium and large screens, which are in the [mockups directory](https://github.com/jamesahorne/milestone-4/blob/master/mockups/mockups.pdf). The changes I’ve made to the mock ups are:
- Indent all headers except for h1s. In the mock up, no headers are indented.
- Remove the option for setting the status of a ticket in the bug and feature forms. The default is now set to “ToDo”, so that only an admin can change the ticket status.
- Categorise some links in the navigation bar. This is neater and uses up less space in the navigation bar.

## Features
### Existing Features
- Accounts app
    - Allows users to register an account and log in to their account by filling out the appropriate forms.
    - Allows users to log out of their account.
    - Allows users to view their profile.
- Cart
    - Allows a users’ shopping cart to persist between sessions.
    - Allows a user to delete an item from the cart.
- Checkout
    - Allows a user to pay for a product by filling out the payment form (which passes the payment details onto Stripe).
- Home
    - Allows a user wanting to buy a ticket go straight to the Buy Ticket page.
    - Allows a user wanting to find out more information about the site find out more information by reading the About page.
    - Allows a user interested in the site data look up some site data.
- Products
    - Allows a user to select a product to buy.
    - Allows a user to post a feature or bug by filling out the appropriate forms.
    - Allows a user to upvote a bug or feature.
    - Allows a user to see all tickets.
    - Allows a user to see the full details of a ticket.
    - Allows a user to edit a ticket by filling out and resubmitting the ticket form.
- Search
    - Allows a user to search for a specific ticket based on text typed into the search form.
- Stripe
    - Takes the card details from Checkout and processes the payments securely with the bank.
- Password reset
    - Allows a user wanting to reset their password to do so by following the instructions sent by email and given on the reset password pages.

### Features left to implement
In the future, I would like to implement more features.
- Only the user who posted the ticket can edit the ticket. (Currently any user who is logged in can edit any ticket.)
- Users can buy more than one product at a given time.






## Technologies Used
Django Rest Framework - for rendering the chart.js data (?? is that right?)
Chart.js - for the data visualisation



## Credits
Ticket image from [here](https://www.vcw-wrestling.com/site/).
Do I put chart js here too? Read requirements...
Stripe code is from Code Institute tutorials

## Deployment
Mention about local vs prod? Ask tutor
