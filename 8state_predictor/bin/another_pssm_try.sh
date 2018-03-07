cd ~/FASTA2/
for files in *.fasta
do psiblast -query $files -evalue 0.01 -db database/uniprot_sprot.fasta -num_iterations 3 -out ../Repo_MTLS/8state_predictor/data/psiblast_files/$files.psiblast -out_ascii_pssm ../Repo_MTLS/8state_predictor/data/PSSM/$files.pssm -num_threads 8
done
