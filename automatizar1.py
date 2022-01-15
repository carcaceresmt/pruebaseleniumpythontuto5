from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

print("Prueba Automatizar Selenium Python")
basee=input("Digite la Base")
alte=input("Digite la Altura")
op=input("Digite la opción")
#ruta del driver para realizar la prueba automatiza en el navegador chrome v 97
controlador=webdriver.Chrome(executable_path=r"C:\demoprueba\driver\chromedriver.exe")
#la app donde se va hacer la prueba automatizada
controlador.get("C:/demoprueba/app/index.html")
#maximizar el navegador
controlador.maximize_window()
#tiempo 1 segundo de espera
time.sleep(1)
base = controlador.find_element_by_id("base")
#base.send_keys("4")
base.send_keys(basee)
time.sleep(1)
altura=controlador.find_element_by_id("altura")
#altura.send_keys(5)
altura.send_keys(alte)
time.sleep(1)
opcion=controlador.find_element_by_id("opcion")
seleccion=Select(opcion)
time.sleep(1)
#seleccion.select_by_value("1")
seleccion.select_by_value(op)
time.sleep(1)
bcalc=controlador.find_element_by_id("bcalc")
bcalc.click()
time.sleep(2)
print("Fin de Prueba Automatizada")


