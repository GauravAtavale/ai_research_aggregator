# AI Research Digest — 2026-10-30

## HF Daily Papers (Trending)
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 159 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 126 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 6 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
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
- **[Investor's Last Exam: Can AI Agents Do Equity Investment Without Seeing the Future?](https://huggingface.co/papers/2610.38342)**  
  ⬆ 9 upvotes — Financial agents must form forecasts and investment judgments from decision-time evidence, with predictions evaluated against subsequent outcomes. Existing benchmarks assess financial knowledge, research workflows, or forecasting, but evaluating the full research process requires a strictly frozen i
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 62 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**  
  ⬆ 107 upvotes — Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system t

## HF Daily Papers (Today, by Upvotes)
- **[Intrinsic Distribution Matching](https://huggingface.co/papers/2610.39633)**  
  ⬆ 238 upvotes — One-step and few-step text-to-image generation must accurately render the details specified in the prompt despite limited opportunities for refinement. Distribution matching distillation (DMD) uses score differences to bring the generated distribution closer to a reference distribution. Following pr
- **[A-RSI: Adaptive Task Refresh for Zero-Data Multimodal Self-Improvement](https://huggingface.co/papers/2610.38568)**  
  ⬆ 150 upvotes — Recursive self-improvement requires models not only to acquire useful training experience, but also to decide when their current experience has ceased to be useful. Existing methods often focus on what experience to generate next, while paying less attention to when fresh experience should be introd
- **[Your Benchmark Is an Empirical Measure Over Difficulty](https://huggingface.co/papers/2610.29927)**  
  ⬆ 140 upvotes — A benchmark is not merely a collection of test questions; it naturally induces an empirical measure over difficulty. In this work, we develop this measure-based view of benchmark evaluation. This perspective allows us to identify and formalize two central failure modes: measure mismatch, where the b
- **[Look Only When Needed: Certificate-Guided Visual Routing for Efficient Diffusion VLMs](https://huggingface.co/papers/2610.36671)**  
  ⬆ 91 upvotes — Diffusion vision-language models (DVLMs) process their entire input at every denoising step. Since visual tokens make up 89-97% of this input on the benchmarks we study, most of the decoding computation is spent repeatedly processing the same image. Visual token pruning methods partially relieve thi
- **[Youtu-Parsing-Omni: One Encoder, One Schema, All Modalities](https://huggingface.co/papers/2610.39301)**  
  ⬆ 55 upvotes — We present Youtu-Parsing-Omni, an omni-modal parser that converts documents, images, audio, and video into structured records grounded in space and time, providing a perception layer for agents that read, locate, and cite evidence across modalities. Its design rests on one encoder for every modality
- **[Proving and Improving the Platonic Representation Hypothesis with JEPAs](https://huggingface.co/papers/2610.39302)**  
  ⬆ 54 upvotes — Whether models trained on different modalities converge to the same representation of the world is central to AI. The Platonic Representation Hypothesis (PRH) conjectures that they do as they scale, but without a proof it offers neither a guarantee nor a recipe. We turn the hypothesis into a theorem
- **[L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](https://huggingface.co/papers/2610.40614)**  
  ⬆ 35 upvotes — Interactive world models generate visual content conditioned on user actions, yet maintaining spatial consistency over long-horizon exploration in real time remains challenging. Existing approaches rely on either temporal context or explicit 3D memory, both of which scale poorly because memory grows
- **[Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers](https://huggingface.co/papers/2610.40647)**  
  ⬆ 31 upvotes — Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency structure benefits from gl
- **[WorkFactory: Turning Professional Intents into Executable Work for Scalable Agent Training](https://huggingface.co/papers/2610.37161)**  
  ⬆ 30 upvotes — Scaling supervised training for working agents requires diverse professional tasks that yield reliable expert demonstrations. However, missing or inconsistent task information can obstruct teacher execution and weaken the resulting supervision. We propose WorkFactory, a scalable framework for constr
- **[A Broader Look into MLLM's Retrieval Heads](https://huggingface.co/papers/2610.32411)**  
  ⬆ 28 upvotes — Locating relevant evidence in long inputs is a core capability of Multimodal Large Language Models. Prior studies attribute this capability to retrieval heads, a sparse set of attention heads that transfer information from the context to the output. However, these analyses are confined to a limited 

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Elucidating the Design Space of LM Data Attribution](https://arxiv.org/abs/2610.40655v1)**  
  Data attribution methods for Language Models (LMs) are typically evaluated using downstream tasks like fact retrieval. However, existing evaluations vary multiple dataset properties simultaneously, making it impossible to isolate exactly why an attribution algorithm fails. To diagnose these failures
- **[Propose-Filter-Release: Scaling Noise to Typical Sensitivity via Private Filtering](https://arxiv.org/abs/2610.40654v1)**  
  An estimator can be accurate and stable on typical data, yet sensitive to a few possible records. Differentially private mechanisms commonly scale their noise to the worst-case influence of a single record, which lets these records dictate the noise even when the remaining data would allow far less.
- **[Rethinking Neural Thickets Without Weight Perturbations](https://arxiv.org/abs/2610.40649v1)**  
  The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a sing
- **[Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers](https://arxiv.org/abs/2610.40647v1)**  
  Pixel-space generative Transformers typically use one token per image patch, so capturing finer detail requires more tokens and makes global attention increasingly expensive. We observe that finer detail does not necessarily require more global communication: low-frequency structure benefits from gl
- **[Adaptive Scenario Generation for KL-DRO Around a Learned Density Model](https://arxiv.org/abs/2610.40644v1)**  
  Distributionally robust optimization (DRO) hedges data-driven two-stage stochastic programs against error in the distribution estimated from a finite record, and standard ambiguity sets differ in how they treat realizations absent from that record. A divergence ball around the empirical distribution
- **[Luggage re-identification: A study of strategies towards a real-world application](https://arxiv.org/abs/2610.40643v1)**  
  Luggage re-identification (ReID) is a critical task in video surveillance for forensics, security or border management (suspicious or abandoned luggage recognition), as well as luggage management (lost luggage recovery). It enables the association of observations of the same luggage across disjoint 
- **[From extreme weather to agricultural consequences with agentic AI](https://arxiv.org/abs/2610.40641v1)**  
  Extreme weather is forecast days ahead, yet its consequences for agriculture remain hard to predict: a forecast says where a storm will strike, not which crops will suffer or how much is at risk, and the records that could tell span many sources. We present WxCrop, the first agent that judges agricu
- **[world2vec: Mechanistic world models through latent dynamics learning](https://arxiv.org/abs/2610.40637v1)**  
  World models can achieve strong control performance without faithfully capturing the dynamics of their environment, limiting their potential for mechanistic interpretability and scientific discovery. Here, we introduce world2vec to learn mechanistic world models without reward information directly f
- **[Probing Spatial State Representations in Visual Foundation Models](https://arxiv.org/abs/2610.40636v1)**  
  An observer sees only part of the surrounding world, yet must keep track of what lies beyond the current view. Spatial perception therefore involves more than recognizing individual images: it calls for a persistent spatial state that is updated under self-motion and used to guide action. Do visual 
- **[ShallowDefend: Harnessing Shallow Safety Alignment for Multi-Turn Defender](https://arxiv.org/abs/2610.40627v1)**  
  Safety alignment has enabled large language models to reliably refuse harmful requests directly, yet the same request distributed across a multi-turn conversation still succeeds far too often. This brittleness has a mechanistic root: Alignment is shallow, with safety behavior concentrated in a model

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Making it easier for websites to express AI training preferences](https://openai.com/index/helping-websites-express-ai-training-preferences)**  
  OpenAI will honor a shared robots.txt signal to help website operators communicate their AI training preferences to participating providers.
- **[Community safety report and new protections for teens](https://openai.com/index/community-safety-report-and-new-protections-for-teens)**  
  OpenAI is strengthening violence prevention in ChatGPT with expanded safeguards, earlier interventions, and a new commitment to public safety reporting.
- **[Fair use benefits everyone](https://openai.com/index/fair-use-benefits-everyone)**  
  OpenAI shares excerpts from court briefs by creators, academics, accessibility advocates, and legal experts, among others, on how fair use supports AI training and innovation.
- **[An updated Model Spec for more capable and beneficial AI](https://openai.com/index/updated-model-spec)**  
  OpenAI’s updated Model Spec outlines five core values to guide more capable AI toward sound judgment, human agency, and faithfulness to human intent.
- **[How we detect frontier model misalignment](https://openai.com/index/how-we-detect-frontier-model-misalignment)**  
  OpenAI uses layered monitoring to detect frontier model misalignment and unauthorized agent behavior so responders can intervene before incidents escalate.

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
- **[Things That Go Beep in the Night: Agentic AI Joins the Search for Extraterrestrial Signals](https://blogs.nvidia.com/blog/ai-joins-the-search-for-extraterrestrial-signals/)**  
  While science fiction lore tells us that humans will meet extraterrestrial life in the form of little green men, the detail that should raise hairs this Halloween is this: the search for extraterrestrial intelligence took a major leap forward with AI
- **[Into the Omniverse: How Developers Turn Ideas Into Simulations With Frontier AI Agents](https://blogs.nvidia.com/blog/developers-simulation-frontier-ai-agents/)**  
  Turning a simulation idea into a working application means assembling assets, connecting physics and rendering, and checking that the scene behaves as intended. Developers are combining frontier AI models with NVIDIA Omniverse libraries to help carry
- **[Slice Into GFN Thursday: ‘Phantom Blade Zero’ Launches on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-phantom-blade-zero/)**  
  This Halloween week, GFN Thursday is delivering a fresh batch of gaming treats. Something wicked this blade comes. S-GAME’s Phantom Blade Zero launches on GeForce NOW today, bringing a scarily good blend of martial arts and punk fantasy to the cloud.
- **[Thin, Light and Built for Everything: NVIDIA RTX Spark Windows Laptops Gain New Models, Agent Tools and Games](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-updates-models-agents-games/)**  
  NVIDIA RTX Spark powers thin and light laptops built for everything that developers, creators and gamers do. RTX Spark laptops are now available from ASUS, Dell, HP, Lenovo, Microsoft and MSI. These powerful systems combine an NVIDIA Blackwell RTX GP
- **[How AI Is Changing the Pace of Discovery for Millions Living With Dementia](https://blogs.nvidia.com/blog/open-source-ai-tools-cbrain-dementia/)**  
  There are 57 million people worldwide living with dementia today. For the researchers working to help them, the obstacle isn’t a lack of effort — it’s too much data, too few experts to synthesize it and a pace of discovery that can’t keep up with the

## Lab Blog: NVIDIA Technical Blog
- **[Build a Validated Kubernetes Runtime for NVIDIA Dynamo](https://developer.nvidia.com/blog/build-a-validated-kubernetes-runtime-for-nvidia-dynamo/)**  
  <img alt="Glowing green AI network illustration in front of server racks." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/inline-image-1-1-768x432.png" style="display: bloc
- **[Run AI Models for Edge Application Development with Just a Few Commands](https://developer.nvidia.com/blog/run-ai-models-for-edge-application-development-with-just-a-few-commands/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/nvidia-trtedge-chat-terminal-1920x1080-1-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" ti
- **[Build Specialized Agents on a Stack You Control with NVIDIA NemoClaw](https://developer.nvidia.com/blog/build-specialized-agents-on-a-stack-you-control-with-nvidia-nemoclaw/)**  
  <img alt="Orange lobster character holding a green shield with a padlock beside a computer displaying code and an NVIDIA DGX Spark on a desk." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-conten
- **[How to Check and Configure NVIDIA GPUDirect Storage for Your Platform](https://developer.nvidia.com/blog/how-to-check-and-configure-nvidia-gpudirect-storage-for-your-platform/)**  
  <img alt="Data center server racks with network cables connecting rack-mounted equipment." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/inline-image-1-e1793140900880-768x
- **[Unlocking Tensor Core Performance for Machine Learning Interatomic Potentials](https://developer.nvidia.com/blog/unlocking-tensor-core-performance-for-machine-learning-interatomic-potentials/)**  
  <img alt="Colorful matrix-like blocks transition into a lattice of spheres, illustrating computation for atomistic simulation." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/

## GitHub Trending (AI, new repos)
- **[OFat34764e/InterviewCopilot-rpocket-team](https://github.com/OFat34764e/InterviewCopilot-rpocket-team)**  
  ★ 56 — EdTech application designed to bridge the gap between learning and landing your dream job
- **[Omianheart/Deadline-resp-Tracker-AI](https://github.com/Omianheart/Deadline-resp-Tracker-AI)**  
  ★ 32 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[SRN0129/Agenttrust](https://github.com/SRN0129/Agenttrust)**  
  ★ 20 — Enterprise Zero-Trust AI Security & Governance Gateway: Real-Time Prompt Injection Defense, Action Scoping, HITL Approvals, Post-Quantum Merkle Audit & EU AI Act Compliance for Autonomous Agent Swarms
- **[lucidrains/attention-contact-planning](https://github.com/lucidrains/attention-contact-planning)**  
  ★ 10 — Implementation of Attention-based Contact Planning, by Junzhe He of ETH Zürich
- **[eDurphy/QATNN-HFP](https://github.com/eDurphy/QATNN-HFP)**  
  ★ 3 — Local Neural Network Quantized and Trainable On The Fly on CPU
- **[biletian/awesome-ai-news-sources-zh](https://github.com/biletian/awesome-ai-news-sources-zh)**  
  ★ 3 — 精选 AI 资讯信源清单（中英双语）· Curated AI news sources, read daily by Zhiyike
- **[ALANDVO/sentinel-console-144](https://github.com/ALANDVO/sentinel-console-144)**  
  ★ 2 — Alan Vo | Work in progress: sentinel-console-144
- **[ALANDVO/tensor-foundry-144](https://github.com/ALANDVO/tensor-foundry-144)**  
  ★ 2 — Alan Vo | Work in progress: tensor-foundry-144
- **[Anil-matcha/open-spaces](https://github.com/Anil-matcha/open-spaces)**  
  ★ 2 — Free, open-source alternative to ChatGPT Spaces: a self-hostable AI workspace for shared pages and conversations.
- **[A220man/tensor-engine-144-ryan-vo](https://github.com/A220man/tensor-engine-144-ryan-vo)**  
  ★ 2 — Ryan Vo | Work in progress: tensor-engine-144-ryan-vo
