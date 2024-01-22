const Patient = require('./patient');
const Event = require('./event');

const eventStore = require('./eventStore');

function addPatient(lastname, firstname) {
    const patient = new Patient(lastname, firstname)
    const event  = new Event("addEvent", patient.id, patient);
    eventStore.addEvent(event);
}

function savePatient(id, lastName, firstName) {

    const patient = eventStore.restorePatientId(id);
    patient.lastName=lastName;
    patient.firstName=firstName;
    eventStore.addEvent(new Event('patientSave', patient.id,patient));
    
}


module.exports={addPatient,savePatient}