# AI Research Digest — 2026-10-21

## HF Daily Papers (Trending)
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 117 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 62 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**  
  ⬆ 89 upvotes — Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system t
- **[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**  
  ⬆ 118 upvotes — Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 154 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 29 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://huggingface.co/papers/2610.14162)**  
  ⬆ 12 upvotes — Diffusion language models (DLMs) offer parallel sampling for faster generation than autoregressive models, an increasingly important advantage as inference becomes a dominant computational workload. However, DLMs degrade quickly with fewer sampling steps, process the full sequence at every step, and
- **[SolarRenderer: Few-Step Generative Reference Rendering](https://huggingface.co/papers/2610.28630)**  
  ⬆ 47 upvotes — Game engines and coding agents can specify the layout, motion, and camera of a scene, yet turning such coarse structure into realistic video requires a renderer that follows the structure and completes the appearance it leaves open. Existing renderers are tied to the representation of one engine, ne
- **[StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions](https://huggingface.co/papers/2610.17309)**  
  ⬆ 24 upvotes — We introduce StartLux-Decision, decision models from 0.8B to 27B parameters that combine efficient single-pass prediction with adaptive, confidence-guided reasoning. The Instant models use bidirectional attention in full-attention layers to improve decision accuracy while keeping single-pass inferen
- **[Internal Safety Collapse in Frontier Large Language Models](https://huggingface.co/papers/2603.23509)**  
  ⬆ 31 upvotes — This work identifies a critical failure mode in frontier large language models (LLMs), which we term Internal Safety Collapse (ISC): under certain task conditions, models enter a state in which they continuously generate harmful content while executing otherwise benign tasks. We introduce TVD (Task,

## HF Daily Papers (Today, by Upvotes)
- **[Focused Omni-Modal GUI Agents](https://huggingface.co/papers/2610.26203)**  
  ⬆ 224 upvotes — Graphical User Interface (GUI) agents increasingly act over streaming omni-modal observations spanning screenshots, audio, video, interaction history, and device states. However, exposing this complete context uniformly at every step ignores that relevance is transient and sparse: the signal determi
- **[Matrix-Game 4.0: Harnessing Video Models for Real-Time Playable Game Worlds](https://huggingface.co/papers/2610.27999)**  
  ⬆ 181 upvotes — Moving from controllable videos to genuinely playable worlds requires persistent world state, executable game rules, and low-latency interaction. We outline a roadmap for the next generation of Matrix-Game that separates game execution from visual generation through an executable game harness, and i
- **[Ropedia W0: Scaling Loco-Manipulation World Models across Embodiments with Human Experience](https://huggingface.co/papers/2610.26855)**  
  ⬆ 177 upvotes — World models enable embodied agents to anticipate action consequences, yet jointly modeling locomotion and manipulation across diverse embodiments remains challenging due to heterogeneous action spaces and limited multimodal supervision. We present Ropedia W0, the first egocentric loco-manipulation 
- **[PAR: Progress-Aligned Recurrence for Length Generalization in State Tracking](https://huggingface.co/papers/2610.27628)**  
  ⬆ 147 upvotes — Looped language models can run more iterations at test time, but additional iterations need not help them solve longer problems. For sequential state tracking, final-answer supervision does not specify how far each iteration should advance, and repeated updates can change the scale of the recurrent 
- **[S-Agent 2.0: Spatial Reasoning with a General Coding Agent](https://huggingface.co/papers/2610.28354)**  
  ⬆ 92 upvotes — Spatial reasoning asks a model to work out where objects are in 3D space, how they relate to one another, and how they move. Agentic VLMs have recently brought large improvements on such tasks by letting the model actively gather evidence with 3D perception tools instead of answering in a single pas
- **[Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition](https://huggingface.co/papers/2610.28578)**  
  ⬆ 63 upvotes — In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage-A1.5 learns not only to solve individual tasks, but also to organize work and revise its approach d
- **[CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?](https://huggingface.co/papers/2610.25078)**  
  ⬆ 59 upvotes — Model--harness co-evolution has emerged as a prominent paradigm for recursive self-improving (RSI) agents, jointly evolving their execution scaffolds and intrinsic capabilities. We study the persistent yet often overlooked brain--body mismatch problem in this paradigm, where an evolving harness (bod
- **[VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse](https://huggingface.co/papers/2610.25043)**  
  ⬆ 59 upvotes — Flow-matching vision-language-action (VLA) models generate an action chunk by iteratively denoising Gaussian noise, but typically execute only a short prefix before replanning with updated observations. Under this receding-horizon paradigm, the unexecuted remainder---the action tail---is discarded, 
- **[SolarRenderer: Few-Step Generative Reference Rendering](https://huggingface.co/papers/2610.28630)**  
  ⬆ 46 upvotes — Game engines and coding agents can specify the layout, motion, and camera of a scene, yet turning such coarse structure into realistic video requires a renderer that follows the structure and completes the appearance it leaves open. Existing renderers are tied to the representation of one engine, ne
- **[Learning the 4D World through Point Trajectory Forecasting](https://huggingface.co/papers/2610.28594)**  
  ⬆ 41 upvotes — Reliable multi-view forecasting requires videos from different cameras to describe the same evolving 3D scene. To this end, we introduce Video-Point Model (VPM), a world model that conditions on multi-view video histories and a language instruction to jointly forecast future videos from arbitrary vi

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs](https://arxiv.org/abs/2610.28632v1)**  
  Video generation models can now depict remarkably realistic motion. Yet it is unclear how to use this motion beyond pixels: to animate a specific 3D asset and replay the animation in its 3D scene. For instance, a video model can show a monkey jumping over a crossbar, but it cannot return that jump a
- **[GBClaw: An agentic AI framework for atomistic grain boundary research and mechanistic discovery](https://arxiv.org/abs/2610.28629v1)**  
  Agentic artificial intelligence (AI) systems hold immense potential for automating complex workflows in materials discovery and design, but extending them to domain-intensive mechanistic investigations remains challenging. Here, we present GBClaw, an agentic AI framework for investigating the struct
- **[Learning Adaptable Dexterous Skills via Hybrid Dexterous Mimicking](https://arxiv.org/abs/2610.28628v1)**  
  Dexterous multi-finger hands hold promise to unlock diverse skills like functional grasps, in-hand reorientation, and dynamic handover that the human-designed world assumes, yet existing learning recipes force a trade-off. Goal-reaching reinforcement learning generalizes to arbitrary object poses bu
- **[UniWALM: Unified World Action Language Model for Embodied Robot Control](https://arxiv.org/abs/2610.28626v1)**  
  Motivated by the human ability to integrate experience across language, perception, and action, we introduce UniWALM, a unified world-action-language model that learns video, action, and language in a single shared representation, where each modality is both a conditioning signal and a supervision t
- **[Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets](https://arxiv.org/abs/2610.28624v1)**  
  Warehouse robot fleets continuously observe operational conditions, but preserving these observations as reusable semantic memory incurs substantial computation, communication, and storage costs. For example, explaining recurring aisle blockages can require reviewing video from multiple robots acros
- **[Planning under Noise with Neural Operators](https://arxiv.org/abs/2610.28623v1)**  
  Planning under uncertain control execution noise requires reliable feedback policies across diverse environments. We introduce Planning Under Noise (PUN), a neural operator that learns noise-aware value fields for planning in unseen geometries. Building on an established screened-Poisson formulation
- **[MindView: Benchmarking Generative Multi-View Spatial Intelligence](https://arxiv.org/abs/2610.28622v1)**  
  Spatial intelligence has recently been assessed through generative tasks such as spatially grounded image editing, yet language-guided generation of spatially consistent views from partial multi-view observations remains underexplored. We introduce MindView, a benchmark for generative multi-view spa
- **[Adaptive Multi-Token Prediction: How far should we go?](https://arxiv.org/abs/2610.28619v1)**  
  Multi-token prediction (MTP) can accelerate language-model decoding by drafting several tokens and verifying them in a single target-model pass. However, the best speculation horizon changes with context: longer drafts offer greater amortization when reliable, but can waste compute on suffixes disca
- **[Efficient Edge-aware Attention Network for Graph Generation](https://arxiv.org/abs/2610.28618v1)**  
  Graph generative models commonly use graph-specific Transformer architectures to jointly update node and edge features. However, these architectures do not directly benefit from recent hardware-aware attention implementations, limiting their scalability. The adaptation is, however, non-trivial: edge
- **[NarraSpace: Multimodal Scene-Grounded Evidence for Picture-Description Dementia Classification](https://arxiv.org/abs/2610.28616v1)**  
  Picture-description dementia classification uses a shared visual scene, but a transcript-level prediction alone does not identify the scene evidence underlying its inputs. NarraSpace links words and speech times to named picture elements and retrieves utterances for predefined scene events. Narrativ

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[How AT&T is rethinking in-house legal work with OpenAI](https://openai.com/index/att-legal)**  
  AT&amp;T is working with OpenAI to make legal knowledge easier to access. Learn how its LegalEdge team is rethinking intake and scaling legal judgment.
- **[Broad access through consistent standards](https://openai.com/index/broad-access-through-consistent-standards)**  
  How OpenAI works with distribution partners to uphold consistent safeguards, support responsible access, and clarify expectations in our Usage Policies.
- **[OpenAI models are coming to Google Cloud](https://openai.com/index/openai-models-google-cloud)**  
  OpenAI and Google Cloud are bringing frontier models and Codex workflows to Gemini’s Model Garden, available through Google Cloud Marketplace.
- **[Patch the Planet: global response coordination as agents uncover critical vulnerabilities](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities)**  
  Patch the Planet connects security researchers, maintainers, and incident responders to help address critical vulnerabilities across open source.
- **[ChatGPT Ads expands to 26 new countries as over 100,000 advertisers have used the platform](https://openai.com/index/chatgpt-ads-expands-26-new-countries)**  
  From local businesses to global brands, more advertisers can now reach people as they explore, compare and decide what to buy in ChatGPT.

## Lab Blog: DeepMind
- **[Accelerating the search for antimicrobial peptides with Google Antigravity](https://deepmind.google/blog/accelerating-antimicrobial-discovery/)**  
  Accelerating the search for novel antimicrobial peptides using Google Antigravity for Science.
- **[Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)**  
  Learn how Google DeepMind and GovTech Singapore uses lightweight on-device Gemma models to intercept conversational scams in private chats with zero cloud data egress.
- **[Developing Gemini 4 Argon responsibly and safely](https://deepmind.google/blog/developing-gemini-4-argon-responsibly-and-safely/)**  
  
- **[Gemini 4 Argon for Robotics](https://deepmind.google/blog/gemini-4-argon-for-robotics/)**  
  
- **[Gemini 4 Argon: Built to solve your hardest problems](https://deepmind.google/blog/introducing-gemini-4-argon/)**  
  

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
- **[Bringing the Spark to Europe: Local Intelligence Powers Next Wave of Agents](https://blogs.nvidia.com/blog/local-ai-gtc-rtx-dgx-spark-station-sync/)**  
  At GTC Berlin, NVIDIA is showcasing its full lineup of local AI hardware. RTX Spark, which launched last week, powers personal agents on Windows PCs; DGX Spark supports developers building and scaling applications on Linux; and DGX Station serves ent
- **[Google Cloud and NVIDIA Announce General Availability of NVIDIA Vera Rubin Infrastructure](https://blogs.nvidia.com/blog/google-cloud-vera-rubin-infrastructure/)**  
  General availability of the instances is coming next month, with planned expansion of availability to Europe — bringing an integrated platform for training, inference and large-scale reinforcement learning to cloud customers. A5X instances bring toge
- **[NVIDIA Cloud Partners Scale Across Europe — Sovereign, Open and Built for Safe AI Agents](https://blogs.nvidia.com/blog/cloud-partners-europe-sovereign-safety-open-agents/)**  
  Demand from AI-natives is pulling the European AI cloud ecosystem forward faster than ever. Developers need compute closer to their data, open models they can customize and serve at scale, and full-stack infrastructure that is secure by design.  NVID
- **[Europe’s Industrial Leaders Reinvent Engineering and Manufacturing With NVIDIA](https://blogs.nvidia.com/blog/europe-industrial-leaders-engineering-manufacturing/)**  
  To increase productivity, accelerate innovation and create new opportunities for economic growth, Europe’s industrial leaders are tapping NVIDIA CUDA-X and Omniverse libraries, as well as NVIDIA Cosmos and Nemotron open models, across the engineering
- **[NVIDIA cuDSS Now Generally Available to Accelerate Engineering and Scientific Simulations](https://blogs.nvidia.com/blog/cudss-generally-available-engineering-scientific-simulation/)**  
  NVIDIA cuDSS, launched today in general availability, is an NVIDIA CUDA-X library that shifts a critical part of engineering and scientific simulations onto GPUs.  Complex engineering feats — from advanced chips to aircraft to industrial systems —– d

## Lab Blog: NVIDIA Technical Blog
- **[Design Proteins with RFD4-Proteina Using Reward-Guided Inference-Time Search](https://developer.nvidia.com/blog/design-proteins-with-rfd4-proteina-using-reward-guided-inference-time-search/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image4-2-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image4" width="768" />Prote
- **[Inside NVIDIA Sentry: Secure AI Agents at Runtime](https://developer.nvidia.com/blog/inside-nvidia-sentry-secure-ai-agents-at-runtime/)**  
  <img alt="NVIDIA BlueField chip beneath icons representing AI protection, traffic control, monitoring, data security, and a firewall." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/upload
- **[How NVIDIA OpenShell Reference Architecture Secures and Governs AI Agent Workloads at Scale](https://developer.nvidia.com/blog/how-nvidia-openshell-reference-architecture-secures-and-governs-ai-agent-workloads-at-scale/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/OpenShellKVcroppped-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="OpenShellKVcropp
- **[Developing an AI Factory Digital Twin with an Agent-Assisted Workflow](https://developer.nvidia.com/blog/developing-an-ai-factory-digital-twin-with-an-agent-assisted-workflow/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="338" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/omniverse-overall-dsx-sim-gtc-berlin-26-5796136-600x338-r2.gif" style="display: block; margin-bottom: 5px; clear:
- **[Achieve Productive AI Capacity Faster and More Predictably with NVIDIA DSX POD](https://developer.nvidia.com/blog/achieve-productive-ai-capacity-faster-and-more-predictably-with-nvidia-dsx-pod/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/ai-infrastructure-modual-aif-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="ai-infr

## GitHub Trending (AI, new repos)
- **[Fazmin/cve-intel](https://github.com/Fazmin/cve-intel)**  
  ★ 86 — Local security intelligence for CVE triage - 38 data sources and 36 tools, risk scores and an MCP server for AI agents, all in native Rust. Private by default.
- **[dcarrero/genpic](https://github.com/dcarrero/genpic)**  
  ★ 19 — AI portrait SaaS (Laravel 11, Livewire, Filament, Stripe, fal.ai) — run in production, released as open source after closing
- **[FareedKhan-dev/dynamic-workflow-agents](https://github.com/FareedKhan-dev/dynamic-workflow-agents)**  
  ★ 5 — Claude and Qwen editions of Dynamic Workflows from Scratch
- **[Sociaro-Research/open-media-gateway](https://github.com/Sociaro-Research/open-media-gateway)**  
  ★ 4 — OMG - Open Media Gateway
- **[codebyshambhavi/pramana-dfir](https://github.com/codebyshambhavi/pramana-dfir)**  
  ★ 3 — Evidence-first AI platform for cyber investigation and digital forensics, turning digital traces into traceable, defensible findings.
- **[aisecnomad/Nexus-ShadowBench](https://github.com/aisecnomad/Nexus-ShadowBench)**  
  ★ 2 — Open Benchmarks and reproducible evaluation harnesses for Shadow AI Agent Discovery & Inventory
- **[taikaikaikai-pixel/post-agi-value-repricing](https://github.com/taikaikaikai-pixel/post-agi-value-repricing)**  
  ★ 2 — 从大模型估值幻觉看后 AGI 时代的价值重定价与制度锚漂移
- **[Mayank32935M/3d-portfolio](https://github.com/Mayank32935M/3d-portfolio)**  
  ★ 2 — 🚀 Interactive 3D portfolio of Mayank Dabas — AI & ML student & developer. Built with Next.js 16 (Turbopack), Three.js, React 19, and Tailwind CSS. Showcasing verifiable forensics frameworks, applied A
- **[kzndotsh/companion](https://github.com/kzndotsh/companion)**  
  ★ 2 — An AI companion that tries to be as human-like as we can make it, and the memory engine underneath it.
- **[Faizan-khan144/awesome-free-ai](https://github.com/Faizan-khan144/awesome-free-ai)**  
  ★ 2 — A curated list of free & open-source AI tools, models, APIs and learning resources for developers.
