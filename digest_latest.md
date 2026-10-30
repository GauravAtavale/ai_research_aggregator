# AI Research Digest — 2026-10-29

## HF Daily Papers (Trending)
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 158 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 125 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 31 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 105 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,
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
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 6 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 62 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**  
  ⬆ 107 upvotes — Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system t
- **[Hy-Nomas: Towards Free-form Interactive World Generation](https://huggingface.co/papers/2610.36729)**  
  ⬆ 126 upvotes — Interactive world generation requires models to follow successive commands while preserving relevant history and action consequences. We present Hy-Nomas, a video world model with an 8B diffusion backbone that supports free-form text instructions and continuous camera control across multiple interac

## HF Daily Papers (Today, by Upvotes)
- **[Efficient Streaming Audio-Visual Target Speaker Extraction for Real-World Acoustic Scenes](https://huggingface.co/papers/2610.32749)**  
  ⬆ 150 upvotes — Streaming audio-visual target speaker extraction (AVTSE) is essential for latency-sensitive applications. However, current causal systems face two coupled gaps. First, standard benchmarks fix the number of speakers at two and ignore the near-/far-field interference, reverberation, and sudden noise o
- **[OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images](https://huggingface.co/papers/2610.35684)**  
  ⬆ 47 upvotes — Generating videos of a specific subject from a few reference images remains challenging when the camera reveals surfaces that are not visible in the input. Early subject-to-video (S2V) methods condition on a single reference image and must therefore infer the subject's unseen appearance and geometry
- **[Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success](https://huggingface.co/papers/2610.31670)**  
  ⬆ 21 upvotes — Robot foundation models are typically evaluated through costly closed-loop rollouts, motivating low-cost offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, modalities such as vision and language converge toward a shared statis
- **[TAO: Tool-Aware Joint Scheduling for LLM-Based Agentic Serving](https://huggingface.co/papers/2610.37230)**  
  ⬆ 18 upvotes — Agentic services alternate between model inference on clustered GPUs and external tools on distributed CPUs. In this scenario, existing systems (1) overlook tool-return readiness in service evaluation, wasting limited resources, and (2) use heuristic strategies to decide admission and placement on G
- **[RealCLI: Toward a Unified Evaluation of Human-Agent Collaboration for CLI Agents](https://huggingface.co/papers/2610.22507)**  
  ⬆ 17 upvotes — Command-line interface (CLI) agents increasingly execute longer-horizon tasks, yet existing benchmarks either assume that user instructions remain fixed throughout execution or evaluate task outcomes without capturing runtime collaboration quality. In this paper, we present REALCLI, a paired benchma
- **[PersonaCUABench: Benchmarking Computer-Use Agents Serving Diverse Personas](https://huggingface.co/papers/2610.22990)**  
  ⬆ 13 upvotes — Computer-use agents (CUAs) are commonly evaluated against fixed task specifications, but users may omit requirements, add constraints, or require approval before consequential actions. Completing the benchmark instruction does not guarantee serving the person who asked. We introduce PersonaCUABench,
- **[TauIndianBankBench: Procedure-Aware, Action-Oriented Evaluation of Tool-Using Conversational Agents](https://huggingface.co/papers/2610.30161)**  
  ⬆ 9 upvotes — Many Indian banks serve customers through FAQ pages and scripted chatbots. Assistants based on language models could respond faster and carry out requests such as blocking a card, but only if they give correct information and follow the bank's rules. These rules prescribe a procedure, a set of requi
- **[Amortizing Sequential Experimental Design in Reasoning LLMs](https://huggingface.co/papers/2610.20832)**  
  ⬆ 6 upvotes — Despite their extensive pretraining knowledge and strong reasoning capabilities, large language models (LLMs) struggle to adaptively gather information in experimental design tasks. We study how to amortize sequential Bayesian experimental design (BED) into an LLM by explicitly training the reasonin
- **[LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data](https://huggingface.co/papers/2610.30132)**  
  ⬆ 5 upvotes — Reinforcement learning (RL) is an effective way to strengthen the long-context reasoning of large language models (LLMs), but it needs training data that are long, diverse, challenging, and verifiable. Human annotation of such data is expensive, naturally occurring data are too scarce to sustain RL,
- **[CausGround: Causal Interaction Grounding for Adaptive Embodied Planning](https://huggingface.co/papers/2610.29702)**  
  ⬆ 4 upvotes — Multimodal large language models (MLLMs) show promising reasoning capabilities, but reliable physical interaction requires planning that accounts for when actions are executable and how they change the world. These preconditions and effects are environment-dependent and often not captured by MLLMs, 

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Autonomous Quantum Measurement with Agentic AI](https://arxiv.org/abs/2610.38850v1)**  
  Quantum materials exhibit diverse electronic and functional phenomena, but their characterization requires extensive experimental expertise, iterative decision-making and accumulated laboratory knowledge that is difficult to document and transfer. Here we introduce Quantum Agent (QUANTA), an agentic
- **[Discovery of Diverse and Realistic Financial Tail-Risk Using Generative Flow Networks](https://arxiv.org/abs/2610.38838v1)**  
  Accurate modeling of rare, high-impact financial events is essential for robust risk management. Sampling-based techniques such as Sequential Markov Chain Monte Carlo (SMCMC) generate diverse scenarios but inefficiently explore high-risk regions, while Deep Reinforcement Learning (DRL) converges on 
- **[What to randomize matters: a controlled study of volume, axis and representation in low-data molecular generation](https://arxiv.org/abs/2610.38835v1)**  
  Chemical language models can struggle to generate new molecules when trained on small datasets, where a model may reproduce training examples rather than learn a useful generative distribution. Randomized SMILES augmentation varies atom traversal, whereas Sequential Attachment-based Fragment Embeddi
- **[Discovering Jailbreaks via Curriculum of Models](https://arxiv.org/abs/2610.38833v1)**  
  Automated jailbreak discovery aims to find prompts that elicit prohibited behaviors from safety-trained language models, helping developers identify vulnerabilities before deployment. One class of approaches uses reinforcement learning to train an investigator model to generate prompts that elicit a
- **[Evaluating Visual Realism of AI-Generated Videos with Eye Tracking](https://arxiv.org/abs/2610.38825v1)**  
  Human evaluation of AI-generated videos has so far relied on explicit human feedback, such as judgments or ratings. While these signals capture the conclusions viewers reach, they fail to offer insights into the perception that leads to them. This paper investigates eye tracking as a complementary h
- **[CopyLoop: Fast Looped Transformer Decoding via Context Copying and Shallow Screening](https://arxiv.org/abs/2610.38822v1)**  
  Looped Transformers increase computational capacity through the repeated application of shared blocks, but their recurrent depth makes conventional full-depth decoding expensive. While existing speculative pipelines accelerate generation by processing consecutive token positions at varying depths, t
- **[UnEZ: A Fully Unsupervised Self-Templating Neural Network for Redshift and Line Strength Estimation](https://arxiv.org/abs/2610.38816v1)**  
  As spectroscopic surveys grow, estimating galaxy properties such as metallicity, star formation rate, and redshift becomes computationally cumbersome. Methods of estimating such properties rely on template spectra or curated redshift catalogs, which fail to represent the diversity of objects seen in
- **[Causal Attention on CPU: A Cache-Aware and Load-Balanced Scheduling Kernel for Prefill](https://arxiv.org/abs/2610.38809v1)**  
  Agentic AI drives significant productivity gains across diverse domains, but concurrent long-context prefills from multiple agents can saturate GPU compute resources. Although CPUs offer a viable alternative, existing CPU attention kernels fall short in adapting to multi-tier cache hierarchies and l
- **[Pinpointing Pivot Points: The DECIDE Framework for Data Analysis Decision Importances](https://arxiv.org/abs/2610.38797v1)**  
  Human judgment calls made throughout the data science life cycle can change the conclusions drawn from data. Independent analysts often make different choices when given the same data, leading to often unacceptable variations in results and contributing to the ongoing reproducibility crisis across s
- **[Routed Continual Learning](https://arxiv.org/abs/2610.38796v1)**  
  Agents deployed at scale repeatedly encounter related problems, and it is natural to let them learn from each other's experience rather than starting over each time. Unfortunately, there is no single way to retain that experience that works well across settings, and no way to know in advance which f

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[An updated Model Spec for more capable and beneficial AI](https://openai.com/index/updated-model-spec)**  
  OpenAI’s updated Model Spec outlines five core values to guide more capable AI toward sound judgment, human agency, and faithfulness to human intent.
- **[How we detect frontier model misalignment](https://openai.com/index/how-we-detect-frontier-model-misalignment)**  
  OpenAI uses layered monitoring to detect frontier model misalignment and unauthorized agent behavior so responders can intervene before incidents escalate.
- **[How Ropes & Gray is developing AI for transactional diligence](https://openai.com/index/ropes-gray-ai-diligence)**  
  Ropes & Gray is developing AI for transactional diligence with OpenAI. Lawyers review grouped documents, summaries, and reports before advising clients.
- **[OpenAI and ServiceNow expand partnership across enterprise workflows](https://openai.com/index/openai-servicenow-partnership-expansion)**  
  OpenAI and ServiceNow expand their partnership to bring OpenAI models and agents into ServiceNow and ServiceNow workflows into ChatGPT and Codex.
- **[The future of the firm](https://openai.com/index/the-future-of-the-firm)**  
  How AI might enter the org chart—beneath, beside, and between us.

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
- **[Into the Omniverse: How Developers Turn Ideas Into Simulations With Frontier AI Agents](https://blogs.nvidia.com/blog/developers-simulation-frontier-ai-agents/)**  
  Turning a simulation idea into a working application means assembling assets, connecting physics and rendering, and checking that the scene behaves as intended. Developers are combining frontier AI models with NVIDIA Omniverse libraries to help carry
- **[Slice Into GFN Thursday: ‘Phantom Blade Zero’ Launches on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-phantom-blade-zero/)**  
  This Halloween week, GFN Thursday is delivering a fresh batch of gaming treats. Something wicked this blade comes. S-GAME’s Phantom Blade Zero launches on GeForce NOW today, bringing a scarily good blend of martial arts and punk fantasy to the cloud.
- **[Thin, Light and Built for Everything: NVIDIA RTX Spark Windows Laptops Gain New Models, Agent Tools and Games](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-updates-models-agents-games/)**  
  NVIDIA RTX Spark powers thin and light laptops built for everything that developers, creators and gamers do. RTX Spark laptops are now available from ASUS, Dell, HP, Lenovo, Microsoft and MSI. These powerful systems combine an NVIDIA Blackwell RTX GP
- **[How AI Is Changing the Pace of Discovery for Millions Living With Dementia](https://blogs.nvidia.com/blog/open-source-ai-tools-cbrain-dementia/)**  
  There are 57 million people worldwide living with dementia today. For the researchers working to help them, the obstacle isn’t a lack of effort — it’s too much data, too few experts to synthesize it and a pace of discovery that can’t keep up with the
- **[Kazakhstan Expands Compute for Its AI Future](https://blogs.nvidia.com/blog/kazakhstan-ai-compute-ecosystem/)**  
  Kazakhstan’s AI ecosystem is moving from infrastructure plans to deployment.  The shift is visible across the full AI stack — from infrastructure to models to applications. The announcements below — coinciding with a visit to Astana by NVIDIA founder

## Lab Blog: NVIDIA Technical Blog
- **[Unlocking Tensor Core Performance for Machine Learning Interatomic Potentials](https://developer.nvidia.com/blog/unlocking-tensor-core-performance-for-machine-learning-interatomic-potentials/)**  
  <img alt="Colorful matrix-like blocks transition into a lattice of spheres, illustrating computation for atomistic simulation." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/
- **[Memory-Enforced GPU Sharing in Kubernetes with NVIDIA CUDA 13.4](https://developer.nvidia.com/blog/memory-enforced-gpu-sharing-in-kubernetes-with-nvidia-cuda-13-4/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/CUDAMemoryKV-768x432.webp" style="display: block; margin-bottom: 5px; clear: both;" title="CUDAMemoryKV" width="7
- **[NVIDIA RTX Spark Powers Neural Rendering and AI Characters in Games](https://developer.nvidia.com/blog/nvidia-rtx-spark-powers-neural-rendering-and-ai-characters-in-games/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image6-2-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image6" width="768" />NVIDI
- **[Fine-Tuning NVIDIA Nemotron to Know Local Rules, Not Just Local Languages](https://developer.nvidia.com/blog/fine-tuning-nvidia-nemotron-to-know-local-rules-not-just-local-languages/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/agentic-promo-nemotron-models-eu-gtc-berlin-press-1600x900-5811620-768x432.png" style="display: block; margin-bot
- **[3 Ways to Boost MoE Inference on NVIDIA DGX Spark](https://developer.nvidia.com/blog/3-ways-to-boost-moe-inference-on-nvidia-dgx-spark/)**  
  <img alt="Abstract green computing cube with layered panels, performance icons, and streams of data on a black background" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/dg

## GitHub Trending (AI, new repos)
- **[OFat34764e/InterviewCopilot-rpocket-team](https://github.com/OFat34764e/InterviewCopilot-rpocket-team)**  
  ★ 64 — EdTech application designed to bridge the gap between learning and landing your dream job
- **[Omianheart/Deadline-resp-Tracker-AI](https://github.com/Omianheart/Deadline-resp-Tracker-AI)**  
  ★ 32 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[Doravanaheim/telegram-acp-bridge-IntelliJ-rpocket-IDEA](https://github.com/Doravanaheim/telegram-acp-bridge-IntelliJ-rpocket-IDEA)**  
  ★ 32 — Мост между Telegram и Codex ACP в IntelliJ IDEA: запускайте задачи и управляйте чатами с агентом прямо из Telegram.
- **[ElectroixHigh/rpocket-SmartGrow-AI](https://github.com/ElectroixHigh/rpocket-SmartGrow-AI)**  
  ★ 32 — AI and IoT-based plant monitoring system with sensor monitoring and a Telegram chatbot.
- **[lucidrains/attention-contact-planning](https://github.com/lucidrains/attention-contact-planning)**  
  ★ 10 — Implementation of Attention-based Contact Planning, by Junzhe He of ETH Zürich
- **[xAerux/aerus-ezai](https://github.com/xAerux/aerus-ezai)**  
  ★ 7 — EZ AI — Local AI made easy: Windows command center for local AI apps, model library, and coding agents.
- **[eDurphy/QATNN-HFP](https://github.com/eDurphy/QATNN-HFP)**  
  ★ 3 — Local Neural Network Quantized and Trainable On The Fly on CPU
- **[ALANDVO/sentinel-console-144](https://github.com/ALANDVO/sentinel-console-144)**  
  ★ 2 — Alan Vo | Work in progress: sentinel-console-144
- **[A220man/cobalt-lab-144-ryan-vo](https://github.com/A220man/cobalt-lab-144-ryan-vo)**  
  ★ 2 — Ryan Vo | Work in progress: cobalt-lab-144-ryan-vo
- **[hardikkoul/markclean-ai](https://github.com/hardikkoul/markclean-ai)**  
  ★ 2 — Convert any URL or HTML into clean, token-optimized LLM Markdown, structured JSON/CSV tables, and traceable RAG chunks with automatic table-header repetition and deep-linked citation URLs. Cuts LLM to
