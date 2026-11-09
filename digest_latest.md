# AI Research Digest — 2026-11-08

## HF Daily Papers (Trending)
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 163 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[VibeVoice Technical Report](https://huggingface.co/papers/2508.19205)**  
  ⬆ 184 upvotes — This report presents VibeVoice, a novel model designed to synthesize
long-form speech with multiple speakers by employing next-token diffusion,
which is a unified method for modeling continuous data by autoregressively
generating latent vectors via diffusion. To enable this, we introduce a novel
con
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 14 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 64 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 67 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**  
  ⬆ 111 upvotes — Frontier open-weight models are increasingly available, but serving them still largely assumes datacenter infrastructure. We present FreeToken, an edge-native MoE serving system that treats a personal machine not as a small GPU, but as a unified, elastic inference platform. FreeToken co-designs the 
- **[Persistent Recursive Worlds Enable Autonomous Software Evolution](https://huggingface.co/papers/2608.10450)**  
  ⬆ 8 upvotes — Complex software systems develop over timescales that exceed the lifespan of any individual coding agent. Most agentic software systems preserve continuity through persistent sessions, memories, managers or shared context. We introduce EvoX Genesis (hereafter, Genesis), which instead makes the softw
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
- **[No papers indexed yet for 2026-11-08 (HF submissions can lag up to 14 days behind arXiv)]()**  
  

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Energy-Based Reasoners: Your Recurrent Reasoner Should Be an Energy-Based Model](https://arxiv.org/abs/2611.08977v1)**  
  Looping is a powerful inductive bias for reasoning. By repeatedly iterating a recurrent block, looped models can scale their effective depth and enable multi-step reasoning in latent space. However, existing looped models are not inherently guided by an explicit measure of progress, making it diffic
- **[Beyond Truncation? Entailment-Licensed Elision and the Limits of Semantic Preservation in LLM Decoding](https://arxiv.org/abs/2611.08975v1)**  
  Instruction-tuned large language models (LLMs) answer at greater length than a request needs. We ask whether a training-free controller inside the decoding loop can remove that surplus while preserving content, judged against the simplest possible baseline: truncating the model's own answer to the s
- **[Phantom Consensus: Measuring Social Reasoning in Multi-Agent LLM Decision-Making](https://arxiv.org/abs/2611.08971v1)**  
  Multi-agent LLM systems increasingly aggregate judgments across model instances, but reasoning about other agents can itself introduce failure. We study a setting in which LLMs shift their public decisions after observing ambiguous social signals while reporting inaccurate estimates of what other ag
- **[PhysioWave-T: Token-Efficient Wavelet Foundation Models for Biosignals](https://arxiv.org/abs/2611.08969v1)**  
  We present PhysioWave-T, a token-efficient wavelet foundation model family for EEG, ECG, and sEMG. Dynamic scale folding recombines J+1 wavelet subbands prior to tokenization, compressing sequence length from (J+1)CS to CS tokens for J levels, C channels, and S temporal patches. Route-specific front
- **[Using an LLM to Tackle Difficult Cases in NER for Nepali Tweets](https://arxiv.org/abs/2611.08967v1)**  
  Named entity recognition (NER) is challenging for social media data in a low-resource language. LLMs often lag behind pretrained language models (PLMs) in NER performance, but they show promise in handling cases that PLMs struggle with. Using a dataset of Nepali tweets, we split the test set into "e
- **[Concordance-Optimal Continuous Music Emotion Estimation: Variance Decomposition, Dual-Branch Temporal Fusion, and Conformal Prediction Intervals](https://arxiv.org/abs/2611.08966v1)**  
  Continuous music emotion recognition (MER) estimates how Arousal and Valence evolve within a song, yet the field's standard metric, pooled frame-level correlation, is dominated by between-song differences and cannot distinguish a model that tracks emotional dynamics from one that only ranks songs by
- **[Accuracy Is Not Value: Choosing Weak Supervisors by What the Student Inherits](https://arxiv.org/abs/2611.08959v1)**  
  Weak supervisors are usually judged by their own errors, but what matters is what a student learns from them. For squared loss and any linear learner shared by all supervisors, we show that a supervisor's value is determined by its errors after they pass through the student's learning operator. Cons
- **[More with Less: Efficient Parallel Scientific Code Translation via an Agent-Skill Workflow](https://arxiv.org/abs/2611.08947v1)**  
  Translating parallel scientific codes between HPC programming frameworks is a critical but labor-intensive task. Existing LLM-based approaches rely on fixed sequential pipelines with undifferentiated repair strategies and correctness criteria that do not match scientific computing practice. We prese
- **[Flex-RSI: Benchmarking Recursive Self-Improvement of Frontier Agents](https://arxiv.org/abs/2611.08946v1)**  
  Frontier language models are increasingly deployed as agents, and how well an agent performs depends not only on its model but also on its harness: the prompts, tools, memory, and control loop through which the model acts. When an agent is applied to a new problem, a natural question is whether it c
- **[Surrogate Quality Score: A Novel Composite Performance Metric for Model Selection](https://arxiv.org/abs/2611.08937v1)**  
  The growing reliance on high-fidelity, state-of-the-art machine learning based models for engineering decision-making necessitates robust and systematic approaches for model selection. While high predictive accuracy at untrained points is a necessary trait in the final model, other attributes such a

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Partnering with Hacktron to find vulnerabilities in OpenAI’s systems](https://openai.com/index/partnering-with-hacktron)**  
  OpenAI is partnering with Hacktron to find vulnerabilities, test connections with third-party services, and strengthen defenses with frontier AI.
- **[Measuring how AI agents handle everyday wet-lab science](https://openai.com/index/measuring-how-ai-agents-handle-wet-lab-science)**  
  OpenAI introduces BioBasicsBench, a 100-task benchmark measuring how well AI agents interpret raw experimental data and handle everyday wet-lab science.
- **[Australian universities are creating AI-native graduates](https://openai.com/index/australian-universities-ai-native-graduates)**  
  Australian universities are expanding access to ChatGPT and bringing AI into teaching and learning to prepare students for an AI-enabled workforce.
- **[Cult.fit builds operational muscle with Codex](https://openai.com/index/cultfit-builds-with-codex)**  
  Cult.fit is using Codex to help teams across functions build tools, move faster, and change how work gets done.
- **[GPT‑6 Cyber: Advancing the frontier of aligned cybersecurity agents](https://openai.com/index/introducing-gpt-6-cyber)**  
  Introducing GPT‑6 Cyber, OpenAI’s cybersecurity model for finding exploitable vulnerabilities and developing fixes, trained to stay within authorized scope.

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
- **[How NVIDIA Open Source Tools Are Helping Researchers Build Next-Generation 6G Networks](https://blogs.nvidia.com/blog/telco-open-source-tools-research-6g-networks/)**  
  A year ago, NVIDIA open sourced its Aerial wireless software, joining Sionna and a broader suite of open source tools for accelerating next-generation 6G network development. Together, they give researchers a foundation for testing ideas, comparing r
- **[Vera Delivers the Best of Both Worlds: Highest Throughput and Fastest Agents](https://blogs.nvidia.com/blog/vera-cpu-highest-throughput-fastest-agents/)**  
  AI agents do more than generate answers. They search for information, query databases, write and test code and take action.  Each of those steps relies on a CPU, with agents moving between GPU reasoning and CPU execution throughout a task.  As busine
- **[Into the Omniverse: How Developers Turn Ideas Into Simulations With Frontier AI Agents](https://blogs.nvidia.com/blog/developers-simulation-frontier-ai-agents/)**  
  Turning a simulation idea into a working application means assembling assets, connecting physics and rendering, and checking that the scene behaves as intended. Developers are combining frontier AI models with NVIDIA Omniverse libraries to help carry
- **[The Wizard of Open Weights: Chris Alexiuk Makes AI Easy With Open Models](https://blogs.nvidia.com/blog/nvidia-life-chris-alexiuk/)**  
  Chris Alexiuk has a simple rule about open source AI: If you believe in it, be loud about it. “We should be shouting about this technology from the rooftops,” said Alexiuk, a Toronto-based senior product research engineer in deep learning at NVIDIA w
- **[More Performance From Every Byte: How Full-Stack Codesign Solves AI’s Memory Challenge](https://blogs.nvidia.com/blog/memory-full-stack-codesign/)**  
  Larger models, longer contexts and agentic applications are increasing GPU memory pressure while supply tightens and prices rise — a trend expected to continue through the near term. NVIDIA works closely with memory partners to rapidly adopt the late

## Lab Blog: NVIDIA Technical Blog
- **[Speed Up Image Generation with FLUX 3 Image Klein on NVIDIA Blackwell GPUs](https://developer.nvidia.com/blog/speed-up-image-generation-with-flux-3-image-klein-on-nvidia-blackwell-gpus/)**  
  <img alt="Two generated images of a red fox beside a moss-covered fallen tree in an autumn forest." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/techblog-5893-article-kix
- **[Accelerating Reinforcement Learning Weight Refit with the Reshard Collective](https://developer.nvidia.com/blog/accelerating-reinforcement-learning-weight-refit-with-the-reshard-collective/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="338" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/green-cube.webp" style="display: block; margin-bottom: 5px; clear: both;" title="green-cube" width="600" />During
- **[Configure, Certify, and Operate Kubernetes GPU Clusters with NVIDIA DSX OS](https://developer.nvidia.com/blog/configure-certify-and-operate-kubernetes-gpu-clusters-with-nvidia-dsx-os/)**  
  <img alt="Glowing green modular cube with gauge, clock, and gear icons on a black background." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/dsx-os-cluster-readiness-featu
- **[Five Ways NVIDIA Co-Design Maximizes the Value of Every Byte in the AI Factory](https://developer.nvidia.com/blog/five-ways-nvidia-co-design-maximizes-the-value-of-every-byte-in-the-ai-factory/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image5-1-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image5" width="768" />In an
- **[How NVIDIA Uses AI Agents to Streamline AI Factory Operations](https://developer.nvidia.com/blog/how-nvidia-uses-ai-agents-to-streamline-ai-factory-operations/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/11/image2-3-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="image2" width="768" />As GP

## GitHub Trending (AI, new repos)
- **[DjibrilM/MagicVoiceAI](https://github.com/DjibrilM/MagicVoiceAI)**  
  ★ 29 —  An offline desktop Text-to-Speech (TTS) studio built with Electron and the Qvac sdk 
- **[AstralBeneathSilver/Deadline-resp-Tracker-AI](https://github.com/AstralBeneathSilver/Deadline-resp-Tracker-AI)**  
  ★ 23 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[mannanloomba/PayGuard](https://github.com/mannanloomba/PayGuard)**  
  ★ 13 — AI-powered payment safety assistant that detects suspicious activity, analyzes UPI QR codes, extracts bill details, and provides smart spending insights.
- **[ctianye/CodeSlice](https://github.com/ctianye/CodeSlice)**  
  ★ 10 — Local-first AI code-reading desktop app with navigable source citations and human-approved actions.
- **[DeepakSingh98/qwenlab](https://github.com/DeepakSingh98/qwenlab)**  
  ★ 9 — Six small transformers compiled into Qwen3.5-9B, trained in its own forward passes. Qwen runs the experiments.
- **[Hrity7/smart-course-recommendation-system](https://github.com/Hrity7/smart-course-recommendation-system)**  
  ★ 3 — An AI-powered platform for personalized course recommendations and skill-based learning paths.
- **[big-data-team/ai-course](https://github.com/big-data-team/ai-course)**  
  ★ 2 — AI Agents Engineer Specialization / Practical AI Course
- **[Pentexa/metargon](https://github.com/Pentexa/metargon)**  
  ★ 2 — METARGON — A crow-inspired AI research project exploring adaptive learning, memory, reasoning, and autonomous discovery.
- **[Sumit-tech01/DevSphere-Community](https://github.com/Sumit-tech01/DevSphere-Community)**  
  ★ 2 — A global developer community to learn, connect, collaborate and build together.
- **[A220man/tensor-studio-144](https://github.com/A220man/tensor-studio-144)**  
  ★ 2 — Ryan Vo | Work in progress: tensor-studio-144
