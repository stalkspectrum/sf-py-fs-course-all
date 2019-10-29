const dataURL = "https://api.myjson.com/bins/jcmhn";

function Write_Data(We_Got_Data) {
    let Story_Output = "";
    const Field1 = $("input[name=var1]")[0].value;
    const Field2 = $("input[name=var2]")[0].value;
    const Field3 = $("input[name=var3]")[0].value;
    const Field4 = $("input[name=var4]")[0].value;
    const Field5 = $("input[name=var5]")[0].value;
    const Field6 = $("input[name=var6]")[0].value;
    const Field7 = $("textarea[name=var7]")[0].value;
    const Strings_Array = We_Got_Data["text"];
    for(let ns = 0; ns < Strings_Array.length; ns++) {
        Strings_Array[ns] = Strings_Array[ns].replace(/{var1}/g, Field1);
        Strings_Array[ns] = Strings_Array[ns].replace(/{var2}/g, Field2);
        Strings_Array[ns] = Strings_Array[ns].replace(/{var3}/g, Field3);
        Strings_Array[ns] = Strings_Array[ns].replace(/{var4}/g, Field4);
        Strings_Array[ns] = Strings_Array[ns].replace(/{var5}/g, Field5);
        Strings_Array[ns] = Strings_Array[ns].replace(/{var6}/g, Field6);
        Strings_Array[ns] = Strings_Array[ns].replace(/{speach}/g, Field7);
        Story_Output = Story_Output + Strings_Array[ns] + "<br>";
    }
    $("div#result").html(Story_Output);
}

function Fill_Data() {
    $.getJSON(dataURL, Write_Data);
}

function Do_It() {
	$("#button-fetch").click(Fill_Data);
}

$(document).ready(Do_It);
