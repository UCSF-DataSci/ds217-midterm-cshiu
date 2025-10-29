#!/bin/bash

# TODO: Add shebang line: #!/bin/bash
# Assignment 5, Question 8: Pipeline Automation Script
# Run the clinical trial data analysis pipeline

# NOTE: This script assumes Q1 has already been run to create directories and generate the dataset
# NOTE: Q2 (q2_process_metadata.py) is a standalone Python fundamentals exercise, not part of the main pipeline
# NOTE: Q3 (q3_data_utils.py) is a library imported by the notebooks, not run directly
# NOTE: The main pipeline runs Q4-Q7 notebooks in order

echo "Starting clinical trial data pipeline..." > reports/pipeline_log.txt

# TODO: Run analysis notebooks in order (q4-q7) using nbconvert with error handling
# Use either `$?` or `||` operator to check exit codes and stop on failure
# Add a log entry for each notebook execution or failure
# jupyter nbconvert --execute --to notebook q4_exploration.ipynb


LOG_FILE="reports/notebook_execution_log.txt"

# Activate virtual environment
source venv/bin/activate  # or venv/bin/activate

# Initialize log file
echo "================================" > $LOG_FILE
echo "Notebook Execution Log" >> $LOG_FILE
echo "Notebook execution started: $(date)" >> $LOG_FILE
echo "" >> $LOG_FILE

run_notebook() {
    NOTEBOOK=$1
    echo "Executing $NOTEBOOK..." | tee -a $LOG_FILE
    python -m jupyter nbconvert --execute --to notebook --inplace $NOTEBOOK
    if [ $? -eq 0 ]; then
        echo "$NOTEBOOK executed successfully." | tee -a $LOG_FILE
        echo "" >> $LOG_FILE
        return 0
    else
        echo "$NOTEBOOK execution failed" | tee -a $LOG_FILE
        echo "Execution stopped due to error." | tee -a $LOG_FILE
        echo "" >> $LOG_FILE
        return 1
    fi
}

run_notebook "q4_exploration.ipynb" || exit 1
run_notebook "q5_missing_data.ipynb" || exit 1
run_notebook "q6_transformation.ipynb" || exit 1
run_notebook "q7_aggregation.ipynb" || exit 1

echo "===============================" | tee -a $LOG_FILE
echo "All notebooks executed successfully: $(date)" | tee -a $LOG_FILE
echo "===============================" | tee -a $LOG_FILE

echo "Pipeline complete!" >> reports/pipeline_log.txt

