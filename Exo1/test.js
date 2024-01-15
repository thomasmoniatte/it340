import validpass from "./password";

test("validpPassword", ()=>{
    const res = validpass('Password1$');
    expect(res).toEqual(true);
}
);
test("lenghtError",()=>{
    expect(validpass('Lengt1$')).toEqual(false);    
})

test("uperCaseError",()=>{
    expect(validpass('pasdemaj1$')).toEqual(false);
})

test("numberError",()=>{
    expect(validpass('NumberError$')).toEqual(false);

})

test("userLengthError",()=>{
    expect(validpass('Length1$',9)).toEqual(false);

})

test("userUperCaseError",()=>{
    expect(validpass('Length1$',8,2)).toEqual(false);
    
})


test("userUperCaseError",()=>{
    expect(validpass('Length1$',8,2)).toEqual(false);
    
})

test("userNumberError",()=>{
    expect(validpass('Length1$',8,1,2)).toEqual(false);
})


test("userSpecialError",()=>{
    expect(validpass('Length1$',8,1,1,'[]')).toEqual(false);
})


test("userRegExpError",()=>{
    expect(validpass('Length1$',8,1,1,'[$\*]', '\\')).toEqual(false);
})