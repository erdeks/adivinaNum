from flask import Flask
from flask import render_template
from flask import request
from random import randint
app= Flask (__name__)
#Crear numero para ejercicio adivina
rand = randint(1,100)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/adivinaNum', methods=['GET', 'POST'])
def adivina():
    global rand
    
    sol = "No hay Numero"
    if request.method == "POST":
        num = request.form["numero"]
        num = int(num)
        if rand != num:
            if(rand<num):
                sol = "El numero es MENOR que el numero introducido"
            else:
                sol = "El numero es MAYOR que el numero introducido"
        else:
            sol = "Correcto! Se ha generado otro numero"
            rand = randint(1,100)
            
    return render_template("adivinaNum.html", mensaje=sol)
if __name__=="__main__":
	app.run()
