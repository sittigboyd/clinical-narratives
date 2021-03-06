import re

class RecordReader:
    def __init__(self,patient_name=None):
        if patient_name!=None:
            self.name=patient_name
        self.patient_info=[]
        self.medications=[]
        self.history=[]
        self.diabetes=[]
        
    def read_record(self,filename):
        emr=open(filename,'r')
        rec=""
        for line in emr:
            line=line.rstrip()
            rec+=line
        emr.close()
        self.patient_info=self.find_tags(rec)

                
    def find_tags(self,record):
        exp="<TAGS>(.*)</TAGS>"
        tags=re.search(exp,record,re.IGNORECASE)
        if tags!=None:
            return tags.group(1).split("    ")
        else:
            return False
    
    def split_tags(self):
        exp="<([A-Z]+).*?(/(\1)?>)"
        for tag in self.patient_info:
            indiv_tags=re.search(exp,tag,re.IGNORECASE)
            if indiv_tags!=None:
                tag=indiv_tags.group(1)
                self.add_info(tag)
                ## TODO THIS kt listen to ur past self

    def add_info(self,t):
        if contains(t,"MEDICATION"):
            self.medications.append(t)
        elif contains(t,"HISTORY"):
            self.history.append(t)
        
def main():
    reader=RecordReader()
    reader.read_record("../i2b2_2014/RiskFactor-gold/100-01.xml")
    #TODO add functionality so that you can read in actual/inferred ages, gender, etc from the csv file that prof. stubbs read
    
def contains(string,term):
    term=term.lower()
    #TODO     
                
