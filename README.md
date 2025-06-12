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

| GPU Model | Memory (GB) | Precision | Compile | ResNet50 (samples/sec) | ViT-S (samples/sec) | Swin-v2-T (samples/sec) |
|-----------|-------------|-----------|---------|----------------------|-------------------|------------------------|
| **GTX 1080 Ti** | 11 | FP32 | No | - | - | - |
| | | FP32 | Yes | - | - | - |
| | | FP16 | No | - | - | - |
| | | FP16 | Yes | - | - | - |
| **RTX 2080 Ti** | 11 | FP32 | No | - | - | - |
| | | FP32 | Yes | - | - | - |
| | | FP16 | No | - | - | - |
| | | FP16 | Yes | - | - | - |
| **RTX 3090 Ti** | 24 | FP32 | No | - | - | - |
| | | FP32 | Yes | - | - | - |
| | | FP16 | No | - | - | - |
| | | FP16 | Yes | - | - | - |
| | | BF16 | No | - | - | - |
| | | BF16 | Yes | - | - | - |
| **Tesla V100** | 32 | FP32 | No | - | - | - |
| | | FP32 | Yes | - | - | - |
| | | FP16 | No | - | - | - |
| | | FP16 | Yes | - | - | - |
| | | BF16 | No | - | - | - |
| | | BF16 | Yes | - | - | - |

*Note: Results are measured in samples processed per second during training. Higher values indicate better performance.*

- **Compile**: Whether PyTorch model compilation is enabled (torch.compile)
- **Precision**: FP32 (32-bit), FP16 (16-bit), BF16 (Brain Float 16-bit)


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
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/kai271828/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/kai271828/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kai271828/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/kai271828/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/kai271828/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/kai271828/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/kai271828/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/kai271828/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/kai271828/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/kai271828/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kai271828
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com  -->
