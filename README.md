# Simulação de Órbita - Método de Verlet

## Descrição
Este projeto simula o movimento de um corpo em órbita ao redor de uma estrela, usando uma abordagem física baseada nas leis da gravitação de Newton.

Inicialmente, foi implementado um método simples de integração numérica, o **método de Euler**, mas após perceber os erros acumulativos no cálculo da posição e velocidade do corpo, o algoritmo foi alterado para o **método de Verlet**, que é mais estável para esse tipo de simulação.

## Objetivo
O objetivo principal do projeto é simular a órbita de um corpo ao redor de uma estrela e observar as mudanças nas trajetórias dependendo dos parâmetros físicos.

## Como funciona?
1. O código usa a biblioteca **pygame** para renderizar a simulação em tempo real.
2. As forças gravitacionais entre a estrela e o corpo são calculadas com base na Lei da Gravitação Universal de Newton.
3. A aceleração do corpo é calculada a partir da força e da massa do corpo.
4. A posição do corpo é atualizada usando o **método de Verlet**, que é uma forma eficiente de integrar o movimento sem acumular erros de arredondamento significativos.

## Método de Euler vs. Método de Verlet

### Método de Euler (Inicial):
O método de Euler foi o primeiro escolhido para a simulação, pois é um método simples e intuitivo. No entanto, o método de Euler apresenta **erros acumulativos** que afetam a precisão das simulações, especialmente em sistemas com movimentos complexos e de longo prazo. Como o método usa aproximações de primeira ordem para a posição e velocidade, os erros podem crescer rapidamente, fazendo com que a órbita se distorça ao longo do tempo.

### Método de Verlet (Atual):
O método de Verlet foi adotado após os problemas com o método de Euler. Ele oferece uma solução mais estável, sem acumular erros de maneira tão significativa. O método de Verlet é particularmente adequado para simulações de partículas sob forças conservativas (como a gravitação), porque ele calcula a posição com base nas posições anteriores e atuais, sendo mais preciso em simulações com grandes intervalos de tempo.



