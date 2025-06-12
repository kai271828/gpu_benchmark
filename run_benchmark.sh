#!/bin/bash
EXP_NAME=${1:-"gpu_benchmark"}

if [ -f "./$EXP_NAME.log" ]; then
    rm "./$EXP_NAME.log"
fi

for precision in fp32 fp16 bf16; do
    for task in resnet swintransformer vit; do
        python run_benchmark.py \
            --task $task \
            --precision $precision \
            --device cuda \
            --compile_model \
            --exp_name "$EXP_NAME"
        echo ""
        echo ""
        python run_benchmark.py \
            --task $task \
            --precision $precision \
            --device cuda \
            --exp_name "$EXP_NAME"
        echo ""
        echo ""
    done
done