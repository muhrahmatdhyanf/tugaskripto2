s = []
for i in range(256):
    s.append(i)

kunci = 'saputra1'
k = bytearray(kunci, "utf8")

j = 0
for i in range(len(kunci)):
     j = (j + s[i] + k[i % len(kunci)]) % 256
     x = s[i] 
     s[j] = x
     s[i] = j

P = input ("Masukan Nim 5 angka terakhir = ")
C = []
i=0
j=0
for idx in range(5):
   i = (i + 1)  % 256
   j = (j + s[i]) % 256
   s[i], s[j] = s[j], s[i]
   t = (s[i] + s[j]) % 256
   u = s[t]
   c = u^ord(P[idx])
   C.append(c)
for i in range(len(C)):
    print(chr(C[i]))