Feedback Collection System using Google Cloud Platform

This project is a simple feedback system built using Google Cloud Platform services. Customers can submit feedback through a web form, while admins can log in to view all submitted entries. The system leverages Cloud Storage for hosting the frontend, Compute Engine for running the backend, Pub/Sub for message handling, and Cloud SQL for data storage.

Key Features

Web-based feedback form for customers
Admin login (username: admin, password: admin@123) to view all feedback
Feedback stored in a MySQL database via Pub/Sub pipeline
Technologies

Frontend: HTML, CSS, JavaScript
Backend: Flask (Python)
Cloud Storage (static site hosting)
Compute Engine (backend hosting)
Pub/Sub (message queue)
Cloud SQL (MySQL database)
How It Works

Customer submits feedback using the form
Flask backend receives the data and publishes it to a Pub/Sub topic
A subscriber service listens and inserts the feedback into Cloud SQL
Admin can log in and view all stored feedback
Setup Instructions

Create a GCP project and enable necessary services
Set up a Cloud SQL MySQL instance and create the feedback table
Create a Pub/Sub topic and subscription
Create a Compute Engine VM, install Python and Flask, and clone the project from Git
Upload index.html to Cloud Storage and make it public
Update and run the backend (app.py) and subscriber (subscriber.py) scripts on the VM
