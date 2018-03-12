cd ~/FASTA2/

psiblast -query '>D1A04.fasta' -evalue 0.01 -db database/uniprot_sprot.fasta -num_iterations 3 -out ../Repo_MTLS/8state_predictor/data/psiblast_files/'>D1A04.fasta.psiblast' -out_ascii_pssm ../PSSM/'>D1A04.fasta.pssm' -num_threads 8

