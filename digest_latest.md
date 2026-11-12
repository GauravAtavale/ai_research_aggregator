# AI Research Digest — 2026-11-11

## HF Daily Papers (Trending)
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 164 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 29 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**  
  ⬆ 22 upvotes — Weight-activation quantization can reduce the memory and compute cost of neural-network inference, but recent methods often require expensive optimization and architecture-specific propagation of basis transforms across layers. We introduce MACaQ, an MXFP4 W4A4 post-training quantization method that
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 15 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**  
  ⬆ 186 upvotes — This report presents VibeVoice, a novel model designed to synthesize
long-form speech with multiple speakers by employing next-token diffusion,
which is a unified method for modeling continuous data by autoregressively
generating latent vectors via diffusion. To enable this, we introduce a novel
con
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 65 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**  
  ⬆ 99 upvotes — Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering ir
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 68 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**  
  ⬆ 8 upvotes — Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning ma
- **[Flide: Accelerating Decision Inference with Exact State Forking](https://huggingface.co/papers/2610.42148)**  
  ⬆ 35 upvotes — Decision models such as Jev have emerged as a highly promising paradigm for LLM agent systems, providing lightweight and reliable categorical reasoning for rapid System One execution. However, existing generation-oriented inference engines fail to support these workloads effectively, suffering from 

## HF Daily Papers (Today, by Upvotes)
- **[Tree-Ising: Repairing Language Models with Bit-Level Ising Edits](https://huggingface.co/papers/2611.14210)**  
  ⬆ 77 upvotes — Weight-space programming, introduced in recent MIT work by Takehi et al., enables a frontier LLM agent to read a network's weights and write a repair. Their GPT-6 Astra agent corrected the reasoning loops of Qwen3.5-0.8B without gradients, using 158 agent turns, 89.7 million tokens, and 50 forward-p
- **[Few-Step Streaming Video Generation via Condition Shifting](https://huggingface.co/papers/2611.14033)**  
  ⬆ 68 upvotes — Few-step sampling reduces the cost of streaming video generation. Distribution Matching Distillation (DMD) supervises few-step generators with a separate fake-score network, which adds training memory and computation and must track the evolving generator. We extend APEX to streaming video by using c
- **[World In-Context Learning for Agentic Robot Manipulation](https://huggingface.co/papers/2611.12885)**  
  ⬆ 65 upvotes — Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the wor
- **[Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents](https://huggingface.co/papers/2611.14320)**  
  ⬆ 53 upvotes — External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it follows a lesson that 
- **[dNaViT: Discrete Codes are General-Purpose Visual Representations](https://huggingface.co/papers/2611.12426)**  
  ⬆ 33 upvotes — Discrete autoregressive modeling, notably through next-token prediction, has become a cornerstone of modern language models. Extending this paradigm to vision allows visual and language models to converge on a unified framework, thereby fostering shared methodology and infrastructure. This work inve
- **[MMDM: Measuring Massive Multitask Decision Making](https://huggingface.co/papers/2611.14309)**  
  ⬆ 26 upvotes — System-1 Decision Models directly make structured probabilistic decisions over query-specified options given a state in a single forward pass, without autoregressively generating reasoning trajectories or textual responses. Recent evaluations cover diverse tasks but often rely on existing benchmarks
- **[DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight](https://huggingface.co/papers/2611.11166)**  
  ⬆ 24 upvotes — Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand. Existing world-action models often acquire such predictive knowledge through explicit future prediction. We introduce DexForesight, a framework that learns spatial foresight implicitly by injec
- **[Embodied First Exam](https://huggingface.co/papers/2611.12177)**  
  ⬆ 23 upvotes — Early successes on agentic robotics point to a potential paradigm shift toward using coding agents to control robots. Existing robotics benchmarks are built around visuomotor policy learning, leaving it open whether coding agents can reliably control diverse robots under physical-world constraints. 
- **[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**  
  ⬆ 22 upvotes — Weight-activation quantization can reduce the memory and compute cost of neural-network inference, but recent methods often require expensive optimization and architecture-specific propagation of basis transforms across layers. We introduce MACaQ, an MXFP4 W4A4 post-training quantization method that
- **[FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance](https://huggingface.co/papers/2611.07464)**  
  ⬆ 22 upvotes — Language agents increasingly work for users on the open Web, and finance is where trusting them is hardest. The data must come from the Web, the strategy lives in the user's head, and correctness depends on time, so an agent can fail silently: a strategy the user never asked for, unverified data, or

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training](https://arxiv.org/abs/2611.14519v1)**  
  Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whos
- **[Toward Foundation Detection Models via Example-Based Grounding in EM-DETR](https://arxiv.org/abs/2611.14518v1)**  
  DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and th
- **[TorchCurves: Differentiable Parametric Curves](https://arxiv.org/abs/2611.14516v1)**  
  We present TorchCurves, a PyTorch library that treats vector-valued parametric curves as learnable primitives. Its central operation maps batches of scalar inputs to points on curves represented in B-spline or Legendre polynomial bases, with differentiation through both inputs and coefficients. Curv
- **[AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models](https://arxiv.org/abs/2611.14515v1)**  
  Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way
- **[Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations](https://arxiv.org/abs/2611.14514v1)**  
  LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternati
- **[Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents](https://arxiv.org/abs/2611.14511v1)**  
  Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,500 pose pairs across 
- **[When Does the Real Wiring Win? Testing connectome structure-function claims against unmeasured physiology](https://arxiv.org/abs/2611.14508v1)**  
  Connectome-constrained models are often used to argue that a measured wiring diagram outperforms shuffled or rewired wiring, and hence that structure shapes function. Such comparisons can confound wiring with how the models are tuned: a connectome fixes who connects to whom, not the excitability, ga
- **[Continual-ARC: Measuring Skill Acquisition over a Working Lifetime](https://arxiv.org/abs/2611.14505v1)**  
  Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on a single applied domain, serve each instance only once, and assume a single family of learner, so m
- **[Emergent Biological Capabilities in a Foundation Model for Molecular Interactions](https://arxiv.org/abs/2611.14504v1)**  
  Foundation models trained on large unlabeled corpora develop emergent capabilities, tasks that go beyond the training objective. We extend this paradigm to multimodal biology with Bonbon, a foundation model for molecular interactions trained on approximately 3.2 trillion tokens of paired protein-lig
- **[Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents](https://arxiv.org/abs/2611.14493v1)**  
  Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based 

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Gilbert + Tobin rethinks the business of law with AI](https://openai.com/index/gilbert-tobin-sam-nickless)**  
  A conversation with Sam Nickless, Partner and Chief Executive Officer at Gilbert + Tobin.
- **[ChatGPT Plus for veterans and servicemembers](https://openai.com/index/chatgpt-plus-for-veterans)**  
  More than 20,000 veterans and transitioning service members have claimed a free year of ChatGPT Plus. See how they use it to prepare for civilian careers.
- **[JioStar’s chief architect on AI discovery at 500M-user scale](https://openai.com/index/jiostar-vijay-seshadri)**  
  JioStar’s Vijay Seshadri explains AI discovery at 500M-user scale. Read his lessons on evals, guardrails, and taking AI into production.
- **[Helping caregivers use AI in everyday life](https://openai.com/index/helping-caregivers-use-ai-in-everyday-life)**  
  OpenAI Academy is bringing free, hands-on ChatGPT workshops to caregivers in five U.S. cities, helping them build practical AI skills for everyday life.
- **[Introducing Businesses in ChatGPT](https://openai.com/index/introducing-businesses-chatgpt)**  
  Manage your business information, get insights about how your business shows up, and turn interest into action in ChatGPT.

## Lab Blog: DeepMind
- **[AlphaGenome 2: Deciphering how cells read DNA to better understand disease](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)**  
  Predicting how DNA sequences and their variations impact specific human cell types and disease.
- **[Gemini 4 Carbon is now available](https://deepmind.google/blog/gemini-4-carbon-is-now-available/)**  
  
- **[Introducing AlphaProof Code: a breakthrough in verifying complex software at depth](https://deepmind.google/blog/introducing-alphaproof-code/)**  
  AlphaProof Code agents wrote three  million lines of proofs in Lean to verify Signal’s core encryption.
- **[Gemini Robotics 2.5 accelerates real-world general dexterity](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)**  
  Our most capable vision-language-action model enhances robot dexterity, reliability, and safety
- **[Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips](https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/)**  
  

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
- **[How AI Helps Recyclers Turn Mixed Waste Into Reusable Material](https://blogs.nvidia.com/blog/ai-recycling-startups/)**  
  Vision AI and robotics pick what’s worth recovering out of conveyor belts of used clothing, bottles and mixed recyclables, diverting thousands of tons of materials from landfills.
- **[NVIDIA Expands Open Source Commitment With OpenShell Donation and New AI Infrastructure](https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/)**  
  Kubernetes, the open source system that manages how applications run across thousands of AI factories, has become the foundation for AI, and the demands on it are only growing. To help meet them, NVIDIA is deepening its commitment to open source at K
- **[Practice Makes Precise: At CoRL, NVIDIA and Partners Reveal How Robots Rehearse Delicate Work in Simulation](https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/)**  
  Simulation, which has long been the proving ground for robots learning to walk, roll and hop, is now helping researchers teach robots tasks that require a finer touch: aligning gears, connecting cables and assembling small components.  The shift from
- **[NVIDIA Announces New Planned Investments in Korean Startups at the MSIT-NVIDIA AI Startup Partnership Forum](https://blogs.nvidia.com/blog/korean-startup-investments-msit/)**  
  Korea’s Ministry of Science and ICT and NVIDIA hosted the MSIT-NVIDIA AI Startup Partnership Forum at COEX. Representatives from the Ministry of Science and ICT and NVIDIA met with over 20 Korean startups across foundation models, physical AI, AI inf
- **[Korea Advances Physical AI Across Industries With NVIDIA](https://blogs.nvidia.com/blog/korea-physical-ai-ecosystem/)**  
  Tapping into the country’s strengths in manufacturing and engineering, NVIDIA is helping advance Korea’s physical AI ecosystem. The country’s industry leaders are applying accelerated computing, AI and simulation to everything from semiconductor manu

## Lab Blog: NVIDIA Technical Blog
- **[Validating GPU Platforms with Runtime AI Inventory via the NVIDIA DSX AI Factory](https://developer.nvidia.com/blog/validating-gpu-platforms-with-runtime-ai-inventory-via-the-nvidia-dsx-ai-factory/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image1-7-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="Best Models Trained on NVID
- **[Running AV Reasoning Models Within Onboard Compute and Latency Limits](https://developer.nvidia.com/blog/running-av-reasoning-models-within-onboard-compute-and-latency-limits/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="338" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/auto-alpamayo-2-edge-tech-blog-promo-600x338_r2-1.gif" style="display: block; margin-bottom: 5px; clear: both;" t
- **[Agent Substrate: Advancing Kubernetes for Agents at Scale](https://developer.nvidia.com/blog/agent-substrate-advancing-kubernetes-for-agents-at-scale/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image2-5-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="image2" width="768" />AI ag
- **[Start and Restore GPU Workloads in Seconds with NVIDIA Snapshot](https://developer.nvidia.com/blog/start-and-restore-gpu-workloads-in-seconds-with-nvidia-snapshot/)**  
  <img alt="Green cube with a neural-network diagram, surrounded by circular arrows beneath descending data blocks on a purple background." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/upl
- **[Manage Kubernetes Clusters for GPU Infrastructure with NVIDIA Kubernetes Engine](https://developer.nvidia.com/blog/manage-kubernetes-clusters-for-gpu-infrastructure-with-nvidia-kubernetes-engine/)**  
  <img alt="An illustration of a layered computing stack shows connected AI models above a Kubernetes layer and a processor." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/n

## GitHub Trending (AI, new repos)
- **[kokoc30/Auto-Stitch](https://github.com/kokoc30/Auto-Stitch)**  
  ★ 49 — AI-powered video editing platform for transforming long-form content into short, engaging videos. Public product showcase.
- **[rohitjee7022-blip/Anonymous-Campus](https://github.com/rohitjee7022-blip/Anonymous-Campus)**  
  ★ 37 — Anonymous Campus protects student identities while enabling honest campus facility feedback. It uses aggregated ratings and issue tracking to help administrators improve facilities, with BharatCode AI
- **[ctianye/CodeSlice](https://github.com/ctianye/CodeSlice)**  
  ★ 18 — Local-first AI code-reading desktop app with navigable source citations and human-approved actions.
- **[byte-od/mixture-of-scars](https://github.com/byte-od/mixture-of-scars)**  
  ★ 8 — Breaking the barrier between LLMs and hardware. Mixture of Scars (MoS) static weight compression & SCache O(1) constant KV-cache replacement.
- **[dharunram-lgtm/Echo_Knowledge](https://github.com/dharunram-lgtm/Echo_Knowledge)**  
  ★ 4 — ECHO Knowledge is a local-first AI-powered knowledge management system for organizing documents, semantic search, grounded AI answers, and interactive knowledge graphs. Built with Tauri, Rust, React, 
- **[joedejesus/JJ_ML_DL_BOOK](https://github.com/joedejesus/JJ_ML_DL_BOOK)**  
  ★ 4 — Recurso educativo en español sobre Data Science, Machine Learning, Deep Learning, NLP y Transformers con Python, PyTorch y Jupyter.
- **[ALANDVO/axiom-station-144](https://github.com/ALANDVO/axiom-station-144)**  
  ★ 2 — Alan Vo | Work in progress: axiom-station-144
- **[Pentexa/metargon](https://github.com/Pentexa/metargon)**  
  ★ 2 — METARGON — A crow-inspired AI research project exploring adaptive learning, memory, reasoning, and autonomous discovery.
- **[webDMX/followspot-AI](https://github.com/webDMX/followspot-AI)**  
  ★ 2 — Tool for using moving lights as followspots based on video camera image.
- **[A220man/tensor-pilot-145](https://github.com/A220man/tensor-pilot-145)**  
  ★ 2 — Ryan Vo | Work in progress: tensor-pilot-145
