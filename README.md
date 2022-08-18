# Description

This repository includes source code files and screencast in accordance with the subtask provided by "B1 Solutions" as a pre-test for RPA developer position.

## Task

The task was to create a proper DB-scheme on the basis of data provided in xls-file and implement a web-application which is capable of uploading data from xls-file of proper structure into the database, displaying uploaded files' data and displaying their contents in a view, simmilar to their xls representation, upload data from web-server into file.

## Technological stack in use
- [x] Python 3.9
- [x] Flask Framework + Jinja2 Template engine
- [x] SQLAlchemy ORM + sqlite DB
- [x] xlrd Library for xls parsing
- [x] HTML5 + CSS3 + a some small embedded jQuerry for Frontend

## Accomplished tasks

### Mandatory
- [x] Upload data from xls-file of proper structure into DB. Display error messages in case no file is chosen, file type or format (provided it's xls-file structured in a different way) is invalid. Replace obsolete data from DB if any DB file's metadata (`pub_date` and `bank_name`) matches the newly uploaded one.
- [x] Display a table of files stored in database.
- [x] Display content of each file stored in database in a way simmilar to xls table formatting.

### Optional
- [x] Upload each file content as a valid csv (including plain text separators as strings and numeric data as numeric data with a scale of 2).

## Additional comments

Static string mapping was done via `mappings.py` assuming that no other xls file is going to register more than 9 classes of data. 

Some css styles were left embedded and some styles were extremely simplified, as there wasn't required any complex and rich css styling, though I'm familiar with a dozen of HTML/CSS concepts and BEM methodology.

Numeric data was merged into a single DB table due to its simmilar structure. In addition, some aggregate data (for ex., Closing Balance, Class and Group Aggregate, Class Names) was thought meaningless to be stored in the DB. 

Even though gathered data had a huge scale and precision (`Numeric(30, 10)` to be precise) during its summation in some Group, Class and Overall cases it didn't reach the value written in xls file. That was the main problem I couldn't explain and fix. Concerning numeric data table display, the numbers were rounded with only two scale digits left (to display both numeric and string data stored in a single collection correctly, I've written a custom template filter `filters.py` to determine whether a value is stirng or numeric data).

## Gif screencast:
![Task 2 Screencast](https://github.com/AVPa1ly/B1-Tasks/blob/release/v1.0/Screencasts/Task2.gif)
