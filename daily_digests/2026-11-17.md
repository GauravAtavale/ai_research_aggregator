# AI Research Digest — 2026-11-17

## HF Daily Papers (Trending)
- **[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**  
  ⬆ 8 upvotes — Synthesizing unstructured research materials into manuscripts is an essential yet under-explored challenge in AI-driven scientific discovery. Existing autonomous writers are rigidly coupled to specific experimental pipelines, and produce superficial literature reviews. We introduce PaperOrchestra, a
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 17 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 33 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**  
  ⬆ 122 upvotes — We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D gr
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 169 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 71 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://huggingface.co/papers/1910.03771)**  
  ⬆ 34 upvotes — Recent progress in natural language processing has been driven by advances in
both model architecture and model pretraining. Transformer architectures have
facilitated building higher-capacity models and pretraining has made it
possible to effectively utilize this capacity for a wide variety of task
- **[PyTorch Distributed: Experiences on Accelerating Data Parallel Training](https://huggingface.co/papers/2006.15704)**  
  ⬆ 15 upvotes — This paper presents the design, implementation, and evaluation of the PyTorch
distributed data parallel module. PyTorch is a widely-adopted scientific
computing package used in deep learning research and applications. Recent
advances in deep learning argue for the value of large datasets and large
m
- **[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**  
  ⬆ 78 upvotes — High throughput serving of large language models (LLMs) requires batching
sufficiently many requests at a time. However, existing systems struggle
because the key-value cache (KV cache) memory for each request is huge and
grows and shrinks dynamically. When managed inefficiently, this memory can be

- **[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**  
  ⬆ 106 upvotes — Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering ir

## HF Daily Papers (Today, by Upvotes)
- **[Sage S2.1 Flash Technical Report](https://huggingface.co/papers/2611.21072)**  
  ⬆ 92 upvotes — We introduce Sage S1.5 Flash, a 320-billion-parameter general-purpose mixture-of-experts model designed to reason over scientific evidence and act in interactive environments. Sage Sci-Perception uses dedicated encoders for molecular graphs and biological sequences and represents spectra as ordered 
- **[InclusionMed: Benchmarking AI for Inclusive Healthcare](https://huggingface.co/papers/2611.21218)**  
  ⬆ 75 upvotes — Advancing medical AI for inclusive healthcare requires evaluation across diverse healthcare roles, tasks, and care settings, but benchmark coverage remains uneven. We introduce InclusionMed, an open medical AI evaluation initiative for inclusive healthcare. The InclusionMed Atlas organizes benchmark
- **[K2-Horizon: A Frontier Fleet of Open Source Language Models](https://huggingface.co/papers/2611.21003)**  
  ⬆ 74 upvotes — We present K2-Horizon, a fleet of six fully open language models, from a 0.9B dense model to a 375B-A23B MoE, built for general-purpose reasoning and agentic work across math and science, software engineering, deep research, office automation, and beyond. The models lead or are competitive with stro
- **[AllocFlow: End-to-End Portfolio Trading Action Generation from Raw Market Data](https://huggingface.co/papers/2611.19937)**  
  ⬆ 69 upvotes — Real-world portfolio management requires converting noisy market observations into coordinated, simultaneous allocations across multiple assets under shared capital constraints. Advances in forecasting models and alpha discovery help identify opportunities. However, traditional pipelines often decou
- **[SPILLWAY: Separating Target Admission from Sanitization to Defend Tool-Using Agents against Prompt Injection](https://huggingface.co/papers/2611.07222)**  
  ⬆ 57 upvotes — Tool-using agents act on email, files, and payments, so an instruction hidden in a web page or a shared document can make an agent send data or money to an attacker. Many runtime defenses put a language model on the decision that lets an action through, so the decision depends on a model that may re
- **[SWE-CoWork: Benchmarking Coding Agents as Digital Employees in Organizations](https://huggingface.co/papers/2611.20218)**  
  ⬆ 47 upvotes — A coding agent working within a software organization must establish what to build, collaborate with colleagues, and verify what it delivers. We introduce SWE-CoWork, a benchmark comprising 101 development assignments across 101 real repositories, 11 programming languages, and 12 application domains
- **[ScaleVLA: Scaling Vision-Language-Action Models to 552 Billion Parameters](https://huggingface.co/papers/2611.21607)**  
  ⬆ 42 upvotes — Frontier Vision-Language Models (VLMs) such as GPT-6 Astra have demonstrated remarkable capabilities in robot control, suggesting that broad pretraining provides knowledge valuable for physical action. Yet most Vision-Language-Action (VLA) policies still rely on much smaller VLM backbones, leaving t
- **[PaperCritic: Training AI Reviewers to Assess the Soundness of Papers](https://huggingface.co/papers/2611.17834)**  
  ⬆ 29 upvotes — As AI conference submissions grow rapidly, AI reviewers are being considered as an alternative. However, simply imitating human reviewing is problematic because reviewing serves multiple purposes, including evaluating papers' soundness, interestingness, and clarity, the last two of which are subject
- **[VoxMel TTS Technical Report](https://huggingface.co/papers/2611.20254)**  
  ⬆ 22 upvotes — Continuous autoregressive TTS relies on an acoustic target that enables stable next-latent modeling while preserving fine-grained acoustic details. While existing approaches employ learned compressed representations (e.g., continuous VAE latents) to render prediction tractable, they rely on complex 
- **[Accelerate Bench: Evaluating Agents for Application-Level Program Optimization](https://huggingface.co/papers/2611.20882)**  
  ⬆ 17 upvotes — Application optimization requires coding agents to discover useful changes and coordinate them across a complete program while preserving the required computation. We introduce Accelerate Bench, a benchmark of 32 CPU optimization tasks adapted from scientific applications and supercomputing competit

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Know When to Zoom: How Small Is Too Small for Vision-Language Models?](https://arxiv.org/abs/2611.22709v1)**  
  Online vision-language models often miss small details in large images, because the service shrinks the image, or rejects it, before the model ever sees it. A car 20 pixels wide in an 8000 by 6000 drone photo reaches Claude about 6 pixels wide, and OpenAI's default rejects the photo outright. We mea
- **[Cross-cultural Adaptation of Recipes for Low-Resource Languages: A Benchmark and Multilingual Culinary Lexicon for Hausa, Yorùbá, and Igbo](https://arxiv.org/abs/2611.22708v1)**  
  Recent multilingual large language models (LLMs) have improved machine translation, yet culturally adaptive translation for low-resource languages (LRLs) remains underexplored. This is particularly challenging for recipes, where ingredients, cooking tools, measurements, and procedures may require ad
- **[Route Optimization under Port Congestion and Carbon Reduction: An NSGA-II Approach](https://arxiv.org/abs/2611.22705v1)**  
  Maritime shipping simultaneously faces the dual challenges of escalating port congestion and increasingly stringent decarbonization mandates. Large-scale vessel anchorage at hub ports inflates unit transport costs while generating significant additional \(CO_2\) emissions from idling auxiliary engin
- **[Social Signal Bench: Evidence-Weighted Evaluation of Co-occurring Social Signals in Video and Audio](https://arxiv.org/abs/2611.22704v1)**  
  Recognizing social signals such as interest and hesitation requires interpreting context-dependent behaviors that may co-occur in conversation. Existing affective computing benchmarks rarely evaluate such co-occurring signals, and conventional multi-label F1 overlooks semantic relationships and anno
- **[Remembered as Brief: Stored Preferences SilentlyRemove Decision-Critical Information](https://arxiv.org/abs/2611.22697v1)**  
  People increasingly learn what they need for decisions about health, money, law and safety from AI assistants, and what an assistant leaves out the user never sees. An answer with a warning removed can be true in every sentence, so fact-checks pass it, and an assistant with memory applies a preferen
- **[Making the World React Realistically: A Closed-Loop Interactive World Model for Autonomous Driving](https://arxiv.org/abs/2611.22691v1)**  
  World models (WMs) generate driving scenarios beyond recorded logs, enabling the training and evaluation of autonomous driving systems in unseen interactions. However, existing WMs struggle to ensure both behavioral realism and visual fidelity, since they overlook the relationship between vehicle in
- **[Visibility Graph Representations of Word Embeddings for Text Classification](https://arxiv.org/abs/2611.22685v1)**  
  Text classifiers depend on representations that expose the distinctions between classes in a form the learning model can use, and a restricted vocabulary changes which representation is most effective. This paper studies natural visibility graphs as an intermediate representation for news topic clas
- **[CULypso: A Clustered Federated Unlearning paradigm for Vehicular Ad-Hoc Networks](https://arxiv.org/abs/2611.22682v1)**  
  Unlearning has emerged as an essential security and privacy-preserving solution in Machine Learning, enabling networks to support their clients' rights for data erasure, as mandated by data protection regulations. Introducing such a non-trivial task to an edge, highly mobile and time-sensitive vehic
- **[FVScore: Specification-Driven Neuro-Symbolic Video Evaluation](https://arxiv.org/abs/2611.22673v1)**  
  We introduce Faithfulness Video Score (FVSCORE), a neuro-symbolic framework for specification-driven video generation evaluation. Existing evaluators rely on holistic MLLM judgments or vision-language metrics, yet aligning their scores with human judgments and tracing them to specific temporal viola
- **[Worldviews in Large Language Models](https://arxiv.org/abs/2611.22670v1)**  
  Large language models (LLMs) are often described in terms of personas and this framing has become central to alignment research. In this paper, we argue that there is a deeper level of description that lies in the agent's worldviews, i.e., its beliefs about what reality is and how it works. Treating

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Introducing GPT-6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol)**  
  Introducing GPT‑6.2 Astra and Sol, with better professional outputs, coding, computer use, and efficiency at lower cost across ChatGPT Work, Codex, and the API.
- **[Strengthening NATO and allied cyber defenses with AI](https://openai.com/index/strengthening-nato-allied-cyber-defences-ai)**  
  How OpenAI is working with NATO and allied cyber agencies to help trusted defenders find vulnerabilities, test fixes and protect essential systems.
- **[Introducing ChatGPT for Sales](https://openai.com/index/introducing-chatgpt-for-sales)**  
  Explore the new Sales plugin and 30+ new and expanded partner plugins in ChatGPT to research prospects, prepare pitches, update your CRM, and move deals forward.
- **[Astra for Law leads in legal intelligence](https://openai.com/index/astra-law-6-2)**  
  Astra for Law ranked first in a launch evaluation spanning 24 areas of law. Every ChatGPT Enterprise customer can now request access.
- **[Introducing OpenAI for Chile](https://openai.com/index/introducing-openai-for-chile)**  
  OpenAI and the Government of Chile are partnering to support responsible AI adoption, build public-sector skills and help local startups develop AI applications.

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
- **[Ian Buck Kicks Off NVIDIA’s Week at SC26 as Science Enters the Age of Agents](https://blogs.nvidia.com/blog/ian-buck-sc26/)**  
  NVIDIA’s Ian Buck kicked off the company’s week at SC26 in Chicago on Monday with new tools for AI agents, software that can plan experiments, run code and check results on researchers’ own systems. In NVIDIA’s special address, Buck announced Nemotro
- **[NVIDIA DGX Spark Developer Kit Turns a Desk Into a Supercomputing Lab](https://blogs.nvidia.com/blog/dgx-spark-hpc-developer-kit-sc26/)**  
  At SC26, an annual supercomputing conference taking place this week in Chicago, NVIDIA is introducing the DGX Spark HPC Developer Kit for researchers, academics and developers. The kit is a four-node cluster of NVIDIA DGX Spark systems, each connecte
- **[How the World’s Most Advanced AI Infrastructure Supply Chain Invents the Future](https://blogs.nvidia.com/blog/ai-infrastructure-supply-chain/)**  
  Deb Shoquist leads operations at NVIDIA, overseeing the supply chain and manufacturing behind its AI platforms. That description sums up the job, but it doesn’t begin to encompass what Shoquist has made possible over decades. Shoquist, her team and t
- **[Lambda Boosts AI Factory Resiliency and Efficiency With NVIDIA Photonics](https://blogs.nvidia.com/blog/lambda-photonics/)**  
  To train an AI model, thousands of GPUs have to work together, requiring a network that’s fast, efficient and resilient. Lambda is tackling the network piece of the puzzle with NVIDIA Photonics co-packaged optics (CPO) switches. The cloud provider is
- **[NVIDIA Expands Slurm to Bring Quantum Computing Into Supercomputing](https://blogs.nvidia.com/blog/slurm-quantum-computing-supercomputing/)**  
  Quantum processor deployments at supercomputing centers have grown nearly sevenfold over the past five years, with nearly 30 supercomputing centers around the world now in the process of deploying over 50 quantum processors.  Many of these centers us

## Lab Blog: NVIDIA Technical Blog
- **[Co-Designing Sparse Attention for Efficient Long-Context Inference](https://developer.nvidia.com/blog/co-designing-sparse-attention-for-efficient-long-context-inference/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/llm-optimize-deploy-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="llm-optimize-dep
- **[Integrating QPUs into Supercomputing Centers Using Slurm HRES Plugins](https://developer.nvidia.com/blog/integrating-qpus-into-supercomputing-centers-using-slurm-hres-plugins/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/hybrid-quantum-classical-computing-architecture-768x432.png" style="display: block; margin-bottom: 5px; clear: bo
- **[Accelerate Molecular Dynamics Simulations with Accurate, Flexible Primitives Using NVIDIA cuPotential](https://developer.nvidia.com/blog/accelerate-molecular-dynamics-simulations-with-accurate-flexible-primitives-using-nvidia-cupotential/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/healthcare-cupotential-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="healthcare-cu
- **[Post-Training NVIDIA Nemotron to Increase Accuracy in Your Scientific Domain](https://developer.nvidia.com/blog/post-training-nvidia-nemotron-to-increase-accuracy-in-your-scientific-domain/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image4-5-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image4" width="768" />Agent
- **[NVIDIA Vera Rubin NVL72 Leads Agentic Inference Performance on MLPerf Endpoints v1.0](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-leads-agentic-inference-performance-on-mlperf-endpoints-v1-0/)**  
  <img alt="Two rows of black data center racks with gold-colored server components against a black background." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/mlperf-endpoin

## GitHub Trending (AI, new repos)
- **[CrimflintVenom/rob-run-roulette-session-analytics](https://github.com/CrimflintVenom/rob-run-roulette-session-analytics)**  
  ★ 32 — A Windows desktop analytics tool for ROB RUN featuring visual screen capture, AI-assisted roulette session analysis, statistical insights and a real-time HUD interface.
- **[Igniaemage/Deadline-resp-Tracker-AI](https://github.com/Igniaemage/Deadline-resp-Tracker-AI)**  
  ★ 25 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[samhoon000/Oribi](https://github.com/samhoon000/Oribi)**  
  ★ 13 — Python library for generating AI-ready data context without sharing raw data.
- **[lucidrains/supermimic-pytorch](https://github.com/lucidrains/supermimic-pytorch)**  
  ★ 8 — Unofficial implementation of Supermimic, Scaling Humanoid Whole-Body Control with One Differentiable World Model, from Qiayuan Liao et al. of Berkeley
- **[Pro-GenAI/awesome-checklists](https://github.com/Pro-GenAI/awesome-checklists)**  
  ★ 4 — ✅ Practical, reusable checklists for planning, building, reviewing, and launching software and AI products.
- **[aayushch/codjiva](https://github.com/aayushch/codjiva)**  
  ★ 4 — Codjiva opens a folder like an IDE. But where an IDE shows you the text of a file, Codjiva shows you a blueprint of it: the machines, the pipes between them, the limits, and a short narrated film that
- **[hanspeterdietiker/open-agent-skills](https://github.com/hanspeterdietiker/open-agent-skills)**  
  ★ 4 — Discover. Share. Build.
- **[ALANDVO/axiom-station-144](https://github.com/ALANDVO/axiom-station-144)**  
  ★ 2 — Alan Vo | Work in progress: axiom-station-144
- **[sudo-nova-nsac26/sudo-nova-portfolio](https://github.com/sudo-nova-nsac26/sudo-nova-portfolio)**  
  ★ 2 — Sudo Nova’s team portfolio, built with React, showcasing our NASA Space Apps projects, open-source work, and experiments in software engineering, data, and AI.
- **[A220man/prism-forge-144](https://github.com/A220man/prism-forge-144)**  
  ★ 2 — Ryan Vo | Work in progress: prism-forge-144
