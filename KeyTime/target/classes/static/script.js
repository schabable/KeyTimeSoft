$(document).ready(function () {

    var timeClick = [];
    var timeTemp = [];
    var timeNext = [];
    var timeNextTemp = 0;
    var keydown = [];
    var first = true;
    var name = "";
    var areaLength = 0;
    $("#txtArea").prop("disabled", true);

    $("#txtInput").on("input", function (event) {
        if ($("#txtInput").val().length !== 0 && $("#txtInput").val().length !== 1) {
            $("#txtArea").prop("disabled", false);
        }
    });

    $("#txtArea").keydown(function (event) {


        areaLength = $("#txtArea").val().length;
        if (areaLength !== 0) {
            $("#txtInput").prop("disabled", true);
        } else {
            $("#txtInput").prop("disabled", false);
        }

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
    }).keyup(function (event) {
        keydown[event.which] = false;
        timeClick[event.which] = Date.now() - timeTemp[event.which];
        name = $("#txtInput").val();

        if (event.which !== 8 && event.which !== 9 && event.which !== 16 && event.which !== 17 && event.which !== 18 && event.which !== 46)
        {
            send(event.which);
        }
    });



    function send(key) {
        $("#id").val(key+"["+String.fromCharCode(key)+"]");
        $("#click").val(timeClick[key] + "ms");
        $("#next").val(timeNext[key] + "ms");

        console.log("Wciśnięty klawisz: " + key +"["+ String.fromCharCode(key)+ "]\n" +
            "Czas przytrzymania klawisza: " + timeClick[key] + "ms\n" +
            "Czas od poprzedniego znaku: " + timeNext[key] + "ms");

        if (name.length !== 0 && name.length !== 1 && areaLength !== 3000) {
            $.ajax({
                CrossDomain: true,
                contentType: "application/json; charset:utf-8",
                type: "POST",
                data: JSON.stringify({
                    "name": name,
                    "keyCode": key,
                    "timeClick": timeClick[key],
                    "timeNext": timeNext[key]
                }),
                dataType: "json",
                url: "/ArrayData",
                success: function (data) {
                    console.log('done');
                }
            });
        }
        timeClick[key] = 0;
    }
})

function reset() {
    location.reload();
}

function newwin(){
    location.replace("./verify.html");
}
