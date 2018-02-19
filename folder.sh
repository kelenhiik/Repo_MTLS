#usage: bash folder.sh filename_of_project_main_directory

mkdir "$1"
cd "$1" 
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
