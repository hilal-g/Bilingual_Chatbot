# Monolingual Chatbot

## Implementation

### Train the model
If model does not exist:

```
python3 train.py
```

### Run the chatbot on Terminal
```
python3 main.py
```

### Run the chatbot using GUI
```
python3 app.py
```

## Connecting to Database (Optional)

Connecting to database stores all of the responses from the user into a PostgreSQL database based on detected language. Gathering responses from users can be useful to improve the chatbot's responses. 

### 1. Create database. 
Connect to Postgres and in the terminal create the database: 

```
create database bilingual_chatbot;
```

### 2. Create table to store user queries. 
Create table 'user_queries' by running the command in the terminal: 

```
python3 create_table.py
```

### 3. Run the chatbot using GUI or on Terminal. 
To run the chatbot with GUI:

```
python3 app.py --use-database=True
```

To run the chatbot on terminal:

```
python3 main.py --use-database=True
```
