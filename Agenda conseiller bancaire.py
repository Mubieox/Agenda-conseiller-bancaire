class RDV:
    def __init__(self,date,heure,prenom,motif):
        self.d,self.h,self.p,self.m=date,heure,prenom,motif
    def __repr__(self):
        return f"RDV({self.d},{self.h},{self.p},{self.m})"
    def __str__(self):
        return f"{self.d} {self.h} {self.p} {self.m}"
def rdv_personne(E,p):
    LRDV=set()
    for rdv in E:
        if p==rdv.p:
            LRDV.add(rdv)
    return LRDV
def rdv_restants(E,d,h):
    LRDV=set()
    for rdv in E:
        if rdv.h>h and rdv.d==d:
            LRDV.add(rdv)
    return LRDV
def nb_rdv(E):
    LRDV={}
    for rdv in E:
        if rdv.d not in LRDV:
            LRDV[rdv.d]=1
        else:
            LRDV[rdv.d]+=1
    return LRDV
def dict_date(E):
    LRDV={}
    for rdv in E:
        if rdv.d not in LRDV:
            LRDV[rdv.d]={(rdv.h,rdv.p,rdv.m)}
        else:
            LRDV[rdv.d].add((rdv.h,rdv.p,rdv.m))
    return LRDV
def conflit_rdv(r,s):
    if r.d==s.d and r.h==s.h:
        return True
    else:
        return False
def conflit_agenda(E):
    TF=False
    for i in E:
        for j in E:
            if i!=j and conflit_rdv(i,j)==True:
                TF=True
                return TF
    return TF
    
Agenda={RDV("18/05/2022",10,"Paul","Assurance"),
        RDV("18/05/2022",14,"Julien","Compte"),
        RDV("18/05/2022",15,"Thomas","Internet"),
        RDV("19/05/2022",10,"Claude","Compte"),
        RDV("19/05/2022",11,"Michel","Assurance"),
        RDV("19/05/2022",16,"Claude","Bourse"),
        RDV("20/05/2022",10,"Julien","Crédit"),
        RDV("20/05/2022",15,"Paul","Internet"),
        RDV("22/05/2022",13,"Paul","Bourse")}

print(repr(RDV("18/05/2022",10,"Paul","Assurance")))

print(RDV("18/05/2022",10,"Paul","Assurance"))

print(rdv_personne(Agenda,"Laeticia"),"\n",
      rdv_personne(Agenda,"Paul"),"\n",
      rdv_restants(Agenda,"18/05/2022",11),"\n",
      nb_rdv(set()),"\n",
      nb_rdv(Agenda),"\n",
      dict_date(set()),"\n",
      dict_date(Agenda),"\n",
      conflit_rdv(RDV("18/05/2022",10,"Paul","Assurance"),RDV("18/05/2022",10,"Julien","Bourse")),"\n",
      conflit_rdv(RDV("18/05/2022",10,"Paul","Assurance"),RDV("22/05/2022",10,"Julien","Bourse")),"\n",
      conflit_agenda(Agenda),"\n",
      conflit_agenda({RDV("18/05/2022",10,"Paul","Assurance"),RDV("18/05/2022",10,"Julien","Bourse")}),"\n",
      conflit_agenda({RDV("19/05/2022",16,"Paul","Assurance")})
      )
