print('Calculadora:')
o1 = str(input()).strip()
a = '+' in o1
if a == True:
   a1 = o1.split('+')
   r1 = (float(a1[0]) + float(a1[1]))
   o2 = str(input(r1))
   if o2[0] == '-':
      a2 = o2.split('-')
      r2 = (r1 - float(a2[1]))
      print(r2)
   if o2[0] == 'x':
      a3 = o2.split('x')
      r3 = (r1 * float(a3[1]))
      print(r3)
   if o2[0] == '/':
      a4 = o2.split('/')
      r4 = (r1 / float(a4[1]))
      print(r4)
   if o2[0] == '^':
      a5 = o2.split('^')
      r5 = (r1 ** float(a5[1]))
      print(r5)
b = '-' in o1
if b == True:
   a6 = o1.split('-')
   r6 = (float(a6[0]) - float(a6[1]))
   o7 = str(input(r6)).strip()
   if o7[0] == '+':
      a7 = o7.split('+')
      r7 = (r6 + float(a7[1]))
      print(r7)
   if o7[0] == 'x':
      a8 = o7.split('x')
      r8 = (r6 * float(a8[1]))
      print(r8)
   if o7[0] == '/':
      a9 = o7.split('/')
      r9 = (r6 / float(a9[1]))
      print(r9)
   if o7[0] == '^':
      a10 = o7.split('^')
      r10 = (r6 ** float(a10[1]))
      print(r10)
c = 'x' in o1
if c == True:
   a11 = o1.split('x')
   r11 = (float(a11[0]) * float(a11[1]))
   o8 = str(input(r11)).strip()
   if o8[0] == '+':
      a12 = o8.split('+')
      r12 = (r11 + float(a12[1]))
   if o8[0] == '-':
      a13 = o8.split('-')
      r13 = (r11 - float(a13[1]))
      print(r13)
   if o8[0] == '^':
      a14 = o8.split('^')
      r14 = (r11 ** float(a14[1]))
      print(r14)
   if o8[0] == '/':
      a15 = o8.split('/')
      r15 = (r11 / float(a15[1]))
      print(r15)
d = '/' in o1
if d == True:
   a16 = o1.split('/')
   r16 = (float(a16[0]) / float(a16[1]))
   o9 = str(input(r16)).strip()
   if o9[0] == '+':
      a17 = o9.split('+')
      r17 = (r16 + float(a17[1]))
      print(r17)
   if o9[0] == '-':
      a18 = o9.split('-')
      r18 = (r16 - float(a18[1]))
      print(r18)
   if o9[0] == 'x':
      a19 = o9.split('x')
      r19 = (r16 * float(a19[1]))
      print(r19)
   if o9[0] == '^':
      a20 = o9.split('^')
      r20 = (r16 ** float(a20[1]))
      print(r20)
e = '^' in o1
if e == True:
   a21 = o1.split('^')
   r21 = (float(a21[0]) ** float(a21[1]))
   o10 = str(input(r21)).strip()
   if o10[0] == '-':
      a22 = o10.split('-')
      r22 = (r21 - float(a22[1]))
      print(r22)
   if o10[0] == '+':
      a23 = o10.split('+')
      r23 = (r21 + float(a23[1]))
      print(r23)
   if o10[0] == 'x':
      a24 = o10.split('x')
      r24 = (r21 * float(a24[1]))
      print(r24)
   if o10[0] == '/':
      a25 = o10.split('/')
      r25 = (r21 / float(a25[1]))
      print(r25)
saida = input('Digite 1 para um novo calculo\nOu 2 para Sair ').strip(' ')
if saida =='2':
   quit('')
if saida == '1':
   import teste024
   print(teste024)
