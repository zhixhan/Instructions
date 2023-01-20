batch_dir=data/gpt3_generations_original_seed/

python self_instruct/identify_clf_or_not.py \
    --batch_dir ${batch_dir} \
    --engine "davinci" \
    --request_batch_size 20