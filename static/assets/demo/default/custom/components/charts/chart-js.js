"use strict";
// Class definition
var KChartJSDemo = function() {

	var produced_line = function() {
		var barChartData = {
			labels: [period6, period5, period4, period3, period2, period1, period0],
			datasets: [{
				label: 'Side A',
				backgroundColor: '#21964c',
				borderColor: '#21964c',
				borderWidth: 3,
				fill: false,
				data: [
					a_ok_6,
					a_ok_5,
					a_ok_4,
					a_ok_3,
					a_ok_2,
					a_ok_1,
					a_ok_0
				]
			}, {
				label: 'Side B',
				backgroundColor: '#50c47c',
				borderColor: '#50c47c',
				borderWidth: 3,
				fill: false,
				data: [
					b_ok_6,
					b_ok_5,
					b_ok_4,
					b_ok_3,
					b_ok_2,
					b_ok_1,
					b_ok_0
				]
			}]

		};

		var ctx = $('#k_chartjs_3');
		var myBarChart = new Chart(ctx, {
			type: 'line',
			data: barChartData,
			options: {
				responsive: true,
				title: {
					display: true,
					text: 'Boxed Caps'
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
						// scaleLabel: {
						// 	display: true,
							// labelString: 'Time Span'
						// }
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Number of Caps Produced'
						}
					}]
				}
			}
		});
	}


// // // // // // // // // // //
// Data for reject line charts //
// // // // // // // // // // //
	var rejects_line = function() {
		var barChartData = {
			labels: [period6, period5, period4, period3, period2, period1, period0],
			datasets: [{
				label: 'Side A',
				backgroundColor: '#ad4545',
				borderColor: '#ad4545',
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
				backgroundColor: '#ad4545',
				borderColor: '#ad4545',
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
					display: true,
					text: 'Combined Rejects'
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
							labelString: 'Time Span'
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


// // // // // // // // // // // // // // // // // //
// This is where the Donut Chart is starting from  //
// // // // // // // // // // // // // // // // // //
	var rejects_donut = function() {
		var chartData = {
			datasets: [{
				data: [
					// round results to 2 decimal places
					(ng_top_0_a).toFixed(2),
					(ng_top_0_b).toFixed(2),
					(ng_bottom_0_a).toFixed(2),
					(ng_bottom_0_b).toFixed(2),
					(ng_side_0_a).toFixed(2),
					(ng_side_0_b).toFixed(2),
				],
				backgroundColor: [
					'#00FF40',
					'#8CFF70',
					'#0040FF',
					'#68BCFF',
					'#FFBF00',
					'#FFF82A'
				],
			}],
			labels: [
				'Top A',
				'Top B',
				'Bottom A',
				'Bottom B',
				'Side A',
				'Side B'
					]

		};


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
					text: 'Per Camera'
				},
				animation: {
					animateScale: true,
					animateRotate: true
				}
			}
		});
	}


	return {
		// public functions
		init: function() {

			produced_line();
			// line charts
			rejects_line();

			// donut chart
			rejects_donut();

		}
	};
}();

jQuery(document).ready(function() {
    KChartJSDemo.init();
});
