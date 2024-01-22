const database = require('./database');

function retrievePatientList() {
   // return database.patients.map(({creationDate, ...patient}) => patient);
    return database.patientList
}


module.exports={retrievePatientList};