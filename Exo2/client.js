const patientCommand = require('./patientCommand');
const patientQuery = require('./patientQuery');

patientCommand.addPatient('michel','gustave');

console.log(patientQuery.getPatientList());

patientCommand.savePatient(0,'michel','michel');

console.log(patientQuery.getPatientList());