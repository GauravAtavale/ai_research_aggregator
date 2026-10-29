# AI Research Digest — 2026-10-28

## HF Daily Papers (Trending)
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 157 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 125 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 104 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,
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
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 62 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[Hy-Nomas: Towards Free-form Interactive World Generation](https://huggingface.co/papers/2610.36729)**  
  ⬆ 107 upvotes — Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences. We present Hy-Nomas, a video world model with an 8B diffusion backbone that supports free-form text instructions and continuous camera control across multiple interac
- **[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**  
  ⬆ 107 upvotes — Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system t
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 31 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training](https://huggingface.co/papers/2610.05416)**  
  ⬆ 23 upvotes — Natively training joint video-audio generation models at higher resolutions empowers them to learn richer visual details and sharper motion dynamics. However, full attention incurs quadratic cost and, as resolution increases, spreads attention over increasingly redundant tokens, diluting learning si

## HF Daily Papers (Today, by Upvotes)
- **[The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents](https://huggingface.co/papers/2610.36077)**  
  ⬆ 531 upvotes — Multimodal intelligence can be viewed as human-guided co-evolution between worlds and agents through interaction. However, scaling this process faces two bottlenecks: constructing heterogeneous, verifiable environments is costly, and manual Harness iteration cannot keep pace with growing task divers
- **[Multiscale Policy Optimization for Long-Horizon LLM Agents](https://huggingface.co/papers/2610.35013)**  
  ⬆ 373 upvotes — Long-horizon LLM agents interact with their environments through complete assistant turns while generating each action token by token. We observe that critic values vary primarily across turns, motivating optimization anchored at turns with finer credit allocation among tokens. We propose Multiscale
- **[ChronoReplay: One Answer Interface Is Not Enough for Streaming Spatial Intelligence](https://huggingface.co/papers/2610.34283)**  
  ⬆ 346 upvotes — Training a spatial VLM to answer which side an object lies on does not require it to preserve the metric displacement that determines that answer, while supervision for a distance estimate may leave categorical relations largely unconstrained. When post-training emphasizes one readout, improvements 
- **[VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation](https://huggingface.co/papers/2610.35864)**  
  ⬆ 172 upvotes — Diffusion video models produce striking clips, but they cannot reliably render an exact formula, a correct chart, a rule-consistent game or narration synchronized to on-screen events. A different route is emerging: multimodal agents that write code to render every frame and synthesize every sound. W
- **[PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://huggingface.co/papers/2610.37381)**  
  ⬆ 137 upvotes — Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited. Video world models can capture scene dynamics, yet generating future videos introduces high latency into the control loop. We
- **[Memory Tax: Dissecting the Net Value of Agent Memory](https://huggingface.co/papers/2610.34073)**  
  ⬆ 137 upvotes — Memory is increasingly used in long-horizon agents, yet the net value of building memory over direct retrieval from raw history remains largely unclear. Through a large-scale evaluation across multiple benchmarks and model backbones, we find many dedicated memory systems underperform naive RAG in ma
- **[Hy-Nomas: Towards Free-form Interactive World Generation](https://huggingface.co/papers/2610.36729)**  
  ⬆ 107 upvotes — Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences. We present Hy-Nomas, a video world model with an 8B diffusion backbone that supports free-form text instructions and continuous camera control across multiple interac
- **[Can Test-Time Memory Evolution Outperform Test-Time Training for Scientific Discovery?](https://huggingface.co/papers/2610.32046)**  
  ⬆ 101 upvotes — Recent test-time training (TTT) frameworks have enabled open-weight large language models (LLMs) to outperform inference-only frameworks powered by frontier models on scientific discovery tasks. However, TTT introduces additional computational cost for online weight updates during the discovery proc
- **[Can Discrete Tokens Serve as Semantically Lossless Representations of Visual Signals?](https://huggingface.co/papers/2610.37662)**  
  ⬆ 82 upvotes — Discrete visual tokens represent vision in a discrete form analogous to language, offering a native interface for multimodal modeling under a shared next-token prediction objective. However, quantization error is widely assumed to cause unavoidable semantic loss, fundamentally limiting the semantic 
- **[HABIT-Bench: Evaluating Habit Induction from Longitudinal Weak Evidence in Agent Memory](https://huggingface.co/papers/2610.24520)**  
  ⬆ 79 upvotes — In long-term interactions with large language model (LLM) agents, users reveal habits through their choices and actions. These habits capture implicit user information that agents must infer across conversations. However, individual observations may provide only partial evidence about a habit or whe

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction](https://arxiv.org/abs/2610.37668v1)**  
  Novel view synthesis and 3D reconstruction have advanced rapidly with radiance fields and splatting, yet their memory and computational demands limit their use in resource-constrained settings. We introduce Hexels: novel planar hexagonal surface elements with a first-order spatial color field for ef
- **[ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning](https://arxiv.org/abs/2610.37666v1)**  
  Vision-Language-Action (VLA) models have made substantial progress in robotic manipulation, but their generalization remains constrained by the diversity and coverage of action-labeled robot demonstrations. Human videos provide much broader behavioral and environmental experience, while learning fro
- **[When Should We Intervene at Test Time?](https://arxiv.org/abs/2610.37658v1)**  
  Test-time adaptation helps a deployed model respond to changing inputs, but the same intervention can rescue one batch and damage the next. Updating normalization statistics, for example, can improve corrupted images yet fail when a batch contains mostly one class. Average accuracy hides these failu
- **[Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness](https://arxiv.org/abs/2610.37657v1)**  
  We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens, enabling models to reason over untrusted conten
- **[Attention as Lattice Gauge Theory: Relations Interact Only Through Wilson Loops](https://arxiv.org/abs/2610.37656v1)**  
  Relations compose through the entity they share - Alice is Bob's mother and Bob is Carol's father, so Alice is Carol's grandmother - and the order matters, since a father's mother is not a mother's father; verifying a composed relation means closing the loop. We show that if each entity's coordinate
- **[KPPax: preprocess differentiable kinetic ODE for machine learning in atmospheric chemistry](https://arxiv.org/abs/2610.37655v1)**  
  Atmospheric chemical mechanisms are commonly distributed in the language of the Kinetic PreProcessor (KPP), which generates efficient Fortran or C code but does not fit into the differentiable programming frameworks in which machine-learning models are developed. We present KPPax, a kinetic preproce
- **[Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well](https://arxiv.org/abs/2610.37652v1)**  
  Dexterous manipulation with multi-fingered hands is the next frontier of robotics, yet learned hand skills remain limited to simple grasps or basic repeated motions, such as rotating an object. As robots attempt more demanding in-hand maneuvers, safety, such as not dropping the object, becomes criti
- **[GEPA-Curator: Curated Learning for Self Improving Agents](https://arxiv.org/abs/2610.37651v1)**  
  Large Language Models (LLMs) are increasingly used in multi-turn agentic workloads that require sustained interaction with complex environments. Existing reflective prompt optimizers such as GEPA learn from failed rollouts, but agentic failures can also come from prompt weaknesses, harness limitatio
- **[Can LLMs Uncover Hidden Physical Laws through Free Exploration?](https://arxiv.org/abs/2610.37649v1)**  
  Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier objects falling more slowly, and discover the law through experiments without bei
- **[Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis](https://arxiv.org/abs/2610.37648v1)**  
  We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthAPI pipeline, which e

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[OpenAI and ServiceNow expand partnership across enterprise workflows](https://openai.com/index/openai-servicenow-partnership-expansion)**  
  OpenAI and ServiceNow expand their partnership to bring OpenAI models and agents into ServiceNow and ServiceNow workflows into ChatGPT and Codex.
- **[The future of the firm](https://openai.com/index/the-future-of-the-firm)**  
  How AI might enter the org chart—beneath, beside, and between us.
- **[Legora is building the agentic operating system for legal work](https://openai.com/index/legora)**  
  See how Legora uses OpenAI models, ChatGPT, and Codex to accelerate legal workflows, expand contract analysis, and free lawyers to focus on higher-value work.
- **[Retell uses OpenAI models to help power 100M monthly calls](https://openai.com/index/retell-ai)**  
  GPT-6 Astra tops Retell’s voice agent benchmark, while Codex helps it reach a $1.6M annual revenue run rate per employee.
- **[OpenAI expands partnership with Oracle to bring its apps to ChatGPT](https://openai.com/index/oracle-apps-in-chatgpt)**  
  OpenAI and Oracle are expanding their partnership to bring business applications and AI agents into ChatGPT and power new Oracle offerings.

## Lab Blog: DeepMind
- **[Gemini 4 Carbon: Our next frontier model](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)**  
  
- **[Genie 4: A new generation of world simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)**  
  Genie 4: our new world model unlocking unprecedented realism in real-time simulation.
- **[Beyond tree cover: mapping the world’s forest types](https://deepmind.google/blog/beyond-tree-cover-mapping-the-worlds-forest-types/)**  
  A global map categorizing every 10-meter patch of land on Earth into distinct forest types.
- **[Accelerating the search for antimicrobial peptides with Google Antigravity](https://deepmind.google/blog/accelerating-antimicrobial-discovery/)**  
  Accelerating the search for novel antimicrobial peptides using Google Antigravity for Science.
- **[Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)**  
  Learn how Google DeepMind and GovTech Singapore uses lightweight on-device Gemma models to intercept conversational scams in private chats with zero cloud data egress.

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
  <p>The mission of Thinking Machines is to build AI that extends human will and judgment.</p>
<p>Artificial intelligence can do more every day, but deciding what it should do is up to us: individuals, organizations, humanity as a whole. These decision
- **[Interaction Models: A Scalable Approach to Human-AI Collaboration](https://thinkingmachines.ai/blog/interaction-models/)**  
  <p>Today, we’re announcing a research preview of interaction models: models that handle interaction natively rather than through external scaffolding. We think interactivity should scale alongside intelligence; the way we work with AI should not be t
- **[On-Policy Distillation](https://thinkingmachines.ai/blog/on-policy-distillation/)**  
  <p>LLMs are capable of expert performance in focused domains, a result of several capabilities stacked together: perception of input, knowledge retrieval, plan selection, and reliable execution. This requires a stack of training approaches, which we 
- **[LoRA Without Regret](https://thinkingmachines.ai/blog/lora/)**  
  <p>Today’s leading language models contain upwards of a trillion parameters, pretrained on tens of trillions of tokens. Base model performance keeps improving with scale, as these trillions are necessary for learning and representing all the patterns

## Lab Blog: NVIDIA Blog
- **[Thin, Light and Built for Everything: NVIDIA RTX Spark Windows Laptops Gain New Models, Agent Tools and Games](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-updates-models-agents-games/)**  
  NVIDIA RTX Spark powers thin and light laptops built for everything that developers, creators and gamers do. RTX Spark laptops are now available from ASUS, Dell, HP, Lenovo, Microsoft and MSI. These powerful systems combine an NVIDIA Blackwell RTX GP
- **[How AI Is Changing the Pace of Discovery for Millions Living With Dementia](https://blogs.nvidia.com/blog/open-source-ai-tools-cbrain-dementia/)**  
  There are 57 million people worldwide living with dementia today. For the researchers working to help them, the obstacle isn’t a lack of effort — it’s too much data, too few experts to synthesize it and a pace of discovery that can’t keep up with the
- **[Kazakhstan Expands Compute for Its AI Future](https://blogs.nvidia.com/blog/kazakhstan-ai-compute-ecosystem/)**  
  Kazakhstan’s AI ecosystem is moving from infrastructure plans to deployment.  The shift is visible across the full AI stack — from infrastructure to models to applications. The announcements below — coinciding with a visit to Astana by NVIDIA founder
- **[NVIDIA Unveils Minerva to Bring End-to-End Observability for AI Factories](https://blogs.nvidia.com/blog/minerva-platform-infrastructure/)**  
  Launched today, NVIDIA Minerva is an AIOps platform built to help teams find problems earlier and keep AI factories productive. It brings together telemetry from infrastructure and AI workloads, then applies purpose-built AI models to turn that data 
- **[Cloud Deployment Incoming: ‘Call of Duty: Modern Warfare 4’ Arrives on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-call-of-duty-modern-warfare-4/)**  
  Lock in and load out this GFN Thursday. Call of Duty: Modern Warfare 4 arrives on GeForce NOW at launch, bringing a new campaign, multiplayer action and DMZ, high-stakes extraction mode to supported devices. The campaign also gets an enhanced look: G

## Lab Blog: NVIDIA Technical Blog
- **[Memory-Enforced GPU Sharing in Kubernetes with NVIDIA CUDA 13.4](https://developer.nvidia.com/blog/memory-enforced-gpu-sharing-in-kubernetes-with-nvidia-cuda-13-4/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/CUDAMemoryKV-768x432.webp" style="display: block; margin-bottom: 5px; clear: both;" title="CUDAMemoryKV" width="7
- **[NVIDIA RTX Spark Powers Neural Rendering and AI Characters in Games](https://developer.nvidia.com/blog/nvidia-rtx-spark-powers-neural-rendering-and-ai-characters-in-games/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image6-2-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image6" width="768" />NVIDI
- **[Fine-Tuning NVIDIA Nemotron to Know Local Rules, Not Just Local Languages](https://developer.nvidia.com/blog/fine-tuning-nvidia-nemotron-to-know-local-rules-not-just-local-languages/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/agentic-promo-nemotron-models-eu-gtc-berlin-press-1600x900-5811620-768x432.png" style="display: block; margin-bot
- **[3 Ways to Boost MoE Inference on NVIDIA DGX Spark](https://developer.nvidia.com/blog/3-ways-to-boost-moe-inference-on-nvidia-dgx-spark/)**  
  <img alt="Abstract green computing cube with layered panels, performance icons, and streams of data on a black background" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/dg
- **[How NVIDIA Minerva Turns Telemetry Chaos Into Peak GPU Yield](https://developer.nvidia.com/blog/how-nvidia-minerva-turns-telemetry-chaos-into-peak-gpu-yield/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/MinervaKV-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="MinervaKV" width="768" />A

## GitHub Trending (AI, new repos)
- **[Cinderubasp/InterviewCopilot-rpocket-team](https://github.com/Cinderubasp/InterviewCopilot-rpocket-team)**  
  ★ 53 — EdTech application designed to bridge the gap between learning and landing your dream job
- **[faraflow/faraflow](https://github.com/faraflow/faraflow)**  
  ★ 49 — Visual builder and execution engine for AI powered organizations
- **[OFat34764e/InterviewCopilot-rpocket-team](https://github.com/OFat34764e/InterviewCopilot-rpocket-team)**  
  ★ 32 — EdTech application designed to bridge the gap between learning and landing your dream job
- **[lucidrains/attention-contact-planning](https://github.com/lucidrains/attention-contact-planning)**  
  ★ 10 — Implementation of Attention-based Contact Planning, by Junzhe He of ETH Zürich
- **[xAerux/aerus-ezai](https://github.com/xAerux/aerus-ezai)**  
  ★ 7 — EZ AI — Local AI made easy: Windows command center for local AI apps, model library, and coding agents.
- **[eDurphy/QATNN-HFP](https://github.com/eDurphy/QATNN-HFP)**  
  ★ 3 — Local Neural Network Quantized and Trainable On The Fly on CPU
- **[A220man/axiom-observatory-144-ryan-vo](https://github.com/A220man/axiom-observatory-144-ryan-vo)**  
  ★ 2 — Ryan Vo | Work in progress: axiom-observatory-144-ryan-vo
- **[ALANDVO/sentinel-console-144](https://github.com/ALANDVO/sentinel-console-144)**  
  ★ 2 — Alan Vo | Work in progress: sentinel-console-144
- **[ALANDVO/signal-forge-144-alan-vo](https://github.com/ALANDVO/signal-forge-144-alan-vo)**  
  ★ 2 — Alan Vo | Work in progress: signal-forge-144-alan-vo
- **[A220man/cobalt-lab-144-ryan-vo](https://github.com/A220man/cobalt-lab-144-ryan-vo)**  
  ★ 2 — Ryan Vo | Work in progress: cobalt-lab-144-ryan-vo
