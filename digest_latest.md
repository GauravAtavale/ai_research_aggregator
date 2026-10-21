# AI Research Digest — 2026-10-20

## HF Daily Papers (Trending)
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 115 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 62 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**  
  ⬆ 74 upvotes — Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system t
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 29 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 153 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Has GPT-6-Astra Achieved Embodied Intelligence?](https://huggingface.co/papers/2610.22471)**  
  ⬆ 421 upvotes — GPT-6-Astra demonstrates a level of competence in robotic manipulation and navigation that challenges the conventional paradigm of building specialized models for individual tasks and embodiments. In this report, we ask not only how capable GPT-6-Astra is, but what its capabilities imply for the fie
- **[Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://huggingface.co/papers/2610.14162)**  
  ⬆ 8 upvotes — Diffusion language models (DLMs) offer parallel sampling for faster generation than autoregressive models, an increasingly important advantage as inference becomes a dominant computational workload. However, DLMs degrade quickly with fewer sampling steps, process the full sequence at every step, and
- **[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**  
  ⬆ 117 upvotes — Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person
- **[Internal Safety Collapse in Frontier Large Language Models](https://huggingface.co/papers/2603.23509)**  
  ⬆ 31 upvotes — This work identifies a critical failure mode in frontier large language models (LLMs), which we term Internal Safety Collapse (ISC): under certain task conditions, models enter a state in which they continuously generate harmful content while executing otherwise benign tasks. We introduce TVD (Task,
- **[MemT-1.0: Towards Memory-Native Evolution](https://huggingface.co/papers/2610.26825)**  
  ⬆ 146 upvotes — Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of model computation. Buil

## HF Daily Papers (Today, by Upvotes)
- **[Scaling Parameter-Efficient Fine-Tuning for Brain Encoding](https://huggingface.co/papers/2610.26802)**  
  ⬆ 234 upvotes — Brain encoding models aim to predict neural responses to stimuli. The most widely used approach fits readouts from frozen pretrained backbones. Using neural data to train large models from scratch or fully fine-tune them after task-pretraining has proven difficult because neural data is costly and l
- **[OR-License: Evaluating LLM Agents as Real-World Operations Research Practitioners](https://huggingface.co/papers/2610.24087)**  
  ⬆ 176 upvotes — Can large language model (LLM) agents deliver expert-level operations research (OR) solutions directly from original client materials, without prior expert reformulation? Existing OR benchmarks typically begin with self-contained descriptions or predefined optimization tasks, underrepresenting the t
- **[EgoXperience: Learning World-Grounded Egocentric Representations from Human Experience](https://huggingface.co/papers/2610.26625)**  
  ⬆ 122 upvotes — Reconstructing human activity from egocentric video requires more than recovering individual 3D components: the observer's motion, surrounding geometry, and hand-object interactions must fit together in a consistent world. Achieving this coherence requires both joint reconstruction and aligned super
- **[MemT-1.0: Towards Memory-Native Evolution](https://huggingface.co/papers/2610.26825)**  
  ⬆ 109 upvotes — Memory-native evolution requires making memory an intrinsic capability of foundation models, enabling them to continuously accumulate and utilize information. To this end, we introduce MemT-1.0, a new architecture of memory foundation models that internalize memory as part of model computation. Buil
- **[Holi-World: Building Holistic World Intelligence from Human-Ego Experience](https://huggingface.co/papers/2610.26549)**  
  ⬆ 109 upvotes — Human egocentric experience offers a rich foundation for learning how the world is organized and how it changes through interaction. Realizing this potential at scale requires turning growing volumes of recordings into learning resources that connect scene structure, object semantics, and interactio
- **[Learning from Fleet Experience: A Collective Learning Paradigm for Robots](https://huggingface.co/papers/2610.25736)**  
  ⬆ 107 upvotes — Experience generated during deployment offers an opportunity for robots to improve policy reliability through learning from their own executions. However, learning through human corrections requires teleoperators to monitor execution and intervene when policies fail, a demand that is difficult to me
- **[OpenVLHarness: Real World Visual Agentic Tool-Use with Multimodal Memory](https://huggingface.co/papers/2610.26860)**  
  ⬆ 97 upvotes — Multimodal large language models (MLLMs) have made rapid progress on visual reasoning, yet many tasks require evidence that is difficult to obtain through internal reasoning alone: our controlled study on 22 benchmarks shows that simply increasing the inference budget of the base model yields only m
- **[ScaleNav: Scalable Internet Video Pretraining for Language-Conditioned Local Navigation](https://huggingface.co/papers/2610.25690)**  
  ⬆ 84 upvotes — We study language-conditioned local navigation, where a robot must navigate to a text-specified target visible in its initial observation and stop at the described location. End-to-end navigation policies require diverse training data to generalize across scenes, yet real-robot data is costly to col
- **[SpecMRL: Redesign Matryoshka Representation Learning within Parametric Spectrum](https://huggingface.co/papers/2610.26824)**  
  ⬆ 80 upvotes — Matryoshka Representation Learning (MRL) is designed to support flexible representation sizes by jointly optimizing nested prefixes. While effective, this design lacks an explicit constraint to ensure that the leading portion provides a suitable compact encoding. To address this, we propose SpecMRL,
- **[Self-Evolving Coding Agents via Harness-Policy Optimization](https://huggingface.co/papers/2610.22791)**  
  ⬆ 41 upvotes — Large language model (LLM) agents have shown promising potential in coding tasks, and their performance is jointly determined by the policy model and the harness that mediates their interaction with the environment. Indeed, harness and policy are mutually reinforcing and evolving only one component 

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Near-Duplicate Image Selection Transfers Preferences in Vision-Language Models](https://arxiv.org/abs/2610.27943v1)**  
  Subliminal learning is the phenomenon in which a model transmits its preferences to another model through data that do not explicitly express them. As models increasingly curate training data for other models, we ask whether this transfer can arise from choosing among near-duplicate images while kee
- **[APRIL: Ambiguity-Aware Expert Routing for Respiratory Sound Domain-Incremental Learning](https://arxiv.org/abs/2610.27942v1)**  
  Automated respiratory sound classification enables continuous, non-invasive respiratory assessment, yet long-term deployment remains challenging due to domain shifts from evolving recording devices and acquisition periods. When privacy and governance regulations prohibit replaying historical data, s
- **[HypTI: Hyperbolic Geometry-Aware Multimodal Feature Fusion Framework for Dementia Detection Based on Tabular-Image Data](https://arxiv.org/abs/2610.27941v1)**  
  AI-assisted dementia detection usually requires multimodal fusion of diverse data, such as clinical tabular assessments and neuroimaging data. However, most existing approaches perform feature fusion in Euclidean space. This overlooks the geometric structure of representation, including hierarchical
- **[From DQI to C-DQI: Automatic Codebook Generation and Evaluation for Measuring Computational Discourse Quality Index](https://arxiv.org/abs/2610.27937v1)**  
  Effective democratic deliberation is vital for civic engagement and the health of legislative institutions. However, assessing parliamentary discourse quality is traditionally done using expert-scored, theory-based codebooks (CBs), which are rigid, labor-intensive, and prone to biases. While Large L
- **[From Comparison to Selection: Enhancing Cross-Scale Generalization of Pointer Networks Trained with Reinforcement Learning for Capacitated Drone Delivery Routing](https://arxiv.org/abs/2610.27936v1)**  
  Unmanned aerial vehicles (UAVs) enable fast, flexible last-mile and emergency delivery, but their routing remains challenging as the number of clients varies. Classical approaches based on mixed-integer programming and heuristics can scale poorly or require problem-specific design, motivating learni
- **[Why Do LLMs Accept Generics? Explaining Acceptability using Psycholinguistic and Model-Derived Factors](https://arxiv.org/abs/2610.27928v1)**  
  Psycholinguistic studies explore why humans accept some generic statements but reject others by showing that these judgments depend on more than how common a property is. People consider several other factors such as how well it sets the kind apart from others or whether it is characteristic of the 
- **[Quantum-JEPA: Quantum Born Priors for Latent-Action JEPA World Models](https://arxiv.org/abs/2610.27921v1)**  
  A single observation can admit several plausible futures, making uncertainty an essential part of world modelling. However, quantum generative models remain underexplored for this task. We introduce Quantum-JEPA, a latent-action JEPA framework that learns distributions of future representations usin
- **[ACE-Compression: An Ability-Centric Evaluation of Compressed Large Language Models](https://arxiv.org/abs/2610.27913v1)**  
  Model compression makes large language models deployable, but today's evaluation tells an incomplete story. Standard practice measures retained task performance and stops there. This misses a critical fact: compression perturbs the distributed knowledge embedded across billions of weights, and task 
- **[MMEnterprise-Bench: Evaluating Enterprise Agents over Evolving Multimodal Records](https://arxiv.org/abs/2610.27911v1)**  
  Enterprise agents answer questions over workplace records that evolve through team collaboration. As information is shared, corrected, and revised across documents, chats, and figures, multiple versions of the same information accumulate in the workspace. Reliable question answering therefore requir
- **[Polarity Blindness in LLM Safety: A Systematic Study of Negation, Antonym Substitution, and Adversarial Framing](https://arxiv.org/abs/2610.27908v1)**  
  Negation remains a persistent challenge for language models across NLP tasks and modalities. We show that this weakness can undermine LLM safety guardrails through a structural vulnerability we term polarity blindness: the failure to recognize harmful intent after polarity-altering linguistic transf

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Franchisee reconciles cash in 94% less time with ChatGPT Work](https://openai.com/index/ted-taylor-restaurant)**  
  An independent Schlotzsky’s and Cinnabon franchisee cut menu repricing time by 95% and built a workflow that could free up $100K in cash flow.
- **[Terminal X matches senior investor judgment 88.6% with GPT-6.1](https://openai.com/index/terminal-x)**  
  Terminal X’s Eval Agent grades outputs against a 54-criterion rubric, catching 25% more deviances from a fund’s mandate with GPT-6.1 Sol.
- **[OpenAI acquires Orchestra Bio](https://openai.com/index/openai-to-acquire-orchestra-bio)**  
  OpenAI is acquiring Orchestra Bio to bring AI-powered operations to life sciences R&amp;D, helping biopharma teams accelerate drug development and advance new treatments.
- **[Advancing coding in low‑resource programming languages](https://openai.com/index/low-resource-programming-languages)**  
  Learn how OpenAI is improving ChatGPT across low-resource programming languages, with new evaluations for software engineering, SQLite, and COBOL migration.
- **[How Itaú is building generative AI for its entire customer base](https://openai.com/index/itau-generative-ai)**  
  With ia.i, a conversational interface, and the IARA governance platform, Itaú is applying its AI First strategy to customers and employees — in one of Brazil’s most regulated sectors.

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
- **[Spain-Based Startups Advance Regional Innovation With Barcelona Supercomputing Center](https://blogs.nvidia.com/blog/spain-startups-barcelona-supercomputing-center/)**  
  The Barcelona Supercomputing Center (BSC)’s AI Factory Accelerator Programme, now in full operation following a pilot initiative, gives startups access to sovereign compute, technical support and training to support innovation across industries.  Man
- **[Germany Wants to Lead the World in Industrial AI: How NVIDIA Will Help](https://blogs.nvidia.com/blog/germany-wants-to-lead-the-world-in-industrial-ai-how-nvidia-will-help/)**  
  In the cavernous hall of Kraftwerk, a former power station in Berlin, German Chancellor Friedrich Merz and NVIDIA founder and CEO Jensen Huang sat down to discuss Germany’s AI roadmap, and in particular, the industrial applications of AI. Huang opene
- **[NVIDIA Advances Agentic Security for Media, From European Public Service Broadcasting to Global Content Production](https://blogs.nvidia.com/blog/media-agentic-security-european-public-service-broadcasting-global-content-production/)**  
  At a creative industry event that took place today in Berlin — hosted in collaboration with Adobe, Bertelsmann, NVIDIA and UFA — the latest advancements in intelligent media were on display. Key to the news: the European Broadcasting Union (EBU) is c
- **[RTX Spark Ignites Global Celebration as New Windows PCs Arrive](https://blogs.nvidia.com/blog/local-ai-rtx-spark-windows-laptops-celebration/)**  
  NVIDIA RTX Spark laptops are now available, bringing NVIDIA Blackwell RTX graphics, up to 128GB of unified memory and the full NVIDIA AI platform to slim, premium Windows PCs.  Starting at $2,399, laptops from ASUS, Dell, HP, Lenovo, Microsoft and MS
- **[Be There for the Beginning: Celebrate the Launch of NVIDIA RTX Spark](https://blogs.nvidia.com/blog/local-ai-rtx-spark-launch-event-invite/)**  
  A new beginning for Windows PCs starts tomorrow with the launch of NVIDIA RTX Spark — one PC built for creators, gamers and AI agents. All are invited to celebrate with NVIDIA and partners at launch events around the world. Share Your Spark Every PC 

## Lab Blog: NVIDIA Technical Blog
- **[Accelerating Mamba-2 with High-Performance Forward Pass Kernels in NVIDIA CUDA Tile](https://developer.nvidia.com/blog/accelerating-mamba-2-with-high-performance-forward-pass-kernels-in-nvidia-cuda-tile/)**  
  <img alt="Decorative math image." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2025/11/Solving-Math-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="S
- **[Code, Test, and Deploy on One Machine with NVIDIA RTX Spark](https://developer.nvidia.com/blog/code-test-and-deploy-on-one-machine-with-nvidia-rtx-spark/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image2-7-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image2" width="768" />AI ag
- **[NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)**  
  <img alt="Illustration of a central AI model connecting code, charts, credit memo data extraction, and video analysis." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/Nemot
- **[Scale Agentic Coding Workflows with Meta’s Muse Spark Open on NVIDIA GB300 NVL72](https://developer.nvidia.com/blog/scale-agentic-coding-workflows-with-metas-muse-spark-open-on-nvidia-gb300-nvl72/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/open-model-unbox-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="open-model-unbox" w
- **[Optimizing Agent Reliability and Tool Calling Efficiency for Chip Design Using NVIDIA NeMo Gym](https://developer.nvidia.com/blog/optimizing-agent-reliability-and-tool-calling-efficiency-for-chip-design-using-nvidia-nemo-gym/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/agentic-workflow-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="agentic-workflow" w

## GitHub Trending (AI, new repos)
- **[Fazmin/cve-intel](https://github.com/Fazmin/cve-intel)**  
  ★ 82 — Local security intelligence for CVE triage - 38 data sources and 36 tools, risk scores and an MCP server for AI agents, all in native Rust. Private by default.
- **[dcarrero/genpic](https://github.com/dcarrero/genpic)**  
  ★ 16 — AI portrait SaaS (Laravel 11, Livewire, Filament, Stripe, fal.ai) — run in production, released as open source after closing
- **[codebyshambhavi/pramana-dfir](https://github.com/codebyshambhavi/pramana-dfir)**  
  ★ 3 — Evidence-first AI platform for cyber investigation and digital forensics, turning digital traces into traceable, defensible findings.
- **[Sociaro-Research/open-media-gateway](https://github.com/Sociaro-Research/open-media-gateway)**  
  ★ 3 — OMG - Open Media Gateway
- **[FareedKhan-dev/dynamic-workflow-agents](https://github.com/FareedKhan-dev/dynamic-workflow-agents)**  
  ★ 3 — Claude and Qwen editions of Dynamic Workflows from Scratch
- **[Vrajm12/astraforge](https://github.com/Vrajm12/astraforge)**  
  ★ 3 — Open-source, model-agnostic AI skill toolkit for structured reasoning, reliable coding, research, and verified execution.
- **[taikaikaikai-pixel/post-agi-value-repricing](https://github.com/taikaikaikai-pixel/post-agi-value-repricing)**  
  ★ 2 — 从大模型估值幻觉看后 AGI 时代的价值重定价与制度锚漂移
- **[kzndotsh/companion](https://github.com/kzndotsh/companion)**  
  ★ 2 — An AI companion that tries to be as human-like as we can make it, and the memory engine underneath it.
- **[Faizan-khan144/awesome-free-ai](https://github.com/Faizan-khan144/awesome-free-ai)**  
  ★ 2 — A curated list of free & open-source AI tools, models, APIs and learning resources for developers.
- **[lord-kirby-kirk69/Athena](https://github.com/lord-kirby-kirk69/Athena)**  
  ★ 2 — A lightweight desktop AI assistant built with Tauri, React, and Rust, designed to support multiple AI models through a simple, customizable interface.
