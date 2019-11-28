( function ( $ ) {
    "use strict";

    var cod_1o = document.getElementById("1o").getAttribute("data-produto");
    var cod_2o = document.getElementById("2o").getAttribute("data-produto");
    var cod_3o = document.getElementById("3o").getAttribute("data-produto");
    var cod_4o = document.getElementById("4o").getAttribute("data-produto");
    var cod_5o = document.getElementById("5o").getAttribute("data-produto");
    var cod_6o = document.getElementById("6o").getAttribute("data-produto");
    var cod_7o = document.getElementById("7o").getAttribute("data-produto");
    var cod_8o = document.getElementById("8o").getAttribute("data-produto");
    var cod_9o = document.getElementById("9o").getAttribute("data-produto");
    var cod_10o = document.getElementById("10o").getAttribute("data-produto");
    var cod_11o = document.getElementById("11o").getAttribute("data-produto");
    var cod_12o = document.getElementById("12o").getAttribute("data-produto");

    var cod_1c = document.getElementById("1c").getAttribute("data-produto");
    var cod_2c = document.getElementById("2c").getAttribute("data-produto");
    var cod_3c = document.getElementById("3c").getAttribute("data-produto");
    var cod_4c = document.getElementById("4c").getAttribute("data-produto");
    var cod_5c = document.getElementById("5c").getAttribute("data-produto");
    var cod_6c = document.getElementById("6c").getAttribute("data-produto");
    var cod_7c = document.getElementById("7c").getAttribute("data-produto");
    var cod_8c = document.getElementById("8c").getAttribute("data-produto");
    var cod_9c = document.getElementById("9c").getAttribute("data-produto");
    var cod_10c = document.getElementById("10c").getAttribute("data-produto");
    var cod_11c = document.getElementById("11c").getAttribute("data-produto");
    var cod_12c = document.getElementById("12c").getAttribute("data-produto");

var ctx = document.getElementById( "barChart" );
//   ctx.height = 200;
var myChart = new Chart( ctx, {
    type: 'bar',
    data: {
        labels: [ "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec" ],
        datasets: [
            {
                label: "Opened",
                data: [cod_1o, cod_2o, cod_3o, cod_4o, cod_5o, cod_6o, cod_7o, cod_8o, cod_9o, cod_10o, cod_11o, cod_12o],
                borderColor: "#ff0000",
                borderWidth: "0",
                backgroundColor: "#ff0000"
                        },
            {
                label: "Closed",
                data: [cod_1c, cod_2c, cod_3c, cod_4c, cod_5c, cod_6c, cod_7c, cod_8c, cod_9c, cod_10c, cod_11c, cod_12c],
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

} )( jQuery );