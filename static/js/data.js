"use strict";

var endpoint = '/api/graphs/data/';

$.ajax({
    method: 'GET',
    url: endpoint,
    success: function(data) {
        var tickets = JSON.parse(data);
        charts(tickets);
    },
});

var options = {scales: {yAxes: [{ticks: {beginAtZero: true}}]}};


// Make bar colors all white? Then make var backgroundColor and var borderColor

// Should each chart be in a separate function and not all in charts()?


function charts(tickets) {
    var ticket_statuses = [];
    for (var i = 0; i < tickets.length; i++) {
        ticket_statuses.push(tickets[i].fields.status);
    }
    var todo_count = ticket_statuses.filter(status => status === 'Todo').length;
    var doing_count = ticket_statuses.filter(status => status === 'Doing').length;
    var done_count = ticket_statuses.filter(status => status === 'Done').length;
    var ctx = $('#status');
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Todo', 'Doing', 'Done'],
            datasets: [{
                label: 'Type',
                data: [todo_count, doing_count, done_count],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            grid: false
        }
    });

    var ticket_types = [];
    for (var i = 0; i < tickets.length; i++) {
        ticket_types.push(tickets[i].fields.type);
    }
    var bug_count = ticket_types.filter(type => type === 'Bug').length;
    var feature_count = ticket_types.length - bug_count;
    var ctx1 = $('#type');
    var myChart = new Chart(ctx1, {
        type: 'bar',
        data: {
            labels: ['Bug', 'Feature'],
            datasets: [{
                label: 'Type',
                data: [bug_count, feature_count],
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
        options: options
    });

    var ticket_urgencies = [];
    for (var i = 0; i < tickets.length; i++) {
        ticket_urgencies.push(tickets[i].fields.urgent);
    }
    var is_urgent_count = ticket_urgencies.filter(Boolean).length;
    var not_urgent_count = ticket_urgencies.length - is_urgent_count;
    var ctx2 = $('#urgent');
    var myChart = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: ['Urgent', 'Not Urgent'],
            datasets: [{
                label: 'Urgency',
                data: [is_urgent_count, not_urgent_count],
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
        options: options
    });
}
