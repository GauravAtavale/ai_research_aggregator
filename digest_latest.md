# AI Research Digest — 2026-11-13

## HF Daily Papers (Trending)
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 30 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 165 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 16 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 69 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**  
  ⬆ 102 upvotes — Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering ir
- **[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**  
  ⬆ 30 upvotes — Weight-activation quantization can reduce the memory and compute cost of neural-network inference, but recent methods often require expensive optimization and architecture-specific propagation of basis transforms across layers. We introduce MACaQ, an MXFP4 W4A4 post-training quantization method that
- **[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**  
  ⬆ 11 upvotes — Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning ma
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 65 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**  
  ⬆ 186 upvotes — This report presents VibeVoice, a novel model designed to synthesize
long-form speech with multiple speakers by employing next-token diffusion,
which is a unified method for modeling continuous data by autoregressively
generating latent vectors via diffusion. To enable this, we introduce a novel
con
- **[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**  
  ⬆ 86 upvotes — Software is one of the most powerful tools that we humans have at our
disposal; it allows a skilled programmer to interact with the world in complex
and profound ways. At the same time, thanks to improvements in large language
models (LLMs), there has also been a rapid development in AI agents that


## HF Daily Papers (Today, by Upvotes)
- **[SO-Arena: Benchmarking the Capability Spectrum and Reliability of System One Models](https://huggingface.co/papers/2611.15777)**  
  ⬆ 82 upvotes — System One models promise fast, general-purpose decision-making without lengthy token generation. However, understanding their capability spectrum and decision reliability requires more than aggregate performance on current benchmarks. Existing evaluations often provide limited insight into the brea
- **[BirdDreams: Joint Perspective and BEV Video Generation for a Plausible, Reactive Driving World Model](https://huggingface.co/papers/2611.14815)**  
  ⬆ 46 upvotes — Driving world models aim to simulate how a scene unfolds under different ego actions. This requires plausible motion of surrounding vehicles as well as precise ego-trajectory control. Learning vehicle motion from perspective video alone is challenging because motion is entangled with appearance and 
- **[PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models](https://huggingface.co/papers/2611.16748)**  
  ⬆ 42 upvotes — Video generation models produce visually realistic videos but still struggle with physical dynamics and causal consistency. Learning from generated videos requires fine-grained physical supervision, yet reliable quality judgments, correction pairs, and controlled variations are difficult to obtain. 
- **[G-STAR: Group-Scaled Token Capacity for Deeply Compressed Autoregressive Generation](https://huggingface.co/papers/2611.13004)**  
  ⬆ 41 upvotes — Discrete autoregressive models offer a scalable framework for image generation. However, they face a fundamental trade-off: long token sequences preserve representation quality but slow generation, while aggressive spatial compression reduces representation capacity. Based on product quantization, w
- **[Duo: A Reciprocal World Model for Full-Duplex Interaction](https://huggingface.co/papers/2611.15131)**  
  ⬆ 37 upvotes — In this report, we introduce the Reciprocal World Model (RWM) and present Duo v1, a full-duplex world model that continuously perceives audiovisual inputs while responding to users in real time. The RWM treats intelligence and physical reality as equally fundamental to what constitutes a world. Exis
- **[Open Vision Banana: A Fully Open Recipe for Generative Visual Perception](https://huggingface.co/papers/2611.15844)**  
  ⬆ 30 upvotes — Recent work suggests that pretrained image generators encode real-world understanding beyond image synthesis. Vision Banana exploits this by framing vision tasks as conditional image editing. However, its data, weights, code, and implementation details are not public. We present Open Vision Banana (
- **[Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents](https://huggingface.co/papers/2611.17167)**  
  ⬆ 29 upvotes — Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as ac
- **[Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors](https://huggingface.co/papers/2611.17060)**  
  ⬆ 26 upvotes — Large foundation models such as GPT-6 Astra and Claude Fable 5.1 have recently been shown to control robots directly from visual observations. They nevertheless remain brittle on long-horizon, contact-rich tasks in real-world environments. Further progress depends on two complementary resources: dem
- **[On the Design of Hyper-Connections: Simplification, Stability, and Scalability](https://huggingface.co/papers/2611.05984)**  
  ⬆ 26 upvotes — Hyper-Connections (HC) architectures are increasingly adopted in frontier language models, yet their components remain insufficiently understood and introduce non-negligible training overhead. In this work, we systematically study the HC architecture to understand its components and identify simpler
- **[TTB: Test-time Baking for Efficient Rendering of Decoder-only View Synthesis Models](https://huggingface.co/papers/2611.17331)**  
  ⬆ 21 upvotes — Decoder-only Large View Synthesis Models (LVSMs) with KV-cache have recently achieved state-of-the-art quality by regressing novel views from neural networks without reconstructing 3D geometry, while Test-Time Training (TTT) layers save computation but sacrifice quality. We propose Test-Time Baking 

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Unbundling Multimodal Vision Encoding](https://arxiv.org/abs/2611.17334v1)**  
  How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design choices: a visual prior f
- **[ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research](https://arxiv.org/abs/2611.17332v1)**  
  Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document
- **[Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation](https://arxiv.org/abs/2611.17329v1)**  
  Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been shown to optimize financial performance but typically does not enforce rule compliance, making it unsuit
- **[AgentSSL: Can MLE Agents Leverage Unlabeled Data?](https://arxiv.org/abs/2611.17323v1)**  
  Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline design, they have been studied almost exclusively in fully supervised settings, leaving them untested 
- **[Learning When Diffusion Language Models Should Regenerate](https://arxiv.org/abs/2611.17320v1)**  
  Remasking allows diffusion language models to revisit generated text, but effective correction requires knowing when and what to revise. Our diagnosis on Sudoku reveals two gaps. Hidden states contain error information that token confidence does not reliably expose, and remasking an isolated error u
- **[CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation](https://arxiv.org/abs/2611.17316v1)**  
  Coding agents tackle successive tasks on an evolving repository, carrying forward edits and writing memory before the next task is known. Selecting memory for unknown next tasks requires balancing future usefulness against the costs of writing and reading it. The actor must also decide when acting o
- **[Linking Rapid Learning to Compositional Structure in Neural Networks: Evidence from Additive Analogies in Meta-Learned Parameter Spaces](https://arxiv.org/abs/2611.17314v1)**  
  Humans can learn rapidly from limited experience, while neural networks typically require extensive training. In this work, we investigate what properties of a neural network can enable it to learn rapidly. We study neural networks that have been optimized via meta-learning, a technique that exposes
- **[Sketching Language Models for Context Attribution](https://arxiv.org/abs/2611.17313v1)**  
  Context attribution asks how removing parts of a prompt changes a language model's output. We study leave-one-out (LOO) attribution for a prompt of $n$ tokens and a fixed measurement function. Computing all LOO values directly requires $n$ model evaluations. Under a stability assumption, our algorit
- **[Classical Energies Learn to Reason 1,000x Faster than Looped Models](https://arxiv.org/abs/2611.17309v1)**  
  Looped models have emerged as a prominent paradigm for reasoning, with successes on simple reasoning puzzles such as Sudoku-Extreme and Maze-Unique. However, these models can be unstable, slow to train, and use many parameters and FLOPs to solve simple puzzles. Descent on an energy not only mitigate
- **[Quantifying structural stability of transparent models for general insurance pricing](https://arxiv.org/abs/2611.17308v1)**  
  The short duration of general insurance contracts leads to rapid distributional shifts in the data, warranting regular model updates. This process may yield a post-update model that differs considerably from the pre-update model in both predictions and structure. Structural stability is upstream of 

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Introducing ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet)**  
  Introducing ChatGPT Wallet, a secure way for agents in ChatGPT Work, Codex, and dots to complete purchases with user approval and existing card protections.
- **[Shield helps technicians hand off legacy portal work with OpenAI](https://openai.com/business/customer-stories/shield)**  
  Shield uses OpenAI to help IT technicians hand off work in legacy portals. Its Forge agents navigate systems so technicians can focus on issues needing their judgment.
- **[How Amplitude ships product improvements in 1–2 days with OpenAI](https://openai.com/business/customer-stories/amplitude)**  
  Built primarily on OpenAI models, Amplitude’s proactive product agent, Wave, identifies what to build, helps teams ship changes with coding agents, and measures the impact.
- **[Gondola doubles revenue as its team builds more with Codex](https://openai.com/business/customer-stories/gondola)**  
  Gondola helps creatives get credit and get hired, with Codex raising its lead engineer’s output by 50% and ChatGPT simplifying daily work.
- **[Holiday Extras is rethinking what it can build with Codex](https://openai.com/business/customer-stories/holidays-extras-codex)**  
  With Codex, Holiday Extras is turning customer expertise into better apps, higher booking conversion and new possibilities for growth.

## Lab Blog: DeepMind
- **[Introducing Gemini 4 Hydrogen](https://deepmind.google/blog/introducing-gemini-4-hydrogen/)**  
  
- **[AlphaGenome 2: Deciphering how cells read DNA to better understand disease](https://deepmind.google/blog/alphagenome-2-deciphering-how-cells-read-dna-to-better-understand-disease/)**  
  Predicting how DNA sequences and their variations impact specific human cell types and disease.
- **[Gemini 4 Carbon is now available](https://deepmind.google/blog/gemini-4-carbon-is-now-available/)**  
  
- **[Introducing AlphaProof Code: a breakthrough in verifying complex software at depth](https://deepmind.google/blog/introducing-alphaproof-code/)**  
  AlphaProof Code agents wrote three  million lines of proofs in Lean to verify Signal’s core encryption.
- **[Opening the datasets behind our AI weather models](https://deepmind.google/blog/opening-the-datasets-behind-our-ai-weather-models/)**  
  Foundational precipitation and geostationary satellite datasets to observe the planet clearly.

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

## Lab Blog: NVIDIA Blog
- **[How AI Is Helping Care Teams Get Patients the Right Care, Sooner](https://blogs.nvidia.com/blog/how-ai-is-helping-care-teams/)**  
  From pediatric research to smart hospitals, AI is helping care teams spend less time on routine tasks and more time with patients.  Health systems and startups are putting it to work across healthcare, from matching patients to clinical trials to sup
- **[A New Dawn in the Cloud: ‘Warhammer 40,000: Dawn of War IV’ Is Coming to GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-warhammer-dawn-of-war-iv-coming/)**  
  Rally the ranks this GFN Thursday. Warhammer 40,000: Dawn of War IV is coming to GeForce NOW, allowing players to experience the battle for Kronus through cloud gaming. There’s more on the horizon, with NVIDIA DLSS 5 technology coming to War Thunder 
- **[How AI Helps Recyclers Turn Mixed Waste Into Reusable Material](https://blogs.nvidia.com/blog/ai-recycling-startups/)**  
  Vision AI and robotics pick what’s worth recovering out of conveyor belts of used clothing, bottles and mixed recyclables, diverting thousands of tons of materials from landfills.
- **[NVIDIA Expands Open Source Commitment With OpenShell Contribution and New AI Infrastructure](https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/)**  
  Kubernetes, the open source system that manages how applications run across thousands of AI factories, has become the foundation for AI, and the demands on it are only growing. To help meet them, NVIDIA is deepening its commitment to open source at K
- **[Practice Makes Precise: At CoRL, NVIDIA and Partners Reveal How Robots Rehearse Delicate Work in Simulation](https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/)**  
  Simulation, which has long been the proving ground for robots learning to walk, roll and hop, is now helping researchers teach robots tasks that require a finer touch: aligning gears, connecting cables and assembling small components.  The shift from

## Lab Blog: NVIDIA Technical Blog
- **[Faster Scientific Simulations with New FP64 Algorithms in NVIDIA cuBLAS](https://developer.nvidia.com/blog/faster-scientific-simulations-with-new-fp64-algorithms-in-nvidia-cublas/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="431" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image5-7-768x431.png" style="display: block; margin-bottom: 5px; clear: both;" title="image5" width="768" />Many 
- **[Run GPU-Powered Black Hole Interferometry with NVIDIA cuPhoton](https://developer.nvidia.com/blog/run-gpu-powered-black-hole-interferometry-with-nvidia-cuphoton/)**  
  <img alt="Black hole illustration with a dark central region surrounded by bright orange rings and curved bands of light against a black background." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp
- **[Run Native DLA Inference in Python on NVIDIA Jetson AGX Orin Using cuDLA](https://developer.nvidia.com/blog/run-native-dla-inference-in-python-on-nvidia-jetson-agx-orin-using-cudla/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/08/dla-inference-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="dla-inference" width="
- **[When One GPU Isn’t Enough: Serving GLM-5.3 Across Two NVIDIA DGX Stations with vLLM](https://developer.nvidia.com/blog/when-one-gpu-isnt-enough-serving-glm-5-3-across-two-nvidia-dgx-stations-with-vllm/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image3-3-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image3" width="768" />Runni
- **[Adapt Human Motion for Robots with NVIDIA SOMA Retargeter](https://developer.nvidia.com/blog/adapt-human-motion-for-robots-with-nvidia-soma-retargeter/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="338" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/SOMA_Retargeter_Featured_600x338.gif" style="display: block; margin-bottom: 5px; clear: both;" title="SOMA_Retarg

## GitHub Trending (AI, new repos)
- **[rohitjee7022-blip/Anonymous-Campus](https://github.com/rohitjee7022-blip/Anonymous-Campus)**  
  ★ 37 — Anonymous Campus protects student identities while enabling honest campus facility feedback. It uses aggregated ratings and issue tracking to help administrators improve facilities, with BharatCode AI
- **[byte-od/mixture-of-scars](https://github.com/byte-od/mixture-of-scars)**  
  ★ 8 — Breaking the barrier between LLMs and hardware. Mixture of Scars (MoS) static weight compression & SCache O(1) constant KV-cache replacement.
- **[joedejesus/JJ_ML_DL_BOOK](https://github.com/joedejesus/JJ_ML_DL_BOOK)**  
  ★ 7 — Recurso educativo en español sobre Data Science, Machine Learning, Deep Learning, NLP y Transformers con Python, PyTorch y Jupyter.
- **[dharunram-lgtm/Echo_Knowledge](https://github.com/dharunram-lgtm/Echo_Knowledge)**  
  ★ 4 — ECHO Knowledge is a local-first AI-powered knowledge management system for organizing documents, semantic search, grounded AI answers, and interactive knowledge graphs. Built with Tauri, Rust, React, 
- **[pathbit/AgentDevKit](https://github.com/pathbit/AgentDevKit)**  
  ★ 4 — Repositório com as skills, comandos e outros que agentes de código irão utilizar.
- **[hanspeterdietiker/open-agent-skills](https://github.com/hanspeterdietiker/open-agent-skills)**  
  ★ 3 — Discover. Share. Build.
- **[haoqinhe8-boop/NeuroShaqma](https://github.com/haoqinhe8-boop/NeuroShaqma)**  
  ★ 3 — 小沙大脑：288,964 神经元脉冲皮层（果蝇 2.07x/4.16x），12 岁初中生在家用 2080Ti+4090 做的 SNN，主力开发 DeepSeek-V4-Pro
- **[Zar-Manah/HELIOS-Space-Weather](https://github.com/Zar-Manah/HELIOS-Space-Weather)**  
  ★ 3 — ☀️ Single-File Plug-and-Play 4 AI Models for Real-Time Solar Storm Impact & CME Arrival. Outperforms NASA supercomputers on consumer hardware. 🇪🇸
- **[webDMX/followspot-AI](https://github.com/webDMX/followspot-AI)**  
  ★ 2 — Tool for using moving lights as followspots based on video camera image.
- **[ALANDVO/tensor-hub-145](https://github.com/ALANDVO/tensor-hub-145)**  
  ★ 2 — Alan Vo | Work in progress: tensor-hub-145
