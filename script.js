// Store expenses in an array
let expenses = [];

// DOM Elements
const expenseForm = document.getElementById('expenseForm');
const expensesList = document.getElementById('expensesList');
const totalAmountElement = document.getElementById('totalAmount');
const averageDailyElement = document.getElementById('averageDaily');
const topExpensesElement = document.getElementById('topExpenses');

// Event Listeners
expenseForm.addEventListener('submit', handleFormSubmit);

// Functions
function handleFormSubmit(e) {
    e.preventDefault();
    
    const category = document.getElementById('category').value.trim();
    const amount = parseFloat(document.getElementById('amount').value);
    
    if (category && amount) {
        addExpense(category, amount);
        updateUI();
        expenseForm.reset();
    }
}

function addExpense(category, amount) {
    expenses.push({ category, amount });
}

function deleteExpense(index) {
    expenses.splice(index, 1);
    updateUI();
}

function calculateTotal() {
    return expenses.reduce((total, expense) => total + expense.amount, 0);
}

function calculateAverageDaily() {
    const total = calculateTotal();
    return total / 30; // Assuming 30 days in a month
}

function getTopExpenses() {
    return [...expenses]
        .sort((a, b) => b.amount - a.amount)
        .slice(0, 3);
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(amount);
}

function updateUI() {
    // Update expenses table
    expensesList.innerHTML = expenses.map((expense, index) => `
        <tr>
            <td>${expense.category}</td>
            <td>${formatCurrency(expense.amount)}</td>
            <td>
                <button class="delete-btn" onclick="deleteExpense(${index})">Delete</button>
            </td>
        </tr>
    `).join('');

    // Update total amount
    const total = calculateTotal();
    totalAmountElement.textContent = formatCurrency(total);

    // Update average daily expense
    const averageDaily = calculateAverageDaily();
    averageDailyElement.textContent = formatCurrency(averageDaily);

    // Update top 3 expenses
    const topExpenses = getTopExpenses();
    topExpensesElement.innerHTML = topExpenses.map(expense => `
        <li>${expense.category}: ${formatCurrency(expense.amount)}</li>
    `).join('');
}

// Initialize UI
updateUI(); 