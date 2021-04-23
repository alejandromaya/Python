#Le pedimos al usuario que ingrese un sintoma
#Se asignara en nuestra variable tiene_sintoma
tiene_sintoma = input("Ingrese un sintoma: ")
#Definimos nuestra funcion que pedirá el sintoma ingresado.
def enfermo_de(tiene_sintoma):                              
    if tiene_sintoma == 'Fiebre' or tiene_sintoma == 'Tos': #Pregunta Si el sintoma es igual a fiebre ó Tos si ambos casos son verdaderos 
        sintoma_de = 'Gripe'                                #Asignara a otra variable el padecimiento y lo retornara para informar de que esta enfermo, en este caso gripe.
        return sintoma_de                                   
        print (sintoma_de)
    elif tiene_sintoma == 'Cansancio':                      #En el caso contrario si el sintoma es cansansio le asginara al usuario anemia.
        sintoma_de = 'Anemia'
        return sintoma_de
        print (sintoma_de)
        
def alivia(tiene_sintoma):                                  #Ahora recetamos un medicamento por cada sintoma que presente el paciente.
    if tiene_sintoma == 'Fiebre':                           #En este caso si el sintoma presentado anteriormente cumple la condicion se le asignara un medicamento para tratar la molestia
        elimina = 'aspirinas'                               #Se receta aspirinas si es fiebre.
        return elimina                                      #Nos regresa el medicamento recetado
        print (elimina)
    elif tiene_sintoma == 'Tos':                            #Se repite el mismo proceso
        elimina = 'Jarabe'                                  #Se receta en este caso jarabe si es Tos
        return elimina
        print (elimina)
    elif tiene_sintoma == 'Cansancio':                      #Se repite el mismo proceso            
        elimina = 'Vitaminas'                               #Se receta vitaminas si es cansanscio
        return elimina
        print (elimina)
        
def recetar(tiene_sintoma):
    if  tiene_sintoma != 'Fiebre' and tiene_sintoma != 'Tos' and tiene_sintoma != 'Cansancio':      #En el caso de que no se conozca el sintoma no se presenta un diagnostico.
        sintoma_de = ' no se presentan diagnosticos'
        print ("Para el sintoma: " + tiene_sintoma + sintoma_de)
    elif tiene_sintoma == 'Fiebre' or tiene_sintoma == 'Tos' or tiene_sintoma == 'Cansancio':       #Si existe los sintomas ejecutara las funciones anteriores.
        enfermo = enfermo_de(tiene_sintoma)                                                         #Asignamos la respuesta que arrojara la función en otra variable que dira de que esta enfermo.
        medicamento = alivia(tiene_sintoma)                                                         #Asignamos la respuesta que arrojara la función en otra variable el medicamento que se recomienda tomar.
        print ("El paciente tiene sintomas de: " + tiene_sintoma +                                  #Al final imprimimos en pantalla una receta medica.
               " lo que se manifiesta por causa de : " + enfermo +
               " Se le recetara al paciente es: " + medicamento)
