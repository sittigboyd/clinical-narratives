class Patient(self):
   def __init__(self,n=None,a=None,d_status=None,idno=None):
       self.name=n
       self.age=a
       self.patient_id=idno
       self.diabetic=d_status # boolean 
       self.medications=[]
       self.history=[] # a blank slate 
       self.smoking=[]
       #TODO make sure that medications, history, patient info are all sets of tuples (date, info)
           
   def add_medication(self,m):
       self.medications.append(m)
       
   def remove_medication(self,m):
       self.medications.remove(m)
       
       
       
       
       
       
       
       
   
       
       
   