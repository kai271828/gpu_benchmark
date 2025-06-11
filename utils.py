import multiprocessing as mp
import psutil

import torch
import torchvision.transforms.v2 as v2
import torchvision.models
from torchvision import datasets
from torch.utils.data import DataLoader


def get_data_loader(batch_size):
    transforms = v2.Compose(
        [
            v2.ToImage(),
            v2.ToDtype(torch.float32, scale=True),
            v2.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5]),
        ]
    )

    dataset = datasets.FakeData(
        size=10000,
        image_size=(3, 224, 224),
        num_classes=10,
        transform=transforms,
    )

    num_workers = get_num_workers()

    data_loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        pin_memory=True,
        persistent_workers=True if num_workers > 0 else False,
        prefetch_factor=2 if num_workers > 0 else 2,
        drop_last=True,
    )

    return data_loader


def get_batch_size(task):
    if not torch.cuda.is_available():
        return 8

    # Get GPU memory information
    device = torch.cuda.current_device()
    gpu_memory_gb = torch.cuda.get_device_properties(device).total_memory / (1024**3)

    model_memory_requirements = {
        "resnet": 50,  # ResNet-50: ~25MB per sample (25.6M parameters)
        "swintransformer": 110,  # Swin-V2-T: ~30MB per sample (28.4M parameters, smaller than base)
        "vit": 100,  # ViT-B-16: ~35MB per sample (86.6M parameters)
    }

    if task not in model_memory_requirements:
        raise ValueError(f"Unsupported task: {task}")
    else:
        memory_per_sample = model_memory_requirements[task]

    available_memory_gb = gpu_memory_gb * 0.75  # Use 75% of total memory
    available_memory_mb = available_memory_gb * 1024

    # Calculate maximum batch size
    max_batch_size = int(available_memory_mb / memory_per_sample)

    optimal_batch_size = max(min(max_batch_size, 256), 1)

    # Round down to nearest power of 2 for optimal GPU performance
    if optimal_batch_size >= 2:
        optimal_batch_size = 2 ** int(
            torch.log2(torch.tensor(optimal_batch_size)).item()
        )

    return optimal_batch_size


def get_num_workers():
    # Get CPU count
    cpu_count = mp.cpu_count()

    # Get available memory in GB
    available_memory_gb = psutil.virtual_memory().available / (1024**3)

    # Conservative approach: use fewer workers to avoid memory pressure
    # Each worker typically uses ~100-500MB memory
    max_workers_by_memory = int(available_memory_gb / 0.5)  # Assume 0.5GB per worker

    # GPU benchmark specific logic
    if torch.cuda.is_available():
        # For GPU training, too many workers can cause CPU bottleneck
        gpu_count = torch.cuda.device_count()
        recommended_workers = min(cpu_count, gpu_count * 8)
    else:
        # For CPU training, use more workers but leave some cores free
        recommended_workers = max(1, cpu_count - 2)

    # Final decision: take minimum of all constraints
    optimal_workers = min(recommended_workers, max_workers_by_memory)

    # Ensure at least 1 worker and at most cpu_count workers
    return optimal_workers


def get_model(task, compile_model=False):
    if task == "resnet":
        model = torchvision.models.resnet50()
    elif task == "swintransformer":
        model = torchvision.models.swin_v2_t()
    elif task == "vit":
        model = torchvision.models.vit_b_16()
    else:
        raise ValueError(f"Unsupported task: {task}")

    if compile_model:
        model = torch.compile(model, mode="reduce-overhead", fullgraph=True)

    return model


def get_optimizer(model):
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)

    return optimizer


def get_criterion():
    criterion = torch.nn.CrossEntropyLoss()

    return criterion
