Film Blog
--
For my milestone project 4 for Code Institute Diplome in Software development, I have chosen Project Example Idea 2 Reddit Style News Site. This site will be for movie reviewers to be able to give their opinions on films, directors or Actors. Film Blog provides a platform for movie lovers to reach out and connect and share their ideas and thoughts. We are all critics at heart so it is great to be able to express yourself. It will be developed using Django which is a high-level Python web framework. 

Heroku URL: https://ckz8780-django-filmblog-app.herokuapp.com/

GitHub  URL: https://github.com/colinshaw1/portfolio-project-4


Who is Film Blog intended for?
--

Film Blog is intended to attract movie bloggers but will be limited to approval from the administration. The purpose is to attract individuals who want to share information about their love for movies and thoughts on the directors, actors and cinematography. 


Owner
--

The owner of this game is Colin Shaw. The goal is to help film lovers express their feelings in a safe and secure environment. 

How to use
--

The film blog is deployed and you can see reviews, likes and comments from other owners if a user wants to leave a comment or like they can register for an account and easily log in. Anyone can leave a comment but it has to be approved by Admin before it is published. 

Screenshots of Application
--
Successful  Install of Django 
--

![image](https://user-images.githubusercontent.com/56481190/189747882-06e9b79a-4c1b-45ba-8f35-0bbbaf121cea.png)

--
Admin Log in 
----
![image](https://user-images.githubusercontent.com/56481190/189748251-fdb3dd39-710a-4ae1-9b82-81a163f4040e.png)
----
CRSF verification would not work this was the most challenging part of the project. I needed tutor support to help show me how to fix this. the issue was related to Django 4, been recently fully released. I had to set a new variable in my settings.py file called CRSF_TRUSTED_ORIGINS, which is a list holding all the URLs of the site that are trusted and had to include my workspace. It needed to contain HTTPS at the start to stop the error. The port number had to be included which was what I was doing wrong I only had my workspace entered.  

---
![image](https://user-images.githubusercontent.com/56481190/189748440-30672517-407b-4879-b8f9-031eb702f059.png)
----
Adding a post on admin page
-----
![image](https://user-images.githubusercontent.com/56481190/189750006-121d830a-a014-4a10-943f-3de5badc1e53.png)
--
Post added and shown in the list, where they can be searched for or filtered

![image](https://user-images.githubusercontent.com/56481190/189750492-fbac3eb5-5d4e-47a8-9136-d726968b14ee.png)
--
Home page deployed on Heroku
--
![image](https://user-images.githubusercontent.com/56481190/221403634-ccce31a9-550f-4eba-9f4a-076bed3cf182.png)
--
logged in home screen
--
![image](https://user-images.githubusercontent.com/56481190/221403652-2551cccf-232f-41b5-a82f-3c854ff84c39.png)
--
Editing a post
--
![image](https://user-images.githubusercontent.com/56481190/221403741-975ae3b2-bac7-4d93-aa53-d2cebb12eb14.png)

--
Deleting post 
--
![image](https://user-images.githubusercontent.com/56481190/221403757-35326dfd-41d4-4ea9-a7b9-f01bac72cc90.png)

--
Leaving a comment
--
![image](https://user-images.githubusercontent.com/56481190/221403802-6984763d-f71c-4153-b166-9d57bc83973b.png)

---
Comment awaiting approval
---
![image](https://user-images.githubusercontent.com/56481190/221403815-96d3d46e-e16d-4c13-89a3-13ef086125dc.png)

---
Comment approved
---

![image](https://user-images.githubusercontent.com/56481190/206544744-27ce498d-4e68-4d01-9c8d-abc8e2bf44bb.png)

Liked a post

![image](https://user-images.githubusercontent.com/56481190/206542440-c3e176e3-0600-481d-806d-7ad66aa8b030.png)

Logout

![image](https://user-images.githubusercontent.com/56481190/206544834-7ae0be5d-9202-4d60-b099-7a7ec7968614.png)

Register

![image](https://user-images.githubusercontent.com/56481190/206544877-d6dbaf40-2a55-4324-b1d4-78461358f1f9.png)


Agile Methodology
--
---
For project management of Film, Blog Trello was used to track the Agile Methodology. 
---
Start planning the Trello board
Planning underway deciding tasks that are most important and how to plan and design the project
---
![image](https://user-images.githubusercontent.com/56481190/189648539-795b182d-fcb7-4ff9-bdb3-52069e507e2b.png)
---
Progress is underway and projects planning and wireframes are under consideration
Project planning starts with drawing up wireframes of how the application will look, looking at other blogs and seeing the most user-friendly methods to help with ideas.
---
![image](https://user-images.githubusercontent.com/56481190/189648782-b9c86ab0-0271-48e5-86de-1d7c32ae9775.png)
---
The planning stage is over and development starts and error fixing as progress through the plan.
Development started and the app is under construction in gitpod. App is built using Django and models, views and templates are been used. Project plans and wireframes are finished.
---
![image](https://user-images.githubusercontent.com/56481190/189648851-4c94921a-c1bd-402e-9033-56d914cc880c.png)
---
As development is progressing testing starts to be a factor and the app gets tested.
Development is progressing so it is time to see how templates are reacting and rendering results to the database. ReadMe file is started. 
---
![image](https://user-images.githubusercontent.com/56481190/189648905-8ba1cb00-b805-433a-a5f9-885f08cc66c7.png)
--
Development finishing up and the ReadMe file starting to get worked on.
App is developed and deployed and now the final touches are added. The ReadMe file is getting updated with progress.
--
![image](https://user-images.githubusercontent.com/56481190/189648996-5b88e13a-5892-4431-8682-6b8b994d510b.png)
--
Project finished and ReadMe file
--
![image](https://user-images.githubusercontent.com/56481190/189649065-f65be60b-7abf-4101-a9fe-ec2bdfed3251.png)
---


User Stories
---
![image](https://user-images.githubusercontent.com/56481190/206549991-714eefbd-5898-4898-8670-222a7753f3b6.png)

---
User Experience
--
Website users 
--

• As a user, you want to be able to navigate clearly and hassle-free throughout the whole application. 

• As a user, you want to be able to scroll and read the content on the website with no contrast. 

• As a user, you want to be able to click on any link on the website to go to the source destination with no errors. 

• As a user, you want to be able to fill out a comment and submit it with no issues.

• As a user you want to be able to register, login and logout.

• As a user you want to be able to like and comment on a post.

Strategy Plane
---
Filmblog was created and designed for movie lovers to have a safe and secure environment to share their thoughts on the film. Anyone can comment or like on a blog post. Users must be registered to leave a comment or like a post. Comments have to be approved by admin. 

Scope Plane
--

•	Created in Django

• Home page has clickable links for Film Blog logo, Register and Login or Logout once logged in

• Like button for liking posts.

• To open each article there is a Read More button which will open the whole article

• At the bottom there is a button to leave a comment or view comments


Structure Plane
--
• The application consists of two pages a base HTML file which has a nav bar and displays the articles and some information on the right-hand side of the application.

• The details_post page consists of a sidebar for information and a full article with an option to leave a comment or view comments. The comments section extends on the details_post page when clicked on. 

• A register, login and logout page are available for users thanks to Django and Allauths powerful built in tools.


Technologies used
--
• Python is used to implement complex functions 

• Django is used as it is a python based framework and its models, templates and views simplify complex tasks

• Git for storing files and deployment 

• Heroku is used for final deployment

• Gitpod for design


Resources
--

•	Code institute for material and ideas

•	Geeks for Geeks for information and ideas

•	W3 Schools for information and ideas

•	Slack for inspiration

•	YouTube for tutorials

•	My mentor Spencer Barbell was extremely helpful throughout the process

• Tutor support 

• Forms on Django blog posts

• Course content for some functionality


Testing
--
Tested on desktop. Checked in Google chrome, firefox and safari.

Bugs

CRSF verification would not work this was the most challenging part of the project. I needed tutor support to help show me how to fix this. the issue was related to Django 4, been recently fully released. I had to set a new variable in my settings.py file called CRSF_TRUSTED_ORIGINS, which is a list holding all the URLs of the site that are trusted and had to include my workspace. It needed to contain HTTPS at the start to stop the error. The port number had to be included which was what I was doing wrong I only had my workspace entered.
The same issue occurred for hosting in Heroku but was easily fixed after thinking of how the problem above was solved.

Validation
---

• Passed validation through PEP8 online checker

Version Control
--

GitHub and GitPod to update and commit changed to my repository all commits tracked to mark progress


Deployment
--

Deployed through Heroku.
