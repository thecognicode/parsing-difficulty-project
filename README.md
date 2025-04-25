# 🧠 Simulating Parsing Difficulty & ANOVA Analysis

This mini-project simulates how difficult different sentence structures are to process, using Python and some basic stats. Inspired by classic psycholinguistic studies, it models reading times for different sentence types and uses ANOVA to see if those differences are statistically meaningful.

What’s the Goal?
To explore how sentence structure affects processing difficulty. We’re modeling this using simulated reading times and comparing the results with a one-way ANOVA. It’s a simple but insightful way to connect cognitive science concepts with hands-on Python code.

## How It Works

We simulate reading times for three types of English sentences:

    SVO (Subject-Verb-Object) – e.g., "The dog chased the cat." (easy)

    Passive – e.g., "The cat was chased by the dog." (moderately hard)

    OSV (Object-Subject-Verb) – e.g., "The cat the dog chased." (hardest)

## Here’s what the script does:

    Generates 30 fake “reading time” samples per sentence type using a normal distribution

    Runs a one-way ANOVA to check for significant differences

    Plots the results with a Seaborn boxplot

 ## Tools Used

    Python 3

    numpy, pandas – for data handling

    statsmodels – for the ANOVA

    matplotlib, seaborn – for visualization

## What You Get

    A console printout showing the ANOVA results

    A PNG image (parsing_difficulty_plot.png) that visualizes the simulated reading times for each sentence type

## Why It Matters

This project ties directly into psycholinguistics and cognitive science. It touches on how we mentally parse different sentence structures—and how we can simulate and analyze that with data. Plus, it’s a great example of using stats to answer a research question.

## Project Structure

parsing_difficulty_project/
- parsing_difficulty.py
- parsing_difficulty_plot.png
- README.md
- .gitignore

## How to Run It

    Make sure you’ve got Python 3 installed.

    Set up a virtual environment:

python -m venv venv

Activate the virtual environment:((depends on your OS)

Install the required packages:

pip install -r requirements.txt

Run the script:

python parsing_difficulty.py
