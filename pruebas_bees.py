from valuador import Valuador_Bees

valuador = Valuador_Bees('s%3AZ4iTsymzv47sSN35LpCT53O4Jq8PbDNJ.9%2FLi7rFcVQeXhbAz6ywVQXM5XoO4Or1gm3TGqgzkLrQ')

bees = {'7777': ['QUILMES CLASICA 473CC 4X6', '324238490328', 'BEES', '2218'], 
        '6666': ['7UP REGULAR 2250CC X8', '3948203480932', 'BEES','19342']
        }

bees = valuador.get_prices(bees)

print(bees)

