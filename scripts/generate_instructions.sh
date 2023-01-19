
batch_dir=data/gpt3_generations_original_seed/

for i in {1..50}
do
    export AKEY=$(az account get-access-token --resource https://ml.azure.com -o tsv | cut -d $'\t' -f1)
    python self_instruct/bootstrap_instructions.py \
        --batch_dir ${batch_dir} \
        --num_instructions_to_generate 50000 \
        --seed_tasks_path data/seed_tasks.jsonl \
        --engine "text-davinci-003" 
done