#coba perhitungan MU linac
print("=====Linac High Energy Photon=====")
MU=int(input("Nilai MU: ")) #100MU
P=float(input("Tekanan lab: ")) #101.3
T=float(input("Temperatur lab: ")) #21.3
T0=(20)
P0=(100.8)
M1=300
M2=300
readv1=(15.289)
readv2=(15.191)
ndw=(4.85E-2)
kQ=(0.986)
PDD=(73.67)

KTP=(((273.2+T)*P0)/((273.2+T0)*P))
ratio=(readv1/MU)
kpol=((M1+M2)/(2*M1))
ks=(1.198+(-0.8753)*(readv1/readv2)+(0.6773*((readv1/readv2)**2)))
Dzref=(kpol*ks*ratio*KTP*ndw*kQ)
Dzmax=(100*(Dzref/PDD))
print("Nilai Dosis Serap: ", Dzmax,"Gy/MU")
print("dalam cGy/MU: ",Dzmax*100, "cGy/MU")


