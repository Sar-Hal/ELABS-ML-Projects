\# AlphaFold-Lite: Protein Secondary Structure Prediction



\## 📌 Project Overview



This project is a \*\*lightweight version inspired by AlphaFold\*\*, focused on predicting \*\*protein secondary structure\*\* (Helix, Sheet, Coil) from amino acid sequences using classical Machine Learning techniques.



Unlike AlphaFold, which is a very large deep learning model requiring huge computational resources, \*\*AlphaFold-Lite\*\* is designed to:



\* Use a \*\*small dataset\*\*

\* Run on a \*\*normal laptop\*\*

\* Be easy to understand and explain for students



---



\## 🎯 Objective



To build a \*\*simple and efficient ML model\*\* that can predict protein secondary structure using sequence-based features.



---



\## 📂 Project Structure



```

ELABS-ML-Projects/

│

├── Sritama\_AlphaFoldLite/

│   └── AlphaFoldLite\_ProteinSecondaryStructure.ipynb

│

├── protein.csv

└── README.md

```



---



\## 🧬 Dataset



\* \*\*File\*\*: `protein.csv`

\* Contains amino acid sequences and their corresponding secondary structure labels

\* Labels include:



&nbsp; \* \*\*H\*\* – Alpha Helix

&nbsp; \* \*\*E\*\* – Beta Sheet

&nbsp; \* \*\*C\*\* – Coil



---



\## ⚙️ Methodology



1\. \*\*Data Preprocessing\*\*



&nbsp;  \* Clean protein sequences

&nbsp;  \* Encode amino acids using numerical features



2\. \*\*Feature Engineering\*\*



&nbsp;  \* Amino acid frequency

&nbsp;  \* Sequence length



3\. \*\*Model Used\*\*



&nbsp;  \* Classical Machine Learning model (Logistic Regression / Random Forest)



4\. \*\*Training \& Evaluation\*\*



&nbsp;  \* Train-test split

&nbsp;  \* Accuracy used as evaluation metric



---



\## 📊 Results



\* The model achieves reasonable accuracy despite being lightweight

\* Demonstrates that \*\*small models can still be useful\*\* for biological prediction tasks



---



\## 🚀 Why AlphaFold-Lite?



| AlphaFold                      | AlphaFold-Lite        |

| ------------------------------ | --------------------- |

| Very large deep learning model | Lightweight ML model  |

| Needs huge compute             | Runs on normal laptop |

| Complex                        | Simple \& explainable  |



---



\## 🛠 Technologies Used



\* Python

\* Pandas

\* NumPy

\* Scikit-learn

\* Jupyter Notebook



---



\## 👩‍💻 Author



\*\*Sritama Kolay\*\*

Machine Learning Enthusiast



---



\## 📌 Conclusion



This project shows that \*\*domain-focused, lightweight ML models\*\* can still provide meaningful insights in protein structure prediction and are suitable for educational and small-scale research purposes.



