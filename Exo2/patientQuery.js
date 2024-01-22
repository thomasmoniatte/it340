const patientQueryDAO = require('./patientQueryDAO');

function getPatientList() {
    return patientQueryDAO.retrievePatientList()
}

module.exports={getPatientList};