# Dynamic Vending Machine v1.0


# Quick Start

1. Install requirements
2. Create MySQL database
3. Run generator.sql
4. Run Django server
5. Run PyQT client     

# Install requirements

Clone this repo and install requirements.txt in a python ≥ 3.8.0 environment    

```bash
git clone https://github.com/yeongin-ji/Algorithm-Term-Project #clone
cd Algorithm-Term-Project
pip install -r requirements.txt # install    
```    
    
# Create MySQL database

Install MySQL 8.0.35 in [this site](https://dev.mysql.com/downloads/installer/)    
    
# Run generator.sql

Create dataset by running generator.sql in your MySQL database

```bash
\sql
\connect --mysql root@localhost:3306
\source <your_path>\Algorithm-Term-Project\generator.sql
```    
    
## Database Relation

- user: Define the user information required to provide the recommended service.
- product: Defines a list of drinks sold by vending machines.
- orders: Define which users ordered which drinks.    
    
# Run Django server

Run Django Rest API server

```bash
python manage.py runserver
```    
    
# Run PyQT client

Run PyQT client and enjoy Dynamic Vending Machine!
```bash
python dvm_client.py
```    