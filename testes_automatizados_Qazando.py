import time
import warnings

from selenium.webdriver.support.wait import WebDriverWait

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class ExemploSeleniumWebDriver(unittest.TestCase):

     def setUp(self):
          self.driver = webdriver.Chrome()
          warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

     def test_cadastro(self):
          driver = self.driver
          driver.get("https://automationpratice.com.br/")
          print("URL:", driver.current_url)
          self.assertIn("QAZANDO Shop E-Commerce", driver.title)

          elem_cadastro = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[1]/div/div/div[2]/div/ul/li[2]/a")))
          elem_cadastro.click()

          elem_nome = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div/div/div[1]/input")))
          elem_nome.send_keys("Cristoffer")

          elem_email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div/div/div[2]/input")))
          elem_email.send_keys("cristoffer@gmail.com")

          elem_senha = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div/div/div[3]/input")))
          elem_senha.send_keys("123456")

          elem_cadastrar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div/div/button")))
          driver.execute_script("arguments[0].click();", elem_cadastrar)

          elem_cadastro_realizado = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div[2]/div/h2")))
          self.assertEqual("Cadastro realizado!", elem_cadastro_realizado.text)

          elem_bemvindo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div[2]/div/div[2]")))

          self.assertIn("Bem-vindo", elem_bemvindo.text)

          print(" ")
          print(elem_cadastro_realizado.text)
          print(elem_bemvindo.text)
          print(" ")

     def test_login(self):
          driver = self.driver
          driver.get("https://automationpratice.com.br/")
          print("URL:", driver.current_url)
          self.assertIn("QAZANDO Shop E-Commerce", driver.title)

          elem_login = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[1]/div/div/div[2]/div/ul/li[1]/a")))
          elem_login.click()

          elem_email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/div/section[2]/div/div/div/div/div[1]/input")))
          elem_email.send_keys("cristoffer@gmail.com")

          elem_senha = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/div/section[2]/div/div/div/div/div[2]/input")))
          elem_senha.send_keys("123456")

          elem_logar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/div/section[2]/div/div/div/div/div[3]/button")))
          driver.execute_script("arguments[0].click();", elem_logar)

          elem_login_realizado = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div[2]/div/h2")))

          self.assertEqual("Login realizado", elem_login_realizado.text)

          elem_boasvindas = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div[2]/div/div[2]")))

          self.assertEqual("Olá, cristoffer@gmail.com", elem_boasvindas.text)
          
          print(" ")
          print(elem_login_realizado.text)
          print(elem_boasvindas.text)
          print(" ")

     def test_adicionar_produto_carrinho(self):
          driver = self.driver
          driver.get("https://automationpratice.com.br/")

          elem_produto = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[4]/div/div[2]/div/div/div/div[1]/div/div[7]/div/div[1]/div[1]/a")))
          driver.execute_script("arguments[0].click();", elem_produto)

          elem_add_produto_carrinho = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div[1]/div[2]/div/div/div[4]/a")))
          driver.execute_script("arguments[0].click();", elem_add_produto_carrinho)

          elem_produto_h5 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div[1]/div[2]/div/div/h3")))

          elem_produto_titulo = elem_produto_h5.text

          time.sleep(5)
          elem_carrinho = driver.find_element(By.XPATH, "/html/body/div/header/div/div/div/div/div/ul/li[2]/a")
          driver.execute_script("arguments[0].click();", elem_carrinho)

          elem_ver_carrinho = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/div[4]/div[2]/ul[2]/li[1]/a")))
          driver.execute_script("arguments[0].click();", elem_ver_carrinho)

          elem_quarto_produto_carrinho = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/div[1]/table/tbody/tr[4]/td[3]/a")))
          
          self.assertEqual(elem_produto_titulo, elem_quarto_produto_carrinho.text)

          print(" ")
          print(f"Produto selecionado: {elem_produto_titulo}\nÉ igual ao produto no carrinho: {elem_quarto_produto_carrinho.text}")
          print(" ")

     
     def test_comprar(self):
          driver = self.driver
          driver.get("https://automationpratice.com.br/")

          time.sleep(2)
          elem_carrinho = driver.find_element(By.XPATH, "/html/body/div/header/div/div/div/div/div/ul/li[2]/a")
          driver.execute_script("arguments[0].click();", elem_carrinho)

          elem_checkout = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/div[4]/div[2]/ul[2]/li[2]/a")))
          driver.execute_script("arguments[0].click();", elem_checkout)

          elem_primeiro_nome = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/div[2]/form/div/div[1]/div/input")))
          elem_primeiro_nome.send_keys("Cristoffer")

          elem_ultimo_nome = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/div[2]/form/div/div[2]/div/input")))
          elem_ultimo_nome.send_keys("Laner")

          elem_companhia = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/div[2]/form/div/div[3]/div/input")))
          elem_companhia.send_keys("Senac RS")

          elem_email = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/div[2]/form/div/div[4]/div/input")))
          elem_email.send_keys("cristoffer@gmail.com")

          elem_pais = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/div[2]/form/div/div[6]/div/select/option[2]")))
          elem_pais.click()

          elem_cidade = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/div[2]/form/div/div[6]/div/select/option[2]")))
          elem_cidade.click

          elem_cep = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/div[2]/form/div/div[7]/div/input")))
          elem_cep.send_keys("96154000")

          elem_endereço = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/div[2]/form/div/div[8]/div/input")))
          elem_endereço.send_keys("rua tal numero tal")

          elem_comentario = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/div[2]/form/div/div[8]/div/input")))
          elem_comentario.send_keys("Obrigado.")

          elem_salvar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[1]/div/button")))
          driver.execute_script("arguments[0].click();", elem_salvar)

          elem_comprar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div/div[2]/div[2]/button")))
          driver.execute_script("arguments[0].click();", elem_comprar)
          
          elem_sucesso = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div[3]/div/div/div/div/div/div/div[2]/div/div[1]/div/h2")))

          self.assertIn("Order success!", elem_sucesso.text)

          print(" ")
          print(elem_sucesso.text)
          print(" ")


     def test_pesquisar_e_favoritar_produto(self):
          driver = self.driver
          driver.get("https://automationpratice.com.br/")

          time.sleep(2)
          elem_pesquisa = driver.find_element(By.CLASS_NAME, "search_width")
          driver.execute_script("arguments[0].click();", elem_pesquisa)
          
          elem_q = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/div[6]/form/input")))
          elem_q.send_keys("computer")

          elem_submit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/div[6]/form/button")))
          driver.execute_script("arguments[0].click();", elem_submit)

          elem_ok = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")))
          driver.execute_script("arguments[0].click();", elem_ok)

          elem_favoritar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((
               By.XPATH, "/html/body/div/section[2]/div/div[2]/div[1]/div/div[1]/div/a[1]")))
          elem_favoritar.click()
          
          elem_sucesso = driver.find_element(By.CLASS_NAME, "swal2-title")
          elem_wishlist = driver.find_element(By.CLASS_NAME, "swal2-html-container")

          self.assertEqual("Success", elem_sucesso.text)
          self.assertEqual("Added to Wishlist", elem_wishlist.text)

          print(" ")
          print(elem_sucesso.text)
          print(elem_wishlist.text)
          print(" ")


     def tearDown(self):
          self.driver.close()


if __name__ == "__main__":
    unittest.main()
