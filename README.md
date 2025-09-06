# Helli 5 Website

<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangomade124x25_grey.gif" border="0" alt="Made with Django." title="Made with Django." /></a>
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-360/)

This project is a comprehensive website for a high school, designed to facilitate communication and information sharing between the school administration, teachers, and students.

## Table of Contents

* [About the Project](#about-the-project)
  * [Features](#features)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Project Structure](#project-structure)
* [Database Structure](#database-structure)

## About the Project

This project is a high school website that provides a platform for the school to manage its daily activities and communication. It allows teachers to upload homework and course materials, students to access their grades and submit their work, and the administration to publish news and announcements.

### Features

The project is divided into several Django apps, each responsible for a specific set of features:

*   **`loginApp`**: Handles user authentication, registration, and profile management.
*   **`courseApp`**: Manages courses, homework, and student reports.
*   **`postingApp`**: A blog for publishing news and announcements.
*   **`honorsApp`**: Displays student honors and awards.
*   **`pansouqApp`**: A platform for programming contests.
*   **`smsApp`**: Sends SMS notifications to users.
*   **`paymentApp`**: Handles student payments and debts.
*   **`dynamicApp`**: Manages dynamic content, such as the homepage slider.
*   **`eLearning`**: Provides tools for online learning, including class attendance tracking.

### Built With

*   [Django](https://www.djangoproject.com/)
*   [Bootstrap](https://getbootstrap.com/)
*   [JQuery](https://jquery.com/)

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

You will need to have Python 3.7 and `pip` installed on your system.

*   **Python 3.7**
    ```sh
    sudo apt-get update
    sudo apt-get install python3.7
    ```
*   **pip**
    ```sh
    sudo apt install python3-pip
    ```

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/TheMn/internet-engineering-project.git
    ```
2.  Install the required packages:
    ```sh
    pip3 install -r requirements.txt
    ```
3.  Create the database:
    ```sh
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
4.  Run the development server:
    ```sh
    python3 manage.py runserver
    ```

## Project Structure

The project is organized into several Django apps, each with its own models, views, and templates. The main project directory is `helli5`, which contains the project-wide settings and URL configuration.

```
.
├── courseApp/
├── dynamicApp/
├── eLearning/
├── helli5/
├── honorsApp/
├── loginApp/
├── pansouqApp/
├── paymentApp/
├── postingApp/
├── smsApp/
├── manage.py
└── README.md
```

## Database Structure

The project uses SQLite3 as its database. The ER diagram below shows the relationships between the different models in the database.

![Database ER Diagram](http://bayanbox.ir/view/8823936539620629848/db-er.jpg)
