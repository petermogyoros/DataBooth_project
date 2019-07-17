
// Class definition
var KDashboard = function() {

// double bar chart script
    var DG_Dashboard_Chart = function() {
        if (!document.getElementById('k_chart_sales_statistics')) {
            return;
        }

        var color = Chart.helpers.color;
        var barChartData = {
            labels: ['Line 3', 'Line 4', 'Line 5', 'Line 7', 'Line 8', 'Line 9', 'Line 10'],
            datasets: [{
                label: 'Side A',
                backgroundColor: color(KApp.getStateColor('brand')).alpha(1).rgbString(),
                borderWidth: 0,
                data: [a3, a4, a5, a7, a8, a9, a10]
            }, {
                label: 'Side B',
                backgroundColor: color(KApp.getStateColor('primary', 1)).alpha(1).rgbString(),
                borderWidth: 0,
                data: [b3, b4, b5, b7, b8, b9, b10]
            }]
        };

        var ctx = document.getElementById('k_chart_sales_statistics').getContext('2d');
        var myBar = new Chart(ctx, {
            type: 'bar',
            data: barChartData,
            options: {
                responsive: true,
                maintainAspectRatio: false,
                legend: false,
                scales: {
                    xAxes: [{
                        categoryPercentage: 0.35,
                        barPercentage: 0.70,
                        display: true,
                        scaleLabel: {
                            display: false,
                            labelString: 'Month'
                        },
                        gridLines: false,
                        ticks: {
                            display: true,
                            beginAtZero: true,
                            fontColor: KApp.getBaseColor('shape', 4),
                            fontSize: 13,
                            padding: 10
                        }
                    }],
                    yAxes: [{
                        categoryPercentage: 0.75,
                        barPercentage: 0.70,
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: '%'
                        },
                        gridLines: {
                            color: KApp.getBaseColor('shape', 3),
                            drawBorder: false,
                            offsetGridLines: false,
                            drawTicks: false,
                            borderDash: [3, 4],
                            zeroLineWidth: 1,
                            zeroLineColor: KApp.getBaseColor('shape', 2),
                            zeroLineBorderDash: [3, 4]
                        },
                        ticks: {
                            max: 25,
                            stepSize: 5,
                            display: true,
                            beginAtZero: true,
                            fontColor: KApp.getBaseColor('shape', 3),
                            fontSize: 18,
                            padding: 10
                        }
                    }]
                },
                title: {
                    display: true
                },
                hover: {
                    mode: 'index'
                },
                tooltips: {
                    enabled: true,
                    intersect: false,
                    mode: 'nearest',
                    bodySpacing: 5,
                    yPadding: 10,
                    xPadding: 10,
                    caretPadding: 0,
                    displayColors: false,
                    backgroundColor: KApp.getStateColor('brand'),
                    titleFontColor: '#ffffff',
                    cornerRadius: 4,
                    footerSpacing: 0,
                    titleSpacing: 0
                },
                layout: {
                    padding: {
                        left: 0,
                        right: 0,
                        top: 5,
                        bottom: 5
                    }
                }
            }
        });
    }




    return {
        init: function() {
            DG_Dashboard_Chart();
        }
    };
}();

// Class initialization
jQuery(document).ready(function() {
    KDashboard.init();
});
