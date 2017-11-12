# Contributors

    Vini Garg
    Rama Rohit
    Rohit Dayama
    Sanket Shah

# Medical-Persona-Classification-in-Social-Media

## Problem Statement

Identifying medical persona from a social media posts like twitter and blogs is important for drug marketing and drug safety. In this project we will explore different approaches  to classify medical persona associated with the social media post. It can be considered a multi labeled supervised text classification problem.

The task of the project is two fold :

* Manually generating additional dataset , or crawling over less dependable dataset for features.

* Medical Social media post classification.

## Dataset
We will use dataset with 1971 tweets extracted from twitter and annotated manually. 

The label cardinality tweets is 1.8 . The maximum label cardinality of a tweet is 3.

### Approaches
1. Semi Supervised Approach
We collected the handles of different people belonging to different persona, on basis of of the popularity of the person.
We then crawled tweets made by these handles, using TwitterSearch API. 

2. Supervised Approach
While crawling some filters were applied to retrieve tweets of medical domain only by the selected handle users. Noisy tweets were removed . Like ones which aren’t relevant to medical field. For example: Top400 drugs used in medicines were treated as a filter parameter.
Then resulted tweets were then manually annotated as:
* Positive / Negative / Neutral Sentiment
* Possible personna like Patient, Caretaker, Consultant, etc.

## Applications:
Some of the applications of this problem statement are :

* To gather information about drug usage, adverse events, benefits and side effects from patients.  

* To find out the kind of informational assistance sought by caretakers and put such information readily available.

* To identify key opinion leaders in a drug or disease area.

* To find out if a doctor has patients who can take part in a clinical trial.

* To find information on symptoms of newly evolving diseases.

* To gather information on conversations between pharmacists and others to identify drug dosage, interactions and therapeutic effects.

* To acquire or collaborate on technologies invented by researchers that can be a part of the drug pipeline.

* To gather information about journalists’ survey on quality of life of patients.

## Challenges:
Application of normal text parsing rules not applicable.  

For example :

* Multiple Sclerosis is a disease name but Multiple could be mistaken for a common terminology.

* Our task is to identify author of the document (twitter posts) not identifying words / phrases. This makes the job of classification more difficult, as deep semantic analysis and inference is involved.

* Tweets are informal, noisy with linguistic errors and idiosyncratic style which degrades the performance of NLP tools on them.

* Learning distributed representations for medical tweets.

* Use of Non standard medical terminology.

* Entities can range from being a token to a sentence. Thus detection and delimitation of phrasal information referring to medical entities in textual corpora is a task.

* Tokenisation seems difficult can’t remove numbers, special characters, etc

* Spell correction and normalisation is difficult

* Entity linking for exploiting semantic features from ontologies (UMLS, MetaMap).
