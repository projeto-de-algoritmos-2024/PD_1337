class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Tamanhos das strings
        n, m = len(t), len(s)
        
        # Função recursiva com memoização
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def dfs(i, j):
            # Caso base: se toda a string `t` foi percorrida, encontramos uma subsequência válida
            if i == n:
                return 1
            # Caso base: se toda a string `s` foi percorrida, mas `t` não foi completamente encontrada
            if j == m:
                return 0
            
            # Inicializa o contador de resultados
            result = 0
            
            # Se os caracteres atuais de `t` e `s` coincidem, avança em ambas as strings
            if t[i] == s[j]:
                result += dfs(i + 1, j + 1)
            
            # Avança apenas em `s` para explorar outras possibilidades
            result += dfs(i, j + 1)
            
            return result
        
        # Inicia a recursão a partir dos primeiros índices de `t` e `s`
        return dfs(0, 0)
