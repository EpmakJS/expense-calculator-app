# SQL Analysis Project

This project contains SQL queries to analyze sales data for an online store using SQLite.

## Project Structure

- `setup.sql`: Contains the table creation and sample data insertion scripts
- `analysis.sql`: Contains the analysis queries for the given tasks

## Database Schema

The project uses a single table called `orders` with the following structure:

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    amount REAL,
    order_date DATE
);
```

## Analysis Tasks

The project includes three main analysis tasks:

1. Calculate the total sales volume for March 2024
   - Expected result: 27,000

2. Find the customer who spent the most overall
   - Expected result: Alice (20,000)

3. Calculate the average order value for the last three months
   - Expected result: 6,000

## How to Use

1. Open SQLite Online or your preferred SQLite environment
2. Run the contents of `setup.sql` to create and populate the database
3. Run the queries from `analysis.sql` to perform the analysis

## Sample Data

The database is populated with the following sample data:

- Alice's orders: 5,000 (Mar 1), 3,000 (Mar 15), 10,000 (Feb 28), 2,000 (Mar 30)
- Bob's orders: 8,000 (Mar 5), 4,000 (Feb 10)
- Charlie's orders: 7,000 (Feb 20), 9,000 (Mar 22) 