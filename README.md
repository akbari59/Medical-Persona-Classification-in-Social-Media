# Contributors

-Vini Garg
-Rama Rohit
-Rohit Dayama
-Sanket Shah

# Medical-Persona-Classification-in-Social-Media


## Problem Statement
Identifying medical persona from a social media posts like twitter and blogs is important for drug marketing and drug safety. In this project we will explore different approaches  to classify medical persona associated with the social media post.

it can be considered a multi labeled supervised text classification problem.

The task of the project is two fold :
-Manually generating additional dataset , or crawling over less dependable dataset for features.
-Medical Social media post classification.

## Dataset
We will use previously prepared data, where 1581 blogs and 1025 tweets were annotated. 
The inter-annotator agreement between 4 annotators is 0.708 for blogs and 0.70 for tweets. The label cardinality of blogs and tweets is 1.18 and 1.24 respectively. The maximum label cardinality of a blog is 2 and that of a tweet is 3.

Also, if more data is required then we will either crawl over tweets which have already been labelled or manually generate more data like our predecessors did.

## Applications:
Some of the applications of this problem statement are :
-To gather information about drug usage, adverse events, benefits and side effects from patients.  
-To find out the kind of informational assistance sought by caretakers and put such information readily available.
-To identify key opinion leaders in a drug or disease area.
-To find out if a doctor has patients who can take part in a clinical trial.
-To find information on symptoms of newly evolving diseases.
-To gather information on conversations between pharmacists and others to identify drug dosage, interactions and therapeutic effects.
-To acquire or collaborate on technologies invented by researchers that can be a part of the drug pipeline.
-To gather information about journalists’ survey on quality of life of patients.

## Challenges:

-Application of normal text ­parsing rules not applicable.  
-For example :
-Multiple Sclerosis is a disease name but Multiple could be mistaken for a common terminology.
-Our task is to identify author of the document (twitter posts) not identifying words / phrases. This makes the job of classification more difficult, as deep semantic analysis and inference is involved.
-Tweets are informal, noisy with linguistic errors and idiosyncratic style which degrades the performance of NLP tools on them.
-Learning distributed representations for medical tweets.
-Use of Non standard medical terminology.
-Entities can range from being a token to a sentence. Thus detection and delimitation of phrasal information referring to medical entities in textual corpora is a task.
-Tokenisation seems difficult ­can’t remove numbers, special characters, etc
-Spell correction and normalisation is difficult
-Entity linking for exploiting semantic features from ontologies (UMLS, MetaMap).


