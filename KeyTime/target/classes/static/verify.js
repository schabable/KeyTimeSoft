$(document).ready(function () {

    var timeClick = [];
    var timeTemp = [];
    var timeNext = [];
    var timeNextTemp = 0;
    var keydown = [];
    var first = true;
    var name = "";
    var areaLength = 0;
    var check= [];
    var i=0;
    var array= [];

    $("#txtAreaVerify").keydown(function (event) {


        if (first) {
            first = !first;
            timeNextTemp = Date.now();
        }
        if (!keydown[event.which]) {
            keydown[event.which] = true;
            timeTemp[event.which] = new Date();
            timeNext[event.which] = Date.now() - timeNextTemp;
        }
        timeNextTemp = Date.now();
    });

    $("#txtAreaVerify").keyup(function (event) {
        keydown[event.which] = false;
        timeClick[event.which] = Date.now() - timeTemp[event.which];

        if (event.which !== 8 && event.which !== 9 && event.which !== 16 && event.which !== 17 && event.which !== 18 && event.which !== 46) {
            toPython(event.which);
        }
    });


    function toPython(key) {

        array=JSON.stringify({
            "keyCode": key,
            "timeClick": timeClick[key],
            "timeNext": timeNext[key]
        });

        console.log("Wciśnięty klawisz: " + key + "[" + String.fromCharCode(key) + "]\n" +
            "Czas przytrzymania klawisza: " + timeClick[key] + "ms\n" +
            "Czas od poprzedniego znaku: " + timeNext[key] + "ms");

        check[i]=array;
        i++;
    }

    $("#check").on("click", function () {

        console.log(check);

        $.ajax({
            url: 'http://localhost:5000/test',
            type: 'post',
            contentType: 'application/json;charset=utf-8',
            data: JSON.stringify(check)
        }).done(function (result) {
            console.log(result);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            console.log("fail: ", textStatus, errorThrown);
        });
    });
})

function back() {
    location.replace("./index.html");
}

$(document).ready(function () {
    $("#check").on("click", function () {

    });
});
