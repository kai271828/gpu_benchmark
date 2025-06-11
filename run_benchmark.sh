#!/bin/bash

if [ -f "./benchmark.log" ]; then
    rm ./benchmark.log
fi

for precision in fp32 fp16 bf16; do
    for task in resnet swintransformer vit; do
        python run_benchmark.py \
            --task $task \
            --precision $precision \
            --device cuda \
            --compile_model
        echo ""
        echo ""
        python run_benchmark.py \
            --task $task \
            --precision $precision \
            --device cuda
        echo ""
        echo ""
    done
done

if [ $# -gt 0 ]; then
    if [ -f "./benchmark.log" ]; then
        mv ./benchmark.log "$1.log"
    fi
fi