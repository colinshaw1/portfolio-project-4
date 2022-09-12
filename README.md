Film Blog
--
For my milestone project 4 for Code Institute Diplome in Software development, i have choose Project Example Idea 2 Reddit Style News Site. Except this site will be for movie reviewers to be able to give there opions on films, directors or Actors. Film Blog provodes a platrfom for movie loveres to reach out and connect with each other and share there ideas and thoughts. We are all critics at heart so it is great to be able to express yourself. It will be deveolped using Django which is a highg-level Python web framework. 

Heroku URL: https://ckz8780-django-filmblog-app.herokuapp.com/

GITHUB URL: https://github.com/colinshaw1/portfolio-project-4


Who is Film Blog intended for?
--
Film Blog is intened to attract movie bloggers but will be limited to approval from administration. The purpose is to attract individuals who wat to share information about there love for movies and thoughts on the dirctors, actors and cinomagraph. 


Owner
--
The owner of this game is Colin Shaw. The goal is to help film lovers express there feelings in a safe and secure environment. 


How to use
--
Film blog is depolyed and you can see reviews and comments from other owners, if a user wants to leave a review they have to supply there email and discuss with Admin if they can get a log in to share views. Anyone can leave a comment but it has to be approved by Admin before it is published. 

Screenshots of Application
--
Install of Django sucessful

![image](https://user-images.githubusercontent.com/56481190/189747882-06e9b79a-4c1b-45ba-8f35-0bbbaf121cea.png)


Admin Log in 

![image](https://user-images.githubusercontent.com/56481190/189748251-fdb3dd39-710a-4ae1-9b82-81a163f4040e.png)

CRSF verification would not work this was the most challanging part of the porject. I needed tutor support to help show me how to fix this. the issue was related to Django 4, been recently fully relaesed. I had to set a new variable in my settings.py file called CRSF_TRUSTED_ORIGINS, which is a list holding all the URLs of the site that are trusted and had to include my work space. It needed to contain HTTPS at the start to stop the error. The port number had to be included which was the what I was doing wrong I only had my workspaced entered.  

![image](https://user-images.githubusercontent.com/56481190/189748440-30672517-407b-4879-b8f9-031eb702f059.png)

Adding a post in admin page

![image](https://user-images.githubusercontent.com/56481190/189750006-121d830a-a014-4a10-943f-3de5badc1e53.png)

Post added and showing in list, where they can be searched for or filtered

![image](https://user-images.githubusercontent.com/56481190/189750492-fbac3eb5-5d4e-47a8-9136-d726968b14ee.png)

Field for leaving a comment

![image](https://user-images.githubusercontent.com/56481190/189750566-d11aaa1c-3dbe-436c-ac9e-8529b14d1f5f.png)

Comment notification for awaitng comfirmation

![image](https://user-images.githubusercontent.com/56481190/189750647-2508b7d1-18da-452b-9426-720ee34554e2.png)

Comments approved or awaitng approval

![image](https://user-images.githubusercontent.com/56481190/189750776-0bc5f132-77b5-46c3-b3da-57fd8a61b0bc.png)

Comment showing the number of comments and comment

![image](https://user-images.githubusercontent.com/56481190/189750936-bef72ce4-cd0b-454d-90e7-0081ecba9289.png)

Agile Methoglogy
--
For project management of Film Blog trello was used to track the Agile Methodology. 

Start of planning trello board

![image](https://user-images.githubusercontent.com/56481190/189648539-795b182d-fcb7-4ff9-bdb3-52069e507e2b.png)

Progress under way and project planning and wireframes under consideration

![image](https://user-images.githubusercontent.com/56481190/189648782-b9c86ab0-0271-48e5-86de-1d7c32ae9775.png)

Planning stage over and development starting and eror fixing as progressing through plan

![image](https://user-images.githubusercontent.com/56481190/189648851-4c94921a-c1bd-402e-9033-56d914cc880c.png)

As developing is progressing testing starts been a factor and app gets tested

![image](https://user-images.githubusercontent.com/56481190/189648905-8ba1cb00-b805-433a-a5f9-885f08cc66c7.png)

Development finsihing up and ReadMe file starting to get worked on

![image](https://user-images.githubusercontent.com/56481190/189648996-5b88e13a-5892-4431-8682-6b8b994d510b.png)

Porject finsihed and ReadMe file

![image](https://user-images.githubusercontent.com/56481190/189649065-f65be60b-7abf-4101-a9fe-ec2bdfed3251.png)

User Experience
--

Strategy Plane

Filmblog was created to and designed for movie lovers to have a safe and secure environment to share there thoughts on film. Anyone can comment on a post and it will have to be approved by the moderator. Users have to be approved by admin before getting a log in. Once logged in they can post about any movie.  

Scope Plane

•	Created in Django


Structure Plane




Technologies used
--
• Python is used to implement complex functionse 

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


Testing
--


Bugs

Solved



Remaining Bugs



Version Control
--

GitHub and GitPod to update and commit changed to my repository all commits tracked to mark progress

Deployment
--

