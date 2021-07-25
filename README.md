# Pipeline lambda com AWS CDK

Todo este projeto foi instanciado no bootcamp de engenharia de dados da HOWBootcamps, ministrado pelo senior data engineer André Sionek. Com base neste projeto realizado, montei a minha versão da sua pipeline.
--

 A imagem a abaixo mostra a pipeline desenvolvida em todo o bootcamp.

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

Dessa maneira toda implementação e na aplicação segue o seguinte cookbook:

## **1) Criação dos ambientes de trabalho**

Caso você esteja trabalhando com mais de uma pessoa em um projeto, ou mesmo sozinho é de extrema importancia **criar hábitos e boas práticas de produção**. Para isso a primeira delas é a utilização de um **ambiente de versionamento de código**, no caso deste repositorio utilizamos o git como versionador local e o github como remoto.

Outra prática é a criação de workflows que vai garantir a qualidade e veracidade de sua aplicação. Esse workflow recebe o nome de CI ou *continouos integration*, e neste estão contidos diversos testes unitários para validação de sua aplicação. Validado a aplicação vamos para o segundo round de teste. Essa parte recebe o nome de CD ou *continouos deployment*, e nesta parte vamos fazer  alguns testes de integração que vão validar como essa nova aplicação está rodando em contato com um sistema ja aplicado.

Dessa maneira temos a nossa "polícia" criada para validar a nossa aplicação. Agora podemos criar os nossos ambientes, estes serão:
* **Production** : Que seria como a nossa aplicação em execução, a utima e a mais estável.
* **Staging** : Que seria a próxima versão a ser executada mas ainda em testes.
* **Deployment** : Ambiente de criação de novas features sem afetar as ja validadas. Neste caso é mais de trabalho pessoal.

## **2) Criação da infraestrutura**

 Uma vez ouvi um cometário muito bacana que dizia "Antes de você morar em sua casa, vocẽ precisa construi-lá". Claro que você também pode aluga-la, mas o que podemos aprender com esta frase?

Para você rodar toda uma aplicação, neste caso de engenharia de dados, você precisa fudamentar toda ela. Dessa forma crie todas as suas instancias e conexões antes de começar a rodar os seus dados e pensar nos tratamentos a serem realizados.

Dessa maneira, instancie seus bancos de dados e suas conexões e gerencie alertas para governancia dos seus dados.

## **3) Criação dos seus Jobs**

Agora você passa a mudar seus móveis para sua casa e vai por aplicação em funcionamento integrando na sua infraestrutura parte a parte.

Na pasta Project_aws_cdk terá os jobs e a infraestrutura instanciadas e explicadas pontualmente.


