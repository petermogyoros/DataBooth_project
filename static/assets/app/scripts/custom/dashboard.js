//
// Dashboard
//



// Class definition
var KDashboard = function() {

// double bar chart script
    var DG_Dashboard_Chart = function() {
        if (!document.getElementById('k_chart_sales_statistics')) {
            return;
        }

        // var MONTHS = ['1 Aug', '2 Aug', '3 Aug', '4 Aug', '5 Aug', '6 Aug', '7 Aug'];

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
                            display: false,
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
                            max: 40,
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
                    display: false
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


    var recentOrdersInit = function() {
        if ($('#k_recent_orders').length === 0) {
            return;
        }

        var datatable = $('#k_recent_orders').KDatatable({
            // datasource definition
            data: {
                type: 'remote',
                source: {
                    read: {
                        url: 'https://keenthemes.com/keen/themes/themes/keen/dist/preview/inc/api/datatables/demos/default.php',
                    },
                },
                pageSize: 10,
                serverPaging: true,
                serverFiltering: true,
                serverSorting: true
            },

            // layout definition
            layout: {
                scroll: true,
                footer: false,
                height: 430
            },

            // column sorting
            sortable: true,

            pagination: true,

            search: {
                input: $('#generalSearch'),
            },

            // columns definition
            columns: [{
                field: 'id',
                title: '#',
                sortable: false,
                width: 20,
                type: 'number',
                selector: {class: 'k-checkbox--solid k-checkbox--brand'},
                textAlign: 'center',
            }, {
                field: 'employee_id',
                title: 'Order ID',
                template: function(row) {
                    return '<span class="k-label-font-color-3 k-font-bold">' + row.employee_id + '</span>';
                },
            }, {
                field: 'name',
                title: 'Customer',
                width: 130,
                template: function(row) {
                    return '<span class="k-label-font-color-3 k-font-bold">' + row.first_name + ' ' + row.last_name + '</span>';
                },
            }, {
                field: 'hire_date',
                title: 'Date',
                type: 'date',
                format: 'MM/DD/YYYY',
            }, {
                field: 'status',
                title: 'Status',
	            autoHide: false,
                // callback function support for column rendering
                template: function(row) {
                    var status = {
                        1: {
                            'title': 'Pending',
                            'class': 'brand'
                        },
                        2: {
                            'title': 'Delivered',
                            'class': 'focus'
                        },
                        3: {
                            'title': 'Canceled',
                            'class': 'primary'
                        },
                        4: {
                            'title': 'Success',
                            'class': 'success'
                        },
                        5: {
                            'title': 'Info',
                            'class': 'info'
                        },
                        6: {
                            'title': 'Danger',
                            'class': 'danger'
                        },
                        7: {
                            'title': 'Warning',
                            'class': 'warning'
                        }
                    };
                    return '<span class="k-badge k-badge--' + status[row.status].class + ' k-badge--dot k-badge--md"></span>&nbsp;&nbsp;<span class="k-label-font-color-2 k-font-bold">' +
                        status[row.type].title + '</span>';
                }
            }, {
                field: 'Actions',
                title: 'Actions',
                sortable: false,
                width: 80,
                overflow: 'visible',
                textAlign: 'center',
	            autoHide: false,
                template: function() {
                    return '\
                        <div class="dropdown" >\
                            <a href="#" class="btn btn-clean btn-icon btn-sm btn-icon-md" data-toggle="dropdown">\
                                <i class="la la-ellipsis-h"></i>\
                            </a>\
                            <div class="dropdown-menu dropdown-menu-right">\
                                <a class="dropdown-item" href="#"><i class="la la-edit"></i> Edit Details</a>\
                                <a class="dropdown-item" href="#"><i class="la la-leaf"></i> Update Status</a>\
                                <a class="dropdown-item" href="#"><i class="la la-print"></i> Generate Report</a>\
                            </div>\
                        </div>\
                        <a href="#" class="btn btn-clean btn-icon btn-sm btn-icon-md" title="Edit details">\
                            <i class="la la-edit"></i>\
                        </a>\
                    ';
                }
            }]
        });
    };

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
