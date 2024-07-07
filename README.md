# Country-News
This repository contains python script helps us to get the fresh `NEWS` based on the countries you entered. It retrive the information with the help of 'NewsAPI'.
## Features
- Takes country name as input from the user
- Fetches the fresh news from the News website including **title** and **link** for the detailed explaination.
- It handles the various errors like JSON decoding and HTTP error while sending requests.

## Prerequisites
- Python 3.x
- `requests` library
- `colorama` library
- No need to install JSON module manually, as it comes with the python STL.
## Installation
1. Clone this repository
```cmd
https://github.com/Spandana-M-Patil/Country-News.git
```
2. Install required libraries
```cmd
pip install requests
```
```cmd
pip install colorama
```
## Usage
1. Replace <YOUR_API_KEY> with the actual api key from NewsAPI
2. Run the script
```cmd
python script.py
```
3. Enter the country name when it's prompted
## Example
```cmd
Helloo, News Reader!!
Enter the country Name:india

BSP Tamil Nadu Chief Hacked To Death By 6 Men On Bikes In Chennai - NDTV
Link: https://www.ndtv.com/india-news/bsp-tamil-nadu-chief-hacked-to-death-by-6-men-on-bikes-in-chennai-6042943

CMF Watch Pro 2 with detachable bezels teased ahead of its launch: What to expect - Moneycontrol
Link: https://www.moneycontrol.com/technology/cmf-watch-pro-2-with-detachable-bezels-teased-ahead-of-its-launch-what-to-expect-article-12763403.html

Venezuela vs Canada highlights, VEN 1-1 CAN, Copa America 2024: Les Rogues win penalty shootout (4-3) to make maiden semifinals - Sportstar
Link: https://sportstar.thehindu.com/football/venezuela-vs-canada-live-match-updates-score-highlights-copa-america-2024-quarterfinal-ven-v-can/article68373756.ece
.....
.....
```
## Conclusion
It helps us to be updated with current news across the country upon entering the country name.
I'm very greatful for the NewsAPI for providing an API, that helped me to make this project.
