# AI Research Digest — 2026-10-15

## HF Daily Papers (Trending)
- **[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**  
  ⬆ 26 upvotes — The landscape of software development has witnessed a paradigm shift with the
advent of AI-powered assistants, exemplified by GitHub Copilot. However,
existing solutions are not leveraging all the potential capabilities available
in an IDE such as building, testing, executing code, git operations, e
- **[Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation](https://huggingface.co/papers/2610.20571)**  
  ⬆ 323 upvotes — Long-form agentic video generation must turn a screenplay into shots that remain spatially and temporally consistent across nonconsecutive requests. Passing prompts or recent frames between shots does not provide a shared spatial frame for revisiting a scene or a time-indexed record for replaying an
- **[RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://huggingface.co/papers/2610.13912)**  
  ⬆ 46 upvotes — Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predict
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 27 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 152 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Player-1: Learning to Play from Synthetic Experience](https://huggingface.co/papers/2610.20584)**  
  ⬆ 269 upvotes — Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent lea
- **[Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes](https://huggingface.co/papers/2610.18356)**  
  ⬆ 116 upvotes — City-scale 3D grounding is commonly formulated as candidate ranking, which requires precomputed instance proposals and becomes inefficient in large outdoor scenes. We propose Urbex, an agentic vision-language framework that instead casts grounding as active spatial search. Urbex represents a city-sc
- **[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**  
  ⬆ 115 upvotes — Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person
- **[YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality](https://huggingface.co/papers/2609.33757)**  
  ⬆ 237 upvotes — Symbolic models make melody, harmony, rhythm, and form explicit but typically stop before a finished recording; audio models produce complete songs while leaving composition implicit. We introduce YuE2, which unifies symbolic and audio music generation at frontier quality through symbolic planning. 
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 93 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,

## HF Daily Papers (Today, by Upvotes)
- **[Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation](https://huggingface.co/papers/2610.20571)**  
  ⬆ 323 upvotes — Long-form agentic video generation must turn a screenplay into shots that remain spatially and temporally consistent across nonconsecutive requests. Passing prompts or recent frames between shots does not provide a shared spatial frame for revisiting a scene or a time-indexed record for replaying an
- **[Player-1: Learning to Play from Synthetic Experience](https://huggingface.co/papers/2610.20584)**  
  ⬆ 269 upvotes — Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent lea
- **[Beyond Domain-Routed Supervision: Cross-Teacher Guarding for Multi-Teacher On-Policy Distillation](https://huggingface.co/papers/2610.13521)**  
  ⬆ 233 upvotes — Multi-teacher on-policy distillation (MOPD) extends on-policy distillation (OPD) by routing domain-specific data to specialized teachers, integrating their capabilities through dense token-level supervision on student-generated trajectories. However, domain routing only distinguishes the supervision
- **[Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents](https://huggingface.co/papers/2610.20344)**  
  ⬆ 93 upvotes — Agents driven by large language models are increasingly deployed on long-horizon tasks, where they use tools and modify real workspaces. How well they perform depends as much on the harness around the model as on the model itself. Existing benchmarks measure downstream task success under a fixed har
- **[More Methods, Better Agents? A Reality Check on Self-Distillation in Agentic Reinforcement Learning](https://huggingface.co/papers/2610.19789)**  
  ⬆ 72 upvotes — Self-distillation in agentic reinforcement learning has produced a growing number of methods. However, existing evaluations often reuse published baseline scores under differing experimental conditions, provide few direct comparisons among contemporaneous methods, and give limited attention to train
- **[Recovering Reliable Supervision via Critique-Guided On-Policy Distillation](https://huggingface.co/papers/2610.20572)**  
  ⬆ 70 upvotes — On-policy distillation (OPD) trains a student model on its own rollouts with token-level supervision from a teacher, assuming that the teacher can reach a correct answer from any prefix the student writes. We call this property the recoverability of the teacher and show it fails on incorrect rollout
- **[LatentLoop: Scaling Looped MoE Models with Asymmetric Compute Allocation](https://huggingface.co/papers/2610.19975)**  
  ⬆ 64 upvotes — Looped Mixture-of-Experts (MoE) models combine parameter reuse with sparse computation to improve performance under matched budgets. Prior work demonstrates that different loop visits can play different roles even when they share parameters. To probe the contributions of different loop visits, we le
- **[Cortex: Consolidating Context into Parametric Memory](https://huggingface.co/papers/2610.20399)**  
  ⬆ 63 upvotes — Context can improve large language model performance, but these gains may be lost after context removal. Inspired by biological systems consolidation, we formulate Memory Consolidation (MC) as internalizing these gains while preserving non-target capabilities, connecting context-specified editing, s
- **[ActionOPD: Distilling Decisions, Not Tokens](https://huggingface.co/papers/2610.19820)**  
  ⬆ 53 upvotes — Distilling capable language-model agents into smaller models requires aligning the student's behavior with the teacher's. This raises a fundamental question: at which states and at what granularity should this alignment be performed? Offline imitation provides dense but token-specific supervision an
- **[Seeing, Maintaining, and Learning: The Evolution of Multimodal Agent Memory](https://huggingface.co/papers/2610.19366)**  
  ⬆ 45 upvotes — Multimodal models and agents have emerged to enable AI systems to learn from and interact with the real world more like humans by integrating information across multiple modalities. However, enabling multimodal agents to continually acquire useful information from complex, heterogeneous multimodal d

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Modeling and Understanding Neural Weights of Humanoid Policies with Diffusion](https://arxiv.org/abs/2610.20606v1)**  
  Recent advances in robot learning have driven rapid progress in humanoid control, enabling increasingly agile behaviors in the real world. However, humanoid control networks are typically obtained through conventional training procedures, while comparatively little attention has been given to direct
- **[Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance](https://arxiv.org/abs/2610.20607v1)**  
  Mobile Manipulation (MoMa) is a cornerstone of autonomous robotic systems, yet real-world fine-tuning remains a formidable challenge because of high-dimensional action spaces and intricate coupling between heterogeneous modules. In this paper, we propose HiRe-MoMa (Hierarchical Residual Mobile Manip
- **[Co-Evolving Acting and Forecasting for Language Agents](https://arxiv.org/abs/2610.20597v1)**  
  Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision through value targets tha
- **[Your Transformer Is Secretly Elastic](https://arxiv.org/abs/2610.20588v1)**  
  Scaling up transformers has produced models with broad capabilities, deployed across heterogeneous hardware and fluctuating workloads. Yet, model families offer only a few fixed sizes (e.g., S, B, L), forcing users to commit to a model based on hardware and latency constraints. This rigidity is ofte
- **[Price of Anarchy of First-Price Auctions in Agentic Markets](https://arxiv.org/abs/2610.20587v1)**  
  An agentic market is a decentralized serving-time market where AI agents bid to claim each user prompt. An agent's bid is based on its expected value for the prompt, which is the expectation of the reward for its response minus its inference costs. First-price auctions (FPAs), in which the highest b
- **[Continuum Attention](https://arxiv.org/abs/2610.20586v1)**  
  We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve. Each query induces an exponential relevance density along the curve. Integrating the density and interpolated 
- **[Learnable Hodge-Laplacian Driven Mixture of Experts for Steady-PDE Surrogates on Coarse Unstructured Meshes](https://arxiv.org/abs/2610.20585v1)**  
  Current approaches for steady partial differential equations surrogate models on unstructured meshes apply a single mixing mechanism to the whole solution. This paper proposes an architecture that partitions the solution among vanilla transformer experts, each focused on a different spectral scale. 
- **[Player-1: Learning to Play from Synthetic Experience](https://arxiv.org/abs/2610.20584v1)**  
  Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent lea
- **[Latent Compaction with Test-Time Training](https://arxiv.org/abs/2610.20582v1)**  
  Long contexts enlarge key--value (KV) caches, increasing memory use and attention costs during generation. Compressing these caches must preserve information for unseen questions. We introduce **Latent Compaction**, which learns a compact document-specific cache through test-time training. We initia
- **[One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness](https://arxiv.org/abs/2610.20576v1)**  
  Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave the underlying task unchanged yet make the agent worse at it. Scoring each sample independently mean

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Bringing GPT-Rosalind to academic research labs](https://openai.com/index/introducing-the-rosalind-academic-plan)**  
  Introducing the Rosalind Academic Plan, offering eligible academic labs sponsored access to GPT-Rosalind and tools to advance life sciences research.
- **[Teaching students to think and learn through questions](https://openai.com/index/teaching-students-to-think-and-learn-through-questions)**  
  Celebrate Teachers’ Day with AI for Educators in Brazilian Portuguese and see how Study Mode can help teachers support active, step-by-step learning.
- **[Sullivan & Cromwell brings legal expertise into agreement review](https://openai.com/index/sullivan-cromwell)**  
  In collaboration with OpenAI, Sullivan & Cromwell developed Agreement Analyzer, an AI tool for identifying issues in a draft agreement.
- **[Amp puts AI agents to work beyond code with OpenAI models](https://openai.com/index/amp-beyond-coding)**  
  See how Amp pushes the frontier of what agents can do with GPT-6 Astra, Ultrafast, GPT-Live-1, and Sign in with ChatGPT.
- **[SentinelOne cuts malware analysis from weeks to hours](https://openai.com/index/sentinelone)**  
  With OpenAI Daybreak, SentinelOne cuts weeks of malware analysis to hours, creating capacity to investigate more threats.

## Lab Blog: DeepMind
- **[Accelerating the search for antimicrobial peptides with Google Antigravity](https://deepmind.google/blog/accelerating-antimicrobial-discovery/)**  
  Accelerating the search for novel antimicrobial peptides using Google Antigravity for Science.
- **[Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)**  
  Learn how Google DeepMind and GovTech Singapore uses lightweight on-device Gemma models to intercept conversational scams in private chats with zero cloud data egress.
- **[Developing Gemini 4 Argon responsibly and safely](https://deepmind.google/blog/developing-gemini-4-argon-responsibly-and-safely/)**  
  
- **[Gemini 4 Argon for Robotics](https://deepmind.google/blog/gemini-4-argon-for-robotics/)**  
  
- **[Gemini 4 Argon: Built to solve your hardest problems](https://deepmind.google/blog/introducing-gemini-4-argon/)**  
  

## Lab Blog: Anthropic (unofficial mirror)
- **[An update on independent evaluators](https://www.anthropic.com/news/an-update-on-independent-evaluators)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><img alt="An update on independent evaluators" class="PostDetail-module-scss-module__U
- **[Preparing for the 2026 US midterms](https://www.anthropic.com/news/2026-us-midterms)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"></div><div class="page-wrapper"><article><div class="ArticleDetail-module-scss-module__YVTUHa__grid"><div class="ArticleDetail-module-scss-module__YVTUHa__sidebar
- **[Anthropic opens Singapore office and signs MOU with the Government of Singapore](https://www.anthropic.com/news/singapore-office-opening)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><div class="Illustration-module-scss-module__WyGOtq__root Illustration-module-scss-mod
- **[2026 Usage Policy update](https://www.anthropic.com/news/2026-usage-policy-update)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"></div><div class="page-wrapper"><article><div class=""><div class="Body-module-scss-module__z40yvW__body"><p class="Body-module-scss-module__z40yvW__reading-colum
- **[Building on our commitment to American scientific discovery](https://www.anthropic.com/news/genesis-mission-commitment)**  
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
- **[Be There for the Beginning: Celebrate the Launch of NVIDIA RTX Spark](https://blogs.nvidia.com/blog/local-ai-rtx-spark-launch-event-invite/)**  
  A new beginning for Windows PCs starts tomorrow with the launch of NVIDIA RTX Spark — one PC built for creators, gamers and AI agents. All are invited to celebrate with NVIDIA and partners at launch events around the world. Share Your Spark Every PC 
- **[Open From Data Center to Desktop: NVIDIA Expands Nemotron Family With Highest Efficiency Super VL and Bolt Models](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)**  
  NVIDIA today released Nemotron 3.5 Super VL, an open 120-billion-parameter model that delivers the fastest task completion and highest accuracy for specialized always-on agents. Joining it are two new edge models: Nemotron 3.5 Bolt 74B-A9B 24GB, opti
- **[Dial Up the Cloud: NVIDIA DLSS 4.5 Controls Arrive on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-enshrouded-update/)**  
  Dial in the next gaming session this GFN Thursday. New NVIDIA DLSS 4.5 controls give GeForce NOW members more choice over how supported games look and perform in the cloud, even without the latest hardware. Then, step into the Shroud as Keen Games’ E
- **[NVIDIA Expands Advanced Technology Access for Europe’s Scientific Community Through Open Learning Resources, Collaborations and Compute](https://blogs.nvidia.com/blog/ec-scientific-computing-pledge/)**  
  Much of today’s scientific progress begins with computation.  But turning accelerated computing’s potential into scientific progress — modeling climate systems, designing molecules, simulating materials and more — depends on more than breakthrough te
- **[The Nordics and NVIDIA Show What’s Possible When a Region Commits to Advanced Computing](https://blogs.nvidia.com/blog/nordics-technology-ecosystem/)**  
  The Nordic countries have become the European leader in unicorn startup density, producing the most emerging companies valued at $1 billion or more per capita on the continent. Now, a new chapter for the region is unfolding as countries race to build

## Lab Blog: NVIDIA Technical Blog
- **[NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)**  
  <img alt="Illustration of a central AI model connecting code, charts, credit memo data extraction, and video analysis." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/Nemot
- **[Scale Agentic Coding Workflows with Meta’s Muse Spark Open on NVIDIA GB300 NVL72](https://developer.nvidia.com/blog/scale-agentic-coding-workflows-with-metas-muse-spark-open-on-nvidia-gb300-nvl72/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/open-model-unbox-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="open-model-unbox" w
- **[Optimizing Agent Reliability and Tool Calling Efficiency for Chip Design Using NVIDIA NeMo Gym](https://developer.nvidia.com/blog/optimizing-agent-reliability-and-tool-calling-efficiency-for-chip-design-using-nvidia-nemo-gym/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/agentic-workflow-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="agentic-workflow" w
- **[How to Rewrite Apache Spark UDFs for GPU Acceleration with AI Agents](https://developer.nvidia.com/blog/rewrite-apache-spark-udfs-gpu-acceleration-ai-agents/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image2-5-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image2" width="768" />Enter
- **[NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/01/run-ai-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="run-ai" width="768" />NVIDIA 

## GitHub Trending (AI, new repos)
- **[Generated-Computers/Locals](https://github.com/Generated-Computers/Locals)**  
  ★ 13 — Run many AI agents at once on your Mac, about three times faster.
- **[enhesa/big-agentic-brain](https://github.com/enhesa/big-agentic-brain)**  
  ★ 10 — Memory, messaging and collaboration for AI agents. Shared learnings, reminders and agent-to-agent messages with trust-weighted ranking, behind a JSON API, MCP and a Claude Code plugin. One container, 
- **[burlakovmb/NOWA-Bio-Inspired-AI](https://github.com/burlakovmb/NOWA-Bio-Inspired-AI)**  
  ★ 8 — New bio inspired AI
- **[alfera-labs/company-use](https://github.com/alfera-labs/company-use)**  
  ★ 7 — The Open Source AI Co-worker for your whole team. Lives in Slack, API, Whatsapp, web and gets work done.
- **[gautamjajoo/awesome-economics-of-ai](https://github.com/gautamjajoo/awesome-economics-of-ai)**  
  ★ 3 — A curated guide to the costs, markets, adoption, and economic effects of AI.
- **[DefinetlyNotAI/Ageatopia](https://github.com/DefinetlyNotAI/Ageatopia)**  
  ★ 3 — A local-first multi-agent AI research platform for studying autonomous behavior, survival incentives, emergent dynamics, and learning in isolated simulated worlds.
- **[federicolaterra/knemora](https://github.com/federicolaterra/knemora)**  
  ★ 3 — Open-source, Local-first AI (SI) Second Brain.
- **[47thtechcorner/RayCodes_LFM-2.5-A2B](https://github.com/47thtechcorner/RayCodes_LFM-2.5-A2B)**  
  ★ 2 — Liquid AI's New LFM 2.5 Is INSANE — 184 TOK/S With Only 2B Active! (Live Tests) - High-performance local edge reasoning guide, prompts, and deployment for LFM2.5-24B-A2B hybrid architecture
- **[ydvsamiirrr2007/polar-science-hub](https://github.com/ydvsamiirrr2007/polar-science-hub)**  
  ★ 2 — An AI-powered polar science knowledge hub for discovering research, exploring Arctic and Antarctic science, and creating accessible science outreach content.
- **[Muguett-DBY/Muguett-DBY](https://github.com/Muguett-DBY/Muguett-DBY)**  
  ★ 2 — Custard: data science, AI, creative tools, and little worlds.
