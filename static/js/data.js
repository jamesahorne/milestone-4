var endpoint = '/api/graphs/data/';

$.ajax({
    method: 'GET',
    url: endpoint,
    success: function(data) {
        console.log(`var data = ${data}`);
        var tickets = JSON.parse(data);
        charts(tickets);
    },
    error: function(error_tickets) {
        console.log(error);
        console.log(error_tickets);
    }
});

// Chart.js code
function charts(tickets) {
    var urgent_tickets = [];
    for (var i = 0; i < tickets.length; i++) {
        urgent_tickets.push(tickets[i].fields.urgent);
    }
    var urgent_true = urgent_tickets.filter(Boolean).length;
    var urgent_false = urgent_tickets.length - urgent_true;
    
    var ctx = $('#urgent');
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Urgent', 'Not Urgent'], // tickets_urgent,
            datasets: [{
                label: 'Urgent',
                
                // Need to get tickets_urgent to be a number
                
                data: [urgent_true, urgent_false],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}
    

// Chart.js documentation example
// var ctx2 = document.getElementById('type').getContext('2d');
// var myChart2 = new Chart(ctx2, {
//     type: 'bar',
//     data: {
//         labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
//         datasets: [{
//             label: '# of Votes',
//             data: [7, 9, 3, 5, 2, 3],
//             backgroundColor: [
//                 'rgba(255, 99, 132, 0.2)',
//                 'rgba(54, 162, 235, 0.2)',
//                 'rgba(255, 206, 86, 0.2)',
//                 'rgba(75, 192, 192, 0.2)',
//                 'rgba(153, 102, 255, 0.2)',
//                 'rgba(255, 159, 64, 0.2)'
//             ],
//             borderColor: [
//                 'rgba(255, 99, 132, 1)',
//                 'rgba(54, 162, 235, 1)',
//                 'rgba(255, 206, 86, 1)',
//                 'rgba(75, 192, 192, 1)',
//                 'rgba(153, 102, 255, 1)',
//                 'rgba(255, 159, 64, 1)'
//             ],
//             borderWidth: 1
//         }]
//     },
//     options: {
//         scales: {
//             yAxes: [{
//                 ticks: {
//                     beginAtZero: true
//                 }
//             }]
//         }
//     }
// });
