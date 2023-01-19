#batch_dir=data/data/gpt3_generations_original_seed/

    python self_instruct/generate_instances.py \
        --batch_dir ${batch_dir} \
        --input_file machine_generated_instructions.jsonl \
        --output_file machine_generated_instances.jsonl \
        --max_instances_to_gen 5 \
        --engine "davinci" \
        --request_batch_size 5
done