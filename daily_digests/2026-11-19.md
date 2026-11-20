# AI Research Digest — 2026-11-19

## HF Daily Papers (Trending)
- **[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**  
  ⬆ 10 upvotes — Synthesizing unstructured research materials into manuscripts is an essential yet under-explored challenge in AI-driven scientific discovery. Existing autonomous writers are rigidly coupled to specific experimental pipelines, and produce superficial literature reviews. We introduce PaperOrchestra, a
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 21 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[π^4: A Foundation Model for 4D Scene Geometry and Motion](https://huggingface.co/papers/2611.23144)**  
  ⬆ 17 upvotes — π^4 is a unified foundation model for 4D scene perception. From diverse, uncalibrated RGB observations in the wild---a single image, an unordered collection, or a video sequence---it recovers dense geometry, camera poses, and metric scale, together with 2D/3D point tracks and moving-object masks for
- **[Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent](https://huggingface.co/papers/2611.18397)**  
  ⬆ 138 upvotes — We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D gr
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 36 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**  
  ⬆ 20 upvotes — The advent of 1-bit large language models (LLMs), led by BitNet b1.58, has
spurred interest in ternary LLMs. Despite this, research and practical
applications focusing on efficient edge inference for ternary LLMs remain
scarce. To bridge this gap, we introduce Bitnet.cpp, an inference system
optimiz
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 169 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 70 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**  
  ⬆ 78 upvotes — High throughput serving of large language models (LLMs) requires batching
sufficiently many requests at a time. However, existing systems struggle
because the key-value cache (KV cache) memory for each request is huge and
grows and shrinks dynamically. When managed inefficiently, this memory can be

- **[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**  
  ⬆ 87 upvotes — Software is one of the most powerful tools that we humans have at our
disposal; it allows a skilled programmer to interact with the world in complex
and profound ways. At the same time, thanks to improvements in large language
models (LLMs), there has also been a rapid development in AI agents that


## HF Daily Papers (Today, by Upvotes)
- **[Jeveration: System One Models Now Generate](https://huggingface.co/papers/2611.24738)**  
  ⬆ 120 upvotes — System One models such as Jev return decisions through fast, parallel prediction. In this paper, we introduce Jeveration, showing that the same decision paradigm can also generate high-quality images in a single forward pass. Jeveration builds on a frozen vision-language model, repurposing its visua
- **[The Resolution Hypothesis: Agent Evolution's Key Is Identifying Improvements](https://huggingface.co/papers/2611.23068)**  
  ⬆ 35 upvotes — Agent evolution follows a simple loop: a proposer writes candidate artifacts (prompts, skills, memories) and selection accepts those that score higher. This loop has shown promise, yet practitioners face a puzzle: methods trade wins across papers, and evolution often fails to bootstrap on certain ta
- **[ALIVE: Making Streaming Video Models Interactive](https://huggingface.co/papers/2611.21366)**  
  ⬆ 35 upvotes — Streaming video LLMs can continuously observe the world, yet often handle user requests in isolation. We introduce ALIVE, an interactive streaming video model supporting proactive monitoring, streaming task coordination, and feedback-seeking interaction. We construct ALIVE-SFT-288K and ALIVE-RL-3K f
- **[PROLA: Principal-Orthogonal Low-rank Adaptation for Predictive Spatiotemporal Weather Downscaling](https://huggingface.co/papers/2611.11318)**  
  ⬆ 27 upvotes — High-resolution weather prediction is important for resolving local atmospheric patterns missed by coarse global forecasts. Large pretrained weather backbones have improved global forecasting, but adapting them to produce future high-resolution fields from recent coarse states remains challenging an
- **[Game2Player: Scaling Gameplay Experience for Visual Agents through Environment-Player Co-Development](https://huggingface.co/papers/2611.24154)**  
  ⬆ 25 upvotes — Games are a rich testbed for visual agents, demanding perception, long-horizon planning, and precise control. However, collecting human gameplay is costly, and learning from gameplay videos requires inferring missing actions. Existing datasets also cover a limited range of games, often without expli
- **[CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning](https://huggingface.co/papers/2611.24654)**  
  ⬆ 22 upvotes — A central challenge in adapting large language models (LLMs) is capability preservation: an adaptation can achieve its target while degrading general capabilities. We introduce CurvDelta, a scalable framework that incorporates the preservation constraint into the parameterization of the model update
- **[HINT-WAM: Hindsight-Informed Training for World Action Models](https://huggingface.co/papers/2611.24789)**  
  ⬆ 22 upvotes — World action models (WAMs) have shown promising generalization and data efficiency in robot manipulation by coupling action generation with predictions of future visual dynamics. Translating these capabilities into reliable task execution, however, remains a challenge for existing post-training meth
- **[LightTAR: Light and Fast Target-Aware Representations for Multimodal Tabular Learning](https://huggingface.co/papers/2611.17600)**  
  ⬆ 20 upvotes — Multimodal tabular learning involves classification and regression on tables combining structured numerical and categorical features with unstructured text and images. These unstructured fields are commonly represented by pretrained encoder embeddings reduced with principal component analysis (PCA).
- **[WorldRuler: Interactive World Modeling under Configurable Rules](https://huggingface.co/papers/2611.24869)**  
  ⬆ 18 upvotes — Rules govern how player actions change interactive worlds. Different rules create distinct gameplay experiences within similar scenes and action spaces. For customizable gameplay, generative world models must follow user-defined rules beyond real-world behaviors. However, realizing user-defined rule
- **[Code World Model 2.0: Towards Infinite Controllable Video Generation](https://huggingface.co/papers/2611.22925)**  
  ⬆ 17 upvotes — Visual proxies decouple explicit world-state simulation from photorealistic video synthesis, offering a controllable interface for both offline clip creation and real-time interactive streaming. Yet a practical renderer must address two challenges. Upstream proxies vary from coarse layouts to fine a

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[When Do Rankings Beat Signs? Gradient Direction Recovery under Even Nuisance](https://arxiv.org/abs/2611.26055v1)**  
  Can ranking a batch of antipodal query pairs recover a gradient direction with fewer evaluations than using within-pair signs alone? We study fixed-center recovery in $d$ dimensions for a linear signal plus an unknown differentiable even nuisance, counting function evaluations and feedback rounds se
- **[Reference-Free Humanoid Skateboarding via Termination-Shaped Reinforcement Learning](https://arxiv.org/abs/2611.26054v1)**  
  Humanoid locomotion research has advanced rapidly on walking and running, but \emph {object-mediated} locomotion, in which a robot must coordinate its body with a passive external object, remains difficult. One challenging task is skateboarding, which requires simultaneous interaction with the groun
- **[Studying AI Act Mentions: A first look at the impact of the European Union's AI regulation on Hugging Face](https://arxiv.org/abs/2611.26050v1)**  
  The European Union's Artificial Intelligence Act (AI Act) entered into force in August 2024, and its obligations apply in stages. Obligations for providers of general-purpose AI models have applied since August 2025, and transparency rules since August 2026. These obligations affect developers who s
- **[Fixing the Twin, Not the Detector: Sim-to-Real Roadside LiDAR Detection from Digital-Twin Data](https://arxiv.org/abs/2611.26035v1)**  
  Roadside LiDAR detectors are expensive to train on real labels, and digital twins promise to replace these labels, but a detector trained on a twin meets a different sensor, different objects and different annotation conventions on the real site. We describe the pipeline that placed first in the LUM
- **[SEOYUN: Refusal-Inducing Exam Documents for AI-Glasses Pipelines](https://arxiv.org/abs/2611.26033v1)**  
  Camera-equipped glasses can convert an examination page into a query to a vision-language model (VLM). Device detection addresses possession; a complementary question is whether an examination document can reduce the usefulness of an unauthorized capture. We present SEOYUN, an application-specific f
- **[The Delayed Societal Cost of Unfairness](https://arxiv.org/abs/2611.26030v1)**  
  Fair machine learning typically evaluates the societal costs of a decision policy -- the loss incurred by the decision-maker (DM) and the unfair distribution of costs among demographic groups of decision-subjects (DS) -- on static data, where reducing one often comes at the expense of the other. Yet
- **[Serialization Tax in Shared-Latent Exchangeable Decisions](https://arxiv.org/abs/2611.26029v1)**  
  Accurate item probabilities can produce inaccurate group-level decisions. A system may score each item separately, yet act on whether enough hidden items succeed: show a slate, defer a panel decision, or inspect a batch. When items share an uncertain latent state, independent marginalization preserv
- **[ForeSeek: Foresight-Driven Reasoning for Long-Form Video Understanding](https://arxiv.org/abs/2611.26024v1)**  
  Long-form video understanding, as a fundamental yet crucial vision task, is being revolutionized by multimodal large language model (MLLM)-based video agents. However, the retrieval-driven nature inherent to these agents creates a significant bottleneck, forcing them to reactively fetch clips based 
- **[FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models](https://arxiv.org/abs/2611.26020v1)**  
  Hybrid language models combine self-attention with recurrent layers whose in-place state updates restrict prefix reuse to exact saved positions. Saving states on a coarse grid wastes reusable prefixes, whereas existing fine-grained exact caches must cut the prefill forward pass at each mid-prompt ch
- **[Does the Workspace Do the Work? A Causal Protocol for Verifying Global-Workspace Computation in a Language Model](https://arxiv.org/abs/2611.26018v1)**  
  Global Workspace Theory (GWT), a leading theory of consciousness, holds that information becomes conscious when it is broadcast to specialized processes that use it. Building a workspace into a network does not reveal what the trained network computes with it: a module that reports an answer may hav

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[How OpenAI’s Performance Factory keeps ChatGPT fast](https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)**  
  Learn how OpenAI built the Performance Factory, a system of Codex-powered workflows that finds and fixes performance issues to help keep ChatGPT fast.
- **[Deploying Daybreak Red](https://openai.com/business/learn/deploying-daybreak-red)**  
  Explore a reference architecture for supervised security investigations with Daybreak Red, including safety controls, setup, and monitoring.
- **[See PR scans in action](https://openai.com/business/learn/pr-scans-demo)**  
  Watch a walkthrough of PR scans and see how the presenter reviews scan results in a pull request workflow.
- **[Explore the Codex Security Plugin](https://openai.com/business/learn/codex-security-plugin-demo)**  
  Watch a demo of the Codex Security Plugin and see the workflow in action, from getting started to reviewing the results shown in the recording.
- **[Get started with Daybreak Blue](https://openai.com/business/learn/daybreak-blue-onboarding-demo)**  
  Watch a walkthrough of onboarding to Daybreak Blue, with a closer look at the setup experience and how to get started.

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
- **[Igniaemage/Deadline-resp-Tracker-AI](https://github.com/Igniaemage/Deadline-resp-Tracker-AI)**  
  ★ 25 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[lucidrains/supermimic-pytorch](https://github.com/lucidrains/supermimic-pytorch)**  
  ★ 14 — Unofficial implementation of Supermimic, Scaling Humanoid Whole-Body Control with One Differentiable World Model, from Qiayuan Liao et al. of Berkeley
- **[aayushch/codjiva](https://github.com/aayushch/codjiva)**  
  ★ 4 — Codjiva opens a folder like an IDE. But where an IDE shows you the text of a file, Codjiva shows you a blueprint of it: the machines, the pipes between them, the limits, and a short narrated film that
- **[cookllm/AI-PhD-Internships-2027](https://github.com/cookllm/AI-PhD-Internships-2027)**  
  ★ 3 — AI and ML research internships that require or prefer a PhD, for Summer 2027 and off-cycle terms. Updated daily from company career pages, with direct apply links.
- **[sudo-nova-nsac26/sudo-nova-portfolio](https://github.com/sudo-nova-nsac26/sudo-nova-portfolio)**  
  ★ 2 — Sudo Nova’s team portfolio, built with React, showcasing our NASA Space Apps projects, open-source work, and experiments in software engineering, data, and AI.
- **[A220man/vector-lens-144](https://github.com/A220man/vector-lens-144)**  
  ★ 2 — Ryan Vo | Work in progress: vector-lens-144
- **[ALANDVO/lumen-lab-147](https://github.com/ALANDVO/lumen-lab-147)**  
  ★ 2 — Alan Vo | Work in progress: lumen-lab-147
- **[ALANDVO/nexus-studio-145](https://github.com/ALANDVO/nexus-studio-145)**  
  ★ 2 — Alan Vo | Work in progress: nexus-studio-145
- **[ALANDVO/orbit-pilot-145](https://github.com/ALANDVO/orbit-pilot-145)**  
  ★ 2 — Alan Vo | Work in progress: orbit-pilot-145
- **[ALANDVO/orbit-foundry-146](https://github.com/ALANDVO/orbit-foundry-146)**  
  ★ 2 — Alan Vo | Work in progress: orbit-foundry-146
