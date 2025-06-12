import argparse
import logging
import time
import numpy as np
import torch
from torch.amp import autocast, GradScaler


from utils import (
    get_data_loader,
    get_model,
    get_optimizer,
    get_criterion,
    get_batch_size,
)


def main(args):
    # Create log filename based on benchmark parameters
    log_filename = f"{args.exp_name}.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_filename, mode="a"),
            logging.StreamHandler(),
        ],
    )

    if torch.cuda.is_available() and args.device == "cuda":
        if torch.cuda.get_device_capability()[0] < 7 and args.compile_model:
            logging.error(f"Your GPU does not support model compilation.")
            exit(1)

        if torch.cuda.get_device_capability()[0] < 8 and args.precision == "bf16":
            logging.error("Your GPU does not support BF16.")
            exit(1)

        if torch.cuda.get_device_capability()[0] >= 8:
            torch.set_float32_matmul_precision("high")
            logging.info("🚀 Enabled TF32 for faster FP32 operations")

    torch.backends.cudnn.benchmark = True

    batch_size = get_batch_size(args.task)
    if args.compile_model:
        batch_size //= 2
    if args.precision != "fp32":
        batch_size *= 2

    logging.info("=" * 60)
    logging.info(f"🚀 Starting {args.task.upper()} Training Benchmark")
    logging.info("=" * 60)
    logging.info(f"📋 Task: {args.task}")
    logging.info(f"📦 Batch Size: {batch_size}")
    logging.info(f"🎯 Precision: {args.precision}")
    if args.device.startswith("cuda") and torch.cuda.is_available():
        device_info = f"{args.device} ({torch.cuda.get_device_name(args.device)})"
    elif args.device == "cpu":
        import platform

        cpu_info = platform.processor() or platform.machine()
        device_info = f"cpu ({cpu_info})"
    else:
        device_info = args.device
    logging.info(f"💻 Device: {device_info}")
    logging.info(f"⚡ Compile Model: {args.compile_model}")
    logging.info("=" * 60)

    data_loader = get_data_loader(batch_size)
    model = get_model(args.task, args.compile_model)
    optimizer = get_optimizer(model)
    criterion = get_criterion()
    device = args.device
    time_record = []

    model = model.to(device)
    model.train()

    warmup_steps = 10 if args.compile_model else 5
    for _ in range(warmup_steps):
        with torch.no_grad():
            dummy_input = torch.randn(batch_size, 3, 224, 224, device=device)
            _ = model(dummy_input)
        if torch.cuda.is_available():
            torch.cuda.synchronize()

    scaler = (
        GradScaler(device.split(":")[0]) if args.precision in ["fp16", "bf16"] else None
    )

    # Determine autocast dtype
    autocast_dtype = None
    if args.precision == "fp16":
        autocast_dtype = torch.float16
    elif args.precision == "bf16":
        autocast_dtype = torch.bfloat16

    epoch_start_time = time.time()
    for idx, (inputs, targets) in enumerate(data_loader):
        inputs, targets = inputs.to(device=device), targets.to(device=device)

        # Synchronize GPU before timing
        if torch.cuda.is_available():
            torch.cuda.synchronize()

        start_time = time.time()

        # Use autocast for forward pass
        with autocast(
            device_type=device.split(":")[0],
            dtype=autocast_dtype,
            enabled=args.precision in ["fp16", "bf16"],
        ):
            # Forward pass
            outputs = model(inputs)
            loss = criterion(outputs, targets)

        # Backward pass
        # optimizer.zero_grad()
        for param in model.parameters():
            param.grad = None

        if scaler is not None:
            scaler.scale(loss).backward()
            scaler.step(optimizer)
            scaler.update()
        else:
            loss.backward()
            optimizer.step()

        # Synchronize GPU after timing
        if torch.cuda.is_available():
            torch.cuda.synchronize()

        elapsed_time = time.time() - start_time
        time_record.append(elapsed_time)

    epoch_end_time = time.time()
    epoch_time = epoch_end_time - epoch_start_time

    time_record = np.asarray(time_record)
    logging.info("")
    logging.info("=" * 60)
    logging.info("BENCHMARK RESULTS")
    logging.info("=" * 60)
    logging.info(f"📈 Total batches processed: {len(time_record)}")
    logging.info(f"⏱️ Total epoch time: {epoch_time:.6f} seconds")
    logging.info("-" * 40)
    logging.info("📋 Per-batch timing statistics:")
    logging.info(f"  📊 Average time: {time_record.mean():.6f} seconds")
    logging.info(f"  📏 Standard deviation: {time_record.std():.6f} seconds")
    logging.info(f"  ⚡ Minimum time: {time_record.min():.6f} seconds")
    logging.info(f"  🐌 Maximum time: {time_record.max():.6f} seconds")
    logging.info("-" * 40)
    logging.info(
        f"⭐ Estimated Throughput: {batch_size / time_record[1:].mean():.2f} samples/second"
    )
    logging.info("=" * 60)
    logging.info("")
    logging.info("")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Deep Learning Benchmark")
    parser.add_argument(
        "--task",
        type=str,
        default=None,
        choices=["resnet", "swintransformer", "vit"],
        required=True,
        help="Task to benchmark (resnet, swintransformer, or vit)",
    )
    parser.add_argument(
        "--precision",
        type=str,
        default="fp32",
        choices=["fp32", "fp16", "bf16"],
        help="Data type for model training (fp32, fp16, bf16)",
    )
    parser.add_argument(
        "--device",
        type=str,
        default="cuda" if torch.cuda.is_available() else "cpu",
        help="Device to run the benchmark on (cuda or cpu)",
    )
    parser.add_argument(
        "--compile_model",
        action="store_true",
        help="Compile the model using torch.compile",
    )
    parser.add_argument(
        "--exp_name",
        type=str,
        default="gpu_benchmark",
        help="The name of the log file.",
    )

    args = parser.parse_args()

    main(args)
