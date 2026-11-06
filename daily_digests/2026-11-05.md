# AI Research Digest — 2026-11-05

## HF Daily Papers (Trending)
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 162 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 63 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 13 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 67 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**  
  ⬆ 110 upvotes — Frontier open-weight models are increasingly available, but serving them still largely assumes datacenter infrastructure. We present FreeToken, an edge-native MoE serving system that treats a personal machine not as a small GPU, but as a unified, elastic inference platform. FreeToken co-designs the 
- **[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**  
  ⬆ 183 upvotes — This report presents VibeVoice, a novel model designed to synthesize
long-form speech with multiple speakers by employing next-token diffusion,
which is a unified method for modeling continuous data by autoregressively
generating latent vectors via diffusion. To enable this, we introduce a novel
con
- **[Democratizing Robot-Use Agents: A Unified Harness with Open Models](https://huggingface.co/papers/2611.01560)**  
  ⬆ 47 upvotes — Robot-use Agents (RUAs) have shown promising zero-shot manipulation capabilities, but reliance on frontier, proprietary models limits research into further training. To democratize RUA research, we introduce uni-robot-agent, a unified harness for competitive open-weight robot use that supports furth
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 102 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,
- **[WeVisOne-VL: Unified Visual Perception from Objects to Pixels](https://huggingface.co/papers/2610.31329)**  
  ⬆ 44 upvotes — Existing vision-language models (VLMs) remain unreliable for fine-grained visual perception. In this report, we present WeVisOne-VL (WeChat Vision All-in-One), a powerful VLM that unifies object-level and pixel-level perception through structured next-token prediction. It supports multiple visual ta
- **[Differentiable Data Augmentation with Kornia](https://huggingface.co/papers/2011.09832)**  
  ⬆ 1 upvotes — In this paper we present a review of the Kornia differentiable data
augmentation (DDA) module for both for spatial (2D) and volumetric (3D)
tensors. This module leverages differentiable computer vision solutions from
Kornia, with an aim of integrating data augmentation (DA) pipelines and
strategies 

## HF Daily Papers (Today, by Upvotes)
- **[Turns Matter: Advancing Streaming Video RL via Turn-Level Credit](https://huggingface.co/papers/2611.06728)**  
  ⬆ 83 upvotes — Streaming video understanding requires models to repeatedly decide whether to respond or continue observing. Recently, Group Relative Policy Optimization (GRPO) has been applied to this setting, with existing approaches emphasizing reward design while retaining a single trajectory-level advantage ac
- **[From Pixels to Actions - Towards Native Vision-Language-Action Policies](https://huggingface.co/papers/2611.06918)**  
  ⬆ 56 upvotes — Vision-language-action models are typically built on a simple premise: perception is first compressed by visual encoders, and action reasoning begins only afterwards. Yet manipulation often hinges on precisely the visual signals most vulnerable to this abstraction, e.g., local geometry, boundaries, 
- **[FrontierPhysics: Evaluating Agents for End-to-End Physics Research](https://huggingface.co/papers/2611.06910)**  
  ⬆ 48 upvotes — AI agents are playing an increasingly important role in physics research. However, existing physics benchmarks only evaluate fixed questions, isolated sub-tasks, or paper reproduction with given solutions, and rarely check research quality alongside correctness. We introduce FrontierPhysics, an end-
- **[What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents?](https://huggingface.co/papers/2611.06483)**  
  ⬆ 35 upvotes — While multi-turn agentic reinforcement learning (RL) excels on long-horizon tasks, its performance gains remain highly sensitive to interaction constraints. Evaluating across sampling breadth K and interaction depth T via Pass@(K,T), we show that trajectory-level RL advantages depend on sufficient t
- **[Halley: A Predictive Control Plane for Optical AI Data Center Networks](https://huggingface.co/papers/2611.04408)**  
  ⬆ 34 upvotes — A frontier AI model is trained in an AI data center, on tens of thousands of accelerators joined by a dedicated network, and every training step ends with all of them exchanging data at once. Between racks, that network is optical, and each of its four layers, from lasers to switches, runs a fixed o
- **[GameVerse: A Minute-Scale Gameplay Dataset for Long-Horizon Interactive World Modeling](https://huggingface.co/papers/2610.37257)**  
  ⬆ 34 upvotes — Recent advances in interactive world models have made it possible to generate controllable, dynamic environments from action inputs. Yet current models struggle to maintain coherence beyond roughly one minute of rollout, a limitation rooted not in model capacity but in the scarcity of long-horizon t
- **[PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data](https://huggingface.co/papers/2611.05320)**  
  ⬆ 23 upvotes — Teleoperation remains the default way to collect robot demonstrations, but every episode costs robot and operator time, and every new task starts from scratch. We ask whether a coding agent can take over the teleoperator's job. In our DataFarm, the agent receives a data request and one calibration e
- **[EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](https://huggingface.co/papers/2611.06518)**  
  ⬆ 22 upvotes — Group Relative Policy Optimization (GRPO) has advanced generative model post-training in verifiable domains such as code and mathematics, but evaluating video quality, especially emotional expression, often depends on subjective aesthetics and has no uniquely correct target. Existing approaches typi
- **[StreamDuo: A Live Commentator and a Research Agent for Unseen Games](https://huggingface.co/papers/2611.01120)**  
  ⬆ 20 upvotes — Streaming video LLMs can now commentate live gameplay, but they are trained and tested on the same games. We study cross-game streaming commentary, in which a model trained on one game commentates games it has never seen, and find that current commentators transfer their timing but not their knowled
- **[On the Generalization Limitation of On-Policy Distillation for Post-RL Consolidation](https://huggingface.co/papers/2611.05609)**  
  ⬆ 16 upvotes — Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) to consolidate capabilities from multiple teachers. Although prior work reports near-perfect in-distribution (IND) distillation performance, we find that this can mask incomplete capability consolidation beyond the supe

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Automatic keyphrase extraction and annotation: modern theoretical approaches and practical solutions for text and speech](https://arxiv.org/abs/2611.08006v1)**  
  The exponential growth of textual and audiovisual information has made the task of automatic keyphrase extraction (KE) increasingly significant. This article provides a comprehensive analysis of contemporary theoretical approaches and practical solutions for KE across both text and speech modalities
- **[Towards Multiscale Molecular Representation Learning through Geometry-Based Fragmentation for Polymer Property Prediction](https://arxiv.org/abs/2611.07998v1)**  
  It is well established that molecular substructures can contribute unequally to chemical and physical properties, with specific motifs or side chains often playing dominant roles. Fragment-based representations have therefore emerged as an effective strategy for incorporating chemically meaningful i
- **[Compression Through a Context Lens: Evaluating Adaptation, Quantization, and Distillation in Arabic Legal LLMs](https://arxiv.org/abs/2611.07988v1)**  
  Model compression can facilitate the deployment of large language models in resource-constrained legal settings, but its effects on domain-specific performance may depend on the evaluation protocol. We investigate this issue using ArabLegalEval, a Saudi Arabic legal benchmark, under both with-contex
- **[Technohybridism: Recursive Semantic Normalization in AI-Mediated Societies](https://arxiv.org/abs/2611.07984v1)**  
  Language-generating AI systems are no longer only objects of linguistic interaction: their outputs increasingly re-enter the communicative and institutional practices from which their training material was drawn. Drawing on social theory, social epistemology, and the philosophy of language, this art
- **[How Far Can Lightweight LLMs Go in Intent-to-SLO Translation?](https://arxiv.org/abs/2611.07982v1)**  
  Intent-based networking (IBN) promises QoS provisioning in which the network derives the configuration from operator-stated goals. Its first step, translating a natural-language intent into enforceable service-level objectives (SLOs) grounded in a live snapshot of the network state, increasingly rel
- **[QRAE: Query-Relevant Attention Entropy for Context Compression in DeepSearch Agents](https://arxiv.org/abs/2611.07976v1)**  
  DeepSearch LLM agents repeatedly search and carry retrieved sources into subsequent reasoning steps. This expanding context increases token consumption and latency, although many results do not contribute to later reasoning. We propose Query-Relevant Attention Entropy (QRAE), an online context compr
- **[Tight Asymptotic Bounds on the Maximum Number of Linear Regions of Piecewise-Linear Kolmogorov--Arnold networks](https://arxiv.org/abs/2611.07973v1)**  
  Schoots et al.~\citep{schoots2025relating} (AISTATS 2025) established a generally loose upper bound on the number of linear regions of continuous piecewise-linear (CPWL) Kolmogorov--Arnold networks (KANs), without providing a lower bound. We consider a $T$-layer network with width vector $\mathbf n=
- **[TCSExam: Evaluating Frontier LLMs on the Full Range of TCS Research](https://arxiv.org/abs/2611.07962v1)**  
  Can large language models (LLMs) advance theoretical computer science and resolve its long-standing open conjectures? To study progress toward this goal, we introduce TCSExam, a unified framework and benchmark covering the full range of TCS research. It evaluates theorem proving, solver engineering,
- **[CoRD: Coupled Rollouts Fill the Blind Spot of On-Policy Distillation](https://arxiv.org/abs/2611.07959v1)**  
  On-policy distillation trains a student on its own rollouts, so states the teacher would reach but the student does not are seldom supervised. We introduce CoRD (coupled-rollout distillation), which keeps the on-policy loss and moves only the distribution of training states toward the teacher, drawi
- **[A Behavioural Framework for Predicting and Understanding Loss of Control in Frontier Artificial Intelligence Systems](https://arxiv.org/abs/2611.07953v1)**  
  Frontier artificial intelligence (AI) systems are increasingly operating over longer horizons with diminishing human oversight, raising the risk of loss of control: systems acting beyond effective human control with potentially irreversible consequences. Because such failures may become observable o

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Australian universities are creating AI-native graduates](https://openai.com/index/australian-universities-ai-native-graduates)**  
  Australian universities are expanding access to ChatGPT and bringing AI into teaching and learning to prepare students for an AI-enabled workforce.
- **[Cult.fit builds operational muscle with Codex](https://openai.com/index/cultfit-builds-with-codex)**  
  Cult.fit is using Codex to help teams across functions build tools, move faster, and change how work gets done.
- **[GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents](https://openai.com/index/introducing-gpt-6-cyber)**  
  Introducing GPT‑6 Cyber, OpenAI’s cybersecurity model for finding exploitable vulnerabilities and developing fixes, trained to stay within authorized scope.
- **[Merge builds product and business tools with OpenAI technology](https://openai.com/index/merge-builds-with-openai)**  
  Merge uses GPT-6 Astra, ChatGPT, and Codex to review product code and support marketing. Its teams also use AI to plan executive dinners and prepare sales updates.
- **[Setting a new standard for responsible AI infrastructure](https://openai.com/index/setting-new-standard-responsible-ai-infrastructure)**  
  OpenAI introduces its National Community Compact and Compute Campus Policy Blueprint to protect local resources, create jobs, and guide responsible AI infrastructure development.

## Lab Blog: DeepMind
- **[Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips](https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/)**  
  
- **[Agentic cheminformatics with Google Antigravity](https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/)**  
  Learn how Google Antigravity and our Cheminformatics Skills accelerate drug discovery workflows, search compounds, and propose novel rigidified macrocycles.
- **[Speeding up planning decisions with AI](https://deepmind.google/blog/speeding-up-planning-decisions-with-ai/)**  
  Google DeepMind and UK government work together to reduce planning assessment times
- **[Gemini 4 Carbon: Our next frontier model](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)**  
  
- **[Genie 4: A new generation of world simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)**  
  Genie 4: our new world model unlocking unprecedented realism in real-time simulation.

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
  <blockquote class="epigraph"><p><strong>Abstract:</strong> Safe open-weight models are public goods, as they put AI development and safety work in many hands and make training choices inspectable. Open models also carry real misuse risks, and release
- **[The Future Worth Building Is Human](https://thinkingmachines.ai/blog/the-future-worth-building-is-human/)**  
  <p id="introduction">The mission of Thinking Machines is to build AI that extends human will and judgment.</p>
<p>Artificial intelligence can do more every day, but deciding what it should do is up to us: individuals, organizations, humanity as a who
- **[Interaction Models: A Scalable Approach to Human-AI Collaboration](https://thinkingmachines.ai/blog/interaction-models/)**  
  <p id="introduction">Today, we’re announcing a research preview of interaction models: models that handle interaction natively rather than through external scaffolding. We think interactivity should scale alongside intelligence; the way we work with 
- **[On-Policy Distillation](https://thinkingmachines.ai/blog/on-policy-distillation/)**  
  <p id="introduction">LLMs are capable of expert performance in focused domains, a result of several capabilities stacked together: perception of input, knowledge retrieval, plan selection, and reliable execution. This requires a stack of training app
- **[LoRA Without Regret](https://thinkingmachines.ai/blog/lora/)**  
  <p id="introduction">Today’s leading language models contain upwards of a trillion parameters, pretrained on tens of trillions of tokens. Base model performance keeps improving with scale, as these trillions are necessary for learning and representin

## Lab Blog: NVIDIA Blog
- **[Vera Delivers the Best of Both Worlds: Highest Throughput and Fastest Agents](https://blogs.nvidia.com/blog/vera-cpu-highest-throughput-fastest-agents/)**  
  AI agents do more than generate answers. They search for information, query databases, write and test code and take action.  Each of those steps relies on a CPU, with agents moving between GPU reasoning and CPU execution throughout a task.  As busine
- **[Into the Omniverse: How Developers Turn Ideas Into Simulations With Frontier AI Agents](https://blogs.nvidia.com/blog/developers-simulation-frontier-ai-agents/)**  
  Turning a simulation idea into a working application means assembling assets, connecting physics and rendering, and checking that the scene behaves as intended. Developers are combining frontier AI models with NVIDIA Omniverse libraries to help carry
- **[The Wizard of Open Weights: Chris Alexiuk Makes AI Easy With Open Models](https://blogs.nvidia.com/blog/nvidia-life-chris-alexiuk/)**  
  Chris Alexiuk has a simple rule about open source AI: If you believe in it, be loud about it. “We should be shouting about this technology from the rooftops,” said Alexiuk, a Toronto-based senior product research engineer in deep learning at NVIDIA w
- **[More Performance From Every Byte: How Full-Stack Codesign Solves AI’s Memory Challenge](https://blogs.nvidia.com/blog/memory-full-stack-codesign/)**  
  Larger models, longer contexts and agentic applications are increasing GPU memory pressure while supply tightens and prices rise — a trend expected to continue through the near term. NVIDIA works closely with memory partners to rapidly adopt the late
- **[‘Hogwarts Legacy’ Gets a Magical NVIDIA DLSS 5 Upgrade on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-hogwarts-legacy-dlss-5/)**  
  Hogwarts Legacy receives an NVIDIA DLSS 5 upgrade with 3D-Guided Neural Rendering today, bringing lifelike lighting and materials to the wizarding world on GeForce NOW. Blizzard Entertainment’s World of Warcraft: Forever also opens a new chapter in A

## Lab Blog: NVIDIA Technical Blog
- **[Configure, Certify, and Operate Kubernetes GPU Clusters with NVIDIA DSX OS](https://developer.nvidia.com/blog/configure-certify-and-operate-kubernetes-gpu-clusters-with-nvidia-dsx-os/)**  
  <img alt="Glowing green modular cube with gauge, clock, and gear icons on a black background." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/dsx-os-cluster-readiness-featu
- **[Five Ways NVIDIA Co-Design Maximizes the Value of Every Byte in the AI Factory](https://developer.nvidia.com/blog/five-ways-nvidia-co-design-maximizes-the-value-of-every-byte-in-the-ai-factory/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image5-1-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image5" width="768" />In an
- **[How NVIDIA Uses AI Agents to Streamline AI Factory Operations](https://developer.nvidia.com/blog/how-nvidia-uses-ai-agents-to-streamline-ai-factory-operations/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image2-3-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="image2" width="768" />As GP
- **[NVIDIA CUDA 13.5 Brings NVIDIA Vera Rubin GA Support](https://developer.nvidia.com/blog/nvidia-cuda-13-5-brings-nvidia-vera-rubin-ga-support/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image1-16-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image1" width="768" />As a
- **[How NVIDIA Factory Operations Blueprint Coordinates AI Agents to Investigate Production Issues](https://developer.nvidia.com/blog/how-nvidia-factory-operations-blueprint-coordinates-ai-agents-to-investigate-production-issues/)**  
  <img alt="Factory Manager Agent illustration surrounded by a humanoid robot, a circuit board, an electronics production line, and automated material handling equipment." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer

## GitHub Trending (AI, new repos)
- **[vixhal-baraiya/qwenFS](https://github.com/vixhal-baraiya/qwenFS)**  
  ★ 91 — Qwen3.5-2B with a filesystem compiled and inserted directly into its weights.
- **[Jumbomuffin777/Frontier-UI](https://github.com/Jumbomuffin777/Frontier-UI)**  
  ★ 63 — ChatGPT-style generative UI for Open WebUI: photo galleries, live maps with real routes, multi-day trips, budgets, calculators, live weather & stocks, link previews, and one-click Word/Excel/PowerPoin
- **[AstralBeneathSilver/Deadline-resp-Tracker-AI](https://github.com/AstralBeneathSilver/Deadline-resp-Tracker-AI)**  
  ★ 40 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[DjibrilM/MagicVoiceAI](https://github.com/DjibrilM/MagicVoiceAI)**  
  ★ 11 —  An offline desktop Text-to-Speech (TTS) studio built with Electron and the Qvac sdk 
- **[DeepakSingh98/qwenlab](https://github.com/DeepakSingh98/qwenlab)**  
  ★ 9 — Six small transformers compiled into Qwen3.5-9B, trained in its own forward passes. Qwen runs the experiments.
- **[abchughtai786/automated-job-posting-pipeline](https://github.com/abchughtai786/automated-job-posting-pipeline)**  
  ★ 3 — Node.js pipeline that collects, screens with AI, de-duplicates and publishes job listings demo with sample data
- **[bogdancstrike/image-organizer](https://github.com/bogdancstrike/image-organizer)**  
  ★ 3 — Turn a messy photo folder into beautifully organized albums. Locally, in seconds, with an undo button.  Sort by what's in the photos, cull a shoot like a pro (blurry · eyes closed · best of burst), an
- **[KCFindstr/RSI-Bench](https://github.com/KCFindstr/RSI-Bench)**  
  ★ 3 — Frontier Foundation Model Benchmark
- **[olidesarrollador-png/Quack-Efficient](https://github.com/olidesarrollador-png/Quack-Efficient)**  
  ★ 2 — Aplicación local para Ollama: lista modelos instalados, chatea y ajusta contexto. El ahorro de RAM depende del modelo y equipo.
- **[big-data-team/ai-course](https://github.com/big-data-team/ai-course)**  
  ★ 2 — AI Agents Engineer Specialization / Practical AI Course
