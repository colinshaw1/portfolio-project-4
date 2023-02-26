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

Home screen 
--
![image](https://user-images.githubusercontent.com/56481190/221404446-62d47942-ea69-4c48-9176-55b528f260ce.png)

--

logged in home screen
--
![image](https://user-images.githubusercontent.com/56481190/221404426-a8b25d39-5724-4793-a5b9-8692985dbdb7.png)
--

Leave a review
--
![image](https://user-images.githubusercontent.com/56481190/221404471-34f43fa7-a920-4ede-9fdf-43e75424c035.png)
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

![image](https://user-images.githubusercontent.com/56481190/221404299-4061f65c-7df6-44b8-8c8a-21256bb7d33a.png)

--

Liked a post
--
![image](https://user-images.githubusercontent.com/56481190/221404305-4b357016-fd8d-430d-b8b1-c749d56d0896.png)
--

Logout
--
![image](https://user-images.githubusercontent.com/56481190/221404335-1713aa16-de9a-4dad-9f5c-48c98e61fb43.png)

--

Sign In
--

![image](https://user-images.githubusercontent.com/56481190/221404366-1f0bc86d-bf25-4ad4-ba48-bfd92b03e8f7.png)

--

Register
--
![image](https://user-images.githubusercontent.com/56481190/221404403-7da8330b-bf15-47dd-a7d3-6cd4615077e8.png)


--

Agile Methodology
--
---
For project management of Film, Blog Trello was used to track the Agile Methodology. 
---
Start planning the Trello board
Planning underway deciding tasks that are most important and how to plan and design the project
---
![image](https://user-images.githubusercontent.com/56481190/221417240-6e827d20-27b3-4584-9014-76b02a92babb.png)
---
Progress is underway and projects planning and wireframes are under consideration
Project planning starts with drawing up wireframes of how the application will look, looking at other blogs and seeing the most user-friendly methods to help with ideas.
---
![image](https://user-images.githubusercontent.com/56481190/189648782-b9c86ab0-0271-48e5-86de-1d7c32ae9775.png)
---
Design Phase under way
--

![image](https://user-images.githubusercontent.com/56481190/221417318-c89a463b-75e0-4b19-bfc4-082ebb87816f.png)

Design pahse completed
--
![image](https://user-images.githubusercontent.com/56481190/221417405-78f51b15-1021-45d5-a170-68224fdcdfb3.png)



The planning stage is over and development starts and error fixing as progress through the plan.
Development started and the app is under construction in gitpod. App is built using Django and models, views and templates are been used. Project plans and wireframes are finished.
---
![image](https://user-images.githubusercontent.com/56481190/221417454-13cc42e8-6f77-4392-8e85-05b9dde8bd16.png)


![image](https://user-images.githubusercontent.com/56481190/221417525-c388a71e-503b-4d18-9a85-dcd89a5ad486.png)

![image](https://user-images.githubusercontent.com/56481190/221417596-df56a77a-477b-4074-994f-464412ab6b03.png)

---
As development is progressing testing starts to be a factor and the app gets tested.
Development is progressing so it is time to see how templates are reacting and rendering results to the database. ReadMe file is started. 
---
![image](https://user-images.githubusercontent.com/56481190/221417655-4939ce46-9387-45b1-9c8a-6ca859c62f5a.png)


--

Development finishing up and the ReadMe file starting to get worked on.
App is developed and deployed and now the final touches are added. The ReadMe file is getting updated with progress.
--


![image](https://user-images.githubusercontent.com/56481190/221417676-f20d34fc-1e22-43e3-b8ce-2769bd16cbb7.png)

![image](https://user-images.githubusercontent.com/56481190/221417767-ff76654c-bb70-45c8-bc42-05639a7af53b.png)

![image](https://user-images.githubusercontent.com/56481190/221417792-c06b4628-e0a7-4568-828a-a97be92ec1ab.png)

--
Project finished and ReadMe file
--
![image](https://user-images.githubusercontent.com/56481190/221417829-16b407b7-1458-42e6-b7c8-644afd133135.png)
---


User Stories
---
First Time User
--
a. As a user visiting the site for the first time you want to be able to understand the main objective of the application.

b. As a user visiting the site for the first time you want to easily navigate the blog.

c. As a user visiting the site for the first time you want to be able to set up a profile.
d. A user can register for a profile.

Frequent User
--
a. As a returning user you want to be able to log in to your profile.

b. As a returning user you want to be able to logout once already logged in.

c. A returning user is able to add a review.

d. As a retruing user you want to be able to scroll the homeoage and click a review to read.

e. As a returning user you want to be able to edit a review.

f. As a returning user you want to be able to delete a preivious review.

g. A returing user you want to leave a comment.

---
User Experience
--

--
Design
--

Wireframes
--

Homepage
--
![image](https://user-images.githubusercontent.com/56481190/221404990-4f9db42a-da7c-4fbc-8b29-44323d7c6a9b.png)

Logged in
--
![image](https://user-images.githubusercontent.com/56481190/221405067-943c5a9a-65b8-4f24-824e-5e9247353b9b.png)

Film review page
--
![image](https://user-images.githubusercontent.com/56481190/221405150-7cfd5e1b-314f-4801-b458-6507efabb345.png)

--
Other
-- 
The other web pages for adding a review, regsitering for an account, and editing a post will use bootstrap forms. 


Colour Scheme
---
• A white background, with a bootstrap dark navabar and blog sections used bootstrap white text and a dark background.

Buttons
• Delete button uses bootstrap and a warning colour to make it stand out. 

• All other buttons use bootstraps secondary colour as it goes best with the dark themes. 



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
All user stories below are evident in screenshots in the above screenshot section. 

First Time User
----

a. As a user visiting the site for the first time you want to be able to understand the main objective of the application.

• This is achieved and a user can easily find the way through the application. Users can use clickable buttons to register, login or read more to view a a blog post.

b. As a user visiting the site for the first time you want to easily navigate the blog.

• Users will navigate through eaisly to be able to register, login or read a blog post.

c. As a user visiting the site for the first time you want to be able to set up a profile.

• A user can register for a profile easily through the resister button.

d. A user can register for a profile.

• When register button is clicked the user will be brought to the resgisteration form. The user can enter their detials and will be redirected the loffed in screen once they hit sign up. 


Frequent User
----------
a. As a returning user you want to be able to log in to your profile.

• A returning user can log in easily if they have a profile set up.

b. As a returning user you want to be able to logout once already logged in.

• A returning user clicks the logout button they will be logged out to the homescreen.

c. A returning user is able to add a review.

• As a returning user once the add review button is clickd the user will be brought to the add review form. Here the user will enter the details of the film like the title, tags, director, actors and content about the film. Once the post button is clicked the user can post will be published to the application.

d. As a retruing user you want to be able to scroll the homeoage and click a review to read. 

• Once a returning user clicks the read more button, they will be brougth to the blog details page with the full review. 

e. As a returning user you want to be able to edit a review. 

• As a retruing user you can edit a review by clicking the edit button on the homepage and in the blog detials page. When in the edit form the user can edit there review detials and once finsihied clik the post button which will redirect them to the home page. 

f. As a returning user you want to be able to delete a preivious review. 

• As a returning user you are able to delete a review by clicking the yellow delete buttton. Once clicked the user will be brought to the delete psot bag. Here the user will see the title of the review to delete and a short message asking if they are sure they want to delete the review. Once the delete post button the review is deleted and the user is redirected to the homepage. 

g. A returing user you want to leave a comment. 

• As a returning user you can leave a comment in the details page. Beside the previous comments card there is an add comment section. A user can write there review and click submit. Once submit is clicked a messsage will appear for the comment to be approved. Comments need to be approved incase of any unwated comments. 


Testing deployed code
--

Tested on desktop thorughout development. Checked in Google chrome thoughout devlopment. Checked on my mobile device a S22, my dads ipad and my work laptop. 

Bugs

CRSF verification would not work this was the most challenging part of the project. I needed tutor support to help show me how to fix this. the issue was related to Django 4, been recently fully released. I had to set a new variable in my settings.py file called CRSF_TRUSTED_ORIGINS, which is a list holding all the URLs of the site that are trusted and had to include my workspace. It needed to contain HTTPS at the start to stop the error. The port number had to be included which was what I was doing wrong I only had my workspace entered.
The same issue occurred for hosting in Heroku but was easily fixed after thinking of how the problem above was solved.

Responsive testing 
---
Used https://www.websiteplanet.com/webtools/responsive-checker/ for testing responsivness of website

Mobile
--
![image](https://user-images.githubusercontent.com/56481190/221418281-4235e673-5aa9-41e9-a8a5-b1ec9447d9a2.png)

Tablet
--
![image](https://user-images.githubusercontent.com/56481190/221418351-f6466af8-9395-47b1-a85f-3e3e151ff884.png)


Desktop
--
![image](https://user-images.githubusercontent.com/56481190/221418329-80fc2755-bf7b-4ebc-a47a-eeeac31229ab.png)


Validation
---

• Passed validation through PEP8 online checker

Version Control
--

GitHub and GitPod to update and commit changed to my repository all commits tracked to mark progress


Deployment
--

Deployed via Heroku. The application was deployed to Heroku very easily. A new database is needed for production which is postgress, the SQLite database can be used for development. changes needed to be incorporated in the settings.py file and a secret key was removed and added to the config vars in Heroku.
