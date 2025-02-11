from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Verifica se a lista de preços está vazia
        if not prices:
            return 0
        
        # Inicializa as variáveis para acompanhar as compras e vendas
        first_buy = float('inf')  # Menor preço para a primeira compra
        first_sell = 0            # Maior lucro após a primeira venda
        second_buy = float('inf') # Menor preço para a segunda compra (considerando o lucro da primeira venda)
        second_sell = 0           # Maior lucro após a segunda venda

        # Itera sobre os preços
        for price in prices:
            # Atualiza o preço da primeira compra
            first_buy = min(first_buy, price)
            # Atualiza o lucro da primeira venda
            first_sell = max(first_sell, price - first_buy)
            # Atualiza o preço da segunda compra (considerando o lucro da primeira venda)
            second_buy = min(second_buy, price - first_sell)
            # Atualiza o lucro da segunda venda
            second_sell = max(second_sell, price - second_buy)
        
        # Retorna o lucro máximo após duas transações
        return second_sell
