# AI Research Digest — 2026-11-09

## HF Daily Papers (Trending)
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 164 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 15 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**  
  ⬆ 185 upvotes — This report presents VibeVoice, a novel model designed to synthesize
long-form speech with multiple speakers by employing next-token diffusion,
which is a unified method for modeling continuous data by autoregressively
generating latent vectors via diffusion. To enable this, we introduce a novel
con
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 64 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 67 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across Arbitrary Scenes](https://huggingface.co/papers/2611.08264)**  
  ⬆ 64 upvotes — We identify a key limitation of existing feed-forward 3DGS methods: Gaussian attributes are typically predicted in a radial-distance-normalized space that canonicalizes a global radial statistic of the reconstructed geometry, while the spacing between neighboring Gaussian centers can still vary subs
- **[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**  
  ⬆ 111 upvotes — Frontier open-weight models are increasingly available, but serving them still largely assumes datacenter infrastructure. We present FreeToken, an edge-native MoE serving system that treats a personal machine not as a small GPU, but as a unified, elastic inference platform. FreeToken co-designs the 
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 103 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,
- **[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**  
  ⬆ 77 upvotes — High throughput serving of large language models (LLMs) requires batching
sufficiently many requests at a time. However, existing systems struggle
because the key-value cache (KV cache) memory for each request is huge and
grows and shrinks dynamically. When managed inefficiently, this memory can be

- **[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**  
  ⬆ 86 upvotes — Software is one of the most powerful tools that we humans have at our
disposal; it allows a skilled programmer to interact with the world in complex
and profound ways. At the same time, thanks to improvements in large language
models (LLMs), there has also been a rapid development in AI agents that


## HF Daily Papers (Today, by Upvotes)
- **[SplatAnything: Gaussian Spacing Normalization for Feed-forward 3DGS across Arbitrary Scenes](https://huggingface.co/papers/2611.08264)**  
  ⬆ 64 upvotes — We identify a key limitation of existing feed-forward 3DGS methods: Gaussian attributes are typically predicted in a radial-distance-normalized space that canonicalizes a global radial statistic of the reconstructed geometry, while the spacing between neighboring Gaussian centers can still vary subs
- **[Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription](https://huggingface.co/papers/2611.06043)**  
  ⬆ 57 upvotes — Streaming speech recognition is increasingly consumed by machines, such as translators and voice agents, that act on each token as it appears. A token that is later revised costs wasted work or a wrong action. In this work, we present Confucius4-R2T2 (short for Real Real-Time Transcription), a stabl
- **[P^2-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter Priors](https://huggingface.co/papers/2611.03953)**  
  ⬆ 45 upvotes — Multi-teacher on-policy distillation consolidates expert capabilities by supervising student-generated trajectories, whereas task arithmetic offers a training-free alternative through linear parameter combinations. We view the linear combination of student and expert parameters as a single different
- **[PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?](https://huggingface.co/papers/2611.08175)**  
  ⬆ 34 upvotes — Automating printed circuit board (PCB) routing requires coordinating board-level connectivity decisions with geometric execution under strict design rules. Although recent agents can interact with native routing tools, reliable routing on complex boards remains challenging. We present PCBRouteAgent,
- **[Toward the Era of Agentic Embodied Intelligence](https://huggingface.co/papers/2611.09124)**  
  ⬆ 29 upvotes — Foundation models increasingly guide robot actions, yet sustained autonomy requires efficient control and failure recovery. We introduce A2-MEAS, an embodied multi-agent framework built around code as a scaling interface. Learned correction codes combine corrective language, spatial evidence, execut
- **[LongBanana: An Expert-Verified Benchmark for Long-Context Multi-Reference Image Synthesis](https://huggingface.co/papers/2611.06856)**  
  ⬆ 29 upvotes — We introduce LongBanana, to our knowledge the first expert-designed and expert-verified benchmark for long-context multi-reference image synthesis in the age of agent-driven image generation. The task requires retrieving dispersed visual evidence, rejecting distractors, binding entities and relation
- **[LLMs Don't Know What They Know: Benchmarking Temporal Self-Knowledge for Financial Backtesting](https://huggingface.co/papers/2611.06808)**  
  ⬆ 25 upvotes — Financial backtests of large language models (LLMs) are meaningful only if the model did not already know the outcomes it is asked to predict. Practitioners guard against this by trusting a vendor's stated knowledge cutoff, by asking the model what it knows, or by instructing it to answer as of a pa
- **[Beneath the Surface: What We Overlook When We Talk About Agent Evolution](https://huggingface.co/papers/2611.07624)**  
  ⬆ 23 upvotes — Agent harness evolution enables recursive self-improvement (RSI) without updating model weights. We examine whether higher benchmark scores yield reliable, efficient, and transferable improvement. We evaluate four methods across harnesses, general and coding tasks. Repeated evaluations, controlled a
- **[EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models](https://huggingface.co/papers/2611.06748)**  
  ⬆ 20 upvotes — Generative video models are increasingly used as visual world simulators, yet their primary strength lies in rendering plausible pixels rather than reasoning about how a world should evolve. Coherent world evolution requires more than visual fidelity: when an event occurs, a model must infer its con
- **[Fast and Exact Relative-Position Attention via Structure-Aware Kernels](https://huggingface.co/papers/2611.01182)**  
  ⬆ 19 upvotes — Relative-position attention mechanisms offer compelling alternatives to RoPE across various transformer architectures, delivering superior performance in domains such as audio. These mechanisms typically modify attention scores by adding content-position or bias-position terms. Unlike RoPE, which en

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Hybrid Source Code Change Impact Analysis](https://arxiv.org/abs/2611.10958v1)**  
  Change impact analysis (CIA) helps developers identify code entities impacted by their initial changes. While several approaches for CIA were proposed, they still struggle with either low precision or low recall, thereby increasing manual effort for developers to verify the results. Furthermore, lim
- **[Risk-Sensitive Reinforcement Learning for an Options Market Maker: An Empirical Study with Real S&P 500 Options](https://arxiv.org/abs/2611.10956v1)**  
  Options market makers absorb client order flow and must hedge the resulting inventory risk under trading frictions. We study whether an option hedging reinforcement learning (RL) agent trained on historical market data outperforms three alternatives in tail-risk protection: (i) traditional delta hed
- **[Interpretable Cyber-Physical Attack Detection in Smart Grids: A Leakage-Controlled Multi-Testbed Evaluation of Fusion, Robustness, and Observability Limits](https://arxiv.org/abs/2611.10950v1)**  
  Cyber-physical smart-grid detectors are typically treated as black boxes and validated exclusively on clean, temporally shuffled datasets, which risk overly optimistic performance claims. This work presents a multi-testbed evaluation study built around an interpretable, time-windowed fusion Random F
- **[CoupledFlow: One-Step Neural Operators for Coupled Multi-Physics PDEs](https://arxiv.org/abs/2611.10945v1)**  
  This paper introduces COUPLED FLOW, a new neural operator learning framework for multi-physics PDE systems that captures the co-evolution of multiple physical processes by modeling their cross-process interactions. Unlike existing neural operator methods that primarily target single-physics settings
- **[Semantic Synthesis over Brute-Force Search: LLM-Guided Transformation Design for Efficient Learning](https://arxiv.org/abs/2611.10940v1)**  
  Data transformation pipelines shape the training distribution in computer vision, but designing them is a computationally expensive problem. We investigate whether large language models can enable efficient discovery by synthesizing executable transformation programs outside predefined augmentation 
- **[Can small transformers learn the language of Coxeter groups?](https://arxiv.org/abs/2611.10936v1)**  
  The field of mechanistic interpretability is well-suited to collaborative projects between mathematicians and AI researchers. This work describes one such project. We trained a small transformer to learn the language of the Coxeter group affine A2, best known as the symmetries of the tiling of the E
- **[Gendered Misclassification from Surname-Based Race Imputation](https://arxiv.org/abs/2611.10931v1)**  
  Researchers increasingly estimate political behavior based on race and gender from voter files, where race is imputed from surnames and geography. This only works where surnames suggest group membership, an assumption violated where surnames follow norms around marriage. Imputation is therefore bias
- **[DeepFinance: Can AI Diligence a $100MM Deal?](https://arxiv.org/abs/2611.10926v1)**  
  Existing evaluations of AI models on high-finance work focus on retrieving answers from financial documents and producing numerically correct outputs. Real private equity (PE) and investment banking (IB) work also depends on choosing between conflicting sources, making sound assumptions, and keeping
- **[Prescriptive Learning of Linear Policies with Feasibility Guarantees for Binary Decision-Making](https://arxiv.org/abs/2611.10923v1)**  
  Binary decision-making under uncertainty arises across a wide range of applications, including energy systems scheduling, transportation, and workforce planning. While machine learning has been increasingly applied to accelerate or replace mixed-integer solvers in such settings, existing approaches 
- **[Pole or Vector? Encoders Capture Bangla Compound Verbs, but LLMs Read Them Literally](https://arxiv.org/abs/2611.10909v1)**  
  In Bangla, a main verb is often followed by one of a small set of vector verbs. These verbs lose their own meaning and add a shade of meaning instead, such as completion. For example, likhe phello means that someone finished writing, not that they wrote and threw something. The same two verbs can al

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[ChatGPT Enterprise now available in AWS Marketplace](https://openai.com/index/chatgpt-enterprise-aws-marketplace)**  
  ChatGPT Enterprise is now available through AWS Marketplace, helping organizations simplify procurement through existing AWS purchasing and billing relationships.
- **[Control Room: A central system to track and stop model workloads across our research infrastructure](https://openai.com/index/control-room)**  
  Learn how OpenAI’s Control Room tracks model workloads across our research infrastructure and can rapidly stop them when safety or security concerns arise.
- **[CodeRabbit scales agentic software development and ships 20x more](https://openai.com/index/coderabbit-codex-daybreak)**  
  CodeRabbit uses OpenAI models to govern and trust AI-generated code and Codex to ship 20 times more software with the same engineering team.
- **[Kuken Industries searches 70 years of drawings in minutes](https://openai.com/index/kuken)**  
  Kuken Industries uses the OpenAI API to search 70 years of cooling tower drawings. Engineers can find the drawing for a repair in 4.5 minutes, down from nearly an hour.
- **[Partnering with Hacktron to find vulnerabilities in OpenAI’s systems](https://openai.com/index/partnering-with-hacktron)**  
  OpenAI is partnering with Hacktron to find vulnerabilities, test connections with third-party services, and strengthen defenses with frontier AI.

## Lab Blog: DeepMind
- **[Gemini Omni 1.2 Flash: Fast and cost-effective with longer clips](https://deepmind.google/blog/gemini-omni-12-flash-fast-and-cost-effective-with-longer-clips/)**  
  
- **[Agentic cheminformatics with Google Antigravity](https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity/)**  
  Learn how Google Antigravity and our Cheminformatics Skills accelerate drug discovery workflows, search compounds, and propose novel rigidified macrocycles.
- **[Speeding up planning decisions with AI](https://deepmind.google/blog/speeding-up-planning-decisions-with-ai/)**  
  Google DeepMind and UK government work together to reduce planning assessment times
- **[Gemini 4 Carbon: Our next frontier model](https://deepmind.google/blog/gemini-4-carbon-our-next-frontier-model/)**  
  
- **[Genie 4: A new generation of world simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)**  
  Genie 4: our new world model unlocking unprecedented realism in real-time simulation.

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
- **[Practice Makes Precise: At CoRL, NVIDIA and Partners Reveal How Robots Rehearse Delicate Work in Simulation](https://blogs.nvidia.com/blog/robotics-simulation-advancements-corl/)**  
  Simulation, which has long been the proving ground for robots learning to walk, roll and hop, is now helping researchers teach robots tasks that require a finer touch: aligning gears, connecting cables and assembling small components.  The shift from
- **[NVIDIA Announces New Planned Investments in Korean Startups at the MSIT-NVIDIA AI Startup Partnership Forum](https://blogs.nvidia.com/blog/korean-startup-investments-msit/)**  
  Korea’s Ministry of Science and ICT and NVIDIA hosted the MSIT-NVIDIA AI Startup Partnership Forum at COEX. Representatives from the Ministry of Science and ICT and NVIDIA met with over 20 Korean startups across foundation models, physical AI, AI inf
- **[Korea Advances Physical AI Across Industries With NVIDIA](https://blogs.nvidia.com/blog/korea-physical-ai-ecosystem/)**  
  Tapping into the country’s strengths in manufacturing and engineering, NVIDIA is helping advance Korea’s physical AI ecosystem. The country’s industry leaders are applying accelerated computing, AI and simulation to everything from semiconductor manu
- **[Korea’s AI Ecosystem Advances and Secures Agentic AI With NVIDIA](https://blogs.nvidia.com/blog/korea-secure-agentic-ai/)**  
  As AI agents take on more work, they need capable open models and security that advances alongside them. Hyundai Motor Group is exploring NVIDIA NemoClaw blueprints and the NVIDIA OpenShell runtime, while AIM Intelligence is integrating its Starfort 
- **[From Chips to Skills, NVIDIA and Korea Expand Sovereign AI Collaboration](https://blogs.nvidia.com/blog/korea-sovereign-ai-collaboration/)**  
  NVIDIA and Korea’s Ministry of Science and ICT (MSIT) are expanding their collaboration across the country’s sovereign AI ecosystem, from AI semiconductors and data center infrastructure to talent, startups, models, agents and security. The collabora

## Lab Blog: NVIDIA Technical Blog
- **[Make a Robot Arm Feel Weightless with NVIDIA Holoscan 5](https://developer.nvidia.com/blog/make-a-robot-arm-feel-weightless-with-nvidia-holoscan-5/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/featured-image-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="featured-image" width
- **[Speed Up Image Generation with FLUX 3 Image Klein on NVIDIA Blackwell GPUs](https://developer.nvidia.com/blog/speed-up-image-generation-with-flux-3-image-klein-on-nvidia-blackwell-gpus/)**  
  <img alt="Two generated images of a red fox beside a moss-covered fallen tree in an autumn forest." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/techblog-5893-article-kix
- **[Accelerating Reinforcement Learning Weight Refit with the Reshard Collective](https://developer.nvidia.com/blog/accelerating-reinforcement-learning-weight-refit-with-the-reshard-collective/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="338" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/green-cube.webp" style="display: block; margin-bottom: 5px; clear: both;" title="green-cube" width="600" />During
- **[Configure, Certify, and Operate Kubernetes GPU Clusters with NVIDIA DSX OS](https://developer.nvidia.com/blog/configure-certify-and-operate-kubernetes-gpu-clusters-with-nvidia-dsx-os/)**  
  <img alt="Glowing green modular cube with gauge, clock, and gear icons on a black background." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/dsx-os-cluster-readiness-featu
- **[Five Ways NVIDIA Co-Design Maximizes the Value of Every Byte in the AI Factory](https://developer.nvidia.com/blog/five-ways-nvidia-co-design-maximizes-the-value-of-every-byte-in-the-ai-factory/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image5-1-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image5" width="768" />In an

## GitHub Trending (AI, new repos)
- **[AstralBeneathSilver/Deadline-resp-Tracker-AI](https://github.com/AstralBeneathSilver/Deadline-resp-Tracker-AI)**  
  ★ 59 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[kokoc30/Auto-Stitch](https://github.com/kokoc30/Auto-Stitch)**  
  ★ 49 — AI-powered video editing platform for transforming long-form content into short, engaging videos. Public product showcase.
- **[mannanloomba/PayGuard](https://github.com/mannanloomba/PayGuard)**  
  ★ 22 — AI-powered payment safety assistant that detects suspicious activity, analyzes UPI QR codes, extracts bill details, and provides smart spending insights.
- **[ctianye/CodeSlice](https://github.com/ctianye/CodeSlice)**  
  ★ 13 — Local-first AI code-reading desktop app with navigable source citations and human-approved actions.
- **[DeepakSingh98/qwenlab](https://github.com/DeepakSingh98/qwenlab)**  
  ★ 9 — Six small transformers compiled into Qwen3.5-9B, trained in its own forward passes. Qwen runs the experiments.
- **[byte-od/mixture-of-scars](https://github.com/byte-od/mixture-of-scars)**  
  ★ 5 — Breaking the barrier between LLMs and hardware. Mixture of Scars (MoS) static weight compression & SCache O(1) constant KV-cache replacement.
- **[big-data-team/ai-course](https://github.com/big-data-team/ai-course)**  
  ★ 3 — AI Agents Engineer Specialization / Practical AI Course
- **[Hrity7/smart-course-recommendation-system](https://github.com/Hrity7/smart-course-recommendation-system)**  
  ★ 3 — An AI-powered platform for personalized course recommendations and skill-based learning paths.
- **[Pentexa/metargon](https://github.com/Pentexa/metargon)**  
  ★ 2 — METARGON — A crow-inspired AI research project exploring adaptive learning, memory, reasoning, and autonomous discovery.
- **[twpkevin06222/pathoinfer](https://github.com/twpkevin06222/pathoinfer)**  
  ★ 2 — Whole-slide image inference for pathology: stitches tile predictions into seamless slide-level outputs, parquet and low-res image overlay. ONNX/TensorRT runtimes, Triton and vLLM serving. Works with p
