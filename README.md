VW Data Cleanup

Overview

This project is a SQL data-cleaning and transformation project built with PostgreSQL.

The dataset contains application and opportunity information with missing values, inconsistent date formats, numeric values stored as text, and status fields that need to be made easier to work with.

I created a cleaned SQL view that transforms these fields into a more consistent format while keeping the original source tables unchanged.

What I worked on

The cleaning process includes:

* Handling missing values with COALESCE()
* Checking values before converting them to numeric types
* Converting text and timestamp values into usable dates
* Standardizing application and record statuses
* Creating additional status fields from existing data
* Joining learner information with opportunity information
* Cleaning fields used for analysis and reporting
* Keeping the transformation logic inside a reusable SQL view

SQL Techniques Used

* COALESCE()
* CASE statements
* Regular expressions
* CAST
* SPLIT_PART()
* LEFT()
* Date and timestamp conversion
* LEFT JOIN
* SQL views

Data Cleaning Examples

Missing values

Several fields contain missing or blank values. I used COALESCE() to provide a consistent fallback value where appropriate.

For example:

COALESCE(l.assigned_cohort, 'Unknown')

This prevents missing cohort information from being left as an empty value in the cleaned view.

Numeric values stored as text

Some fields contain numbers stored as strings. Before converting them, I checked whether the values matched a numeric pattern.

CASE
    WHEN l.fee ~ '^[0-9.]+$'
    THEN l.fee
    ELSE '0.0'
END

The result is then converted into a numeric data type.

Inconsistent date formats

Some date fields contain regular date strings, while others contain numeric timestamp values.

I used conditional logic to handle these different formats and convert them into PostgreSQL dates.

Status fields

I created readable status fields from existing information.

For example, the presence or absence of an acceptance date can be used to classify a record as:

* Pending Decision
* Decided

Similar logic is used for application, completion, withdrawal, payment, and other record states.

Combining Related Data

The project combines information from multiple datasets using LEFT JOIN.

Learner records are connected with status information and opportunity information so that the final view contains the fields needed for further analysis.

Why I Built This Project

I built this project to practice working with real-world data that is not always clean or consistently formatted.

It helped me strengthen my SQL skills and gave me practical experience with:

* Data validation
* Missing-value handling
* Data type conversion
* Date cleaning
* Conditional logic
* Data transformation
* Joining related datasets
* Preparing data for analysis

Tools

* PostgreSQL
* SQL

Project File

vw_data_cleanup.sql

This file contains the SQL used to create the cleaned data view.

Notes

This is a portfolio project created for learning and demonstration purposes.

The main focus is the SQL transformation and data-cleaning process rather than the original source data.
