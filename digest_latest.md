# AI Research Digest — 2026-11-12

## HF Daily Papers (Trending)
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 164 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 30 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 16 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**  
  ⬆ 30 upvotes — Weight-activation quantization can reduce the memory and compute cost of neural-network inference, but recent methods often require expensive optimization and architecture-specific propagation of basis transforms across layers. We introduce MACaQ, an MXFP4 W4A4 post-training quantization method that
- **[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**  
  ⬆ 102 upvotes — Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering ir
- **[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**  
  ⬆ 186 upvotes — This report presents VibeVoice, a novel model designed to synthesize
long-form speech with multiple speakers by employing next-token diffusion,
which is a unified method for modeling continuous data by autoregressively
generating latent vectors via diffusion. To enable this, we introduce a novel
con
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 68 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 65 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**  
  ⬆ 11 upvotes — Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning ma
- **[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**  
  ⬆ 86 upvotes — Software is one of the most powerful tools that we humans have at our
disposal; it allows a skilled programmer to interact with the world in complex
and profound ways. At the same time, thanks to improvements in large language
models (LLMs), there has also been a rapid development in AI agents that


## HF Daily Papers (Today, by Upvotes)
- **[Scaling Mathematical Proof Supervision from Structured Textbooks](https://huggingface.co/papers/2610.40394)**  
  ⬆ 41 upvotes — Mathematical supervision for language models is typically flattened into isolated problem-solution pairs, discarding the curricular organization and evidential structure of the original sources. We introduce TOME-Math (Textbook-Oriented Mathematical Evidence), a large-scale corpus that converts 2,11
- **[SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering](https://huggingface.co/papers/2611.13410)**  
  ⬆ 32 upvotes — Low-bit quantization reduces the inference cost of LLM agents but can compromise task success. Examining failed rollouts, we find that quantized agents overlook task requirements or environmental conditions, producing environment transitions that diverge from successful full-precision references. Co
- **[Incentivizing Self-Learning in Large Language Models via Reinforcement Learning](https://huggingface.co/papers/2610.39671)**  
  ⬆ 28 upvotes — Large language models (LLMs) draw on parametric knowledge and retrieval-augmented generation (RAG) to solve knowledge-intensive tasks. Yet problem solving in unfamiliar domains calls for tightly coupled knowledge acquisition and reasoning, beyond factual retrieval and aggregation or learning solely 
- **[Read Less, Solve More: Token-Efficient Sparse Reading of External Content for AI Agents](https://huggingface.co/papers/2608.22237)**  
  ⬆ 19 upvotes — Web-facing AI agents repeatedly access webpages, documents, repositories, and tool responses, yet reading interfaces often expose entire objects when only sparse evidence is needed. This over-reading increases token and latency costs and can dilute relevant evidence. We present SparseRead, a reusabl
- **[Ensemble Routing for Prompt-Adaptive Cost-Aware LLM Inference](https://huggingface.co/papers/2611.10193)**  
  ⬆ 14 upvotes — Large language models (LLMs) increasingly support Web-based services that must balance response quality and inference cost across heterogeneous requests. Conventional routing selects one model per prompt, while fixed ensembles cannot adapt their composition and cost to individual requests. We introd
- **[Interactive Visual Gym: Evaluating Visual Interaction Models with Simulated Users in Interactive Worlds](https://huggingface.co/papers/2611.08286)**  
  ⬆ 13 upvotes — Visual interaction models that support users during ongoing physical tasks require evaluation in closed loop, where assistant responses can change subsequent user behavior and task outcomes. Existing benchmarks largely rely on offline replay and therefore cannot capture these effects. We introduce I
- **[GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning](https://huggingface.co/papers/2611.13028)**  
  ⬆ 12 upvotes — AAA games offer a rich testbed for evaluating agent perception, reasoning, and control. However, evaluating whether agents can complete tasks in AAA games is challenging and often human-annotated because task outcomes are often difficult to verify automatically, let alone applying it for Reinforceme
- **[Evolving Infra: Agent-Adaptive LLM Serving at Scale](https://huggingface.co/papers/2611.12304)**  
  ⬆ 10 upvotes — Agentic workloads are a major source of LLM inference demand. Existing prefill--decode (PD) disaggregated serving systems offer limited flexibility for runtime adaptation of compute allocation and KV cache management, and rely on coarse signals that only partly capture the diverse and dynamic agent 
- **[Where Does Alignment Emerge and What Does It Mean? A Closer Look at the Platonic Representation Hypothesis](https://huggingface.co/papers/2611.12869)**  
  ⬆ 7 upvotes — The Platonic Representation Hypothesis (PRH) suggests that neural networks are converging toward similar representation spaces. As language models become more capable, their representations are aligning with those of vision models. However, recent work has questioned whether this trend continues to 
- **[Subliminal Learning in Vision-Language Models](https://huggingface.co/papers/2611.08538)**  
  ⬆ 4 upvotes — Subliminal learning is a phenomenon in large language models (LLMs) where a teacher passes a hidden preference to a student through training data unrelated to that preference. We study whether subliminal learning also occurs in vision-language models (VLMs). We finetune a teacher VLM to prefer a spe

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Learning a calibrated decision head from logged bandit feedback](https://arxiv.org/abs/2611.15572v1)**  
  A decision head reads a state and a list of options and returns a probability per option in one forward pass. Once deployed, it usually observes only whether the option it chose was right: logged bandit feedback. We adapt such a head, LoRA on Qwen3-0.6B-Base and 1.7B-Base, from that feedback and rep
- **[TraceKV: Policy-Preserving Low-Rank KV Cache Compression for Reasoning Vision-Language Models](https://arxiv.org/abs/2611.15569v1)**  
  Reasoning vision-language models (VLMs) impose substantial KV cache demands from both large multimodal contexts and growing reasoning traces. Low-rank KV compression has emerged as a promising paradigm that stores low-dimensional latents of KV states and can be combined with quantization. However, e
- **[Can We Make an LLM Dumber, or Is It Just Playing Dumb? An Empirical Study of Believable Performance Throttling](https://arxiv.org/abs/2611.15568v1)**  
  A benchmark score is commonly read as a proxy for model capability. We study the inverse problem: can a model be driven to a target score, and do its failures resemble those of a naturally weaker model? We operationalize believable performance reduction along three axes: target calibration, item-dif
- **[Observations Drift, Structures Remain: Structural Pretraining with Time Alignment for Electromagnetic Signals](https://arxiv.org/abs/2611.15566v1)**  
  Electromagnetic signal modeling is increasingly moving toward self-supervised pretraining on heterogeneous I/Q observations. However, an observed waveform is jointly shaped by signal generation, propagation environments, and acquisition processes, which mix reusable structural regularities with obse
- **[What Conformal Selection Can Certify in CRISPR Off-Target Design:Benchmark Leakage, Free Baselines, and a Finite-Sample Cohort Requirement](https://arxiv.org/abs/2611.15555v1)**  
  Conformal selection promises distribution-free, finite-sample control of the error rate of a decision, and has been proposed as a safety layer for machine-learning CRISPR guide design. We ask whether such a certificate is attainable from the validated off-target data that exist. The constraint is ar
- **[Testing Conversation Preservation Across LLM APIs: A Rule-Based Oracle for Detecting Silent Information Loss](https://arxiv.org/abs/2611.15543v1)**  
  LLM applications increasingly rely on translators and compatibility layers to move conversations across APIs. Yet a translated request can be accepted by the target API while silently losing information about instruction roles, tool interactions, error states, or generation controls. We introduce is
- **[Faithful in Steps: Improving Generalization and Citation in RAG via Query Decomposition](https://arxiv.org/abs/2611.15538v1)**  
  Retrieval-augment generation is a prevalent strategy to mitigate hallucinations of LLMs. The attributable RAG (RAGQ) generates quotes for its answers. The quotes indicate which input contexts support the RAG to derive the answers, enhancing the answer's verifiability and trustworthiness. However, ex
- **[Analysis choices decide whether untrained networks beat trained ones at V1: a multiverse analysis of model-brain RSA](https://arxiv.org/abs/2611.15533v1)**  
  Untrained convolutional networks have been reported to rival trained networks as models of visual cortex, and we had reported an untrained-network advantage over backpropagation at V1 in THINGS fMRI, together with a dependence on evaluation resolution. Under a pre-specified ridge readout, the untrai
- **[MAGIC: Modality-Aware Gini Inspection for Clinical Hallucination Detection in LMMs](https://arxiv.org/abs/2611.15530v1)**  
  Recent advances in medical large multimodal models (LMMs) have brought promising progress to clinical decision support, yet hallucination, the generation of confident but clinically unverifiable outputs, poses a critical threat to the reliability demanded in high-stakes medical settings. Existing ha
- **[One Hierarchy, Many Sports: Hierarchy-Aligned Multi-Task Learning for Next-Shot Prediction](https://arxiv.org/abs/2611.15529v1)**  
  Next-shot prediction in racket sports requires learning from event data with different match structures, recorded attributes, and label vocabularies. Table tennis, badminton, and tennis nevertheless share a hierarchy in which shots form rallies and rallies form higher scoring units. We present MT-HT

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[How Amplitude ships product improvements in 1–2 days with OpenAI](https://openai.com/business/customer-stories/amplitude)**  
  Built primarily on OpenAI models, Amplitude’s proactive product agent, Wave, identifies what to build, helps teams ship changes with coding agents, and measures the impact.
- **[Gondola doubles revenue as its team builds more with Codex](https://openai.com/business/customer-stories/gondola)**  
  Gondola helps creatives get credit and get hired, with Codex raising its lead engineer’s output by 50% and ChatGPT simplifying daily work.
- **[Holiday Extras is rethinking what it can build with Codex](https://openai.com/business/customer-stories/holidays-extras-codex)**  
  With Codex, Holiday Extras is turning customer expertise into better apps, higher booking conversion and new possibilities for growth.
- **[Supporting research on AI and children’s safety](https://openai.com/index/children-first-declaration)**  
  OpenAI commits $2 million to research on AI and children’s safety. The work supports shared tools to measure risks and opportunities for young people.
- **[Gilbert + Tobin rethinks the business of law with AI](https://openai.com/index/gilbert-tobin-sam-nickless)**  
  A conversation with Sam Nickless, Partner and Chief Executive Officer at Gilbert + Tobin.

## Lab Blog: DeepMind
- **[Introducing Gemini 4 Hydrogen](https://deepmind.google/blog/introducing-gemini-4-hydrogen/)**  
  
- **[AlphaGenome 2: Deciphering how cells read DNA to better understand disease](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)**  
  Predicting how DNA sequences and their variations impact specific human cell types and disease.
- **[Gemini 4 Carbon is now available](https://deepmind.google/blog/gemini-4-carbon-is-now-available/)**  
  
- **[Introducing AlphaProof Code: a breakthrough in verifying complex software at depth](https://deepmind.google/blog/introducing-alphaproof-code/)**  
  AlphaProof Code agents wrote three  million lines of proofs in Lean to verify Signal’s core encryption.
- **[Gemini Robotics 2.5 accelerates real-world general dexterity](https://deepmind.google/blog/gemini-robotics-2-5-accelerates-real-world-physical-intelligence/)**  
  Our most capable vision-language-action model enhances robot dexterity, reliability, and safety

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
- **[A New Dawn in the Cloud: ‘Warhammer 40,000: Dawn of War IV’ Is Coming to GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-warhammer-dawn-of-war-iv-coming/)**  
  Rally the ranks this GFN Thursday. Warhammer 40,000: Dawn of War IV is coming to GeForce NOW, allowing players to experience the battle for Kronus through cloud gaming. There’s more on the horizon, with NVIDIA DLSS 5 technology coming to War Thunder 
- **[How AI Helps Recyclers Turn Mixed Waste Into Reusable Material](https://blogs.nvidia.com/blog/ai-recycling-startups/)**  
  Vision AI and robotics pick what’s worth recovering out of conveyor belts of used clothing, bottles and mixed recyclables, diverting thousands of tons of materials from landfills.
- **[NVIDIA Expands Open Source Commitment With OpenShell Contribution and New AI Infrastructure](https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/)**  
  Kubernetes, the open source system that manages how applications run across thousands of AI factories, has become the foundation for AI, and the demands on it are only growing. To help meet them, NVIDIA is deepening its commitment to open source at K
- **[Practice Makes Precise: At CoRL, NVIDIA and Partners Reveal How Robots Rehearse Delicate Work in Simulation](https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/)**  
  Simulation, which has long been the proving ground for robots learning to walk, roll and hop, is now helping researchers teach robots tasks that require a finer touch: aligning gears, connecting cables and assembling small components.  The shift from
- **[NVIDIA Announces New Planned Investments in Korean Startups at the MSIT-NVIDIA AI Startup Partnership Forum](https://blogs.nvidia.com/blog/korean-startup-investments-msit/)**  
  Korea’s Ministry of Science and ICT and NVIDIA hosted the MSIT-NVIDIA AI Startup Partnership Forum at COEX. Representatives from the Ministry of Science and ICT and NVIDIA met with over 20 Korean startups across foundation models, physical AI, AI inf

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
  ★ 20 — Local-first AI code-reading desktop app with navigable source citations and human-approved actions.
- **[byte-od/mixture-of-scars](https://github.com/byte-od/mixture-of-scars)**  
  ★ 8 — Breaking the barrier between LLMs and hardware. Mixture of Scars (MoS) static weight compression & SCache O(1) constant KV-cache replacement.
- **[joedejesus/JJ_ML_DL_BOOK](https://github.com/joedejesus/JJ_ML_DL_BOOK)**  
  ★ 6 — Recurso educativo en español sobre Data Science, Machine Learning, Deep Learning, NLP y Transformers con Python, PyTorch y Jupyter.
- **[dharunram-lgtm/Echo_Knowledge](https://github.com/dharunram-lgtm/Echo_Knowledge)**  
  ★ 4 — ECHO Knowledge is a local-first AI-powered knowledge management system for organizing documents, semantic search, grounded AI answers, and interactive knowledge graphs. Built with Tauri, Rust, React, 
- **[pathbit/AgentDevKit](https://github.com/pathbit/AgentDevKit)**  
  ★ 3 — Repositório com as skills, comandos e outros que agentes de código irão utilizar.
- **[ALANDVO/axiom-station-144](https://github.com/ALANDVO/axiom-station-144)**  
  ★ 2 — Alan Vo | Work in progress: axiom-station-144
- **[phillarmonic/mcpdev](https://github.com/phillarmonic/mcpdev)**  
  ★ 2 — A dummy harness for debugging/CI testing MCPs
- **[webDMX/followspot-AI](https://github.com/webDMX/followspot-AI)**  
  ★ 2 — Tool for using moving lights as followspots based on video camera image.
