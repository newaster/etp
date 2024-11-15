

$(function() {
    "use strict";



var bardict3 = document.getElementById('flowc').value;
const jsonData = JSON.parse(bardict3.replace(/'/g, "\""));

//console.log(jsonData)

var a = new Date(jsonData.date[0]);

var today = new Date();

var result1;
var result2;

if (today.toDateString() === a.toDateString()) {

    console.log(today);
    console.log(a);
    result1 = ['data1',100];
    result2 = ['data2', 0];
} else {
    result1 = ['data1',0];
    result2 = ['data2', 100];
}

//console.log(result);

    setTimeout(function(){ 
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-employment', // id of chart wrapper   
                data: {
                    columns: [
                        // each columns data
                        ['data1', jsonData.itpr[0], jsonData.itpr[1], jsonData.itpr[2], jsonData.itpr[3], jsonData.itpr[4], jsonData.itpr[5]],
                        ['data2', jsonData.stpr[0], jsonData.stpr[1], jsonData.stpr[2], jsonData.stpr[3], jsonData.stpr[4], jsonData.stpr[5]],
                        ['data3', jsonData.blwr[0], jsonData.blwr[1], jsonData.blwr[2], jsonData.blwr[3], jsonData.blwr[4], jsonData.blwr[5]]
                    ],
                    type: 'line', // default type of chart
                    colors: {
                        'data1': Aero.colors["cyan"],
                        'data2': Aero.colors["blue"],
                        'data3': Aero.colors["green"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'ITP',
                        'data2': 'STP',
                        'data3': 'BLOWER'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: jsonData.date
                    },
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-temperature', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6],
                        ['data2', 3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
                    ],
                    labels: true,
                    type: 'line', // default type of chart
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Tokyo',
                        'data2': 'London'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-area', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 11, 8, 15, 18, 19, 17],
                        ['data2', 7, 7, 5, 7, 9, 12]
                    ],
                    type: 'area', // default type of chart
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Maximum',
                        'data2': 'Minimum'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-area-spline', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 11, 8, 15, 18, 19, 17],
                        ['data2', 7, 7, 5, 7, 9, 12]
                    ],
                    type: 'area-spline', // default type of chart
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Maximum',
                        'data2': 'Minimum'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-area-spline-sracked', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 11, 8, 15, 18, 19, 17],
                        ['data2', 7, 7, 5, 7, 9, 12]
                    ],
                    type: 'area-spline', // default type of chart
                    groups: [
                        [ 'data1', 'data2']
                    ],
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Maximum',
                        'data2': 'Minimum'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-spline', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 0.2, 0.8, 0.8, 0.8, 1, 1.3, 1.5, 2.9, 1.9, 2.6, 1.6, 3, 4, 3.6, 4.5, 4.2, 4.5, 4.5, 4, 3.1, 2.7, 4, 2.7, 2.3, 2.3, 4.1, 7.7, 7.1, 5.6, 6.1, 5.8, 8.6, 7.2, 9, 10.9, 11.5, 11.6, 11.1, 12, 12.3, 10.7, 9.4, 9.8, 9.6, 9.8, 9.5, 8.5, 7.4, 7.6],
                        ['data2', 0, 0, 0.6, 0.9, 0.8, 0.2, 0, 0, 0, 0.1, 0.6, 0.7, 0.8, 0.6, 0.2, 0, 0.1, 0.3, 0.3, 0, 0.1, 0, 0, 0, 0.2, 0.1, 0, 0.3, 0, 0.1, 0.2, 0.1, 0.3, 0.3, 0, 3.1, 3.1, 2.5, 1.5, 1.9, 2.1, 1, 2.3, 1.9, 1.2, 0.7, 1.3, 0.4, 0.3]
                    ],
                    labels: true,
                    type: 'spline', // default type of chart
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Hestavollane',
                        'data2': 'Vik'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-spline-rotated', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 11, 8, 15, 18, 19, 17],
                        ['data2', 7, 7, 5, 7, 9, 12]
                    ],
                    type: 'spline', // default type of chart
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Maximum',
                        'data2': 'Minimum'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                    rotated: true,
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-step', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 11, 8, 15, 18, 19, 17],
                        ['data2', 7, 7, 5, 7, 9, 12]
                    ],
                    type: 'step', // default type of chart
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Maximum',
                        'data2': 'Minimum'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
       
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-bar', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 11, 8, 15, 18, 19, 17],
                        ['data2', 7, 7, 5, 7, 9, 12]
                    ],
                    type: 'bar', // default type of chart
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Maximum',
                        'data2': 'Minimum'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                },
                bar: {
                    width: 16
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-bar-rotated', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 11, 8, 15, 18, 19, 17],
                        ['data2', 7, 7, 5, 7, 9, 12]
                    ],
                    type: 'bar', // default type of chart
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Maximum',
                        'data2': 'Minimum'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                    rotated: true,
                },
                bar: {
                    width: 16
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-bar-stacked', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 11, 8, 15, 18, 19, 17],
                        ['data2', 7, 7, 5, 7, 9, 12]
                    ],
                    type: 'bar', // default type of chart
                    groups: [
                        [ 'data1', 'data2']
                    ],
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Maximum',
                        'data2': 'Minimum'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                },
                bar: {
                    width: 30,
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-pie', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 63],
                        ['data2', 44],
                        ['data3', 12],
                        ['data4', 14]
                    ],
                    type: 'pie', // default type of chart
                    colors: {
                        'data1': Aero.colors["blue-darker"],
                        'data2': Aero.colors["blue"],
                        'data3': Aero.colors["blue-light"],
                        'data4': Aero.colors["blue-lighter"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'A',
                        'data2': 'B',
                        'data3': 'C',
                        'data4': 'D'
                    }
                },
                axis: {
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-donut', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        result1,
                        result2
                    ],
                    type: 'donut', // default type of chart
                    colors: {
                        'data1': Aero.colors["green"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Online',
                        'data2': 'Offline'
                    }
                },
                axis: {
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-scatter', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 11, 8, 15, 18, 19, 17],
                        ['data2', 7, 7, 5, 7, 9, 12]
                    ],
                    type: 'scatter', // default type of chart
                    colors: {
                        'data1': Aero.colors["blue"],
                        'data2': Aero.colors["cyan"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Maximum',
                        'data2': 'Minimum'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
                    },
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-combination', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 30, 20, 50, 40, 60, 50],
                        ['data2', 200, 130, 90, 240, 130, 220],
                        ['data3', 300, 200, 160, 400, 250, 250],
                        ['data4', 200, 130, 90, 240, 130, 220]
                    ],
                    type: 'bar', // default type of chart
                    types: {
                        'data2': "line",
                        'data3': "spline",
                    },
                    groups: [
                        [ 'data1', 'data4']
                    ],
                    colors: {
                        'data1': Aero.colors["cyan"],
                        'data2': Aero.colors["indigo"],
                        'data3': Aero.colors["green"],
                        'data4': Aero.colors["blue"]
                    },
                    names: {
                        // name of each serie
                        'data1': 'Development',
                        'data2': 'Marketing',
                        'data3': 'Sales',
                        'data4': 'Sales'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['2013', '2014', '2015', '2016', '2019', '2018']
                    },
                },
                bar: {
                    width: 30,
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0
                },
            });
        });
    }, 500);
});