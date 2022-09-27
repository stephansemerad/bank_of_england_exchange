
python -m venv venv      
venv\scripts\activat

# ----------------------------------------------------------------
python -m pip install --upgrade pip
python -m pip install beautifulsoup4
python -m pip install requests
python -m pip install sqlalchemy

# ----------------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Dec"]
url = 'https://www.bankofengland.co.uk/boeapps/database/Rates.asp?TD=2&TM=Sep&TY=2022&into=GBP&rateview=D'
result = requests.get(url)
soup = BeautifulSoup(result.content, "html.parser")


