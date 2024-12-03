# Boxing: The Pound for Pound King
## Introduction
This is my first project in this field. Boxing is the sport I'm most passionate about because of its unique martial art and rich history. With the skills I've acquired and continue to develop, I decided to dedicate this project to boxing. I want to find out who is the true pound for pound king of boxing today.

## Objectives
The main objectives of this project are:

To determine the best pound-for-pound boxer using various statistical analyses.

To visualize the data effectively using Tableau.

To provide insights based on the data analysis that highlight the strengths and weaknesses of the top boxers.

## Methodology
## Data Cleaning
### Data cleaning steps involved:

Removing null values.

Standardizing fighter names.

Ensuring consistent data types.

## Analysis
The analysis involved calculating various statistics, such as total punches landed, missed punches, and comparing fighter performance across different matches.

## Results and Insights

Fighter A had the highest number of landed punches.

Fighter B showed significant improvement over successive rounds.

## Tableau Dashboard
The visualizations created using Tableau can be accessed here (provide a link to my Tableau Public dashboard).

## Set-up
Activate the virtual environment based on your operating system.
1. Clone the repository to your local machine using `git clone https://github.com/MaliMcDiesel/Boxing_P4P.git`.
2. Navigate to the project folder in your terminal or Gitbash. `cd` to project folder.
3. Create your virtual environment using `python3 -m venv venv` on Mac/Linux or `python -m venv venv` in Windows Gitbash.
4. Activate the virtual environment. `source venv/Bin/activate` on Mac/Linux. `venv/Scripts/activate` in Windows PowerShell. [^1]. Windows Gitbash `source venv/Scripts/activate`.
5. Install the required packages. `pip install -r requirements.txt`


### Running the Data Cleaning Script
1. Make sure the virtual environment is active.  
2. Run the `clean_data.ipynb` file. I should clean the data and create the SQLite database `boxing.db`.

### SQL Queries


### Exporting Results to CSV
Use the provided script to export the query results to CSV files for use in Tableau.

## Data Source
The data used in this project is sourced from Kaggle. It includes detailed information about fighters, rounds, and punch statistics.
The data I used can be found here: https://www.kaggle.com/datasets/omarrojasnguyen/boxbynumbers-boxing-data

### Contributing
If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

## License
This project does not have any licensing issues as the data was sourced from Kaggle.

## Acknowledgements
Thanks to Code:You, Kaggle for providing the data, my mentors, and everyone who has supported me in this project.

