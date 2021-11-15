QA-DevOps-Fundamental-Project-DevOps Forum

This repository contains all of my work for the QA Fundamental Project that I was assigned. It goes over all aspects of the development stages that I had to under go to reach the final stage and meet the requirements that have been set out by the project brief.	

Project Brief:
The idea for this project was to create a forum page that would follow the basis of a CRUD application. I have incorporated these features within my project by creating a forum page that allows users to create a post (like a tweet), read that same post, update and make changes to that post as well as delete it from the system completly entirely through the webpage that I have developed over the course of 3 days.

App Design:
To show that I have implamented a CRUD application, I created a forum page that would work like twitter where users are able to:

*Create a post
*Read a post
*Update a post
*Delete a post

Entity Relationship Background:

 


Above is the ERD that I create to demonstrate how my system will have a one to many relationship. Which shows that one user is able to create multiple posts, read them, update them as well as delete them. In  the near future I would like to create a category folder that would allow the user to create posts inside a folder that are generalised as a whole within that folder.

CI Pipeline:
I decided to use Jenkins to show the stages for this project through a CI Pipeline. Jenkins allowed me to structure my work through a timeline and define the requirements that would make my project functional from a user perspective. I created my User Stories to better understand what I would need and how my tasks could be broken down between the three days I had to complete this project whilst meeting all of the requirments.
 
 
 

Above you can see my timelined list of tasks as well as user stories that I created to plan out the course journey of my project.

Version Control (GIT)
For version control, I used GitHub to manage my project as it allowed me to directly upload and save my work onto my repository without having to create a local back up. It has also allowed me to go back to previous versions of my work to pull down any work that could be useful if I managed to create issues with the file version on my local machine.

Build Server:
I used Jenkins to build a server for my project to incorporate functions of building, testing and deploying a system through continuous integration via GIT.

Risk Assessment:
I created a table that would be my risk assessment table so that I could better understand the risks of the project and what it could potentionally be vulnerable to. Within having done this research it allowed me to strategize ways to control this.
 


Testing:
I was unable to get my tests to work due to a magnitude of technical reasons. However I did attempt to use pytest within my project and unfortunatley was unable to get it to work.

The App:

Below is a screenshot of the homepage that the users will first see with the option to access the login page, register page and home page as well as the contact page.
 
Below is a screenshot of the login page that the user can access to log into their account if they have registered for one prior so that they can delete and or update their posts as well as make new ones.
 
Below is a picture of the registration form that the user can use to create a new acconut so the system stores it and remembers their credentials for when they want to log back in.
 
Below is a screenshot of the create post form so that the user is able to create a post and upload it onto the forum page.
 
Below is a screenshot of what the user will see what they upload their post with the confirmation message that it has gone through.
 
The screenshot below shows what the user can see when they click on their post which allows them to either delete or update the post.

 
The screenshot below is what the user sees once they have selected to update the post.
 
And this is what the webpage looks like when the user has selected to delete the post.
 


Known Issues:
*A user is able to delete someone else's post
*Pytest won't work to show coverage of how many tests are passing
*Contact page doesn't redirect anywhere.

Future Work:
I want to incorporate a way for users to create categories/folders so that they can create posts that directly co-relate to those folders to create a filtering system to find posts with ease.
Another good feature would be too incorporate a search engine function that would allow users to search for key words within a post header to increase ease of use for the user.
Being able to incorporate the option to add a video or image file would also be interesting as it could be a platform like instagram or facebook.








 




