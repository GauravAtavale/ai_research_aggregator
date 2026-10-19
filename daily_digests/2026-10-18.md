# AI Research Digest — 2026-10-18

## HF Daily Papers (Trending)
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 115 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 28 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 153 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation](https://huggingface.co/papers/2610.20571)**  
  ⬆ 343 upvotes — Long-form agentic video generation must turn a screenplay into shots that remain spatially and temporally consistent across nonconsecutive requests. Passing prompts or recent frames between shots does not provide a shared spatial frame for revisiting a scene or a time-indexed record for replaying an
- **[RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://huggingface.co/papers/2610.13912)**  
  ⬆ 49 upvotes — Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predict
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 93 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,
- **[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**  
  ⬆ 77 upvotes — High throughput serving of large language models (LLMs) requires batching
sufficiently many requests at a time. However, existing systems struggle
because the key-value cache (KV cache) memory for each request is huge and
grows and shrinks dynamically. When managed inefficiently, this memory can be

- **[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**  
  ⬆ 116 upvotes — Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person
- **[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**  
  ⬆ 90 upvotes — Software is one of the most powerful tools that we humans have at our
disposal; it allows a skilled programmer to interact with the world in complex
and profound ways. At the same time, thanks to improvements in large language
models (LLMs), there has also been a rapid development in AI agents that

- **[Internal Safety Collapse in Frontier Large Language Models](https://huggingface.co/papers/2603.23509)**  
  ⬆ 31 upvotes — This work identifies a critical failure mode in frontier large language models (LLMs), which we term Internal Safety Collapse (ISC): under certain task conditions, models enter a state in which they continuously generate harmful content while executing otherwise benign tasks. We introduce TVD (Task,

## HF Daily Papers (Today, by Upvotes)
- **[No papers indexed yet for 2026-10-18 (HF submissions can lag up to 14 days behind arXiv)]()**  
  

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation](https://arxiv.org/abs/2610.22372v1)**  
  Personalization is essential for general-purpose robots to transition into household environments and achieve true practicality. While general robotic manipulation has been extensively studied, personalized robotic manipulation (PeRM) lacks a controlled benchmark for separating task completion from 
- **[Discovering state-of-the-art quantum circuits with large language models](https://arxiv.org/abs/2610.22367v1)**  
  Significant efforts are currently being directed toward the implementation of large-scale quantum information processors, but realizing useful quantum advantage also requires the development of efficient quantum algorithms. While for many practical problems the dominant resource costs are associated
- **[T2-z: Test-Time Optimization of Environment Latents for Robotic World Models](https://arxiv.org/abs/2610.22364v1)**  
  Predicting how the world responds to an action requires more than what can be seen: robots must account for environmental factors that are neither directly observable nor explicitly specified, from physical properties such as friction and mass to human-defined environmental rules. We introduce T2-Z 
- **[CoDA: Co-Evolution of Data Engines and Action Policies](https://arxiv.org/abs/2610.22362v1)**  
  Generative simulation can automate robot environment construction, but physically valid environments are not necessarily useful for training. The challenge is to identify environments that address a policy's failures and supervision that helps it overcome them. We introduce CoDA, a framework in whic
- **[PathFM: Fast Generative Forecasting of Multivariate Trajectories](https://arxiv.org/abs/2610.22358v1)**  
  Time series foundation models are becoming increasingly popular for general-purpose forecasting. However, most leading models predict marginal quantiles, leaving the dependence structure of future trajectories unspecified. This distinction matters for trajectory-dependent quantities such as cumulati
- **[OmniVerifier-C1: Decomposed Graded Verifier for Rule-Governed Generative World Modeling](https://arxiv.org/abs/2610.22355v1)**  
  Generative visual verifiers play a crucial role in advancing multimodal intelligence. To enhance the robustness of visual verifiers in complex multimodal scenarios involving compositional requirements, we move beyond conventional binary verifiers that produce only True/False discrete judgments and i
- **[Rethinking Routing Exploration in Modern Mixture-of-Experts](https://arxiv.org/abs/2610.22353v1)**  
  Mixture-of-experts (MoE) models have become an important approach for scaling model parameters. Modern MoE architectures increasingly combine two design choices: fine-grained expert segmentation and shared experts. The former increases expressiveness by enabling more expert combinations at a fixed a
- **[FDE-Gym: The Last Mile of AI Delivery](https://arxiv.org/abs/2610.22350v1)**  
  Existing agent benchmarks typically evaluate agents on well-specified tasks defined by issue reports, specifications, or task tickets. Real-world customer delivery is different: forward-deployed engineers (FDEs) must clarify ambiguous requirements, work in live systems, and uncover unstated constrai
- **[MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering](https://arxiv.org/abs/2610.22344v1)**  
  Large language models (LLMs) are expanding from assisting scientific research and engineering to autonomously developing and improving AI systems, advancing AI for AI (AI4AI) as a pathway toward recursive self-improvement (RSI). Workflow-driven machine learning engineering (MLE) systems provide a pr
- **[GeoState: Learning View-Decoupled Geometry States for 3D World Modeling](https://arxiv.org/abs/2610.22343v1)**  
  Recent 3D world models increasingly use features from geometry foundation models (GFMs) as predictive world states, benefiting from their rich geometric priors. However, the view dependence of these features entangles scene dynamics with camera-induced variation, making the resulting state evolution

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[How Itaú is building generative AI for its entire customer base](https://openai.com/index/itau-generative-ai)**  
  With ia.i, a conversational interface, and the IARA governance platform, Itaú is applying its AI First strategy to customers and employees — in one of Brazil’s most regulated sectors.
- **[Benefit Street Partners answers questions faster with Codex](https://openai.com/index/benefit-street-partners)**  
  Anant Kumar builds tools to compare loan valuations and analyze credit agreements, using Codex for code review and faster follow-ups.
- **[Stack Overflow for Agents triples signups with ChatGPT plugin](https://openai.com/index/stack-overflow-chatgpt-plugin)**  
  Two engineers shipped Stack Overflow for Agents in a few weeks with Codex, and its ChatGPT plugin helped drive up to 10× growth in agent creation.
- **[Bringing GPT-Rosalind to academic research labs](https://openai.com/index/introducing-the-rosalind-academic-plan)**  
  Introducing the Rosalind Academic Plan, offering eligible academic labs sponsored access to GPT-Rosalind and tools to advance life sciences research.
- **[Teaching students to think and learn through questions](https://openai.com/index/teaching-students-to-think-and-learn-through-questions)**  
  Celebrate Teachers’ Day with AI for Educators in Brazilian Portuguese and see how Study Mode can help teachers support active, step-by-step learning.

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
- **[RTX Spark Ignites Global Celebration as New Windows PCs Arrive](https://blogs.nvidia.com/blog/local-ai-rtx-spark-windows-laptops-celebration/)**  
  NVIDIA RTX Spark laptops are now available, bringing NVIDIA Blackwell RTX graphics, up to 128GB of unified memory and the full NVIDIA AI platform to slim, premium Windows PCs.  Starting at $2,399, laptops from ASUS, Dell, HP, Lenovo, Microsoft and MS
- **[Be There for the Beginning: Celebrate the Launch of NVIDIA RTX Spark](https://blogs.nvidia.com/blog/local-ai-rtx-spark-launch-event-invite/)**  
  A new beginning for Windows PCs starts tomorrow with the launch of NVIDIA RTX Spark — one PC built for creators, gamers and AI agents. All are invited to celebrate with NVIDIA and partners at launch events around the world. Share Your Spark Every PC 
- **[Open From Data Center to Desktop: NVIDIA Expands Nemotron Family With Highest Efficiency Super VL and Bolt Models](https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/)**  
  NVIDIA today released Nemotron 3.5 Super VL, an open 120-billion-parameter model that delivers the fastest task completion and highest accuracy for specialized always-on agents. Joining it are two new edge models: Nemotron 3.5 Bolt 74B-A9B 24GB, opti
- **[Dial Up the Cloud: NVIDIA DLSS 4.5 Controls Arrive on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-enshrouded-update/)**  
  Dial in the next gaming session this GFN Thursday. New NVIDIA DLSS 4.5 controls give GeForce NOW members more choice over how supported games look and perform in the cloud, even without the latest hardware. Then, step into the Shroud as Keen Games’ E
- **[NVIDIA Expands Advanced Technology Access for Europe’s Scientific Community Through Open Learning Resources, Collaborations and Compute](https://blogs.nvidia.com/blog/ec-scientific-computing-pledge/)**  
  Much of today’s scientific progress begins with computation.  But turning accelerated computing’s potential into scientific progress — modeling climate systems, designing molecules, simulating materials and more — depends on more than breakthrough te

## Lab Blog: NVIDIA Technical Blog
- **[Code, Test, and Deploy on One Machine with NVIDIA RTX Spark](https://developer.nvidia.com/blog/code-test-and-deploy-on-one-machine-with-nvidia-rtx-spark/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image2-7-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image2" width="768" />AI ag
- **[NVIDIA Nemotron 3.5 Super VL Powers Specialized Agents with Multimodal Reasoning](https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/)**  
  <img alt="Illustration of a central AI model connecting code, charts, credit memo data extraction, and video analysis." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/Nemot
- **[Scale Agentic Coding Workflows with Meta’s Muse Spark Open on NVIDIA GB300 NVL72](https://developer.nvidia.com/blog/scale-agentic-coding-workflows-with-metas-muse-spark-open-on-nvidia-gb300-nvl72/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/open-model-unbox-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="open-model-unbox" w
- **[Optimizing Agent Reliability and Tool Calling Efficiency for Chip Design Using NVIDIA NeMo Gym](https://developer.nvidia.com/blog/optimizing-agent-reliability-and-tool-calling-efficiency-for-chip-design-using-nvidia-nemo-gym/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/agentic-workflow-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="agentic-workflow" w
- **[How to Rewrite Apache Spark UDFs for GPU Acceleration with AI Agents](https://developer.nvidia.com/blog/rewrite-apache-spark-udfs-gpu-acceleration-ai-agents/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image2-5-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image2" width="768" />Enter

## GitHub Trending (AI, new repos)
- **[Fazmin/cve-intel](https://github.com/Fazmin/cve-intel)**  
  ★ 42 — Local security intelligence for CVE triage - 34 tools, 25 sources, risk scores and an MCP server for AI agents, all in native Rust. Private by default.
- **[gautamjajoo/awesome-economics-of-ai](https://github.com/gautamjajoo/awesome-economics-of-ai)**  
  ★ 4 — A curated guide to the costs, markets, adoption, and economic effects of AI.
- **[KarimELMERNISSI/Cohort-Studio](https://github.com/KarimELMERNISSI/Cohort-Studio)**  
  ★ 3 — Clinical cohort data, from raw file to reproducible evidence: data quality, an analysis population with its participant flow, multiple imputation pooled with Rubin's rules, survival models and a Word 
- **[Vrajm12/astraforge](https://github.com/Vrajm12/astraforge)**  
  ★ 3 — Open-source, model-agnostic AI skill toolkit for structured reasoning, reliable coding, research, and verified execution.
- **[47thtechcorner/RayCodes_LFM-2.5-A2B](https://github.com/47thtechcorner/RayCodes_LFM-2.5-A2B)**  
  ★ 2 — Liquid AI's New LFM 2.5 Is INSANE — 184 TOK/S With Only 2B Active! (Live Tests) - High-performance local edge reasoning guide, prompts, and deployment for LFM2.5-24B-A2B hybrid architecture
- **[kzndotsh/companion](https://github.com/kzndotsh/companion)**  
  ★ 2 — An AI companion that tries to be as human-like as we can make it, and the memory engine underneath it.
- **[rafidaaziz23/assay](https://github.com/rafidaaziz23/assay)**  
  ★ 2 — Every AI study tool answers questions. Assay interrogates your answers. Gated Socratic syllabus from a topic or PDF, honeypot probes that catch pasted LLM answers, on-device focus tracking. AI Builder
- **[Faizan-khan144/awesome-free-ai](https://github.com/Faizan-khan144/awesome-free-ai)**  
  ★ 2 — A curated list of free & open-source AI tools, models, APIs and learning resources for developers.
- **[lord-kirby-kirk69/Athena](https://github.com/lord-kirby-kirk69/Athena)**  
  ★ 2 — A lightweight desktop AI assistant built with Tauri, React, and Rust, designed to support multiple AI models through a simple, customizable interface.
- **[Yvngval/ASADI-Assistant](https://github.com/Yvngval/ASADI-Assistant)**  
  ★ 2 — Intelligent educational assistant built with Python and NLP for document-based learning and academic support.
