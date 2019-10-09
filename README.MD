### To run my project locally
`python3 manage.py runserver`   
first need to make sure that the container is running in docker

# Life App
An app that brings together all parts of keeping my life organized.  
Python Django web app, mobile friendly.  

Will include:  
## Task app 
> intentionally choose the word "task" b/c 1) Eisenhower Task Matrix 2) not syntax issues with 'ToDo' vs 'to-do' etc.
  - tags that act like folders (no need for both)
  - no "due" dates
  - focus feature:
    - forced to ask if you completed tasks marked...in a certain way
    - what to do today/week/weekend
  - priority settings:
    - ex: Important & Urgent (asap), Important & Not Urgent (get to it), Not Important & Urgent(do it), Not & Not (eventually)
    - code: table: name, description, number to use for organization
  - IDEAS:
    -  be able to link different app things in a task (ie note, calendar event, meal)

  

## Calendar integration app
> Ability to look at a day and see what task items there are to do and what the meal plan is.  
  `33126
## Note app
## Meal planning
## Main app
  - views that combine the apps & a summary

### Admin control:
- tag names
- priority settings

---
3
# Phases

### Start
- main app
- push to github
  - or at least git versioning
- login
https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/  

### Task App phase 1
- [X] createapp
- [X] task model - minimal
- [X] create view
- [X] list view
- [X] detail view
- [ ] CRUD on detail view
- [ ] write test
- [ ] add bootstrap

### Later
- look mobile

---
# Running Todo List
- [X] login logout
- [X] push to github  

- [X] use postgres instead of sqlight --> specifically running on docker postgres container
- [ ] setup postgres the same way it is at work

- [ ] add home/index path for each app
- [ ] add registration

