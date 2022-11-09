# :dart: ETHSF-scorebox-backend
Python credit scoring model ft. [Covalent HQ](https://www.covalenthq.com/) and a self-built off-chain encryptor.


### :package: Requirements
Install necessary Python modules
```bash
pip install -r requirements.txt
```

### :open_file_folder: Environment Variables
Create an `.env` file
```bash
# basic
DATABASE_URL=url_of_database
COVALENT_KEY=covalent_api_key
ETH_ADDRESS=your_metamask_wallet_address
COINMARKETCAP_KEY=coinmarketcap_api_key

# for PUSH notification
db_table=postgres_table_name
host=postgres_host_name
dbname=postgres_database_name
user=postgres_user_name
password=postgres_database_password
push_url_update=push_notification_url
push_url_leaderboard=push_notification_leaderboard
```
> :bulb: If you depoy this Python backend as an Heroku app, then you can spin up a Heroku postgres database and use those database's credentials.

### :hammer_and_wrench: Test on Swagger
Test API endpoints on Swagger passing a payload into the request body and simulating a response
```bash
uvicorn main:app --reload
```
