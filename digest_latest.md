# AI Research Digest — 2026-10-25

## HF Daily Papers (Trending)
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 123 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 154 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 62 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 30 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**  
  ⬆ 103 upvotes — Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system t
- **[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**  
  ⬆ 120 upvotes — Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person
- **[StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions](https://huggingface.co/papers/2610.17309)**  
  ⬆ 81 upvotes — We introduce StartLux-Decision, decision models from 0.8B to 27B parameters that combine efficient single-pass prediction with adaptive, confidence-guided reasoning. The Instant models use bidirectional attention in full-attention layers to improve decision accuracy while keeping single-pass inferen
- **[Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training](https://huggingface.co/papers/2610.05416)**  
  ⬆ 23 upvotes — Natively training joint video-audio generation models at higher resolutions empowers them to learn richer visual details and sharper motion dynamics. However, full attention incurs quadratic cost and, as resolution increases, spreads attention over increasingly redundant tokens, diluting learning si
- **[Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://huggingface.co/papers/2610.14162)**  
  ⬆ 16 upvotes — Diffusion language models (DLMs) offer parallel sampling for faster generation than autoregressive models, an increasingly important advantage as inference becomes a dominant computational workload. However, DLMs degrade quickly with fewer sampling steps, process the full sequence at every step, and
- **[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**  
  ⬆ 71 upvotes — Driven by rapid advancements of Large Language Models (LLMs), agents are
empowered to combine intrinsic knowledge with dynamic tool use, greatly
enhancing their capacity to address real-world tasks. In line with such an
evolution, AgentScope introduces major improvements in a new version (1.0),
towa

## HF Daily Papers (Today, by Upvotes)
- **[No papers indexed yet for 2026-10-25 (HF submissions can lag up to 14 days behind arXiv)]()**  
  

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://arxiv.org/abs/2610.31670v1)**  
  Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a
- **[Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning](https://arxiv.org/abs/2610.31667v1)**  
  Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes th
- **[Phase Transition from Random Features to Fully Trainable Networks](https://arxiv.org/abs/2610.31663v1)**  
  Constructing accurate and computationally tractable approximation spaces is a fundamental task in scientific computing. Partially trainable neural networks bridge fixed random features and fully adaptive representations. This paper quantifies a phase transition pattern in approximation bounds and ob
- **[Reliable AI-Assisted Decisions via Selective Auditing](https://arxiv.org/abs/2610.31662v1)**  
  We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by the same model: for ex
- **[SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing](https://arxiv.org/abs/2610.31659v1)**  
  Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then later che
- **[Cost-Aware Abstention for LLM-Based IT Ticket Classification](https://arxiv.org/abs/2610.31657v1)**  
  Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a
- **[METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning](https://arxiv.org/abs/2610.31656v1)**  
  Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from 
- **[EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence](https://arxiv.org/abs/2610.31650v1)**  
  Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an 
- **[Low-Bit N-Gram Embeddings for Language Models](https://arxiv.org/abs/2610.31646v1)**  
  Many recent open-weight language models use n-gram embedding tables to improve performance. These tables store learned representations of short token sequences, such as pairs or triples of consecutive tokens, which the model retrieves during processing. However, they can require substantial memory: 
- **[A Fix for Softmax and Cross-Entropy](https://arxiv.org/abs/2610.31642v1)**  
  Standard implementations of softmax, log-softmax, and cross-entropy have two numerical bugs. The first bug, Softmax Collapse, rounds the target logit's gradient to zero if that one logit is much larger than the others, resulting in gradients that no longer sum to zero. The second bug, Softmax Cancel

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)](https://openai.com/index/scaling-storage-one-billion-users-part-two)**  
  Learn how OpenAI scaled Habitat with reliable multi-tenancy, global caching, and Azure Cosmos DB to deliver 12× faster reads for ChatGPT.
- **[Securing our frontier model training environment](https://openai.com/index/securing-our-frontier-model-training-environment)**  
  OpenAI explains how we strengthened containment for frontier model training and evaluation, including offline environments and high-compute red-teaming.
- **[OpenAI and Poland’s NASK partner to advance AI safety and security](https://openai.com/index/openai-nask-ai-safety-security-partnership)**  
  OpenAI and Poland’s NASK are partnering on AI safety, security, and technical research to strengthen safeguards and support a more resilient digital ecosystem.
- **[Build more responsive apps with the Decisions API](https://openai.com/index/decisions-api)**  
  Fast, focused, low-cost decisions for any application.
- **[What FDE means at OpenAI](https://openai.com/index/forward-deployed-engineering-means)**  
  What forward deployed engineering means at OpenAI

## Lab Blog: DeepMind
- **[Beyond tree cover: mapping the world’s forest types](https://deepmind.google/blog/beyond-tree-cover-mapping-the-worlds-forest-types/)**  
  A global map categorizing every 10-meter patch of land on Earth into distinct forest types.
- **[Accelerating the search for antimicrobial peptides with Google Antigravity](https://deepmind.google/blog/accelerating-antimicrobial-discovery/)**  
  Accelerating the search for novel antimicrobial peptides using Google Antigravity for Science.
- **[Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)**  
  Learn how Google DeepMind and GovTech Singapore uses lightweight on-device Gemma models to intercept conversational scams in private chats with zero cloud data egress.
- **[Developing Gemini 4 Argon responsibly and safely](https://deepmind.google/blog/developing-gemini-4-argon-responsibly-and-safely/)**  
  
- **[Gemini 4 Argon for Robotics](https://deepmind.google/blog/gemini-4-argon-for-robotics/)**  
  

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

## Lab Blog: Thinking Machines Lab
- **[A Safe Path to Open Weights](https://thinkingmachines.ai/blog/a-safe-path-to-open-weights/)**  
  <blockquote class="epigraph">
<p><strong>Abstract:</strong> Safe open-weight models are public goods, as they put AI development and safety work in many hands and make training choices inspectable. Open models also carry real misuse risks, and releas
- **[The Future Worth Building Is Human](https://thinkingmachines.ai/blog/the-future-worth-building-is-human/)**  
  <p>The mission of Thinking Machines is to build AI that extends human will and judgment.</p>
<p>Artificial intelligence can do more every day, but deciding what it should do is up to us: individuals, organizations, humanity as a whole. These decision
- **[Interaction Models: A Scalable Approach to Human-AI Collaboration](https://thinkingmachines.ai/blog/interaction-models/)**  
  <p>Today, we’re announcing a research preview of interaction models: models that handle interaction natively rather than through external scaffolding. We think interactivity should scale alongside intelligence; the way we work with AI should not be t
- **[On-Policy Distillation](https://thinkingmachines.ai/blog/on-policy-distillation/)**  
  <p>LLMs are capable of expert performance in focused domains, a result of several capabilities stacked together: perception of input, knowledge retrieval, plan selection, and reliable execution. This requires a stack of training approaches, which we 
- **[LoRA Without Regret](https://thinkingmachines.ai/blog/lora/)**  
  <p>Today’s leading language models contain upwards of a trillion parameters, pretrained on tens of trillions of tokens. Base model performance keeps improving with scale, as these trillions are necessary for learning and representing all the patterns

## Lab Blog: NVIDIA Blog
- **[Kazakhstan Expands Compute for Its AI Future](https://blogs.nvidia.com/blog/kazakhstan-ai-compute-ecosystem/)**  
  Kazakhstan’s AI ecosystem is moving from infrastructure plans to deployment.  The shift is visible across the full AI stack — from infrastructure to models to applications. The announcements below — coinciding with a visit to Astana by NVIDIA founder
- **[NVIDIA Unveils Minerva to Bring End-to-End Observability for AI Factories](https://blogs.nvidia.com/blog/minerva-platform-infrastructure/)**  
  Launched today, NVIDIA Minerva is an AIOps platform built to help teams find problems earlier and keep AI factories productive. It brings together telemetry from infrastructure and AI workloads, then applies purpose-built AI models to turn that data 
- **[Cloud Deployment Incoming: ‘Call of Duty: Modern Warfare 4’ Arrives on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-call-of-duty-modern-warfare-4/)**  
  Lock in and load out this GFN Thursday. Call of Duty: Modern Warfare 4 arrives on GeForce NOW at launch, bringing a new campaign, multiplayer action and DMZ, high-stakes extraction mode to supported devices. The campaign also gets an enhanced look: G
- **[Leading European Financial Services Organizations Embrace Open Models to Build Proprietary Intelligence](https://blogs.nvidia.com/blog/european-financial-services-organizations-open-models-proprietary-intelligence/)**  
  At GTC Berlin, banks, payment companies and financial data providers are showing what production-scale intelligence looks like — built on NVIDIA accelerated computing, powered by open weight models and running on their own infrastructure. Revolut is 
- **[NVIDIA Cosmos Opens New Tools to Train, Evaluate and Deploy World Models](https://blogs.nvidia.com/blog/cosmos-open-train-evaluate-deploy-world-models/)**  
  To help developers rapidly build world models, which help physical AI systems understand and simulate the real world, NVIDIA has expanded the Cosmos platform with new training tools, simulation checkpoints and Cosmos Data Factory blueprints.  Ranking

## Lab Blog: NVIDIA Technical Blog
- **[Scaling NVIDIA TensorRT Performance Optimization Beyond a Single Build Route with the Global Performance Tuner, Part 2](https://developer.nvidia.com/blog/scaling-nvidia-tensorrt-performance-optimization-beyond-a-single-build-route-with-the-global-performance-tuner-part-2/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/desktop-computer-overlay-light-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="deskt
- **[Scaling NVIDIA TensorRT Performance Optimization Beyond a Single Build Route with the Global Performance Tuner, Part 1](https://developer.nvidia.com/blog/scaling-nvidia-tensorrt-performance-optimization-beyond-a-single-build-route-with-the-global-performance-tuner-part-1/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/desktop-computer-overlay-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="desktop-com
- **[Using AI Agents to Teach Robots Like Microduck to Walk in Simulation](https://developer.nvidia.com/blog/using-ai-agents-to-teach-robots-like-microduck-to-walk-in-simulation/)**  
  <img alt="Microduck robot in an obstacle course with labeled ramps, platforms, a rubber mat, and other objects." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/Microduck-la
- **[How to Read Data into GPU Memory in Python with NVIDIA GPUDirect Storage](https://developer.nvidia.com/blog/how-to-read-data-into-gpu-memory-in-python-with-nvidia-gpudirect-storage/)**  
  <img alt="Deocrative image." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/ai-data-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="ai-data" wi
- **[Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes](https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/workstation-3d-render-dgx-spark-key-visual-single-gtc26-4655400-768x432.png" style="display: block; margin-bottom

## GitHub Trending (AI, new repos)
- **[agentshield-dev/agentshield](https://github.com/agentshield-dev/agentshield)**  
  ★ 51 — Agentshield is open source defense for Kubernetes and AWS. It learns how your workloads really talk, flags lateral movement with evidence, and proposes fixes you approve.
- **[Cinderubasp/InterviewCopilot-rpocket-team](https://github.com/Cinderubasp/InterviewCopilot-rpocket-team)**  
  ★ 29 — EdTech application designed to bridge the gap between learning and landing your dream job
- **[Sociaro-Research/open-media-gateway](https://github.com/Sociaro-Research/open-media-gateway)**  
  ★ 21 — OMG - Open Media Gateway
- **[faraflow/faraflow](https://github.com/faraflow/faraflow)**  
  ★ 14 — Visual builder and execution engine for AI powered organizations
- **[zidniryi/cutvii](https://github.com/zidniryi/cutvii)**  
  ★ 14 — CutVii - Creative editing. Flexible workflow. On-device AI
- **[refraction-ray/free-energy-to-llms](https://github.com/refraction-ray/free-energy-to-llms)**  
  ★ 6 — Generative models from variational free energy to LLM
- **[mostwanted7/ygo-agent](https://github.com/mostwanted7/ygo-agent)**  
  ★ 4 — AI Yu-Gi-Oh! players for EDOPro: a headless duel host, pluggable model backends, live coaching and deck training.
- **[sukhee-2626/plot-docs](https://github.com/sukhee-2626/plot-docs)**  
  ★ 4 — A local-first AI office suite for Docs, Sheets, Slides, PDF, Markdown and HTML. Windows, macOS and Linux.
- **[amorey/agent-zero](https://github.com/amorey/agent-zero)**  
  ★ 4 — A starter template for AI-native coding projects
- **[ashtonckj/Purrrfessorrr-Slothhh](https://github.com/ashtonckj/Purrrfessorrr-Slothhh)**  
  ★ 3 — A playful, pixel-inspired data analysis app that makes exploring, cleaning, and visualising datasets simple, interactive, and fun! 🐈✨
