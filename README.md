# Boxing: The Pound for Pound King
## Overview:
This is my first project in this field. Boxing is the sport I'm most passionate about because of its unique martial art and rich history. With the skills I've acquired and continue to develop, I decided to dedicate this project to boxing. Right now in the sport of boxing, there are huge debates about who truly is the "face of boxing." Two names usually come up in these debates: Canelo Álvarez and Oleksandr Usyk. Both fighters have been in the business for decades and have earned undisputed titles in multiple weight classes. I found data that covers two distinct career fights for each fighter, and I have tasked myself with manipulating and analyzing this data to determine who is the true face of boxing/Pound for Pound King. I believe this project will give well-deserved recognition to the better fighter.

In the world of boxing, data is often closely guarded to protect fighters' reputations. Many fighters prefer fans to remember their victories rather than scrutinize their performance metrics, such as missed punches versus thrown punches. My goal is to present data that transparently and visually showcases their boxing skills. Using SQLite and Tableau Public, I've analyzed and displayed key metrics such as the number of punches missed versus thrown, the percentage of jabs and power punches, and which fighter absorbed more punches, among other insights.
 
## Features:
**Loading Data:** Reads four CSV files into a Jupyter Notebook.

**Cleaning and Combining Data:** Uses Pandas in Jupyter Notebook to clean the data, then writes it to a SQLite database. Joins and unions are executed with SQLite.

**Data Visualization:** Visualizations are created with Tableau Public and organized in a Tableau Story.

**Best Practices:** Utilizes a virtual environment and includes set-up instructions in a README.

**Data Interpretation:** Final analysis is included in README and with the Tableau Story.

## Set-up:
Activate the virtual environment based on your operating system.
> **Note:** This project was created and completed on a Windows computer. I can not attest that this project will work with a Mac or Linux operating sytem.

1. **Clone the repository to your local machine:** use `git clone https://github.com/MaliMcDiesel/Boxing_P4P.git`.

2. **Navigate to the project folder in your terminal or Gitbash:** `cd` to project folder.

3. **Create your virtual environment in your terminal:**
    * Mac/Linux:  `python3 -m venv venv`  
    * Windows Gitbash: `python -m venv venv`.

4. **Activate the virtual environment:** 
    * Mac/Linux: `source venv/Bin/activate`. 
    * Windows PowerShell: `venv/Scripts/activate`. 
    * Windows Gitbash: `source venv/Scripts/activate`.

5. **Install the required packages:** use `pip install -r requirements.txt`


### Running the Data Cleaning Script:
>**Note:** Make sure the virtual environment is active.  

1. Open the `clean_data.ipynb` file and click "Run All" to run the file. It will clean the data and create the SQLite database `boxing.db`.

2. You can click the `boxing.sql` file to see performed queries.

### To see the file I used for my visualization:
Open the `boxing_tocsv.py` file and run it.
It should create a `visualization_data` folder with the csv files in it.

## Tableau Visualization Story:
The visualizations created using Tableau can be accessed here: 

https://public.tableau.com/app/profile/malachi.mcdaniel/viz/ThePoundforPoundKing/ThePoundforPoundKing?publish=yes.

## Main Conclusion
In this analysis, I compared the performance of Oleksandr Usyk and Canelo Alvarez across two respective fights, focusing on various aspects of their boxing strategies and effectiveness. Through detailed visualizations, I examined the number of punches thrown and landed by each fighter, highlighting Usyk's superior activity and scoring ability. Notably, Usyk outscored his opponents by a significant margin of 258 punches, demonstrating his efficiency by landing 30.7% of his punches compared to Canelo's 21.7%.Canelo's fighting style is known for being "laid back" but it really could work in the favor of an opponent who throws lots of punches. Additionally, Usyk's preference for combination punches was evident, with 53.2% of his punches being combinations, whereas Canelo maintained a lessnbalanced approach with 44.3% of his punches being combinations. Usyk threw many more jabs than Canelo which takes much less effort, but has been highly effective for Usyk.

Another key insight was Usyk's consistent activity, never throwing fewer than 100 punches in any round, underscoring his relentless pressure. Canelo can also be considered a pressure fighter at times, but he often gives away many rounds. Despite Canelo's high punch output in certain rounds, he struggled to match Usyk's accuracy and overall effectiveness. This analysis underscores Usyk's technical prowess and adaptability in the ring, making him a formidable opponent. Canelo might need to adjust his strategy for future bouts, especially when he moves up to light heavyweight. Canelo Alvarez and Oleksandr Usyk are two of my favorite fighters today, and they are both very talented and all-time greats. However, I would have to say that Oleksandr Usyk is the "Pound for Pound King" right now.

## Data Source
The data used in this project is sourced from Kaggle. It includes detailed information about fighters, rounds, and punch statistics.
The data I used can be found here: https://www.kaggle.com/datasets/omarrojasnguyen/boxbynumbers-boxing-data


## Acknowledgements
Thanks to Code:You, Kaggle for providing the data, my mentors, and everyone who has supported me in this project.

