# Pipeline lambda com AWS CDK

Todo este projeto foi instanciado no bootcamp de engenharia de dados da HOWBootcamps, ministrado pelo senior data engineer André Sionek.
--

---
No bootcamp de engenaria de dados foi proposto a construção de uma pipeline que nos proporcionaria o contato com a ingestão, tratamento e disponibilidade de dados. Como diferencial o bootcamp focou em entregar a pipeline com automações e testes automatizados para monitoramento de cada etapa.

 A imagem a abaixo mostra a pipeline desenvolvida em todo o bootcamp.
 --

<center><img src='img/arquitetura_sionek.png'></center>

> Podemos ver que foram utilizadas as ferramentas:
> * (1) instanciamento de uma banco de dados, 
> * (2) captura de dados com DMS, 
> * (3) coleta de dados por meio de uma stream de dados com o Kinisis, 
> * (4) ingestão de dados por meio de uma API orquestrada pelo Airflow, 
> * (5) Criação das três camadas do datalake (bronze, silver, gold),
> * (6) processamento de dados via databricks(microserviço de processamento baseado no framework spark), 
> * (7) catalogo de metadados com glue catalog, 
> * (8) sistema de queries com athena, 
> * (9) implementação de um Data WareHouse com a utilização do framework DBT para gestão de um MDW(Modern Data WareHhouse) e 
> * (10) Orquestração da pipeline com Airflow.

> Todo CI/CD no bootcamp foi instanciado e monitorado por meio do GitHub Actions utilizando e criando worflows.

Com base no que foi proposto no bootcamp, resolvi implementar algumas outras funcionalidade como:

* Criar uma coleta de dados de um FTP utilizando a criação de uma **lambda function.**
* Vamos fazer uma aplicação totalmente ligada a AWS, dessa maneira retirando o uso do databricks e instanciando clusters EMR.
* Criar o controle de toda pipeline no airflow e não so a insgestão e DBT.


---
# **HANDS-ON**

Para montar esta pipeline vamos dividir todo o processo em 3 etapa de criação.
--


<h1 align="center">
     1) Criação dos ambientes de trabalho
</h1>

Caso você esteja trabalhando com mais de uma pessoa em um projeto, ou mesmo sozinho é de extrema importancia **criar hábitos e boas práticas de produção**. Para isso a primeira delas é a utilização de um **ambiente de versionamento de código**, no caso deste repositorio utilizamos o git como versionador local e o github como remoto.

Outra prática é a criação de workflows que vai garantir a qualidade e veracidade de sua aplicação. Esse workflow recebe o nome de CI ou *continouos integration*, e neste estão contidos diversos testes unitários para validação de sua aplicação. Validado a aplicação vamos para o segundo round de teste. Essa parte recebe o nome de CD ou *continouos deployment*, e nesta parte vamos fazer  alguns testes de integração que vão validar como essa nova aplicação está rodando em contato com um sistema ja aplicado.

Dessa maneira temos a nossa "polícia" criada para validar a nossa aplicação. Agora podemos criar os nossos ambientes, estes serão:
* **Production** : Que seria como a nossa aplicação em execução, a utima e a mais estável.
* **Staging** : Que seria a próxima versão a ser executada mas ainda em testes.
* **Deployment** : Ambiente de criação de novas features sem afetar as ja validadas. Neste caso é mais de trabalho pessoal.

<h1 align="center">
  2) Criação da infraestrutura
</h1>



<h1 align="center">
    3) Criação dos seus Jobs
</h1>



