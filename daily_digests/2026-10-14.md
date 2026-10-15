# AI Research Digest — 2026-10-14

## HF Daily Papers (Trending)
- **[AutoDev: Automated AI-Driven Development](https://huggingface.co/papers/2403.08299)**  
  ⬆ 25 upvotes — The landscape of software development has witnessed a paradigm shift with the
advent of AI-powered assistants, exemplified by GitHub Copilot. However,
existing solutions are not leveraging all the potential capabilities available
in an IDE such as building, testing, executing code, git operations, e
- **[RSI-Anything: Unlocking Recursive Self-Improvement with World Models](https://huggingface.co/papers/2610.13912)**  
  ⬆ 44 upvotes — Recursive self-improvement (RSI) aims to transform interaction experience into persistent improvements, yet external feedback is costly and world-model predictions may become unreliable as policies evolve. We introduce RSI-Anything, a domain-general framework built on JEPA-Anything that uses predict
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 27 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes](https://huggingface.co/papers/2610.18356)**  
  ⬆ 110 upvotes — City-scale 3D grounding is commonly formulated as candidate ranking, which requires precomputed instance proposals and becomes inefficient in large outdoor scenes. We propose Urbex, an agentic vision-language framework that instead casts grounding as active spatial search. Urbex represents a city-sc
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 151 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[YuE2: Unifying Symbolic and Audio Music Generation at Frontier Quality](https://huggingface.co/papers/2609.33757)**  
  ⬆ 236 upvotes — Symbolic models make melody, harmony, rhythm, and form explicit but typically stop before a finished recording; audio models produce complete songs while leaving composition implicit. We introduce YuE2, which unifies symbolic and audio music generation at frontier quality through symbolic planning. 
- **[nanoMuse: An Open-Source Personal Agent for Every Device You Own](https://huggingface.co/papers/2610.08699)**  
  ⬆ 113 upvotes — Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person
- **[Bitnet.cpp: Efficient Edge Inference for Ternary LLMs](https://huggingface.co/papers/2502.11880)**  
  ⬆ 18 upvotes — The advent of 1-bit large language models (LLMs), led by BitNet b1.58, has
spurred interest in ternary LLMs. Despite this, research and practical
applications focusing on efficient edge inference for ternary LLMs remain
scarce. To bridge this gap, we introduce Bitnet.cpp, an inference system
optimiz
- **[Unlimited OCR Works](https://huggingface.co/papers/2606.23050)**  
  ⬆ 93 upvotes — Recently, end-to-end OCR models, exemplified by DeepSeek OCR, have once again thrust OCR into the spotlight. A widely held view is that employing a large language model (LLM) as the decoder allows the model to leverage the prior distribution of language, leading to improved OCR performance. However,
- **[VideoJev: System One Model for Video Understanding and Interaction](https://huggingface.co/papers/2610.18615)**  
  ⬆ 195 upvotes — Visual agents must turn video observations into timely decisions to track progress and choose what to do next. Building on the emerging System One paradigm, we introduce VideoJev, a family of models that cast video understanding and interaction as structured decision tasks. We adapt pretrained multi

## HF Daily Papers (Today, by Upvotes)
- **[Jeva: System One Models from First Principles](https://huggingface.co/papers/2610.18773)**  
  ⬆ 266 upvotes — System one models enable direct, low-latency decision-making. Yet recent practice of predicting an answer from serialized text does not, by itself, respect the structure of a decision problem. We argue that current designs underemphasize four important structural requirements. (i) null-aware: Models
- **[VideoJev: System One Model for Video Understanding and Interaction](https://huggingface.co/papers/2610.18615)**  
  ⬆ 194 upvotes — Visual agents must turn video observations into timely decisions to track progress and choose what to do next. Building on the emerging System One paradigm, we introduce VideoJev, a family of models that cast video understanding and interaction as structured decision tasks. We adapt pretrained multi
- **[Agent-Reflex: Teaching Language Agents to Act Reflectively](https://huggingface.co/papers/2610.17953)**  
  ⬆ 193 upvotes — Large language models have evolved from single-turn chatbots into interactive agents capable of long-horizon reasoning. In real deployments, MCP tool services can return noisy feedback and users may intervene to correct the agent, but existing methods provide limited supervision for reflection learn
- **[Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes](https://huggingface.co/papers/2610.18356)**  
  ⬆ 110 upvotes — City-scale 3D grounding is commonly formulated as candidate ranking, which requires precomputed instance proposals and becomes inefficient in large outdoor scenes. We propose Urbex, an agentic vision-language framework that instead casts grounding as active spatial search. Urbex represents a city-sc
- **[Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](https://huggingface.co/papers/2610.18868)**  
  ⬆ 95 upvotes — Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horizon tasks, largely fo
- **[GreenWAM: A World Foundation Model for Robotics](https://huggingface.co/papers/2610.18774)**  
  ⬆ 82 upvotes — A robot needs a world model that predicts how its actions will change the scene and a policy that chooses those actions. Models are usually built and evaluated for only one of these roles, and every robot records its actions in its own format. We ask whether one robot world model can serve both role
- **[AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards](https://huggingface.co/papers/2610.18860)**  
  ⬆ 79 upvotes — Generating information-rich visual artifacts such as slides, posters, and dashboards as code is appealing because the outputs are structured, editable, and verifiable. Yet code models cannot see how their choices of layout and color come together on the canvas, often limiting spatial planning and ae
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 77 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[TPPO: Tracking-Value PPO For Language Model Reasoning](https://huggingface.co/papers/2610.16794)**  
  ⬆ 72 upvotes — Proximal Policy Optimization (PPO) is widely used in reinforcement learning with verifiable rewards for language-model reasoning. While value evolution along trajectory characterizes relative token-level credit, yet standard critics often fail to track it under sparse terminal rewards. To model this
- **[Vela: User Behavior as Supervision Sparks LLM Intelligence](https://huggingface.co/papers/2610.14709)**  
  ⬆ 69 upvotes — Large language models are increasingly deployed in applications that act on users' long-term behavior histories, from personal assistants to recommendation and advertising systems. These applications demand the user dimension of LLM intelligence: inferring a person's preferences, intent, and likely 

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[ChunkAct: Action Chunking for Agentic Robotics](https://arxiv.org/abs/2610.18874v1)**  
  Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficie
- **[Cepheid: Decoupling Scale from Structure for Cross-Family Motion Completion](https://arxiv.org/abs/2610.18871v1)**  
  Sparse-to-dense motion completion recovers dense mesh motion from sparse vertex displacements. Residual priors trained on one geometry family frequently fail to beat parameter-free harmonic extension off-family. Moreover, cross-family training meets a scaling barrier: residual amplitude varies by mo
- **[What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study](https://arxiv.org/abs/2610.18869v1)**  
  How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and
- **[Tev: Scaling Long-Horizon Agentic Environments with Dense Progress Rewards](https://arxiv.org/abs/2610.18868v1)**  
  Long-horizon agents have drawn growing attention for their ability to work autonomously -- from hours to days -- on economically valuable tasks, a capability essential to automated discovery and recursive self-improvement (RSI). Yet open-source models still struggle on long-horizon tasks, largely fo
- **[Data Free Training of Diffusion Models for Lattice Field Theories](https://arxiv.org/abs/2610.18863v1)**  
  Sampling equilibrium field configurations remains a major computational bottleneck in lattice field theory, motivating the development of generative samplers that can produce independent configurations. Diffusion models are promising for this purpose, but their standard denoising score matching obje
- **[DoubtLess: Training-Free Contrastive Decoding for Efficient Reasoning](https://arxiv.org/abs/2610.18862v1)**  
  Reasoning models achieve strong performance through long chains of thought (CoT), but often spend more tokens than needed to solve a problem. Existing ways to shorten the CoT require additional training for each model, add a fixed steering vector to the model's hidden states, or use decoding heurist
- **[AesCode: Aesthetic Code Generation with Decoupled Cross-Modal Rewards](https://arxiv.org/abs/2610.18860v1)**  
  Generating information-rich visual artifacts such as slides, posters, and dashboards as code is appealing because the outputs are structured, editable, and verifiable. Yet code models cannot see how their choices of layout and color come together on the canvas, often limiting spatial planning and ae
- **[Hybrid Reasoning Agents](https://arxiv.org/abs/2610.18861v1)**  
  How can we build an agent that thinks beyond human language, yet still acts through it in the external environment? Modern LLM agents still reason and interact through text, while latent reasoning offers an efficient internal medium but lacks native tool access and reasoning transparency. We bridge 
- **[Exact Topological Compliance: Generating Persistence-Equivalent Graphs](https://arxiv.org/abs/2610.18856v1)**  
  Persistent homology summarizes the topological evolution of a graph as persistence diagrams (PDs). Generating graphs whose topology matches a target descriptor is increasingly important, yet existing topology-aware generative models rely on soft regularization, producing graphs whose PDs may only be
- **[Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2610.18853v1)**  
  Reinforcement learning with verifiable rewards (RLVR) relies on costly model-generated responses, motivating larger rollout batches and square-root learning-rate scaling. Reported to approximately preserve progress per sample with one optimizer step per rollout, this rule is less understood in pract

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[Amp puts AI agents to work beyond code with OpenAI models](https://openai.com/index/amp-beyond-coding)**  
  See how Amp pushes the frontier of what agents can do with GPT-6 Astra, Ultrafast, GPT-Live-1, and Sign in with ChatGPT.
- **[SentinelOne cuts malware analysis from weeks to hours](https://openai.com/index/sentinelone)**  
  With OpenAI Daybreak, SentinelOne cuts weeks of malware analysis to hours, creating capacity to investigate more threats.
- **[How Third Moment Research runs 10,000 agents for 36+ hours](https://openai.com/index/third-moment-research)**  
  With GPT-6 Astra and GPT-6.1 Sol, Codex, and Daybreak for cybersecurity, this AI lab builds agents that focus for days and improve with use.
- **[How Block is building AI-powered security with OpenAI technology](https://openai.com/index/block-ai-powered-security)**  
  Block is building AI-powered security with OpenAI. Its security team investigates threats faster and proposes patches in minutes.
- **[The EU’s next chapter in AI is agentic](https://openai.com/index/the-eus-next-chapter-in-ai-is-agentic)**  
  New analysis shows how agentic AI adoption is growing across EU enterprises and small businesses—and where deeper use could unlock more value.

## Lab Blog: DeepMind
- **[Google DeepMind and Singapore Government collaborate to build fine-tuned AI model for scam detection](https://deepmind.google/blog/on-device-ai-scam-detection-mddi/)**  
  Learn how Google DeepMind and GovTech Singapore uses lightweight on-device Gemma models to intercept conversational scams in private chats with zero cloud data egress.
- **[Developing Gemini 4 Argon responsibly and safely](https://deepmind.google/blog/developing-gemini-4-argon-responsibly-and-safely/)**  
  
- **[Gemini 4 Argon for Robotics](https://deepmind.google/blog/gemini-4-argon-for-robotics/)**  
  
- **[Gemini 4 Argon: Built to solve your hardest problems](https://deepmind.google/blog/introducing-gemini-4-argon/)**  
  
- **[EmbeddingGemma 2: an open, lightweight multimodal embedding model](https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model/)**  
  

## Lab Blog: Anthropic (unofficial mirror)
- **[Preparing for the 2026 US midterms](https://www.anthropic.com/news/2026-us-midterms)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"></div><div class="page-wrapper"><article><div class="ArticleDetail-module-scss-module__YVTUHa__grid"><div class="ArticleDetail-module-scss-module__YVTUHa__sidebar
- **[Anthropic opens Singapore office and signs MOU with the Government of Singapore](https://www.anthropic.com/news/singapore-office-opening)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><div class="Illustration-module-scss-module__WyGOtq__root Illustration-module-scss-mod
- **[2026 Usage Policy update](https://www.anthropic.com/news/2026-usage-policy-update)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"></div><div class="page-wrapper"><article><div class=""><div class="Body-module-scss-module__z40yvW__body"><p class="Body-module-scss-module__z40yvW__reading-colum
- **[Building on our commitment to American scientific discovery](https://www.anthropic.com/news/genesis-mission-commitment)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"></div><div class="page-wrapper"><article><div class=""><div class="Body-module-scss-module__z40yvW__body"><p class="Body-module-scss-module__z40yvW__reading-colum
- **[Introducing the Anthropic Cyber Mission](https://www.anthropic.com/news/anthropic-cyber-mission)**  
  <article class=""><div class="page-wrapper PostDetail-module-scss-module__UQuRMa__hero"><div class="PostDetail-module-scss-module__UQuRMa__illustrationHeroWrapper"><img alt="Introducing the Anthropic Cyber Mission" class="PostDetail-module-scss-modul

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
- **[NVIDIA Announces New Investments in the UK Startup Ecosystem](https://blogs.nvidia.com/blog/uk-ecosystem-deployment/)**  
  Across industries, the U.K. is putting the full stack to work. The scale of deployment is growing fast, from enterprises transforming their businesses to startups solving some of the planet’s hardest problems. NVIDIA is putting that principle into pr
- **[European Cities Deploy NVIDIA-Powered AI Agents to Run Smarter Urban Operations](https://blogs.nvidia.com/blog/european-cities-agents-urban-operations/)**  
  Keeping a city running means making decisions that affect residents every day — from when to repair a road to how to use energy more efficiently. Across the EMEA region, cities and local software, infrastructure and integration partners are using NVI
- **[All Systems Go: Global PC App Ecosystem Ready for NVIDIA RTX Spark](https://blogs.nvidia.com/blog/local-ai-rtx-spark-laptops-software-updates/)**  
  NVIDIA RTX Spark is a new beginning for the PC — a reinvention combining the capabilities of a gaming PC, a creative studio and a personal AI supercomputer into a single superchip. With up to 128GB of unified memory and 1 petaflop of AI compute, RTX 
- **[NVIDIA Announces New Investments in France’s Startups](https://blogs.nvidia.com/blog/france-ecosystem-agentic-computing/)**  
  Companies in France are deploying agentic computing across industries spanning space, financial services, the public sector and scientific research, demonstrating how the country’s ecosystem has moved from ambition to application. France’s progress s
- **[OCP Global Summit: Amid Ecosystem Adoption, NVIDIA Opens Vera Rubin Architecture to Help Scale AI Factories Worldwide](https://blogs.nvidia.com/blog/ocp-global-summit-vera-rubin-scale-ai-factories/)**  
  As AI factories grow from megawatts to gigawatts, building them takes more than advanced computing. Open standards are helping the industry scale AI infrastructure faster, more efficiently and more reliably. At the Open Compute Project (OCP) Global S

## Lab Blog: NVIDIA Technical Blog
- **[Optimizing Agent Reliability and Tool Calling Efficiency for Chip Design Using NVIDIA NeMo Gym](https://developer.nvidia.com/blog/optimizing-agent-reliability-and-tool-calling-efficiency-for-chip-design-using-nvidia-nemo-gym/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/agentic-workflow-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="agentic-workflow" w
- **[How to Rewrite Apache Spark UDFs for GPU Acceleration with AI Agents](https://developer.nvidia.com/blog/rewrite-apache-spark-udfs-gpu-acceleration-ai-agents/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image2-5-768x432.png" style="display: block; margin-bottom: 5px; clear: both;" title="image2" width="768" />Enter
- **[NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform](https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/01/run-ai-768x432.jpg" style="display: block; margin-bottom: 5px; clear: both;" title="run-ai" width="768" />NVIDIA 
- **[ReplaySSM: Rethinking State Storage for Faster Hybrid-Model Decoding](https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/)**  
  <img alt="A cube assembled from smaller dark blocks, with glowing cyan, pink, yellow, and green sections against a black background." class="webfeedsFeaturedVisual wp-post-image" height="432" src="https://developer-blogs.nvidia.com/wp-content/uploads
- **[5 Steps to Create SimReady Assets for Robotics with Frontier AI Models](https://developer.nvidia.com/blog/5-steps-to-create-simready-assets-for-robotics-with-frontier-ai-models/)**  
  <img alt="" class="webfeedsFeaturedVisual wp-post-image" height="360" src="https://developer-blogs.nvidia.com/wp-content/uploads/2026/10/image6-2.gif" style="display: block; margin-bottom: 5px; clear: both;" title="image6" width="640" />Preparing CAD

## GitHub Trending (AI, new repos)
- **[burlakovmb/NOWA-Bio-Inspired-AI](https://github.com/burlakovmb/NOWA-Bio-Inspired-AI)**  
  ★ 7 — New bio inspired AI
- **[alfera-labs/company-use](https://github.com/alfera-labs/company-use)**  
  ★ 6 — The Open Source AI Co-worker for your whole team. Lives in Slack, API, Whatsapp, web and gets work done.
- **[gautamjajoo/awesome-economics-of-ai](https://github.com/gautamjajoo/awesome-economics-of-ai)**  
  ★ 3 — A curated guide to the costs, markets, adoption, and economic effects of AI.
- **[federicolaterra/knemora](https://github.com/federicolaterra/knemora)**  
  ★ 3 — Open-source, Local-first AI (SI) Second Brain.
- **[DefinetlyNotAI/Ageatopia](https://github.com/DefinetlyNotAI/Ageatopia)**  
  ★ 3 — A local-first multi-agent AI research platform for studying autonomous behavior, survival incentives, emergent dynamics, and learning in isolated simulated worlds.
- **[ydvsamiirrr2007/polar-science-hub](https://github.com/ydvsamiirrr2007/polar-science-hub)**  
  ★ 2 — An AI-powered polar science knowledge hub for discovering research, exploring Arctic and Antarctic science, and creating accessible science outreach content.
- **[icon-lab/FLEX-MRI](https://github.com/icon-lab/FLEX-MRI)**  
  ★ 2 — Official PyTorch implementation of FLEX-MRI: Stochastic Finite-Transition Learning and Exploration for Accelerated MRI Reconstruction
- **[Muguett-DBY/Muguett-DBY](https://github.com/Muguett-DBY/Muguett-DBY)**  
  ★ 2 — Custard: data science, AI, creative tools, and little worlds.
- **[ekkinox/kronk-jev-game](https://github.com/ekkinox/kronk-jev-game)**  
  ★ 2 — Play versus a local AI decision model.
- **[agshukla14/Tic-Tac-Toe-Minimax-AI](https://github.com/agshukla14/Tic-Tac-Toe-Minimax-AI)**  
  ★ 1 — Tic-Tac-Toe game implemented in python using Minimax and Alpha-Beta Pruning
