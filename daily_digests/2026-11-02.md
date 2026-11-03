# AI Research Digest — 2026-11-02

## HF Daily Papers (Trending)
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 9 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 162 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 63 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**  
  ⬆ 111 upvotes — Frontier open-weight models are increasingly available, but serving them still largely assumes datacenter infrastructure. We present FreeToken, an edge-native MoE serving system that treats a personal machine not as a small GPU, but as a unified, elastic inference platform. FreeToken co-designs the 
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 86 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 103 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,
- **[Differentiable Data Augmentation with Kornia](https://huggingface.co/papers/2011.09832)**  
  ⬆ 1 upvotes — In this paper we present a review of the Kornia differentiable data
augmentation (DDA) module for both for spatial (2D) and volumetric (3D)
tensors. This module leverages differentiable computer vision solutions from
Kornia, with an aim of integrating data augmentation (DA) pipelines and
strategies 
- **[HairDeck: Animation-Ready Stylized Hair Cards from a Single Image](https://huggingface.co/papers/2610.40599)**  
  ⬆ 41 upvotes — The hair of stylized characters in games and avatars is built from hair cards: artist-placed ribbons whose geometry is the visible hair, animated by spring bones. Existing image-based methods produce realistic hair or a single fused mesh, while CHARM, the only generator of stylized hair cards, decod
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 33 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Xiaomi-OCR-0 Technical Report](https://huggingface.co/papers/2609.36136)**  
  ⬆ 13 upvotes — Compact OCR-specific vision-language models achieve strong document parsing performance, but often rely on costly supervision and focus primarily on visual-text reconstruction. We introduce Xiaomi-OCR-0, a unified 0.8B model for document parsing and OCR-centric understanding. We build an approximate

## HF Daily Papers (Today, by Upvotes)
- **[REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control](https://huggingface.co/papers/2610.42053)**  
  ⬆ 114 upvotes — Foundation models are becoming remarkably reliable at high-level reasoning, yet they remain too slow and costly to serve as fine-grained controllers. Conversely, fast policies like VLAs and whole-body controllers offer more efficient reflexes, but struggle to generalize. While pairing a deliberative
- **[FrameForge: Harnessing Priors of Video Foundation Models for Unified Image Generation](https://huggingface.co/papers/2610.36545)**  
  ⬆ 112 upvotes — Unified conditional image generation requires a single model to preserve different aspects of a visual input while producing a target image that follows textual guidance. Pretrained video models provide a promising foundation by encoding visual transformations across time, yet existing approaches ty
- **[R^2Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop](https://huggingface.co/papers/2610.22740)**  
  ⬆ 90 upvotes — In recent years, agentic orchestration has been widely applied to solve complex human tasks. However, existing orchestration learning still faces key challenges, including hand-designed curricula, advantage collapse when a task's rollouts all reach the same outcome, and unreliable evaluation signals
- **[Does Scaling Toward AGI Depend on What System-1 Lets System-2 Execute?](https://huggingface.co/papers/2610.39497)**  
  ⬆ 55 upvotes — Progress toward artificial general intelligence (AGI) has largely relied on scaling a resource-intensive executive, System-2, through larger models, more data and compute, longer reasoning, and more agents. We ask whether the next stage may come instead from co-designing it with System-1, a lightwei
- **[Apriel Voice 27B Preview: An Open Model for Speech, Reasoning, and Tool Use](https://huggingface.co/papers/2610.40738)**  
  ⬆ 33 upvotes — A capable voice assistant must do more than recognize words; it must understand requests, reason over context, sustain conversations, and act through tools. We present Apriel Voice 27B Preview, an open speech-language model that unifies these capabilities within a shared reasoning backbone while ret
- **[Follow the Gradient: Tracing Safety Degradation Back to Training Data](https://huggingface.co/papers/2610.37481)**  
  ⬆ 28 upvotes — Fine-tuning Large Language Models (LLMs) on instruction data can quietly erode their safety, even when no training example looks harmful. Because this safety-degrading data looks benign, standard content filters struggle to catch it. We tackle this problem by developing SimpleLoRIF, a scalable gradi
- **[Latent Reasoning in Continuous Space for Unified Multimodal Models](https://huggingface.co/papers/2610.42149)**  
  ⬆ 27 upvotes — Unified Multimodal Models (UMMs) achieve remarkable success on diverse multimodal understanding and generation tasks, yet they still struggle to effectively leverage language-based chain-of-thought reasoning for image generation. As a result, existing reasoning-augmented UMMs often fail to inherit t
- **[WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in Short-Video Search](https://huggingface.co/papers/2610.16927)**  
  ⬆ 26 upvotes — Short-video search needs compact query rewriters that recover users' personalized intent from ambiguous queries under strict latency constraints. Existing LLM-based methods have improved rewriting by using synthetic reasoning and subsequent consumption-behavioral feedback. However, overemphasizing s
- **[OSWAM: An Effective World Action Model with One-Step Action Generation](https://huggingface.co/papers/2610.35850)**  
  ⬆ 24 upvotes — Direct-policy World Action Models (WAM) have demonstrated the benefits of decoupling action generation from explicit future visual prediction for efficient inference in autonomous driving and embodied control. However, they still require tens of denoising steps to achieve competitive action quality,
- **[Wizard: Manipulate Any World in Real Time via Agentic Control](https://huggingface.co/papers/2610.40339)**  
  ⬆ 24 upvotes — Recent advances in video world models have enabled the generation of increasingly realistic and interactive virtual environments, opening new possibilities for player-customizable gameplay. Agentic frameworks further advance this direction by decoupling explicit game logic and controllable world rep

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Accelerating posterior sampling in Bayesian inverse problems with diffusion models: an online-offline perspective](https://arxiv.org/abs/2611.01300v1)**  
  Bayesian inverse problems require both informative prior models and computationally feasible posterior inference. Score-based diffusion models provide expressive learned priors, but their use for inversion introduces a conditioning problem: the score of a noised posterior is generally unavailable fr
- **[Best-of-Both-Worlds FTRL for Linear Bandits: The Interplay of Information Acquisition, Corruption, and Geometry](https://arxiv.org/abs/2611.01299v1)**  
  We study \textit{best-of-both-worlds} (BOBW) algorithms for linear bandits, which aim to simultaneously guarantee $\gO(\sqrt T)$ regret in the adversarial regime and $\gO(\log T)$ regret in the stochastic regime over $T$ rounds. For finite action sets, we introduce \emph{information-acquisition foll
- **[[Re] Pure Noise to the Rescue of Insufficient Data](https://arxiv.org/abs/2611.01295v1)**  
  We examine the main claims of Zada, Benou, and Irani (2021), which states that in an image classification task with imbalanced training data, (i) using pure noise to augment minority-class images encourages generalization by improving minority-class accuracy. This method is paired with (ii) a new ba
- **[Character-Name Concentration in LLM Fiction: Measuring Displacement and Mitigating Repetition](https://arxiv.org/abs/2611.01284v1)**  
  Character names in large language model (LLM) fiction concentrate on a handful of recurrent names such as 'Elara' and 'Elias', a measurable face of AI slop. Existing fixes either require logit access or retraining, or operate per request and cannot control concentration across a corpus. How much pro
- **[OntoDoc: Automatically Generating Ontology Resource Descriptions](https://arxiv.org/abs/2611.01276v1)**  
  Knowledge graphs and ontologies form the backbone of structured, machine-readable knowledge representation, yet ontology terms often lack natural language descriptions, limiting their accessibility and reuse. Existing ontology verbalization approaches tend to rely on rule-based or template-driven te
- **[Geometry of Confabulation and Refusal in Small Language Models](https://arxiv.org/abs/2611.01272v1)**  
  Faced with an unanswerable question, small language models can either refuse or confabulate: confidently produce a wrong answer. Can the hidden state before the first generated token provide a clue? Can we flip confabulations into refusals? I introduce ConfabQA, a 784-item benchmark whose obscure-pr
- **[Learning momenta for Hamiltonian-based models](https://arxiv.org/abs/2611.01269v1)**  
  There has been increasing interest in methodologies that incorporate physics priors into neural network architectures to enhance their modeling capabilities. Among these methodologies, Hamiltonian neural networks (HNNs) and their variants have gained considerable attention. These architectures expli
- **[EZ-Ar-VC: Robust Arabic Voice Anonymization with Generalization across Dialects and Code-Switching](https://arxiv.org/abs/2611.01268v1)**  
  Voice conversion (VC) models can be used to anonymize speech data while preserving naturalness. Existing models, however, are mainly optimized for English and other high-resource languages, and they fail to generalize well to Arabic due to its distinct phonology. In this work, we comprehensively eva
- **[Toward Bounding Coding-Agent Autonomy in Software Maintenance: A Pilot Study of Boundary Contracts](https://arxiv.org/abs/2611.01265v1)**  
  As coding agents gain greater autonomy to modify software repositories, relevant context alone does not define their operational authority. An artifact may be relevant to a maintenance task while being inappropriate to edit; conversely, another artifact may be required even when it is not explicitly
- **[Does Random Search Discover Task Experts? Revisiting Neural Thickets](https://arxiv.org/abs/2611.01262v1)**  
  Pretrained models are typically viewed as generalists, requiring bespoke post-training to achieve task-specific expertise. Gan & Isola (2026) recently proposed a striking alternative: that pretrained models lie in a dense neural thicket of task specialists, which can be surfaced with simple Gaussian

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Scaling Git at OpenAI](https://openai.com/index/scaling-git-at-openai)**  
  How OpenAI built Pando, a Git-compatible backend designed for the scale of development that Codex makes possible.
- **[Introducing the Grid Protectors Program](https://openai.com/index/grid-protectors-program)**  
  OpenAI’s Grid Protectors Program will work with utilities to help future compute campuses support grid reliability and protect consumer electricity costs.
- **[Rewarding defenders with bigger bug bounties](https://openai.com/index/rewarding-defenders-with-bigger-bug-bounties)**  
  OpenAI is raising Security Bug Bounty rewards and introducing report quality, loyalty, and priority campaign bonuses for independent security researchers.
- **[Preparing our next security sprint to harden OpenAI](https://openai.com/index/preparing-our-next-security-sprint-to-harden-openai)**  
  OpenAI is preparing its next internal security sprint with Cathedral Systems to test and strengthen its defenses using AI.
- **[LifeVal](https://openai.com/index/lifeval)**  
  Introducing LifeVal, a benchmark measuring how well AI helps people complete everyday tasks, from finding childcare to managing finances and government paperwork.

## Lab Blog: DeepMind
- **[Speeding up planning decisions with AI](https://deepmind.google/blog/speeding-up-planning-decisions-with-ai/)**  
  Google DeepMind and UK government work together to reduce planning assessment times
- **[Gemini 4 Carbon: Our next frontier model](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)**  
  
- **[Genie 4: A new generation of world simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)**  
  Genie 4: our new world model unlocking unprecedented realism in real-time simulation.
- **[Beyond tree cover: mapping the world’s forest types](https://deepmind.google/blog/beyond-tree-cover-mapping-the-worlds-forest-types/)**  
  A global map categorizing every 10-meter patch of land on Earth into distinct forest types.
- **[Accelerating the search for antimicrobial peptides with Google Antigravity](https://deepmind.google/blog/accelerating-antimicrobial-discovery/)**  
  Accelerating the search for novel antimicrobial peptides using Google Antigravity for Science.

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
- **[Diagnose Distributed AI Workload Failures with NVIDIA Attribution](https://developer.nvidia.com/blog/diagnose-distributed-ai-workload-failures-with-nvidia-attribution/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image3-1-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="image3" width="768" />In di
- **[Keep Distributed Training Running with Automated Workload Recovery](https://developer.nvidia.com/blog/keep-distributed-training-running-with-automated-workload-recovery/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image8-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image8" width="768" />As dist
- **[Making Kubernetes AI-Ready for NVIDIA Vera Rubin on Day One](https://developer.nvidia.com/blog/making-kubernetes-ai-ready-for-nvidia-vera-rubin-on-day-one/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/runai-tech-blog-compute-domains-1920x1080-4504000-1024x576-png-768x432.webp" style="display: block; margin-bottom
- **[Build World Models for Interactive Simulation with NVIDIA Cosmos](https://developer.nvidia.com/blog/build-world-models-for-interactive-simulation-with-nvidia-cosmos/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="338" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/cosmos-framework-tech-blog-600x338-5784057.webp" style="display: block; margin-bottom: 5px; clear: both;" title="
- **[Support New AI Frameworks Faster Using NVIDIA Workload Map](https://developer.nvidia.com/blog/support-new-ai-frameworks-faster-using-nvidia-workload-map/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="431" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/AdobeStock_1f14ed65-d635-4fac-a472-570887464326-e1793050942456-768x431.webp" style="display: block; margin-bottom

## GitHub Trending (AI, new repos)
- **[Jumbomuffin777/Frontier-UI](https://github.com/Jumbomuffin777/Frontier-UI)**  
  ★ 54 — ChatGPT-style generative UI for Open WebUI: photo galleries, live maps with real routes, multi-day trips, budgets, calculators, live weather & stocks, link previews, and one-click Word/Excel/PowerPoin
- **[Omianheart/Deadline-resp-Tracker-AI](https://github.com/Omianheart/Deadline-resp-Tracker-AI)**  
  ★ 25 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[Anil-matcha/open-spaces](https://github.com/Anil-matcha/open-spaces)**  
  ★ 3 — Free, open-source alternative to ChatGPT Spaces: a self-hostable AI workspace for shared pages and conversations.
- **[abchughtai786/automated-job-posting-pipeline](https://github.com/abchughtai786/automated-job-posting-pipeline)**  
  ★ 3 — Node.js pipeline that collects, screens with AI, de-duplicates and publishes job listings demo with sample data
- **[biletian/awesome-ai-news-sources-zh](https://github.com/biletian/awesome-ai-news-sources-zh)**  
  ★ 3 — 精选 AI 资讯信源清单（中英双语）· Curated AI news sources, read daily by Zhiyike
- **[KCFindstr/RSI-Bench](https://github.com/KCFindstr/RSI-Bench)**  
  ★ 3 — Frontier Foundation Model Benchmark
- **[ashh-droid/AksharaCheck](https://github.com/ashh-droid/AksharaCheck)**  
  ★ 3 — AksharaCheck detects Hindi and Kannada text-rendering issues using Chromium, with multilingual BharatCode AI explanations, visual evidence, and browser-verified repair suggestions.
- **[ALANDVO/sentinel-console-144](https://github.com/ALANDVO/sentinel-console-144)**  
  ★ 2 — Alan Vo | Work in progress: sentinel-console-144
- **[ALANDVO/vector-lab-144](https://github.com/ALANDVO/vector-lab-144)**  
  ★ 2 — Alan Vo | Work in progress: vector-lab-144
- **[A220man/beacon-observatory-144](https://github.com/A220man/beacon-observatory-144)**  
  ★ 2 — Ryan Vo | Work in progress: beacon-observatory-144
