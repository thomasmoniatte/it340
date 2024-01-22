class Event {
    constructor(name,patientID,payload) {
        this.name = name;
        this.patientID=patientID;
        this.payload = payload;
        this.creationDate = new  Date();
    }
}

module.exports=Event;