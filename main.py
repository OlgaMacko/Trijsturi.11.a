import math
print("Programma aprēķina trijstūra laukumu")
print("Ja ir zināms trijstūra augstums un pamats, tad nospiediet 1")
print("Ja ir zināms divas malas un leņķis starp tiem, tad nospiediet 2")
print("Ja ir zināms 3 dažādas malas, tad nospiediet 3")
print("Ja ir zināms 3 vienādas malas, tad nospiediet 4")
print("Ja ir zināms 3 malas un ievilktas r.l. rādiuss, tad nospiediet 5")
print("Ja ir zināms 3 malas un apvilktas r.l. rādiuss, tad nospiediet 6")
cipars=int(input())
if cipars==1:
  a=float(input("Ievadiet malu "))
  h=float(input("Ievadiet augstumu "))
  s=a*h/2
  print (round(s,2))
if cipars==2:
  a=float(input("Ievadiet 1.malu "))
  b=float(input("Ievadiet 2.malu "))
  l=int(input("Ievadiet leņķi grados "))
  radians=180/l
  s=a*b*math.sin(math.pi/radians)/2
  print (round(s,2))
if cipars==3:
  a=float(input("Ievadiet 1.malu "))
  b=float(input("Ievadiet 2.malu "))
  c=float(input("Ievadiet 3.malu "))
  p=(a+b+c)/2
  if ((a+b>c) and (a+c>b) and (b+c>a)):           s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    print (round(s,2))
  else: print("trijstūrs neeksistē")
 




