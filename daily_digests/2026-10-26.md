# AI Research Digest — 2026-10-26

## HF Daily Papers (Trending)
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 123 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 154 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 30 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 62 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**  
  ⬆ 104 upvotes — Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system t
- **[Very Large-Scale Multi-Agent Simulation in AgentScope](https://huggingface.co/papers/2407.17789)**  
  ⬆ 48 upvotes — Recent advances in large language models (LLMs) have opened new avenues for
applying multi-agent systems in very large-scale simulations. However, there
remain several challenges when conducting multi-agent simulations with existing
platforms, such as limited scalability and low efficiency, unsatisf
- **[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**  
  ⬆ 71 upvotes — Driven by rapid advancements of Large Language Models (LLMs), agents are
empowered to combine intrinsic knowledge with dynamic tool use, greatly
enhancing their capacity to address real-world tasks. In line with such an
evolution, AgentScope introduces major improvements in a new version (1.0),
towa
- **[Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training](https://huggingface.co/papers/2610.05416)**  
  ⬆ 23 upvotes — Natively training joint video-audio generation models at higher resolutions empowers them to learn richer visual details and sharper motion dynamics. However, full attention incurs quadratic cost and, as resolution increases, spreads attention over increasingly redundant tokens, diluting learning si
- **[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**  
  ⬆ 121 upvotes — Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 99 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,

## HF Daily Papers (Today, by Upvotes)
- **[Reading, Writing, Sharing, and Interacting with the World through Video](https://huggingface.co/papers/2610.31668)**  
  ⬆ 216 upvotes — Video foundation models have advanced rapidly in understanding and generating visual sequences, while video world models seek to capture the underlying dynamics of the world they depict. Despite their different objectives, both concern the relationship between video observations and an evolving worl
- **[UserArena: Benchmarking Interactive User Simulation for Long-Horizon Shopping Agents](https://huggingface.co/papers/2610.30932)**  
  ⬆ 47 upvotes — Agentic recommendation pursues shopper goals through sequences of context-dependent decisions. Developing and evaluating such policies requires faithful recommendation world models that capture both the interactive shopping environment and users' behavioral responses over long interactions. Existing
- **[HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games](https://huggingface.co/papers/2610.31162)**  
  ⬆ 38 upvotes — Building virtual embodied agents that operate in open-ended games like human players is a long-standing goal requiring both long-horizon autonomy and reliable native-interface control. As a procedurally generated open world, Minecraft provides a natural testbed for studying the integration of these 
- **[RSIHub: A Composable Framework for Agent-Evolution Methods](https://huggingface.co/papers/2610.32253)**  
  ⬆ 34 upvotes — Agent-evolution methods use execution feedback to improve prompts, skills, tools, and orchestration, but their implementations often rebuild the same experimental machinery. We present RSIHub, an open-source framework for building, comparing, and extending these methods on shared infrastructure. Rec
- **[RynnUnify: Towards Unified Embodied Brain](https://huggingface.co/papers/2610.32965)**  
  ⬆ 33 upvotes — We introduce RynnUnify, a 16B unified embodied model that combines strong embodied understanding with long-horizon visual planning through interleaved video--language reasoning. With capabilities spanning spatial reasoning, physical prediction, and grounding, RynnUnify connects an understanding of t
- **[Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for Omni LLMs](https://huggingface.co/papers/2610.27103)**  
  ⬆ 21 upvotes — Recent Omni LLMs (OLLMs) have demonstrated remarkable capabilities in joint audio-visual reasoning, yet cross-modal hallucinations remain a major challenge. Existing mitigation methods mainly operate at the output level, overlooking the entanglement of grounding evidence and learned priors within fu
- **[Every Weight Is a Path of Shared Discrete Decisions](https://huggingface.co/papers/2610.31931)**  
  ⬆ 19 upvotes — We introduce TWIG (Tree-structured Weights with Inherited Gates), a representation in which every weight of a neural network is the end of a path of small discrete decisions: a sign, a shift by a power of two, a zero gate, an index into a shared table. Weights that belong together share the upper pa
- **[Dual Exam: Controlled Evaluation of Multimodal Agents and World Models](https://huggingface.co/papers/2610.31066)**  
  ⬆ 16 upvotes — World Models (WMs) can support Multimodal Agents (MAs) through simulated experience, while Agent trajectories can inform World Model refinement. Evaluating this interaction requires separate evidence about action selection and state evolution. We introduce Dual Exam, which tests Agents under fixed e
- **[DirCast: Live Esports Directing and Commentary with a Single Streaming Video-Language Model](https://huggingface.co/papers/2610.31734)**  
  ⬆ 16 upvotes — A live esports broadcast needs a director who chooses which camera goes on air and a caster who talks over that choice, every second and without knowing what comes next. Streaming video language models have learned to commentate, but only over a broadcast that a human director has already produced. 
- **[TenetBench: A Clause-Anchored Russian Corpus for Evaluating Language Models against Professional Codes of Ethics](https://huggingface.co/papers/2610.29477)**  
  ⬆ 12 upvotes — Codes of professional ethics guide and restrict specialists, who increasingly work with assistants built on large language models. Such an assistant can breach the user's code, or help the user breach it, without the user noticing. Evaluations reporting broad categories of harm cannot show how often

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[TCSP3.0: Template-Based Crystal Structure Prediction with Coefficient-Preserving Element Substitution and Structural Diversity](https://arxiv.org/abs/2610.34029v1)**  
  Template-based crystal structure prediction (CSP) transfers a known crystal structure to a new composition by element substitution, so its accuracy depends on retrieving suitable templates, mapping elements and ranking the resulting candidates correctly. Auditing the original TCSP2.0 implementation 
- **[When Does GEPA Merge Help? A Mechanism-Level Diagnostic](https://arxiv.org/abs/2610.34027v1)**  
  GEPA is among the strongest reflective prompt optimizers for language-model programs, but its system-aware merge operator is unstable across models: merge improves gpt-4.1-mini on average while degrading Qwen3-8B, an asymmetry noted but left unexplained by the GEPA paper. We investigate this instabi
- **[The Symmetry of Differential Neural Tangent Kernel under the Orthogonal Group](https://arxiv.org/abs/2610.34023v1)**  
  The differential neural tangent kernel (DNTK) is a tool for analyzing the training dynamics of overparameterized physics informed neural networks. In this work, we investigate the symmetry of the infinite DNTK under an orthogonal group, for two layer and deep neural networks separately, based on the
- **[Deep Scientific Reasoning under Physical Constraints: Structure-Aware Spectrum Prediction](https://arxiv.org/abs/2610.34021v1)**  
  Structured scientific spectra encode rich physical information while obeying hard constraints, such as conservation laws and characteristic spectral geometry. Accurate prediction of these spectra is central to materials discovery, yet existing methods often treat them as unconstrained sequences and 
- **[BriLLM-MetaPred: A Representation-Prediction Unity Language Model with Adaptive Self-Measurement](https://arxiv.org/abs/2610.34018v1)**  
  We present BriLLM-MetaPred, the first engineering implementation of the MetaPred machine-learning framework established by a mathematical theory of AGI, instantiated for language modeling. The theory argues that MetaPred is both necessary and sufficient as a machine-learning primitive for general co
- **[The Information Geometry of Representation Formation](https://arxiv.org/abs/2610.34015v1)**  
  Most analyses of neural representations focus on trained endpoints, leaving the process by which internal structure forms comparatively unmeasured. We instead treat representation formation itself as an object of study, asking whether the path a representation takes through training reveals informat
- **[The Patient Is Always Right? Evaluating Sycophancy in Medical Diagnosis with Graded Patient Beliefs](https://arxiv.org/abs/2610.34013v1)**  
  More people are seeking out general-purpose AI models for medical advice, including diagnosis. Yet, AI models are susceptible to sycophancy, like validating users' beliefs even when they are untrue, which could lead to false positive diagnoses. Here, we evaluate how nine AI models change their diagn
- **[Reversible Pseudonymisation of Documents Sent to External LLMs: an Open Bilingual Benchmark and an Engine](https://arxiv.org/abs/2610.34012v1)**  
  Professionals send working documents to external large language models. A common safeguard is reversible pseudonymisation: personal data are replaced with placeholders before the request and restored locally in the answer. We present an open benchmark of five existing open tools and a regular-expres
- **[Cross-User Adaptation for sEMG Gesture Recognition via Continual Learning](https://arxiv.org/abs/2610.34011v1)**  
  Prosthetic and assistive interfaces increasingly depend on decoding hand gestures from surface electromyography (sEMG). Because the signal is shaped by person-specific factors, the recurrent neural networks (RNNs) commonly used to model these temporal streams must adapt to new wearers and new gestur
- **[Fed-Universe: A Semantic-Geometric-Topological-Human (S-G-T-H) Stack for Negotiated Alignment in Federated Systems](https://arxiv.org/abs/2610.34009v1)**  
  Conventional federated learners implicitly optimize for global means, creating a "one-size-fits-all" paradigm that inevitably suppresses the minority under cross-site heterogeneity. To bridge this critical gap, we present Fed-Universe, a generalizable Semantic-Geometric-Topological-Human (S-G-T-H) a

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Greptile takes bug detection beyond code review with GPT-6 Astra](https://openai.com/index/greptile-code-review-codex-astra)**  
  How Greptile uses GPT-6 Astra to test user workflows, Daybreak to strengthen security, and Codex to reduce rework.
- **[Working with academic communities to build scientific understanding](https://openai.com/index/building-scientific-understanding-with-academic-communities)**  
  OpenAI shares model results on the Kakeya conjecture, Exponential Time Hypothesis, and quantum chromodynamics—and how researchers can verify and build on them.
- **[GPT-6.1 Sol helps CodeRabbit strengthen security across complex codebases](https://openai.com/index/gpt-6-1-sol-coderabbit-code-security)**  
  CodeRabbit uses GPT-6.1 Sol to investigate security risks across complex codebases. Its security agent helps developers review findings and proposed fixes.
- **[ChatGPT’s expanding world of work](https://openai.com/index/chatgpt-expanding-world-of-work)**  
  Explore OpenAI Signals data on 165 work activities across nearly 100 countries, revealing how people use ChatGPT for work and how usage changes over time.
- **[How Fanatics and OpenAI streamline the fan experience](https://openai.com/index/fanatics-streamline-fan-experience)**  
  Fanatics uses OpenAI to help fans complete their game-day outfits with Shop the Look. Testing across roughly 30,000 MLB products showed 10% higher engagement.

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
- **[How NVIDIA Minerva Turns Telemetry Chaos Into Peak GPU Yield](https://developer.nvidia.com/blog/how-nvidia-minerva-turns-telemetry-chaos-into-peak-gpu-yield/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/MinervaKV-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="MinervaKV" width="768" />A
- **[How NVIDIA Mission Control 2.5 Brings Autonomous Recovery to Kubernetes](https://developer.nvidia.com/blog/how-nvidia-mission-control-2-5-brings-autonomous-recovery-to-kubernetes/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="431" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/7_resized-768x431.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="7_resized" width="768" />T
- **[Scaling NVIDIA TensorRT Performance Optimization Beyond a Single Build Route with the Global Performance Tuner, Part 2](https://developer.nvidia.com/blog/scaling-nvidia-tensorrt-performance-optimization-beyond-a-single-build-route-with-the-global-performance-tuner-part-2/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/desktop-computer-overlay-light-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="deskt
- **[Scaling NVIDIA TensorRT Performance Optimization Beyond a Single Build Route with the Global Performance Tuner, Part 1](https://developer.nvidia.com/blog/scaling-nvidia-tensorrt-performance-optimization-beyond-a-single-build-route-with-the-global-performance-tuner-part-1/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/desktop-computer-overlay-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="desktop-com
- **[Using AI Agents to Teach Robots Like Microduck to Walk in Simulation](https://developer.nvidia.com/blog/using-ai-agents-to-teach-robots-like-microduck-to-walk-in-simulation/)**  
  <img alt="Microduck robot in an obstacle course with labeled ramps, platforms, a rubber mat, and other objects." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/Microduck-la

## GitHub Trending (AI, new repos)
- **[agentshield-dev/agentshield](https://github.com/agentshield-dev/agentshield)**  
  ★ 54 — Agentshield is open source defense for Kubernetes and AWS. It learns how your workloads really talk, flags lateral movement with evidence, and proposes fixes you approve.
- **[Cinderubasp/InterviewCopilot-rpocket-team](https://github.com/Cinderubasp/InterviewCopilot-rpocket-team)**  
  ★ 54 — EdTech application designed to bridge the gap between learning and landing your dream job
- **[faraflow/faraflow](https://github.com/faraflow/faraflow)**  
  ★ 47 — Visual builder and execution engine for AI powered organizations
- **[OFat34764e/InterviewCopilot-rpocket-team](https://github.com/OFat34764e/InterviewCopilot-rpocket-team)**  
  ★ 32 — EdTech application designed to bridge the gap between learning and landing your dream job
- **[zidniryi/cutvii](https://github.com/zidniryi/cutvii)**  
  ★ 19 — CutVii - Creative editing. Flexible workflow. On-device AI
- **[xAerux/aerus-ezai](https://github.com/xAerux/aerus-ezai)**  
  ★ 7 — EZ AI — Local AI made easy: Windows command center for local AI apps, model library, and coding agents.
- **[refraction-ray/free-energy-to-llms](https://github.com/refraction-ray/free-energy-to-llms)**  
  ★ 6 — Generative models from variational free energy to LLM
- **[lucidrains/attention-contact-planning](https://github.com/lucidrains/attention-contact-planning)**  
  ★ 6 — Implementation of Attention-based Contact Planning, by Junzhe He of ETH Zürich
- **[sukhee-2626/plot-docs](https://github.com/sukhee-2626/plot-docs)**  
  ★ 5 — A local-first AI office suite for Docs, Sheets, Slides, PDF, Markdown and HTML. Windows, macOS and Linux.
- **[mostwanted7/ygo-agent](https://github.com/mostwanted7/ygo-agent)**  
  ★ 4 — AI Yu-Gi-Oh! players for EDOPro: a headless duel host, pluggable model backends, live coaching and deck training.
