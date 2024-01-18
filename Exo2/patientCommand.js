const Patient = require('./patient');
const patientCommandDAO = require('./patientCommandDAO');
function addPatient(lastname, firstname) {
    const patient = new Patient(lastname, firstname)
    patientCommandDAO.insertPatient(patient)
}

module.exports={addPatient}