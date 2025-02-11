from bisect import bisect_left
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Ordena os envelopes primeiro pela largura em ordem crescente e, em caso de empate, pela altura em ordem decrescente
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Inicializa a lista dp com a altura do primeiro envelope
        dp = [envelopes[0][1]]
        
        # Itera sobre os envelopes restantes
        for env in envelopes[1:]:
            # Se a altura do envelope atual for maior que a última altura em dp, adiciona ao final de dp
            if env[1] > dp[-1]:
                dp.append(env[1])
            else:
                # Caso contrário, encontra a posição onde a altura poderia ser inserida para manter dp ordenado
                idx = bisect_left(dp, env[1])
                dp[idx] = env[1]
        
        # O comprimento de dp representa o número máximo de envelopes que podem ser encaixados
        return len(dp)
