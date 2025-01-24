<div style="text-align: center; margin-bottom: 20px;">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://www.zypp.io/static/assets/img/logos/zypp/white/500px.png" width="150">
    <source media="(prefers-color-scheme: light)" srcset="https://www.zypp.io/static/assets/img/logos/zypp/black/500px.png" width="150">
    <img alt="Zypp logo">
  </picture>
</div>

Zypp Skill Test: Dutch Weather Analysis
===

> Skilltest designed for Zypp's Recruitment process

**Time Cap:** 4 hours  
**Coding Skills:** Python, SQL, optional: HTML, CSS, JavaScript  
**Fundamental Skills:**

- Data Integration
- Data Modeling
- Data Analysis
- Automation or Data Visualization  
<br>

[![Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/)

# Table of Contents

1. [Introduction Skilltest](#introduction)
   - Our expectations
2. [The test: Dutch Weather Analysis](#the-test-dutch-weather-analysis)
   - Case introduction
   - Instructions
   - Guidelines
3. [Part 1: Data Integration](#part-1-data-integration)
   - Question 1: Create station measurement data
   - Question 2: Create weather station data
   - Question 3: Store data in an SQL database
   - Question 4: Create an ERD of the SQL database
4. [Part 2: Data Analysis](#part-2-data-analysis)
   - Question 5: Find the weather station with the highest temperature
   - Question 6: Calculate the average temperature
   - Question 7: Identify the coldest time of the day
   - Question 8: Locate the weather station in the North Sea
5. [Part 3: Automation](#part-3-automation-or-data-visualization)
   - Question 9A: Automate data collection
   - Question 9B: Data visualization

# Introduction

Welcome to this Zypp's skill test! This test is designed to assess your proficiency in Python programming and problemsolving with a focus on data integration, data analysis, and automation.

You may have arrived here as you're heading into the second part of our recruitment process. In this second part, we're eager to explore the world of coding together. Our focus will be on observing your coding skills, understanding your thought process, and discovering how you solve problems. In essence, we want to initiate an engaging dialogue about code.
This skill test serves as a starting point for you to demonstrate your coding skills, but as well for us to show what kind of projects you will encounter during your career at Zypp.

## Our expectations
This project is not designed to be a pass or fail test. There are multiple ways to solve the questions, we want to see
how you solve them. Based on your answers, we will:

- Determine your 'base' level of skills.
- Have a follow up conversations, were we will talk about the project and the choices you have made.

# The test: Dutch Weather Analysis

## Case introduction
The Buienradar API provides data from all weather stations in the Netherlands,updated 3 times an hour. You can query the data via the endpoints [json](https://json.buienradar.nl) or [xml](https://xml.buienradar.nl), and it will return the current weather data for each station.
The goal is to answer some data analysis questions, but we need data for a full day from buienradar. In order to answer the questions, the candidate needs to be able to:

1. Create a script for importing the data and exporting it to a database.
2. Model the data in the database, by relating the tables and type casting the data in the proper format.
3. Automate the script to collect 1 day of data from the buienradar API.

The test is decomposed into 3 parts.

> Note: make sure the code is reproducible for us

## Instructions:

1. This repository contains a set of Python coding tasks related to data integration, data analysis, and automation.
2. Fork this repository to your GitHub account to get started with the test.
3. Complete the tasks within the specified time frame, there is a **4 hours** timecap.
4. Commit your solutions to your forked repository.
5. In the test you will create a database, please be sure to also commit the database to the repository.
6. Send the link to your forked repository to <hello@zypp.io>

## Guidelines:

- You are encouraged to use Python 3.10 and any relevant libraries or frameworks for the tasks.
- Each section starts with a time estimation. This is not a hard requirement, but meant to give you clarity in how much time a topic should take.
- Feel free to reach out to the recruitment team if you have any questions or need clarification.
- The repository is public, and other candidates may also have access to it. **Avoid sharing your solutions or collaborating with others during the test** to maintain fairness.

Best of luck with the skill test! We are excited to see your engineering skills in action.

---

## Part 1: Data Integration

**Time Estimation:** 2 hours

In this section, you will design the datamodel and ETL code for answering the questions in Part 2. This step is the most
time consuming in this project, or general data-analysis projects.

**Question 1:**
Create a dataset with the following information about the weather _station measurements_.

- measurementid (not in dataset by default)
- timestamp
- temperature
- groundtemperature
- feeltemperature
- windgusts
- windspeedBft
- humidity
- precipitation
- sunpower
- stationid

**Question 2:**
Create a dataset with the information about the _weather stations_:

- stationid
- stationname
- lat
- lon
- regio

**Question 3:**
Store the measurements data and the station data in an SQL database. Use .sqlite for the database. Consider using index, Primary Key, and defining the relationship between the two tables.

Note: if you are not sure how to create a local database, store the data in a format you are familiar with and save it in a `data` folder

**Question 4:**
Create an ERD  of the SQL database you created. Tip: you can use [draw.io](https://app.diagrams.net/) for making the diagram.

---

## Part 2: Data Analysis
This section is about performing data analysis on your gathered data. 

**Time Estimation:** 1 hour  
In this part you are required to answer questions based on data collected in step 1.

**Question 5:**
Which weather station recorded the highest temperature?

**Question 6:**
What is the average temperature?

**Question 7:**
What is the station with the biggest difference between feel temperature and the actual temperature?

**Question 8:**
Which weather station is located in the North Sea?

---

## Part 3: Automation or Data Visualization

**Time estimation:** 1 hour  

In this section you can choose between an engineering or visualization question based on your background. We recommend the data engineers to choose the automation question and the BI developers to choose for the visualization question. The software developers and data scientist can choose based on their preference.

**Question 9A: Automation**

Describe how you would automate the population of the database with all measurements for a specific day.
In other words, the script you created in question 1 should be used to fetch the weather station data multiple times per hour, as the weather station data is updated every 20 minutes.

Feel free to use a flowchat to show the steps of your approach.

**Question 9B: Data Visualization**

Visualize your analysis of part 2. You can choose between a data visualization tool which you are familiar with and you see fit. It can also be a visualization library in Python or JavaScripts for example. 

Bonuspoints if you manage to do both!
