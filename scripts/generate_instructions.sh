
#batch_dir=data/gpt3_generations_original_seed/
batch_dir=data/data/gpt3_generations_original_tmp2/

for i in {1..5}
do
    python self_instruct/bootstrap_instructions.py \
        --batch_dir ${batch_dir} \
        --num_instructions_to_generate 50 \
        --seed_tasks_path data/seed_tasks.jsonl \
        --engine "text-davinci-003" 
done