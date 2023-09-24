# Crea un detector de palindromos en python
# Puentos extra : detectar error y repetir
band=True
while band :
    try :
        text=input("Introduzca su palabra a detectar : ").upper().strip(); i=len(text)-1; x=""
        while i>=0 : x+=text[i]+""; i=i-1
        if text==x : print("Es palindromo"); band=False
        else : print("No es palindromo"); band=False
        y=input("Quiere detectar otra palabra? si/no : ").upper().strip()
        if y=="SI" : band=True
        else : band=False
    except :
        print("Ha ocurrido un error")
