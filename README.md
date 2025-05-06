# Expense Calculator

A web application for calculating and tracking monthly expenses.

## Features

- Add new expenses with category and amount
- View all expenses in a table format
- Calculate total monthly expenses
- Calculate average daily expenses
- Display top 3 largest expenses
- Delete individual expenses
- Responsive design for all devices

## How to Use

1. Open `index.html` in your web browser
2. Add new expenses using the form:
   - Enter the expense category (e.g., Groceries, Rent)
   - Enter the amount in dollars
   - Click "Add Expense"
3. View your expenses in the table below
4. The summary section will automatically update with:
   - Total amount of expenses
   - Average daily expense (calculated based on 30 days)
   - Top 3 largest expenses
5. To delete an expense, click the "Delete" button next to the expense

## Technical Details

- Built with vanilla JavaScript, HTML, and CSS
- No external dependencies required
- Responsive design using modern CSS
- Currency formatting using Intl.NumberFormat
- Data stored in memory (resets on page refresh)

## Example Usage

Add the following expenses:
- Groceries: $15,000
- Rent: $40,000
- Transportation: $5,000
- Entertainment: $10,000
- Communication: $2,000
- Gym: $3,000

The application will show:
- Total Expenses: $75,000
- Average Daily Expense: $2,500
- Top 3 Expenses:
  1. Rent: $40,000
  2. Groceries: $15,000
  3. Entertainment: $10,000