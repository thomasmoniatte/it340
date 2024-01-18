const patientCommand = require('./patientCommand');
const patientQuery = require('./patientQuery');

patientCommand.addPatient('michel','gustave');

console.log(patientQuery.getPatientList());