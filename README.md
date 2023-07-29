Python Skill Test for Zypp Recruitment
===

#  Introduction Skilltest 
Welcome to the Python Skill Test designed for Zypp's recruitment process! This skill test is designed to assess your proficiency in Python programming with a focus on data integration, data analysis, and automation.

## Instructions:
1. This repository contains a set of Python coding tasks related to data integration, data analysis, and automation.
2. Fork this repository to your GitHub account to get started with the test.
3. Complete the tasks within the specified time frame.
4. Commit your solutions to your forked repository.
5. Send the link to your forked repository to hello@zypp.io

## Guidelines:
- Create a new branch for each task before starting to work on it.
- Each task will have a dedicated directory with a README.md file explaining the task and any specific instructions.
- You are encouraged to use Python 3 and any relevant libraries or frameworks for the tasks unless specified otherwise.
- Please ensure your code is well-documented and maintainable.
- Feel free to reach out to the recruitment team if you have any questions or need clarification.

## Important Note:
- **Do not modify the original repository.** Work only on your forked repository.
- The repository is public, and other candidates may also have access to it. **Avoid sharing your solutions or collaborating with others during the test** to maintain fairness.

Best of luck with the skill test! We are excited to see your Python skills in action.

---

# Start Buienradar Skilltest

## Case introduction:
The Buienradar API provides data from all weather stations in the Netherlands every 10 minutes. You can query the data via the endpoints json.buienradar.nl or xml.buienradar.nl, and it will return the current weather data for each station.

## Data Integration

**Question 1:**
Create a pandas DataFrame with the following information about the weather station measurements. Use type casting to store the data in the appropriate format.
- Maximum and minimum temperature
- Precipitation (mm)
- x
- y
- z

**Question 2:**
Create a pandas DataFrame with the information about the weather stations:
- Name
- Latitude of the weather station
- Longitude of the weather station

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