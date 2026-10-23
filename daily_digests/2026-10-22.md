# AI Research Digest — 2026-10-22

## HF Daily Papers (Trending)
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 116 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 62 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**  
  ⬆ 92 upvotes — Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system t
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 154 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**  
  ⬆ 118 upvotes — Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 29 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Next-Concept Modeling: Fast, Parallel Coarse-to-Fine Text Generation](https://huggingface.co/papers/2610.14162)**  
  ⬆ 15 upvotes — Diffusion language models (DLMs) offer parallel sampling for faster generation than autoregressive models, an increasingly important advantage as inference becomes a dominant computational workload. However, DLMs degrade quickly with fewer sampling steps, process the full sequence at every step, and
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 97 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,
- **[StartLux-Decision: AutoThink Decision Models with Reinforcement Learning for Calibrated Deliberative Decisions](https://huggingface.co/papers/2610.17309)**  
  ⬆ 25 upvotes — We introduce StartLux-Decision, decision models from 0.8B to 27B parameters that combine efficient single-pass prediction with adaptive, confidence-guided reasoning. The Instant models use bidirectional attention in full-attention layers to improve decision accuracy while keeping single-pass inferen
- **[Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://huggingface.co/papers/2610.29989)**  
  ⬆ 116 upvotes — Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher forcing, strong temporal redundancy may allow local visual continuity to serve as a shortcut for current-chunk denoising, 

## HF Daily Papers (Today, by Upvotes)
- **[StreamEval: Evaluating Interactive Streaming Video Generation Models](https://huggingface.co/papers/2610.28402)**  
  ⬆ 354 upvotes — As streaming video generation advances, enabling real-time interaction with generated video is becoming increasingly important. We introduce StreamEval, a unified benchmark for interactive streaming video generation spanning five tasks: avatar dialogue, avatar performance, world generation, instruct
- **[SpatialScout: Can VLM Agents Actively Explore and Map 3D Scenes?](https://huggingface.co/papers/2610.26659)**  
  ⬆ 129 upvotes — Spatial intelligence requires agents to actively acquire visual evidence and integrate observations into a coherent representation of the three-dimensional world. Yet spatial question answering offers limited evidence of whether models can construct accurate metric maps through autonomous exploratio
- **[DONIC: Generalist Dexterous Bimanual Tracking Control from Human Demonstrations](https://huggingface.co/papers/2610.29997)**  
  ⬆ 124 upvotes — Despite recent progress in dexterous reference tracking, existing models focus primarily on single-hand manipulation and a limited range of interactions, leaving the bimanual dexterous behaviors common in real life unaddressed. The scarcity of contact-rich bimanual manipulation data and the increase
- **[Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://huggingface.co/papers/2610.29989)**  
  ⬆ 116 upvotes — Autoregressive video diffusion models generate videos chunk by chunk, yet producing plausible continuations does not guarantee that they capture how scenes evolve. Under teacher forcing, strong temporal redundancy may allow local visual continuity to serve as a shortcut for current-chunk denoising, 
- **[Cache Engineering for Agents](https://huggingface.co/papers/2610.28577)**  
  ⬆ 113 upvotes — Large Language Model (LLM) agents can handle increasingly complex tasks, navigating long trajectories of observations and actions. As these trajectories grow, key-value (KV) cache I/O and storage become the dominant cost. Trajectories can also exceed the LLM's maximum context length, requiring contr
- **[Right Screen, Wrong Transition: World Models as Verifiers for GUI Agents](https://huggingface.co/papers/2610.11942)**  
  ⬆ 88 upvotes — A login screen that appears after a tap on Sign in is expected; the same screen after a tap on View order is an attack. For GUI agents, safety is therefore a property of the transition rather than of the screen, and a monitor that inspects only screens can be defeated by reusing a legitimate one. Ju
- **[Spectral-Spatial Interpretation](https://huggingface.co/papers/2610.21114)**  
  ⬆ 67 upvotes — Post-hoc image explanations usually show where a model looks using spatial heatmaps or indicate which channels matter using global channel scores. These separate views are limiting for multispectral data because channel relevance is often spatially localized and physically meaningful. We introduce S
- **[Agent World Model in the Wild: Computer-Use Agent Environment Synthesis](https://huggingface.co/papers/2610.26828)**  
  ⬆ 64 upvotes — Agent learning is shifting from learning from human data toward learning through interaction with the world. However, scaling such learning directly in real-world computer systems is challenging and can introduce substantial security risks. We therefore propose Agent World Model in the Wild (WildAWM
- **[PrismaCoder: Pushing the Boundaries of Open Multimodal Code Intelligence through Decomposed Rubric Synthesis](https://huggingface.co/papers/2610.20538)**  
  ⬆ 49 upvotes — Multimodal code intelligence connects the symbolic world of programs with the visual world their execution creates. Interest in this capability is burgeoning, as models are increasingly asked to produce charts, webpages, animations, and semi-structured documents. Recently, proprietary models have pu
- **[Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://huggingface.co/papers/2610.28698)**  
  ⬆ 49 upvotes — Scaling data, diversity and model capacity has improved embodied learning in physical environments, where diverse experiences remain grounded in shared physical laws. Whether these gains extend to virtual worlds with different visual styles, dynamics, controls, and objectives remains unclear. We inv

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data](https://arxiv.org/abs/2610.30132v1)**  
  Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL,
- **[Think Harder Where It Matters: Item-Level Adaptive Recursion for Sequential Recommendation](https://arxiv.org/abs/2610.30128v1)**  
  Existing sequential recommenders usually allocate a fixed computational budget to every item in a user's interaction history, regardless of the item's contribution to the final prediction. We challenge this de facto design with two diagnostic findings. (1) Non-uniform computational need: items withi
- **[PhysiCalWorld: In-Context Physics Calibration for World Models](https://arxiv.org/abs/2610.30125v1)**  
  Existing world models typically perceive a scene through current visual frame or a narrow history window. However, these observations may not reveal the physics properties that determine transition dynamics, such as an object's mass distribution, joint damping, or surface friction. Without calibrati
- **[A Quasipolynomial Algorithm for $\ell_\infty$ Contractions](https://arxiv.org/abs/2610.30122v1)**  
  We give an algorithm for computing an $\eps$-approximate fixed point of any $d$-dimensional nonexpansion with respect to the $\ell_\infty$ norm in time $\log(1/\eps)^{O(\log^2 d)}$. At its core, our method uses a boosting argument to geometrically shrink a search region. Among other consequences, ou
- **[Self-normalized Bernstein Inequalities for Regenerative Processes and Applications to Learning Without Independence](https://arxiv.org/abs/2610.30119v1)**  
  We prove a self-normalized Bernstein inequality for bounded functions of a regenerative process with independent, identically distributed marked cycles of finite mean length. The bound uses observed cycle lengths and retains explicit terms for truncation and the cycle ending after the observation ho
- **[The role of locality and weight sharing in convolutional neural networks](https://arxiv.org/abs/2610.30118v1)**  
  The success of convolutional neural networks is often attributed to locality and weight sharing. However, how these two properties separately shape learning, and how their effects depend on the spatial correlations of natural images, remain poorly understood. We address these questions in a teacher-
- **[Environment Duels: A Microcosm of LLM Co-Evolution](https://arxiv.org/abs/2610.30116v1)**  
  Through a tangle of real-world interactions, from synthetic training pipelines to data shared on the open web, frontier LLMs absorb what their predecessors and competitors create. How well does each model play its role in this ecosystem, as a creator and as a solver? We introduce Environment Duels, 
- **[The End of Consensus Research?](https://arxiv.org/abs/2610.30114v1)**  
  Consensus is a fundamental problem in distributed computing and at the core of state machine replication (SMR). Despite decades of active human research, discovering practical low-latency solutions to the problem is still open, as it requires combining protocol knowledge, correctness reasoning, impl
- **[Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research](https://arxiv.org/abs/2610.30113v1)**  
  Quantitative research is an iterative loop: a researcher proposes a market hypothesis, implements it as an executable signal, tests it on historical data, and decides what to keep. Existing benchmarks score formulas, code, or individual trading decisions, leaving open whether large language models (
- **[Minimax Optimality of the NPMLE for Gaussian Mixtures in Hellinger Distance](https://arxiv.org/abs/2610.30109v1)**  
  We analyze the problem of estimating univariate Gaussian mixture densities using the nonparametric maximum likelihood estimator (NPMLE) based on $n$ independent and identically distributed samples. We show that the unconstrained NPMLE achieves the minimax optimal rate $\log(n)/n$ in squared Hellinge

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Build more responsive apps with the Decisions API](https://openai.com/index/decisions-api)**  
  Fast, focused, low-cost decisions for any application.
- **[What FDE means at OpenAI](https://openai.com/index/forward-deployed-engineering-means)**  
  What forward deployed engineering means at OpenAI
- **[Uber brings ChatGPT Work to all employees with OpenAI](https://openai.com/index/uber-chatgpt-work-rollout)**  
  Uber is rolling out ChatGPT Work to more than 30,000 employees, helping teams research, analyze data, create presentations, and complete complex workflows.
- **[How AT&T is rethinking in-house legal work with OpenAI](https://openai.com/index/att-legal)**  
  AT&amp;T is working with OpenAI to make legal knowledge easier to access. Learn how its LegalEdge team is rethinking intake and scaling legal judgment.
- **[Broad access through consistent standards](https://openai.com/index/broad-access-through-consistent-standards)**  
  How OpenAI works with distribution partners to uphold consistent safeguards, support responsible access, and clarify expectations in our Usage Policies.

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
- **[NVIDIA Unveils Minerva to Bring End-to-End Observability for AI Factories](https://blogs.nvidia.com/blog/minerva-platform-infrastructure/)**  
  Launched today, NVIDIA Minerva is an AIOps platform built to help teams find problems earlier and keep AI factories productive. It brings together telemetry from infrastructure and AI workloads, then applies purpose-built AI models to turn that data 
- **[Cloud Deployment Incoming: ‘Call of Duty: Modern Warfare 4’ Arrives on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-call-of-duty-modern-warfare-4/)**  
  Lock in and load out this GFN Thursday. Call of Duty: Modern Warfare 4 arrives on GeForce NOW at launch, bringing a new campaign, multiplayer action and DMZ, high-stakes extraction mode to supported devices. The campaign also gets an enhanced look: G
- **[Leading European Financial Services Organizations Embrace Open Models to Build Proprietary Intelligence](https://blogs.nvidia.com/blog/european-financial-services-organizations-open-models-proprietary-intelligence/)**  
  At GTC Berlin, banks, payment companies and financial data providers are showing what production-scale intelligence looks like — built on NVIDIA accelerated computing, powered by open weight models and running on their own infrastructure. Revolut is 
- **[NVIDIA Cosmos Opens New Tools to Train, Evaluate and Deploy World Models](https://blogs.nvidia.com/blog/cosmos-open-train-evaluate-deploy-world-models/)**  
  To help developers rapidly build world models, which help physical AI systems understand and simulate the real world, NVIDIA has expanded the Cosmos platform with new training tools, simulation checkpoints and Cosmos Data Factory blueprints.  Ranking
- **[How Companies Are Using NVIDIA DSX to Break the Power Bottleneck](https://blogs.nvidia.com/blog/dsx-power/)**  
  Companies around the world are building on the NVIDIA DSX AI Factory Platform to plan, simulate and run the grid and the AI factory as one system, from the substation to the rack. Their adoption of the platform responds to an acute problem. Power is 

## Lab Blog: NVIDIA Technical Blog
- **[How to Read Data into GPU Memory in Python with NVIDIA GPUDirect Storage](https://developer.nvidia.com/blog/how-to-read-data-into-gpu-memory-in-python-with-nvidia-gpudirect-storage/)**  
  <img alt="Deocrative image." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/03/ai-data-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="ai-data" wi
- **[Running Frontier-Class AI Models Across 8 NVIDIA DGX Spark Nodes](https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/workstation-3d-render-dgx-spark-key-visual-single-gtc26-4655400-768x432.png" style="display: block; margin-bottom
- **[Design Proteins with RFD4-Proteina Using Reward-Guided Inference-Time Search](https://developer.nvidia.com/blog/design-proteins-with-rfd4-proteina-using-reward-guided-inference-time-search/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image4-2-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image4" width="768" />Prote
- **[Inside NVIDIA Sentry: Secure AI Agents at Runtime](https://developer.nvidia.com/blog/inside-nvidia-sentry-secure-ai-agents-at-runtime/)**  
  <img alt="NVIDIA BlueField chip beneath icons representing AI protection, traffic control, monitoring, data security, and a firewall." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/upload
- **[How NVIDIA OpenShell Reference Architecture Secures and Governs AI Agent Workloads at Scale](https://developer.nvidia.com/blog/how-nvidia-openshell-reference-architecture-secures-and-governs-ai-agent-workloads-at-scale/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/OpenShellKVcroppped-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="OpenShellKVcropp

## GitHub Trending (AI, new repos)
- **[Fazmin/cve-intel](https://github.com/Fazmin/cve-intel)**  
  ★ 91 — Local security intelligence for CVE triage - 38 data sources and 36 tools, risk scores and an MCP server for AI agents, all in native Rust. Private by default.
- **[agentshield-dev/agentshield](https://github.com/agentshield-dev/agentshield)**  
  ★ 27 — Agentshield is open source defense for Kubernetes and AWS. It learns how your workloads really talk, flags lateral movement with evidence, and proposes fixes you approve.
- **[dcarrero/genpic](https://github.com/dcarrero/genpic)**  
  ★ 20 — AI portrait SaaS (Laravel 11, Livewire, Filament, Stripe, fal.ai) — run in production, released as open source after closing
- **[Sociaro-Research/open-media-gateway](https://github.com/Sociaro-Research/open-media-gateway)**  
  ★ 4 — OMG - Open Media Gateway
- **[amorey/agent-zero](https://github.com/amorey/agent-zero)**  
  ★ 4 — A starter template for AI-native coding projects
- **[codebyshambhavi/pramana-dfir](https://github.com/codebyshambhavi/pramana-dfir)**  
  ★ 3 — Evidence-first AI platform for cyber investigation and digital forensics, turning digital traces into traceable, defensible findings.
- **[mostwanted7/ygo-agent](https://github.com/mostwanted7/ygo-agent)**  
  ★ 3 — AI Yu-Gi-Oh! players for EDOPro: a headless duel host, pluggable model backends, live coaching and deck training.
- **[aisecnomad/Nexus-ShadowBench](https://github.com/aisecnomad/Nexus-ShadowBench)**  
  ★ 2 — Open Benchmarks and reproducible evaluation harnesses for Shadow AI Agent Discovery & Inventory
- **[JitendraSuryavanshi/RD-AI-Dashboad](https://github.com/JitendraSuryavanshi/RD-AI-Dashboad)**  
  ★ 2 — AI-powered BMW sales intelligence dashboard that transforms natural-language questions into SQL queries, data insights, and visual charts using Gemini.
- **[taikaikaikai-pixel/post-agi-value-repricing](https://github.com/taikaikaikai-pixel/post-agi-value-repricing)**  
  ★ 2 — 从大模型估值幻觉看后 AGI 时代的价值重定价与制度锚漂移
