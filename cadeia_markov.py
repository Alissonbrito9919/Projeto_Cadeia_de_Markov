import numpy as np

print('######## Opinião Pública ##########')
print('Foi feito uma pesquisa para saber opinião dos eleitores sobre um projeto de lei está dividida em três estados: A favor (F), Contra (C) e Indeciso (I). \n')
texto="""
A cada mês, as opiniões mudam da seguinte forma:
De A Favor (F): 70% continuam A Favor, 10% mudam para Contra e 20% ficam Indecisos.
De Contra (C): 60% continuam Contra, 10% mudam para A Favor e 30% ficam Indecisos.
De Indeciso (I): 40% continuam Indecisos, 30% decidem-se A Favor e 30% decidem-se Contra.
Pergunta: No estado estacionário (no longo prazo), qual será o percentual de eleitores em cada grupo de opinião?
"""
print(texto)

#Matriz de trasinção P
P = np.array([
    [0.7, 0.1, 0.2],  # De F -> (Para F, Para C, Para I)
    [0.1, 0.6, 0.3],  # De C -> (Para F, Para C, Para I)
    [0.3, 0.3, 0.4]   # De I -> (Para F, Para C, Para I)
])
print("Matriz de Transição P:")
print(P)
print("-" * 50)

# 1. Pegar a transposta da matriz
# P.T inverte as linhas e colunas da matriz P.
P_t = P.T

# 2. Calcular autovalores (eigenvalues) e autovetores (eigenvectors)
# np.linalg.eig faz todo o trabalho pesado:
# 'eigenvalues' será uma lista com os autovalores (um deles será 1.0)
# 'eigenvectors' será uma matriz onde cada coluna é um autovetor
eigenvalues, eigenvectors = np.linalg.eig(P_t)

# 3. Encontrar o autovetor associado ao autovalor 1
# Define nosso alvo
target_eigenvalue = 1.0

# Encontra o índice (0, 1 ou 2) do autovalor que está MAIS PRÓXIMO de 1.0.
# np.abs(eigenvalues - target_eigenvalue) calcula a diferença
# np.argmin(...) encontra o índice da menor diferença
index = np.argmin(np.abs(eigenvalues - target_eigenvalue))

# Pega a coluna inteira (:) desse índice. Este é o nosso vetor.
stationary_vector = eigenvectors[:, index]

# 4. Normalizar o vetor para que a soma seja 1
# O vetor encontrado pode ser algo como [0.62, 0.49, 0.45] (soma != 1)
# E pode ter partes imaginárias (resíduos do cálculo)
# '.real' pega apenas a parte real (descarta o "0j")
pi_eigen = stationary_vector.real

# Divide cada elemento do vetor pela soma total do vetor.
# Isso força o vetor a somar 1, mantendo a proporção.
pi_eigen = pi_eigen / np.sum(pi_eigen)

# Imprime os resultados formatados
print("Usando: AUTOVETORES")
# pi_eigen[0] é πF, pi_eigen[1] é πC, pi_eigen[2] é πI
print(f"A Favor (πF):   {pi_eigen[0]:.4f}")
print(f"Contra (πC):   {pi_eigen[1]:.4f}")
print(f"Indeciso (πI):  {pi_eigen[2]:.4f} ")
print("-" * 50)
texto_dois="""
Estado Estacionário dos votos
A Favor: 39,47%
Contra: 31,58%
Indeciso: 28,95%
"""
print(texto_dois)