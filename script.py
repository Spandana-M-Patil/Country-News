import requests
import json
from colorama import Fore

API_KEY = '<YOUR_API_KEY>'

# Get the response by sending a request to the NewsAPI
def get_response(country_code):
    url = f'https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={API_KEY}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Unauthorized access - perhaps the API key is incorrect or expired.")
        elif response.status_code == 404:
            print("The requested resource was not found.")
        elif response.status_code == 429:
            print("Too many requests - you have hit the rate limit.")
        else:
            print(f"HTTP error occured: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
    return None

# Retriving the information such as title and link of the news.  
def get_news(country):
    country_code = country[:2].lower()
    api_response = get_response(country_code)
    if api_response:
        try:
            articles = json.loads(api_response)
            if articles:
                for article in articles['articles']:
                    title = article['title']
                    url = article['url']
                    print(f'{Fore.WHITE + title}\n{Fore.RED}Link: {Fore.BLUE + url}')
                    print()
            else:
                print('No articles found.')
        except json.JSONDecodeError as e:
            print(f"Error decodeing JSON: {e}")
    else:
        print('Failed to retrive the data.')


if __name__ == '__main__':
    print(Fore.GREEN + 'Helloo, News Reader!!'+ Fore.RESET)
    input_country = input('Enter the country Name:').strip()
    print()
    if len(input_country) >= 2:
        get_news(input_country)
    else:
        print(' Please enter atleast 2 character for the country news.')

    
