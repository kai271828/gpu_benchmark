@echo off

if "%~1"=="" (
    set "EXP_NAME=gpu_benchmark"
) else (
    set "EXP_NAME=%~1"
)

if exist "%EXP_NAME%.log" del "%EXP_NAME%.log"

for %%p in (fp32 fp16 bf16) do (
    for %%t in (resnet swintransformer vit) do (
        python run_benchmark.py --task %%t --precision %%p --device cuda --compile_model --exp_name "%EXP_NAME%"
        echo.
        echo.
        python run_benchmark.py --task %%t --precision %%p --device cuda --exp_name "%EXP_NAME%"
        echo.
        echo.
    )
)