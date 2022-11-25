print("************Bienvenido*************");
input("Presine una tecla para continuar...");
print("---------DATOS--------");
name=str(input("Nombre....: "));
age=int(input("Año de macimiento...: "));

resta=(2022-age);
if(resta<18):
    print("Lo sentimos",name," usted es menor de edad!");
    input("Presine una tecla para continuar...");
else:
    venta1=float(input("Venta del primer semeste: "));
    venta2=float(input("Venta de segundo semestre: "));

    total=float(venta2+venta1);

    resultado=str;
    medalla=str;
    descanso=str;
    bono=int;


    if(venta1==venta2):
        resultado=("Ambos son iguales");
    elif(venta1>venta2):
        resultado=("Primer semestre");
    else:
        resultado=("Segundo semestre");

    if(total<=100000):
        medalla=("Bronce");
        descanso=("Un dia libre");
        bono=0.0;
    elif(total<=500000):
        medalla=("Plata");
        descanso=("Un dia libre");
        bono=250;
    elif(total<=1000000):
        medalla=("Oro");
        descanso=("Un dia libre");
        bono=500;
    else:
        medalla=("Diamante");
        descanso=("Un dia libre");
        bono=100;

    print("=========RESULTADOS===========");
    print("Vendedor: ",name);
    print("Ventas anuales: Q",total);
    print("Mejores Ventas: ",resultado);
    print("Medalla acreditada: ",medalla);
    print("Premio: ",descanso,"y Q",bono,"de bono");
    input("Presine una tecla para continuar.....");







