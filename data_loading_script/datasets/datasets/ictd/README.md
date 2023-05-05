---
annotations_creators:
- other
language_creators:
- other
languages:
- en-US
licenses:
- apache-2.0
multilinguality:
- monolingual
pretty_name: 'ICTD: IA choosing table dataset'
size_categories:
- unknown
source_datasets:
- original
task_categories:
- text-classification
task_ids:
- entity-linking-classification

---
# Dataset Card for ICTD

## Table of Contents
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-instances)
  - [Data Splits](#data-instances)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)

## Dataset Description

- **Homepage:** https://surajjkumar.github.io/
- **Repository:** https://github.com/surajjkumar/surajjkumar.github.io
- **Paper:** N/A
- **Leaderboard:** N/A
- **Point of Contact:** Suraj Kumar
suraj.kumar@infiniteanalytics.com

### Dataset Summary

ICTD(IA choosing table dataset): "This new dataset is designed to assign a table/schema to any natural language query as an input. The task in hand is to create a search engine via making a SQL query in between and running the SQL query on any database. Now to get the result from the database, one can train the NLQ-dataset pair where we will run the SQL query on a particular dataset/table.  
for example, "all campaigns that are active" is related to "campaign" table. and "number of houses with 5 bedrooms" 
is related to well being table."

### Supported Tasks and Leaderboards

The dataset can be used to train a model for classify NLQ, which consists in classifying any natural language query to it's related dataset.

### Languages

English

## Dataset Structure

### Data Instances

A data point comprises a natural language query('NLQ'), which is the input and a table/dataset name corresponding to the NLQ. 
An example from the classify_NLQ test set looks as follows:
{'nlq': 'all campaigns that are active'
'table': 'campaign'
}

### Data Fields

- nlq: a string query to be put as an input.
- table: a table/dataset in any database to run our SQL query at 

### Data Splits

The data is split into a training and validation set.

## Dataset Creation

### Curation Rationale

ICTD was built to provide a testbed for machines to learn the understanding of any Natural Language query and then assigning a table/dataset to the NLQ. This dataset was built by generating natural language query to get SQL query for the same using transformers model. Now after a table/dataset is assigned to any NLQ, we will run the SQL query generated on the database for that particular table/dataset.

### Source Data

#### Initial Data Collection and Normalization

The data was obtained by generating natural language query and assigning a table/dataset to that NLQ.

#### Who are the source language producers?

Used English language and produced the dataset myself.

### Annotations

#### Annotation process

[N/A]

#### Who are the annotators?

N/A

### Personal and Sensitive Information

This data contains Natural language queries which is asked on any search engine around the web

## Considerations for Using the Data

### Social Impact of Dataset

[Needs More Information]

### Discussion of Biases

[Needs More Information]

### Other Known Limitations

[Needs More Information]

## Additional Information

### Dataset Curators

[Needs More Information]

### Licensing Information

[Needs More Information]

### Citation Information

[Needs More Information]