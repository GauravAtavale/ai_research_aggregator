# AI Research Digest — 2026-11-18

## HF Daily Papers (Trending)
- **[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**  
  ⬆ 8 upvotes — Synthesizing unstructured research materials into manuscripts is an essential yet under-explored challenge in AI-driven scientific discovery. Existing autonomous writers are rigidly coupled to specific experimental pipelines, and produce superficial literature reviews. We introduce PaperOrchestra, a
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 18 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**  
  ⬆ 13 upvotes — π^4 is a unified foundation model for 4D scene perception. From diverse, uncalibrated RGB observations in the wild---a single image, an unordered collection, or a video sequence---it recovers dense geometry, camera poses, and metric scale, together with 2D/3D point tracks and moving-object masks for
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 34 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**  
  ⬆ 132 upvotes — We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D gr
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 168 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 69 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**  
  ⬆ 18 upvotes — The advent of 1-bit large language models (LLMs), led by BitNet b1.58, has
spurred interest in ternary LLMs. Despite this, research and practical
applications focusing on efficient edge inference for ternary LLMs remain
scarce. To bridge this gap, we introduce Bitnet.cpp, an inference system
optimiz
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


## HF Daily Papers (Today, by Upvotes)
- **[TeleChat to Xing4: Advancing Frontier Agentic Models on Domestic Chips and Frameworks](https://huggingface.co/papers/2611.22115)**  
  ⬆ 151 upvotes — We present Xing 4, a series of large language models that extends the TeleChat lineage through coordinated advances in model architecture and training infrastructure on Ascend. This report describes the design principles and systems engineering behind the series, spanning architecture selection, lar
- **[AscendGYM: A Cost-Aware Kernel Optimization Benchmark for Real-World Workloads on Ascend NPUs](https://huggingface.co/papers/2611.17621)**  
  ⬆ 91 upvotes — Kernel optimization is essential for efficient large language model (LLM) training and inference on Ascend NPUs. Existing Ascend kernel benchmarks primarily focus on kernel generation, with less emphasis on the ability of agents to optimize existing implementations under input configurations drawn f
- **[Weight-Space Programming Doesn't Need Transformers](https://huggingface.co/papers/2611.22055)**  
  ⬆ 51 upvotes — Standard neural architectures such as the Transformer were chosen because they train well with gradient descent and run fast on GPUs. In weight-space programming, a large language model (LLM) writes target weights by hand without gradient-based training, so those reasons no longer apply. Should we k
- **[Multi-Branch Transformer](https://huggingface.co/papers/2611.19800)**  
  ⬆ 45 upvotes — Transformer language models are commonly scaled by making their blocks wider or stacking them deeper. In this work, we explore a complementary path: branching, the parallel composition of full Transformer blocks. We introduce the Multi-Branch Transformer (MBT), which processes the input through shar
- **[ForceHarness: Turning Force into Action and Physics for Frozen Frontier Models](https://huggingface.co/papers/2611.21099)**  
  ⬆ 40 upvotes — Frontier multimodal models can now control robots zero-shot from images, yet many manipulation tasks depend on contact forces that images cannot show. Bringing force to an API-only frozen model raises two challenges. First, contact evolves much faster than an API model can decide, so the system must
- **[Breath-Dx: A Time Series Classification Benchmark for Disease Screening with eNose](https://huggingface.co/papers/2611.15348)**  
  ⬆ 32 upvotes — Electronic nose (eNose) technology offers a portable, non-invasive route for disease screening via exhaled breath analysis. However, progress in the field is hindered by the lack of systematic benchmarks that compare machine learning methods under realistic conditions, particularly sensor drift, a k
- **[Self-Improvement Memory Enables Continual Recursive Self-Improvement](https://huggingface.co/papers/2611.18856)**  
  ⬆ 31 upvotes — Harness optimization is often studied with a fixed policy model and benchmark. When either changes, the optimizer must decide which parts of an evolved harness to reuse or revise, but the harness alone may not explain why earlier edits were made or how they performed. In this work, we study Continua
- **[FastFrames: Video Generation at Interactive Latency](https://huggingface.co/papers/2611.23226)**  
  ⬆ 24 upvotes — Autoregressive video diffusion models generate frames based on new observations and inputs, making them a promising medium for interactive visual experiences. However, existing models are orders of magnitude too slow for fluid interaction. This paper introduces FastFrames, a family of fast autoregre
- **[TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation](https://huggingface.co/papers/2611.23143)**  
  ⬆ 23 upvotes — Robot manipulation videos provide a rich visual experience, yet recovering robot action and gripper-state annotations from RGB observations still remains challenging. Using the embodiment-agnostic tool-center-point (TCP) pose as the action space, we present TCP4D, a unified model in which a shared 4
- **[Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration](https://huggingface.co/papers/2611.22275)**  
  ⬆ 21 upvotes — Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framewor

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[RSIBench-Infra: Can Agents Optimize Their Own Training and Inference Infrastructure at Production Scale?](https://arxiv.org/abs/2611.24395v1)**  
  Improving the efficiency of training and inference infrastructure is a practical component of recursive self-improvement. Existing benchmarks for agent-driven optimization largely focus on individual software layers such as kernel, leaving unclear whether agents can deliver end-to-end performance ga
- **[Temporal Rank in Recurrent Neural Networks](https://arxiv.org/abs/2611.24394v1)**  
  Recurrent Neural Networks (RNNs) are a natural framework for temporal modelling, yet are often dismissed due to their sequential, non-parallelisable computation and difficulty in capturing long-range dependencies, typically attributed to vanishing and exploding gradients. We identify a distinct and 
- **[Enhancing Active Learning Performance with Initial Data Selection Based on Foundation Models](https://arxiv.org/abs/2611.24384v1)**  
  In active object detection, selecting the initial labeled pool is essential, especially in complex datasets with expensive labeling and low resource budget. This study presents an active learning framework designed to optimize the initial training cycle of active learning for the object detection ta
- **[What Majority Labels Hide: Annotator Disagreement and Model Errors in Multi-Dialect Arabic Sexism Detection](https://arxiv.org/abs/2611.24383v1)**  
  Judgements of sexism are subjective and may vary across communities, yet sexism detection datasets usually reduce annotator judgements to a single majority label, obscuring disagreement and how models behave on contested cases. We introduce MuDAS, a dataset of YouTube comments in Saudi, Egyptian and
- **[How to Turn an Attention Neural Network into an Interpretable Hard-Logic Predicate Circuit: Truth-Table Predicate Extraction and State-Machine Merging under Ship-of-Theseus Replacement](https://arxiv.org/abs/2611.24381v1)**  
  We convert a trained attention network as a whole, attention included, into a hard-logic predicate circuit that runs in its place. Every unit of the circuit is a 0/1 predicate on tokens, and every map between predicates is a minimised truth table. Short tables, such as the product of a query code an
- **[MoE-Context: Show the Model Only What It Needs](https://arxiv.org/abs/2611.24379v1)**  
  AI agents read their whole history at every step. People do not work like that: we keep what the moment needs and hold the rest as a rough note we can recall. MoE-Context applies this to language models. The context is split into blocks. Before each step a fast yes or no pass decides which blocks th
- **[LLM-Assisted Multi-Fidelity Bayesian Optimization: Fusing Expert Knowledge with Numerical Data](https://arxiv.org/abs/2611.24377v1)**  
  Multi-fidelity Bayesian optimization (MFBO) reduces engineering design cost by combining inexpensive low-fidelity (LF) models with a few accurate high-fidelity (HF) evaluations and sequentially selecting designs to evaluate. However, when HF data are scarce, the LF-HF discrepancy is difficult to lea
- **[VAFL: A Vertical Analytic Federated Learning Mechanism for Efficient Crowdsourced Services via Closed-Form Solutions](https://arxiv.org/abs/2611.24367v1)**  
  Intelligent services often rely on complementary information held by different organizations, motivating Vertical Federated Learning without centralized raw-data pooling. We propose VAFL, a Vertical Analytic Federated Learning framework that fits classification and regression heads on fixed local re
- **[PIPETTE: Prompt Injection Purple-Teaming for Robust LLM Agents](https://arxiv.org/abs/2611.24362v1)**  
  Large language model (LLM) agents routinely interact with untrusted external data, exposing them to indirect prompt injection (IPI) attacks that hijack agents into executing attacker-chosen tasks. To uncover these vulnerabilities at scale, automated red-teaming methods often leverage reinforcement l
- **[Towards Pose-Robust Few-Shot Vision-Language-Action Models](https://arxiv.org/abs/2611.24360v1)**  
  Fine-tuning a vision-language-action (VLA) model on a few dozen demonstrations is the standard way to put a manipulation policy on a robot, yet the resulting policy silently assumes that the camera and the robot base stay exactly where they were during data collection: a bumped tripod or a base re-d

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[The Silent Consensus](https://openai.com/index/the-silent-consensus)**  
  Dean Ball, Head of Strategic Futures at OpenAI, examines how more capable AI could reshape society and how people can retain control of their institutions.
- **[Research acceleration: The jagged frontier](https://openai.com/index/research-acceleration-jagged-frontier)**  
  OpenAI measures how coding agents are accelerating AI research, where their performance remains uneven, and what this signals about recursive self-improvement.
- **[How Sumitomo Life’s leaders helped teams adopt ChatGPT Enterprise](https://openai.com/business/customer-stories/sumitomo-life)**  
  Sumitomo Life uses ChatGPT Enterprise to research insurers, prepare proposals, and draft code for investment analysis. Early use by executives helped drive adoption.
- **[Inside the Codex sandbox](https://openai.com/index/inside-the-codex-sandbox)**  
  See how Codex runs commands on your machine while enforcing the filesystem and network limits you control across macOS, Linux, and Windows.
- **[Managing frontier AI risk: From training to deployment](https://openai.com/index/managing-frontier-ai-risk)**  
  OpenAI explains how it manages frontier AI risk from training through deployment with model alignment, sandboxing, blocking safeguards, and monitoring.

## Lab Blog: DeepMind
- **[Introducing Gemini 4 Neon](https://deepmind.google/blog/introducing-gemini-4-neon/)**  
  
- **[Genie 4 is now available](https://deepmind.google/blog/genie-4-is-now-available/)**  
  
- **[Introducing Gemini 4 Hydrogen](https://deepmind.google/blog/introducing-gemini-4-hydrogen/)**  
  
- **[AlphaGenome 2: Deciphering how cells read DNA to better understand disease](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)**  
  Predicting how DNA sequences and their variations impact specific human cell types and disease.
- **[Gemini 4 Carbon is now available](https://deepmind.google/blog/gemini-4-carbon-is-now-available/)**  
  

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
- **[NVIDIA RTX Spark Compact Desktops Out Now](https://blogs.nvidia.com/blog/rtx-spark-desktop-local-ai-available-now/)**  
  New NVIDIA RTX Spark compact desktops from ASUS, Dell and MSI are available today, bringing local AI agents, image and video generation, and model fine-tuning to a dedicated Windows PC. With up to 128GB of unified memory and NVIDIA’s AI software stac
- **[Ian Buck Kicks Off NVIDIA’s Week at SC26 as Science Enters the Age of Agents](https://blogs.nvidia.com/blog/ian-buck-sc26/)**  
  NVIDIA’s Ian Buck kicked off the company’s week at SC26 in Chicago on Monday with new tools for AI agents, software that can plan experiments, run code and check results on researchers’ own systems. In NVIDIA’s special address, Buck announced Nemotro
- **[NVIDIA DGX Spark Developer Kit Turns a Desk Into a Supercomputing Lab](https://blogs.nvidia.com/blog/dgx-spark-hpc-developer-kit-sc26/)**  
  At SC26, an annual supercomputing conference taking place this week in Chicago, NVIDIA is introducing the DGX Spark HPC Developer Kit for researchers, academics and developers. The kit is a four-node cluster of NVIDIA DGX Spark systems, each connecte
- **[How the World’s Most Advanced AI Infrastructure Supply Chain Invents the Future](https://blogs.nvidia.com/blog/ai-infrastructure-supply-chain/)**  
  Deb Shoquist leads operations at NVIDIA, overseeing the supply chain and manufacturing behind its AI platforms. That description sums up the job, but it doesn’t begin to encompass what Shoquist has made possible over decades. Shoquist, her team and t
- **[Lambda Boosts AI Factory Resiliency and Efficiency With NVIDIA Photonics](https://blogs.nvidia.com/blog/lambda-photonics/)**  
  To train an AI model, thousands of GPUs have to work together, requiring a network that’s fast, efficient and resilient. Lambda is tackling the network piece of the puzzle with NVIDIA Photonics co-packaged optics (CPO) switches. The cloud provider is

## Lab Blog: NVIDIA Technical Blog
- **[Build Training-Ready Physical AI Datasets with Two Prompts in NVIDIA Cosmos](https://developer.nvidia.com/blog/build-training-ready-physical-ai-datasets-with-two-prompts-in-nvidia-cosmos/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="338" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/cosmos-gif.gif" style="display: block; margin-bottom: 5px; clear: both;" title="cosmos-gif" width="600" />World m
- **[Tackling GPU Bottlenecks in Plane-Wave DFT with K-Point Batching and Mixed Precision](https://developer.nvidia.com/blog/tackling-gpu-bottlenecks-in-plane-wave-dft-with-k-point-batching-and-mixed-precision/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image4-10-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image4" width="768" />Trai
- **[Co-Designing Sparse Attention for Efficient Long-Context Inference](https://developer.nvidia.com/blog/co-designing-sparse-attention-for-efficient-long-context-inference/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/llm-optimize-deploy-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="llm-optimize-dep
- **[Integrating QPUs into Supercomputing Centers Using Slurm HRES Plugins](https://developer.nvidia.com/blog/integrating-qpus-into-supercomputing-centers-using-slurm-hres-plugins/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/hybrid-quantum-classical-computing-architecture-768x432.png" style="display: block; margin-bottom: 5px; clear: bo
- **[Accelerate Molecular Dynamics Simulations with Accurate, Flexible Primitives Using NVIDIA cuPotential](https://developer.nvidia.com/blog/accelerate-molecular-dynamics-simulations-with-accurate-flexible-primitives-using-nvidia-cupotential/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/healthcare-cupotential-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="healthcare-cu

## GitHub Trending (AI, new repos)
- **[Igniaemage/Deadline-resp-Tracker-AI](https://github.com/Igniaemage/Deadline-resp-Tracker-AI)**  
  ★ 25 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[lucidrains/supermimic-pytorch](https://github.com/lucidrains/supermimic-pytorch)**  
  ★ 13 — Unofficial implementation of Supermimic, Scaling Humanoid Whole-Body Control with One Differentiable World Model, from Qiayuan Liao et al. of Berkeley
- **[aayushch/codjiva](https://github.com/aayushch/codjiva)**  
  ★ 4 — Codjiva opens a folder like an IDE. But where an IDE shows you the text of a file, Codjiva shows you a blueprint of it: the machines, the pipes between them, the limits, and a short narrated film that
- **[sudo-nova-nsac26/sudo-nova-portfolio](https://github.com/sudo-nova-nsac26/sudo-nova-portfolio)**  
  ★ 2 — Sudo Nova’s team portfolio, built with React, showcasing our NASA Space Apps projects, open-source work, and experiments in software engineering, data, and AI.
- **[Pro-GenAI/awesome-checklists](https://github.com/Pro-GenAI/awesome-checklists)**  
  ★ 2 — ✅ Practical, reusable checklists for planning, building, reviewing, and launching software and AI products.
- **[ALANDVO/tensor-hub-145](https://github.com/ALANDVO/tensor-hub-145)**  
  ★ 2 — Alan Vo | Work in progress: tensor-hub-145
- **[ALANDVO/lumen-lab-147](https://github.com/ALANDVO/lumen-lab-147)**  
  ★ 2 — Alan Vo | Work in progress: lumen-lab-147
- **[ALANDVO/sentinel-pilot-146](https://github.com/ALANDVO/sentinel-pilot-146)**  
  ★ 2 — Alan Vo | Work in progress: sentinel-pilot-146
- **[lucidrains/torch-population](https://github.com/lucidrains/torch-population)**  
  ★ 2 — A wrapper around torch to help facilitate with population based / genetic algorithm methods
- **[ALANDVO/orbit-foundry-146](https://github.com/ALANDVO/orbit-foundry-146)**  
  ★ 2 — Alan Vo | Work in progress: orbit-foundry-146
