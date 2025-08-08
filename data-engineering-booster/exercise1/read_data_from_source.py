from reader.csv_creator import CSVCreator, CSVConfig
from reader.mysql_creator import MySQLCreator, MySQLConfig

# Declare configs for source data
inventory_data_config: CSVConfig = {"file_path": "data/inventory.csv"}

customer_data_config: MySQLConfig = {
    "server": "localhost",
    "database": "mydb",
    "username": "root",
    "password": "123456",
    "query": "SELECT * FROM customer",
}

# Create Creators objects for loading and transforming data
inventory_creator = CSVCreator(inventory_data_config)
customer_creator = MySQLCreator(customer_data_config)

# Load data
inventory_df = inventory_creator.read_data()
customer_df = customer_creator.read_data()

print(inventory_df.head())
print(customer_df.head())
