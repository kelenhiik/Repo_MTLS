#usage: bash folder.sh and follow instructions

echo "Enter the name for your project's main directory:"
read name
mkdir "$name"
cd "$name" 
echo "This directory organizes a project that trains a SVM.
It creates folders for:
bin - scripts/binaries
src - source codes
data - has folders for training and testing sets
results - contains folders with results from training/testing and prediction results." > README.txt
mkdir bin
mkdir data
mkdir results
mkdir src
cd data
mkdir training_sets
mkdir testing_sets
cd ../results
mkdir testing_results
mkdir prediction_results
