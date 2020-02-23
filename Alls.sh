python MAIN.py ISD.txt        
ls *10.sort.bam > 10.bam.list       
ls *11.sort.bam > 11.bam.list       
ls *12.sort.bam > 12.bam.list       
ls *13.sort.bam > 13.bam.list       
ls *14.sort.bam > 14.bam.list       
ls *15.sort.bam > 15.bam.list       
ls *16.sort.bam > 16.bam.list       
ls *17.sort.bam > 17.bam.list       
ls *18.sort.bam > 18.bam.list       
ls *19.sort.bam > 19.bam.list       
ls *20.sort.bam > 20.bam.list       
ls *21.sort.bam > 21.bam.list       
ls *22.sort.bam > 22.bam.list       
ls *23.sort.bam > 23.bam.list       
ls *24.sort.bam > 24.bam.list       
ls *25.sort.bam > 25.bam.list       
ls *26.sort.bam > 26.bam.list       
ls *27.sort.bam > 27.bam.list       
ls *28.sort.bam > 28.bam.list       
ls *29.sort.bam > 29.bam.list       
ls *30.sort.bam > 30.bam.list       
ls *31.sort.bam > 31.bam.list       
ls *32.sort.bam > 32.bam.list       
ls *33.sort.bam > 33.bam.list       
ls *34.sort.bam > 34.bam.list       
ls *35.sort.bam > 35.bam.list       
ls *36.sort.bam > 36.bam.list       
ls *37.sort.bam > 37.bam.list       
ls *38.sort.bam > 38.bam.list       
ls *39.sort.bam > 39.bam.list       
ls *40.sort.bam > 40.bam.list       
ls *41.sort.bam > 41.bam.list       
ls *42.sort.bam > 42.bam.list       
ls *43.sort.bam > 43.bam.list       
ls *44.sort.bam > 44.bam.list       
ls *45.sort.bam > 45.bam.list       
ls *46.sort.bam > 46.bam.list       
ls *47.sort.bam > 47.bam.list       
ls *48.sort.bam > 48.bam.list       
ls *49.sort.bam > 49.bam.list       
ls *50.sort.bam > 50.bam.list       
samtools merge -@ 6 -b 10.bam.list 10.merge.bam    
samtools merge -@ 6 -b 11.bam.list 11.merge.bam    
samtools merge -@ 6 -b 12.bam.list 12.merge.bam    
samtools merge -@ 6 -b 13.bam.list 13.merge.bam    
samtools merge -@ 6 -b 14.bam.list 14.merge.bam    
samtools merge -@ 6 -b 15.bam.list 15.merge.bam    
samtools merge -@ 6 -b 16.bam.list 16.merge.bam    
samtools merge -@ 6 -b 17.bam.list 17.merge.bam    
samtools merge -@ 6 -b 18.bam.list 18.merge.bam    
samtools merge -@ 6 -b 19.bam.list 19.merge.bam    
samtools merge -@ 6 -b 20.bam.list 20.merge.bam    
samtools merge -@ 6 -b 21.bam.list 21.merge.bam    
samtools merge -@ 6 -b 22.bam.list 22.merge.bam    
samtools merge -@ 6 -b 23.bam.list 23.merge.bam    
samtools merge -@ 6 -b 24.bam.list 24.merge.bam    
samtools merge -@ 6 -b 25.bam.list 25.merge.bam    
samtools merge -@ 6 -b 26.bam.list 26.merge.bam    
samtools merge -@ 6 -b 27.bam.list 27.merge.bam    
samtools merge -@ 6 -b 28.bam.list 28.merge.bam    
samtools merge -@ 6 -b 29.bam.list 29.merge.bam    
samtools merge -@ 6 -b 30.bam.list 30.merge.bam    
samtools merge -@ 6 -b 31.bam.list 31.merge.bam    
samtools merge -@ 6 -b 32.bam.list 32.merge.bam    
samtools merge -@ 6 -b 33.bam.list 33.merge.bam    
samtools merge -@ 6 -b 34.bam.list 34.merge.bam    
samtools merge -@ 6 -b 35.bam.list 35.merge.bam    
samtools merge -@ 6 -b 36.bam.list 36.merge.bam    
samtools merge -@ 6 -b 37.bam.list 37.merge.bam    
samtools merge -@ 6 -b 38.bam.list 38.merge.bam    
samtools merge -@ 6 -b 39.bam.list 39.merge.bam    
samtools merge -@ 6 -b 40.bam.list 40.merge.bam    
samtools merge -@ 6 -b 41.bam.list 41.merge.bam    
samtools merge -@ 6 -b 42.bam.list 42.merge.bam    
samtools merge -@ 6 -b 43.bam.list 43.merge.bam    
samtools merge -@ 6 -b 44.bam.list 44.merge.bam    
samtools merge -@ 6 -b 45.bam.list 45.merge.bam    
samtools merge -@ 6 -b 46.bam.list 46.merge.bam    
samtools merge -@ 6 -b 47.bam.list 47.merge.bam    
samtools merge -@ 6 -b 48.bam.list 48.merge.bam    
samtools merge -@ 6 -b 49.bam.list 49.merge.bam    
samtools merge -@ 6 -b 50.bam.list 50.merge.bam    
ls *.merge.bam > bam.list       
samtools merge -@ 6 -b bam.list all.merge.bam    
samtools view all.merge.bam -@ 6 -b -o result.bam -L all.bed 
samtools index result.bam        
bedtools genomecov -bg -ibam result.bam > result.bg    
samtools fasta result.bam > result.fa      
python Res.py result.fa ISD.txt result.filt.fa      
bowtie2 -a -p 4 -x GCA_000001405.15_GRCh38_no_alt_analysis_set.fna.bowtie_index -U result.filt.fa -f -S result.sam
samtools view -F 4 -bh result.sam -o result.bam   
samtools sort result.bam -o result.sort.bam      
samtools index result.sort.bam        

