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

var options = {
    scales: {
        yAxes: [{
            ticks: {
                beginAtZero: true,
                fontColor: 'white'
            },
            gridLines: {
                display: false,
                color: 'white'
            }
        }],
        xAxes: [{
            ticks: {
                beginAtZero: true,
                fontColor: 'white'
            },
            gridLines: {
                display: false,
                color: 'white'
            }
        }]
    },
    legend: {
        display: false
    }
};

var backgroundColorWhite = [
    'rgba(255, 255, 255, 0.2)',
    'rgba(255, 255, 255, 0.2)'
];

var borderColorWhite = [
    'rgba(255, 255, 255, 1)',
    'rgba(255, 255, 255, 1)'
];

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
                label: 'Status',
                data: [todo_count, doing_count, done_count],
                backgroundColor: [
                    'rgba(255, 255, 255, 0.2)',
                    'rgba(255, 255, 255, 0.2)',
                    'rgba(255, 255, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 255, 255, 1)',
                    'rgba(255, 255, 255, 1)',
                    'rgba(255, 255, 255, 1)'
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
        type: 'horizontalBar',
        data: {
            labels: ['Bug', 'Feature'],
            datasets: [{
                label: 'Type',
                data: [bug_count, feature_count],
                backgroundColor: backgroundColorWhite,
                borderColor: borderColorWhite,
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
                backgroundColor: backgroundColorWhite,
                borderColor: borderColorWhite,
                borderWidth: 1
            }]
        },
        options: options
    });
}
