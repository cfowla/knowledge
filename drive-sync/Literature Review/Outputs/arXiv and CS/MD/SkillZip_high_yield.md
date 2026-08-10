One-page synthesis
Core thesis. Agent skills should not be retrieved and compressed as indivisible documents. SkillZip instead treats source-grounded procedural sections—with explicit interfaces, dependencies, resources, guards, verifiers, and provenance—as the shared unit for retrieval, compression, execution, and maintenance.
What changes conceptually
The paper reframes skill retrieval as executable-context compilation. Sec2Graph creates occurrence-specific section nodes; MotifZip compresses recurring contract-compatible subgraphs into reversible ported macros; PathHydrate retrieves a dependency-closed verifier-reachable subgraph under a context budget; ReZip promotes or revises macros as new skills and execution traces arrive.
Main empirical claim
Across the directly comparable main settings, SkillZip reports the highest task performance and retrieval quality, with a 3.46× compression ratio, 99.2% dependency preservation, 98.7% verifier reachability, and substantially lower delivered context than whole-skill loading.
Most important result. Compression quality depends on preserving executable structure, not merely reducing tokens. At the same rounded 3.46× compression ratio and 1,941-token rendered context, text compression drops dependency preservation to 65.0%, verifier reachability to 60.0%, and reward to 25.5, whereas SkillZip retains 99.2% / 98.7% and reward 33.3.
Principal limitation. Evidence remains benchmark-centered and author-controlled. The paper tests two benchmark families, many perturbations, and six LLM backbones, but the source does not report independent replication or real production skill-library deployment. Contract extraction is a central dependency and is imperfect (macro-F1 91.6; exact match 84.6).
Best use
Architecture and implementation reference for procedural-memory systems, skill retrieval, graph-based context compilation, and reversible compression.
Do not use for
Assuming that graph compression is safe simply because benchmark structural metrics are high, or treating the framework as production-validated.
Bottom line
Build-useful and benchmark-useful. The contract-preserving abstraction is the paper’s durable idea; exact performance numbers need independent reproduction.


Method architecture
Sec2Graph
Segments packages using headings, lists, code, warnings, argument descriptions, tool references, and tests; infers roles; extracts signatures/resources/guards; connects dependencies, verifiers, repairs, weak order, membership, and endpoints; then links contract-compatible occurrences through canonical prototypes without erasing source identity.
MotifZip
Starts from typed signature buckets, grows motifs over dependency/weak-order neighborhoods, counts non-conflicting source occurrences, validates macro contracts, scores positive description-length gain, then greedily rewrites non-overlapping motifs into ported reversible macros.
PathHydrate
Analyzes the task into goal, outputs, capabilities, inputs, domain/profile, and ordered subgoals; fuses section-level and skill-level evidence; connects seeds; repairs required roles and verifier paths; then renders each macro at name, contract, outline, or full-source level.
ReZip
Matches new skill regions against existing macros, buffers residuals, promotes recurring valid residual motifs, and tracks macro expansion/failure/repair evidence. Risk first increases hydration detail; persistent risk can split or retire a macro while retaining source-grounded expansion.

Representation invariant
source skill package
  → occurrence-specific typed sections
  → dependency / verifier / resource / membership edges
  → contract-valid recurring motif
  → reversible macro with typed ports + expansion map
  → task-time dependency-closed hydrated subgraph
  → execution log feeds maintenance

Critical dependency. The safety value of MotifZip and PathHydrate is conditional on correctly extracted contracts. The paper’s corruption study confirms graceful degradation at modest corruption but substantial loss at high corruption.


Implementation takeaways
1. Choose the right atomic unit
If a skill document contains multiple independent operations/verifiers, retrieval should operate below the package level. Preserve occurrence identity even when canonicalizing reusable prototypes.
2. Make contracts first-class
Compression candidates should expose typed inputs/outputs, resource requirements, guards, failure behavior, and verifier hooks. Surface similarity should only be a secondary signal after structural compatibility.
3. Separate hard validity from optimization
Reject motifs that violate boundary clarity, signature stability, dependency closure, or verifier reachability before considering compression gain.
4. Preserve reversible provenance
Every abstraction should retain occurrence-specific source/port maps so a compact macro can be expanded back to the exact source sections.
5. Treat context as a compiled artifact
Retrieve anchors, connect them, repair dependencies/verifiers, then render the smallest sufficient view. Do not simply concatenate top-k snippets or greedily spend the entire budget.
6. Instrument recovery
Log late expansion, fallback, verifier failure, repair cost, and hydration level. A macro that repeatedly needs expansion is evidence that the abstraction is too coarse or unsafe for that task family.
7. Keep structural and sufficiency validation distinct
Graph validity (ports/closure/reachability) is not the same as task sufficiency. The runtime compiler still needs to verify that the selected subgraph covers task anchors and required roles.
8. Benchmark the full lifecycle
Measure active representation size, source storage, construction time, retrieval latency, rendered context, downstream tool calls, verifier failures, and trajectory tokens separately.
