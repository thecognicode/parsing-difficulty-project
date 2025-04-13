# Parsing Difficulty Simulation & ANOVA (Python)

This mini-project simulates human sentence processing difficulty based on syntactic structure. It is inspired by classic psycholinguistic research and uses statistical analysis to compare simulated reading times for different sentence types.

## 💡 Project Goal

To model and analyze parsing difficulty in human language processing using Python and ANOVA. This project demonstrates basic cognitive modeling and statistical analysis relevant to cognitive science and psycholinguistics.

## 🧪 Method

- Simulated reading times for three sentence types:
  - **SVO** (Subject-Verb-Object) – e.g., "The dog chased the cat." (easy)
  - **Passive** – e.g., "The cat was chased by the dog." (moderate)
  - **OSV** (Object-Subject-Verb) – e.g., "The cat the dog chased." (harder)
- Generated 30 samples per sentence type using a normal distribution
- Ran **one-way ANOVA** to test for significant differences in reading times
- Visualized results with a **Seaborn boxplot**

## 📊 Tools & Libraries

- Python 3
- `numpy`, `pandas` – for data simulation and handling
- `statsmodels` – for statistical analysis (ANOVA)
- `matplotlib`, `seaborn` – for data visualization

## 📈 Output

- Console output: ANOVA summary table
- File output: `parsing_difficulty_plot.png` – visual comparison of reading times

## 🔍 Relevance to Cognitive Science

This project reflects foundational concepts in psycholinguistics, such as parsing difficulty and sentence structure. It also demonstrates competence in empirical methods and statistical reasoning—key components in cognitive science research.

## 📁 File Structure

