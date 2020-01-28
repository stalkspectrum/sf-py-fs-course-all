$('#subdiv23').hide();

yourCity.value = localStorage.getItem('yourCity');
if (Boolean(yourCity.value)) {
    $('#subdiv11').hide();
    $('#subdiv12').html('<P>Теперь мы знаем ваш город. Это ' + yourCity.value + '</P>');
    $('#goaway').text('Стереть ненужные знания');
    $('#subdiv12').show();
}
yourCity.oninput = () => localStorage.setItem('yourCity', yourCity.value);

cbBitMap = localStorage.getItem('cbBits');
if (Boolean(cbBitMap)) {
    for (let cnt = 0; cnt < cbBitMap.length; cnt++) {
        cbIdStr = '#cb' + String(1 + cnt);
        if (cbBitMap[cnt] == '1') {
            $(cbIdStr).setattrib('checked', 'true');
        } else {
            $(cbIdStr).remattrib('checked');
        }
        $(cbIdStr).setattrib('disabled', 'true');
    }
    $('#subdiv22').hide();
    $('#subdiv23').show();
}

$('#goaway').click(e => {
    localStorage.removeItem('yourCity');
    yourCity.value = '';
});

$('#savestate').click(e => {
    let cbBitStr = '';
    const cbGrp = document.getElementsByName('t2cb');
    for (let cnt = 0; cnt < cbGrp.length; cnt++) {
        if (cbGrp[cnt].checked) {
            cbBitStr += '1';
        } else {
            cbBitStr += '0';
        }
    }
    localStorage.setItem('cbBits', cbBitStr);
});

$('#forgetit').click(e => {
    localStorage.removeItem('cbBits');
    cbBits = '';
});
