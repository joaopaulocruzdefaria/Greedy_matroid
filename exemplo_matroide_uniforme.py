# Importa a função do outro arquivo
from generic_greedy_matroid import generic_greedy_matroid

# --- Definição do Problema (Matróide Uniforme U[k, n]) ---
# Queremos encontrar os 'k' elementos de maior peso.

# O conjunto S de n=5 elementos
elementos = {'a', 'b', 'c', 'd', 'e'}

# Seus pesos
pesos = {
    'a': 8,
    'b': 10,
    'c': 2,
    'd': 15,
    'e': 5
}

# Nosso limite de independência k=3
k_limite = 3

# --- O Oráculo de Independência ---
def is_independent_uniform(subconjunto):
    """
    Oráculo para Matróide Uniforme: 
    Verifica se o subconjunto tem no máximo 'k_limite' elementos.
    """
    return len(subconjunto) <= k_limite

# --- Execução do Algoritmo Genérico ---

print("--- Exemplo: Matróide Uniforme (U_3,5) ---")
solucao = generic_greedy_matroid(
    S=elementos, 
    w=pesos, 
    is_independent=is_independent_uniform,
    verbose=True  # Ativa os prints de passo a passo
)

print("\n--- Resultado Final ---")
print(f"Conjunto independente de peso máximo: {solucao}")
total_peso = sum(pesos[x] for x in solucao)
print(f"Peso total: {total_peso}")