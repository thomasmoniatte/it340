function testpresence(password,regexp,number) {
    const reg = new RegExp(regexp,"g");
    let res = 0;
    for (const letter of password) {
        if (reg.test(letter)){
            res++;
        }
    }
    return res>=number
}


function validpass(password, length=8, nb_integer=1, nb_upercases=1,list_special="[$&\*\\\[]", user_regex = ".") {
    let res = testpresence(password,"\d",nb_integer);
    res = res && testpresence(password,"[A-Z]",nb_upercases);
    res = res && testpresence(password,list_special,1);
    const user_reg = new RegExp(user_regex);
    res = res && user_reg.test(password);
    return password.length>=length?res:false;
}

module.exports=validpass