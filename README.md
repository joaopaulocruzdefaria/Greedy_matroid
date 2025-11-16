
# Implementação de Algoritmo Guloso Genérico para Matróides

Este repositório contém uma implementação em Python do algoritmo guloso genérico para encontrar o conjunto independente de peso máximo em um matróide.

Este código serve como material suplementar para o artigo:
**"Estratégias Avançadas de Projeto e Análise de Algoritmos: Algoritmos Gulosos"**
*Disciplina: Algoritmos e Estruturas de Dados II*
*Instituição: CEFET-MG*
*Autores: Fabricio Quintilhiano, Fernando Siratuti, Hugo Marques, João Paulo Cruz, Otávio Hiratsuka, Pedro Galvão, Vinicius Ramalho, William Leão*
*Data: Novembro, 2025*

---

## O Algoritmo Genérico

O algoritmo está implementado no arquivo `generic_greedy_matroid.py` e segue o pseudocódigo canônico (conforme Cormen et al., 2012, e o Algoritmo 5 do artigo).

## Exemplo de Uso: Matróide Uniforme

O algoritmo é demonstrado com o **Matróide Uniforme** ($U_{k,n}$).

  * **Problema:** Encontrar os k elementos de maior peso em um conjunto S de n elementos.
  * **Oráculo `is_independent`**: A função oráculo (`is_independent_uniform`) simplesmente verifica se o tamanho do subconjunto é menor ou igual a $k$.

O script `exemplo_matroide_uniforme.py` importa o algoritmo genérico e o aplica a este problema.

### Como Executar o Exemplo

```bash
# Executa o exemplo do matróide uniforme
python exemplo_matroide_uniforme.py
```

