#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on Sun Jun  7 13:42:59 2020@author: marceloafonseca"""import numpy as npimport matplotlib.pyplot as pltfrom funcoes import ObtemDados, GraficoXY, ekf# Paremetros de inicioestado_inicial = np.array([0.0, 0.0, 0.0, 0.0, 0.0], dtype=np.float_).reshape((-1, 1))covariancia_inicial = np.array(    [        [0.0, 0.0, 0.0, 0.0, 0.0],        [0.0, 0.0, 0.0, 0.0, 0.0],        [0.0, 0.0, 0.0, 0.0, 0.0],        [0.0, 0.0, 0.0, 10.0, 0.0],        [0.0, 0.0, 0.0, 0.0, 10.0],    ],    dtype=np.float_,)# Obtendo dados do csvdados = ObtemDados("valores.csv")# Passo de previsaoestados, covariancias = ekf(    dados, estado_inicial, covariancia_inicial, com_correcao=False)# Plotando gráfico de estado deterministico em plano XYGraficoXY(estados, 0)# Imprimindo valores de covariancia para t=1000cov_x = covariancias[1000][0][0]cov_y = covariancias[1000][1][1]print()print("Para t=1000 temos:")print("Covariancia X:", cov_x)print("Covariancia Y:", cov_y)# Ganho de Kalmanestados_corrigidos, covariancias_corrigidas = ekf(    dados, estado_inicial, covariancia_inicial, com_correcao=True)cov_x = covariancias_corrigidas[1000][0][0]cov_y = covariancias_corrigidas[1000][1][1]print()print("Para t=1000 temos:")print("Covariancia corrigida X:", cov_x)print("Covariancia corrigida Y:", cov_y)GraficoXY(estados_corrigidos, 1)"""ideias para menu:    - digite nome do arquivo csv dos dados: .csv ou nao    - executar passo de previsao do EKF e correcao separados"""