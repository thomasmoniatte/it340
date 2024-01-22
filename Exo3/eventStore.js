const Patient = require("./patient");

eventList = []

function addEvent(event) {
    eventList.push(event);
}

function restorePatientId(id) {
    let patient={};
    eventList.forEach(p => {
        if (p.patientID===id) {
            for (const key in p.payload) {
                    patient[key] = p.payload[key];       
                
            }   
        }    
    });  
    console.log('restored patient' +patient);
    return patient
}


module.exports={addEvent,restorePatientId}