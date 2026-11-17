# AI Research Digest — 2026-11-17

## HF Daily Papers (Trending)
- **[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**  
  ⬆ 4 upvotes — Synthesizing unstructured research materials into manuscripts is an essential yet under-explored challenge in AI-driven scientific discovery. Existing autonomous writers are rigidly coupled to specific experimental pipelines, and produce superficial literature reviews. We introduce PaperOrchestra, a
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 33 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 17 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 169 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 71 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**  
  ⬆ 95 upvotes — We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D gr
- **[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**  
  ⬆ 105 upvotes — Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering ir
- **[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**  
  ⬆ 77 upvotes — High throughput serving of large language models (LLMs) requires batching
sufficiently many requests at a time. However, existing systems struggle
because the key-value cache (KV cache) memory for each request is huge and
grows and shrinks dynamically. When managed inefficiently, this memory can be

- **[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**  
  ⬆ 86 upvotes — Software is one of the most powerful tools that we humans have at our
disposal; it allows a skilled programmer to interact with the world in complex
and profound ways. At the same time, thanks to improvements in large language
models (LLMs), there has also been a rapid development in AI agents that

- **[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**  
  ⬆ 32 upvotes — Weight-activation quantization can reduce the memory and compute cost of neural-network inference, but recent methods often require expensive optimization and architecture-specific propagation of basis transforms across layers. We introduce MACaQ, an MXFP4 W4A4 post-training quantization method that

## HF Daily Papers (Today, by Upvotes)
- **[No papers indexed yet for 2026-11-17 (HF submissions can lag up to 14 days behind arXiv)]()**  
  

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[A Matrix with Steps: An Episodic and Procedural Memory Method for Tool-Using Agents and Robots](https://arxiv.org/abs/2611.20230v1)**  
  Agents that call tools and robots that execute tasks are challenged by two shortcomings: they repeat what failed before, and they learn from runs that they only believe succeeded. We describe the construction of a memory that addresses both, built for a production agent platform. Every run is record
- **[SWE-CoWork: Benchmarking Coding Agents as Digital Employees in Organizations](https://arxiv.org/abs/2611.20218v1)**  
  A coding agent working within a software organization must establish what to build, collaborate with colleagues, and verify what it delivers. We introduce SWE-CoWork, a benchmark comprising 101 development assignments across 101 real repositories, 11 programming languages, and 12 application domains
- **[FIDEL: Abugida-Aware Pre-tokenization for Ethiopic Languages](https://arxiv.org/abs/2611.20216v1)**  
  Subword tokenizers assume that meaningful linguistic units can be recovered by splitting text at learned boundaries, an assumption better suited to concatenative morphology than to Semitic root-and-pattern systems. The challenge is acute for the Ethiopic languages, whose abugida script encodes conso
- **[Paying Creators for Training Data Can Increase AI Displacement](https://arxiv.org/abs/2611.20204v1)**  
  Generative AI increasingly competes with creators while using their content as training data. In response, policymakers have called for platforms to compensate creators for training data use and allow opting out. We study how such policies affect creator displacement in a model of a platform where c
- **[Radar Panoptic Transformer: Semantic-Guided Mask Queries for Dynamic Scene Understanding](https://arxiv.org/abs/2611.20203v1)**  
  Automotive radar provides long-range sensing and direct Doppler velocity measurements, but its sparse and non-uniformly sampled point clouds pose significant challenges for panoptic segmentation. Dynamic objects often yield only a few detections amid a dominant static background, providing limiting 
- **[DoF-Query Transformer for Adaptive Fusion of Egocentric Vision and Forearm HD-sEMG in Continuous Hand Kinematics](https://arxiv.org/abs/2611.20196v1)**  
  Continuous and accurate estimation of human hand kinematics is important not only for intuitive human-machine interaction, but also for capturing fine-grained human manipulation demonstrations that can provide action supervision for embodied-intelligence datasets and dexterous robot learning. Howeve
- **[How Specification Explicitness Shapes Failure in LLM-Generated Code](https://arxiv.org/abs/2611.20195v1)**  
  When LLMs turn requirements into code, every underspecified constraint becomes behavior that the model must decide during generation. We test when specifications move beyond structure and begin to control generated behavior. In a controlled experiment, 72 participants implemented and revised Python 
- **[Do We Still Need Fine-Tuned Classifiers? Swapping Typed Decision Models into 24 ACL-Venue Papers](https://arxiv.org/abs/2611.20191v1)**  
  Typed Decision Models such as TypeSafe's Jev, also called System One or System 1 models, answer typed questions about an input with a probability for each option, and they need no training. Many NLP papers still fine-tune a task-specific classifier, and prompted large language models (LLMs) trail su
- **[Cyber-Secure Wearable, Ultra-Low-Power Networked Sensors for Soldier Health Monitoring: Insights from the CAPSARII project](https://arxiv.org/abs/2611.20187v1)**  
  The CAPSARII project advances a cyber-secure, ultra-low-power wearable platform and Internet of Battlefield Things (IoBT) framework to support real-time monitoring of military personnel and data-driven decision support. The architecture integrates smart-textile sensing, a body/squad area mesh, edge-
- **[RoboKit: Accelerating Parallel Differentiable Optimization for Robot Learning](https://arxiv.org/abs/2611.20185v1)**  
  We present RoboKit, a high-performance, general-purpose toolkit for parallel differentiable optimization in robotics, built on three principles: (i) Performance and flexibility: GPU-parallel multi-seed solvers pair sampling with versatile optimizers, running 2-60$\times$ faster than task-specific ba

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Broadening access to AI for scientists](https://openai.com/index/expanding-chatgpt-for-academic-researchers)**  
  We’re expanding our ChatGPT for Academic Researchers program to offer 200,000 researchers worldwide free access to our frontier models.
- **[Strengthening the fight against online child sexual abuse with new tools and support](https://openai.com/index/strengthening-online-child-safety)**  
  New tools, practical guidance, and partnerships will help prevent, detect and respond to online child sexual exploitation and abuse.
- **[Science at the Frontier: How scientists use ChatGPT](https://openai.com/index/science-at-the-frontier)**  
  Explore how more than 1,800 scientists use ChatGPT in research. See findings on daily workflows, reported productivity, and expectations for discovery.
- **[LVMH’s Media Division announces strategic partnership with OpenAI](https://openai.com/index/lvmh-media-division-partnership)**  
  LVMH’s Media Division and OpenAI announce a partnership to support journalism with AI and make its publications more accessible through ChatGPT.
- **[Our first phase of embedded assessments](https://openai.com/index/our-first-phase-of-embedded-assessments)**  
  OpenAI begins embedded assessments with Apollo Research, METR, and Transluce, and Goodfire to independently evaluate model alignment, safeguards, and monitoring systems.

## Lab Blog: DeepMind
- **[Introducing Gemini 4 Hydrogen](https://deepmind.google/blog/introducing-gemini-4-hydrogen/)**  
  
- **[AlphaGenome 2: Deciphering how cells read DNA to better understand disease](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)**  
  Predicting how DNA sequences and their variations impact specific human cell types and disease.
- **[Gemini 4 Carbon is now available](https://deepmind.google/blog/gemini-4-carbon-is-now-available/)**  
  
- **[Introducing AlphaProof Code: a breakthrough in verifying complex software at depth](https://deepmind.google/blog/introducing-alphaproof-code/)**  
  AlphaProof Code agents wrote three  million lines of proofs in Lean to verify Signal’s core encryption.
- **[Opening the datasets behind our AI weather models](https://deepmind.google/blog/opening-the-datasets-behind-our-ai-weather-models/)**  
  Foundational precipitation and geostationary satellite datasets to observe the planet clearly.

## Lab Blog: Anthropic (unofficial mirror)
- **[Investing in the public benefit](https://www.anthropic.com/news/public-benefit-fund)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><img alt="Investing in the public benefit" class="PostDetail-module-scss-module__UQuRM
- **[An update on independent evaluators](https://www.anthropic.com/news/an-update-on-independent-evaluators)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><img alt="An update on independent evaluators" class="PostDetail-module-scss-module__U
- **[Preparing for the 2026 US midterms](https://www.anthropic.com/news/2026-us-midterms)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><img alt="Preparing for the 2026 US midterms" class="PostDetail-module-scss-module__UQ
- **[Anthropic opens Singapore office and signs MOU with the Government of Singapore](https://www.anthropic.com/news/singapore-office-opening)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><div class="Illustration-module-scss-module__WyGOtq__root Illustration-module-scss-mod
- **[2026 Usage Policy update](https://www.anthropic.com/news/2026-usage-policy-update)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"></div><div class="page-wrapper"><article><div class=""><div class="Body-module-scss-module__z40yvW__body"><p class="Body-module-scss-module__z40yvW__reading-colum

## Lab Blog: NVIDIA Blog
- **[NVIDIA DGX Spark Developer Kit Turns a Desk Into a Supercomputing Lab](https://blogs.nvidia.com/blog/dgx-spark-hpc-developer-kit-sc26/)**  
  At SC26, an annual supercomputing conference taking place this week in Chicago, NVIDIA is introducing the DGX Spark HPC Developer Kit for researchers, academics and developers. The kit is a four-node cluster of NVIDIA DGX Spark systems, each connecte
- **[How the World’s Most Advanced AI Infrastructure Supply Chain Invents the Future](https://blogs.nvidia.com/blog/ai-infrastructure-supply-chain/)**  
  Deb Shoquist leads operations at NVIDIA, overseeing the supply chain and manufacturing behind its AI platforms. That description sums up the job, but it doesn’t begin to encompass what Shoquist has made possible over decades. Shoquist, her team and t
- **[Lambda Boosts AI Factory Resiliency and Efficiency With NVIDIA Photonics](https://blogs.nvidia.com/blog/lambda-photonics/)**  
  To train an AI model, thousands of GPUs have to work together, requiring a network that’s fast, efficient and resilient. Lambda is tackling the network piece of the puzzle with NVIDIA Photonics co-packaged optics (CPO) switches. The cloud provider is
- **[NVIDIA Expands Slurm to Bring Quantum Computing Into Supercomputing](https://blogs.nvidia.com/blog/slurm-quantum-computing-supercomputing/)**  
  Quantum processor deployments at supercomputing centers have grown nearly sevenfold over the past five years, with nearly 30 supercomputing centers around the world now in the process of deploying over 50 quantum processors.  Many of these centers us
- **[NVIDIA Sweeps MLPerf Training and Endpoints as Vera Rubin Debuts With Leading Performance](https://blogs.nvidia.com/blog/mlperf-training-endpoints-vera-rubin/)**  
  In its MLPerf benchmarks debut, with results released today, the NVIDIA Vera Rubin platform delivers leading performance across training, post-training and agentic inference.  NVIDIA swept every MLPerf Training v6.1 benchmark and, in its first MLPerf

## Lab Blog: NVIDIA Technical Blog
- **[Accelerate Molecular Dynamics Simulations with Accurate, Flexible Primitives Using NVIDIA cuPotential](https://developer.nvidia.com/blog/accelerate-molecular-dynamics-simulations-with-accurate-flexible-primitives-using-nvidia-cupotential/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/healthcare-cupotential-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="healthcare-cu
- **[Post-Training NVIDIA Nemotron to Increase Accuracy in Your Scientific Domain](https://developer.nvidia.com/blog/post-training-nvidia-nemotron-to-increase-accuracy-in-your-scientific-domain/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image4-5-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image4" width="768" />Agent
- **[NVIDIA Vera Rubin NVL72 Leads Agentic Inference Performance on MLPerf Endpoints v1.0](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-leads-agentic-inference-performance-on-mlperf-endpoints-v1-0/)**  
  <img alt="Two rows of black data center racks with gold-colored server components against a black background." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/mlperf-endpoin
- **[NVIDIA Vera Rubin NVL72 Achieves up to 2x Blackwell Ultra Performance in MLPerf Training v6.1](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-achieves-up-to-2x-blackwell-ultra-performance-in-mlperf-training-v6-1/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/techblog_featured2_1520x855-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="techblog
- **[Faster Scientific Simulations with New FP64 Algorithms in NVIDIA cuBLAS](https://developer.nvidia.com/blog/faster-scientific-simulations-with-new-fp64-algorithms-in-nvidia-cublas/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="431" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image5-7-768x431.png" style="display: block; margin-bottom: 5px; clear: both;" title="image5" width="768" />Many 

## GitHub Trending (AI, new repos)
- **[Igniaemage/Deadline-resp-Tracker-AI](https://github.com/Igniaemage/Deadline-resp-Tracker-AI)**  
  ★ 21 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[lucidrains/supermimic-pytorch](https://github.com/lucidrains/supermimic-pytorch)**  
  ★ 5 — Unofficial implementation of Supermimic, Scaling Humanoid Whole-Body Control with One Differentiable World Model, from Qiayuan Liao et al. of Berkeley
- **[Pro-GenAI/awesome-checklists](https://github.com/Pro-GenAI/awesome-checklists)**  
  ★ 4 — ✅ Practical, reusable checklists for planning, building, reviewing, and launching software and AI products.
- **[hanspeterdietiker/open-agent-skills](https://github.com/hanspeterdietiker/open-agent-skills)**  
  ★ 4 — Discover. Share. Build.
- **[pathbit/AgentDevKit](https://github.com/pathbit/AgentDevKit)**  
  ★ 4 — Repositório com as skills, comandos e outros que agentes de código irão utilizar.
- **[aayushch/codjiva](https://github.com/aayushch/codjiva)**  
  ★ 3 — Codjiva opens a folder like an IDE. But where an IDE shows you the text of a file, Codjiva shows you a blueprint of it: the machines, the pipes between them, the limits, and a short narrated film that
- **[notsointresting/awesome-rea-builds](https://github.com/notsointresting/awesome-rea-builds)**  
  ★ 3 — Explore 44+ real-world projects built with REA (Reverse Engineer Anything). AI-powered reverse engineering, software reconstruction, source evidence, and interactive project discovery.
- **[sudo-nova-nsac26/sudo-nova-portfolio](https://github.com/sudo-nova-nsac26/sudo-nova-portfolio)**  
  ★ 2 — Sudo Nova’s team portfolio, built with React, showcasing our NASA Space Apps projects, open-source work, and experiments in software engineering, data, and AI.
- **[ALANDVO/axiom-station-144](https://github.com/ALANDVO/axiom-station-144)**  
  ★ 2 — Alan Vo | Work in progress: axiom-station-144
- **[ALANDVO/tensor-hub-145](https://github.com/ALANDVO/tensor-hub-145)**  
  ★ 2 — Alan Vo | Work in progress: tensor-hub-145
