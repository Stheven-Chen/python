#ubah 1 tipe data ke tipe data lain

#Integer
print("================================================================")
dataint=12
print("data=", dataint, ", tipe=", type(dataint))
datafloat=float(dataint)
datastring=str(dataint)
databoolean=bool(dataint)
print("data=", datafloat, ", tipe=", type(datafloat))
print("data=", datastring, ", tipe=", type(datastring))
print("data=", databoolean, ", tipe=", type(databoolean)) #falase jika int=0

#Float
print("================================================================")
float2=12.2
print("data=", float2, ", tipe=", type(float2))
int2=int(float2)
string2=str(float2)
bolean2=bool(float2)
print("data=", int2, ", tipe=", type(int2))
print("data=", string2, ", tipe=", type(string2))
print("data=", bolean2, ", tipe=", type(bolean2))

#String
print("================================================================")
string3="12"
print("data=", string3, ", tipe=", type(string3))
int3=int(string3)
float3=float(string3)
bolean3=bool(string3)
print("data=", int3, ", tipe=", type(int3))
print("data=", float3, ", tipe=", type(float3))
print("data=", bolean3, ", tipe=", type(bolean3))

#Boolean
print("================================================================")
bolean=True
print("data=", bolean, ", tipe=", type(bolean))
int4=int(bolean)
float4=float(bolean)
string4=str(bolean)
print("data=", int4, ", tipe=", type(int4))
print("data=", float4, ", tipe=", type(float4))
print("data=", string4, ", tipe=", type(string4))
