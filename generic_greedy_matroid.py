def generic_greedy_matroid(S, w, is_independent, verbose=False):
    """
    Executa o algoritmo guloso genérico para encontrar o conjunto 
    independente de peso máximo em um matróide.

    Argumentos:
    S -- O conjunto base de elementos (qualquer iterável).
    w -- Um dicionário (ou função) mapeando elementos de S para seus pesos.
         ex: {'a': 10, 'b': 20}
    is_independent -- Uma função "oráculo" (callable) que recebe um 
                      conjunto de elementos e retorna True se esse 
                      conjunto for independente, False caso contrário.
    verbose -- Se True, imprime o passo a passo da execução.
    
    Retorna:
    Um 'set' contendo os elementos do conjunto independente de peso máximo.
    """
    
    # 1. Comece com um conjunto vazio
    A = set()
    
    # 2. Ordene os elementos de S por peso, em ordem decrescente
    try:
        sorted_S = sorted(S, key=lambda x: w.get(x, 0), reverse=True)
    except Exception as e:
        print(f"Erro ao ordenar elementos. Verifique se 'w' é um mapa de pesos (dicionário).")
        print(f"Erro: {e}")
        return A

    if verbose:
        print("--- Iniciando Algoritmo Guloso Genérico ---")
        print(f"Elementos ordenados por peso: {[(x, w.get(x, 0)) for x in sorted_S]}")

    # 3. Itere pelos elementos ordenados
    for x in sorted_S:
        # 4. Tente adicionar o elemento x ao conjunto A
        temp_set = A.union({x})
        
        # 5. Use o oráculo para verificar se o novo conjunto é independente
        if is_independent(temp_set):
            # 6. Se for, adicione x permanentemente
            A = temp_set
            if verbose:
                print(f"  -> Adicionado '{x}' (Peso: {w.get(x, 0)}). Conjunto atual: {len(A)} elementos.")
        else:
            # 7. Caso contrário, descarte x
            if verbose:
                print(f"  -> Rejeitado '{x}' (Peso: {w.get(x, 0)}). Violaria a independência.")
            
    if verbose:
        print("--- Execução Concluída ---")
        
    # 8. Retorne a solução ótima
    return A