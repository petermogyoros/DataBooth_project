"use strict";
// Class definition
var KChartJSDemo = function() {

	var demo1 = function() {
		var barChartData = {
			labels: [1, 'February', 'March', 'April', 'May', 'June', 'July'],
			datasets: [{
				label: 'Dataset 1',
				backgroundColor: '#6e4ff5',
				borderColor: '#6e4ff5',
				borderWidth: 1,
				data: [
					54,
					47,
					62,
					84,
					79,
					61,
					24
				]
			}, {
				label: 'Dataset 2',
				backgroundColor: '#f6aa33',
				borderColor: '#f6aa33',
				borderWidth: 1,
				data: [
					42,
					52,
					84,
					67,
					32,
					69,
					58
				]
			}]

		};

		var ctx = $('#k_chartjs_1');
		var myBarChart = new Chart(ctx, {
			type: 'bar',
			data: barChartData,
			options: {
				responsive: true,
				legend: {
					position: 'top',
				},
				title: {
					display: true,
					text: 'Vertical Bar Chart'
				}
			}
		});
	}

	var demo2 = function() {
		var barChartData = {
			labels: [2, 'February', 'March', 'April', 'May', 'June', 'July'],
			datasets: [{
				label: 'Dataset 1',
				backgroundColor: '#6e4ff5',
				borderColor: '#6e4ff5',
				borderWidth: 1,
				data: [
					54,
					47,
					62,
					84,
					79,
					61,
					24
				]
			}, {
				label: 'Dataset 2',
				backgroundColor: '#f6aa33',
				borderColor: '#f6aa33',
				borderWidth: 1,
				data: [
					42,
					52,
					84,
					67,
					32,
					69,
					58
				]
			}]

		};

		var ctx = $('#k_chartjs_2');
		var myBarChart = new Chart(ctx, {
			type: 'horizontalBar',
			data: barChartData,
			options: {
				responsive: true,
				legend: {
					position: 'top',
				},
				title: {
					display: true,
					text: 'Horizontal Bar Chart'
				}
			}
		});
	}

	var demo3 = function() {
		var barChartData = {
			labels: [3, 'February', 'March', 'April', 'May', 'June', 'July'],
			datasets: [{
				label: 'Dataset 1',
				backgroundColor: '#6e4ff5',
				borderColor: '#6e4ff5',
				borderWidth: 1,
				data: [
					54,
					-47,
					62,
					-84,
					-79,
					61,
					24
				]
			}, {
				label: 'Dataset 2',
				backgroundColor: '#f6aa33',
				borderColor: '#f6aa33',
				borderWidth: 1,
				data: [
					42,
					52,
					84,
					-67,
					32,
					69,
					-58
				]
			}, {
				label: 'Dataset 3',
				backgroundColor: '#fe3995',
				borderColor: '#fe3995',
				borderWidth: 1,
				data: [
					-21,
					43,
					74,
					35,
					-65,
					42,
					34
				]
			}]

		};

		var ctx = $('#k_chartjs_3');
		var myBarChart = new Chart(ctx, {
			type: 'bar',
			data: barChartData,
			options: {
				title: {
					display: true,
					text: 'Bar Chart - Stacked'
				},
				tooltips: {
					mode: 'index',
					intersect: false
				},
				responsive: true,
				scales: {
					xAxes: [{
						stacked: true,
					}],
					yAxes: [{
						stacked: true
					}]
				}
			}
		});
	}
// Data for Line's line charts
	var demo4 = function() {
		// console.log(day0)
		var barChartData = {
			labels: [period6, period5, period4, period3, period2, period1, period0],
			datasets: [{
				label: 'Side A',
				backgroundColor: '#6e4ff5',
				borderColor: '#6e4ff5',
				borderWidth: 3,
				fill: false,
				data: [
					scrap6a,
					scrap5a,
					scrap4a,
					scrap3a,
					scrap2a,
					scrap1a,
					scrap0a
				]
			}, {
				label: 'Side B',
				backgroundColor: '#f6aa33',
				borderColor: '#f6aa33',
				borderWidth: 3,
				fill: false,
				data: [
					scrap6b,
					scrap5b,
					scrap4b,
					scrap3b,
					scrap2b,
					scrap1b,
					scrap0b
				]
			}]

		};

		var ctx = $('#k_chartjs_4');
		var myBarChart = new Chart(ctx, {
			type: 'line',
			data: barChartData,
			options: {
				responsive: true,
				title: {
					display: false,
					text: 'Line Chart'
				},
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							// labelString: 'Period'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Scrap in %'
						}
					}]
				}
			}
		});
	}

	var demo5 = function() {
		var barChartData = {
			labels: [3, 'February', 'March', 'April', 'May', 'June', 'July'],
			datasets: [{
				label: 'Side A',
				backgroundColor: '#6e4ff5',
				borderColor: '#6e4ff5',
				borderWidth: 3,
				fill: false,
				data: [
					54,
					-47,
					62,
					-84,
					-79,
					61,
					24
				]
			}, {
				label: 'Side B',
				backgroundColor: '#f6aa33',
				borderColor: '#f6aa33',
				borderWidth: 3,
				borderDash: [5, 5],
				fill: false,
				data: [
					42,
					52,
					84,
					-67,
					32,
					69,
					-58
				]
			}, {
				label: 'Dataset 3',
				backgroundColor: '#fe3995',
				borderColor: '#fe3995',
				borderWidth: 3,
				fill: true,
				data: [
					-21,
					43,
					74,
					35,
					-65,
					42,
					34
				]
			}]

		};

		var ctx = $('#k_chartjs_5');
		var myBarChart = new Chart(ctx, {
			type: 'line',
			data: barChartData,
			options: {
				responsive: true,
				title: {
					display: true,
					text: 'Multi Line Chart'
				},
				tooltips: {
					mode: 'index',
					intersect: false,
				},
				hover: {
					mode: 'nearest',
					intersect: true
				},
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Month'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Value'
						}
					}]
				}
			}
		});
	}

	var demo6 = function() {

		var randomScalingFactor = function() {
			return Math.round(Math.random() * 100);
		};

		var chartData = {
			datasets: [{
				data: [
					ng_0_a,
					ng_1_a,
					ng_1_a,
					ng_1_a,
					ng_1_a,
				],
				backgroundColor: [
					'#fe3995',
					'#f6aa33',
					'#6e4ff5',
					'#2abe81',
					'#c7d2e7',
				],
				label: 'Dataset 1'
			}],
			labels: [
				'Data 1',
				'Data 2',
				'Data 3',
				'Data 4',
				'Data 5'
			]

		};

		// This is where the Donut Chart is starting from
		var ctx = $('#k_chartjs_6');
		var myBarChart = new Chart(ctx, {
			type: 'doughnut',
			data: chartData,
			options: {
				responsive: true,
				legend: {
					position: 'bottom',
				},
				title: {
					display: true,
					text: 'Rejects by Camera'
				},
				animation: {
					animateScale: true,
					animateRotate: true
				}
			}
		});
	}

	var demo7 = function() {

		var chartData = {
			datasets: [{
				data: [
					combined_scrap_0_a,
					combined_scrap_0_a,
					combined_scrap_0_a,
					combined_scrap_0_a,
					combined_scrap_0_a,
				],
				backgroundColor: [
					'#fe3995',
					'#f6aa33',
					'#6e4ff5',
					'#2abe81',
					'#c7d2e7',
				],
				label: 'Dataset 1'
			}],
			labels: [
				'0',
				'1',
				'2',
				'3',
				4
			]

		};

		var ctx = $('#k_chartjs_7');
		var myBarChart = new Chart(ctx, {
			type: 'pie',
			data: chartData,
			options: {
				responsive: true,
				legend: {
					position: 'top',
				},
				title: {
					display: true,
					text: 'Pie Chart'
				},
				animation: {
					animateScale: true,
					animateRotate: true
				}
			}
		});
	}

	var demo8 = function() {

		var randomScalingFactor = function() {
			return Math.round(Math.random() * 100);
		};

		var chartData = {
			datasets: [{
				data: [
					randomScalingFactor(),
					randomScalingFactor(),
					randomScalingFactor(),
					randomScalingFactor(),
					randomScalingFactor(),
				],
				backgroundColor: [
					'#fe3995',
					'#f6aa33',
					'#6e4ff5',
					'#2abe81',
					'#c7d2e7',
				],
				label: 'Dataset 1',
				borderWidth: [10,10,10,10,10]
			}],
			labels: [
				'Data 1',
				'Data 2',
				'Data 3',
				'Data 4',
				'Data 5'
			]
		};


	}

	return {
		// public functions
		init: function() {
			// bar charts
			demo1();
			demo2();
			demo3();

			// line charts
			demo4();
			demo5();

			// donut chart
			demo6();
			demo8();

			// pie chart
			demo7();
		}
	};
}();

jQuery(document).ready(function() {
    KChartJSDemo.init();
});
