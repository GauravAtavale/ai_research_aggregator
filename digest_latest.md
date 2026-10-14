# AI Research Digest — 2026-10-13

## HF Daily Papers (Trending)
- **[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**  
  ⬆ 23 upvotes — The landscape of software development has witnessed a paradigm shift with the
advent of AI-powered assistants, exemplified by GitHub Copilot. However,
existing solutions are not leveraging all the potential capabilities available
in an IDE such as building, testing, executing code, git operations, e
- **[RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://huggingface.co/papers/2610.13912)**  
  ⬆ 32 upvotes — Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predict
- **[PyTorch Distributed: Experiences on Accelerating Data Parallel Training](https://huggingface.co/papers/2006.15704)**  
  ⬆ 13 upvotes — This paper presents the design, implementation, and evaluation of the PyTorch
distributed data parallel module. PyTorch is a widely-adopted scientific
computing package used in deep learning research and applications. Recent
advances in deep learning argue for the value of large datasets and large
m
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 26 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 151 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality](https://huggingface.co/papers/2609.33757)**  
  ⬆ 234 upvotes — Symbolic models make melody, harmony, rhythm, and form explicit but typically stop before a finished recording; audio models produce complete songs while leaving composition implicit. We introduce YuE2, which unifies symbolic and audio music generation at frontier quality through symbolic planning. 
- **[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**  
  ⬆ 18 upvotes — The advent of 1-bit large language models (LLMs), led by BitNet b1.58, has
spurred interest in ternary LLMs. Despite this, research and practical
applications focusing on efficient edge inference for ternary LLMs remain
scarce. To bridge this gap, we introduce Bitnet.cpp, an inference system
optimiz
- **[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**  
  ⬆ 113 upvotes — Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person
- **[HuggingFace's Transformers: State-of-the-art Natural Language Processing](https://huggingface.co/papers/1910.03771)**  
  ⬆ 34 upvotes — Recent progress in natural language processing has been driven by advances in
both model architecture and model pretraining. Transformer architectures have
facilitated building higher-capacity models and pretraining has made it
possible to effectively utilize this capacity for a wide variety of task
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 92 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,

## HF Daily Papers (Today, by Upvotes)
- **[GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://huggingface.co/papers/2609.39601)**  
  ⬆ 246 upvotes — Precise grounding matters. It specifies which object is the target and where that object is, even in clutter and for tiny objects, and it has to be fast enough for closed-loop control. Yet vision-language-action (VLA) and world-action models (WAMs) take perception from general-purpose vision-languag
- **[Thinking Inertia: LLMs Keep Thinking When Told Not To](https://huggingface.co/papers/2610.11765)**  
  ⬆ 215 upvotes — Large Language Models (LLMs) increasingly ship with explicit "thinking modes", yet their counterpart, "no-thinking", has received far less attention. We study LLMs' no-thinking behavior along two axes. a. How to measure no-thinking? Prior work typically defines no-thinking through proxies such as a 
- **[AgentSWE: Can Coding Agents Build the Agent You Actually Want?](https://huggingface.co/papers/2610.13361)**  
  ⬆ 200 upvotes — As the production of software passes into the hands of software itself, coding agents are increasingly commissioned to build agents fitted to their users' own workflows. This delegation carries a quiet assumption, that the delivered agent will faithfully serve the requirement it was built for, rathe
- **[Scaling Agentic Data for Long-Horizon Terminal Intelligence](https://huggingface.co/papers/2610.13166)**  
  ⬆ 133 upvotes — Terminal agents are moving beyond local operations toward completing real-world professional tasks. Short trajectories can demonstrate commands and tool calls, but they do not fully show how agents accumulate evidence through exploration, use it to inform judgments, continually adjust strategies bas
- **[VIS-Ground: Video Interactive Storytelling with Contextual Grounding](https://huggingface.co/papers/2610.09326)**  
  ⬆ 79 upvotes — Video interactive storytelling enables viewers to actively steer how a video unfolds. However, once we allow viewers to intervene during generation, a new challenge arises: The viewer's request can have latent dependencies on both the grounding source and the current rendered video state. These depe
- **[GroundAnything: Reconciling Parallel Decoding with Precise Visual Grounding at Flash Speed](https://huggingface.co/papers/2609.39600)**  
  ⬆ 71 upvotes — Autoregressive (AR) grounding models serialize spatial predictions, introducing sequential latency and imposing a causal order on output tokens. We view grounding as visual evidence extraction: objects, locations, and spatial relations are jointly constrained by the image and query, yet their depend
- **[Multi-Stream Attention Residuals](https://huggingface.co/papers/2610.13630)**  
  ⬆ 34 upvotes — Attention Residuals (AttnRes) enables content-dependent retrieval over network depth, which can be viewed as single-stream softmax attention along the depth axis. Inspired by the success of multi-head attention along the sequence axis, we introduce Multi-Stream Attention Residuals (MSAR), an extensi
- **[Relevance Does Not Imply Applicability: Experience Activation for Personal GUI Agents](https://huggingface.co/papers/2609.33304)**  
  ⬆ 29 upvotes — Personal Graphical User Interface (GUI) agents rely on interaction history to infer what a user wants from ambiguous instructions and to anticipate recurring routines. Existing approaches retrieve task-relevant history and append it to the policy's context, implicitly assuming that experience releva
- **[PR-OPD: Privileged Representation On-policy Self-Distillation for Agentic Reinforcement Learning](https://huggingface.co/papers/2609.36642)**  
  ⬆ 25 upvotes — Language-model agents are usually trained by reinforcement learning from one reward per episode, and privileged self-distillation enriches it by letting the same policy, given a skill, teach its skill-free self through token probabilities. However, we identify two phenomena that question this channe
- **[CrossTimeEdit: A Decade-Spanning Cross-View Dataset and Reward-Guided Editing for Historical Street-View Generation](https://huggingface.co/papers/2609.36616)**  
  ⬆ 20 upvotes — Historical street-view imagery records urban evolution, but uneven coverage leaves substantial gaps in historical records. Generating plausible past appearances requires restoring changed structures while preserving persistent scene content. We construct VIGOR-his, a decade-spanning cross-view datas

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
- **[Higgsfield takes AI video from 1 minute to over 10](https://openai.com/index/higgsfield-longer-videos-voice)**  
  Higgsfield brings creators longer videos with GPT-6 Astra, precise visuals with GPT-Image-2.5, and a path to voice filmmaking with GPT-Live.
- **[Sophos cuts threat investigation time by 96% with OpenAI Daybreak](https://openai.com/index/sophos)**  
  Discover how Sophos uses OpenAI’s Daybreak to cut cyber-threat investigation time by 96% and automate 52% of MDR cases while preserving human oversight.
- **[Asana cuts model costs 76x in browser tests with GPT-6.1 Sol](https://openai.com/index/asana-browser-agent)**  
  Using GPT-6 Astra in Codex, Asana made its browser agent 76x cheaper and 5x faster in tests to offer customers more capable models.
- **[How Oracle turns days of work into minutes with ChatGPT and Codex](https://openai.com/index/oracle)**  
  Across recruiting, engineering, and operations, Oracle turns specialist knowledge into fast, repeatable workflows with ChatGPT Work and Codex.
- **[Pollo AI turns creative ideas into campaigns with OpenAI](https://openai.com/index/pollo-ai)**  
  With GPT-5.6, GPT-6 Astra, and GPT‑Image‑2.5, Pollo AI helps creators turn bold ideas into detailed images and cinematic video ads.

## Lab Blog: DeepMind
- **[Developing Gemini 4 Argon responsibly and safely](https://deepmind.google/blog/developing-gemini-4-argon-responsibly-and-safely/)**  
  
- **[Gemini 4 Argon for Robotics](https://deepmind.google/blog/gemini-4-argon-for-robotics/)**  
  
- **[Gemini 4 Argon: Built to solve your hardest problems](https://deepmind.google/blog/introducing-gemini-4-argon/)**  
  
- **[EmbeddingGemma 2: an open, lightweight multimodal embedding model](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/)**  
  
- **[Gemini 4 Argon: our next era of frontier intelligence](https://deepmind.google/blog/gemini-4-argon-our-next-era-of-frontier-intelligence/)**  
  

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
- **[All Systems Go: Global PC App Ecosystem Ready for NVIDIA RTX Spark](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-software-updates/)**  
  NVIDIA RTX Spark is a new beginning for the PC — a reinvention combining the capabilities of a gaming PC, a creative studio and a personal AI supercomputer into a single superchip. With up to 128GB of unified memory and 1 petaflop of AI compute, RTX 
- **[NVIDIA Announces New Investments in France’s Startups](https://blogs.nvidia.com/blog/france-ecosystem-agentic-computing/)**  
  Companies in France are deploying agentic computing across industries spanning space, financial services, the public sector and scientific research, demonstrating how the country’s ecosystem has moved from ambition to application. France’s progress s
- **[OCP Global Summit: Amid Ecosystem Adoption, NVIDIA Opens Vera Rubin Architecture to Help Scale AI Factories Worldwide](https://blogs.nvidia.com/blog/ocp-global-summit-vera-rubin-scale-ai-factories/)**  
  As AI factories grow from megawatts to gigawatts, building them takes more than advanced computing. Open standards are helping the industry scale AI infrastructure faster, more efficiently and more reliably. At the Open Compute Project (OCP) Global S
- **[Into the Omniverse: How Developers Turn Ideas Into Simulations With Frontier AI Agents](https://blogs.nvidia.com/blog/developers-simulation-frontier-ai-agents/)**  
  Turning a simulation idea into a working application means assembling assets, connecting physics and rendering, and checking that the scene behaves as intended. Developers are combining frontier AI models with NVIDIA Omniverse libraries to help carry
- **[Rally Up: ‘Gears of War: E-Day’ Launches on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-gears-of-war-e-day/)**  
  Gears of War: E-Day leads the charge on GeForce NOW this week, bringing Marcus Fenix and Dom Santiago’s first fight against the Locust Horde to the cloud with GeForce RTX-powered performance. A new way to join the action is also coming: Fire TV users

## Lab Blog: NVIDIA Technical Blog
- **[How to Rewrite Apache Spark UDFs for GPU Acceleration with AI Agents](https://developer.nvidia.com/blog/rewrite-apache-spark-udfs-gpu-acceleration-ai-agents/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image2-5-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image2" width="768" />Enter
- **[NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/01/run-ai-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="run-ai" width="768" />NVIDIA 
- **[ReplaySSM: Rethinking State Storage for Faster Hybrid-Model Decoding](https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/)**  
  <img alt="A cube assembled from smaller dark blocks, with glowing cyan, pink, yellow, and green sections against a black background." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads
- **[5 Steps to Create SimReady Assets for Robotics with Frontier AI Models](https://developer.nvidia.com/blog/5-steps-to-create-simready-assets-for-robotics-with-frontier-ai-models/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="360" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image6-2.gif" style="display: block; margin-bottom: 5px; clear: both;" title="image6" width="640" />Preparing CAD
- **[Building Reliable Data Analytics Agents: Lessons from the KDD Cup](https://developer.nvidia.com/blog/building-reliable-data-analytics-agents-lessons-from-the-kdd-cup/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/KGMON-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="KGMON" width="768" />The NVIDI

## GitHub Trending (AI, new repos)
- **[burlakovmb/NOWA-Bio-Inspired-AI](https://github.com/burlakovmb/NOWA-Bio-Inspired-AI)**  
  ★ 7 — New bio inspired AI
- **[lucidrains/selfplay2perfect](https://github.com/lucidrains/selfplay2perfect)**  
  ★ 5 — Implementation of Play2Perfect, from Tyler Ga Wei Lum et al. of Stanford, but with a Self Play element
- **[shashikantdev3/attention-span](https://github.com/shashikantdev3/attention-span)**  
  ★ 4 — Daily AI news, fact-checked and traced back to its roots. A source-checked history of AI since 1943, a glossary with lineage, and the labs and people behind it. Open data, built nightly on free Gemini
- **[SamurAIGPT/Text-To-Video-AI](https://github.com/SamurAIGPT/Text-To-Video-AI)**  
  ★ 3 — Generate video from text using AI
- **[Kingsmichaei/oyago](https://github.com/Kingsmichaei/oyago)**  
  ★ 3 — OyaGO: Lagos bus directions with Gemma + Backboard RAG and memory
- **[DefinetlyNotAI/Ageatopia](https://github.com/DefinetlyNotAI/Ageatopia)**  
  ★ 3 — A local-first multi-agent AI research platform for studying autonomous behavior, survival incentives, emergent dynamics, and learning in isolated simulated worlds.
- **[gautamjajoo/awesome-economics-of-ai](https://github.com/gautamjajoo/awesome-economics-of-ai)**  
  ★ 2 — A curated guide to the costs, markets, adoption, and economic effects of AI.
- **[jesusgarciafernandez/Aula-y-Comunidad-Educativa-Aumentada](https://github.com/jesusgarciafernandez/Aula-y-Comunidad-Educativa-Aumentada)**  
  ★ 2 — Aula es un entorno gratuito de IA con agentes, skills y workflow que te ayuda a preparar actividades, adaptar explicaciones y organizar tutorías con inteligencia artificial. Tus conocimientos, habilid
- **[ydvsamiirrr2007/polar-science-hub](https://github.com/ydvsamiirrr2007/polar-science-hub)**  
  ★ 2 — An AI-powered polar science knowledge hub for discovering research, exploring Arctic and Antarctic science, and creating accessible science outreach content.
- **[icon-lab/FLEX-MRI](https://github.com/icon-lab/FLEX-MRI)**  
  ★ 2 — Official PyTorch implementation of FLEX-MRI: Stochastic Finite-Transition Learning and Exploration for Accelerated MRI Reconstruction
