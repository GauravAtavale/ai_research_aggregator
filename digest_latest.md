# AI Research Digest — 2026-11-21

## HF Daily Papers (Trending)
- **[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**  
  ⬆ 11 upvotes — Synthesizing unstructured research materials into manuscripts is an essential yet under-explored challenge in AI-driven scientific discovery. Existing autonomous writers are rigidly coupled to specific experimental pipelines, and produce superficial literature reviews. We introduce PaperOrchestra, a
- **[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://huggingface.co/papers/2611.26603)**  
  ⬆ 31 upvotes — We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-fra
- **[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**  
  ⬆ 147 upvotes — We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D gr
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 21 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**  
  ⬆ 18 upvotes — π^4 is a unified foundation model for 4D scene perception. From diverse, uncalibrated RGB observations in the wild---a single image, an unordered collection, or a video sequence---it recovers dense geometry, camera poses, and metric scale, together with 2D/3D point tracks and moving-object masks for
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 169 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 37 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 70 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**  
  ⬆ 22 upvotes — The advent of 1-bit large language models (LLMs), led by BitNet b1.58, has
spurred interest in ternary LLMs. Despite this, research and practical
applications focusing on efficient edge inference for ternary LLMs remain
scarce. To bridge this gap, we introduce Bitnet.cpp, an inference system
optimiz
- **[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**  
  ⬆ 78 upvotes — High throughput serving of large language models (LLMs) requires batching
sufficiently many requests at a time. However, existing systems struggle
because the key-value cache (KV cache) memory for each request is huge and
grows and shrinks dynamically. When managed inefficiently, this memory can be


## HF Daily Papers (Today, by Upvotes)
- **[No papers indexed yet for 2026-11-21 (HF submissions can lag up to 14 days behind arXiv)]()**  
  

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[RL Post-Training in Diffusion Transformers Is Activation Steering](https://arxiv.org/abs/2611.26627v1)**  
  Reinforcement learning (RL) post-training substantially improves the visual quality, text rendering, and compositional accuracy of diffusion transformers. Because capabilities such as rendering requested text or composing multiple objects are inherently prompt-dependent, a natural hypothesis is that
- **[PlayCraft: Designing Engaging Games from Agent Play Experience](https://arxiv.org/abs/2611.26624v1)**  
  Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its
- **[TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming](https://arxiv.org/abs/2611.26619v1)**  
  Hybrid architectures have become mainstream among open-weight language models. Their global-attention and bounded-state layers maintain heterogeneous caches whose demands vary with context length and concurrency. We present TideCache, a serving system on CPU--GPU superchips with three components for
- **[One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning](https://arxiv.org/abs/2611.26617v1)**  
  Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for
- **[AgentRoboCritic: Understanding the Capability of Frontier Agents on Direct Robot Control](https://arxiv.org/abs/2611.26613v1)**  
  Frontier multimodal language agents such as GPT-6 Astra have demonstrated strong capabilities in controlling robots directly via low-level numerical actions without high-level primitives. However, existing benchmarks report only episode-level success rates, which show neither how these agents succee
- **[Bio-PM-Guided Synthetic IMU Generation](https://arxiv.org/abs/2611.26607v1)**  
  Collecting and labeling inertial measurement unit (IMU) data for human activity recognition (HAR) is expensive, and models trained on one group of subjects often fail to generalize to unseen individuals. Even with balanced data, classifiers struggle to distinguish dynamically similar activity classe
- **[Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth](https://arxiv.org/abs/2611.26603v1)**  
  We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-fra
- **[SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research](https://arxiv.org/abs/2611.26601v1)**  
  LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are scattered across papers, vendor reports an
- **[Active Feature Acquisition by Distilling an Oracle Teacher](https://arxiv.org/abs/2611.26598v1)**  
  Acquiring every feature of an instance is often costly: a measurement can carry a monetary price, a time delay, or a privacy cost. Active Feature Acquisition (AFA) addresses this by learning a policy that decides, per instance, which features to acquire under a budget. Existing AFA methods train thi
- **[PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation](https://arxiv.org/abs/2611.26596v1)**  
  Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within a monolithic model. We propose Physically Grounded Execution (

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Combatting adversarial distillation](https://openai.com/index/combatting-adversarial-distillation)**  
  OpenAI’s layered approach to adversarial distillation combines model training, safeguards, detection, and enforcement to protect against capability extraction.
- **[Hebbia sees improvements in financial research with GPT-6 Astra](https://openai.com/business/customer-stories/hebbia)**  
  Hebbia tested GPT-6 Astra for financial research. Its prerelease evaluations found gains in source coverage, citation relevance, and presentation quality.
- **[Can AI help scientists identify promising drug candidates?](https://openai.com/index/introducing-medchembench)**  
  MedChemBench evaluates how well AI models interpret molecular structures, reason from experimental evidence, and select compounds in early drug discovery.
- **[How OpenAI’s Performance Factory keeps ChatGPT fast](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)**  
  Learn how OpenAI built the Performance Factory, a system of Codex-powered workflows that finds and fixes performance issues to help keep ChatGPT fast.
- **[Explore the Codex Security Plugin](https://openai.com/business/learn/codex-security-plugin-demo)**  
  Watch a demo of the Codex Security Plugin and see the workflow in action, from getting started to reviewing the results shown in the recording.

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
- **[NVIDIA and Microsoft Expand Accelerated Computing From Azure to Windows PCs](https://blogs.nvidia.com/blog/microsoft-ignite-accelerated-computing-azure-windows-pcs/)**  
  NVIDIA and Microsoft are extending their full-stack collaboration to help organizations build, customize and deploy intelligent applications — from next-generation infrastructure on Azure to industrial systems and Windows PCs. At Microsoft Ignite, th
- **[Into the Omniverse: How Developers Turn Ideas Into Simulations With Frontier AI Agents](https://blogs.nvidia.com/blog/developers-simulation-frontier-ai-agents/)**  
  Turning a simulation idea into a working application means assembling assets, connecting physics and rendering, and checking that the scene behaves as intended. Developers are combining frontier AI models with NVIDIA Omniverse libraries to help carry
- **[Season’s Streamings and Savings: Black Friday Deals Come to GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-black-friday-2026/)**  
  GeForce NOW is kicking off Black Friday with more reasons to make time for gaming. Six-month memberships are back for a limited time. Save 30% on the first six-month term of a Performance or Ultimate membership. Big gaming plans, smaller price tag.  
- **[NVIDIA RTX Spark Compact Desktops Out Now](https://blogs.nvidia.com/blog/rtx-spark-desktop-local-ai-available-now/)**  
  New NVIDIA RTX Spark compact desktops from ASUS, Dell and MSI are available today, bringing local AI agents, image and video generation, and model fine-tuning to a dedicated Windows PC. With up to 128GB of unified memory and NVIDIA’s AI software stac
- **[Ian Buck Kicks Off NVIDIA’s Week at SC26 as Science Enters the Age of Agents](https://blogs.nvidia.com/blog/ian-buck-sc26/)**  
  NVIDIA’s Ian Buck kicked off the company’s week at SC26 in Chicago on Monday with new tools for AI agents, software that can plan experiments, run code and check results on researchers’ own systems. In NVIDIA’s special address, Buck announced Nemotro

## Lab Blog: NVIDIA Technical Blog
- **[Reducing Rollout Bottlenecks in Reinforcement Learning with NVIDIA Dynamo](https://developer.nvidia.com/blog/reducing-rollout-bottlenecks-in-reinforcement-learning-with-nvidia-dynamo/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image3-17-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image3" width="768" />Rein
- **[Enabling Real-Time AI for Scientific Instruments with GPU-Native Data Acquisition](https://developer.nvidia.com/blog/enabling-real-time-ai-for-scientific-instruments-with-gpu-native-data-acquisition/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/electron-energy-loss-spectroscopy-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="el
- **[Build Tool-Calling Parsers in Rust with AI Agents](https://developer.nvidia.com/blog/build-tool-calling-parsers-in-rust-with-ai-agents/)**  
  <img alt="A developer, code blocks, a checklist, and a rising bar chart connect to a central network diagram." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/agentic-ai-rl-
- **[Build Training-Ready Physical AI Datasets with Two Prompts in NVIDIA Cosmos](https://developer.nvidia.com/blog/build-training-ready-physical-ai-datasets-with-two-prompts-in-nvidia-cosmos/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="338" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/cosmos-gif.gif" style="display: block; margin-bottom: 5px; clear: both;" title="cosmos-gif" width="600" />World m
- **[Tackling GPU Bottlenecks in Plane-Wave DFT with K-Point Batching and Mixed Precision](https://developer.nvidia.com/blog/tackling-gpu-bottlenecks-in-plane-wave-dft-with-k-point-batching-and-mixed-precision/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image4-10-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image4" width="768" />Trai

## GitHub Trending (AI, new repos)
- **[Morriswawan05/elevenlabs-pro-win](https://github.com/Morriswawan05/elevenlabs-pro-win)**  
  ★ 79 — ElevenLabs - AI voice synthesis platform for text-to-speech generation, voice cloning and multilingual dubbing on Windows 10/11
- **[Cloudcode04/runway-ml-pro-win](https://github.com/Cloudcode04/runway-ml-pro-win)**  
  ★ 72 — Runway - AI video generation platform for text-to-video synthesis, image animation and motion brush editing on Windows 10/11
- **[Juanlabs1989/descript-pro-win](https://github.com/Juanlabs1989/descript-pro-win)**  
  ★ 71 — Descript - AI-powered video and podcast editor for text-based editing, transcription and screen recording on Windows 10/11
- **[debugdigital677/descript-pro-win](https://github.com/debugdigital677/descript-pro-win)**  
  ★ 71 — Descript - AI-powered video and podcast editor for text-based editing, transcription and screen recording on Windows 10/11
- **[GuzmanJacqueline93/copy-ai-pro-win](https://github.com/GuzmanJacqueline93/copy-ai-pro-win)**  
  ★ 69 — Copy Ai Pro - AI copywriting assistant for content generation, tone rewriting and SEO text optimization on Windows 10/11
- **[JieFedorov81/runway-ml-pro-win](https://github.com/JieFedorov81/runway-ml-pro-win)**  
  ★ 68 — Runway - AI video generation platform for text-to-video synthesis, image animation and motion brush editing on Windows 10/11
- **[isanders5152/descript-pro-win](https://github.com/isanders5152/descript-pro-win)**  
  ★ 58 — Descript - AI-powered video and podcast editor for text-based editing, transcription and screen recording on Windows 10/11
- **[suryacode04/jasper-ai-win](https://github.com/suryacode04/jasper-ai-win)**  
  ★ 51 — Jasper AI - AI content generation platform for marketing copy creation, brand voice customization and long-form article drafting on Windows 10/11
- **[lucidrains/supermimic-pytorch](https://github.com/lucidrains/supermimic-pytorch)**  
  ★ 15 — Unofficial implementation of Supermimic, Scaling Humanoid Whole-Body Control with One Differentiable World Model, from Qiayuan Liao et al. of Berkeley
- **[cookllm/AI-PhD-Internships-2027](https://github.com/cookllm/AI-PhD-Internships-2027)**  
  ★ 4 — AI and ML research internships that require or prefer a PhD, for Summer 2027 and off-cycle terms. Updated daily from company career pages, with direct apply links.
