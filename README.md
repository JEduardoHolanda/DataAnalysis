# DataAnalysis

Nesse case, iremos estudar um banco de dados de aerogeradores fornecida pela ANEEL (Agência Nacional de Energia Elétrica). Os dados são fornecidos pela seguinte url: https://sigel.aneel.gov.br/arcgis/rest/services/PORTAL/WFS/MapServer/0/query. 

Em síntese, esse estudo de caso contém:

- **Data Extraction**: por meio de Web Scrapping, os dados da Agência Nacional de Energia Elétrica sobre aerogeradores poderão ser obtidos. A biblioteca *requests* do Python foi utilizada para esse fim;

- **Data Processing**: em resumo, processamento de dados. Visualizar a natureza dos dados, fazer o tratamento dos dados e limpeza dos mesmos a fim de que a análise seja a mais clara e mais coerente possível;

- **Data Visualization** ou **Data Analysis**: fazer análise dos dados e obter insights acerca dos dados obtidos.

# Conclusão

Para uma maior análise dos dados, um *dashboard* foi criado no site *Tableau Public*. Uma gama maior de tabelas e gráficos foram feitas para analisar os dados de aerogeradores.

De acordo com esses dashboards, em resumo, foi possível concluir que:

- O setor Nordeste possui a maior média de potência instalada por número de aerogeradores;

- O setor Sudeste possui a menor média de potência instalada por número de aerogeradores;

- Nota-se que o setor Nordeste há enorme investimento para a geração de energia eólica e para parques eólicos e maior eficiência comparado a outros setores e que baixa média do setor Sudeste pode estar associado a condições climáticas menos favoráveis ou projetos de menor escala comparados aos de outros setores.

- O nordeste possui a maior número de aerogeradores por média de capacidade instalada. Com isso, evidencia-se a alta densidade de aerogeradores para maximizar a eficiência produtiva do setor Nordeste.

- Alta correlação entre a potência instalada e o diâmetro do rotor. Portanto, evidencia-se que turbinas com rotores maiores tendem a gerar mais energia;

- Alta correlação entre altura total e potência instalada, logo evidencia-se que torre mais altas resultam em maior capacidade de geração de energia.

- Grande correlação entre a quantidade de atualizações de aerogeradores e a soma de potências instaladas: Quanto maior a soma de potências instaladas, maior a taxa de atualização e/ou de manutenção de aerogeradores.

- Grande quantidade de atualizações no setor Nordeste. Isso evidencia que ainda há altos investimentos na região.


