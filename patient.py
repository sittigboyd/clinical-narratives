class Patient(self):
    def __init__(self,n=None,a=None,d_status=None,idno=None):
        self.name=n
        self.age=a
        self.patient_id=idno
        self.diabetes=Set()
        self.medications=Set()
        self.history=Set()
        self.smoking=Set()
           
    def add_medication(self,date,med):
        med_add=(date,med)
        self.medications.add(med_add)
        
    def add_smoking(self,date,sm):
        smoke=(date,sm)
        self.smoking.add(smoke)
        
    def add_history(self,date,h):
        hist=(date,h)
        self.history.add(hist)
        
    def add_diabetes(self,date,dia):
        diab=(date,dia)
        self.diabetes.add(diab)
        
        
    
       
   
       
   
   
   
   
   
   
   
   
   
   
   
   
       
       
       
       
       
       
   
       
       
   