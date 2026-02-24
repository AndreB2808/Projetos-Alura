from restaurantes import Restaurante

dios = Restaurante("Dio's Café & Pizza","Pizzaria")
cazum = Restaurante("Cazum's Pudding & Co.", "Doceria")
cazum.alternar_estado()
cazum.receber_avaliacao("Teemo", 11)
cazum.receber_avaliacao("Kneez", 9)
xaulinho = Restaurante("Xaulinho Cozinhador De Porco", "Churrascaria")
xaulinho.alternar_estado()
xaulinho.receber_avaliacao("Peppa Pig", 2)
xaulinho.receber_avaliacao("Bob", 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()