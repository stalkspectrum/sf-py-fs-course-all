const Initial_Pc = 50;
let Current_Pc = Initial_Pc;

function Plus_1() {
    if (Current_Pc < 100) {
        Current_Pc = Current_Pc + 1;
        Current_Width = Current_Pc + "%";
        $("#my-progress-bar").width(Current_Width);
        $("div#my-progress-bar").text(Current_Width);
    }
}
function Plus_3() {
    if (Current_Pc < 98) {
        Current_Pc = Current_Pc + 3;
        Current_Width = Current_Pc + "%";
        $("#my-progress-bar").width(Current_Width);
        $("div#my-progress-bar").text(Current_Width);
    }
}
function Plus_7() {
    if (Current_Pc < 94) {
        Current_Pc = Current_Pc + 7;
        Current_Width = Current_Pc + "%";
        $("#my-progress-bar").width(Current_Width);
        $("div#my-progress-bar").text(Current_Width);
    }
}
function Minus_1() {
    if (Current_Pc > 0) {
        Current_Pc = Current_Pc - 1;
        Current_Width = Current_Pc + "%";
        $("#my-progress-bar").width(Current_Width);
        $("div#my-progress-bar").text(Current_Width);
    }
}
function Minus_3() {
    if (Current_Pc > 2) {
        Current_Pc = Current_Pc - 3;
        Current_Width = Current_Pc + "%";
        $("#my-progress-bar").width(Current_Width);
        $("div#my-progress-bar").text(Current_Width);
    }
}
function Minus_7() {
    if (Current_Pc > 6) {
        Current_Pc = Current_Pc - 7;
        Current_Width = Current_Pc + "%";
        $("#my-progress-bar").width(Current_Width);
        $("div#my-progress-bar").text(Current_Width);
    }
}

function Do_It() {
	$("#button1pc").click(Plus_1);
    $("#button3pc").click(Plus_3);
    $("#button7pc").click(Plus_7);
    $("#button-1pc").click(Minus_1);
    $("#button-3pc").click(Minus_3);
    $("#button-7pc").click(Minus_7);
}

$(document).ready(Do_It);
