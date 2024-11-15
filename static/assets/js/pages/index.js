﻿//[custom Javascript]
//Project:  Aero - Responsive Bootstrap 4 Template
//Version:  1.0
//Last change:  15/12/2019
//Primary use:  Aero - Responsive Bootstrap 4 Template
//should be included in all pages. It controls some layout
$(function() {
    "use strict";
    initSparkline();
    initC3Chart();    
});


var bardict3 = document.getElementById('flowc').value;
const jsonData = JSON.parse(bardict3.replace(/'/g, "\""));


var a = document.getElementById('flowc2').value;

var validJSON = a.replace(/'/g, "\"");
var jso = JSON.parse(validJSON);


function initSparkline() {
    $(".sparkline").each(function() {
        var $this = $(this);
        $this.sparkline('html', $this.data());
    });
}
function initC3Chart() {
    setTimeout(function(){ 
        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-area-spline-sracked', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', 21, 8, 32, 18, 19, 17, 23, 12, 25, 37],
                        ['data2', 7, 11, 5, 7, 9, 16, 15, 23, 14, 55],
                        ['data3', 13, 7, 9, 15, 9, 31, 8, 27, 42, 18],
                    ],
                    type: 'area-spline', // default type of chart
                    groups: [
                        [ 'data1', 'data2', 'data3']
                    ],
                    colors: {
                        'data1': Aero.colors["gray"],
                        'data2': Aero.colors["teal"],
                        'data3': Aero.colors["lime"],
                    },
                    names: {
                        // name of each serie
                        'data1': 'Revenue',
                        'data2': 'Returns',
                        'data3': 'Queries',
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        // name of each category
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sept', 'Oct']
                    },
                },
                legend: {
                    show: true, //hide legend
                },
                padding: {
                    bottom: 0,
                    top: 0,
                },
            });
        });


$(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-area-step',
                data: {
                    columns: [
                        ['data1', jsonData.fv[0], jsonData.fv[1], jsonData.fv[2], jsonData.fv[3], jsonData.fv[4], jsonData.fv[5]]
                    ],
                    type: 'area-step',
                    colors: {
                        'data1': 'blue'
                    },
                    names: {
                        'data1': 'Inlet Flow Rate'
                    }
                },
                axis: {
                    x: {
                        type: 'category',
                        categories: jsonData.date
                    }
                },
                legend: {
                    show: true
                },
                padding: {
                    bottom: 0,
                    top: 0
                }
            });
        });



        $(document).ready(function(){
            var chart = c3.generate({
                bindto: '#chart-pie1', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', jso.sum_value1/(jso.sum_value1+jso.sum_value2)],
                        ['data2', jso.sum_value2/(jso.sum_value1+jso.sum_value2)],
                    ],
                    type: 'pie', // default type of chart
                    colors: {
                        'data1': Aero.colors["lime"],
                        'data2': Aero.colors["teal"],
                    },
                    names: {
                        // name of each serie
                        'data1': 'ITP1',
                        'data2': 'ITP2',
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
                bindto: '#chart-pie2', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', jso.sum_value5/(jso.sum_value5+jso.sum_value6)],
                        ['data2', jso.sum_value6/(jso.sum_value5+jso.sum_value6)],
                    ],
                    type: 'pie', // default type of chart
                    colors: {
                        'data1': Aero.colors["lime"],
                        'data2': Aero.colors["teal"],
                    },
                    names: {
                        // name of each serie
                        'data1': 'STP1',
                        'data2': 'STP2',
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
                bindto: '#chart-pie3', // id of chart wrapper
                data: {
                    columns: [
                        // each columns data
                        ['data1', jso.sum_value3/(jso.sum_value3+jso.sum_value4)],
                        ['data2', jso.sum_value4/(jso.sum_value3+jso.sum_value4)],
                    ],
                    type: 'pie', // default type of chart
                    colors: {
                        'data1': Aero.colors["lime"],
                        'data2': Aero.colors["teal"],
                    },
                    names: {
                        // name of each serie
                        'data1': 'FFP1',
                        'data2': 'FFP2',
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
}, 500);
}
setTimeout(function(){
    "use strict";
    var mapData = {
        "US": 298,
        "SA": 200,
        "AU": 760,
        "IN": 2000000,
        "GB": 120,        
    };  
    if( $('#world-map-markers').length > 0 ){
        $('#world-map-markers').vectorMap({
            map: 'world_mill_en',
            backgroundColor: 'transparent',
            borderColor: '#fff',
            borderOpacity: 0.25,
            borderWidth: 0,
            color: '#e6e6e6',
            regionStyle : {
                initial : {
                fill : '#f4f4f4'
                }
            },

            markerStyle: {
            initial: {
                        r: 5,
                        'fill': '#fff',
                        'fill-opacity':1,
                        'stroke': '#000',
                        'stroke-width' : 1,
                        'stroke-opacity': 0.4
                    },
                },
        
            markers : [{
                latLng : [26.76, 83.37],
                name : 'INDIA : 350'
            
            },
            {
                latLng : [-33.00, 151.00],
                name : 'Australia : 250'
                
            },
            {
                latLng : [36.77, -119.41],
                name : 'USA : 250'
            
            },
            {
                latLng : [55.37, -3.41],
                name : 'UK   : 250'
            
            },
            {
                latLng : [25.20, 55.27],
                name : 'UAE : 250'
            
            }],

            series: {
                regions: [{
                    values: {
                        "US": '#49c5b6',
                        "SA": '#667add',
                        "AU": '#50d38a',
                        "IN": '#60bafd',
                        "GB": '#ff758e',
                    },
                    attribute: 'fill'
                }]
            },
            hoverOpacity: null,
            normalizeFunction: 'linear',
            zoomOnScroll: false,
            scaleColors: ['#000000', '#000000'],
            selectedColor: '#000000',
            selectedRegions: [],
            enableZoom: false,
            hoverColor: '#fff',
        });
    }
}, 800);