
# CarClub App - QA 2022 DevOps BootCamp -Final Project


# Table of content



- [CarClub App - QA 2022 DevOps BootCamp -Final Project](#carclub-app---qa-2022-devops-bootcamp--final-project)
- [Table of content](#table-of-content)
- [Introduction](#introduction)
  - [Objective](#objectice)
  - [The scenario:](#the-scenario)
- [Project Management and Version Control](#project-management-and-version-control)
  - [Risks Assessment](#risks-assessment)
- [CarClub Application](#carclub-application)
  - [Database](#database)
  - [Testing](#testing)
- [CI/CD Pipeline](#cicd-pipeline)
- [Future developments:](#future-developments)
- [Thanks note](#thanks-note)
  
---

# Introduction
## Objective
The objective of this project is to achieve the following:

- To create a web application (CarClub App) that integrates with a database and demonstrates CRUD functionality.
- To utilise containers to host and deploy the application.
- To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy the application.

## The scenario:
A Car Club Manager (the user) asked to have a web application that:
- First, allow the user to have a database of the cub member through a user friendly Interface.
- Second, allow the user to have a database of cars that members own.
- Features to be implemented without having the App down.
  
  
  ---
  
# Project Management and Version Control

**Technologies Used:**

- Trello (Kanban based board)
- Git
- GitHub

I used Agile Scrum/Kanban methods to plan and track the progress of the develpment.

First, User stories were written as a list of required features. Secondly, I priorised the work based on MoSCoW prioritization, finally story points were given to each user story using Fibonacci sequence (1, 2, 3, 5, 8, 13, 21)

All user stories where added to a Kanban prject managment board using Trillo as cards. The Must Have features were first in the Backlog list. Then moved to the In Progress list and finaly to the Completed list when the work on the feature is done. Then Should Have list which also was completed, after that the Could Have list which was completed except of one task which is not important for the app to function. Won’t Have list was not done.

Git was used as my version control system and hosting my code repository using GitHub. Feature branch model was used to complete my work. Feature branchs was linked to User Story Cards on Trello.

![alt text](https://github.com/M0darwish/carsclubproject/blob/dev/README_IMAGES/Trello.png)

*screenshot of Trello board (after project completion)


For more details, Please refer to the project traking board: https://trello.com/b/v24oMBAH/carclub-kanban-dev-board

## Risks Assessment

Initial risk assessment was developed to list the possible threats and risks that might affect the project delivery during development stage and deployment stages. Initial Risk Assessment as follows:

![alt text](https://github.com/M0darwish/carsclubproject/blob/dev/README_IMAGES/Risk1.png)

During the development of the project a new risk was introduced when I was not able to push the repository for some time. Which Later was confirmed to be an issue with GitHub platform. below is a screenshot of the Error.


![alt text](https://github.com/M0darwish/carsclubproject/blob/dev/README_IMAGES/GitHub_Error.png)

 This triggered the need of a reevaluation of the initial Risk Assessment.

Reevaluated Risk Assessment as follows:


![alt text](https://github.com/M0darwish/carsclubproject/blob/dev/README_IMAGES/Risk2.png)

---
# CarClub Application

**Technologies Used:**
- Python
- Flask
- Docker/Docker Compose
- MySQL
- SQlite (For Testing)

 CarClub App is monolithic Flask application that serves both the frontend and backend of the application.With the Don't Repeat Yourself (DRY) mentality, The app has been built using Flask web framework to keep track of two entities (Members and Cars) with One-To-Many relationship where a member can have many cars enrolled.

The frontend aspect of CarClub app uses HTML templates to serve the web pages that allow the user to perform full CRUD functionality with information from the database. The web server Nginx has been used as proxy.

Templating has been used for the frontend. I used a main page (main.html) template with a "block", which allows children templates to inherit from this template the main header of the App (e.g.Create New Member or car).
Children templates has been built as a UI to allow the user to perform CRUD finicality for both entities and display the Forms using Jinja2 templating. Forms has been implemented using the WTForms and Flask-wtf libraries.

I used Flask Routes provide the URL endpoint for the HTML pages as well as passing variables with Forms and the front-end HTML.

The backend aspect of CarClub Application is the use SQLAlchemy to model and integrate with MySQL database (SQlite in the Testing Stage).

Docker-Compose has been used to containtise the application. With the use of docker-compose.yaml, It create three containers. Ninx, carclubapp and a database container which is connected to a volume carclub_database_volume where the data is stored.

## Database

**Technologies Used:**


The app has been built to keep track of two entities (Members Table and Cars Table) with One-To-Many relationship where a member can have many cars enrolled. A user can add a member to the Members table and after that they can add a car to the Cars table, where they can select the name of the car owner from a drop-down menu.

CarClub Entity Relationship Diagram (ERD) shown below:
![alt text](https://github.com/M0darwish/carsclubproject/blob/dev/README_IMAGES/carclup_erd.png)


---

## Testing

**Technologies Used:**
- Pytest
- pytest-cov
- SQlite (For Testing)
- Junit and Cobertura (Jenkins Plugin)
  

  Pytest was used to insure that the code is written, to serve the CURD functionality required by this project, without defects. Unit tests been carried out on the development server before it was pushed to Jenkins as part of CI/CD pipeline. Test stage has been developed to carry out unit test before the Build and Deployment Stages. Starting from CURD functionality for Members part of the application I was able to achieve 71% coverage. Eventually, I was able to achieve 98% coverage (as shown below). Which includes testing the full CURD functionality for both tables. 

Junit and Cobertura Plugin have been used to make tests easier to read and navigate bugs. Configuration has been done to produce those reports post Stages of the pipeline using Junit report xml file.

Below are the testing results (Screenshots from Jenkins):

![alt text](https://github.com/M0darwish/carsclubproject/blob/dev/README_IMAGES/Cobertura_cov.png)
 
 The above shows Cobertura Coverage Report.

![alt text](https://github.com/M0darwish/carsclubproject/blob/dev/README_IMAGES/Final_test_report.png)

The above shows the latest Tests Report.

![alt text](https://github.com/M0darwish/carsclubproject/blob/dev/README_IMAGES/Mid_test_report.png)

The above shows an earlier Tests Report.

---


# CI/CD Pipeline

**Technologies Used:**
- Jenkens
- Docker Swarm
- Microsoft Azure Cloud

Jenkins was used as the automation server to create a CI/CD pipeline to automates the integration and deployment of new code. Hosted on Microsoft Azure cloud platform with SSH connection to Swarm-Manager server which is also hosted Azure cloud platform. DockerHub is used as the Artifact Repository to store Docker images


The pipeline is organised through five stages to achieve the requirements as the following:

0. 	Setup stage: To insure dependences (Docker/Docker compose) are installed in the Jenkins server. Also allow it to access DockerHub using credentials which is pre-stored as a secret Creds and used through environmental variables to insure security.
1.	Test Stage: Run unit tests using Pytest.
2.	Build Stage: Build the Docker images for the three services (CarClup App, MySQL, Nginx)
3.	Push Stage: the Docker images to DockerHub registry.
4.	Deploy Stage: Deploy to a Swarm manager.

A Post stages was created , where Junit and Cobertura Plugin are configured, thus been able to publish testing reports on Jenkins UI.

With the use of GitHub Web-hook, Every time a new code is committed and pushed to the project GitHub repository, the pipeline is triggered. 

The below diagram illustrate the project CI/CD pipeline:

![alt text](https://github.com/M0darwish/carsclubproject/blob/main/README_IMAGES/CarClub_CICD.png)



A screenshot of a pipeline built that's triggered by GitHub Webhook:


![alt text](https://github.com/M0darwish/carsclubproject/blob/dev/README_IMAGES/webhook.png)


---

# Future developments:
 
  Creating dedicated pipelines for different stages of deployment (e.g. feature branches run tests, but build artifacts are only produced on dev and main branches) running on more than two VMs.

# Thanks note
I'd like to thank Leon Robinson, Adam Gray, Luke Benson and Harry Volker for all the support during the Bootcamp.





