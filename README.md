# Boxing: The Pound for Pound King
## Overview:
This is my first project in this field. Boxing is the sport I'm most passionate about because of its unique martial art and rich history. With the skills I've acquired and continue to develop, I decided to dedicate this project to boxing. Right now in the sport of boxing, there are huge debates about who truly is the "face of boxing." Two names usually come up in these debates: Canelo Álvarez and Oleksandr Usyk. Both fighters have been in the business for decades and have earned undisputed titles in multiple weight classes. I found data that covers two distinct career fights for each fighter, and I have tasked myself with manipulating and analyzing this data to determine who is the true face of boxing/Pound for Pound King. I believe this project will give well-deserved recognition to the better fighter.

In the world of boxing, data is often closely guarded to protect fighters' reputations. Many fighters prefer fans to remember their victories rather than scrutinize their performance metrics, such as missed punches versus thrown punches. My goal is to present data that transparently and visually showcases their boxing skills. Using SQLite and Tableau Public, I've analyzed and displayed key metrics such as the number of punches missed versus thrown, the percentage of jabs and power punches, and which fighter absorbed more punches, among other insights.
 
## Features:
**Loading Data:** Read four CSV files into a Jupyter Notebook.

**Cleaning and Combining Data:** Pandas in Jupyter Notebook to clean the data, read to a SQLite database. Joins and Unions were executed with SQLite. 

**Data Visualization:** Visualizations were created with Tableau Public and organized in a Tableau Dashboard.

**Best Practices:** Utilized a virtual environment and included set-up instructions in a README.

**Data Interpretation:** Final analysis is included with the Tableau Dashboard.

## Tableau Visualization Dashboard:
The visualizations created using Tableau can be accessed here: 

(provide a link to my Tableau Public dashboard).

## Set-up:
Activate the virtual environment based on your operating system.
> **Note:** This project was created and completed on a Windows computer. I can not attest that this project will work with a Mac or Linux operating sytem.

1. **Clone the repository to your local machine:** use `git clone https://github.com/MaliMcDiesel/Boxing_P4P.git`.

2. **Navigate to the project folder in your terminal or Gitbash:** `cd` to project folder.

3. **Create your virtual environment:** In your terminal, Mac/Linux:  `python3 -m venv venv` or 
Windows Gitbash: `python -m venv venv`.

4. **Activate the virtual environment:** Mac/Linux: `source venv/Bin/activate`. Windows PowerShell: `venv/Scripts/activate`. Windows Gitbash: `source venv/Scripts/activate`.

5. **Install the required packages:** `pip install -r requirements.txt`


### Running the Data Cleaning Script:
>**Note:** Make sure the virtual environment is active.  

1. Run the `clean_data.ipynb` file. I should clean the data and create the SQLite database `boxing.db`.

2. 


## Data Source
The data used in this project is sourced from Kaggle. It includes detailed information about fighters, rounds, and punch statistics.
The data I used can be found here: https://www.kaggle.com/datasets/omarrojasnguyen/boxbynumbers-boxing-data


## Acknowledgements
Thanks to Code:You, Kaggle for providing the data, my mentors, and everyone who has supported me in this project.

