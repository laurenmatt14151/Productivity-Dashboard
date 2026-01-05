'''
Functions for interacting with the GitHub API.
'''
import requests # For making HTTP requests to GitHub API
import os # Library for accessing environment variables
'''load_dotenv is used to load environment variables from a .env file'''
from dotenv import load_dotenv 

'''
Can't impoort variables directly from .env file
Need to load them into environment first using load_dotenv()
Use os.getenv to access the variables
'''
load_dotenv() # Load environment variables from .env file
TOKEN = os.getenv('GITHUB_TOKEN') # Set Github token
BASE_URL = "https://api.github.com" # Base URL for GitHub API

def get_user_data(username):
    '''
    Function to get user data from GitHub API.
    Print resulting JSON structure.
    Use this to design database models.
    '''  

    '''
    Link for users endpoint is https://api.github.com/users/{username}
    f strings insert variables directly into strings
    '''
    url = f"{BASE_URL}/users/{username}" # Build API endpoint url

    '''
    headers are used to pass additional information with the request
    Accepts format Authorization: token {TOKEN}
    '''
    headers = {'Authorization': f'token {TOKEN}'} # Set up authentication headers using the token

    '''
    resposnse object contains the server's response to the HTTP request
    get takes in url and tokens headers as parameters
    can't use requests.get(url, headers) because headers is not defined within the function
    When calling function with named parameters, use parameter=value syntax
    requests.geturl(url=url, headers=headers) also works
    parameter must be named headers to match the requests.get function definition
    '''
    response = requests.get(url, headers=headers) # Make GET request to GitHub API

    '''
    .json() method of response object converts JSON response to Python dictionary
    '''
    return response.json() # Convert response to dictionary and return



if __name__ == "__main__":
    # Test get_user_data function
    user = get_user_data('laurenmatt14151')
    '''
    commas separarate arguments in print function
    plus signs concatenate strings so values would need to be converted to strings first str(user)
    '''
    print("\n", "="*50,"USER DATA:", "\n", user)