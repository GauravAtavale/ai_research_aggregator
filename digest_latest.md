# AI Research Digest — 2026-10-27

## HF Daily Papers (Trending)
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 155 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 124 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 30 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 102 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 62 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
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
- **[MOSS-Image Technical Report](https://huggingface.co/papers/2610.23374)**  
  ⬆ 105 upvotes — Recent closed-source image generation systems can produce diverse visual content from simple compositions to information-dense graphics, yet open-weight text-to-image models still struggle with dense text and intricate layouts. To narrow this gap, we introduce MOSS-Image, an open generation system t
- **[Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training](https://huggingface.co/papers/2610.05416)**  
  ⬆ 23 upvotes — Natively training joint video-audio generation models at higher resolutions empowers them to learn richer visual details and sharper motion dynamics. However, full attention incurs quadratic cost and, as resolution increases, spreads attention over increasingly redundant tokens, diluting learning si
- **[Work Agents: Systems, Capabilities, and Optimization](https://huggingface.co/papers/2610.35845)**  
  ⬆ 103 upvotes — As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish delegated work. To addres

## HF Daily Papers (Today, by Upvotes)
- **[Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for Tool-Use Agents](https://huggingface.co/papers/2610.33568)**  
  ⬆ 336 upvotes — Successful tool-use trajectories are not necessarily useful supervision. Even successful interactions may underrepresent multi-step dependencies or contain actions that are unjustified by the information visible to the agent at decision time. We identify two coupled requirements for effective trajec
- **[Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution](https://huggingface.co/papers/2610.32285)**  
  ⬆ 264 upvotes — LLM agents are increasingly used to solve real-world problems, and their effectiveness depends on both the underlying models and the harnesses that support their operation. However, most existing benchmarks focus on model capabilities and overall agent performance, with limited attention to the eval
- **[StreamVibe: Proactive Video Agents for Evolving User Intent](https://huggingface.co/papers/2610.34662)**  
  ⬆ 246 upvotes — Vision-language models are shifting from offline passive understanding toward online proactive interaction. However, prevailing methods largely rely on explicit requests while miss the implicit user intent (e.g., "where should I click next?" while a user navigate a website), meanwhile fail to update
- **[DynaFlow: Learning Free-Form Multi-Agent Orchestration](https://huggingface.co/papers/2610.34467)**  
  ⬆ 189 upvotes — Multi-agent systems often rely on predefined collaboration structures, limiting their ability to adapt to diverse task requirements. We introduce DynaFlow, a framework that integrates free-form executable workflow synthesis into the action space of the main agent. The agent decides when collaboratio
- **[InteractiveWorld: A Verifiable Human-Centric Environment for Building Better Interactive MLLM Assistants](https://huggingface.co/papers/2610.33966)**  
  ⬆ 113 upvotes — People have long dreamed of an assistant that is always there to guide them and remind what they forget, from new dishes to lost keys. Powered by multimodal large language models (MLLMs), egocentric AI assistants on wearable devices are bringing this dream within reach: they see what the user sees a
- **[Work Agents: Systems, Capabilities, and Optimization](https://huggingface.co/papers/2610.35845)**  
  ⬆ 103 upvotes — As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish delegated work. To addres
- **[Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning in LLM Agents](https://huggingface.co/papers/2610.33956)**  
  ⬆ 49 upvotes — Continual learning is the ability of LLM agents to improve over time by acquiring, refining, and applying knowledge from experience while retaining useful prior knowledge. It is essential for agents learning over long time horizons, yet current evaluations largely assess individual task performance 
- **[WorldCast: World-Consistent Character Video Generation with Large-Angle Camera Control](https://huggingface.co/papers/2610.33135)**  
  ⬆ 46 upvotes — Precise camera control is essential for cinematic character video generation, yet existing methods struggle to follow large-angle trajectories with combined rotation, translation, and radius variation from arbitrary initial azimuths. Such viewpoint changes also reveal character regions unseen in the
- **[Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion](https://huggingface.co/papers/2610.34415)**  
  ⬆ 42 upvotes — Spatial audio authoring coordinates source decisions with soundfield synthesis. For editing, plans specify what to change and retain, while reference audio supplies further acoustic detail. We present AMBIT, a unified framework for native First-Order Ambisonics (FOA) generation and editing with thre
- **[AV-FABLE: Audio-Visual Manipulation Forensics in Long-Form Videos](https://huggingface.co/papers/2610.33413)**  
  ⬆ 38 upvotes — Localized AI manipulations in long-form videos often affect brief events within otherwise authentic content, making video-level classification insufficient for forensic analysis. Existing audio-visual deepfake benchmarks largely focus on short talking-head clips, while long-form temporal forensics r

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[Dense Representation Learning and Differentiable Shape Modeling for Spine Landmark Detection](https://arxiv.org/abs/2610.36951v1)**  
  Spine landmark detection from spinal X-ray is a key step for estimating spine deformation severity, for building biomechanical models, and for pre-operative planning. We reframe anatomical landmark detection as a pixel-level contrastive representation learning problem, matching dense pixel embedding
- **[DCKV: Learned Transform Coding of the Prompt KV Cache in Hybrid Language Models](https://arxiv.org/abs/2610.36950v1)**  
  Hybrid language models keep a key-value (KV) cache only in their few full-attention layers, but this cache is still the part of a prompt's state that grows with the prompt and that must be stored or moved to reuse it. We present DCKV, a differentiable codec for the KV cache and the first KV-cache co
- **[Self-Keyed In-Parameter Memorization for External Memory-Free Dialogue Recall in Frozen Language Models](https://arxiv.org/abs/2610.36948v1)**  
  A large language model maintains conversational content in an external storage that is outside the model and grows as the dialogue continues. This work assumes an environment where a language model has no external memory and no prior knowledge of the future question or its answer. The motivation is 
- **[Beyond QASecClaw: Agent Scaling, Verifier Feedback, and Evidence Reliability in Software Assurance](https://arxiv.org/abs/2610.36947v1)**  
  Can additional specialist language-model contexts improve software assurance when deterministic tool evidence is already available? We study this question through five experiments spanning authored Java warning controls, OWASP Benchmark assessment, Defects4J test generation, SV-COMP assertion verdic
- **[Algorithmic Monoculture in Machine Learning-based Site-Specific Fertilizer Recommendation](https://arxiv.org/abs/2610.36941v1)**  
  Machine learning recommendations are often evaluated one model at a time, despite deployment across interconnected decision makers. For continuous NPK fertilizer prescriptions, correlated errors can aggregate across farms and generate systemic costs. A model of shared and farm-specific recommendatio
- **[TDLM: Adaptive Temporal Integration for Diffusion Language Models](https://arxiv.org/abs/2610.36940v1)**  
  Masked diffusion language models repeatedly compute representations for unresolved tokens, but conventional denoisers do not explicitly retain these representations for reuse across steps. We introduce Temporal Self-Conditioning Diffusion Language Model (TDLM), which lets each unresolved position at
- **[JevRec: Linguistic Encoding with Jev-like Decision Modeling for LLM-based Generative Recommendation](https://arxiv.org/abs/2610.36937v1)**  
  Generative recommendation (GR) represents items as semantic identifiers (SIDs) and autoregressively generates the next item's SID from interaction history. However, most methods assign the same SID length to all items despite highly unequal interaction frequencies. This uniform design repeatedly inc
- **[Gaussian Process Bandits for Constraint Black Box Lever Optimization](https://arxiv.org/abs/2610.36935v1)**  
  Optimizing discrete allocation weights across competing segments of a shared budget is a fundamental challenge in resource-constrained, sequential decision-making environments. In practice, this optimization is often hindered by delayed, noisy, and aggregate feedback, alongside strict operational co
- **[Provenance Signatures for Low Rank Adaptations of Image Diffusion Models](https://arxiv.org/abs/2610.36933v1)**  
  Diffusion models have revolutionized the generation of realistic artificial images. Efficient techniques such as Low Rank Adaptation (LoRA) can modify these models for particular use cases, making them more diverse and widely usable. At the same time, open base models may be adapted to deliver biase
- **[DocXEval: A Systematic Evaluation of Explainability in Multimodal Document Understanding](https://arxiv.org/abs/2610.36929v1)**  
  Multimodal transformer models have driven unprecedented performance breakthroughs in modern document understanding. However, the inherent black-box nature of these models remains a major obstacle to their safe deployment in high-stakes sectors. Despite significant progress in explainability for visi

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Retell uses OpenAI models to help power 100M monthly calls](https://openai.com/index/retell-ai)**  
  GPT-6 Astra tops Retell’s voice agent benchmark, while Codex helps it reach a $1.6M annual revenue run rate per employee.
- **[OpenAI expands partnership with Oracle to bring its apps to ChatGPT](https://openai.com/index/oracle-apps-in-chatgpt)**  
  OpenAI and Oracle are expanding their partnership to bring business applications and AI agents into ChatGPT and power new Oracle offerings.
- **[How Check Point accelerates vulnerability research with Daybreak](https://openai.com/index/check-point-daybreak)**  
  With OpenAI Daybreak, Check Point speeds up the research behind new security protections, enabling its analysts to turn vulnerability intelligence into customer defenses faster.
- **[Greptile takes bug detection beyond code review with GPT-6 Astra](https://openai.com/index/greptile-code-review-codex-astra)**  
  How Greptile uses GPT-6 Astra to test user workflows, Daybreak to strengthen security, and Codex to reduce rework.
- **[Working with academic communities to build scientific understanding](https://openai.com/index/building-scientific-understanding-with-academic-communities)**  
  OpenAI shares model results on the Kakeya conjecture, Exponential Time Hypothesis, and quantum chromodynamics—and how researchers can verify and build on them.

## Lab Blog: DeepMind
- **[Genie 4: A new generation of world simulation](https://deepmind.google/blog/genie-4-a-new-generation-of-world-simulation/)**  
  Genie 4: our new world model unlocking unprecedented realism in real-time simulation.
- **[Beyond tree cover: mapping the world’s forest types](https://deepmind.google/blog/beyond-tree-cover-mapping-the-worlds-forest-types/)**  
  A global map categorizing every 10-meter patch of land on Earth into distinct forest types.
- **[Accelerating the search for antimicrobial peptides with Google Antigravity](https://deepmind.google/blog/accelerating-antimicrobial-discovery/)**  
  Accelerating the search for novel antimicrobial peptides using Google Antigravity for Science.
- **[Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)**  
  Learn how Google DeepMind and GovTech Singapore uses lightweight on-device Gemma models to intercept conversational scams in private chats with zero cloud data egress.
- **[Developing Gemini 4 Argon responsibly and safely](https://deepmind.google/blog/developing-gemini-4-argon-responsibly-and-safely/)**  
  

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
- **[How AI Is Changing the Pace of Discovery for Millions Living With Dementia](https://blogs.nvidia.com/blog/open-source-ai-tools-cbrain-dementia/)**  
  There are 57 million people worldwide living with dementia today. For the researchers working to help them, the obstacle isn’t a lack of effort — it’s too much data, too few experts to synthesize it and a pace of discovery that can’t keep up with the
- **[Kazakhstan Expands Compute for Its AI Future](https://blogs.nvidia.com/blog/kazakhstan-ai-compute-ecosystem/)**  
  Kazakhstan’s AI ecosystem is moving from infrastructure plans to deployment.  The shift is visible across the full AI stack — from infrastructure to models to applications. The announcements below — coinciding with a visit to Astana by NVIDIA founder
- **[NVIDIA Unveils Minerva to Bring End-to-End Observability for AI Factories](https://blogs.nvidia.com/blog/minerva-platform-infrastructure/)**  
  Launched today, NVIDIA Minerva is an AIOps platform built to help teams find problems earlier and keep AI factories productive. It brings together telemetry from infrastructure and AI workloads, then applies purpose-built AI models to turn that data 
- **[Cloud Deployment Incoming: ‘Call of Duty: Modern Warfare 4’ Arrives on GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-call-of-duty-modern-warfare-4/)**  
  Lock in and load out this GFN Thursday. Call of Duty: Modern Warfare 4 arrives on GeForce NOW at launch, bringing a new campaign, multiplayer action and DMZ, high-stakes extraction mode to supported devices. The campaign also gets an enhanced look: G
- **[Leading European Financial Services Organizations Embrace Open Models to Build Proprietary Intelligence](https://blogs.nvidia.com/blog/european-financial-services-organizations-open-models-proprietary-intelligence/)**  
  At GTC Berlin, banks, payment companies and financial data providers are showing what production-scale intelligence looks like — built on NVIDIA accelerated computing, powered by open weight models and running on their own infrastructure. Revolut is 

## Lab Blog: NVIDIA Technical Blog
- **[Memory-Enforced GPU Sharing in Kubernetes with NVIDIA CUDA 13.4](https://developer.nvidia.com/blog/memory-enforced-gpu-sharing-in-kubernetes-with-nvidia-cuda-13-4/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/CUDAMemoryKV-768x432.webp" style="display: block; margin-bottom: 5px; clear: both;" title="CUDAMemoryKV" width="7
- **[NVIDIA RTX Spark Powers Neural Rendering and AI Characters in Games](https://developer.nvidia.com/blog/nvidia-rtx-spark-powers-neural-rendering-and-ai-characters-in-games/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image6-2-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image6" width="768" />NVIDI
- **[Fine-Tuning NVIDIA Nemotron to Know Local Rules, Not Just Local Languages](https://developer.nvidia.com/blog/fine-tuning-nvidia-nemotron-to-know-local-rules-not-just-local-languages/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/agentic-promo-nemotron-models-eu-gtc-berlin-press-1600x900-5811620-768x432.png" style="display: block; margin-bot
- **[3 Ways to Boost MoE Inference on NVIDIA DGX Spark](https://developer.nvidia.com/blog/3-ways-to-boost-moe-inference-on-nvidia-dgx-spark/)**  
  <img alt="Abstract green computing cube with layered panels, performance icons, and streams of data on a black background" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/dg
- **[How NVIDIA Minerva Turns Telemetry Chaos Into Peak GPU Yield](https://developer.nvidia.com/blog/how-nvidia-minerva-turns-telemetry-chaos-into-peak-gpu-yield/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/MinervaKV-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="MinervaKV" width="768" />A

## GitHub Trending (AI, new repos)
- **[Cinderubasp/InterviewCopilot-rpocket-team](https://github.com/Cinderubasp/InterviewCopilot-rpocket-team)**  
  ★ 54 — EdTech application designed to bridge the gap between learning and landing your dream job
- **[faraflow/faraflow](https://github.com/faraflow/faraflow)**  
  ★ 49 — Visual builder and execution engine for AI powered organizations
- **[OFat34764e/InterviewCopilot-rpocket-team](https://github.com/OFat34764e/InterviewCopilot-rpocket-team)**  
  ★ 32 — EdTech application designed to bridge the gap between learning and landing your dream job
- **[zidniryi/cutvii](https://github.com/zidniryi/cutvii)**  
  ★ 21 — CutVii - Creative editing. Flexible workflow. On-device AI
- **[lucidrains/attention-contact-planning](https://github.com/lucidrains/attention-contact-planning)**  
  ★ 10 — Implementation of Attention-based Contact Planning, by Junzhe He of ETH Zürich
- **[xAerux/aerus-ezai](https://github.com/xAerux/aerus-ezai)**  
  ★ 7 — EZ AI — Local AI made easy: Windows command center for local AI apps, model library, and coding agents.
- **[sukhee-2626/plot-docs](https://github.com/sukhee-2626/plot-docs)**  
  ★ 5 — A local-first AI office suite for Docs, Sheets, Slides, PDF, Markdown and HTML. Windows, macOS and Linux.
- **[mostwanted7/ygo-agent](https://github.com/mostwanted7/ygo-agent)**  
  ★ 4 — AI Yu-Gi-Oh! players for EDOPro: a headless duel host, pluggable model backends, live coaching and deck training.
- **[eDurphy/QATNN-HFP](https://github.com/eDurphy/QATNN-HFP)**  
  ★ 3 — Local Neural Network Quantized and Trainable On The Fly on CPU
- **[A220man/cobalt-console-ryan-vo](https://github.com/A220man/cobalt-console-ryan-vo)**  
  ★ 2 — Ryan Vo | Work in progress: cobalt-console-ryan-vo
