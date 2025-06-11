@echo off
if exist "benchmark.log" del "benchmark.log"

for %%p in (fp32 fp16 bf16) do (
    for %%t in (resnet swintransformer vit) do (
        python run_benchmark.py --task %%t --precision %%p --device cuda --compile_model
        echo.
        echo.
        python run_benchmark.py --task %%t --precision %%p --device cuda
        echo.
        echo.
    )
)

if "%~1" neq "" (
    if exist "benchmark.log" (
        move "benchmark.log" "%~1.log"
    )
)