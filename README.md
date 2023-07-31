Python Skill Test for Zypp Recruitment
===

> Skilltest designed for Zypp Recruitment


#  Introduction Skilltest 
Welcome to the Python Skill Test designed for Zypp's recruitment process! This skill test is designed to assess your proficiency in Python programming with a focus on data integration, data analysis, and automation.

## Instructions:
1. This repository contains a set of Python coding tasks related to data integration, data analysis, and automation.
2. Fork this repository to your GitHub account to get started with the test.
3. Complete the tasks within the specified time frame.
4. Commit your solutions to your forked repository.
5. Send the link to your forked repository to hello@zypp.io

## Guidelines:
- You are encouraged to use Python 3.10 and any relevant libraries or frameworks for the tasks.
- Please ensure your code is well-documented and maintainable.
- Feel free to reach out to the recruitment team if you have any questions or need clarification.

## Important Note:
- The repository is public, and other candidates may also have access to it. **Avoid sharing your solutions or collaborating with others during the test** to maintain fairness.

Best of luck with the skill test! We are excited to see your engineering skills in action.

---

# Start Buienradar Skilltest

## Case introduction:
The Buienradar API provides data from all weather stations in the Netherlands,updated 3 times an hour. You can query the data via the endpoints [json](https://json.buienradar.nl) or [xml](https://xml.buienradar.nl), and it will return the current weather data for each station.
The goal is to answer some data analysis questions, but we need data for a full day from buienradar. In order to answer the questions, the candidate needs to be able to: 
1. create a script for importing the data and exporting it to a database.
2. model the data in the database, by relating the tables and type casting the data in the proper format.
3. automate the script to collect 1 day of data from the buienradar API.

The test is decomposed into 3 sections.

## Data Integration

**Question 1:**
Create a dataset with the following information about the weather _station measurements_.
- timestamp
- temperature
- groundtemperature
- feeltemperature
- windgusts
- windspeedBft
- humidity
- precipitation
- sunpower
- measurementid (calculated, not in dataset by default)

**Question 2:**
Create a dataset with the information about the _weather stations_:
- stationid
- stationname
- lat
- lon
- regio
- sunrise
- sunset

**Question 3:**
Store the measurements data and the station data in an SQL database. Use .sqlite for the database. Consider using index, Primary Key, and defining the relationship between the two tables.

**Question 4:**
Create an ERD diagram of the SQL database.

---

## Data Analysis

**Question 5:**
Which weather station recorded the highest temperature of the day?

**Question 6:**
What was the average temperature throughout the day?

**Question 7:**
At what time was the average temperature the coldest during the day?

**Question 8:**
Which weather station is located in the North Sea?

**Question 9:**
Create a graph of the temperature per measurement point.

---

## Automation

**Question X:**
Ensure that the database is populated with all measurements for a specific day. In other words, the script you created in question 1 should be used to fetch the weather station data multiple times per hour, as the weather station data is updated every 10 minutes.

---