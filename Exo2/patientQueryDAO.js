

function retrievePatientList() {
    return database.patients.map(({creationDate, ...patient}) => patient);
}


module.export={retrievePatientList};