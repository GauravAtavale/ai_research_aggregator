# AI Research Digest — 2026-09-04

## HF Daily Papers (trending)
- **[BDH-CQ: In-Context Learning with Recurrent Latent Reasoning](https://huggingface.co/papers/2608.09888)**  
  ⬆ 772 upvotes — We introduce BDH-CQ, a reasoning model that combines in-context learning with recurrent latent reasoning. Inputs presented at inference time continuously update the model's recurrent memory; the model then solves a query through iterative computation in a high-dimensional latent space, without verba
- **[FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution](https://huggingface.co/papers/2608.16157)**  
  ⬆ 107 upvotes — Frontier open-weight models are increasingly available, but serving them still largely assumes datacenter infrastructure. We present FreeToken, an edge-native MoE serving system that treats a personal machine not as a small GPU, but as a unified, elastic inference platform. FreeToken co-designs the 
- **[A decoder-only foundation model for time-series forecasting](https://huggingface.co/papers/2310.10688)**  
  ⬆ 39 upvotes — Motivated by recent advances in large language models for Natural Language
Processing (NLP), we design a time-series foundation model for forecasting
whose out-of-the-box zero-shot performance on a variety of public datasets
comes close to the accuracy of state-of-the-art supervised forecasting mode
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 127 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Prime Agent: A Self-Improving RLM Harness](https://huggingface.co/papers/2608.23552)**  
  ⬆ 48 upvotes — Language models are sequential processors, but long-horizon agency requires external information and computation beyond model weights and active context. Prime Agent is an open-source harness for long-horizon evaluation and coding-agent workflows. A persistent IPython REPL follows the Recursive Lang
- **[LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation](https://huggingface.co/papers/2608.30935)**  
  ⬆ 28 upvotes — Embodied navigation requires agents to translate heterogeneous goals and visual observations into actions across tasks, environments, and robot embodiments. Modern vision-language models (VLMs) already encode spatial priors for visual grounding, spatial reasoning, and pointing, but these capabilitie
- **[Apodex 1.1: Scaling Agentic Intelligence for Complex Work](https://huggingface.co/papers/2608.23283)**  
  ⬆ 205 upvotes — General-purpose language models can reason and synthesize knowledge, but complex work also requires sustained interaction with files, information sources, and executable code, together with state maintenance, failure recovery, and verifiable delivery. We call this working capability: sustained, veri
- **[OpenDevin: An Open Platform for AI Software Developers as Generalist
  Agents](https://huggingface.co/papers/2407.16741)**  
  ⬆ 85 upvotes — Software is one of the most powerful tools that we humans have at our
disposal; it allows a skilled programmer to interact with the world in complex
and profound ways. At the same time, thanks to improvements in large language
models (LLMs), there has also been a rapid development in AI agents that

- **[AgentScope 1.0: A Developer-Centric Framework for Building Agentic
  Applications](https://huggingface.co/papers/2508.16279)**  
  ⬆ 68 upvotes — Driven by rapid advancements of Large Language Models (LLMs), agents are
empowered to combine intrinsic knowledge with dynamic tool use, greatly
enhancing their capacity to address real-world tasks. In line with such an
evolution, AgentScope introduces major improvements in a new version (1.0),
towa
- **[Revisiting Local Context for Long-Horizon Streaming 3D Reconstruction](https://huggingface.co/papers/2608.27529)**  
  ⬆ 33 upvotes — Streaming 3D reconstruction from extremely long videos requires estimating camera motion and scene geometry online under bounded memory and computation. Early streaming models achieve causal, bounded-cost inference using finite context buffers or compact recurrent states, yet their estimates often d

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Compile by Training: Turning Natural-Language Specifications into Local Neural Functions](https://arxiv.org/abs/2609.04199v1)**  
  Many recurring text functions are easy to describe but difficult to implement with rules, while calling a large remote model for every input introduces repeated cost, latency, and dependency on a provider. We present compile by training, which turns a natural-language specification into a reusable n
- **[Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints](https://arxiv.org/abs/2609.04198v1)**  
  Language-model judges now gate training data, score generations, and drive leaderboards. The judge is then a measurement instrument, resting on one rarely stated assumption: the same request, sent to the same model name, reads the same tomorrow. We audited that assumption in two preregistered campai
- **[ESPO: Error-Structured Prompt Optimization via Diagnose, Diversify, and Stabilize](https://arxiv.org/abs/2609.04197v1)**  
  Evolutionary prompt optimizers such as GEPA suffer from prompt bloat: each iteration appends rules and caveats, producing prompts up to 3$\times$ longer yet no more accurate. We trace this to three deficiencies - incomplete error observation, limited search diversity, and unreliable selection - and 
- **[Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning](https://arxiv.org/abs/2609.04194v1)**  
  Reasoning traces from chain-of-thought models appear to offer a legible window into how a model arrives at its answer. A growing body of work treats them as such, using LLM judges to diagnose errors, evaluate faithfulness, and provide step-level supervision via process reward models and generative c
- **[One Editor, Many Edits: A Unified Training-Free Framework for Diverse Video Editing](https://arxiv.org/abs/2609.04190v1)**  
  Video editing spans diverse editing paradigms, yet achieving high-quality instruction-guided and subject-guided editing within a single unified framework remains challenging. We introduce EditVid, a training-free framework combining sparse causal memory for local coherence, correspondence-based post
- **[Robust PAC Learning of Concurrent Stochastic Games](https://arxiv.org/abs/2609.04189v1)**  
  We introduce the first Probably Approximately Correct (PAC) learning framework for general-sum concurrent stochastic games (CSGs) with transition uncertainty, while addressing the challenge of Nash equilibrium (NE) existence. Our algorithm maintains data-driven $L^1$ confidence sets over transition 
- **[Seeing Before Synthesizing: VLM-Guided Transition Event Discovery for Weakly-Supervised Dense Video Captioning](https://arxiv.org/abs/2609.04183v1)**  
  Weakly-Supervised Dense Video Captioning aims to localize and describe multiple events in untrimmed videos given only an ordered set of event-level captions per video. Recent work synthesizes auxiliary transition captions via LLM to provide additional vision-language alignment, but these captions la
- **[Knowledge Acquisition During Pre-training? Large Language Models Learn Better With Auxiliary Views](https://arxiv.org/abs/2609.04180v1)**  
  Gaps remain in our understanding of how large language models (LLMs) acquire knowledge during pre-training. We posit that auxiliary views, reformulations of knowledge, are causally helpful for learning. We design controlled experiments to isolate this. First, we confirm that repetition is necessary 
- **[A Computationally Feasible Framework for Causal Probabilistic Explanation](https://arxiv.org/abs/2609.04177v1)**  
  Explaining why a specific outcome occurred, and which inputs deserve the blame or credit, is central to philosophical, scientific, and policy analysis. Existing tools split into two camps. The theory of actual causality (AC) gives principled verdicts, but only for toy-sized models, because computing
- **[Last Translation Benchmark](https://arxiv.org/abs/2609.04173v1)**  
  For scientific progress, we need benchmarks that test the limits of state-of-the-art models, and evaluation methods that inform us about failure cases. As models get stronger, standard benchmarks for machine translation are approaching saturation. Further, automatic translation metrics are unreliabl

## Hacker News
- **[Show HN: TERMy – A fast terminal assistant that does not use LLMs](https://github.com/gioblu/NPC-Forge/blob/main/docs/development.md)**  
  1 points, 0 comments

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Daybreak for Frontline Defenders: $1B to protect essential services](https://openai.com/index/daybreak-for-frontline-defenders)**  
  OpenAI introduces Daybreak for Frontline Defenders. A $1 billion commitment expands access to frontier cyber AI, training, and support for essential services.
- **[Legora reviewed 41 documents in minutes with GPT-6 Astra](https://openai.com/index/legora-financial-statement-review-with-astra)**  
  Legora used GPT-6 Astra to review 41 documents in minutes, find all four planted errors, and improve performance by nearly 40% in this financial-review workflow.
- **[Playco cut manual fixes 50% prototyping games with GPT-6 Astra](https://openai.com/index/playco-game-prototyping-with-astra)**  
  Using GPT-6 Astra, Playco built three themed game prototypes from one grey box foundation and reported 50% fewer manual fixes than with the previous model.
- **[Safety overview: GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra)**  
  GPT-6 Astra is our most capable broadly deployed model and our first to reach the Critical level of cybersecurity capability under our Preparedness Framework.
- **[ATV Big Air Tour turned 3 days of work into 3 hours with ChatGPT](https://openai.com/index/atv-big-air-tour)**  
  ATV Big Air Tour uses ChatGPT Work to speed up marketing, merchandising, and more. It even turned merchandise photos into an inventory website in 15 minutes.

## Lab Blog: DeepMind
- **[Introducing WeatherNext 3, our most advanced and accurate global weather AI model](https://deepmind.google/blog/introducing-weathernext-3-our-most-advanced-and-accurate-global-weather-ai-model/)**  
  
- **[Proactive cyber defense for governments and enterprises](https://deepmind.google/blog/proactive-cyber-defense-for-governments-and-enterprises/)**  
  
- **[Introducing Gemini 3.8 Flash and 3.8 Flash Cyber](https://deepmind.google/blog/introducing-gemini-3-8-flash-and-38-flash-cyber/)**  
  
- **[Introducing agentic video understanding with Gemini](https://deepmind.google/blog/introducing-agentic-video-in-gemini/)**  
  
- **[Gemini Omni 1.1 Flash lets you build with more control](https://deepmind.google/blog/gemini-omni-1-1-flash-lets-you-build-with-more-control/)**  
  

## Lab Blog: Anthropic (unofficial mirror)
- **[Developing Enterprise Frontier Safeguards with our customers](https://www.anthropic.com/news/enterprise-frontier-safeguards)**  
  <article><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><div class="Illustration-module-scss-module__WyGOtq__root Illustration-module-scss-module__WyGO
- **[Improving our alignment and security efforts](https://www.anthropic.com/news/improving-alignment-security-efforts)**  
  <article><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><div class="Illustration-module-scss-module__WyGOtq__root Illustration-module-scss-module__WyGO
- **[Previewing the Model Hardware Standard](https://www.anthropic.com/news/model-hardware-standard-research-preview)**  
  <article><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"></div><div class="page-wrapper"><article><div class=""><div class="Body-module-scss-module__z40yvW__body"><div class="Body-module-scss-module__z40yvW__media-column Body-mo
- **[Expanding our support for scientists](https://www.anthropic.com/news/expanding-support-for-scientists)**  
  <article><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><div class="Illustration-module-scss-module__WyGOtq__root Illustration-module-scss-module__WyGO
- **[Funding better evaluations of AI’s impact on wellbeing](https://www.anthropic.com/news/wellbeing-research-grants)**  
  <article><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><div class="Illustration-module-scss-module__WyGOtq__root Illustration-module-scss-module__WyGO

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
- **[Sparks Fly: NVIDIA Accelerates Local AI at IFA 2026](https://blogs.nvidia.com/blog/local-ai-ifa-next-gen-agents-nv-pair-rtx-spark/)**  
  Frontier intelligence is going local. At IFA 2026, NVIDIA, Microsoft and its partners are teaming up to provide faster inference and new tools that make agents easier to set up and run locally on NVIDIA hardware. New compact NVIDIA RTX Spark Windows 
- **[‘NBA 2K27’ With NVIDIA DLSS 5 Leads 28 New Games Coming to GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-september-2026-games-list/)**  
  September is here with 28 more games streaming on GeForce NOW this month, led by a slam dunk: NBA 2K27 with the NVIDIA DLSS 5 3D-Guided Neural Rendering feature. Through NVIDIA’s close collaboration with Visual Concepts and 2K, DLSS 5 brings a new le
- **[NVIDIA to Acquire Hugging Face](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/)**  
  I’m excited to announce that NVIDIA has agreed to acquire Hugging Face for $12,930,300,000. Together, we will scale Hugging Face’s platform, strengthen its infrastructure and expand access to AI for developers and institutions worldwide. Over the pas
- **[NVIDIA and CrowdStrike Strengthen Agentic Cybersecurity Frontier](https://blogs.nvidia.com/blog/nvidia-crowdstrike-fal-con-2026/)**  
  “We’re at an inflection point in cybersecurity,” Jensen Huang told a sold-out crowd at CrowdStrike’s Fal.Con 2026 in Las Vegas Tuesday. Attacks are now automated. Defense has to be, too.  The NVIDIA founder and CEO joined CrowdStrike CEO and founder 
- **[GeForce NOW Gives Gamers More Ways to Play at Gamescom 2026](https://blogs.nvidia.com/blog/geforce-now-thursday-gamescom-2026/)**  
  NVIDIA’s Gamescom announcements are revealing what’s next for GeForce NOW, with new ways to play, more supported devices and platforms, and even more big PC games headed to the cloud. New NVIDIA DLSS 4.5 technology controls give members more ways to 

## Lab Blog: NVIDIA Technical Blog
- **[Frontier Reasoning Reaches the Edge: How to Deploy and Optimize Models on NVIDIA Jetson](https://developer.nvidia.com/blog/frontier-reasoning-reaches-the-edge-how-to-deploy-and-optimize-models-on-nvidia-jetson/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/image2-3-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image2" width="768" />Runni
- **[How to Carry User Identity Across Federated Kubernetes and AI Platforms](https://developer.nvidia.com/blog/how-to-carry-user-identity-across-federated-kubernetes-and-ai-platforms/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/kai-scheduler-representation-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="kai-sch
- **[NVIDIA PAIR Virtual Inference Router Expands Available Compute on Your Local Network](https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/09/nvidia-pair-virtual-inference-router-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title=
- **[The Modern CUDA Toolbox in Practice: A Step-by-Step Optimization Walkthrough](https://developer.nvidia.com/blog/the-modern-cuda-toolbox-in-practice-a-step-by-step-optimization-walkthrough/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="431" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/08/keyboard_16x9-768x431.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="keyboard_16x9" width="
- **[Co-Designing AI Models Using Speculative Decoding for Faster LLM Inference](https://developer.nvidia.com/blog/co-designing-ai-models-using-speculative-decoding-for-faster-llm-inference/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/07/llm-optimize-deploy-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="llm-optimize-dep

## GitHub Trending (AI, new repos)
- **[JoseAngelSolorzanoLuna/UFO-Cathedral-v6.4-FailSafe-Free-AI](https://github.com/JoseAngelSolorzanoLuna/UFO-Cathedral-v6.4-FailSafe-Free-AI)**  
  ★ 13 — 100% Free, Offline, 8GB RAM Computer-Artificial Intelligence + Formal Safety (Gate + Ledger + Council + Shadow Mode) — Free alternative to $200/mo OpenAI Operator / Perplexity Computer / ClawBot / Cla
- **[AlekseiUL/humanlike](https://github.com/AlekseiUL/humanlike)**  
  ★ 12 — Humanlike — deterministic persona, context, memory and privacy controls for conversational AI agents · Детерминированное поведение ИИ-агентов
- **[lucidrains/ccbp-pytorch](https://github.com/lucidrains/ccbp-pytorch)**  
  ★ 10 — Implementation of the proposed CCBP (Continuous Continual BackProp) in Pytorch
- **[PanomaAI/panoma](https://github.com/PanomaAI/panoma)**  
  ★ 6 — The local catalog of your projects — intelligent, always learning, for you and your agents
- **[Felix-Theodore-Zeng/eight-market-quant-ai](https://github.com/Felix-Theodore-Zeng/eight-market-quant-ai)**  
  ★ 6 — Eight-market data collection, quantitative analytics, technical structure, and Hermes AI forecasting system
- **[sanketpadhyal/RivoCode-Cli](https://github.com/sanketpadhyal/RivoCode-Cli)**  
  ★ 3 — An autonomous AI coding assistant for developers. Write code, manage files, run terminal commands, and search the web directly from your terminal. Built with TypeScript and Bun as a modern, fast monor
- **[TirupMehta/ModelRegistry](https://github.com/TirupMehta/ModelRegistry)**  
  ★ 3 — ModelRegistry is a community-driven, machine-readable index tracking the state of foundational artificial intelligence.
- **[Saganaki22/obs-dlss5-nr](https://github.com/Saganaki22/obs-dlss5-nr)**  
  ★ 3 — Unofficial DLSS 5 Neural Rendering filter for OBS Studio.  runs NVIDIA DLSS 5 NR (NGX feature 18) on any video source (Game Capture, Media Source, Webcam, …) with a Default / Natural / Cinematic style
- **[Anil-matcha/awesome-claude-fable-5-1](https://github.com/Anil-matcha/awesome-claude-fable-5-1)**  
  ★ 2 — Curated Claude Fable 5.1 use cases, API migration notes, prompting patterns, integrations, demos, and benchmark evidence.
- **[wajidmir23/AI-resume-analyzer](https://github.com/wajidmir23/AI-resume-analyzer)**  
  ★ 2 — AI-powered resume analyzer that calculates ATS scores, extracts skills, detects missing keywords, and provides improvement suggestion
