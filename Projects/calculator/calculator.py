operación1= "sumar"
operación2= "restar"
operación3= "multiplicar"
operación4= "dividir"
operación5= "potencia"

while(True):
    nombre="CALCULADORA"
    var1=(len(nombre))
    print(var1*"*")
    print(nombre)
    print(var1*"*")
    print("MENÚ PRINCIPAL")
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Potencia" )
    print(var1*"*")
    operación=input("¿Qué operación quieres hacer?")
    
    if (operación=="1"):
        num1=input("Introduce el primer número")
        num2=input("Introduce el segundo número")
        final=float(num1) + float(num2)
        final=round(final,2)
        print(num1 ,"+" , num2, "=", final)
    
  
    if(operación=="2"):
        num1=input("Introduce el primer número")
        num2=input("Introduce el segundo número")
        final=float(num1) - float(num2)
        final=round(final,2)
        print(num1 ,"-" , num2, "=", final)
    
        
    if(operación=="3"):
        num1=input("Introduce el primer número")
        num2=input("Introduce el segundo número")
        final=float(num1) * float(num2)
        final=round(final,2)
        print(num1 ,"*" , num2, "=", final)
        
        
    if(operación=="4"):
        num1=input("Introduce el primer número")
        num2=input("Introduce el segundo número")
        if(num2=="0"):
            print("ERROR, no se puede dividir entre 0")
     
        if(num2!="0"):
            final=float(num1) / float(num2)
            final=round(final,2)
            print(num1 ,"/" , num2, "=", final)
        
        
    if(operación=="5"):
        num1=input("Introduce el primer número")
        num2=input("Introduce el segundo número") 
        final=float(num1) ** float(num2)
        final=round(final,2)
        print(num1 ,"**" , num2, "=", final)
    
    ans=input("¿Quiere hacer otra operación(s/n)?")
    if(ans=="n" or ans=="N"):
        break

    if(ans!= "S" and ans!="s" and ans!="N" and ans!="n"):
        print("Respuesta no válida")
        ans1=input("¿Quiere hacer otra operación(s/n)?")
        if(ans1=="n" or ans1=="N"):
            break
        if(ans1=="s" or ans1=="S"):
            continue
