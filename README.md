## Info Scout Assignment

As part of the initial hiring process, I was given an exercise, with source data in csv and json format, that requested the following be done in python or R: 

1. A function that given a brand, returns the strongest retailer affinity relative to other brands : 
 - def retailer_affinity(focus_brand):
2. A function that returns the number of household (where a household could have many transactions in the provided dataset), allowing for a dynamic optional set of inputs.
 - def count_hhs(brand=None, retailer=None, start_date=None, end_date=None):
3. Identify brand with top buying rate ($ spent/HH).
- def top_buying_brand():

##### This was done with python, utilizing the Pandas library, and can be run as a CLI application.

### Setup
Setup was done on a windows machine running Linux inside of vagrant, so the directions may vary slightly depending on your own setup.

git clone https://github.com/jessigrayson/infoscout_hw.git
cd infoscout_hw

##### Create virtual environment

pip install virtualenv (if on windows, may need to do pip install --always-copy)
virtualenv env
##### Activate virtual environment
source env/bin/activate

##### Install System Dependencies

pip install -r requirements.txt
##### Run Program
python infoscout_fxs.py

Because of the small scope of the assignment, one .py file was created with all 3 functions that were assigned. 

### Additional Notes
- Some comments have been written within the .py file to try to clarify certain areas where I felt there were potentially stylistic differences and/or crude code.

- Due to the limitations in time, there may be some minor syntactical inconsistencies, such as " vs ', etc. 

- There is plenty of opportunity for improvement and optimization; however, the exercise allowed me to learn something new. (Enough to know that I know a very small amount of Pandas!)

