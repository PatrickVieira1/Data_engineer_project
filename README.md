# Data_engineer_project


## Introduction

The objective of this project is to pratice the most used Data Engineer tools currently in the market.

We will be using the following tools:

<li>Python</li>
<li>AWS</li>
<li>PostgreSQL</li>
<li>Apache Airflow</li>

## What we are going to do

From the government of Brazil, we are going to collect the data from their API and store it in a S3 bucket.

The data is a request of limit verification(Pedido de Verificação de Limites - PVL), which each state has to do when they need credit (money).

By web scraping the data through the API, we will be able to get the data in JSON format and then store on our bucket.

Then we will use AWS Glue to transform the data into a table and then store it on our PostgreSQL database.

After that, we will use Apache Airflow to run the ETL process and create a pipeline to run the data analysis.

Only then, our data will be ready for our analysis.



