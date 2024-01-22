const Patient = require('./patient');

const patientCommandDAO = require('./patientCommandDAO');

function addPatient(lastname, firstname) {
    const patient = new Patient(lastname, firstname)
    patientCommandDAO.insertPatient(patient)
    const {creationDate: date, ...patientlist}= patient;
    patientCommandDAO.insertPatientList(patientlist);

}


function savePatient(id, lastName, firstName) {

    const patient = patientCommandDAO.retrievePatient(id);
    patient.lastName = lastName;
    patient.firstName= firstName;
    patientCommandDAO.updatePatient(patient);


    const patient2 = patientCommandDAO.retrievePatientList(id); 
    patient2.lastName = lastName;
    patient2.firstName= firstName;
    patientCommandDAO.updatePatientList(patient2);
}

module.exports={addPatient,savePatient}