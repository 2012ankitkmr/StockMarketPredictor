document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/stocks')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#stocks-table tbody');
            data.forEach(stock => {
                const row = document.createElement('tr');
                const price = typeof stock.price === 'number' ? stock.price.toFixed(2) : stock.price;
                row.innerHTML = `
                    <td>${stock.symbol}</td>
                    <td>${price}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching stock data:', error));
});
