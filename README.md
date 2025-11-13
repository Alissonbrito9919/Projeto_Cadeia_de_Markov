📊 Calculadora de Estado Estacionário de Cadeia de Markov
Este projeto é uma implementação em Python para calcular a distribuição de estado estacionário de uma Cadeia de Markov. Como exemplo, 
ele modela a dinâmica da opinião pública (A Favor, Contra, Indeciso) sobre um projeto de lei.

O script utiliza a biblioteca Numpy e conceitos de Álgebra Linear (autovetores) para encontrar de forma eficiente a distribuição 
de equilíbrio de longo prazo, em vez de usar simulações iterativas.

O Problema: Opinião Pública
O cenário modelado é o seguinte:

Foi feito uma pesquisa para saber opinião dos eleitores sobre um projeto de lei está dividida em três estados: A favor (F), Contra (C) e Indeciso (I).

A cada mês, as opiniões mudam da seguinte forma:

De A Favor (F): 70% continuam A Favor, 10% mudam para Contra e 20% ficam Indecisos.

De Contra (C): 60% continuam Contra, 10% mudam para A Favor e 30% ficam Indecisos.

De Indeciso (I): 40% continuam Indecisos, 30% decidem-se A Favor e 30% decidem-se Contra.

Pergunta: No estado estacionário (no longo prazo), qual será o percentual de eleitores em cada grupo de opinião?

A matriz de transição (P) é definida no código:
P = np.array([
    [0.7, 0.1, 0.2],  # De F -> (Para F, Para C, Para I)
    [0.1, 0.6, 0.3],  # De C -> (Para F, Para C, Para I)
    [0.3, 0.3, 0.4]   # De I -> (Para F, Para C, Para I)
])
Para encontrar a distribuição estacionária ($\pi$), este script aplica um método de Álgebra Linear:
1-Calcula a transposta da matriz de transição (P^T).
2-Encontra os autovalores (eigenvalues) e autovetores (eigenvectors) de P^T usando numpy.linalg.eig.
3-O estado estacionário $\pi$ é o autovetor associado ao autovalor 1.
4-O vetor é então normalizado (dividido pela sua soma) para que seus componentes somem 1 e representem probabilidades.
📈 Resultado Esperado:
Ao executar o script, o console exibirá a matriz de transição e a distribuição de estado estacionário calculada:

Matriz de Transição P:
[[0.7 0.1 0.2]
 [0.1 0.6 0.3]
 [0.3 0.3 0.4]]
--------------------------------------------------
Usando: AUTOVETORES
A Favor (πF):   0.3947
Contra (πC):   0.3158
Indeciso (πI):  0.2895 
--------------------------------------------------
Estado Estacionário dos votos
A Favor: 39,47%
Contra: 31,58%
Indeciso: 28,95%
