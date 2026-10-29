class Doctor:
    def __init__(self,doctor_id,doctor_name,specialization,available_time_slots):
        self.doctor_id=doctor_id
        self.doctor_name=doctor_name
        self.specialization=specialization
        self.available_time_slots=available_time_slots
    def display_doctor_details(self):
        print(f"DoctorId:{self.doctor_id}")
        print(f"Doctor Name:{self.doctor_name}")
        print(f"specialization: {self.specialization}")
        print(f"availability: {self.available_time_slots}")
   
           
class patient:
    def __init__(self,patient_id,patient_name,problem):
        self.patient_id=patient_id
        self.patient_name=patient_name
        self.problem=problem
    def display_patient_details(self):
        print(f"patient id: {self.patient_id}\npatient Name:{self.patient_name}\nproblem: {self.problem}")
class Appointment:
    def __init__(self,appointment_id,doctor,patient,date,time):
        self.appointment_id=appointment_id
        self.doctor=doctor
        self.patient=patient
        self.date=date
        self.time=time
        
class hospital:
    def __init__(self,hospitalname,city):
        self.hospitalname=hospitalname
        self.city=city
        self.doctors_list=[]
        self.patients_list=[]
        self.appointments=[]
    
    def add_doctor(self,doctor):
        
        if doctor not in self.doctors_list:
          self.doctors_list.append(doctor)
        else:
            print("duplicate")
    def add_patient(self,patient):
        if patient not in self.patients_list:
            self.patients_list.append(patient)
        else:
            print("duplicate")
    def find_doctor_by_specialization(self,specialization):
        found=False
        for doctor in self.doctors_list:
            if doctor.specialization==specialization:
                doctor.display_doctor_details()
                found=True
        if not found:
            print("specialist not found")
    def check_doctors_availability(self,doctor):
        if doctor not in self.doctors_list:
            print("doctor not found")
            return
        time=input("enter the time to search")
        date=input("enter the date")
        
        for appointment in self.appointments:
                
            if appointment.time==time and appointment.date==date and appointment.doctor.doctor_id==doctor.doctor_id:
                           
                        print("not available")
                        return
        
        print("available")
            
    def book_appointment(self):
        appoi_id=int(input("enter the appointment_id"))
        doctorid=int(input('enter the doctor'))
        patientid=int(input("enter the patient"))
        date=input('enter the date')
        time=input("enter the time")
        p=d=None
        doctor_found=False
        patient_found=False
        
        appointid=False

        for doctor in self.doctors_list:
            if doctor.doctor_id==doctorid:
                doctor_found=True
                d=doctor
                break

        if doctor_found==False:
            print("doctor not found")
            return
        for patient in self.patients_list:
            if patient.patient_id==patientid:
                patient_found=True
                p=patient
                break
        if patient_found==False:
            print("patient not found")
            return
        
        
        for appointment in self.appointments:
            if appointment.appointment_id==appoi_id:
                    appointid=True
                    break
        if appointid:
            print("duplicate appointment id")
            return
        for appointment in self.appointments:
            if appointment.doctor.doctor_id==doctorid and appointment.date==date and appointment.time==time:
                print("Already booked at this date and time")
                return
        

            
                    
                    

                    
            
         
          
        a=Appointment(appoi_id,d,p,date,time)
                    
        self.appointments.append(a)
                    
                    
        print("appointment boooked successfully")
                    
                    
            
    def cancel_appointment(self,appointment_id):
        found=False
        for appointment in self.appointments:
            if appointment.appointment_id==appointment_id:
                found=True
                self.appointments.remove(appointment)
                print("appointment cancelled succesfully")
                
                break
        if not found:
            print("appointment is not found")

    def display_appointments(self):
        for appoin in self.appointments:
            print(f"appointment Id:{appoin.appointment_id}")
            print(f"{appoin.doctor.doctor_name}\n{appoin.patient.patient_name}\n{appoin.date}\n{appoin.time}")
h=hospital("GOVT","mandya")
d=Doctor(1,"chandana","child_specialist",[10,11,12,1])
h.add_doctor(d)
p=patient(1,"priya","infection")
h.add_patient(p)
h.find_doctor_by_specialization("child_specialist")
h.check_doctors_availability(d)
h.book_appointment()
p=patient(2,"suresh","infection")
h.add_patient(p)
h.find_doctor_by_specialization("child_specialist")
h.check_doctors_availability(d)
h.book_appointment()
print("appointments")




    
    



    


        

        




    
                               
