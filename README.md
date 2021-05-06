# Features of covid-vaccine-locator-india:
Helps in filtering out all the health care centres with availability of Covid-19  vaccines in India.
It resolves few of the issues present with official website https://www.cowin.gov.in:
1. It helps you filter out only those centres which have vaccine(s) available. So it saves you from finding a needle in haystack. 
2. It also helps you filter out only those centres which have vaccine(s) available for your age. So, you do not go through a list of centres who have vaccine, but not for you.


# How to access it?

I will be soon hosting this. Some work to do before that happens. Until then, the APIs can be used to fetch data. 

# Steps to run it locally:

1. Install python and pip (preffered: python3) *[follow: https://realpython.com/installing-python/]*
2. Take a pull of the main branch of this github repository
3. Run: cd ./covid-vaccine-locator-india  **[for windows replace '/' with '\\' ]**
##### #Install, create and activate the virtual environment
4. pip install virtualenv
5. virtualenv virtualenv
6. Run: source ./virtualenv/bin/activate  *[for linux/mac]*  ||  Run: .\virtualenv\Scripts\activate  **[for windows]**
##### #Install all the required python modules   
7. Run: cd ./covid_vaccine_locator  **[for windows replace '/' with '\\' ]**
8. Run: pip install ./requirements.txt   **[for windows replace '/' with '\\' ]**  
##### #Start the Django development server
9. Run: python manage.py runserver    
10. Install Postman (industry stnadard app to test APIs)
11. In Postman, make a GET request on URL: http://127.0.0.1:8000/vaccine_finder/ . In the request body pass the following:

    date:06-05-2021 *# Shows all the centres with available vaccines, for the next 7 days from this date*\
    age:50      *# Age of the person to be vaccinated*\
    state_name:uttar pradesh      *# Name of a state in India*\
    district_name:lucknow      *# Name of a district of that state*

**Note:** *All the values are passed as string*

# Enhancements (TODO)

For now it works perfectly fine, for all the districts in India. 
Backlog:

1. Add a UI to this and host it
2. Make date parameter optional
3. Add exception handling
4. Group the centres by date
5. Provide the list fo districts of the input state, to the user. if asked by the user.

# Work history:
1. Work on a simple POC in python.
2. Develop the POC to handle all the districts in the state of Uttar Pradesh in India and any other district using district_id
3. Develop upon, making it work for all the districts of India (by district_name instead of district_id)
4. Develop an API for this

