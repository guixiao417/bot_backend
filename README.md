
###
Activate virtualenv
`.\venv\Scripts\activate.bat`


### Bot Backend
`Get data from crwaler and save it to db`


#### Development Mode
    + ngrok http -host-header="0.0.0.0:8000" 8000

#### Production Mode
    + Establish backend on heroku
    + host: https://bot-backend-01.herokuapp.com
    
    
#### NLTK error
If you get error in getting job like below
```
 Resource [93mpunkt[0m not found.
  Please use the NLTK Downloader to obtain the resource:
```

 You should use below command to solve that
`python -c "import nltk; nltk.download('punkt')"`
    