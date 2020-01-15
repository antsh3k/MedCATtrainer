# MedCAT: User guide

Version 1
November 2019
 
## Introduction

### 1.1	What is MedCAT?

MedCAT stands for MEDical Concept Annotation Tool. It is a simple information extraction platform where documents containing unstructured/free text can be annotated/labelled with concepts from any chosen dictionary. It has the ability to utilise the most recent advances in natural language processing (NLP) to assist with the annotation process. This means that as a user begins to annotation a set of documents this tool will learn from previous annotations to assist in automatically annotating future documents with increasing accuracy. The user can then simply transition from annotating to validating each prediction. This enables users to annotate 100s of documents, at a rate much faster than by conventional methods, to create a large corpus of annotated documents.

This User guide will walk though:
1) How to access and use the software.
2) Define the Annotation task. The project, Aims and objectives, and what is the annotator required to do?

 
## User interface

### 2.1	Getting started

Before you begin you must have received the appropriate permissions from a MedCAT user with administrator permissions.

A MedCAT Admin user will send you 3 things:
1)	Username
2)	Password
3)	A Link to access MedCAT from within the KCH network


#### 2.1.1 Logging on
To access MedCAT within an NHS Trust, please follow this link and log in with your MedCAT credentials:

1)	Enter the link into the address bar of any web browser (Google Chrome, Internet Explorer, Firefox etc)
2)	A user ID and password is required to log onto web interface.

 

If you have any difficulties with logging in or wish to change your password, please contact the MedCAT team. 
#### 2.1.2 Logging off

In the top right-hand corner of every page there is a “logout” button. Please click here to log out.
 

#### 2.1.3 Changing Username and Password

Only a user with MedCAT Admin Privileges can add users to a project and set usernames and passwords.

Username requirements: 
•	150 characters or fewer. Letters, digits and @/./+/-/_ only.

Password requirements:
•	Not similar to your other personal information.
•	Contains at least 8 characters.
•	Not a commonly used password.
•	Not entirely Numeric.


Please contact your project manager or a person with MedCAT Admin Privileges to change your username or password.



### 2.2	MedCAT Dashboard

Once have logged in you. This will bring you to the main MedCAT Dashboard:

 

1.	Project ID – The ID number of a project
2.	Title – Project Title
3.	Description – The Description of the project should contain information of the annotation task which the documents must be annotated by.
4.	Create Time – Date which the project was created
5.	UMLS Concepts – A positive Filter of the concepts which the documents are to be annotated.
6.	UMLS Terms – A positive Filter of the Terms which the documents are to be annotated.
7.	Annotate/Validate – Denotes whether these documents should be annotated/validated.
8.	Save Model – To download your set of annotated documents.


### 2.3	Annotation Project

#### 2.3.1 Annotation User Interface
Selecting an annotation project will bring you to the following interface:

 

#### 2.3.2 Annotating a document
During the annotation of the document. The significance of each annotation within the document will be highlighted according to the colour scheme in the following table:


|Annotation Label	|Significance	|Colour|
|---|---|---|
|Current concept|	The current word/concept which the user is labelling|	BOLD|
|Predicted Unlabelled concepts|	These are words which have a predicted annotation label. These should be validated.|	Grey|
|Correct labelled concepts|	Word/concept with correct annotation label|	Blue|
|Incorrect labelled concepts|	Word/concept with an incorrect annotation label|	Red|
|Terminate a concept|	Word/concept which have been terminated from the dictionary due to their irrelevance.|	Pink|

#### 2.3.3 Adding a missing annotation

To add a missing annotation label. Highlight the section of text which you would label. Then right click this area. “Add Synonym” will appear. 

In the below example: “epileptic seizures” has been annotated as epilepsy. However, this is incorrect. Instead “non epileptic seizures” should be annotated and provided with an annotation. The below image highlights the text of interest and right clicks to add synonym.


The user will be required to ensure that the New annotation has entirely covered the correct corresponding portion of text for annotation.
 

Click add synonym to add the concept to the document.

##### 2.3.3.1 Search for a concept label:
To attach an appropriate label to a concept: You can search a dictionary by its entries or through the concept code. 

For example: for the UMLS you can label the word “seizure” by searching “seizure” or the CUI: “C0036572” 
Please select the most appropriate label.



Search for UMLS concepts
If the project is using UMLS as the concept database. You will need to create a UMLS Terminology services account to access this feature. For those who have an account, you can search for further information of the CUI and TUI here: 


CUI: To find a list of all possible CUIs please see: https://uts.nlm.nih.gov/metathesaurus.html

TUI: To find a list of all possible TUIs please see: https://metamap.nlm.nih.gov/Docs/SemanticTypes_2018AB.txt




Search for SNOMED concepts
If the project is using SNOMED as the concept database. You can search for further information of the here: https://termbrowser.nhs.uk/


Here you can search for terms and find the SNOMED Concept IDs (SCTID)
 


#### 2.3.4 Adding an alternative concept
Similar to adding a new concept you can add an alternative concept.
You will be required to add a synonym when a concept is labelled incorrectly given the context in which it is used. An example of this is “The patient with epilepsy had a fit” and “fit” is labelled as “healthy and well”. Instead “fit” should be labelled as “Seizure”. 



#### 2.3.4 Terminating an annotation
If a word is being annotated completely incorrect to your objectives in your project. You can terminate the annotation. This will completely remove all annotations of that word from appearing in all future documents.

 
**WARNING:** Terminating an annotation will completely remove this predict from all future annotations. Before you select this option consider if this annotated concept has the possibility to appear correctly within the task in which you are annotating for. If the answer to this question is YES, instead select the “incorrect” annotation button to mark that annotation as wrong. If the answer is NO, then proceed to terminate the incorrect prediction. 


#### 2.3.4 Add a Meta-annotation
If your project requires meta-annotations, they will have been set by your project administrator. A list of possible meta-annotations associated with the project will appear in the right-hand side box as shown below. Please choose the most appropriate meta-annotation for the annotation. 


#### 2.3.5 Submitting a document
Once the user is satisfied that all the required information contained within the document is correctly labelled. The User can then Submit the document by pressing the submit button at the bottom right hand side of the page. Users will then be required to confirm the submission to proceed. Once confirmed, this will automatically save the document which you have annotated and then move you onto the next document.


#### 2.3.6 Short Cuts and Hotkeys
Selecting the grey question mark box (?) in the top right-hand corner will bring up this popup:

All Hotkeys are shown below:

|Hotkey| Function|
|---|---|
|1|	Correct annotation|
|2|	Incorrect annotation|
|3|	Terminate|
|4|	Add synonym|
|Enter/Return (⏎)|	Submit a document|
|Leftwards Arrow (←)|	Previous annotation|
|Rightwards Arrow (→)|	Next annotation|
|Up Arrow (↑)|	Previous document|
|Down Arrow (↓)|	Next document|


#### 2.4	Acronyms and Abbreviations 

NLP – Natural Language Processing
EHR – Electronic Health Record

UMLS – Unified Medical Language System
CUI – Concept Unique Identifier
TUI – Term Unique Identifier

SNOMED CT - Systematized Nomenclature of Medicine - Clinical Terms


#### 2.5	Glossary

Annotation: A note by means of a comment added to a meaningful word from the sentence. For example, to annotate mentions of diseases with UMLS codes within a sentence: “The patient has no family history of epilepsy” {Epilepsy, CUI: C0014544, TUI: T047}. This denotes that the word epilepsy is a disease which can be found within UMLS Metathesaurus under CUI: C0014544, or TUI: T047.

Meta-annotation: A meta-annotation is an annotation that can be applied to another pre-existing annotation. A meta-annotation is usually used to provide further information of the context of the pre-existing annotation. For example: “The patient has a negative family history of epilepsy” {Epilepsy, Negation: negative, Attribution: Family} This denotes that the annotation epilepsy is a negative mention and is mentioned in a context which refers to the Family.


#### 2.6	Help

If any questions arise or if any problems are encountered during the use of the program. Please contact anthony.shek@kcl.ac.uk for assistance.

