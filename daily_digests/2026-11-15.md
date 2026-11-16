# AI Research Digest — 2026-11-15

## HF Daily Papers (Trending)
- **[The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://huggingface.co/papers/2609.18063)**  
  ⬆ 31 upvotes — Mixture-of-experts (MoE) inference on consumer hardware is bounded by weight memory: a 35B-class model is 19.5GB at 4-bit, and sparsity shrinks the compute per token, not the bytes that must be held. Naive offloading to SSD does not help on its own, because layer N+1's experts must be chosen before 
- **[TradingAgents: Multi-Agents LLM Financial Trading Framework](https://huggingface.co/papers/2412.20138)**  
  ⬆ 166 upvotes — Significant progress has been made in automated problem-solving using
societies of agents powered by large language models (LLMs). In finance,
efforts have largely focused on single-agent systems handling specific tasks or
multi-agent frameworks independently gathering data. However, the multi-agent
- **[PaperOrchestra: A Multi-Agent Framework for Automated AI Research Paper Writing](https://huggingface.co/papers/2604.05018)**  
  ⬆ 3 upvotes — Synthesizing unstructured research materials into manuscripts is an essential yet under-explored challenge in AI-driven scientific discovery. Existing autonomous writers are rigidly coupled to specific experimental pipelines, and produce superficial literature reviews. We introduce PaperOrchestra, a
- **[TokenEconomizer: Experience-Driven Black-Box Cost Control for Coding Agents](https://huggingface.co/papers/2610.22732)**  
  ⬆ 16 upvotes — Advances in frontier coding agents have sharply increased the token costs of AI-assisted software engineering. Their token efficiency is typically evaluated on isolated tasks, whereas real-world developers use them to continuously build, update, and maintain large-scale projects. This mismatch motiv
- **[Harness^2: Recursive Agent Harnessing for an Open World](https://huggingface.co/papers/2610.14224)**  
  ⬆ 70 upvotes — LLM agents' capabilities depend not only on their underlying models but also on their execution harnesses. Recursive self-improvement (RSI) offers a promising approach to automatically evolve these harnesses. However, deploying RSI in open-world settings still faces two critical challenges. First, o
- **[Learning Heterogeneous Tactile Representation for General Dexterous Manipulation](https://huggingface.co/papers/2611.12806)**  
  ⬆ 104 upvotes — Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering ir
- **[Efficient Memory Management for Large Language Model Serving with
  PagedAttention](https://huggingface.co/papers/2309.06180)**  
  ⬆ 77 upvotes — High throughput serving of large language models (LLMs) requires batching
sufficiently many requests at a time. However, existing systems struggle
because the key-value cache (KV cache) memory for each request is huge and
grows and shrinks dynamically. When managed inefficiently, this memory can be

- **[MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights and Activations](https://huggingface.co/papers/2611.10649)**  
  ⬆ 30 upvotes — Weight-activation quantization can reduce the memory and compute cost of neural-network inference, but recent methods often require expensive optimization and architecture-specific propagation of basis transforms across layers. We introduce MACaQ, an MXFP4 W4A4 post-training quantization method that
- **[Kronos: A Foundation Model for the Language of Financial Markets](https://huggingface.co/papers/2508.02739)**  
  ⬆ 65 upvotes — The success of large-scale pre-training paradigm, exemplified by Large
Language Models (LLMs), has inspired the development of Time Series Foundation
Models (TSFMs). However, their application to financial candlestick (K-line)
data remains limited, often underperforming non-pre-trained architectures
- **[e-means: outperforming k-means (in one-tenth the epochs)](https://huggingface.co/papers/2611.09501)**  
  ⬆ 14 upvotes — Lloyd's k-means algorithm is a long-running standard for clustering, with applications in data analysis, retrieval, quantization and data curation. In this paper, we introduce an exponential moving average optimization procedure for k-means with mini-batch updates, powered by modern deep learning ma

## HF Daily Papers (Today, by Upvotes)
- **[No papers indexed yet for 2026-11-15 (HF submissions can lag up to 14 days behind arXiv)]()**  
  

## arXiv (cs.AI/cs.LG/cs.CL, recent)
- **[AmbiSteer: Selectively Eliciting Ambiguity-Aware Responses in Vision-Language Models](https://arxiv.org/abs/2611.17900v1)**  
  Vision-language models (VLMs) often exhibit overconfidence, providing firm answers even when visual evidence is insufficient. A prominent case is referential ambiguity in Visual Question Answering (VQA), where multiple entities in an image are plausible referents of a question. Addressing such cases
- **[More Genes, Faster Inference: Efficient Large-Panel Spatial Transcriptomics Prediction from Histology](https://arxiv.org/abs/2611.17899v1)**  
  Spatial transcriptomics (ST) prediction from histology aims to infer spatially resolved gene expression profiles directly from tissue images. This is a challenging problem that is currently often addressed with complicated model architectures, additional inputs, and complicated training procedures, 
- **[Hierarchical Bayesian physics-augmented neural networks for populations of hyperelastic laws: specimen variability and uncertainty from scarce, noisy data](https://arxiv.org/abs/2611.17892v1)**  
  The hyperelastic law of a material such as soft tissue differs between specimens, and often only a few specimens can be tested. Physics-augmented neural networks (PANNs) learn such laws from data without a prescribed functional form while keeping them physically admissible, and Bayesian versions of 
- **[Quantum Graph Neural Networks: Architectures, Trainability, and Applications](https://arxiv.org/abs/2611.17886v1)**  
  Quantum graph neural networks (QGNNs) apply parametrized quantum circuits to graph-structured data, with the aim of overcoming limits of classical graph neural networks in scalability, expressivity, and long-range information flow. Since the first Hamiltonian-based model in 2019, the field has produ
- **[Securing Multi-Agent Systems by Design](https://arxiv.org/abs/2611.17883v1)**  
  Multi-agent systems solve complex tasks by decomposing them into subtasks, delegating the subtasks to agents, and aggregating the agents' responses using an aggregation rule. Malicious agents can manipulate the final solution by providing malicious responses to their assigned subtasks. In this paper
- **[Photogrammetric 3D Model-Based Animal Behavior Classification](https://arxiv.org/abs/2611.17881v1)**  
  Video-based behavior estimation is often implemented end-to-end from image sequences. We advocate a two-stage alternative: reconstruct 3D body and object geometry before classifying behavior. This makes ambiguities of the ill-posed 2D-to-3D inverse problem explicit and potentially correctable. We de
- **[Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents](https://arxiv.org/abs/2611.17880v1)**  
  LLM agents that execute multi-step tool calls must satisfy two objectives simultaneously: completing the user's task (utility) and conforming to domain policies and correctness constraints (safety). These objectives are in tension -- blocking an unsafe action prevents a violation but can leave the a
- **[From Local Prediction Error to Final Outputs: A Theory of Expert Sharing in Multi-Step Reasoning](https://arxiv.org/abs/2611.17879v1)**  
  Mixture-of-experts (MoE) models can share experts across layers or computational steps, pooling training information from different contexts. This can reduce local prediction error, but multi-step systems are ultimately evaluated by their final outputs. We study when these local gains survive compos
- **[DySENSE: Dynamic Spatiotemporal ENergy Synthesis and Emulation with Satellite Imagery](https://arxiv.org/abs/2611.17878v1)**  
  Cities account for over two-thirds of the world's energy and more than 70% of global carbon dioxide emissions. City energy is essential for achieving the 2050 net-zero target and the UN's Sustainable Development Goals 7 and 11. Although existing studies have made progress, they are limited by data a
- **[Delayed Effects of Temporary Weight Decay in Muon Pretraining](https://arxiv.org/abs/2611.17876v1)**  
  A temporary optimization intervention can increase validation loss when it ends yet reduce it at the final training budget. We demonstrate this with temporary weight decay in Muon-trained decoder-only Transformers with 162M, 405M, 1.4B, and 3.4B parameters. For models up to 1.4B parameters, moving a

## Reddit
- **[[Reddit fetch failed: 403 Client Error: Blocked for url: https://www.reddit.com/r/MachineLearning/top.json?limit=10&t=day]]()**  
  

## Lab Blog: OpenAI
- **[A step toward defining the Standard Model on a lattice](https://openai.com/index/step-toward-defining-the-standard-model)**  
  Explore a candidate nonperturbative lattice definition of the Standard Model and how GPT-6 Astra helped turn the idea into a detailed proof.
- **[Our new blog for science](https://openai.com/index/our-new-blog-for-science)**  
  The OpenAI science blog shares new findings, practical methods, and firsthand accounts from researchers using AI to advance scientific discovery.
- **[Introducing ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet)**  
  Introducing ChatGPT Wallet, a secure way for agents in ChatGPT Work, Codex, and dots to complete purchases with user approval and existing card protections.
- **[Shield helps technicians hand off legacy portal work with OpenAI](https://openai.com/business/customer-stories/shield)**  
  Shield uses OpenAI to help IT technicians hand off work in legacy portals. Its Forge agents navigate systems so technicians can focus on issues needing their judgment.
- **[How Amplitude ships product improvements in 1–2 days with OpenAI](https://openai.com/business/customer-stories/amplitude)**  
  Built primarily on OpenAI models, Amplitude’s proactive product agent, Wave, identifies what to build, helps teams ship changes with coding agents, and measures the impact.

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
- **[AI Day Seoul Brings Together Korea’s Industry Leaders, Startups and Developer Communities](https://blogs.nvidia.com/blog/ai-day-seoul-wrapup/)**  
  Over two days at COEX, more than 2,000 attendees converged for AI Day Seoul, bringing together Korea’s industry leaders, startups and developer communities advancing physical AI and AI agents. At the plenary sessions, Deepu Talla, vice president of r
- **[How AI Is Helping Care Teams Get Patients the Right Care, Sooner](https://blogs.nvidia.com/blog/how-ai-is-helping-care-teams/)**  
  From pediatric research to smart hospitals, AI is helping care teams spend less time on routine tasks and more time with patients.  Health systems and startups are putting it to work across healthcare, from matching patients to clinical trials to sup
- **[A New Dawn in the Cloud: ‘Warhammer 40,000: Dawn of War IV’ Is Coming to GeForce NOW](https://blogs.nvidia.com/blog/geforce-now-thursday-warhammer-dawn-of-war-iv-coming/)**  
  Rally the ranks this GFN Thursday. Warhammer 40,000: Dawn of War IV is coming to GeForce NOW, allowing players to experience the battle for Kronus through cloud gaming. There’s more on the horizon, with NVIDIA DLSS 5 technology coming to War Thunder 
- **[How AI Helps Recyclers Turn Mixed Waste Into Reusable Material](https://blogs.nvidia.com/blog/ai-recycling-startups/)**  
  Vision AI and robotics pick what’s worth recovering out of conveyor belts of used clothing, bottles and mixed recyclables, diverting thousands of tons of materials from landfills.
- **[NVIDIA Expands Open Source Commitment With OpenShell Contribution and New AI Infrastructure](https://blogs.nvidia.com/blog/open-source-openshell-infrastructure/)**  
  Kubernetes, the open source system that manages how applications run across thousands of AI factories, has become the foundation for AI, and the demands on it are only growing. To help meet them, NVIDIA is deepening its commitment to open source at K

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
- **[Igniaemage/Deadline-resp-Tracker-AI](https://github.com/Igniaemage/Deadline-resp-Tracker-AI)**  
  ★ 50 — 📅 AI-powered academic deadline assistant that uses Gemini Vision to extract assignments, exams, projects & submission dates from academic documents, with smart deadline Q&A and Telegram notifications.
- **[rohitjee7022-blip/Anonymous-Campus](https://github.com/rohitjee7022-blip/Anonymous-Campus)**  
  ★ 37 — Anonymous Campus protects student identities while enabling honest campus facility feedback. It uses aggregated ratings and issue tracking to help administrators improve facilities, with BharatCode AI
- **[dharunram-lgtm/Echo_Knowledge](https://github.com/dharunram-lgtm/Echo_Knowledge)**  
  ★ 4 — ECHO Knowledge is a local-first AI-powered knowledge management system for organizing documents, semantic search, grounded AI answers, and interactive knowledge graphs. Built with Tauri, Rust, React, 
- **[hanspeterdietiker/open-agent-skills](https://github.com/hanspeterdietiker/open-agent-skills)**  
  ★ 4 — Discover. Share. Build.
- **[pathbit/AgentDevKit](https://github.com/pathbit/AgentDevKit)**  
  ★ 4 — Repositório com as skills, comandos e outros que agentes de código irão utilizar.
- **[ALANDVO/axiom-station-144](https://github.com/ALANDVO/axiom-station-144)**  
  ★ 2 — Alan Vo | Work in progress: axiom-station-144
- **[phillarmonic/mcpdev](https://github.com/phillarmonic/mcpdev)**  
  ★ 2 — A dummy harness for debugging/CI testing MCPs
- **[sudo-nova-nsac26/sudo-nova-portfolio](https://github.com/sudo-nova-nsac26/sudo-nova-portfolio)**  
  ★ 2 — Sudo Nova’s team portfolio, built with React, showcasing our NASA Space Apps projects, open-source work, and experiments in software engineering, data, and AI.
- **[ALANDVO/tensor-hub-145](https://github.com/ALANDVO/tensor-hub-145)**  
  ★ 2 — Alan Vo | Work in progress: tensor-hub-145
- **[A220man/prism-forge-144](https://github.com/A220man/prism-forge-144)**  
  ★ 2 — Ryan Vo | Work in progress: prism-forge-144
