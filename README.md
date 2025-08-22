
# Automatic Paraphrase Categorization with Large Language Models
--------------------------------------------------
  A master's thesis research project on the first systematic ontology-driven paraphrase categorization for Slovenian language using large language models.

  Abstract

    Paraphrase categorization involves systematic classification of different types of linguistic transformations that preserve text meaning while changing surface form. Automatic paraphrase categorization contributes to better understanding of linguistic structures and improves interpretability of natural language processing systems. In this work, we developed the first systematic approach to ontology-driven paraphrase categorization for Slovenian, based on large language models. Due to the specificity of Slovenian as a less-resourced language, we tested the specialized GaMS-1B model and the multilingual LLaMA-3.1-8B model. Both are based on transformer architecture, which currently dominates the field of natural language processing. From four English paraphrase corpora, we obtained examples, translated them into Slovenian, and thus created a training dataset with 372 annotated paraphrase pairs. The dataset is useful for further research and building models for Slovenian paraphrase categorization. We developed a two-level ontological schema with four main categories and twelve subcategories and used it to fine-tune the models, which we evaluated with multidimensional metrics and qualitatively with human judgment. The GaMS model achieved better results in syntactic and pragmatic paraphrasing, while LLaMA performed better in lexical and semantic paraphrasing. Through analysis of the results, we identified suitable training set sizes and showed that large language models require only 6-8 examples per category for successful categorization.<img width="468" height="409" alt="image" src="https://github.com/user-attachments/assets/79bc8b7d-6064-4f3d-b675-7e306e24ad8b" />

  ### Project Overview
    This repository contains research materials and implementation of the master's thesis "Strojna kategorizacija parafraz z velikimi jezikovnimi modeli" (Automatic Paraphrase Categorization with Large Language Models) - the first systematic approach to paraphrase categorization in Slovenian.

  ### Research Objectives
    The project addresses three key research questions:

    - Can paraphrasing reasons be categorized into machine-understandable categories?
    - How successfully do large language models learn paraphrase categorization?
    - What dataset size is required for effective categorization across different model types?

--------------------------------------------------
## Repository Structure
--------------------------------------------------

  ### Key files and their content:

- Datasets:

  training_dataset_final.csv - Final training dataset with 372 Slovenian paraphrase pairs
  paraphrase_dataset_analysis_with_metadata.csv - Dataset with calculated similarity metrics

- Jupyter Notebooks - main implementation:

  preprocessing_datasets_metrics_cleaned.ipynb - Creation of Slovenian training dataset with metrics
  training_and_learning_step_cleaned.ipynb - In-context learning with pre-trained models
  Finetuning_models.ipynb - Weight adaptation using LoRA technique
  paraphrase_datasets_translations_GPT3_5.ipynb - Translation of English paraphrase collections with GPT-3.5

- Results and analyses:

  Rezultati few in zero shot učenja_GaMS in LlaMa.docx - Zero-shot and few-shot learning results
  Translation Comparison - google translate, gpt, deepl, GaMS.xlsx - Translation service comparison on sample examples

- Ontological schema:

  ontološka_shema_rezervna/ - Folder with ontological categorization schema
  paraphrase_schema_slo.json - JSON schema (unused)

- Supporting files:

  backup_preprocessing/ - Preprocessing backup copies

--------------------------------------------------
## Key Contributions:
--------------------------------------------------

1. Methodological Innovations

  First ontology-driven paraphrase categorization system for Slovenian
  Two-level hierarchical schema: 4 main categories + 12 subcategories
  Comparative analysis of specialized (GaMS-1B) vs. multilingual (LLaMA-3.1-8B) models
  Optimal dataset size: 6-8 examples per category sufficient

2. Technical Achievements

  Curated dataset: 372 manually annotated Slovenian paraphrase pairs
  Multi-approach evaluation: Zero-shot, few-shot, and LoRA fine-tuning
  Comprehensive metrics: Semantic, lexical, and hierarchical evaluation
  Parameter efficiency: 1874x reduction in trainable parameters using LoRA

3. Main Results

    ### Average Model Performance
  | Model | Average Accuracy | Best Configuration | Experiment Success | Parsing Success Rate |
  |-------|------------------|-------------------|-------------------|---------------------|
  | **GaMS-1B** | 23.6% ± 21.5% | prompt with 2 examples/category (100%) | 68.8% (77 of 112 tests) | 37.7% ± 29.4% |
  | **LLaMA-3.1-8B** | 23.8% ± 18.8% | prompt with 1 example/category (100%) | 82.1% (92 of 112 tests) | 56.9% ± 31.8% |
  
  ### Performance by Main Categories
  
  **GaMS-1B:**
  | Category | Performance |
  |----------|-------------|
  | Syntactic paraphrasing | 76.0% ± 16.0% |
  | Pragmatic paraphrasing | 73.8% ± 11.2% |
  | Lexical paraphrasing | 66.7% ± 20.1% |
  | Semantic paraphrasing | 46.7% ± 22.1% |
  
  **LLaMA-3.1-8B:**
  | Category | Performance |
  |----------|-------------|
  | Lexical paraphrasing | 70.2% ± 13.4% |
  | Pragmatic paraphrasing | 66.9% ± 18.0% |
  | Semantic paraphrasing | 61.3% ± 19.1% |
  | Syntactic paraphrasing | 57.3% ± 23.7% |
  
  ### LoRA Fine-tuning Results
  | Model | Post-LoRA Accuracy | Trainable Parameters | Percentage of Total Model |
  |-------|-------------------|---------------------|-------------------------|
  | **LLaMA-3.1-8B** | 18.3% | 6,815,744 | 0.083% |
  | **GaMS-1B** | 14.2% | 2,359,296 | 0.251% |
  
  ### Classical Machine Learning (Binary Classification)
  | Model | Classification Accuracy | F1-Score |
  |-------|------------------------|----------|
  | Random Forest | 67.25% ± 2.19% | 70.40% ± 2.83% |
  | SVM | 66.00% ± 6.42% | 69.89% ± 6.33% |

  ### Ontological Framework:
  
      Four Main Categories

      Lexical (leksikalno_parafraziranje): Vocabulary changes
      Syntactic (sintaktično_parafraziranje): Structural transformations
      Semantic (semantično_parafraziranje): Meaning modifications
      Pragmatic (pragmatično_parafraziranje): Contextual adaptations
      
      Twelve Subcategories
      
      Semantic: Synonym substitution, antonym with negation, hierarchical relations (hypernym/hyponym)
      Syntactic: Word order changes, active/passive voice conversion, nominalization
      Pragmatic: Modality changes, focus shifts, register adaptation
      Lexical: Temporal-aspectual changes, text expansion/compression, sentence type conversion

--------------------------------------------------
## How to Use
--------------------------------------------------

1. Data Preprocessing
  jupyter - Open preprocessing_datasets_metrics_cleaned.ipynb
  Notebook contains complete processing of English corpora into Slovenian training set

2. Model Training
  jupyter - For zero-shot and few-shot learning:
  training_and_learning_step_cleaned.ipynb

  For weight adaptation:
    Finetuning_models.ipynb
  
3. Translation
  jupyter - For translating English paraphrases:
  paraphrase_datasets_translations_GPT3_5.ipynb

--------------------------------------------------
## Key Findings
--------------------------------------------------

Dataset Size Optimization

  Classical machine learning: Requires 400-600 examples for binary classification
  Large language models: Optimal with 48-192 examples (8-12x reduction)
  GaMS model: Achieves optimal results with only 48 samples for twelve subcategories
  LLaMA model: Needs 4 examples for basic categorization, 192 samples for subcategories


Model Specialization

  GaMS: Superior results in syntactic and pragmatic paraphrasing
  LLaMA: Better at lexical and semantic paraphrasing
  GaMS top subcategories: Word order changes (95.5%), synonym substitution (89.7%)
  LLaMA top subcategories: Hypernym/hyponym (90.8%), nominalization (89.7%)

Translation Service Comparison
Translation evaluation results are in Translation Comparison - google translate, gpt, deepl, GaMS.xlsx:

  ChatGPT: Best overall quality
  DeepL: Good alternative with some errors
  GaMS: More creative translations but with grammatical errors


Technical Stack

Models: GaMS-1B (Slovenian-specialized), LLaMA-3.1-8B (multilingual)
Fine-tuning: LoRA (Low-Rank Adaptation) for parameter efficiency
Translation: Comparative evaluation of ChatGPT, DeepL, GaMS
Processing: Classla for Slovenian language processing
Evaluation: Multi-dimensional metrics (LaBSE, METEOR, Word Jaccard)

--------------------------------------------------

Citation
bibtex@mastersthesis{zumer2025paraphrasing,
  title={Strojna kategorizacija parafraz z velikimi jezikovnimi modeli},
  author={Žumer, Alenka},
  year={2025},
  school={University of Ljubljana, Joint Interdisciplinary Master's Programme in Cognitive Science},
  type={Master's thesis},
  address={Ljubljana, Slovenia},
  supervisor={Robnik-Šikonja, Marko}
}


Contributions are welcome! If you find issues, have suggestions for improvements, or want to extend the research, feel free to open an issue or submit a pull request. This includes:

Bug fixes in the code
Improvements to the documentation
Extensions to the ontological schema
Additional experiments or analyses
Translation improvements


Contact

Author: Alenka Žumer
Supervisor: Prof. Dr. Marko Robnik-Šikonja
Institution: University of Ljubljana, Cognitive Science Programme


Keywords: paraphrasing, natural language processing, large language models, ontologies, categorization, Slovenian language, transformer architecture, LoRA fine-tuning
