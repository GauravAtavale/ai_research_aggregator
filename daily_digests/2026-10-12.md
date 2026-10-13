# AI Research Digest — 2026-10-12

## HF Daily Papers (Trending)
- **[RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://huggingface.co/papers/2610.13912)**  
  ⬆ 30 upvotes — Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predict
- **[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**  
  ⬆ 22 upvotes — The landscape of software development has witnessed a paradigm shift with the
advent of AI-powered assistants, exemplified by GitHub Copilot. However,
existing solutions are not leveraging all the potential capabilities available
in an IDE such as building, testing, executing code, git operations, e
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 26 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[PyTorch Distributed: Experiences on Accelerating Data Parallel Training](https://huggingface.co/papers/2006.15704)**  
  ⬆ 13 upvotes — This paper presents the design, implementation, and evaluation of the PyTorch
distributed data parallel module. PyTorch is a widely-adopted scientific
computing package used in deep learning research and applications. Recent
advances in deep learning argue for the value of large datasets and large
m
- **[YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality](https://huggingface.co/papers/2609.33757)**  
  ⬆ 233 upvotes — Symbolic models make melody, harmony, rhythm, and form explicit but typically stop before a finished recording; audio models produce complete songs while leaving composition implicit. We introduce YuE2, which unifies symbolic and audio music generation at frontier quality through symbolic planning. 
- **[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**  
  ⬆ 111 upvotes — Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person
- **[DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models](https://huggingface.co/papers/2610.12572)**  
  ⬆ 232 upvotes — Online reinforcement learning (RL) fine-tunes diffusion models with black-box rewards, but reverse-process methods such as Flow-GRPO are limited in efficiency by poor credit assignment, while forward-process methods such as DiffusionNFT are efficient yet unstable without carefully tuned exponential-
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 151 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://huggingface.co/papers/1910.03771)**  
  ⬆ 34 upvotes — Recent progress in natural language processing has been driven by advances in
both model architecture and model pretraining. Transformer architectures have
facilitated building higher-capacity models and pretraining has made it
possible to effectively utilize this capacity for a wide variety of task
- **[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**  
  ⬆ 18 upvotes — The advent of 1-bit large language models (LLMs), led by BitNet b1.58, has
spurred interest in ternary LLMs. Despite this, research and practical
applications focusing on efficient edge inference for ternary LLMs remain
scarce. To bridge this gap, we introduce Bitnet.cpp, an inference system
optimiz

## HF Daily Papers (Today, by Upvotes)
- **[DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models](https://huggingface.co/papers/2610.12572)**  
  ⬆ 232 upvotes — Online reinforcement learning (RL) fine-tunes diffusion models with black-box rewards, but reverse-process methods such as Flow-GRPO are limited in efficiency by poor credit assignment, while forward-process methods such as DiffusionNFT are efficient yet unstable without carefully tuned exponential-
- **[S-Space: Exploring Spatial Workspace in Multimodal Language Models](https://huggingface.co/papers/2610.13527)**  
  ⬆ 202 upvotes — Multimodal language models (MLLMs) exhibit promising spatial reasoning capabilities, yet the internal mechanisms supporting them remain poorly understood. We uncover S-Space, a linear representation subspace in which object-token representations encode continuous coordinates along horizontal, vertic
- **[Reflex: Visually Grounded Reactive Humanoid Control](https://huggingface.co/papers/2610.12772)**  
  ⬆ 132 upvotes — Humans effortlessly react to the world; they adeptly return a tennis shot, catch a falling cup, step aside from a passing cart, or pass a box tossed during truck unloading. These everyday actions require anticipating a moving target and reflexively responding with the whole body within about a secon
- **[SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments](https://huggingface.co/papers/2610.12611)**  
  ⬆ 85 upvotes — Computer-use agents (CUAs) are rapidly improving, yet synthesizing diverse and reliable software environments at scale remains challenging. Native application environments require substantial construction and integration effort, which limits application coverage and increases the risk of application
- **[EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents](https://huggingface.co/papers/2610.13021)**  
  ⬆ 63 upvotes — Continual learning requires models to accumulate past experience and transfer it to new tasks. Despite substantial research on continual learning, existing work remains largely confined to non-embodied settings, without extending to embodied environments. To address this gap, we introduce EmbodiedCL
- **[VisionWeave: Weaving Elastic Visual Representations as a Native Capability of MLLMs](https://huggingface.co/papers/2610.07987)**  
  ⬆ 55 upvotes — Multimodal large language models have become the dominant paradigm for visual understanding, but incur substantial costs by encoding inputs into dense, fixed-size patch tokens. However, visual information is unevenly distributed: some regions require fine-grained detail, while others admit compact r
- **[Hear the World in Stereo: Learning Dynamic Spatial Correspondence for Immersive Joint Video-Audio Generation](https://huggingface.co/papers/2609.38748)**  
  ⬆ 51 upvotes — Recent joint video-audio generation models have achieved strong semantic correspondence and temporal synchronization. However, applications such as AR/VR and interactive gaming further require stereo audio to provide an immersive sense, which remains largely overlooked. Effective stereo audio requir
- **[ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents](https://huggingface.co/papers/2610.13395)**  
  ⬆ 49 upvotes — Coding agents are increasingly used to build programs from scratch as software engineers do rather than to resolve issues within a repository or to generate a repository from a given requirements document. However, scalable verifiable training environments that force agents to discover what is requi
- **[Continually Post-training Small Models via Synthetic Self-distillation](https://huggingface.co/papers/2610.13113)**  
  ⬆ 41 upvotes — Continual post-training faces a dual challenge of acquisition and retention: models must learn new capabilities while preserving prior knowledge. While Self-Distillation Fine-Tuning (SDFT) mitigates this using self-supervision with in-context demonstrations, it relies on strong in-context learning a
- **[Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction](https://huggingface.co/papers/2610.12984)**  
  ⬆ 39 upvotes — Computer-use agents can perform increasingly complex GUI tasks, yet unfamiliar software and workflows requiring human domain knowledge remain challenging. Human demonstrations convey procedural knowledge through the same GUI interaction space, but reuse requires interpreting actions in context and s

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Can Language Models Play the Wikipedia Game?](https://arxiv.org/abs/2610.13948v1)**  
  Language models increasingly support or automate information retrieval from document collections too large to index. This task is difficult when it requires specialist linguistic or scientific knowledge. We used the Wikipedia Game to test language models on an analogous information retrieval task. I
- **[Hide and Seek: HIDE Concepts to SEEK explanations for black box models](https://arxiv.org/abs/2610.13935v1)**  
  Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They requi
- **[Constructive Bounds for the Topological Expressivity of Neural Networks](https://arxiv.org/abs/2610.13931v1)**  
  The expressivity of a neural network $Φ$ describes the class of functions that a network can express. The term topological expressivity refers to a family of measures particularly suited to understand binary classification and is often formulated in terms of the Betti numbers of a decision boundary 
- **[AI Models Can Provably Hide Arbitrary Capabilities](https://arxiv.org/abs/2610.13928v1)**  
  Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural
- **[KL Before and After Mixing: A Round-Complexity Separation in Parallel Sampling](https://arxiv.org/abs/2610.13924v1)**  
  A parallel sampler can choose at random which coordinates to generate together. For a target $p$ and the output law $q_U$ of a schedule $U$ drawn afresh for each output, we compare the schedule-averaged divergence $\mathbb{E}_U D_{\mathrm{KL}}(p\|q_U)$ with the output-law divergence $D_{\mathrm{KL}}
- **[Goal-Oriented Bundle Management and Flow Control for Deep-Space Communications via Reinforcement Learning](https://arxiv.org/abs/2610.13923v1)**  
  Deep-space communications operate under intermittent connectivity, long propagation delays, and relay storage constraints. In such networks, the Bundle Protocol enables store-carry-forward communication, requiring relay nodes to manage limited storage and scarce contact opportunities. Relay-side sch
- **[DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness](https://arxiv.org/abs/2610.13918v1)**  
  Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale bi
- **[Designing Protein Structures from Natural Language](https://arxiv.org/abs/2610.13917v1)**  
  A central challenge in de novo protein design is generating proteins with desired structural and functional properties. Existing design models typically require a dedicated input representation for each property, limiting the design objectives they support. We develop Prompteina, the first all-atom 
- **[RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://arxiv.org/abs/2610.13912v1)**  
  Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predict
- **[When VLMs Destroy What They Know: Spatial Representations Fall Below Lexical Priors](https://arxiv.org/abs/2610.13910v1)**  
  Vision-Language Models (VLMs) increasingly analyze and reason about images, yet it remains unclear whether their internal representations faithfully encode the structured relations required for such reasoning. We introduce EICS (Evaluation-Invariant Concept Stability), a metric for testing whether r

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Sophos cuts threat investigation time by 96% with OpenAI Daybreak](https://openai.com/index/sophos)**  
  Discover how Sophos uses OpenAI’s Daybreak to cut cyber-threat investigation time by 96% and automate 52% of MDR cases while preserving human oversight.
- **[Asana cuts model costs 76x in browser tests with GPT-6.1 Sol](https://openai.com/index/asana-browser-agent)**  
  Using GPT-6 Astra in Codex, Asana made its browser agent 76x cheaper and 5x faster in tests to offer customers more capable models.
- **[How Oracle turns days of work into minutes with ChatGPT and Codex](https://openai.com/index/oracle)**  
  Across recruiting, engineering, and operations, Oracle turns specialist knowledge into fast, repeatable workflows with ChatGPT Work and Codex.
- **[Pollo AI turns creative ideas into campaigns with OpenAI](https://openai.com/index/pollo-ai)**  
  With GPT-5.6, GPT-6 Astra, and GPT‑Image‑2.5, Pollo AI helps creators turn bold ideas into detailed images and cinematic video ads.
- **[LegalOn halves Codex costs while maintaining development speed](https://openai.com/index/legalon-halves-codex-costs)**  
  LegalOn cut estimated daily Codex costs by 65% while maintaining development speed. It matched Astra, Sol, and Luna to tasks and managed budgets strategically.

## Lab Blog: DeepMind
- **[EmbeddingGemma 2: an open, lightweight multimodal embedding model](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/)**  
  
- **[Gemini 4 Argon: our next era of frontier intelligence](https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/)**  
  
- **[Introducing SynthID Bio](https://deepmind.google/blog/introducing-synthid-bio/)**  
  Proof of concept for watermarking AI-generated proteins while preserving biological function.
- **[Introducing Gemini 3.8 Live with Live Avatar](https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/)**  
  
- **[Advancing Private AI Compute with secure, server-side memory](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/)**  
  Introducing private, server-side memory to Private AI Compute for personal AI.

## Lab Blog: Anthropic (unofficial mirror)
- **[2026 Usage Policy update](https://www.anthropic.com/news/2026-usage-policy-update)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"></div><div class="page-wrapper"><article><div class=""><div class="Body-module-scss-module__z40yvW__body"><p class="Body-module-scss-module__z40yvW__reading-colum
- **[Building on our commitment to American scientific discovery](https://www.anthropic.com/news/genesis-mission-commitment)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"></div><div class="page-wrapper"><article><div class=""><div class="Body-module-scss-module__z40yvW__body"><p class="Body-module-scss-module__z40yvW__reading-colum
- **[Introducing the Anthropic Cyber Mission](https://www.anthropic.com/news/anthropic-cyber-mission)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><img alt="Introducing the Anthropic Cyber Mission" class="PostDetail-module-scss-modul
- **[Expanding the Cyber Verification Program](https://www.anthropic.com/news/cyber-verification-program)**  
  <article><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"></div><div class="page-wrapper"><article><div class=""><div class="Body-module-scss-module__z40yvW__body"><p class="Body-module-scss-module__z40yvW__reading-column body-2 
- **[Anthropic invests $100 million to train 10,000 engineers and tackle the enterprise AI talent gap](https://www.anthropic.com/news/claude-frontier-academy)**  
  <article><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><div class="Illustration-module-scss-module__WyGOtq__root Illustration-module-scss-module__WyGO

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
- **[OCP Global Summit: Amid Ecosystem Adoption, NVIDIA Opens Vera Rubin Architecture to Help Scale AI Factories Worldwide](https://blogs.nvidia.com/blog/ocp-global-summit-vera-rubin-scale-ai-factories/)**  
  As AI factories grow from megawatts to gigawatts, building them takes more than advanced computing. Open standards are helping the industry scale AI infrastructure faster, more efficiently and more reliably. At the Open Compute Project (OCP) Global S
- **[Into the Omniverse: How Developers Turn Ideas Into Simulations With Frontier AI Agents](https://blogs.nvidia.com/blog/developers-simulation-frontier-ai-agents/)**  
  Turning a simulation idea into a working application means assembling assets, connecting physics and rendering, and checking that the scene behaves as intended. Developers are combining frontier AI models with NVIDIA Omniverse libraries to help carry
- **[Rally Up: ‘Gears of War: E-Day’ Launches on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-gears-of-war-e-day/)**  
  Gears of War: E-Day leads the charge on GeForce NOW this week, bringing Marcus Fenix and Dom Santiago’s first fight against the Locust Horde to the cloud with GeForce RTX-powered performance. A new way to join the action is also coming: Fire TV users
- **[NVIDIA, Microsoft Kick Off a New Beginning for Windows PCs With RTX Spark and AI Agents](https://blogs.nvidia.com/blog/local-ai-rtx-spark-microsoft-windows-event/)**  
  At a Microsoft event in San Francisco on Wednesday, NVIDIA founder and CEO Jensen Huang and Microsoft CEO Satya Nadella outlined how NVIDIA and Microsoft are co-engineering hardware and software for AI agents to run on Windows PCs. NVIDIA was founded
- **[Why Telecom Operators Are Building Their AI Strategy on Open Models](https://blogs.nvidia.com/blog/telecom-operators-open-models/)**  
  Telecom operators are increasingly building their AI strategies on open models — and the reasons go beyond mere cost.  Open models give telcos the ability to trust, control and customize AI across their most critical workloads — from autonomous netwo

## Lab Blog: NVIDIA Technical Blog
- **[ReplaySSM: Rethinking State Storage for Faster Hybrid-Model Decoding](https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/)**  
  <img alt="A cube assembled from smaller dark blocks, with glowing cyan, pink, yellow, and green sections against a black background." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads
- **[5 Steps to Create SimReady Assets for Robotics with Frontier AI Models](https://developer.nvidia.com/blog/5-steps-to-create-simready-assets-for-robotics-with-frontier-ai-models/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="360" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image6-2.gif" style="display: block; margin-bottom: 5px; clear: both;" title="image6" width="640" />Preparing CAD
- **[Building Reliable Data Analytics Agents: Lessons from the KDD Cup](https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/KGMON-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="KGMON" width="768" />The NVIDI
- **[The Machines that Make the Machines](https://developer.nvidia.com/blog/the-machines-that-make-the-machines/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image-1790985193398-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="image-1790985193
- **[Validate AI Factory Changes with Digital Twins and AI Agents](https://developer.nvidia.com/blog/validate-ai-factory-changes-with-digital-twins-and-ai-agents/)**  
  <img alt="Three monitors display a network simulation and infrastructure monitoring dashboards in front of data center server racks." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads

## GitHub Trending (AI, new repos)
- **[PkLavc/Autotrader](https://github.com/PkLavc/Autotrader)**  
  ★ 26 — Autonomous AI trading system powered by Kronos. Forecasts markets, builds portfolios and paper-trades automatically with GitHub Actions.
- **[burlakovmb/NOWA-Bio-Inspired-AI](https://github.com/burlakovmb/NOWA-Bio-Inspired-AI)**  
  ★ 6 — New bio inspired AI
- **[lucidrains/selfplay2perfect](https://github.com/lucidrains/selfplay2perfect)**  
  ★ 5 — Implementation of Play2Perfect, from Tyler Ga Wei Lum et al. of Stanford, but with a Self Play element
- **[shashikantdev3/attention-span](https://github.com/shashikantdev3/attention-span)**  
  ★ 4 — Daily AI news, fact-checked and traced back to its roots. A source-checked history of AI since 1943, a glossary with lineage, and the labs and people behind it. Open data, built nightly on free Gemini
- **[SamurAIGPT/Text-To-Video-AI](https://github.com/SamurAIGPT/Text-To-Video-AI)**  
  ★ 3 — Generate video from text using AI
- **[Kingsmichaei/oyago](https://github.com/Kingsmichaei/oyago)**  
  ★ 3 — OyaGO: Lagos bus directions with Gemma + Backboard RAG and memory
- **[Tykillita/Umbral](https://github.com/Tykillita/Umbral)**  
  ★ 2 — Evidence-backed news agenda for Panama: ranks five topics for editorial review with transparent scoring, sources, and human-controlled drafts.
- **[jesusgarciafernandez/Aula-y-Comunidad-Educativa-Aumentada](https://github.com/jesusgarciafernandez/Aula-y-Comunidad-Educativa-Aumentada)**  
  ★ 2 — Aula es un entorno gratuito de IA con agentes, skills y workflow que te ayuda a preparar actividades, adaptar explicaciones y organizar tutorías con inteligencia artificial. Tus conocimientos, habilid
- **[Muguett-DBY/Muguett-DBY](https://github.com/Muguett-DBY/Muguett-DBY)**  
  ★ 2 — Custard: data science, AI, creative tools, and little worlds.
- **[A220man/human-approval-console-ryan-vo](https://github.com/A220man/human-approval-console-ryan-vo)**  
  ★ 2 — Ryan Vo | Work in progress: human-approval-console-ryan-vo
