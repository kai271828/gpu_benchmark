<a name="readme-top"></a>


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/kai271828">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">GPU Benchmark </h3>

  <p align="center">
    A simple PyTorch benchmark for testing the GPU performance of deep learning training
    <!-- <br />
    <a href="https://github.com/kai271828"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kai271828">View Demo</a>
    ·
    <a href="https://github.com/kai271828/.../issues">Report Bug</a>
    ·
    <a href="https://github.com/kai271828/.../issues">Request Feature</a>
  </p> -->
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-this-repository">About This Repository</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
    </li>
    <li>
      <a href="#reference-result">Reference Result</a>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About This Repository

This repository contains a simple PyTorch benchmark for testing GPU performance during deep learning training. It benchmarks popular models including ResNet50, Vision Transformer (ViT-S), and Swin Transformer v2 (Tiny) to help you evaluate your GPU's performance for deep learning workloads.



<!-- ### Built With -->

<!-- This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples. -->

<!-- * [![Python][Next.js]][Next-url]
* [![React][React.js]][React-url]
* [![Vue][Vue.js]][Vue-url]
* [![Angular][Angular.io]][Angular-url]
* [![Svelte][Svelte.dev]][Svelte-url]
* [![Laravel][Laravel.com]][Laravel-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JQuery][JQuery.com]][JQuery-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- GETTING STARTED -->
## Getting Started

<!-- This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps. -->

<!-- ### Prerequisites

Install packages through pip.
* pip
  ```sh
  pip install -r requirements.txt
  ``` -->

### Installation

Install packages through pip or conda.

1. Clone the repo
   ```sh
   git clone https://github.com/kai271828/gpu_benchmark.git
   cd gpu_benchmark
   ```
2. Install packages
   
   **Option 1: Using pip**
   ```sh
   pip install -r requirements.txt
   ```
   
   **Option 2: Using conda environment.yaml**
   ```sh
   conda env create -f environment.yml
   conda activate gpu_benchmark
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Linux
```bash
sh run_benchmark.sh [YOUR_EXPERIMENT_NAME]
```

### Windows
```cmd
run_benchmark.bat [YOUR_EXPERIMENT_NAME]
```


## Reference Result
Remember the performance may differ on different machines due to various hardware factors including CPU, RAM, storage, and system configuration.

### Performance Benchmarks (samples/sec)

| GPU Model | VRAM | Precision | Compile | ResNet50 | ViT-S | Swin-v2-T |
|-----------|------|-----------|---------|----------|-------|-----------|
| **GTX 1080 Ti** | 11GB | | | | | |
| | | FP32 | ❌ | 186.04 | 45.50 | 93.97 |
| | | FP16 | ❌ | 228.17 | 56.68 | 99.42 |
| **RTX 2080 Ti** | 11GB | | | | | |
| | | FP32 | ❌ | 285.70 | 87.43 | 162.64 |
| | | FP32 | ✅ | 290.70 | 86.64 | 207.21 |
| | | FP16 | ❌ | 632.09 | 252.88 | 243.74 |
| | | FP16 | ✅ | 837.97 | 265.70 | 457.09 |
| **RTX 3060** | 12GB | | | | | |
| | | FP32 | ❌ | 202.36 | 66.61 | 116.11 |
| | | FP32 | ✅ | 223.68 | 68.99 | 153.19 |
| | | FP16 | ❌ | - | - | - |
| | | FP16 | ✅ | - | - | - |
| | | BF16 | ❌ | - | - | - |
| | | BF16 | ✅ | - | - | - |
| **RTX 3080** | 10GB | | | | | |
| | | FP32 | ❌ | 435.90 | - | 235.18 |
| | | FP32 | ✅ | 465.52 | - | 313.80 |
| | | FP16 | ❌ | - | - | - |
| | | FP16 | ✅ | - | - | - |
| | | BF16 | ❌ | - | - | - |
| | | BF16 | ✅ | - | - | - |
| **RTX 3090** | 24GB | | | | | |
| | | FP32 | ❌ | - | - | - |
| | | FP32 | ✅ | - | - | - |
| | | FP16 | ❌ | - | - | - |
| | | FP16 | ✅ | - | - | - |
| | | BF16 | ❌ | - | - | - |
| | | BF16 | ✅ | - | - | - |
| **RTX 3090 Ti** | 24GB | | | | | |
| | | FP32 | ❌ | 556.69 | 198.40 | 325.77 |
| | | FP32 | ✅ | 626.94 | 214.42 | 461.40 |
| | | FP16 | ❌ | 988.34 | 432.91 | 414.51 |
| | | FP16 | ✅ | 1,300.40 | 489.87 | 836.21 |
| | | BF16 | ❌ | 909.60 | 427.35 | 411.41 |
| | | BF16 | ✅ | 1,385.43 | 492.30 | 655.00 |
| **RTX 4090** | 24GB | | | | | |
| | | FP32 | ❌ | - | - | - |
| | | FP32 | ✅ | - | - | - |
| | | FP16 | ❌ | - | - | - |
| | | FP16 | ✅ | - | - | - |
| | | BF16 | ❌ | - | - | - |
| | | BF16 | ✅ | - | - | - |
| **RTX A4000** | 16GB | | | | | |
| | | FP32 | ❌ | - | - | - |
| | | FP32 | ✅ | - | - | - |
| | | FP16 | ❌ | - | - | - |
| | | FP16 | ✅ | - | - | - |
| | | BF16 | ❌ | - | - | - |
| | | BF16 | ✅ | - | - | - |
| **RTX A6000** | 48GB | | | | | |
| | | FP32 | ❌ | - | - | - |
| | | FP32 | ✅ | - | - | - |
| | | FP16 | ❌ | - | - | - |
| | | FP16 | ✅ | - | - | - |
| | | BF16 | ❌ | - | - | - |
| | | BF16 | ✅ | - | - | - |
| **Tesla T4** | 16GB | | | | | |
| | | FP32 | ❌ | 98.94 | 29.07 | 62.33 |
| | | FP32 | ✅ | 108.49 | 30.14 | N/A |
| | | FP16 | ❌ | 215.27 | 118.35 | 112.28 |
| | | FP16 | ✅ | 358.73 | 136.05 | 214.48 |
| **Tesla V100** | 32GB | | | | | |
| | | FP32 | ❌ | 368.26 | 105.07 | 209.90 |
| | | FP32 | ✅ | 392.08 | 110.09 | 271.49 |
| | | FP16 | ❌ | 779.25 | 384.17 | 355.81 |
| | | FP16 | ✅ | 1066.69 | 439.50 | 709.32 |

### Legend
- **Compile**: PyTorch model compilation status
  - ✅ = torch.compile enabled
  - ❌ = torch.compile disabled
- **Precision Types**:
  - **FP32**: 32-bit floating point
  - **FP16**: 16-bit floating point (Half precision)
  - **BF16**: Brain Float 16-bit (Ampere+ architecture)
- **N/A**: Data not available or not tested
- **Results**: Measured in samples (3×224×224 images) processed per second during training

> 📊 **Higher values indicate better performance**

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
<!-- ## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/kai271828/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->

<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTACT -->
<!-- ## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
