cd ~/FASTA3/
for files in *.fasta
do psiblast -query $files -evalue 0.01 -db ../FASTA2/database/uniprot_sprot.fasta -num_iterations 3 -out_ascii_pssm ../Repo_MTLS/8state_predictor/data/PSSM/52_external_proteins/$files.pssm -num_threads 8
done
