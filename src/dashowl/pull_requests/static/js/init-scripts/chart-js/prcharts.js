( function ( $ ) {
    "use strict";

    //Team chart
    var ctx = document.getElementById( "team-chart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "Sprint 1", "Sprint 2", "Sprint 3", "Sprint 4", "Sprint 5", "Sprint 6", "Sprint 7" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                data: [ 0, 7, 3, 5, 2, 10, 7 ],
                label: "Expense",
                backgroundColor: 'rgba(0,103,255,.15)',
                borderColor: '#b7b7b7',
                borderWidth: 3.5,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: '#b7b7b7',
                    }, ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
            },
            legend: {
                display: false,
                position: 'top',
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                },


            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Month'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false
                    }
                        } ]
            },
            title: {
                display: false,
            }
        }
    } );


    //Sales chart
    var ctx = document.getElementById( "sales-chart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul" ],
            type: 'line',
            defaultFontFamily: 'Montserrat',
            datasets: [ {
                label: "int1",
                data: [ 1, 3, 2, 4, 1, 3, 3],
                backgroundColor: 'transparent',
                borderColor: '#ff9900',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: '#ff9900',
                    }, {
                label: "int2",
                data: [ 2, 1, 3, 4, 3, 1, 4],
                backgroundColor: 'transparent',
                borderColor: '#434343',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: '#434343',
                    }, {
                
                label: "int3",
                data: [ 0, 2, 1, 5, 3, 2, 7],
                backgroundColor: 'transparent',
                borderColor: '#ff0000',
                borderWidth: 3,
                pointStyle: 'circle',
                pointRadius: 5,
                pointBorderColor: 'transparent',
                pointBackgroundColor: '#ff0000',        
                    } ]
        },
        options: {
            responsive: true,

            tooltips: {
                mode: 'index',
                titleFontSize: 12,
                titleFontColor: '#000',
                bodyFontColor: '#000',
                backgroundColor: '#fff',
                titleFontFamily: 'Montserrat',
                bodyFontFamily: 'Montserrat',
                cornerRadius: 3,
                intersect: false,
            },
            legend: {
                display: false,
                labels: {
                    usePointStyle: true,
                    fontFamily: 'Montserrat',
                },
            },
            scales: {
                xAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false,
                        labelString: 'Dayli'
                    }
                        } ],
                yAxes: [ {
                    display: true,
                    gridLines: {
                        display: false,
                        drawBorder: false
                    },
                    scaleLabel: {
                        display: false
                    }
                        } ]
            },
            title: {
                display: false,
                text: 'Normal Legend'
            }
        }
    } );

    /*
    //line chart
    var ctx = document.getElementById( "lineChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'line',
        data: {
            labels: [ "January", "February", "March", "April", "May", "June", "July" ],
            datasets: [
                {
                    label: "My First dataset",
                    borderColor: "#b7b7b7",
                    borderWidth: "1",
                    backgroundColor: "rgba(0,103,255,.15)",
                    data: [ 22, 44, 67, 43, 76, 45, 12 ]
                            },
                {
                    label: "My Second dataset",
                    borderColor: "#ff9900",
                    borderWidth: "1",
                    backgroundColor: "#f9cb9c",
                    pointHighlightStroke: "#ff9900",
                    data: [ 16, 32, 18, 26, 42, 33, 44 ]
                            }
                        ]
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                intersect: false
            },
            hover: {
                mode: 'nearest',
                intersect: true
            }

        }
    } ); */

    var cod_10o = document.getElementById("10o").getAttribute("data-produto");
    var cod_11o = document.getElementById("11o").getAttribute("data-produto");
    var cod_12o = document.getElementById("12o").getAttribute("data-produto");

    var cod_10c = document.getElementById("10c").getAttribute("data-produto");
    var cod_11c = document.getElementById("11c").getAttribute("data-produto");
    var cod_12c = document.getElementById("12c").getAttribute("data-produto");
    
        alert("Produto passado: " + cod_10c + ", " + cod_11c + ", " + cod_12c);

    //bar chart
    var ctx = document.getElementById( "barChart" );
    //   ctx.height = 200;
    var myChart = new Chart( ctx, {
        type: 'bar',
        data: {
            labels: [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ],
            datasets: [
                {
                    label: "Opened",
                    data: [1, 7, 9, 5, 13, 8, 9, 1, 2, cod_10o, cod_11o, cod_12o],
                    borderColor: "#ff0000",
                    borderWidth: "0",
                    backgroundColor: "#ff0000"
                            },
                {
                    label: "Closed",
                    data: [11, 7, 8, 5, 12, 2, 0, 1, 2, cod_10c, cod_11c, cod_12c],
                    borderColor: '#434343',
                    borderWidth: "0",
                    backgroundColor: "#434343"
                            }
                        ]
        },
        options: {
            scales: {
                yAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            },
            legend: {
                position: 'top'
            }
        }
    } );

    /*
    //radar chart
    var ctx = document.getElementById( "radarChart" );
    ctx.height = 160;
    var myChart = new Chart( ctx, {
        type: 'radar',
        data: {
            labels: [ [ "Eating", "Dinner" ], [ "Drinking", "Water" ], "Sleeping", [ "Designing", "Graphics" ], "Coding", "Cycling", "Running" ],
            datasets: [
                {
                    label: "My First dataset",
                    data: [ 65, 59, 66, 45, 56, 55, 40 ],
                    borderColor: "rgba(0, 123, 255, 0.6)",
                    borderWidth: "1",
                    backgroundColor: "rgba(0, 123, 255, 0.4)"
                            },
                {
                    label: "My Second dataset",
                    data: [ 28, 12, 40, 19, 63, 27, 87 ],
                    borderColor: "rgba(0, 123, 255, 0.7",
                    borderWidth: "1",
                    backgroundColor: "rgba(0, 123, 255, 0.5)"
                            }
                        ]
        },
        options: {
            legend: {
                position: 'top'
            },
            scale: {
                ticks: {
                    beginAtZero: true
                }
            }
        }
    } ); */

    //Circle chart
    var ctx = document.getElementById( "circleChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'doughnut',
        data: {
            datasets: [ {
                data: [ 45, 25, 20, 10 ],
                backgroundColor: [
                                    "#ff9900",
                                    "#434343",
                                    "#ff0000",
                                    "#b7b7b7"
                                ],
                hoverBackgroundColor: [
                                    "#ff9900",
                                    "#434343",
                                    "#ff0000",
                                    "#b7b7b7"
                                ]

                            } ],
            labels: [
                            "Sprint 1",
                            "Sprint 2",
                            "Sprint 3",
                            "Sprint 4"
                        ]
        },
        options: {
            responsive: true,
            legend: {
                display: true,
                position: 'left'
            }
        }
    } );

    /*
    //doughut chart
    var ctx = document.getElementById( "doughutChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'doughnut',
        data: {
            datasets: [ {
                data: [ 45, 25, 20, 10 ],
                backgroundColor: [
                                    "#ff9900",
                                    "#434343",
                                    "#ff0000",
                                    "#b7b7b7"
                                ],
                hoverBackgroundColor: [
                                    "#ff9900",
                                    "#434343",
                                    "#ff0000",
                                    "#b7b7b7"
                                ]

                            } ],
            labels: [
                            "Sprint 1",
                            "Sprint 2",
                            "Sprint 3",
                            "Sprint 4"
                        ]
        },
        options: {
            responsive: true
        }
    } ); */

    /*
    //polar chart
    var ctx = document.getElementById( "polarChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'polarArea',
        data: {
            datasets: [ {
                data: [ 15, 18, 9, 6, 19 ],
                backgroundColor: [
                                    "rgba(0, 123, 255,0.9)",
                                    "rgba(0, 123, 255,0.8)",
                                    "rgba(0, 123, 255,0.7)",
                                    "rgba(0,0,0,0.2)",
                                    "rgba(0, 123, 255,0.5)"
                                ]

                            } ],
            labels: [
                            "green",
                            "green",
                            "green",
                            "green"
                        ]
        },
        options: {
            responsive: true
        }
    } ); */

    // single bar chart
    var ctx = document.getElementById( "singleBarChart" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'bar',
        data: {
            labels: [ "Int1", "Int2", "Int3", "Int4", "Int5" ],
            datasets: [
                {
                    //label: false,
                    data: [ 4, 3, 5, 6, 2 ],
                    borderColor: "#ff9900",
                    borderWidth: "0",
                    backgroundColor: "#ff9900"
                    } ]
        },
        options: {
            legend: {
                display: false
            },
            scales: {
                yAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            }
        }
    } );

    var ctx = document.getElementById( "singleBarChart2" );
    ctx.height = 150;
    var myChart = new Chart( ctx, {
        type: 'bar',
        data: {
            labels: [ "Int1", "Int2", "Int3", "Int4", "Int5" ],
            datasets: [
                {
                    //label: false,
                    data: [ 4, 3, 5, 6, 2 ],
                    borderColor: "#b7b7b7",
                    borderWidth: "0",
                    backgroundColor: "#b7b7b7"
                    } ]
        },
        options: {
            legend: {
                display: false
            },
            scales: {
                yAxes: [ {
                    ticks: {
                        beginAtZero: true
                    }
                                } ]
            }
        }
    } );

} )( jQuery );