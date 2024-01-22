const database = require("./database")

function insertPatient(patient) {
    database.patients.push(patient)
}
function insertPatientList(patient) {
    database.patientList.push(patient)
}

function Patientindex(id, db) {
    let i =-1;
    const array = database[db];
    for (let index = 0; index < array.length; index++) {
        if ( array[index].id === id ) {
            i = index;
            break;
        };
    }
    if( i==-1){
        throw('id not found')
    }
    return i ;
}

function retrievePatient(id) {
    let patient=database.patients.find((patient)=> patient.id === id)
    if (patient!=null){
        return patient
    }
    
    throw Error("Invalid id");
}
function retrievePatientList(id) {
    let patient=database.patientList.find((patient)=> patient.id === id)
    if (patient!=null){
        return patient
    }
    
    throw Error("Invalid id");
}

function updatePatient(patient) {
    const index = Patientindex(patient.id,'patients')
    database.patients[index] = patient;
}

function updatePatientList(patient) {    
    const index = Patientindex(patient.id,'patientList')
    database.patientList[index] = patient;
}

module.exports= {insertPatient,insertPatientList,retrievePatient,retrievePatientList,updatePatient,updatePatientList}  