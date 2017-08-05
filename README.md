# Stock Quote Application

## Overview

**Goal** Compare specific components' performance to the Dow Jones Industrial Average
over a desired period of time.

### Functionality
Users will be able to pick any number of Dow Jones components and compare their
performance to that of the Index over a specific time period. Users can also choose
to retrieve any one day as well. However, returns for specific date retrievals will
not have returns provided. Data will be displayed as well as written to a csv file
called "my_data".

### Usage
1. The user will be prompted for Dow Jones stock tickers; this can be one or several.
2. Any tickers not in the Dow Jones will kick back an error message and prompt the user again.
3. When ticker selection is complete, the user should type "DONE".
4. The user will then be prompted with a yes or no question regarding time period.
5. Dates must be in yyyy/mm/dd format. Please adhere to this standard.
6. Start Dates of ranges must be prior to End Dates.
7. Finally, the users data will be retrieved and cumulative returns will be calculated.
8. The display will be written to a csv file called  "my_data".

## Prerequisite
1. python3 should be installed in order to run this application.
2. Knowledge of how to work with csv files and formats.


## Installation

Download the source code:

```shell
git clone https://github.com/aeg48/freestyle.git
cd some/path/to/freestyle
```

### Go to the required folder in Windows Terminal
```shell
cd some/path/to/freestyle
```

### Run the python
```shell
python app/DJA_stocks.py
```

### Additional Requirements/information
This application has imported the csv, datetime, and pandas python packages.
