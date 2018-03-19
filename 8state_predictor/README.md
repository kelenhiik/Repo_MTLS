This directory organizes a project that trains a SVM.
It creates folders for:
bin - scripts/binaries
src - source codes
data - has folders for training and testing sets
results - contains folders with results from training/testing and prediction results.

__```A. RFC_eight_state_ss_predictor.py```__
Topology prediction using random forests based on sequence information. Input already provided in fasta format. Also prints the predictions out on the screen and gives directions to the .txt file.


__```B. RFC_PSFM_external_dataset_predictor.py```__


Topology prediction using random forests based on PSFM information. The input is the same as the previous one and already provided, however prediction is made using information from PSSM profiles of input proteins that have to be in the designated folder. Also prints the predictions out on the screen and gives directions to the .txt file.


__```C. RFC_singlePSFM_eight_state_predictor_pssm.py```__

 
Topology prediction using random forests based on PSFM information. The input is one PSSM profile, which is already provided, but can be easily changed in the script. Also prints the prediction out on the screen and gives directions to the .txt file.

__```D. RFC_train_predict.py```__


Since all of these models have been trained on 11 sequences and additionally compressed, because the model would otherwise be too large, the script that creates the actual model for which all the validations and results have been made for has also been provided under RFC_train_predict.py. This is the one for regular sequences. This is also coded in a way that you can basically just run it, it trains a model on 109 protein sequences, dumps it for further usage and predicts the topology for the 50 external proteins and writes it out to a file (./results/prediction_results/Prediction_from_external_dataset_seqs.txt) + the screen. Probably completely unnecessary, since it takes tons of time, but if time is not money and you want to mess around with all the parameters and use different window sizes and what not (since here you can actually change them right in the beginning), then this script allows you to train a model however you wish and predict stuff.
