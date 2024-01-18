const database = require("./database")

function insertPatient(patient) {
    database.patients.push(patient)
}

module.exports= {insertPatient}