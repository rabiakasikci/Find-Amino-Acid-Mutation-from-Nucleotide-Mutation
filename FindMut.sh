
python Do_Point_Mutation.py Ref_Nuc.txt Mutation_List.txt
python Dna2Pro.py Mutation_List.txt
python Merged2File.py Ref_Protein.txt Mutation_List.txt


file_name="Mutation_List.txt"

list=()


while IFS= read -r line; do
    list+=("${line:0:${#line}-1}")
	
done < $file_name

length=${#list[@]}			

echo $length
for (( i=0; i<${length}; i++ ));			
do			
			
	echo Ref_${list[$i]}.txt
	clustalo -i Ref_${list[$i]}.txt -o CO_Ref_${list[$i]}.txt 
done
python Compare2Sequnces.py Mutation_List.txt