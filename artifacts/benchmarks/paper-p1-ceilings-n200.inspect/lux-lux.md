# Pair `lux-lux` — `paper-p1-ceilings-n200`

[← compact index](../paper-p1-ceilings-n200.inspect.md) · **Download full HTML**: [raw](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) · [`paper-p1-ceilings-n200.inspect.html`](../paper-p1-ceilings-n200.inspect.html)

- eval_run_id: `paper-n200:lux-lux`
- S1=`decision20-lux` · S2=`decision20-lux`
- row status: `completed` · completed=119 · failed_retriable=81

## Examples

### ex-dev-chunk-only-q075970f6eb46

- **example_id**: `dev:chunk-only:q075970f6eb46`
- **state**: `completed`
- **query**: What did Fastenal Company’s leadership say about Fastenal Company’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '10-Q', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=105

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q075970f6eb46:DEF14A:chunk-24` | 1.5621106743751865 |  | 7 |
| 2 | `q075970f6eb46:DEF14A:chunk-17` | 1.502612597201757 |  | 6 |
| 3 | `q075970f6eb46:DEF14A:chunk-39` | 1.4707901475101004 |  | 12 |
| 4 | `q075970f6eb46:DEF14A:chunk-101` | 0.8540447598272327 |  | 28 |
| 5 | `q075970f6eb46:DEF14A:chunk-82` | 0.8437656367172357 |  | 21 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q075970f6eb46`)._

### ex-dev-chunk-only-q0fd4ca04c0a5

- **example_id**: `dev:chunk-only:q0fd4ca04c0a5`
- **state**: `completed`
- **query**: How does Molina Healthcare view the pace of innovation cycles in healthcare delivery and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0fd4ca04c0a5:10-K:chunk-95` | 0.7698605986907359 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 59 |
| 2 | `q0fd4ca04c0a5:10-K:chunk-65` | 0.7530352022756202 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 48 |
| 3 | `q0fd4ca04c0a5:10-K:chunk-49` | 0.7047880733105771 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 40 |
| 4 | `q0fd4ca04c0a5:10-K:chunk-56` | 0.6942299088228039 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 43 |
| 5 | `q0fd4ca04c0a5:10-K:chunk-138` | 0.6873030037396636 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 71 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q0fd4ca04c0a5`)._

### ex-dev-chunk-only-q299865e6e67e

- **example_id**: `dev:chunk-only:q299865e6e67e`
- **state**: `completed`
- **query**: What dependency risks exist for Consolidated Edison due to concentration of revenue in a limited number of service territories or customer segments?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=286

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q299865e6e67e:10-K:chunk-6` | 1.4667148450961507 |  | 4 |
| 2 | `q299865e6e67e:10-K:chunk-16` | 1.4667121828892233 |  | 8 |
| 3 | `q299865e6e67e:10-K:chunk-3` | 1.4468062436973532 |  | 3 |
| 4 | `q299865e6e67e:10-K:chunk-27` | 1.2631911608214876 |  | 12 |
| 5 | `q299865e6e67e:10-K:chunk-285` | 1.2089098580882645 |  | 95 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q299865e6e67e`)._

### ex-dev-chunk-only-q2a401c1edf73

- **example_id**: `dev:chunk-only:q2a401c1edf73`
- **state**: `completed`
- **query**: How often is Exxon Mobil Corporation’s executive compensation program reviewed and updated?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.3176588314705989 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2a401c1edf73:DEF14A:chunk-83` | 0.8827744597014815 |  | # EXECUTIVE COMPENSATION TABLES ## SUMMARY COMPENSATION TABLE FOR 2023 <table><tr><th>Name and Principal Position</th><… |
| 2 | `q2a401c1edf73:DEF14A:chunk-61` | 0.784936013488644 | 1.0 | # OVERVIEW (cont.) ## AWARD DETERMINATION DIRECTLY TIED TO INDIVIDUAL PERFORMANCE Annual performance assessment against… |
| 3 | `q2a401c1edf73:DEF14A:chunk-123` | 0.7409503607762401 | 1.0 | # PAY VERSUS PERFORMANCE Please refer to the Compensation Discussion and Analysis on pages 47 to 69 for a detailed desc… |
| 4 | `q2a401c1edf73:DEF14A:chunk-43` | 0.7150641738469498 | 2.0 | # Table of Contents ## Compensation Committee The Compensation Committee is comprised exclusively of non-employee, inde… |
| 5 | `q2a401c1edf73:DEF14A:chunk-125` | 0.6986753796687312 | 1.0 | # PAY VERSUS PERFORMANCE (cont.) ## 94 ExxonMobil 2024 Proxy Statement # Table of Contents While the charts below sugge… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q2a401c1edf73`)._

### ex-dev-chunk-only-q3a71644741b7

- **example_id**: `dev:chunk-only:q3a71644741b7`
- **state**: `completed`
- **query**: What questions were asked about Conagra Brands’ customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.5157051110116301 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3a71644741b7:Earnings:chunk-77` | 1.859690165301862 | 2.0 | I just wanted to clarify on promotional activity and other types of brand building that you've referenced. How does the… |
| 2 | `q3a71644741b7:Earnings:chunk-67` | 1.0932413199827893 | 1.0 | Maybe I can just follow up on Rob's question from a different angle. And Sean, I'd love to hear your perspective on thi… |
| 3 | `q3a71644741b7:Earnings:chunk-29` | 0.9236648905480859 | 1.0 | Yes, David, sure. Today, in our material as an example, to your point, I shared the consumption trends for our Frozen b… |
| 4 | `q3a71644741b7:Earnings:chunk-61` | 0.811368722014755 | 1.0 | Sean, you have a lot of brands that skew more heavily towards lower-income consumers. You have a lot of brands that ske… |
| 5 | `q3a71644741b7:Earnings:chunk-5` | 0.7551459283568104 |  | [Operator Instructions] Our first question today comes from Andrew Lazar from Barclays. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q3a71644741b7`)._

### ex-dev-chunk-only-q40d417892141

- **example_id**: `dev:chunk-only:q40d417892141`
- **state**: `completed`
- **query**: What investor views emerged on D.R. Horton’s geographic expansion prospects within new U.S. housing markets?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=27

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q40d417892141:Earnings:chunk-26` | 0.551800397325486 |  | <hr />D.R. HORTON, INC. AND SUBSIDIARIES LAND AND LOT POSITION AND HOMES IN INVENTORY HOMEBUILDING SEGMENT |
| 2 | `q40d417892141:Earnings:chunk-5` | 0.5357870546406139 |  | Forward-looking statements in this release include that we are well-positioned to meet changing market conditions with … |
| 3 | `q40d417892141:Earnings:chunk-13` | 0.42474374824258454 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 4 | `q40d417892141:Earnings:chunk-17` | 0.42474374824258454 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 5 | `q40d417892141:Earnings:chunk-21` | 0.42474374824258454 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q40d417892141`)._

### ex-dev-chunk-only-q504aef305d62

- **example_id**: `dev:chunk-only:q504aef305d62`
- **state**: `completed`
- **query**: How did management describe the performance of the China market in Q4 2023?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.5574297578579929 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q504aef305d62:Earnings:chunk-15` | 2.2625988923759213 | 2.0 | Thank you for the question. Let me start with the answer here. Our brand in China is known as [ Shing Baka ] and it upl… |
| 2 | `q504aef305d62:Earnings:chunk-29` | 0.9006714409516865 |  | David, I would start with saying our guidance on margin for next year is progressive margin expansion. And remember, on… |
| 3 | `q504aef305d62:Earnings:chunk-7` | 0.8418892152778521 | 2.0 | Thank you, Laxman, and good morning, everyone. I'm very pleased to discuss our strong Q4 and full fiscal year 2023 perf… |
| 4 | `q504aef305d62:Earnings:chunk-13` | 0.6950884127638679 | 1.0 | I had a question about China, please, which I think we've heard the competitive environment there very intense. And I w… |
| 5 | `q504aef305d62:Earnings:chunk-9` | 0.46483542959146085 |  | Thank you, Rachel. At this time, we'll proceed with our normal Q&A session, which will last until the top of the hour. … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q504aef305d62`)._

### ex-dev-chunk-only-q5bb4a350edd8

- **example_id**: `dev:chunk-only:q5bb4a350edd8`
- **state**: `completed`
- **query**: How has aircraft delivery volume trended across the last four quarters for the F 35 program?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.11305340175787203 · skipped= · n_scored=98

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5bb4a350edd8:10-Q:chunk-85` | 1.3684134160608579 | 1.0 | Yes. So we delivered 5 aircraft in 2023. We would expect that to triple, potentially quadruple, here in 2024. And so we… |
| 2 | `q5bb4a350edd8:10-Q:chunk-41` | 0.9558416423484954 |  | So let me get into the deliveries. Jason, we do have a handful of deliveries we expect in the first half. But for the m… |
| 3 | `q5bb4a350edd8:10-Q:chunk-39` | 0.7136649241023099 |  | Jay, just a quick clarification then one for Jim and sorry if I missed this, but the deliveries that you're expecting f… |
| 4 | `q5bb4a350edd8:10-Q:chunk-11` | 0.707264078613169 |  | I was hoping to lead off with Aero and F-35 in particular, and the margins, number one, that you're looking for in '24 … |
| 5 | `q5bb4a350edd8:10-Q:chunk-63` | 0.5979343946184912 |  | Maybe one clarification and one question. Jay, on F-35, at the end of '24, should we think about there being maybe 120 … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q5bb4a350edd8`)._

### ex-dev-chunk-only-q7b219decf5da

- **example_id**: `dev:chunk-only:q7b219decf5da`
- **state**: `completed`
- **query**: What did Everest Group, Ltd.’s leadership say about Everest Group, Ltd.’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '10-Q', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=138

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7b219decf5da:DEF14A:chunk-136` | 0.9162271327113124 |  | Operator |
| 2 | `q7b219decf5da:DEF14A:chunk-0` | 0.9101964926879527 |  | Operator |
| 3 | `q7b219decf5da:DEF14A:chunk-10` | 0.9101964926879527 |  | Operator |
| 4 | `q7b219decf5da:DEF14A:chunk-104` | 0.9101964926879527 |  | Operator |
| 5 | `q7b219decf5da:DEF14A:chunk-110` | 0.9101964926879527 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q7b219decf5da`)._

### ex-dev-chunk-only-q7ca4de540868

- **example_id**: `dev:chunk-only:q7ca4de540868`
- **state**: `completed`
- **query**: How does Hologic view the pace of innovation cycles in women's health diagnostics and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.11506378074895644 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ca4de540868:10-K:chunk-3` | 0.44094737273884316 |  | # Dear Fellow Stockholders: (cont.) Moving first to the Hologic Global Women's Health Index, a partnership with Gallup,… |
| 2 | `q7ca4de540868:10-K:chunk-32` | 0.436262962097014 | 1.0 | # Our Board's Role and Responsibilities (cont.) ## A Champion for Women's Health We are committed to improving women's … |
| 3 | `q7ca4de540868:10-K:chunk-2` | 0.40092490564691874 |  | # Dear Fellow Stockholders: (cont.) Moving next to Breast Health, the division grew constant currency revenue more than… |
| 4 | `q7ca4de540868:10-K:chunk-57` | 0.36976237842731274 |  | # Executive Officers (cont.) ## MR. ANDERSON ## Division President, Breast and Skeletal Health Solutions <figure descri… |
| 5 | `q7ca4de540868:10-K:chunk-8` | 0.36822770525361187 | 1.0 | # Performance Highlights (cont.) 15.6% WORLDWIDE ORGANIC REVENUE GROWTH EX. COVID-19 15.6% organic growth in constant c… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q7ca4de540868`)._

### ex-dev-chunk-only-q7ff47a7d2a20

- **example_id**: `dev:chunk-only:q7ff47a7d2a20`
- **state**: `completed`
- **query**: How does Consolidated Edison, Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.5634608948312462 · skipped= · n_scored=212

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ff47a7d2a20:10-K:chunk-129` | 1.2018329914445585 | 1.0 | # OUTSTANDING EQUITY AWARDS TABLE (cont.) <table><tr><th></th><th colspan="2">STOCK AWARDS</th></tr><tr><td></td><td>Eq… |
| 2 | `q7ff47a7d2a20:10-K:chunk-164` | 1.0661284452775355 | 2.0 | # Equity Compensation Plan Information <table><tr><th>Plan category</th><th>Number of securities to be issued upon exer… |
| 3 | `q7ff47a7d2a20:10-K:chunk-78` | 0.7796349537941212 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Features of the Executive Compensation Program <table><tr><th>Type</t… |
| 4 | `q7ff47a7d2a20:10-K:chunk-127` | 0.7280799308737552 | 1.0 | # GRANTS OF PLAN-BASED AWARDS TABLE (cont.) <table><tr><th rowspan="2">Name &amp; Principal Position</th><th colspan="4… |
| 5 | `q7ff47a7d2a20:10-K:chunk-189` | 0.6946680281506156 | 2.0 | # APPENDIX D (cont.) ## ARTICLE 2. SHARES SUBJECT TO PLAN AND DURATION (a) Term. The Plan shall continue until 10 years… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q7ff47a7d2a20`)._

### ex-dev-chunk-only-q853c16a74704

- **example_id**: `dev:chunk-only:q853c16a74704`
- **state**: `completed`
- **query**: What did Tapestry’s management say about Tapestry’s margin outlook and initiatives to improve profitability?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.5800690628219334 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q853c16a74704:Earnings:chunk-7` | 1.200635512448199 | 2.0 | Thanks, Joanne, and good morning, everyone. Looking back at our results for the fiscal year, our commitment to discipli… |
| 2 | `q853c16a74704:Earnings:chunk-47` | 1.1318474650587738 | 1.0 | Well, we are building and continue to drive a healthy business. That's been our focus, not only in China, but around th… |
| 3 | `q853c16a74704:Earnings:chunk-35` | 0.9409776062075931 | 2.0 | A very brief add to your specific question as it relates to what's driving gross margin. It's really the structural dri… |
| 4 | `q853c16a74704:Earnings:chunk-0` | 0.7532337860471944 |  | Operator |
| 5 | `q853c16a74704:Earnings:chunk-12` | 0.7532337860471944 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q853c16a74704`)._

### ex-dev-chunk-only-q90faabe2b483

- **example_id**: `dev:chunk-only:q90faabe2b483`
- **state**: `completed`
- **query**: What operational risks related to technology or IT systems has UDR, Inc. highlighted, and how are these managed?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=31

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q90faabe2b483:10-K:chunk-0` | 0.3618501384911422 |  | # Exhibit 99.1 Vision on Wilshire I Los Angeles, CA INVESTOR PRESENTATION UDR® November 2023 Opening GRESB KUAL sector … |
| 2 | `q90faabe2b483:10-K:chunk-3` | 0.3089236592482199 |  | # UDR AT A GLANCE - DIVERSIFIED PORTFOLIO COMPOSITION UDR is diversified across markets and price points to generate ro… |
| 3 | `q90faabe2b483:10-K:chunk-29` | 0.3032685649867439 |  | # DEFINITIONS AND RECONCILIATIONS (cont.) <table><tr><th rowspan="2">In thousands, except per share and unit amounts</t… |
| 4 | `q90faabe2b483:10-K:chunk-2` | 0.30275724979379537 |  | # UDR AT A GLANCE (1)(2) UDR is a full-cycle investment that consistently generates strong total shareholder return ("T… |
| 5 | `q90faabe2b483:10-K:chunk-6` | 0.20557707941877312 |  | # ACCRETIVE CAPITAL ALLOCATION UDR has a track record of being a proficient steward of capital and can utilize various … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q90faabe2b483`)._

### ex-dev-chunk-only-q9ee9b517f484

- **example_id**: `dev:chunk-only:q9ee9b517f484`
- **state**: `completed`
- **query**: What feedback have investors provided regarding Valero Energy Corporation’s refining margin outlook?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=203

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9ee9b517f484:Earnings:chunk-29` | 1.4267356115305754 |  | 10 |
| 2 | `q9ee9b517f484:Earnings:chunk-24` | 1.4185812760060614 |  | 9 |
| 3 | `q9ee9b517f484:Earnings:chunk-41` | 1.1532477540791306 |  | 13 |
| 4 | `q9ee9b517f484:Earnings:chunk-44` | 1.1193786348410282 |  | 14 |
| 5 | `q9ee9b517f484:Earnings:chunk-197` | 1.0531723900728789 |  | ________________________ |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q9ee9b517f484`)._

### ex-dev-chunk-only-qa431f3f55a5e

- **example_id**: `dev:chunk-only:qa431f3f55a5e`
- **state**: `completed`
- **query**: How are scenario analyses conducted by EPAM Systems, Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=252

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa431f3f55a5e:10-K:chunk-4` | 1.230030579490208 |  | 4 |
| 2 | `qa431f3f55a5e:10-K:chunk-63` | 1.0212641714353454 |  | 40 |
| 3 | `qa431f3f55a5e:10-K:chunk-90` | 0.97774908377648 |  | F-1 |
| 4 | `qa431f3f55a5e:10-K:chunk-86` | 0.9521374755577837 |  | 51 |
| 5 | `qa431f3f55a5e:10-K:chunk-78` | 0.9063129588154925 |  | 49 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qa431f3f55a5e`)._

### ex-dev-chunk-only-qaf2d41946676

- **example_id**: `dev:chunk-only:qaf2d41946676`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Occidental Petroleum Corporation for oil price volatility risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=126

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qaf2d41946676:10-K:chunk-124` | 0.6787077031356826 |  | Operator |
| 2 | `qaf2d41946676:10-K:chunk-0` | 0.6753641030293076 |  | Operator |
| 3 | `qaf2d41946676:10-K:chunk-10` | 0.6753641030293076 |  | Operator |
| 4 | `qaf2d41946676:10-K:chunk-100` | 0.6753641030293076 |  | Operator |
| 5 | `qaf2d41946676:10-K:chunk-110` | 0.6753641030293076 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qaf2d41946676`)._

### ex-dev-chunk-only-qb3a6bec7aedc

- **example_id**: `dev:chunk-only:qb3a6bec7aedc`
- **state**: `completed`
- **query**: What exposure to foreign exchange fluctuations did Citizens Financial Group, Inc. disclose and how is Citizens Financial Group, Inc. managing it?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.5800690628219334 · skipped= · n_scored=423

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb3a6bec7aedc:10-K:chunk-306` | 1.7661218788693858 | 2.0 | NOTE 14 - DERIVATIVES In the normal course of business, Citizens enters into derivative transactions to meet the financ… |
| 2 | `qb3a6bec7aedc:10-K:chunk-111` | 1.2653349368500304 | 1.0 | Our principal non-market risks include credit, operational, regulatory, reputational, liquidity and strategic risks. We… |
| 3 | `qb3a6bec7aedc:10-K:chunk-113` | 1.0778667550653542 | 2.0 | Non-Trading Risk Our non-trading banking activities expose us to market risk. This market risk is composed of interest … |
| 4 | `qb3a6bec7aedc:10-K:chunk-315` | 1.0606766097500275 |  | ####Year Ended December 31,## (dollars in millions)##2023##2022##2021 Amount of pre-tax net gains (losses) recognized i… |
| 5 | `qb3a6bec7aedc:10-K:chunk-137` | 1.0273050288498378 |  | ITEM 7A. QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK Quantitative and qualitative disclosures about mark… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qb3a6bec7aedc`)._

### ex-dev-chunk-only-qb7d1dfae8271

- **example_id**: `dev:chunk-only:qb7d1dfae8271`
- **state**: `completed`
- **query**: What guidance was offered on International Flavors & Fragrances Inc.’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.6992148198508501 · skipped= · n_scored=304

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb7d1dfae8271:10-Q:chunk-4` | 1.1138600648219925 | 1.0 | •evaluating the profitability of whether to buy or make an ingredient; •sourcing from local countries with our own proc… |
| 2 | `qb7d1dfae8271:10-Q:chunk-22` | 1.0767246446328638 | 1.0 | Our performance may be adversely impacted if we are not successful in managing our inventory and/or working capital bal… |
| 3 | `qb7d1dfae8271:10-Q:chunk-296` | 0.9430431090007947 |  | ##INTERNATIONAL FLAVORS & FRAGRANCES INC.## By:####/s/ Glenn Richter Name:####Glenn Richter Title:####Executive Vice Pr… |
| 4 | `qb7d1dfae8271:10-Q:chunk-85` | 0.8513109105360622 | 1.0 | ######December 31,#### (DOLLARS IN MILLIONS)####2023######2022 Raw materials##$##779####$##1,073 Work in process####406… |
| 5 | `qb7d1dfae8271:10-Q:chunk-33` | 0.805360284615448 |  | SOURCE: S&P Capital IQ |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qb7d1dfae8271`)._

### ex-dev-chunk-only-qbcda53de470c

- **example_id**: `dev:chunk-only:qbcda53de470c`
- **state**: `completed`
- **query**: Which competitive advantages has Apple emphasized compared to peers?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbcda53de470c:DEF14A:chunk-107` | 1.8178234413242689 |  | Sure. It's a number of things, Richard. It's the -- some things I can't talk about. It's Vision Pro. It's AI and ML. It… |
| 2 | `qbcda53de470c:DEF14A:chunk-37` | 1.640804219807973 |  | Okay, very clear. And then maybe for you and Tim, you guys have been on the leading edge of innovation across hardware,… |
| 3 | `qbcda53de470c:DEF14A:chunk-71` | 1.454544925192339 |  | It's really enabled us to build products that we could not build without doing it ourselves. And as you know, we like t… |
| 4 | `qbcda53de470c:DEF14A:chunk-69` | 1.172577750258697 |  | Very clear. And for my follow-up, I had a philosophical question. So you guys always try to provide the best experience… |
| 5 | `qbcda53de470c:DEF14A:chunk-67` | 0.9211241881965714 |  | If you kind of zoom out and look at what we've done on AI and machine learning and how we've used it, we view AI and ma… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qbcda53de470c`)._

### ex-dev-chunk-only-qd7ede96b88aa

- **example_id**: `dev:chunk-only:qd7ede96b88aa`
- **state**: `completed`
- **query**: What observations were made about TransDigm Group’s market share trends or competitive positioning in the aerospace components sector?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.07132875491150918 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd7ede96b88aa:Earnings:chunk-30` | 0.5278207371135824 |  | # Corporate Governance (cont.) ## 2024 Feedback and Actions (cont.) <table><tr><th>What We Heard</th><th>What We Did</t… |
| 2 | `qd7ede96b88aa:Earnings:chunk-8` | 0.5032950554237187 | 1.0 | # 2025 Annual Meeting of Shareholders (cont.) ## Composition of our Board (cont.) 31 Years of Growth and Improving Marg… |
| 3 | `qd7ede96b88aa:Earnings:chunk-53` | 0.48237869074005923 |  | # Compensation Discussion and Analysis ("CD&A") (cont.) ## 31-Year Overview Over the past thirty-one years, TransDigm h… |
| 4 | `qd7ede96b88aa:Earnings:chunk-52` | 0.4174036463691634 |  | # Compensation Discussion and Analysis ("CD&A") (cont.) ## 2024 Business Highlights (cont.) Executive Compensation Net … |
| 5 | `qd7ede96b88aa:Earnings:chunk-47` | 0.3969543288159811 |  | # Beneficial Ownership of Equity Securities of TransDigm (cont.) <table><tr><th></th><th colspan="4">Amount and Nature … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qd7ede96b88aa`)._

### ex-dev-chunk-only-qddfea8300793

- **example_id**: `dev:chunk-only:qddfea8300793`
- **state**: `completed`
- **query**: How does Chesapeake Energy view the pace of technological advancements in drilling techniques and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=345

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qddfea8300793:10-K:chunk-138` | 1.4679494490236644 |  | 80 |
| 2 | `qddfea8300793:10-K:chunk-180` | 1.4030477982616854 |  | 102 |
| 3 | `qddfea8300793:10-K:chunk-190` | 1.366157462715562 |  | 104 |
| 4 | `qddfea8300793:10-K:chunk-183` | 1.3493317581823068 |  | 103 |
| 5 | `qddfea8300793:10-K:chunk-208` | 1.3067042497283161 |  | 108 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qddfea8300793`)._

### ex-dev-chunk-only-qed0361d5a9ae

- **example_id**: `dev:chunk-only:qed0361d5a9ae`
- **state**: `completed`
- **query**: How does Apple currently project its growth rate based on the latest management commentary?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=83

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qed0361d5a9ae:Earnings:chunk-81` | 0.9423811415880511 |  | Date: August 3, 2023####Apple Inc.## ##By:####/s/ Luca Maestri ######Luca Maestri ######Senior Vice President, Chief Fi… |
| 2 | `qed0361d5a9ae:Earnings:chunk-56` | 0.7892996704513815 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations This section and other pa… |
| 3 | `qed0361d5a9ae:Earnings:chunk-55` | 0.7398881749231594 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 13 |
| 4 | `qed0361d5a9ae:Earnings:chunk-82` | 0.7165483345104974 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 23 |
| 5 | `qed0361d5a9ae:Earnings:chunk-22` | 0.7059418582554957 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 7 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qed0361d5a9ae`)._

### ex-dev-chunk-only-qeeb1c1a41ae3

- **example_id**: `dev:chunk-only:qeeb1c1a41ae3`
- **state**: `completed`
- **query**: What dependency risks exist for DuPont de Nemours, Inc. due to concentration of revenue in a limited number of end-use industries such as automotive or electronics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3629374413984796 · skipped= · n_scored=112

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeeb1c1a41ae3:10-K:chunk-105` | 0.7794669770563871 |  | # Table of Contents Appendix A <table><tr><th rowspan="3">In Millions, Except per Share Amounts (Unaudited)</th><th></t… |
| 2 | `qeeb1c1a41ae3:10-K:chunk-43` | 0.6124695018976312 | 2.0 | # Compensation Discussion & Analysis ## Executive Summary We experienced significant volume pressure throughout 2023 as… |
| 3 | `qeeb1c1a41ae3:10-K:chunk-53` | 0.5546080674080444 | 1.0 | # Compensation Discussion & Analysis (cont.) ## Business Segment <table><tr><th rowspan="2" colspan="3">Metric / Weight… |
| 4 | `qeeb1c1a41ae3:10-K:chunk-4` | 0.4661035088800598 | 1.0 | # Proxy Statement Summary # About DuPont We are a global innovation leader with technology-based materials and solution… |
| 5 | `qeeb1c1a41ae3:10-K:chunk-108` | 0.43861437742447384 | 1.0 | # Reconciliation of "Income (loss) from continuing operations, net of tax" to "Operating EBITDA" (cont.) ## Reconciliat… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qeeb1c1a41ae3`)._

### ex-dev-chunk-only-qf3b87e3d287f

- **example_id**: `dev:chunk-only:qf3b87e3d287f`
- **state**: `completed`
- **query**: How has Bio-Techne Corporation’s leverage (e.g., debt-to-equity) changed over time?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.07132875491150918 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf3b87e3d287f:10-K:chunk-7` | 0.8616715949651577 |  | CONSOLIDATED CONDENSED BALANCE SHEETS (In thousands) (Unaudited) |
| 2 | `qf3b87e3d287f:10-K:chunk-24` | 0.5014223536038884 | 1.0 | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td colspan="5">NI… |
| 3 | `qf3b87e3d287f:10-K:chunk-0` | 0.49285090125616593 |  | Exhibit 99.1 BIO-TECHNE RELEASES THIRD QUARTER FISCAL 2024 RESULTS Minneapolis/May 1, 2024/ Bio-Techne Corporation (NAS… |
| 4 | `qf3b87e3d287f:10-K:chunk-22` | 0.4216011316302836 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 5 | `qf3b87e3d287f:10-K:chunk-14` | 0.3960398573577317 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qf3b87e3d287f`)._

### ex-dev-chunk-only-qf59bea60dc8d

- **example_id**: `dev:chunk-only:qf59bea60dc8d`
- **state**: `completed`
- **query**: How does Aon manage equity award burn rate or share pool availability?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-Q', '10-K', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=145

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf59bea60dc8d:DEF14A:chunk-11` | 1.3418897119326842 |  | 9 |
| 2 | `qf59bea60dc8d:DEF14A:chunk-19` | 1.0608972964102987 |  | 12 |
| 3 | `qf59bea60dc8d:DEF14A:chunk-31` | 1.0383878244645692 |  | 14 |
| 4 | `qf59bea60dc8d:DEF14A:chunk-50` | 0.9313469099471318 |  | 17 |
| 5 | `qf59bea60dc8d:DEF14A:chunk-119` | 0.9196928751929759 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qf59bea60dc8d`)._

### ex-dev-q00e75b32eb34

- **example_id**: `dev:q00e75b32eb34`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has International Flavors & Fragrances Inc.’s ingredients segment profitability trended over recent periods?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q00e75b32eb34`)._

### ex-dev-q01b84969979c

- **example_id**: `dev:q01b84969979c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How many markets were mentioned as now offering ad tier pricing for Disney Plus
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.7063662475919823 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['8-K', 'Earnings', '10-Q', 'DEF14A', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q01b84969979c`)._

### ex-dev-q0346b2bc5a8b

- **example_id**: `dev:q0346b2bc5a8b`
- **state**: `completed`
- **query**: What investor views emerged on Packaging Corporation of America’s geographic expansion prospects within the packaging industry?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9216809842642141 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.3065735963827292 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0346b2bc5a8b:chunk-103` | 0.8343122369201885 |  | The operational and converting cost, that came down pretty nicely in the back half of 2023. I'm just trying to gauge sh… |
| 2 | `q0346b2bc5a8b:chunk-49` | 0.7959652926015615 |  | Got it. And last question is before turning it over. Can you help us just think about what's next for PKG from a growth… |
| 3 | `q0346b2bc5a8b:chunk-87` | 0.7882495258113247 | 1.0 | I mean we're probably spending close to $250 million just in the box plants alone this year. And that's all of the 30 s… |
| 4 | `q0346b2bc5a8b:chunk-13` | 0.7325980191134264 |  | [Operator Instructions] Our first question today comes from Mark Weintraub from Seaport Research Partners. |
| 5 | `q0346b2bc5a8b:chunk-53` | 0.7181058333884378 |  | Our next question comes from George Staphos from Bank of America Securities. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q0346b2bc5a8b`)._

### ex-dev-q03a704904653

- **example_id**: `dev:q03a704904653`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did IBM’s leadership say about IBM’s dividend policy or share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.5831428296492145 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['DEF14A', 'Earnings', '8-K', '10-K', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q03a704904653`)._

### ex-dev-q044bb2c8810c

- **example_id**: `dev:q044bb2c8810c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on EQT Corporation’s geographic expansion prospects within the U.S. natural gas markets?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.5937688939938958 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['8-K', '10-Q', '10-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q044bb2c8810c`)._

### ex-dev-q05bfc5cb3e17

- **example_id**: `dev:q05bfc5cb3e17`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Northern Trust Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=315

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q05bfc5cb3e17:chunk-311` | 1.3217012310938003 |  | 87 |
| 2 | `q05bfc5cb3e17:chunk-14` | 1.3184165371372734 |  | 5 |
| 3 | `q05bfc5cb3e17:chunk-296` | 1.3179184752413247 |  | 82 |
| 4 | `q05bfc5cb3e17:chunk-314` | 1.2635170732688543 |  | 88 |
| 5 | `q05bfc5cb3e17:chunk-23` | 1.2524298474654612 |  | 6 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q05bfc5cb3e17`)._

### ex-dev-q09b8cfa51b60

- **example_id**: `dev:q09b8cfa51b60`
- **state**: `completed`
- **query**: How does CBRE Group, Inc. view the pace of technological innovation in real estate services and its effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=141

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q09b8cfa51b60:chunk-31` | 1.6651013153368335 |  | 10 |
| 2 | `q09b8cfa51b60:chunk-26` | 1.656811564300256 |  | 9 |
| 3 | `q09b8cfa51b60:chunk-40` | 1.4668300482036951 |  | 12 |
| 4 | `q09b8cfa51b60:chunk-53` | 1.3106502127152135 |  | 17 |
| 5 | `q09b8cfa51b60:chunk-137` | 1.2727390715323996 |  | 58 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q09b8cfa51b60`)._

### ex-dev-q0b8d55d58be2

- **example_id**: `dev:q0b8d55d58be2`
- **state**: `completed`
- **query**: What questions were asked about Chubb Limited’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9506817003345661 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.38685280723454163 · skipped= · n_scored=370

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0b8d55d58be2:chunk-20` | 1.398229261351499 |  | 10 |
| 2 | `q0b8d55d58be2:chunk-250` | 1.1304406219577667 | 1.0 | Premiums Net premiums written increased $410 million, or 8.7 percent, and $1,149 million, or 8.6 percent for the three … |
| 3 | `q0b8d55d58be2:chunk-344` | 1.0180464439477652 |  | 101 |
| 4 | `q0b8d55d58be2:chunk-168` | 0.9923589143933554 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – continued (Unaudited) Chubb Limited and Subsidiaries A lapse rate is the p… |
| 5 | `q0b8d55d58be2:chunk-166` | 0.9265996510850065 |  | ##Valuation Technique##Significant Unobservable Inputs######September 30, 2023##########September 30, 2022 ######Ranges… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q0b8d55d58be2`)._

### ex-dev-q0d51e9ef12aa

- **example_id**: `dev:q0d51e9ef12aa`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did leadership measure the installed base of RTX PCs and relate it to AI‑application adoption?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5509858876386381 · gold=['8-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q0d51e9ef12aa`)._

### ex-dev-q0e5327ae1aff

- **example_id**: `dev:q0e5327ae1aff`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What concerns have institutional investors raised regarding regulatory risk?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5=0.38685280723454163 · gold=['Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q0e5327ae1aff`)._

### ex-dev-q0faf9d780cdc

- **example_id**: `dev:q0faf9d780cdc`
- **state**: `completed`
- **query**: How did aeronautics sustainment hours compare with prior year levels?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9639404333166532 · gold=['10-Q', '10-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0faf9d780cdc:chunk-55` | 0.8152690292090924 |  | production. These increases were partially offset by lower net sales of $400 million on the F-35 program due to lower v… |
| 2 | `q0faf9d780cdc:chunk-207` | 0.6611985294596378 |  | 101 |
| 3 | `q0faf9d780cdc:chunk-137` | 0.6566125798934543 |  | ####Aeronautics####MFC####RMS####Space####Total Balance at December 31, 2021##$##187##$##2,090##$##6,759##$##1,777##$##… |
| 4 | `q0faf9d780cdc:chunk-24` | 0.5925671616973474 |  | ####Owned####Leased####Government- Owned####Total Aeronautics##5.5####3.0####14.8####23.3## Missiles and Fire Control##… |
| 5 | `q0faf9d780cdc:chunk-84` | 0.5840838713962448 |  | 54 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q0faf9d780cdc`)._

### ex-dev-q11ef281af9cd

- **example_id**: `dev:q11ef281af9cd`
- **state**: `completed`
- **query**: How does United Rentals select the peer group for benchmarking executive pay?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9840990003623115 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=223

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q11ef281af9cd:chunk-210` | 1.3916411929504624 |  | 94 |
| 2 | `q11ef281af9cd:chunk-206` | 1.3712440110395732 |  | 92 |
| 3 | `q11ef281af9cd:chunk-204` | 1.3550715373263407 |  | 91 |
| 4 | `q11ef281af9cd:chunk-202` | 1.3545470207142543 |  | 90 |
| 5 | `q11ef281af9cd:chunk-173` | 1.3344503630320033 |  | 80 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q11ef281af9cd`)._

### ex-dev-q140516364bb4

- **example_id**: `dev:q140516364bb4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Principal Financial Group’s international expansion prospects?
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.5292991962953502 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['8-K', 'DEF14A', 'Earnings', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q140516364bb4`)._

### ex-dev-q1463bdfd6910

- **example_id**: `dev:q1463bdfd6910`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Equifax’s Workforce Solutions segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q1463bdfd6910`)._

### ex-dev-q1ab49a3f086f

- **example_id**: `dev:q1ab49a3f086f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What outlook was given for Welltower Inc.’s free cash flow generation over the next year?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7426242736819336 · gold=['8-K', 'Earnings', '10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q1ab49a3f086f`)._

### ex-dev-q1cfcd01ac3a1

- **example_id**: `dev:q1cfcd01ac3a1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does GE HealthCare Technologies manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7118306928082477 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q1cfcd01ac3a1`)._

### ex-dev-q1ded233d05aa

- **example_id**: `dev:q1ded233d05aa`
- **state**: `completed`
- **query**: What questions were asked about IDEXX Laboratories’ customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.20803518926146267 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1ded233d05aa:chunk-41` | 1.2315915391849979 | 1.0 | Yes. So with respect to the point-of-care platform launches, we have a very well-defined tried and true method of devel… |
| 2 | `q1ded233d05aa:chunk-19` | 1.1084535121414427 |  | Yes. And then -- and just to add some color to Brian's remarks. Yes, the end-market appears to be stabilized and health… |
| 3 | `q1ded233d05aa:chunk-27` | 1.0061205241426494 | 1.0 | Yes. Just some follow-up commentary on the inVue launch. Customers, I think, very excited to learn more about that, as … |
| 4 | `q1ded233d05aa:chunk-47` | 0.7481334332480623 |  | We will now take a question from Jon Block of Stifel Financial. |
| 5 | `q1ded233d05aa:chunk-35` | 0.6834694038002342 |  | Yes. So let me talk a little bit about inVue and some of the key opinion leader feedback. We've had a number of key opi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q1ded233d05aa`)._

### ex-dev-q1f722f19a821

- **example_id**: `dev:q1f722f19a821`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What answers were given about progress on Clover Vertica installations?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5=0.6309297535714575 · gold=['Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q1f722f19a821`)._

### ex-dev-q1ff3eed25e64

- **example_id**: `dev:q1ff3eed25e64`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did wage inflation trends affect labor costs in park operations
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6855052752796292 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q1ff3eed25e64`)._

### ex-dev-q2173e7c263c1

- **example_id**: `dev:q2173e7c263c1`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Realty Income Corporation for recessionary or downturn risks in the commercial real estate sector?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=171

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2173e7c263c1:chunk-24` | 0.7310402917528922 |  | -9- |
| 2 | `q2173e7c263c1:chunk-20` | 0.7122115820428702 |  | -8- |
| 3 | `q2173e7c263c1:chunk-98` | 0.68578298327091 |  | experience increased costs of financing, make it difficult to refinance debt at attractive rates or at all, and may adv… |
| 4 | `q2173e7c263c1:chunk-131` | 0.665766369357222 |  | -41- |
| 5 | `q2173e7c263c1:chunk-34` | 0.6351355335265475 |  | -11- |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2173e7c263c1`)._

### ex-dev-q238a8429d152

- **example_id**: `dev:q238a8429d152`
- **state**: `completed`
- **query**: How does Dominion Energy view the pace of innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.12750024571574825 · skipped= · n_scored=209

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q238a8429d152:chunk-3` | 0.461058156064807 |  | # Table of Contents (cont.) ## FORWARD-LOOKING STATEMENTS (cont.) <table><tr><th>Dominion Energy</th><th>1</th></tr><tr… |
| 2 | `q238a8429d152:chunk-4` | 0.4320259921043174 | 1.0 | # Dominion Energy R Dominion Energy, headquartered in Richmond, Virginia, is one of the nation's largest producers and … |
| 3 | `q238a8429d152:chunk-6` | 0.42509652159386524 |  | # BUSINESS REVIEW PROCESS (cont.) ## November Dominion Energy initiates a business review to explore value-maximizing s… |
| 4 | `q238a8429d152:chunk-7` | 0.3393356548706611 |  | # BUSINESS REVIEW PROCESS (cont.) ## Sustainability and Our Path to Net Zero In early 2020, we announced our commitment… |
| 5 | `q238a8429d152:chunk-25` | 0.3248074206726734 |  | # Paul M. Dabbar (cont.) ## Qualifications, Attributes and Skills Mr. Dabbar has substantial technology and innovation … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q238a8429d152`)._

### ex-dev-q2451f8377cf4

- **example_id**: `dev:q2451f8377cf4`
- **state**: `completed`
- **query**: What dependency risks exist for Pool Corporation due to concentration of revenue in specific geographic regions or major pool supply distributors?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.515157140670655 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2451f8377cf4:chunk-121` | 0.9478042986432751 | 2.0 | Yes. I think you really -- you have to go deeper than just seasonal and year-round. Garik, I think you got to look at s… |
| 2 | `q2451f8377cf4:chunk-0` | 0.5956739503197965 |  | Operator |
| 3 | `q2451f8377cf4:chunk-102` | 0.5956739503197965 |  | Operator |
| 4 | `q2451f8377cf4:chunk-112` | 0.5956739503197965 |  | Operator |
| 5 | `q2451f8377cf4:chunk-122` | 0.5956739503197965 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2451f8377cf4`)._

### ex-dev-q24d0f908cfe3

- **example_id**: `dev:q24d0f908cfe3`
- **state**: `completed`
- **query**: What guidance was offered on Fox Corporation’s advertising revenue growth targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9278143341459562 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.38685280723454163 · skipped= · n_scored=111

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q24d0f908cfe3:chunk-4` | 0.8240006117583029 |  | # EXECUTIVE SUMMARY (cont.) ## 2023 Annual Meeting of Stockholders <table><tr><th>Date and Time:</th><th>November 17, 2… |
| 2 | `q24d0f908cfe3:chunk-62` | 0.5929310006102094 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS <table><tr><th>Qualitative Performance Factor</th><th>Fiscal 2023 Achievements</… |
| 3 | `q24d0f908cfe3:chunk-0` | 0.4275886331480543 |  | # UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 # SCHEDULE 14A Proxy Statement Pursuant to Se… |
| 4 | `q24d0f908cfe3:chunk-3` | 0.4183737036316859 |  | # TABLE OF CONTENTS (cont.) This proxy statement contains "forward-looking statements" within the meaning of Section 27… |
| 5 | `q24d0f908cfe3:chunk-61` | 0.406660581582936 |  | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Qualitative Element of Annual Incentive Compensation (cont.) <table><… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q24d0f908cfe3`)._

### ex-dev-q25119b32a2f9

- **example_id**: `dev:q25119b32a2f9`
- **state**: `completed`
- **query**: What performance metrics does Snap-on Incorporated use to establish annual cash incentives or bonuses?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9882048111454694 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=21

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q25119b32a2f9:chunk-10` | 1.2432020642656165 |  | <hr /> |
| 2 | `q25119b32a2f9:chunk-12` | 1.2432020642656165 |  | <hr /> |
| 3 | `q25119b32a2f9:chunk-16` | 1.2432020642656165 |  | <hr /> |
| 4 | `q25119b32a2f9:chunk-18` | 1.2432020642656165 |  | <hr /> |
| 5 | `q25119b32a2f9:chunk-6` | 1.2432020642656165 |  | <hr /> |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q25119b32a2f9`)._

### ex-dev-q27a01443f529

- **example_id**: `dev:q27a01443f529`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Fox Corporation’s international or geographic expansion prospects?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.7204246268326864 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['8-K', 'DEF14A', 'Earnings', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q27a01443f529`)._

### ex-dev-q28b06421804c

- **example_id**: `dev:q28b06421804c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Bio-Techne’s executives discuss plans for new product development or expansion for Bio-Techne?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7189324940540128 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q28b06421804c`)._

### ex-dev-q29a452be41cd

- **example_id**: `dev:q29a452be41cd`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Fox Corporation’s cable network programming segment profitability trended over recent periods?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7693267077702551 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q29a452be41cd`)._

### ex-dev-q29d3cb8df822

- **example_id**: `dev:q29d3cb8df822`
- **state**: `completed`
- **query**: How are investors interpreting guidance on SLB’s customer engagement metrics within its oilfield services operations?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9323478402140176 · gold=['Earnings', 'DEF14A', '8-K', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=47

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q29d3cb8df822:chunk-5` | 1.267045474525052 |  | On a year-to-date basis, the Core businesscomprising Reservoir Performance, Well Construction, and Production Systems… |
| 2 | `q29d3cb8df822:chunk-0` | 0.5615016882579106 |  | Exhibit 99 News Release SLB Announces Third-Quarter 2023 Results  Revenue of $8.31 billion increased 3% sequentially a… |
| 3 | `q29d3cb8df822:chunk-34` | 0.5546307889975246 |  | [Chunk Index 35] <table> <tr> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td>… |
| 4 | `q29d3cb8df822:chunk-42` | 0.5043677341591352 |  | <table> <tr> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td></tr> <tr> <td></… |
| 5 | `q29d3cb8df822:chunk-38` | 0.4524404707925339 |  | <table> <tr> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td></tr> <tr> <td></… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q29d3cb8df822`)._

### ex-dev-q2aae5e2ea500

- **example_id**: `dev:q2aae5e2ea500`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Mondelez International’s snack foods segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2aae5e2ea500`)._

### ex-dev-q2c832749ca0b

- **example_id**: `dev:q2c832749ca0b`
- **state**: `completed`
- **query**: What dependency risks exist for Newmont Corporation due to concentration of revenue in a limited number of geographic regions or gold buyers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2c832749ca0b:chunk-209` | 1.3543881355011327 |  | 79 |
| 2 | `q2c832749ca0b:chunk-206` | 1.2918833071621791 |  | 78 |
| 3 | `q2c832749ca0b:chunk-134` | 1.1233896668889118 |  | 41 |
| 4 | `q2c832749ca0b:chunk-71` | 1.085718985459497 |  | 25 |
| 5 | `q2c832749ca0b:chunk-122` | 1.0758661866418389 |  | 38 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2c832749ca0b`)._

### ex-dev-q2d8eb319367a

- **example_id**: `dev:q2d8eb319367a`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did UDR, Inc.’s leadership address potential risks or uncertainties in forward-looking statements for its multifamily property portfolio?
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.5873006284360539 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['8-K', '10-K', 'DEF14A', 'Earnings', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2d8eb319367a`)._

### ex-dev-q2ec971ec73f9

- **example_id**: `dev:q2ec971ec73f9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What was United Rentals’ Cost of Goods Sold (COGS) in the most recent quarter?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7303575739184495 · gold=['8-K', '10-Q', '10-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2ec971ec73f9`)._

### ex-dev-q2fe5769567d7

- **example_id**: `dev:q2fe5769567d7`
- **state**: `completed`
- **query**: How does Align Technology manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.27051296561346355 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2fe5769567d7:chunk-26` | 1.1747758291306822 |  | 10 |
| 2 | `q2fe5769567d7:chunk-68` | 0.9612493091280299 | 2.0 | 1 Includes MSUs vested during the period below 100% of the original grant as actual shares released is based on Align’s… |
| 3 | `q2fe5769567d7:chunk-66` | 0.9499244087175118 | 1.0 | As of September 30, 2023, we expect to recognize $202.1 million of total unamortized compensation costs, net of estimat… |
| 4 | `q2fe5769567d7:chunk-34` | 0.8847961266743635 |  | 12 |
| 5 | `q2fe5769567d7:chunk-39` | 0.8572643245065403 |  | 14 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2fe5769567d7`)._

### ex-dev-q318eb902f451

- **example_id**: `dev:q318eb902f451`
- **state**: `completed`
- **query**: What questions were asked about Franklin Resources, Inc.’s client retention and engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9199642183398656 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q318eb902f451:chunk-9` | 0.8156866419043627 |  | [Operator Instructions] And our first question comes from the line of Bill Katz with TD Cowen. |
| 2 | `q318eb902f451:chunk-17` | 0.7534536209436299 |  | And Bill, I would add one thing you asked about institutional flows in general. We have really worked hard over the las… |
| 3 | `q318eb902f451:chunk-0` | 0.6797878213445209 |  | Operator |
| 4 | `q318eb902f451:chunk-18` | 0.6797878213445209 |  | Operator |
| 5 | `q318eb902f451:chunk-24` | 0.6797878213445209 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q318eb902f451`)._

### ex-dev-q31f6fd1f392c

- **example_id**: `dev:q31f6fd1f392c`
- **state**: `completed`
- **query**: What governance processes are in place for approving changes to Targa Resources Corp.’s compensation policies?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9979470946084208 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '8-K', '10-Q', 'Earnings']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=99

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q31f6fd1f392c:chunk-27` | 1.372863505342615 | 2.0 | # MEETINGS AND COMMITTEES OF DIRECTORS (cont.) ## Compensation Committee The members of our Compensation Committee are … |
| 2 | `q31f6fd1f392c:chunk-55` | 1.1796270238377278 | 2.0 | # OTHER EXECUTIVE COMPENSATION PRACTICES AND POLICIES (cont.) ## Compensation Committee Report Mses. Bowman and Cooksen… |
| 3 | `q31f6fd1f392c:chunk-43` | 1.0543191633878986 | 2.0 | # OUR DECISION MAKING PROCESS (cont.) ## The Role of the Independent Consultant The Compensation Committee has the auth… |
| 4 | `q31f6fd1f392c:chunk-87` | 0.9733789507298615 | 2.0 | # PROPOSAL THREE ADVISORY VOTE ON EXECUTIVE COMPENSATION ## Introduction We are asking our stockholders to provide advi… |
| 5 | `q31f6fd1f392c:chunk-53` | 0.9226110170943691 | 2.0 | # OTHER EXECUTIVE COMPENSATION PRACTICES AND POLICIES (cont.) ## Incentive Compensation Recovery Policy In September 20… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q31f6fd1f392c`)._

### ex-dev-q33197856c996

- **example_id**: `dev:q33197856c996`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Trane Technologies’ quality metric for its HVAC system manufacturing process changed recently?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.742039158611126 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q33197856c996`)._

### ex-dev-q359aee1441c1

- **example_id**: `dev:q359aee1441c1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered regarding annual capital expenditure levels for park expansions and technology
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.5914218405396885 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q359aee1441c1`)._

### ex-dev-q3ef7ce37ae77

- **example_id**: `dev:q3ef7ce37ae77`
- **state**: `completed`
- **query**: How did investors respond to Tapestry, Inc.’s discussion of supply chain risks?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9734136950814526 · gold=['Earnings', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3ef7ce37ae77:chunk-43` | 0.8275788608588365 |  | Our question is from Brooke Roach of Goldman Sachs. |
| 2 | `q3ef7ce37ae77:chunk-9` | 0.7663260649670305 |  | [Operator Instructions] Our first question comes from Bob Drbul of Guggenheim Securities. |
| 3 | `q3ef7ce37ae77:chunk-68` | 0.7541483200512433 |  | Aneesha Sherman - Analysts |
| 4 | `q3ef7ce37ae77:chunk-44` | 0.7460017267921444 |  | Brooke Roach - Analysts |
| 5 | `q3ef7ce37ae77:chunk-74` | 0.7329201085765437 |  | Mark Altschwager - Analysts |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q3ef7ce37ae77`)._

### ex-dev-q3f9446fe3b94

- **example_id**: `dev:q3f9446fe3b94`
- **state**: `completed`
- **query**: How are scenario analyses conducted by American Tower Corporation for risks related to fluctuations in mobile data demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9484971533659527 · gold=['10-K', 'Earnings', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=342

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3f9446fe3b94:chunk-139` | 1.3375369989914037 |  | 75 |
| 2 | `q3f9446fe3b94:chunk-142` | 1.2820489741723602 |  | 76 |
| 3 | `q3f9446fe3b94:chunk-129` | 1.2791892743098523 |  | 70 |
| 4 | `q3f9446fe3b94:chunk-133` | 1.265220764489435 |  | 72 |
| 5 | `q3f9446fe3b94:chunk-3` | 1.258559708028957 |  | 2 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q3f9446fe3b94`)._

### ex-dev-q41a18ce876e2

- **example_id**: `dev:q41a18ce876e2`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Kellanova’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q41a18ce876e2`)._

### ex-dev-q430300b97e2f

- **example_id**: `dev:q430300b97e2f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Ingersoll Rand’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9840990003623115 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=10

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q430300b97e2f:chunk-13` | 0.98 |  | So let's start with where you ended there on the guidance piece. Certainly, I appreciate all the context and help and u… |
| 2 | `q430300b97e2f:chunk-15` | 0.97 |  | Yes, Mike, so maybe I'll kind of give you a perspective here on how we think about it by region first. I would say that… |
| 3 | `q430300b97e2f:chunk-14` | 0.96 |  | Vicente Reynal - Executives |
| 4 | `q430300b97e2f:chunk-25` | 0.95 |  | Yes. Julian, this is Vik. I'll take the first part of your question, and I'll let Vicente probably talk on the margin f… |
| 5 | `q430300b97e2f:chunk-26` | 0.94 |  | Vicente Reynal - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q430300b97e2f`)._

### ex-dev-q44cfaf358c37

- **example_id**: `dev:q44cfaf358c37`
- **state**: `completed`
- **query**: How do global economic or geopolitical trends shape regional market prospects for Molson Coors Beverage Company's alcoholic beverage portfolio?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.41607037852292533 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q44cfaf358c37:chunk-63` | 1.2143001954023753 | 2.0 | Yes. From a -- from an overall portfolio outside of the U.S., Chris, Canada, we do continue to see softness in the beer… |
| 2 | `q44cfaf358c37:chunk-0` | 0.9298794377219834 |  | Operator |
| 3 | `q44cfaf358c37:chunk-104` | 0.9298794377219834 |  | Operator |
| 4 | `q44cfaf358c37:chunk-110` | 0.9298794377219834 |  | Operator |
| 5 | `q44cfaf358c37:chunk-114` | 0.9298794377219834 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q44cfaf358c37`)._

### ex-dev-q4acd5677c3da

- **example_id**: `dev:q4acd5677c3da`
- **state**: `completed`
- **query**: What questions were asked about Hasbro’s customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9359826917490579 · gold=['Earnings', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.5052077707304854 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4acd5677c3da:chunk-67` | 1.341827121290792 | 1.0 | Well, I think it's, generally speaking, all of the above. However, I think the special emphasis for Universes Beyond is… |
| 2 | `q4acd5677c3da:chunk-87` | 0.9066687118438252 |  | Got it. That's really helpful. And then a follow-up. I was curious if you could help size up how much Baldur's Gate 3 a… |
| 3 | `q4acd5677c3da:chunk-65` | 0.8694347603156778 | 2.0 | Got it. That's very helpful. And then on the Universes Beyond sets coming beyond 2024, is the goal there with Marvel an… |
| 4 | `q4acd5677c3da:chunk-21` | 0.8359950751788017 |  | Yes, for sure. So last year, we were fortunate in that, both MAGIC and D&D were growers for us. The MAGIC tabletop busi… |
| 5 | `q4acd5677c3da:chunk-119` | 0.7242560310181534 |  | Our final question is from the line of Stephen Laszczyk with Goldman Sachs. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4acd5677c3da`)._

### ex-dev-q4bf1699a63fe

- **example_id**: `dev:q4bf1699a63fe`
- **state**: `completed`
- **query**: What dependency risks exist for Boston Properties, Inc. due to concentration of revenue in a limited number of geographic markets or key tenants?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.11305340175787203 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4bf1699a63fe:chunk-117` | 1.009111985090955 | 1.0 | The one other thing I would add is the performance of Reston Town Center. I mean again, the majority of our portfolio i… |
| 2 | `q4bf1699a63fe:chunk-56` | 0.6251580113481314 |  | Unknown Analyst - Analysts |
| 3 | `q4bf1699a63fe:chunk-80` | 0.5534193741428117 |  | Jing Xian Tan - Analysts |
| 4 | `q4bf1699a63fe:chunk-94` | 0.534112515249233 |  | Blaine Heck - Analysts |
| 5 | `q4bf1699a63fe:chunk-130` | 0.5249934658052947 |  | Dylan Burzinski - Analysts |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4bf1699a63fe`)._

### ex-dev-q4d8ac905167b

- **example_id**: `dev:q4d8ac905167b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Citigroup Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=894

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4d8ac905167b:chunk-220` | 1.438496334612462 |  | 95 |
| 2 | `q4d8ac905167b:chunk-2` | 1.3308173277208408 |  | 3 |
| 3 | `q4d8ac905167b:chunk-179` | 1.3097969251630361 |  | 84 |
| 4 | `q4d8ac905167b:chunk-149` | 1.2438128295059574 |  | 74 |
| 5 | `q4d8ac905167b:chunk-25` | 1.1575438235792914 |  | 14 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4d8ac905167b`)._

### ex-dev-q4e3318b7d0e9

- **example_id**: `dev:q4e3318b7d0e9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are data privacy or cybersecurity concerns affecting industry practices relevant to water technology solutions at Xylem Inc.?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-K', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['8-K', '10-K', 'DEF14A', '10-Q', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4e3318b7d0e9`)._

### ex-dev-q4f1cc6ea4ba6

- **example_id**: `dev:q4f1cc6ea4ba6`
- **state**: `completed`
- **query**: What sentiment trends are visible around Agilent Technologies’ free cash flow outlook and capital spending plans?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.557505327736571 · skipped= · n_scored=170

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4f1cc6ea4ba6:chunk-49` | 1.344688764226666 | 2.0 | I'll jump right into that one. So I tried to make that come out in the script. But our plans to continue to invest for … |
| 2 | `q4f1cc6ea4ba6:chunk-161` | 0.9722308049557572 |  | Yes, I would expect us to -- we will have a difficult Q1 and then starting to get better from Q2 and beyond, not dissim… |
| 3 | `q4f1cc6ea4ba6:chunk-47` | 0.9008136524426996 | 2.0 | Maybe just on NASD, I noticed just over the past, call it 1.5 years, we've kind of going from high double digits, low d… |
| 4 | `q4f1cc6ea4ba6:chunk-59` | 0.8329346824085783 |  | Yes. Matt, that's a great question. And we ended the Q4 at just a little under 3% and actually for the full year was gr… |
| 5 | `q4f1cc6ea4ba6:chunk-35` | 0.7327932369728897 |  | Yes. And Patrick, you asked about Q1, as I mentioned in the prepared remarks, I think we're taking a prudent approach h… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4f1cc6ea4ba6`)._

### ex-dev-q536ce4006bf6

- **example_id**: `dev:q536ce4006bf6`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did AutoZone’s leadership say about AutoZone’s share repurchase plans?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5770094797674725 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '8-K', 'DEF14A', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q536ce4006bf6`)._

### ex-dev-q53994e82efbb

- **example_id**: `dev:q53994e82efbb`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Builders FirstSource for recessionary or downturn risks in the residential construction market?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3065735963827292 · skipped= · n_scored=64

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q53994e82efbb:chunk-17` | 1.2534532380520405 |  | 8 |
| 2 | `q53994e82efbb:chunk-48` | 0.7835429480196661 |  | We experienced decreased net sales in all of our product categories primarily due to a slowing economy, a decline in co… |
| 3 | `q53994e82efbb:chunk-45` | 0.7643878157856536 | 1.0 | We experienced decreased net sales in all of our product categories primarily due to a slow-down in single-family housi… |
| 4 | `q53994e82efbb:chunk-39` | 0.5188075091409956 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations The following discussion … |
| 5 | `q53994e82efbb:chunk-58` | 0.3893079937998712 |  | Item 6. Exhibits |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q53994e82efbb`)._

### ex-dev-q56c2aa1b3aa2

- **example_id**: `dev:q56c2aa1b3aa2`
- **state**: `completed`
- **query**: How are scenario analyses conducted by FedEx Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.19519002499605084 · skipped= · n_scored=165

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q56c2aa1b3aa2:chunk-22` | 0.40490281647129883 |  | # Corporate Governance Matters-Nominees for Election to the Board # Summary of Director Nominee Experience, Qualificati… |
| 2 | `q56c2aa1b3aa2:chunk-160` | 0.366136974521323 |  | # Fiscal 2023 Reconciliations for Fiscal 2023 AIC Plan and FY21-FY23, FY22-FY24, FY23-FY25, and FY24-FY26 LTI Plans (co… |
| 3 | `q56c2aa1b3aa2:chunk-28` | 0.36547034140202295 | 1.0 | # Corporate Governance Matters - Nominees for Election to the Board (cont.) ## Board Risk Oversight The Board of Direct… |
| 4 | `q56c2aa1b3aa2:chunk-153` | 0.3233163491617796 |  | # ADDITIONAL INFORMATION ## General Information The principal executive offices of FedEx Corporation are located at 942… |
| 5 | `q56c2aa1b3aa2:chunk-2` | 0.2892072141707349 |  | # A MESSAGE FROM OUR EXECUTIVE CHAIRMAN AND LEAD INDEPENDENT DIRECTOR To our stockholders, In connection with our 2023 … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q56c2aa1b3aa2`)._

### ex-dev-q57e9d5635f56

- **example_id**: `dev:q57e9d5635f56`
- **state**: `completed`
- **query**: What quarter did guidance point to for streaming breakeven achievement
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q57e9d5635f56:chunk-19` | 0.7411111132304748 |  | So first on DTC. I mean, pricing is about to step up. You announced the cost-cutting program, some of which might be a … |
| 2 | `q57e9d5635f56:chunk-3` | 0.5011332157325377 |  | Good afternoon. It's my pleasure to welcome everybody to the Walt Disney Company's Fourth Quarter 2023 Earnings Call. O… |
| 3 | `q57e9d5635f56:chunk-12` | 0.473399780326064 |  | Michael Nathanson - Analysts |
| 4 | `q57e9d5635f56:chunk-0` | 0.46447064721130915 |  | Operator |
| 5 | `q57e9d5635f56:chunk-10` | 0.46447064721130915 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q57e9d5635f56`)._

### ex-dev-q587ea3fc913d

- **example_id**: `dev:q587ea3fc913d`
- **state**: `completed`
- **query**: What guidance did Textron’s leadership give on cost structure optimization efforts?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.4104889601851253 · skipped= · n_scored=174

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q587ea3fc913d:chunk-113` | 1.8892956448056373 | 2.0 | Well, Kristine, as we kind of put out there, there's a sizable piece that's going into Bell, and that's really aligning… |
| 2 | `q587ea3fc913d:chunk-67` | 1.4266276402440565 | 1.0 | Look, Noah. I think, look, the team is doing everything they can to manage costs, control -- do the right cost actions … |
| 3 | `q587ea3fc913d:chunk-0` | 1.0308473492884331 |  | Operator |
| 4 | `q587ea3fc913d:chunk-104` | 1.0308473492884331 |  | Operator |
| 5 | `q587ea3fc913d:chunk-118` | 1.0308473492884331 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q587ea3fc913d`)._

### ex-dev-q5ce8ea5bf1b9

- **example_id**: `dev:q5ce8ea5bf1b9`
- **state**: `completed`
- **query**: What dependency risks exist for Global Payments Inc. due to concentration of revenue in a limited number of payment processing partners or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.05652670087893601 · skipped= · n_scored=119

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5ce8ea5bf1b9:chunk-41` | 1.2003903478831766 |  | 17 |
| 2 | `q5ce8ea5bf1b9:chunk-49` | 1.1464057748410845 |  | 19 |
| 3 | `q5ce8ea5bf1b9:chunk-36` | 1.1094499485031153 | 1.0 | NOTE 4—REVENUES The following tables present a disaggregation of our revenues from contracts with customers by geograph… |
| 4 | `q5ce8ea5bf1b9:chunk-118` | 1.0420838987093244 |  | 49 |
| 5 | `q5ce8ea5bf1b9:chunk-99` | 1.0062998071925535 |  | NM = Not meaningful 36 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q5ce8ea5bf1b9`)._

### ex-dev-q5d75c4f1ac86

- **example_id**: `dev:q5d75c4f1ac86`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What progress was reported in international park attendance recovery relative to pre pandemic levels
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.93228165068934 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=10

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5d75c4f1ac86:chunk-11` | 0.95 |  | # Table of Contents (cont.) ## COVID-19 Response Throughout these challenging times, the Company has continued to suppo… |
| 2 | `q5d75c4f1ac86:chunk-12` | 0.94 |  | # Table of Contents (cont.) ## Executive Leadership (cont.) In fiscal 2021, Mr. Iger successfully directed the Company'… |
| 3 | `q5d75c4f1ac86:chunk-13` | 0.93 |  | # Table of Contents (cont.) ## Board Refreshment (cont.) Working closely with the full Board, the Governance and Nomina… |
| 4 | `q5d75c4f1ac86:chunk-14` | 0.92 |  | # Shareholder Engagement and Responsiveness (cont.) ## Investor Engagement Process During fiscal 2021, including follow… |
| 5 | `q5d75c4f1ac86:chunk-15` | 0.91 |  | # Commitment to Investor Engagement In response to shareholder feedback, the Board has modified our CEO and NEO compens… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q5d75c4f1ac86`)._

### ex-dev-q5d883a6e3ff1

- **example_id**: `dev:q5d883a6e3ff1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How have investors reacted to The TJX Companies, Inc.’s updated guidance or forward-looking projections?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.8498932729020808 · gold=['Earnings', '8-K', '10-K', 'DEF14A']
- **S1 ordered**: `['8-K', 'Earnings', '10-Q', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q5d883a6e3ff1`)._

### ex-dev-q5fca8aed3bbc

- **example_id**: `dev:q5fca8aed3bbc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Camden Property Trust’s recurring rental income to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.6280699432768105 · gold=['10-K', '8-K', 'Earnings', '10-Q']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q5fca8aed3bbc`)._

### ex-dev-q60107966eba4

- **example_id**: `dev:q60107966eba4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Kellanova view the pace of innovation cycles in product development and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7083232243990188 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q60107966eba4`)._

### ex-dev-q63259a02ade0

- **example_id**: `dev:q63259a02ade0`
- **state**: `completed`
- **query**: What does Apple's executive compensation structure look like?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=1.0 · gold=['DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.20253383242385095 · skipped= · n_scored=134

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q63259a02ade0:chunk-64` | 1.5755011387374616 |  | # Executive Compensation Tables (cont.) <table><tr><th>Name and Principal Position</th><th>Year</th><th>Salary ($)</th>… |
| 2 | `q63259a02ade0:chunk-50` | 1.486170366730806 | 1.0 | # The Role of the Compensation Consultant (cont.) ## Alignment with Shareholder Value Creation (cont.) The majority of … |
| 3 | `q63259a02ade0:chunk-79` | 1.370231796818155 |  | # Pay versus Performance (cont.) ## Relationship Between Compensation Actually Paid and our Total Shareholder Return Lo… |
| 4 | `q63259a02ade0:chunk-76` | 1.3699897532375087 |  | # Pay versus Performance (cont.) <table><tr><th rowspan="2">Fiscal Year(a)</th><th rowspan="2">Summary Compensation Tab… |
| 5 | `q63259a02ade0:chunk-58` | 1.3241334678247356 | 2.0 | # Annual Assessment of Apple Values and Key Community Initiatives (cont.) ## 2023 Performance-Based RSUs (cont.) Perfor… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q63259a02ade0`)._

### ex-dev-q636b07dd9c11

- **example_id**: `dev:q636b07dd9c11`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What impact could proposed legislative changes in the U.S. Credit Card Competition Act have on Mastercard?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.5860880558992709 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['8-K', 'DEF14A', 'Earnings', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q636b07dd9c11`)._

### ex-dev-q645be3b7875e

- **example_id**: `dev:q645be3b7875e`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Merck & Co., Inc.’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.5993473179020821 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q645be3b7875e`)._

### ex-dev-q64898e5ba36c

- **example_id**: `dev:q64898e5ba36c`
- **state**: `completed`
- **query**: What clarifications did analysts seek regarding Waters Corporation’s investment in chromatography and mass spectrometry innovation projects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9873464281832952 · gold=['Earnings', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', 'DEF14A', '10-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=274

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q64898e5ba36c:chunk-245` | 1.4370871166418102 |  | 98 |
| 2 | `q64898e5ba36c:chunk-209` | 1.4032957971256326 |  | 92 |
| 3 | `q64898e5ba36c:chunk-150` | 1.385308111178609 |  | 80 |
| 4 | `q64898e5ba36c:chunk-238` | 1.3842673249344462 |  | 97 |
| 5 | `q64898e5ba36c:chunk-200` | 1.3112316773335124 |  | 91 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q64898e5ba36c`)._

### ex-dev-q69d1505292c8

- **example_id**: `dev:q69d1505292c8`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How might global inflationary trends affect Walgreens Boots Alliance’s input costs and pricing strategies?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q69d1505292c8`)._

### ex-dev-q6c95b5e5930d

- **example_id**: `dev:q6c95b5e5930d`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Medtronic’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q6c95b5e5930d`)._

### ex-dev-q6cdb93e02e5f

- **example_id**: `dev:q6cdb93e02e5f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What clawback or recoupment policies apply to SBA Communications Corporation’s incentive compensation in case of restatements or misconduct?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8498932729020808 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q6cdb93e02e5f`)._

### ex-dev-q6d2cc453ca8c

- **example_id**: `dev:q6d2cc453ca8c`
- **state**: `completed`
- **query**: How did analysts probe the outlook for Roper Technologies’ free cash flow generation?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9278143341459562 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.3031246624382913 · skipped= · n_scored=130

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q6d2cc453ca8c:chunk-111` | 1.4263260198341645 | 1.0 | Absolutely. Yes. We're looking forward to the accretion after '24, and it will come, like I said, it's grown mid-teens,… |
| 2 | `q6d2cc453ca8c:chunk-107` | 1.1392892790122573 |  | Correct. |
| 3 | `q6d2cc453ca8c:chunk-59` | 1.0962807827358039 | 1.0 | Got it. And then just following up on the M&A side of things, leverage at 3x, obviously, strong cash flow generator. Bu… |
| 4 | `q6d2cc453ca8c:chunk-51` | 0.8242791132507964 |  | I think just more longer term on the SaaS migration. We have a little bit over $900 million in on-premise maintenance. … |
| 5 | `q6d2cc453ca8c:chunk-109` | 0.78114119955649 |  | Okay. Now going forward, if you're growing at double digits, mid-teens, that implies that you're going to get some pret… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q6d2cc453ca8c`)._

### ex-dev-q70b3e2802bf7

- **example_id**: `dev:q70b3e2802bf7`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Tyson Foods’ average cost per pound of processed chicken trend compared to the prior period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.788088263175707 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q70b3e2802bf7`)._

### ex-dev-q70e4aac30ddb

- **example_id**: `dev:q70e4aac30ddb`
- **state**: `completed`
- **query**: How did leadership respond to analyst questions about AI and personalization initiatives?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9903929125301808 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', 'DEF14A', '10-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q70e4aac30ddb:chunk-42` | 0.8939465803807559 |  | Sharon Zackfia - Analysts |
| 2 | `q70e4aac30ddb:chunk-22` | 0.8813453333639166 |  | Rachel Ruggeri - Executives |
| 3 | `q70e4aac30ddb:chunk-28` | 0.8813453333639166 |  | Rachel Ruggeri - Executives |
| 4 | `q70e4aac30ddb:chunk-36` | 0.8813453333639166 |  | Rachel Ruggeri - Executives |
| 5 | `q70e4aac30ddb:chunk-46` | 0.8813453333639166 |  | Rachel Ruggeri - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q70e4aac30ddb`)._

### ex-dev-q719082ac2068

- **example_id**: `dev:q719082ac2068`
- **state**: `completed`
- **query**: How did management characterize the evolution and strategic importance of AI factories?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9239941662222116 · gold=['Earnings', '10-K', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.38685280723454163 · skipped= · n_scored=15

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q719082ac2068:chunk-6` | 0.8688041711678282 |  | # Q4 Fiscal 2024 Summary (cont.) ## About NVIDIA (cont.) Certain statements in this press release including, but not li… |
| 2 | `q719082ac2068:chunk-3` | 0.5816560318998896 |  | # Q4 Fiscal 2024 Summary (cont.) ## Data Center (cont.) - Introduced NVIDIA MONAITM cloud APIs to help developers and p… |
| 3 | `q719082ac2068:chunk-7` | 0.4748075042804157 |  | # Q4 Fiscal 2024 Summary (cont.) ## About NVIDIA (cont.) © 2024 NVIDIA Corporation. All rights reserved. INVIDIA, the N… |
| 4 | `q719082ac2068:chunk-5` | 0.4477990877319325 |  | # Q4 Fiscal 2024 Summary (cont.) ## About NVIDIA (cont.) Simona Jankowski Investor Relations NVIDIA Corporation sjankow… |
| 5 | `q719082ac2068:chunk-0` | 0.40850722686729984 | 1.0 | # FOR IMMEDIATE RELEASE: NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2024 - Record quarterly reven… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q719082ac2068`)._

### ex-dev-q76caada13eca

- **example_id**: `dev:q76caada13eca`
- **state**: `completed`
- **query**: What causes differences between Weyerhaeuser Company’s cash flow and net income (e.g., timberland harvest cycles or non-cash depreciation)?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9199642183398656 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=86

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q76caada13eca:chunk-0` | 1.3675699372508896 |  | Operator |
| 2 | `q76caada13eca:chunk-10` | 1.3675699372508896 |  | Operator |
| 3 | `q76caada13eca:chunk-20` | 1.3675699372508896 |  | Operator |
| 4 | `q76caada13eca:chunk-30` | 1.3675699372508896 |  | Operator |
| 5 | `q76caada13eca:chunk-40` | 1.3675699372508896 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q76caada13eca`)._

### ex-dev-q78d98dc75a82

- **example_id**: `dev:q78d98dc75a82`
- **state**: `completed`
- **query**: How has Humana’s Medicare Advantage segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '8-K', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.12389007283034911 · skipped= · n_scored=283

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q78d98dc75a82:chunk-78` | 2.0538256908667565 | 1.0 | ####################Change## ####2023####2022######2021####2023####2022 ##########(in millions)############ Medicare##$… |
| 2 | `q78d98dc75a82:chunk-128` | 1.4681566481370851 |  | ####2023####2022####2021 ########(in millions)#### Health care cost payments##$##(7,073)##$##(7,110)##$##(6,943) Health… |
| 3 | `q78d98dc75a82:chunk-176` | 1.2870552021733261 |  | ####(in millions) 2024##$##60 2025####58 2026####43 2027####33 2028####28 |
| 4 | `q78d98dc75a82:chunk-47` | 1.2262758398686475 |  | ####12/31/2018####12/31/2019####12/31/2020####12/31/2021####12/31/2022####12/31/2023 HUM##$##100##$##129##$##145##$##16… |
| 5 | `q78d98dc75a82:chunk-142` | 1.0896139633821638 |  | Statements of income######## ####For the year ended December 31, 2023####August 11, 2022 through December 31, 2022 ####… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q78d98dc75a82`)._

### ex-dev-q79acb772ca6b

- **example_id**: `dev:q79acb772ca6b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Ingersoll Rand Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.93228165068934 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=290

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q79acb772ca6b:chunk-258` | 1.281069247181919 |  | 93 |
| 2 | `q79acb772ca6b:chunk-289` | 1.1927103441164835 |  | 105 |
| 3 | `q79acb772ca6b:chunk-280` | 1.1765057070369735 |  | 102 |
| 4 | `q79acb772ca6b:chunk-242` | 1.1717054345205529 |  | 88 |
| 5 | `q79acb772ca6b:chunk-282` | 1.1657382607151237 |  | 103 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q79acb772ca6b`)._

### ex-dev-q79ae686681b7

- **example_id**: `dev:q79ae686681b7`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Best Buy’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7591919243197319 · gold=['10-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q79ae686681b7`)._

### ex-dev-q7b42f1295dc1

- **example_id**: `dev:q7b42f1295dc1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are scenario analyses conducted by Fiserv for recessionary or downturn risks?
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.6859372277669218 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['8-K', '10-K', 'DEF14A', '10-Q', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7b42f1295dc1`)._

### ex-dev-q7c284aabbba4

- **example_id**: `dev:q7c284aabbba4`
- **state**: `completed`
- **query**: What dependency risks exist for Moderna, Inc. due to concentration of revenue in a limited number of vaccine products or geographic markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9882048111454694 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7c284aabbba4:chunk-80` | 0.9759168388794501 |  | Operator |
| 2 | `q7c284aabbba4:chunk-0` | 0.9720175907217132 |  | Operator |
| 3 | `q7c284aabbba4:chunk-12` | 0.9720175907217132 |  | Operator |
| 4 | `q7c284aabbba4:chunk-18` | 0.9720175907217132 |  | Operator |
| 5 | `q7c284aabbba4:chunk-26` | 0.9720175907217132 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7c284aabbba4`)._

### ex-dev-q7e2586950d8e

- **example_id**: `dev:q7e2586950d8e`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Ball Corporation’s beverage packaging segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7e2586950d8e`)._

### ex-dev-q7eb4e8a11956

- **example_id**: `dev:q7eb4e8a11956`
- **state**: `completed`
- **query**: Summarize Luca Maestri's recent commentary on the gross margin outlook given current FX headwinds.
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7eb4e8a11956:chunk-7` | 1.0852068852200978 |  | Thank you, Tim, and good afternoon, everyone. Revenue for the September quarter was $89.5 billion, down less than 1% fr… |
| 2 | `q7eb4e8a11956:chunk-29` | 0.8653576572912288 |  | As you've seen from our results in Q4 and the guidance for Q1, we're obviously experiencing very strong levels of gross… |
| 3 | `q7eb4e8a11956:chunk-85` | 0.8468814447583746 |  | I have 2 of them, too. First one, Luca, thanks for the color on gross margin. And when I look at it over the last 4 qua… |
| 4 | `q7eb4e8a11956:chunk-25` | 0.8027611892349297 |  | Yes. If you look at how we did in Greater China for the quarter, we came in at, on revenue basis, minus 2. But one thin… |
| 5 | `q7eb4e8a11956:chunk-109` | 0.7852092730427053 |  | And I would add, Richard, on this front, some of the investments that we're making in R&D are also one of the drivers f… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7eb4e8a11956`)._

### ex-dev-q7eb5b91e2366

- **example_id**: `dev:q7eb5b91e2366`
- **state**: `completed`
- **query**: What dependency risks exist for Becton, Dickinson and Company due to concentration of revenue in a limited number of healthcare providers or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9935051443580323 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=76

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7eb5b91e2366:chunk-69` | 0.7429330177353237 |  | Thanks for the question, Rich. |
| 2 | `q7eb5b91e2366:chunk-0` | 0.5938324939741508 |  | Operator |
| 3 | `q7eb5b91e2366:chunk-16` | 0.5938324939741508 |  | Operator |
| 4 | `q7eb5b91e2366:chunk-26` | 0.5938324939741508 |  | Operator |
| 5 | `q7eb5b91e2366:chunk-32` | 0.5938324939741508 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7eb5b91e2366`)._

### ex-dev-q7ebef55d671d

- **example_id**: `dev:q7ebef55d671d`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Chipotle’s supply chain efficiency targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6266239202359082 · gold=['DEF14A', '10-Q', '10-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7ebef55d671d`)._

### ex-dev-q7ed5279a28b4

- **example_id**: `dev:q7ed5279a28b4`
- **state**: `completed`
- **query**: What did Teradyne’s management note about Teradyne’s operational scalability as test equipment demand volumes grow or contract?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-Q', '10-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=156

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ed5279a28b4:chunk-27` | 1.7195903367522267 |  | 9 |
| 2 | `q7ed5279a28b4:chunk-40` | 1.568316843491883 |  | 11 |
| 3 | `q7ed5279a28b4:chunk-50` | 1.545637824434251 |  | 13 |
| 4 | `q7ed5279a28b4:chunk-61` | 1.49531739841147 |  | 16 |
| 5 | `q7ed5279a28b4:chunk-74` | 1.3496824006525507 |  | 19 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7ed5279a28b4`)._

### ex-dev-q811679c2d742

- **example_id**: `dev:q811679c2d742`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What challenges are noted regarding scaling infrastructure or capacity for renewable energy integration to meet growth?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', '8-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5=0.9402694138204842 · skipped= · n_scored=10

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q811679c2d742:chunk-107` | 0.95 | 2.0 | New Technology and Government Grants Hydrogen Hub Grant In October 2023, the DOE selected the Heartland Hydrogen Hub, i… |
| 2 | `q811679c2d742:chunk-105` | 0.94 | 2.0 | If approved by the CPUC, Xcel Energy expects to invest $7.9 billion in generation resources. In addition, the plan requ… |
| 3 | `q811679c2d742:chunk-106` | 0.93 | 2.0 | Colorado Legislation — In May 2023, Colorado Senate Bill 23-291 passed and was signed into law. The bill includes a num… |
| 4 | `q811679c2d742:chunk-104` | 0.92 |  | Generation Resource (in MW)##Company Owned##PPAs##Total Wind Resources##2,531##875##3,406 Solar##1,109##860##1,969 Stor… |
| 5 | `q811679c2d742:chunk-103` | 0.91 | 1.0 | In September 2023, NSP-Wisconsin filed rebuttal testimony and updated its request for depreciation life extensions and … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q811679c2d742`)._

### ex-dev-q84038a74fd59

- **example_id**: `dev:q84038a74fd59`
- **state**: `completed`
- **query**: How many organizations were reported to be using Azure OpenAI Service
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9871901582936081 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '8-K', '10-Q', 'DEF14A', '10-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=76

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q84038a74fd59:chunk-13` | 0.35738383807895024 |  | A very nice end to a great fiscal year. Satya, you started your comments talking about how every customer conversation … |
| 2 | `q84038a74fd59:chunk-15` | 0.3155340356188631 |  | Thank you, Keith, for the question. The fundamental guidance and conversation that we have with customers is twofold. O… |
| 3 | `q84038a74fd59:chunk-0` | 0.31123483459100176 |  | Operator |
| 4 | `q84038a74fd59:chunk-10` | 0.31123483459100176 |  | Operator |
| 5 | `q84038a74fd59:chunk-18` | 0.31123483459100176 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q84038a74fd59`)._

### ex-dev-q86f79f57d973

- **example_id**: `dev:q86f79f57d973`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did Linde’s leadership say about Linde’s dividend policy or share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '8-K', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q86f79f57d973`)._

### ex-dev-q88819064dbb7

- **example_id**: `dev:q88819064dbb7`
- **state**: `completed`
- **query**: What investor views emerged on Dollar Tree, Inc.’s geographic expansion prospects within the domestic discount retail market?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.2145327032398032 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88819064dbb7:chunk-59` | 0.7452477210804127 |  | Yes, recapturing the sales. I think we feel pretty bullish about that. A lot of these stores that were rationalizing ou… |
| 2 | `q88819064dbb7:chunk-45` | 0.7284402322944546 | 1.0 | Yes. Great questions. First thing I'll say to you, John, is we will stagger the rollout. I like to spread an initiative… |
| 3 | `q88819064dbb7:chunk-94` | 0.6978720529364478 |  | Bradley Thomas - Analysts |
| 4 | `q88819064dbb7:chunk-89` | 0.6881903075670525 | 1.0 | Yes. Another really good question. I would look at you and say the initiatives have worked in every store. The problem … |
| 5 | `q88819064dbb7:chunk-32` | 0.6762847217969103 |  | Charles Grom - Analysts |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q88819064dbb7`)._

### ex-dev-q88db5d96c8dd

- **example_id**: `dev:q88db5d96c8dd`
- **state**: `completed`
- **query**: How does Bristol-Myers Squibb manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=176

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88db5d96c8dd:chunk-27` | 1.3014167254206102 |  | 10 |
| 2 | `q88db5d96c8dd:chunk-38` | 1.0101375470775589 |  | 13 |
| 3 | `q88db5d96c8dd:chunk-149` | 0.9311775042776194 |  | 50 |
| 4 | `q88db5d96c8dd:chunk-86` | 0.9084669097964354 |  | Note 16. EQUITY The following table summarizes changes in equity for the nine months ended September 30, 2023: |
| 5 | `q88db5d96c8dd:chunk-175` | 0.8530255172023011 |  | 58 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q88db5d96c8dd`)._

### ex-dev-q89953a08e494

- **example_id**: `dev:q89953a08e494`
- **state**: `completed`
- **query**: How does Globe Life Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.14115639177619477 · skipped= · n_scored=125

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89953a08e494:chunk-100` | 1.1296458351633374 |  | # PAY VERSUS PERFORMANCE (cont.) <table><tr><th></th><th></th><th colspan="5">PEO-2</th></tr><tr><td rowspan="2">Year</… |
| 2 | `q89953a08e494:chunk-80` | 1.1211953634467058 | 1.0 | # 2023 GRANTS OF PLAN-BASED AWARDS <table><tr><th></th><th rowspan="2">Award Type</th><th rowspan="2">Grant Date</th><t… |
| 3 | `q89953a08e494:chunk-85` | 1.0030594057882374 |  | # OUTSTANDING EQUITY AWARDS AT FISCAL YEAR-END 2023 (continued) (cont.) <table><tr><th></th><th colspan="5">Option Awar… |
| 4 | `q89953a08e494:chunk-76` | 0.8715999558618129 |  | # EXECUTIVE COMPENSATION SUMMARY COMPENSATION TABLE (cont.) <table><tr><th>Name and Principal Position</th><th>Year</th… |
| 5 | `q89953a08e494:chunk-66` | 0.7314244564154995 | 1.0 | # Assessment of 2023 Advisory Vote on Executive Compensation (cont.) ## Long-Term Equity Incentives We award long-term … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q89953a08e494`)._

### ex-dev-q89fb186f5e49

- **example_id**: `dev:q89fb186f5e49`
- **state**: `completed`
- **query**: What investor views emerged on Linde’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=287

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89fb186f5e49:chunk-195` | 1.3277892402254303 |  | 80 |
| 2 | `q89fb186f5e49:chunk-241` | 1.3030096890457683 |  | 94 |
| 3 | `q89fb186f5e49:chunk-247` | 1.2842116830923813 |  | 97 |
| 4 | `q89fb186f5e49:chunk-225` | 1.24739140326663 |  | 90 |
| 5 | `q89fb186f5e49:chunk-271` | 1.1002045239474536 |  | 108 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q89fb186f5e49`)._

### ex-dev-q8b55a229e784

- **example_id**: `dev:q8b55a229e784`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of C.H. Robinson Worldwide’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.6885288809404666 · gold=['10-K', '10-Q']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q8b55a229e784`)._

### ex-dev-q8ba6a388d681

- **example_id**: `dev:q8ba6a388d681`
- **state**: `completed`
- **query**: What questions were asked about Broadcom’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '8-K', '10-K']`
- **S2**: nDCG@5=0.8318724637288826 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8ba6a388d681:chunk-101` | 1.0435262268949936 | 1.0 | Hock, in the past, I think we've all been aware that there's one major customer on the accelerated compute side, I susp… |
| 2 | `q8ba6a388d681:chunk-51` | 0.9170239037381489 | 1.0 | I mean you did say 65% on it. I think I recall you saying you were going to run VMware at 65%. So I guess, 65% is the r… |
| 3 | `q8ba6a388d681:chunk-49` | 0.9151767083931852 | 1.0 | It's somewhere between 60% and 65%. How does that sound, Stacy? |
| 4 | `q8ba6a388d681:chunk-53` | 0.7434600554433277 |  | At steady state, you're right. At steady state, we'll get to pretty close to 65% on VMware. |
| 5 | `q8ba6a388d681:chunk-78` | 0.6733004523887953 |  | Toshiya Hari - Analysts |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q8ba6a388d681`)._

### ex-dev-q8cc1033cf552

- **example_id**: `dev:q8cc1033cf552`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance did The Sherwin-Williams Company’s leadership provide on debt reduction or leverage targets for The Sherwin-Williams Company?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9461356536981058 · gold=['10-K', 'Earnings', '10-Q']
- **S1 ordered**: `['10-K', 'DEF14A', 'Earnings', '8-K', '10-Q']`
- **S2**: nDCG@5=0.48522855511632257 · skipped= · n_scored=10

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8cc1033cf552:chunk-88` | 0.98 | 1.0 | Three Months Ended September 30, 2023 Consolidated cost of goods sold decreased $257.5 million, or 7.4%, in the third q… |
| 2 | `q8cc1033cf552:chunk-89` | 0.97 |  | Nine Months Ended September 30, 2023 Consolidated cost of goods sold decreased $236.8 million, or 2.4%, in the first ni… |
| 3 | `q8cc1033cf552:chunk-92` | 0.96 |  | Income Tax Expense The effective tax rate was 24.5% for the third quarter of 2023 compared to 21.9% for the third quart… |
| 4 | `q8cc1033cf552:chunk-93` | 0.95 | 1.0 | FINANCIAL CONDITION, LIQUIDITY AND CASH FLOW Overview The Company’s financial condition and liquidity remained strong a… |
| 5 | `q8cc1033cf552:chunk-105` | 0.94 |  | Item 3. QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK The Company is exposed to market risk associated wit… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q8cc1033cf552`)._

### ex-dev-q8e053e02a010

- **example_id**: `dev:q8e053e02a010`
- **state**: `completed`
- **query**: What dependency risks exist for International Paper Company due to concentration of revenue in a limited number of end-use paper and packaging markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=225

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8e053e02a010:chunk-0` | 0.4421696421440676 |  | # UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 SCHEDULE 14A (Rule 14a-101) INFORMATION REQUI… |
| 2 | `q8e053e02a010:chunk-6` | 0.3894736016673248 |  | # Table of Contents (cont.) ## Index of Frequently Requested Information <table><tr><th>Our Commitment to Sustainabilit… |
| 3 | `q8e053e02a010:chunk-140` | 0.3407479885323588 |  | # Supplemental (cont.) ## Most Important Performance Measures (cont.) Table of Contents The image shows a close-up view… |
| 4 | `q8e053e02a010:chunk-217` | 0.3379198691741175 |  | # Table of Contents (cont.) ## Appendix -Reconciliations of Non-GAAP Measures (cont.) <table><tr><th>In millions, for t… |
| 5 | `q8e053e02a010:chunk-67` | 0.3330212625109516 |  | # Overview of Our CD&A <table><tr><th>Introduction</th><th>47</th><th>Short-Term Incentive</th><th>63</th></tr><tr><td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q8e053e02a010`)._

### ex-dev-q8e26f08be2bc

- **example_id**: `dev:q8e26f08be2bc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What challenges arise for Vertex Pharmaceuticals from data privacy regulations and handling of patient data?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.8403399529073962 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['8-K', '10-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q8e26f08be2bc`)._

### ex-dev-q909c4baef1ee

- **example_id**: `dev:q909c4baef1ee`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did analysts frame queries about Truist Financial Corporation’s shareholder returns, including dividends?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.6266239202359082 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q909c4baef1ee`)._

### ex-dev-q93fb2b2861c4

- **example_id**: `dev:q93fb2b2861c4`
- **state**: `completed`
- **query**: How does Church & Dwight view the pace of product innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9134693626978977 · gold=['10-K', '8-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.33916020527361607 · skipped= · n_scored=208

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q93fb2b2861c4:chunk-11` | 1.5861781582903185 | 2.0 | COMPETITION We compete in the household and personal care consumer product categories, which are highly innovative cate… |
| 2 | `q93fb2b2861c4:chunk-6` | 1.3654554733770006 |  | 3 |
| 3 | `q93fb2b2861c4:chunk-204` | 1.3235247866252833 |  | 92 |
| 4 | `q93fb2b2861c4:chunk-201` | 1.270124821172969 |  | 91 |
| 5 | `q93fb2b2861c4:chunk-207` | 1.1936346551613979 |  | 93 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q93fb2b2861c4`)._

### ex-dev-q95535bca90c9

- **example_id**: `dev:q95535bca90c9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Wells Fargo’s average cost per loan origination trend compared to the prior period?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7085011369669131 · gold=['10-Q', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q95535bca90c9`)._

### ex-dev-q95790ca7c1f5

- **example_id**: `dev:q95790ca7c1f5`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did Dayforce Inc.’s leadership say about Dayforce Inc.’s share repurchase plans?
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.4933965394160924 · gold=['10-K', 'Earnings']
- **S1 ordered**: `['8-K', 'Earnings', 'DEF14A', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q95790ca7c1f5`)._

### ex-dev-q9597b3e4d1b2

- **example_id**: `dev:q9597b3e4d1b2`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has investor sentiment shifted following Archer-Daniels-Midland Company’s most recent earnings release?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.68154288742782 · gold=['10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9597b3e4d1b2`)._

### ex-dev-q98c606bb3ce7

- **example_id**: `dev:q98c606bb3ce7`
- **state**: `completed`
- **query**: What litigation or dispute risks did Williams-Sonoma, Inc. identify and what is the potential financial impact for Williams-Sonoma, Inc.?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.1843821566693812 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q98c606bb3ce7:chunk-30` | 1.3482676115783672 | 1.0 | Table of Contents ITEM 3. LEGAL PROCEEDINGS We are involved in lawsuits, claims and proceedings incident to the ordinar… |
| 2 | `q98c606bb3ce7:chunk-7` | 1.2492437357043515 | 1.0 | Table of Contents Risks Related to Technology •We are exposed to cybersecurity risks and costs associated with credit c… |
| 3 | `q98c606bb3ce7:chunk-146` | 1.0422493102386177 |  | 76 |
| 4 | `q98c606bb3ce7:chunk-134` | 1.0025739459854284 |  | 72 |
| 5 | `q98c606bb3ce7:chunk-137` | 0.9418653298072981 |  | 73 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q98c606bb3ce7`)._

### ex-dev-q99a077efaab0

- **example_id**: `dev:q99a077efaab0`
- **state**: `completed`
- **query**: What dependency risks exist for Align Technology due to concentration of revenue in a limited number of orthodontic practices or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99a077efaab0:chunk-106` | 0.7448169196160263 |  | Operator |
| 2 | `q99a077efaab0:chunk-112` | 0.7448169196160263 |  | Operator |
| 3 | `q99a077efaab0:chunk-122` | 0.7448169196160263 |  | Operator |
| 4 | `q99a077efaab0:chunk-126` | 0.7448169196160263 |  | Operator |
| 5 | `q99a077efaab0:chunk-22` | 0.7448169196160263 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q99a077efaab0`)._

### ex-dev-q99ec5f1aeea5

- **example_id**: `dev:q99ec5f1aeea5`
- **state**: `completed`
- **query**: What questions were asked about Federal Realty Investment Trust’s tenant retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9134693626978977 · gold=['Earnings', '8-K', '10-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=64

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99ec5f1aeea5:chunk-14` | 1.3161675445033372 |  | <hr /> |
| 2 | `q99ec5f1aeea5:chunk-39` | 1.3161675445033372 |  | <hr /> |
| 3 | `q99ec5f1aeea5:chunk-50` | 1.3161675445033372 |  | <hr /> |
| 4 | `q99ec5f1aeea5:chunk-53` | 1.3161675445033372 |  | <hr /> |
| 5 | `q99ec5f1aeea5:chunk-12` | 1.3157942510610048 |  | <hr /> |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q99ec5f1aeea5`)._

### ex-dev-q9a5cfe35fecd

- **example_id**: `dev:q9a5cfe35fecd`
- **state**: `completed`
- **query**: What dependency risks exist for CMS Energy Corporation due to concentration of revenue in a limited number of geographic regions or key utility customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=194

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9a5cfe35fecd:chunk-9` | 1.6270952043414848 |  | 4 |
| 2 | `q9a5cfe35fecd:chunk-15` | 1.6207804061732036 |  | 7 |
| 3 | `q9a5cfe35fecd:chunk-11` | 1.6126065518927488 |  | 5 |
| 4 | `q9a5cfe35fecd:chunk-7` | 1.6110327751140814 |  | 3 |
| 5 | `q9a5cfe35fecd:chunk-13` | 1.5635851291413707 |  | 6 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9a5cfe35fecd`)._

### ex-dev-q9c255237096a

- **example_id**: `dev:q9c255237096a`
- **state**: `completed`
- **query**: What perquisites or fringe benefits are included in The AES Corporation’s executive compensation disclosures?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=1.0 · gold=['DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.17159048162789245 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9c255237096a:chunk-56` | 1.44756368776179 |  | # Three-Year CEO LTC Realizable Pay (cont.) ## Severance and Change-in-Control Arrangements The Company maintains certa… |
| 2 | `q9c255237096a:chunk-58` | 1.3927414650285068 | 1.0 | # 2023 Summary Compensation Table <table><tr><th>Year</th><th>Salary ($)¹</th><th>Bonus ($)</th><th>Stock Awards ($)(2)… |
| 3 | `q9c255237096a:chunk-71` | 1.1264391222798038 | 1.0 | # 2023 Option Exercises and Stock Vested (cont.) ## Potential Payments upon Termination under the Executive Severance P… |
| 4 | `q9c255237096a:chunk-2` | 1.069174022682998 |  | # Table of Contents (cont.) <table><tr><th>2023 Option Exercises and Stock Vested</th><th>57</th></tr><tr><td>2023 Non-… |
| 5 | `q9c255237096a:chunk-68` | 1.0650548809178324 | 1.0 | # 2023 Option Exercises and Stock Vested (cont.) ## Narrative Disclosure Relating to the Non-Qualified Deferred Compens… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9c255237096a`)._

### ex-dev-q9dd3907388e3

- **example_id**: `dev:q9dd3907388e3`
- **state**: `completed`
- **query**: How does Duke Energy view the pace of innovation cycles in renewable energy technologies and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9dd3907388e3:chunk-29` | 0.5754089222351394 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 2 | `q9dd3907388e3:chunk-43` | 0.5274771726588062 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 3 | `q9dd3907388e3:chunk-45` | 0.5274771726588062 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 4 | `q9dd3907388e3:chunk-47` | 0.5274771726588062 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 5 | `q9dd3907388e3:chunk-49` | 0.5274771726588062 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9dd3907388e3`)._

### ex-dev-q9f32df79b0d7

- **example_id**: `dev:q9f32df79b0d7`
- **state**: `completed`
- **query**: How does Capital One view the pace of digital banking innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=4

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9f32df79b0d7:chunk-0` | 0.2745235196167059 | 1.0 | Exhibit 99.1 News Release <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><… |
| 2 | `q9f32df79b0d7:chunk-3` | 0.22324074098527197 |  | Capital One Financial Corporation (www.capitalone.com) is a financial holding company which, along with its subsidiarie… |
| 3 | `q9f32df79b0d7:chunk-1` | 0.19648055190954095 |  | •Total net revenue increased 4 percent to $9.4 billion. •Total non-interest expense increased 1 percent to $4.9 billion… |
| 4 | `q9f32df79b0d7:chunk-2` | 0.10998739010475625 |  | •Auto average loans decreased $493 million, or 1 percent, to $75.7 billion. ◦Commercial Banking average loans decreased… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9f32df79b0d7`)._

### ex-dev-qa057a3d428a2

- **example_id**: `dev:qa057a3d428a2`
- **state**: `completed`
- **query**: What dependency risks exist for McKesson Corporation due to concentration of revenue in a limited number of pharmaceutical manufacturers or healthcare providers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa057a3d428a2:chunk-24` | 1.4714304192766945 |  | 11 |
| 2 | `qa057a3d428a2:chunk-27` | 1.4096642435795117 |  | 12 |
| 3 | `qa057a3d428a2:chunk-135` | 1.1757726338789962 |  | 57 |
| 4 | `qa057a3d428a2:chunk-85` | 1.0800799721522703 |  | 32 |
| 5 | `qa057a3d428a2:chunk-19` | 0.9538427242315316 |  | See Financial Notes 8 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qa057a3d428a2`)._

### ex-dev-qa33b36ffd2c1

- **example_id**: `dev:qa33b36ffd2c1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Garmin’s fitness segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7146598531416503 · gold=['10-Q', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qa33b36ffd2c1`)._

### ex-dev-qa5c748248a5b

- **example_id**: `dev:qa5c748248a5b`
- **state**: `completed`
- **query**: How has the ratio of MSCI’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-Q', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.9125299483251055 · skipped= · n_scored=255

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa5c748248a5b:chunk-48` | 1.9174969349167266 | 2.0 | ######Years Ended######## (in thousands)####December 31, 2023######December 31, 2022##Increase/(Decrease)## Recurring s… |
| 2 | `qa5c748248a5b:chunk-87` | 1.7323530423450801 | 2.0 | ########Years Ended########## (in thousands)####December 31, 2023########December 31, 2022####Increase/(Decrease)## Ope… |
| 3 | `qa5c748248a5b:chunk-84` | 1.7053486667740145 | 2.0 | ########Years Ended########## (in thousands)####December 31, 2023########December 31, 2022####Increase/(Decrease)## Ope… |
| 4 | `qa5c748248a5b:chunk-89` | 1.6103023464512238 | 2.0 | ########Years Ended########## (in thousands)####December 31, 2023########December 31, 2022####Increase/(Decrease)## Ope… |
| 5 | `qa5c748248a5b:chunk-47` | 1.3965249980954497 | 1.0 | The following table presents operating revenues by type for the years indicated: |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qa5c748248a5b`)._

### ex-dev-qa602975e3d19

- **example_id**: `dev:qa602975e3d19`
- **state**: `completed`
- **query**: How has the ratio of Mondelez International’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9411655511901171 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=189

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa602975e3d19:chunk-1` | 1.0021287563707397 |  | # LETTER FROM OUR CHAIR AND CHIEF EXECUTIVE OFFICER (cont.) ## April 5, 2024 (cont.) Dirk Van de Put Chair and Cheif Ex… |
| 2 | `qa602975e3d19:chunk-158` | 0.4850888276039131 |  | # Back to Contents Definitions <table><tr><th>Measures</th><th>(Including Adjustment to GAAP Measure)</th><th rowspan="… |
| 3 | `qa602975e3d19:chunk-100` | 0.43081382659715217 |  | # MONDELÊZ GLOBAL LLC MEDCP (cont.) ## Back to Contents (cont.) <table><tr><th>Severance Benefits</th><th>CEO: 24 month… |
| 4 | `qa602975e3d19:chunk-0` | 0.3916145330984966 |  | # UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, DC 20549 # SCHEDULE 14A PROXY STATEMENT PURSUANT TO SECT… |
| 5 | `qa602975e3d19:chunk-62` | 0.3109193389297581 |  | # COMPENSATION DISCUSSION AND ANALYSIS (CD&A) (cont.) ## Net Revenues ## Cash Flow Reported Net Revenues Growth +14.4% … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qa602975e3d19`)._

### ex-dev-qa9744c8552ed

- **example_id**: `dev:qa9744c8552ed`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did analysts question TJX Companies’ management on their strategies for responsible sourcing and sustainable supply chain practices?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6729475164829866 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qa9744c8552ed`)._

### ex-dev-qab00fabe02dc

- **example_id**: `dev:qab00fabe02dc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Rockwell Automation’s executives address regulatory or policy developments and their potential implications for industrial automation solutions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7083232243990188 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qab00fabe02dc`)._

### ex-dev-qaf55b76bfcad

- **example_id**: `dev:qaf55b76bfcad`
- **state**: `completed`
- **query**: Which partnership with a major telecommunications provider was highlighted for bundling offers
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '8-K', '10-Q', 'DEF14A', '10-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qaf55b76bfcad:chunk-0` | 0.6241026777684845 |  | Operator |
| 2 | `qaf55b76bfcad:chunk-10` | 0.6241026777684845 |  | Operator |
| 3 | `qaf55b76bfcad:chunk-16` | 0.6241026777684845 |  | Operator |
| 4 | `qaf55b76bfcad:chunk-22` | 0.6241026777684845 |  | Operator |
| 5 | `qaf55b76bfcad:chunk-30` | 0.6241026777684845 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qaf55b76bfcad`)._

### ex-dev-qb00e9c27fd32

- **example_id**: `dev:qb00e9c27fd32`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Monster Beverage Corporation’s segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb00e9c27fd32`)._

### ex-dev-qb2123a701a82

- **example_id**: `dev:qb2123a701a82`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Atmos Energy view the pace of pipeline technology innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6388967123938784 · gold=['DEF14A', '8-K', '10-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb2123a701a82`)._

### ex-dev-qb22cbf2f4782

- **example_id**: `dev:qb22cbf2f4782`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Apple management recently commented on services attach rates and other value-added offerings?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.631251450669265 · gold=['10-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb22cbf2f4782`)._

### ex-dev-qb26bf8457b0f

- **example_id**: `dev:qb26bf8457b0f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What risks are associated with opening new healthcare facilities for Universal Health Services, Inc. when patient demand is uncertain?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7860353577841278 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb26bf8457b0f`)._

### ex-dev-qb35a5efa65ce

- **example_id**: `dev:qb35a5efa65ce`
- **state**: `completed`
- **query**: What dependency risks exist for Evergy, Inc. due to concentration of revenue in a limited number of service territories or key industrial customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'Earnings', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.41607037852292533 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb35a5efa65ce:chunk-41` | 0.8811005799614829 | 2.0 | In terms of earnings sensitivity, I wouldn't call it linear from that perspective. These are obviously large industrial… |
| 2 | `qb35a5efa65ce:chunk-43` | 0.8385999341179398 |  | I would just echo Kirk's comment, though, on -- this is David, that the -- these are industrial customers, which, as yo… |
| 3 | `qb35a5efa65ce:chunk-20` | 0.4873657248875085 |  | Michael Sullivan - Analysts |
| 4 | `qb35a5efa65ce:chunk-24` | 0.4873657248875085 |  | Michael Sullivan - Analysts |
| 5 | `qb35a5efa65ce:chunk-28` | 0.4873657248875085 |  | Michael Sullivan - Analysts |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb35a5efa65ce`)._

### ex-dev-qb500a9b42ef8

- **example_id**: `dev:qb500a9b42ef8`
- **state**: `completed`
- **query**: How has the ratio of CMS Energy Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9452713619732751 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=488

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb500a9b42ef8:chunk-29` | 1.1352216011784333 |  | 10 |
| 2 | `qb500a9b42ef8:chunk-8` | 1.0563650058315739 |  | 3 |
| 3 | `qb500a9b42ef8:chunk-2` | 1.0537267534924974 |  | 1 |
| 4 | `qb500a9b42ef8:chunk-14` | 1.00674719546255 |  | 5 |
| 5 | `qb500a9b42ef8:chunk-26` | 0.976307240834799 |  | 9 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb500a9b42ef8`)._

### ex-dev-qb590e4e6d1ec

- **example_id**: `dev:qb590e4e6d1ec`
- **state**: `completed`
- **query**: How has the ratio of PG&E Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.23452925321255158 · skipped= · n_scored=213

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb590e4e6d1ec:chunk-74` | 0.8776722661252846 |  | PACIFIC GAS AND ELECTRIC COMPANY CONDENSED CONSOLIDATED STATEMENTS OF INCOME (in millions) |
| 2 | `qb590e4e6d1ec:chunk-53` | 0.8670977991945656 |  | PG&E CORPORATION CONDENSED CONSOLIDATED STATEMENTS OF COMPREHENSIVE INCOME (in millions) |
| 3 | `qb590e4e6d1ec:chunk-77` | 0.8417021206964097 |  | PACIFIC GAS AND ELECTRIC COMPANY CONDENSED CONSOLIDATED STATEMENTS OF COMPREHENSIVE INCOME (in millions) |
| 4 | `qb590e4e6d1ec:chunk-50` | 0.7887520627368176 |  | ITEM 1. CONDENSED CONSOLIDATED FINANCIAL STATEMENTS PG&E CORPORATION CONDENSED CONSOLIDATED STATEMENTS OF INCOME (in mi… |
| 5 | `qb590e4e6d1ec:chunk-9` | 0.7704605044963202 | 2.0 | ########Nine Months Ended September 30, 2023############Nine Months Ended September 30, 2022#### ########Revenues/Costs… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb590e4e6d1ec`)._

### ex-dev-qba0102803c57

- **example_id**: `dev:qba0102803c57`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Kimco Realty Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=332

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba0102803c57:chunk-242` | 1.4315370516733399 |  | 95 |
| 2 | `qba0102803c57:chunk-158` | 1.4129772057327912 |  | 80 |
| 3 | `qba0102803c57:chunk-181` | 1.2910743562431068 |  | 84 |
| 4 | `qba0102803c57:chunk-276` | 1.2720939489894314 |  | 102 |
| 5 | `qba0102803c57:chunk-148` | 1.2671224666851857 |  | 78 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qba0102803c57`)._

### ex-dev-qba50bc033945

- **example_id**: `dev:qba50bc033945`
- **state**: `completed`
- **query**: What commentary is provided by Teledyne Technologies on demand forecasts in light of government defense spending trends?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.29553891639141344 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba50bc033945:chunk-89` | 0.9869496625282537 | 1.0 | Yes. Okay. And then in past quarters, you sort of broke out [indiscernible] book-to-bill versus legacy Teledyne book-to… |
| 2 | `qba50bc033945:chunk-93` | 0.897736545581024 | 1.0 | Okay. And then a question on you're feeling on incremental defense awards throughout the year. Is there still a lot you… |
| 3 | `qba50bc033945:chunk-21` | 0.8288752401302829 | 1.0 | Alright. Yes. We're right now expecting uptick in those businesses in the second half of the year. We think that what w… |
| 4 | `qba50bc033945:chunk-0` | 0.7970303390700735 |  | Operator |
| 5 | `qba50bc033945:chunk-122` | 0.7970303390700735 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qba50bc033945`)._

### ex-dev-qbd63044fc6b3

- **example_id**: `dev:qbd63044fc6b3`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What risk is associated with franchisee financial health amid rapid expansion requirements
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.708583264987264 · gold=['10-K', 'Earnings', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', 'DEF14A', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qbd63044fc6b3`)._

### ex-dev-qbdbd002b0a41

- **example_id**: `dev:qbdbd002b0a41`
- **state**: `completed`
- **query**: How has the ratio of Caterpillar Inc.’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=1.0 · gold=['10-Q', 'Earnings', '10-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=94

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbdbd002b0a41:chunk-19` | 0.4651358068632364 |  | You guys just reported a record sales and earnings. There's a view that many of your businesses are operating at peak l… |
| 2 | `qbdbd002b0a41:chunk-92` | 0.45313398453249165 |  | Operator |
| 3 | `qbdbd002b0a41:chunk-0` | 0.4473523239490718 |  | Operator |
| 4 | `qbdbd002b0a41:chunk-16` | 0.4473523239490718 |  | Operator |
| 5 | `qbdbd002b0a41:chunk-22` | 0.4473523239490718 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qbdbd002b0a41`)._

### ex-dev-qc03648d89328

- **example_id**: `dev:qc03648d89328`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Moderna’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6806060567602009 · gold=['10-K', '10-Q', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc03648d89328`)._

### ex-dev-qc187429e2dc5

- **example_id**: `dev:qc187429e2dc5`
- **state**: `completed`
- **query**: What dependency risks exist for Huntington Ingalls Industries, Inc. due to concentration of revenue in a limited number of government defense contracts?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=249

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc187429e2dc5:chunk-12` | 1.7101375442164528 | 2.0 | Current U.S. Government spending levels for defense-related or other programs may not be sustained, and future spending… |
| 2 | `qc187429e2dc5:chunk-73` | 1.5858651754679738 | 2.0 | We expect approximately 22% of the $48.1 billion total backlog as of December 31, 2023, to be converted into sales in 2… |
| 3 | `qc187429e2dc5:chunk-235` | 1.5112393338918897 |  | 107 |
| 4 | `qc187429e2dc5:chunk-197` | 1.4606122871174054 |  | 91 |
| 5 | `qc187429e2dc5:chunk-237` | 1.4564160796881052 |  | 108 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc187429e2dc5`)._

### ex-dev-qc20017b12da3

- **example_id**: `dev:qc20017b12da3`
- **state**: `completed`
- **query**: How does Moderna view the pace of mRNA vaccine development cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.6093559763921439 · skipped= · n_scored=11

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc20017b12da3:chunk-7` | 0.6609331863354807 |  | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## About Moderna (cont.) M… |
| 2 | `qc20017b12da3:chunk-4` | 0.5504677026751177 | 2.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## Clinical Updates Modern… |
| 3 | `qc20017b12da3:chunk-6` | 0.48313858818822114 | 1.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## About Moderna In over 1… |
| 4 | `qc20017b12da3:chunk-0` | 0.46766493751354626 |  | Exhibit 99.1 # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates Third quarter 2023 re… |
| 5 | `qc20017b12da3:chunk-1` | 0.40498253725716327 | 1.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## 2023 Commercial Updates… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc20017b12da3`)._

### ex-dev-qc20e5c5b254e

- **example_id**: `dev:qc20e5c5b254e`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Evergy manage equity award burn rate or share pool availability?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.8596355563650325 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc20e5c5b254e`)._

### ex-dev-qc28e5aa0181b

- **example_id**: `dev:qc28e5aa0181b`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are scenario analyses conducted by Humana Inc. for potential shifts in Medicare Advantage enrollment?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7332063582049065 · gold=['Earnings', '10-K', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc28e5aa0181b`)._

### ex-dev-qc4efe3f0f342

- **example_id**: `dev:qc4efe3f0f342`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How could global geopolitical tensions affect Mastercard's cross?border revenues?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6327646179298274 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc4efe3f0f342`)._

### ex-dev-qc6c8c1f4ddfe

- **example_id**: `dev:qc6c8c1f4ddfe`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has CMS Energy Corporation’s electric utility segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6594343379129768 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc6c8c1f4ddfe`)._

### ex-dev-qc8e6b0d72c52

- **example_id**: `dev:qc8e6b0d72c52`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Caesars Entertainment, Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc8e6b0d72c52:chunk-37` | 0.6352721394167753 |  | Yes. We expect to do both. |
| 2 | `qc8e6b0d72c52:chunk-51` | 0.6342741680154566 |  | Yes. I mean we're $4 billion now with digital doing de minimis EBITDA by 25%, we'd expect to be in the neighborhood of … |
| 3 | `qc8e6b0d72c52:chunk-0` | 0.6044968146919171 |  | Operator |
| 4 | `qc8e6b0d72c52:chunk-104` | 0.6044968146919171 |  | Operator |
| 5 | `qc8e6b0d72c52:chunk-114` | 0.6044968146919171 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc8e6b0d72c52`)._

### ex-dev-qcbbca1138c08

- **example_id**: `dev:qcbbca1138c08`
- **state**: `completed`
- **query**: What investor views emerged on Freeport-McMoRan’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.5511729162250785 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcbbca1138c08:chunk-51` | 1.073601397537952 | 1.0 | With regard to your proposed investments in the U.S., maybe even looking in Latin America, maybe could you remind us on… |
| 2 | `qcbbca1138c08:chunk-53` | 0.7618296737941117 | 1.0 | On the first part of the question, with respect to how we evaluate projects and returns, we don't target one number. We… |
| 3 | `qcbbca1138c08:chunk-15` | 0.7530988621697359 | 1.0 | Yes, Alex. Let me just add very brief very briefly that -- Kathleen makes a really good point about these relative econ… |
| 4 | `qcbbca1138c08:chunk-35` | 0.7139652617517235 | 2.0 | Given the cost -- the capital costs involved and the timing of building new projects, and the strength of your balance … |
| 5 | `qcbbca1138c08:chunk-9` | 0.6710348520082158 |  | [Operator Instructions] Our first question comes from the line of Alex Hacking with Citi. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qcbbca1138c08`)._

### ex-dev-qcdb8bc16cf2f

- **example_id**: `dev:qcdb8bc16cf2f`
- **state**: `completed`
- **query**: What guidance was offered on Jack Henry & Associates’ technology platform modernization targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9499797323370371 · gold=['Earnings', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.402555834981569 · skipped= · n_scored=126

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcdb8bc16cf2f:chunk-93` | 1.212978157641365 | 1.0 | You had mentioned that roughly 73% of your clients are now in the public cloud. I think that's up from 69% at the Inves… |
| 2 | `qcdb8bc16cf2f:chunk-53` | 1.0101513934686757 |  | Yes. Will, I appreciate the question. And I would say, this year, we gave probably a little bit more color than we have… |
| 3 | `qcdb8bc16cf2f:chunk-95` | 0.9765838528253594 | 2.0 | Sure, Chuck. I'll take it, and Mimi can add some commentary is -- yes, I think -- so it is up from where we were. I don… |
| 4 | `qcdb8bc16cf2f:chunk-0` | 0.9372320599068974 |  | Operator |
| 5 | `qcdb8bc16cf2f:chunk-100` | 0.9372320599068974 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qcdb8bc16cf2f`)._

### ex-dev-qcf796a17c330

- **example_id**: `dev:qcf796a17c330`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are scenario analyses conducted by FirstEnergy Corp. for fluctuations in electricity demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8498932729020808 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qcf796a17c330`)._

### ex-dev-qd08d64c0654c

- **example_id**: `dev:qd08d64c0654c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Fortive Corporation’s segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9979470946084208 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.8304853296300547 · skipped= · n_scored=10

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd08d64c0654c:chunk-6` | 1.0 | 2.0 | # FORTIVE CORPORATION AND SUBSIDIARIES SEGMENT INFORMATION ($ in millions) <table><tr><th></th><th colspan="2">Three Mo… |
| 2 | `qd08d64c0654c:chunk-5` | 0.95 |  | # FORTIVE CORPORATION AND SUBSIDIARIES CONSOLIDATED STATEMENTS OF EARNINGS ($ and shares in millions, except per share … |
| 3 | `qd08d64c0654c:chunk-1` | 0.9 |  | # Fortive Reports Strong Fourth Quarter and Full Year 2023 Results Introduces First Quarter and Full Year 2024 Outlook … |
| 4 | `qd08d64c0654c:chunk-2` | 0.85 | 1.0 | # Fortive Reports Strong Fourth Quarter and Full Year 2023 Results Introduces First Quarter and Full Year 2024 Outlook … |
| 5 | `qd08d64c0654c:chunk-3` | 0.8 |  | # Fortive Reports Strong Fourth Quarter and Full Year 2023 Results Introduces First Quarter and Full Year 2024 Outlook … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd08d64c0654c`)._

### ex-dev-qd177bdad4bdd

- **example_id**: `dev:qd177bdad4bdd`
- **state**: `completed`
- **query**: What pension discount rate assumption was used for year end valuation?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9751957567060058 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd177bdad4bdd:chunk-173` | 2.3260009270620037 | 2.0 | (a)A pension discount rate of 4.75% was used for the applicable plans following the transaction and remeasurement recog… |
| 2 | `qd177bdad4bdd:chunk-172` | 2.1823060956137286 | 2.0 | ######Qualified Defined Benefit Pension Plans############Retiree Medical and Life Insurance Plans###### ##2023####2022#… |
| 3 | `qd177bdad4bdd:chunk-207` | 0.6639895776316045 |  | 101 |
| 4 | `qd177bdad4bdd:chunk-171` | 0.6468685713229438 |  | Assumptions Used to Determine Benefit Obligations and FAS (Expense) Income We measure the fair value of each plan’s ass… |
| 5 | `qd177bdad4bdd:chunk-160` | 0.6057698778821355 |  | 82 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd177bdad4bdd`)._

### ex-dev-qd2e3bd55f2ee

- **example_id**: `dev:qd2e3bd55f2ee`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about HCA Healthcare’s patient engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7631679915955182 · gold=['DEF14A', 'Earnings', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd2e3bd55f2ee`)._

### ex-dev-qd422350b37cb

- **example_id**: `dev:qd422350b37cb`
- **state**: `completed`
- **query**: What investor views emerged on Martin Marietta Materials’ geographic expansion prospects within domestic markets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9452713619732751 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3295833540079424 · skipped= · n_scored=312

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd422350b37cb:chunk-47` | 1.0111207654813412 | 1.0 | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations As more fully … |
| 2 | `qd422350b37cb:chunk-49` | 0.9777655429680203 | 1.0 | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations Generally, the… |
| 3 | `qd422350b37cb:chunk-268` | 0.8677022921667551 |  | Form 10-K ♦ Page 107 |
| 4 | `qd422350b37cb:chunk-262` | 0.8660152038835647 |  | Form 10-K ♦ Page 106 |
| 5 | `qd422350b37cb:chunk-236` | 0.8580086949880289 |  | Form 10-K ♦ Page 101 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd422350b37cb`)._

### ex-dev-qd483c94f1ec6

- **example_id**: `dev:qd483c94f1ec6`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How do investors view American International Group, Inc.’s valuation relative to peers based on recent disclosures?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['DEF14A', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-K', 'DEF14A', '10-Q', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd483c94f1ec6`)._

### ex-dev-qd5c685de4d7a

- **example_id**: `dev:qd5c685de4d7a`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What themes emerged regarding the convergence of technology and biotechnology in the company operating model
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7373239404693707 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd5c685de4d7a`)._

### ex-dev-qd639a486b106

- **example_id**: `dev:qd639a486b106`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: Which general medicine candidate in obesity was identified for upcoming mid stage data readout
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.5950427489208391 · gold=['Earnings', '10-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd639a486b106`)._

### ex-dev-qd87c2da5e7da

- **example_id**: `dev:qd87c2da5e7da`
- **state**: `completed`
- **query**: How does Kenvue manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.5087403079104241 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd87c2da5e7da:chunk-70` | 0.9155571593610043 | 1.0 | # Executive Compensation <table><tr><th rowspan="14">Paul Ruh</th><th>RSUs (converted PSUs)(4)</th><th>2/8/2021</th><th… |
| 2 | `qd87c2da5e7da:chunk-65` | 0.8956908944473794 |  | # Grants of Plan-Based Awards (cont.) <table><tr><th rowspan="2">Name</th><th rowspan="2">Award</th><th rowspan="2">Gra… |
| 3 | `qd87c2da5e7da:chunk-69` | 0.7840286690023406 | 1.0 | # Outstanding Equity Awards at Fiscal Year-End (cont.) <table><tr><th></th><th></th><th></th><th></th><th colspan="4">O… |
| 4 | `qd87c2da5e7da:chunk-0` | 0.6973317134552851 |  | # UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 # SCHEDULE 14A INFORMATION Proxy Statement Pu… |
| 5 | `qd87c2da5e7da:chunk-58` | 0.6431053406379007 |  | # Executive Compensation Decision-Making (cont.) ## Stock Ownership Guidelines Kenvue has adopted stock ownership guide… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd87c2da5e7da`)._

### ex-dev-qdb9da6a1e373

- **example_id**: `dev:qdb9da6a1e373`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Packaging Corporation of America manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7118306928082477 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdb9da6a1e373`)._

### ex-dev-qdbaa829dd4cc

- **example_id**: `dev:qdbaa829dd4cc`
- **state**: `completed`
- **query**: What questions were asked about Gen Digital Inc.’s customer retention and renewal rates?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=227

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdbaa829dd4cc:chunk-18` | 1.440893870711367 |  | •The number, severity and timing of threat outbreaks and cyber security incidents; •Loss of customers or strategic part… |
| 2 | `qdbaa829dd4cc:chunk-216` | 1.077818592493972 |  | 75 |
| 3 | `qdbaa829dd4cc:chunk-37` | 1.0650863673967608 |  | ######Fiscal Year (1)#### ##2024######2023## Americas##65##%####67##% EMEA##24##%####22##% APJ##11##%####11##% |
| 4 | `qdbaa829dd4cc:chunk-214` | 1.0336316159910164 |  | 74 |
| 5 | `qdbaa829dd4cc:chunk-218` | 0.9302641707238537 |  | 76 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdbaa829dd4cc`)._

### ex-dev-qdec70f55027f

- **example_id**: `dev:qdec70f55027f`
- **state**: `completed`
- **query**: What investor views emerged on Mettler-Toledo International Inc.’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9734136950814526 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.7726578571095908 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdec70f55027f:chunk-51` | 1.1955624162305432 | 1.0 | Sure, absolutely. And again, I'll probably give you some insights into the different regions, but also in different end… |
| 2 | `qdec70f55027f:chunk-83` | 1.0967724451700707 | 2.0 | Got it. And then just on Europe, you've talked pretty cautiously about it, but I still think, unless I misheard, that y… |
| 3 | `qdec70f55027f:chunk-33` | 1.057676360874274 | 1.0 | I'll take that. Look, Shawn and I had been in China in December. And of course, we're in continued conversations with t… |
| 4 | `qdec70f55027f:chunk-101` | 0.9937621334989603 | 1.0 | Yes. Thanks, Rachel. And I'll start and then Shawn if you have some additional comments, feel free to chime in. So I th… |
| 5 | `qdec70f55027f:chunk-113` | 0.8294190371527612 |  | And then just one more, Shawn, on China. If I bake in the first quarter being down in the, call it, low to mid-20s. Doe… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdec70f55027f`)._

### ex-dev-qdfe52ef66df5

- **example_id**: `dev:qdfe52ef66df5`
- **state**: `completed`
- **query**: How has the ratio of IDEXX Laboratories’ recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9452713619732751 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.42502676863708405 · skipped= · n_scored=271

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdfe52ef66df5:chunk-127` | 1.2530183562191723 | 2.0 | (in thousands)########For the Years Ended December 31,#### ####2023####2022####2021 CAG segment revenue:############ CA… |
| 2 | `qdfe52ef66df5:chunk-103` | 1.0121973391672252 |  | F-1 |
| 3 | `qdfe52ef66df5:chunk-108` | 0.9392269681539643 |  | F-4 |
| 4 | `qdfe52ef66df5:chunk-220` | 0.9284841614281666 | 1.0 | Refer to “Note 3. Revenue” for a summary of disaggregated revenue by reportable segment and by major product and servic… |
| 5 | `qdfe52ef66df5:chunk-130` | 0.7942861853172585 |  | F-14 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdfe52ef66df5`)._

### ex-dev-qe1811f4fd3dc

- **example_id**: `dev:qe1811f4fd3dc`
- **state**: `completed`
- **query**: What questions were asked about Digital Realty Trust’s customer or tenant engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9293449960425915 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=108

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qe1811f4fd3dc:chunk-63` | 1.6033766503002669 | 1.0 | Yes. Thanks, Frank, for the question. Appreciate it. As Andy highlighted, the pipeline across the board is robust and t… |
| 2 | `qe1811f4fd3dc:chunk-79` | 0.9844008367734269 |  | Thanks, Simon. So one of our top, top, top priorities is to continue to focus on delivering an acceleration in that 0 t… |
| 3 | `qe1811f4fd3dc:chunk-97` | 0.8962543324478275 |  | The next question comes from Brandon Nispel with KeyBanc Capital Markets. |
| 4 | `qe1811f4fd3dc:chunk-7` | 0.8532433913802495 |  | Thank you, Andy. Let me jump right into our fourth quarter results. We signed a total of $110 million of new leases in … |
| 5 | `qe1811f4fd3dc:chunk-95` | 0.820735864307044 |  | Yes. So thanks, Nick. With regard to -- I think I'll go back to some of the comments I had, I think, from one of the fi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qe1811f4fd3dc`)._

### ex-dev-qe2edf9d38872

- **example_id**: `dev:qe2edf9d38872`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Charter Communications’ broadband segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qe2edf9d38872`)._

### ex-dev-qe8a08fb7bfff

- **example_id**: `dev:qe8a08fb7bfff`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Meta Platforms, Inc.’s advertising segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qe8a08fb7bfff`)._

### ex-dev-qe93fa46ab352

- **example_id**: `dev:qe93fa46ab352`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Philip Morris International view the pace of innovation cycles in reduced-risk products and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7189324940540128 · gold=['Earnings', '10-Q', '10-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qe93fa46ab352`)._

### ex-dev-qe99b7fb80e2c

- **example_id**: `dev:qe99b7fb80e2c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Intercontinental Exchange’s data services segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.665593054087714 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qe99b7fb80e2c`)._

### ex-dev-qeccd6f3b9d06

- **example_id**: `dev:qeccd6f3b9d06`
- **state**: `completed`
- **query**: What feedback surfaced on Akamai Technologies' innovation or new product pipeline prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.8869465982421278 · skipped= · n_scored=140

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeccd6f3b9d06:chunk-23` | 1.5943859647952787 | 2.0 | Yes. I'll take the first question. Yes, Gecko is not packaging. Gecko is a new capability where we're going to be offer… |
| 2 | `qeccd6f3b9d06:chunk-123` | 1.3062607181753423 | 2.0 | Okay. Yes. In terms of the question around inferencing and AI and so forth, yes, we're building full stack compute to h… |
| 3 | `qeccd6f3b9d06:chunk-45` | 1.2485600970197648 | 1.0 | So Tom, you've done a very solid job with the compute business. And in the prepared comments, you mentioned onboarding … |
| 4 | `qeccd6f3b9d06:chunk-67` | 1.2117905755012404 | 2.0 | Yes. Compute is an enormous marketplace and growing rapidly, and there's always new applications that are being created… |
| 5 | `qeccd6f3b9d06:chunk-101` | 1.2090691870804722 | 2.0 | So the new product, Gecko, it is primarily a serverless product, it sounds like. And do you have all the support there … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qeccd6f3b9d06`)._

### ex-dev-qf13afdfcadcf

- **example_id**: `dev:qf13afdfcadcf`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did Howmet Aerospace Inc.’s leadership say about Howmet Aerospace Inc.’s dividend policy?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.6734685045602393 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['8-K', '10-K', 'DEF14A', 'Earnings', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf13afdfcadcf`)._

### ex-dev-qf25e1308bae4

- **example_id**: `dev:qf25e1308bae4`
- **state**: `completed`
- **query**: Which investor concerns about the company’s China exposure did management acknowledge?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9629964747243054 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '8-K', '10-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=74

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf25e1308bae4:chunk-7` | 1.3050649552843754 |  | [Operator Instructions] Your first question comes from the line of Toshiya Hari from Goldman Sachs. |
| 2 | `qf25e1308bae4:chunk-59` | 1.0162787841982857 |  | I wanted to ask about the China business. I know that in the prepared comments, you said that you started shipping some… |
| 3 | `qf25e1308bae4:chunk-45` | 0.9589995312354846 |  | Your next question comes from the line of Ben Reitzes from Melius Research. |
| 4 | `qf25e1308bae4:chunk-39` | 0.9582900854118264 |  | Your next question comes from the line of Timothy Arcuri from UBS. |
| 5 | `qf25e1308bae4:chunk-63` | 0.9223694291820232 |  | Your next question comes from the line of Harsh Kumar from Piper Sandler. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf25e1308bae4`)._

### ex-dev-qf38450369367

- **example_id**: `dev:qf38450369367`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Nordson Corporation’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.665593054087714 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf38450369367`)._

### ex-dev-qf5b4bbe60015

- **example_id**: `dev:qf5b4bbe60015`
- **state**: `completed`
- **query**: How has Cadence Design Systems’ IP segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf5b4bbe60015:chunk-1` | 0.7641833778892128 | 1.0 | For fiscal year 2024, the company expects: •Revenue in the range of $4.60 billion to $4.66 billion •GAAP operating marg… |
| 2 | `qf5b4bbe60015:chunk-15` | 0.6475535660756556 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 3 | `qf5b4bbe60015:chunk-12` | 0.6308530041879853 |  | Condensed Consolidated Income Statements For the Three and Six Months Ended June 30, 2024 and June 30, 2023 (In thousan… |
| 4 | `qf5b4bbe60015:chunk-4` | 0.5825547927674963 |  | [Chunk Index 5] <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><t… |
| 5 | `qf5b4bbe60015:chunk-20` | 0.469407128664721 |  | Impact of Non-GAAP Adjustments on Forward Looking Operating Margin As of July 22, 2024 (Unaudited) |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf5b4bbe60015`)._

### ex-dev-qf7a3126727b8

- **example_id**: `dev:qf7a3126727b8`
- **state**: `completed`
- **query**: How does Sysco Corporation’s debt maturity profile affect liquidity and cost structure?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=148

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf7a3126727b8:chunk-145` | 0.4173281493273819 |  | # NET DEBT TO ADJUSTED EBITDA (LETTER FROM CEO AND CHAIR) (cont.) ## ADJUSTED EBITDA NON-GAAP RECONCILIATION (LETTER FR… |
| 2 | `qf7a3126727b8:chunk-77` | 0.30351675480259616 |  | # COMPENSATION DISCUSSION AND ANALYSIS <table><tr><th>Recipe For Growth SBO</th><th>Committee's Assessment of Performan… |
| 3 | `qf7a3126727b8:chunk-7` | 0.29298137812703473 |  | # PROXY STATEMENT SUMMARY (cont.) ## MEETING AGENDA The matters we will act upon at the Annual Meeting are: <table><tr>… |
| 4 | `qf7a3126727b8:chunk-121` | 0.2827918033348042 |  | # GREG D. BERTRAND (cont.) ## NEIL A. RUSSELL, II <table><tr><th>Termination Scenario</th><th>Severance Payment ($)</th… |
| 5 | `qf7a3126727b8:chunk-120` | 0.2588933530877102 |  | # GREG D. BERTRAND (cont.) ## THOMAS R. PECK, JR. <table><tr><th>Termination Scenario</th><th>Severance Payment ($)</th… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf7a3126727b8`)._

### ex-dev-qf8cbcec9fec6

- **example_id**: `dev:qf8cbcec9fec6`
- **state**: `completed`
- **query**: How has the ratio of Ingersoll Rand’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9688823411593558 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=117

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf8cbcec9fec6:chunk-113` | 0.7283478071666236 | 1.0 | # INGERSOLL RAND INC. AND SUBSIDIARIES ADJUSTED COMBINED FINANCIAL INFORMATION BY SEGMENT (Unaudited; in millions, exce… |
| 2 | `qf8cbcec9fec6:chunk-114` | 0.4164390010053466 |  | # INGERSOLL RAND INC. AND SUBSIDIARIES RECONCILIATION OF NET INCOME TO ADJUSTED EBITDA AND CASH FLOWS FROM OPERATING AC… |
| 3 | `qf8cbcec9fec6:chunk-115` | 0.3914833884169549 |  | # INGERSOLL RAND INC. AND SUBSIDIARIES RECONCILIATION OF DILUTED NET INCOME PER SHARE TO ADJUSTED DILUTED EARNINGS PER … |
| 4 | `qf8cbcec9fec6:chunk-116` | 0.3230024457983774 |  | # INGERSOLL RAND INC. AND SUBSIDIARIES UNAUDITED SUPPLEMENTAL ADJUSTED COMBINED FINANCIAL INFORMATION RECONCILIATION OF… |
| 5 | `qf8cbcec9fec6:chunk-0` | 0.3126137858688192 |  | # 2024 Proxy Statement # Notice of Annual Meeting of Stockholders <figure description="The image shows the logo of Inge… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf8cbcec9fec6`)._

### ex-dev-qf8e3e71e08c9

- **example_id**: `dev:qf8e3e71e08c9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Principal Financial Group’s retirement solutions segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf8e3e71e08c9`)._

### ex-dev-qf9c15fa46d48

- **example_id**: `dev:qf9c15fa46d48`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Live Nation Entertainment’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.788088263175707 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf9c15fa46d48`)._

### ex-dev-qfa38830206fb

- **example_id**: `dev:qfa38830206fb`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does The Clorox Company manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7168795886624337 · gold=['DEF14A', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qfa38830206fb`)._

### ex-dev-qfbef9973c7fb

- **example_id**: `dev:qfbef9973c7fb`
- **state**: `completed`
- **query**: What clarification did management provide on margin durability in the face of potential memory‑cost inflation?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=74

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qfbef9973c7fb:chunk-7` | 1.097757228629483 |  | [Operator Instructions] Your first question comes from the line of Toshiya Hari from Goldman Sachs. |
| 2 | `qfbef9973c7fb:chunk-47` | 1.0274552970683948 |  | Congratulations on the results. Colette, I wanted to talk about your comment regarding gross margins and that it should… |
| 3 | `qfbef9973c7fb:chunk-63` | 1.027357378581451 |  | Your next question comes from the line of Harsh Kumar from Piper Sandler. |
| 4 | `qfbef9973c7fb:chunk-31` | 0.9996331036951995 |  | Your next question comes from the line of Matt Ramsay from TD Cowen. |
| 5 | `qfbef9973c7fb:chunk-39` | 0.9920879267880554 |  | Your next question comes from the line of Timothy Arcuri from UBS. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qfbef9973c7fb`)._

### ex-dev-qfd572ccfcb0f

- **example_id**: `dev:qfd572ccfcb0f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Hasbro’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6107229205982195 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qfd572ccfcb0f`)._

### ex-dev-qff56bedc2f87

- **example_id**: `dev:qff56bedc2f87`
- **state**: `completed`
- **query**: What questions were asked about Globe Life Inc.’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9293449960425915 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=114

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff56bedc2f87:chunk-15` | 0.9610285256140811 |  | [Operator Instructions] Our first question comes from Jimmy Bhullar with JPMorgan. |
| 2 | `qff56bedc2f87:chunk-91` | 0.7656659128733513 |  | [Operator Instructions] And our next question is from Tom Gallagher with Evercore ISI. |
| 3 | `qff56bedc2f87:chunk-51` | 0.6993765095338472 |  | Our next question comes from Ryan Krueger with KBW. |
| 4 | `qff56bedc2f87:chunk-61` | 0.6767025785641501 |  | One thing I would add to that is that I think we're generally pleased clearly with the -- what we were seeing here in t… |
| 5 | `qff56bedc2f87:chunk-35` | 0.6569610629917583 |  | Our next question comes from John Barnidge with Piper Sandler. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qff56bedc2f87`)._

### ex-dev-qff73996028bf

- **example_id**: `dev:qff73996028bf`
- **state**: `completed`
- **query**: How has Williams-Sonoma’s management addressed supply-chain risks and efforts to enhance Williams-Sonoma’s resilience?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.27727342735504823 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff73996028bf:chunk-146` | 1.5061580195613002 |  | 76 |
| 2 | `qff73996028bf:chunk-134` | 1.471366111652333 |  | 72 |
| 3 | `qff73996028bf:chunk-137` | 1.3469066063390054 |  | 73 |
| 4 | `qff73996028bf:chunk-15` | 1.1255717462978785 | 2.0 | Table of Contents In addition, in the past, we have insourced certain aspects of our business, including certain techno… |
| 5 | `qff73996028bf:chunk-39` | 1.0595751756790306 | 2.0 | Table of Contents Elevating our World-Class Customer Service We are continuing to improve our world-class customer serv… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qff73996028bf`)._

### ex-eval-chunk-only-chunk-q0b530d

- **example_id**: `eval:chunk-only:chunk_q0b530d`
- **state**: `completed`
- **query**: How does Brown-Forman view the pace of product innovation cycles and their effect on market competitiveness in the spirits industry?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=90

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q0b530d:10-K:chunk-0` | 0.8832777441269155 |  | Operator |
| 2 | `chunk_q0b530d:10-K:chunk-18` | 0.8832777441269155 |  | Operator |
| 3 | `chunk_q0b530d:10-K:chunk-28` | 0.8832777441269155 |  | Operator |
| 4 | `chunk_q0b530d:10-K:chunk-40` | 0.8832777441269155 |  | Operator |
| 5 | `chunk_q0b530d:10-K:chunk-58` | 0.8832777441269155 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q0b530d`)._

### ex-eval-chunk-only-chunk-q29280e

- **example_id**: `eval:chunk-only:chunk_q29280e`
- **state**: `completed`
- **query**: How does Atmos Energy Corporation manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=83

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q29280e:10-K:chunk-52` | 0.8800019222190829 |  | # Grants of Plan-Based Awards (cont.) ## Grants of Plan-Based Awards for Fiscal Year 2023(a) <table><tr><th rowspan="2"… |
| 2 | `chunk_q29280e:10-K:chunk-51` | 0.7362619481833189 |  | # Named Executive Officer Compensation and Related Matters (cont.) ## All Other Compensation for Fiscal Year 2023 <tabl… |
| 3 | `chunk_q29280e:10-K:chunk-7` | 0.735581849830486 |  | # Compensation Highlights (cont.) ## Key Features of Our Executive Compensation Program ## What We Do ## What We Don't … |
| 4 | `chunk_q29280e:10-K:chunk-49` | 0.7226172562168127 |  | # Named Executive Officer Compensation and Related Matters (cont.) ## Summary Compensation Table for Fiscal Year 2023(a… |
| 5 | `chunk_q29280e:10-K:chunk-65` | 0.5883286019411129 |  | # Named Executive Officer Compensation and Related Matters (cont.) <table><tr><th></th><th>Termination Upon Death</th><… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q29280e`)._

### ex-eval-chunk-only-chunk-q2ccba5

- **example_id**: `eval:chunk-only:chunk_q2ccba5`
- **state**: `completed`
- **query**: What questions were asked about Boston Scientific’s customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q2ccba5:Earnings:chunk-11` | 0.9867115767258268 |  | [Operator Instructions] The first question comes from Robbie Marcus with JPMorgan. |
| 2 | `chunk_q2ccba5:Earnings:chunk-17` | 0.8325855601383668 |  | The next question comes from Joanne Wuensch with Citi. |
| 3 | `chunk_q2ccba5:Earnings:chunk-45` | 0.8175971392366088 |  | The next question comes from Danielle Antalffy with UBS. |
| 4 | `chunk_q2ccba5:Earnings:chunk-73` | 0.7739549873067485 |  | The next question comes from Josh Jennings with TD Cowen. |
| 5 | `chunk_q2ccba5:Earnings:chunk-81` | 0.7734653235265212 |  | The next question comes from Richard Newitter with Truist Securities. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q2ccba5`)._

### ex-eval-chunk-only-chunk-q44d295

- **example_id**: `eval:chunk-only:chunk_q44d295`
- **state**: `completed`
- **query**: How has the ratio of Amphenol Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=235

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q44d295:10-Q:chunk-38` | 1.2444678154709221 |  | ####2023####2022 First Quarter##$##0.21##$##0.20 Second Quarter####0.21####0.20 Third Quarter####0.21####0.20 Fourth Qu… |
| 2 | `chunk_q44d295:10-Q:chunk-154` | 1.0436948753437276 |  | ####2023####2022####2021 First Quarter##$##0.21##$##0.20##$##0.145 Second Quarter####0.21####0.20####0.145 Third Quarte… |
| 3 | `chunk_q44d295:10-Q:chunk-78` | 1.0436948753437276 |  | ####2023####2022####2021 First Quarter##$##0.21##$##0.20##$##0.145 Second Quarter####0.21####0.20####0.145 Third Quarte… |
| 4 | `chunk_q44d295:10-Q:chunk-93` | 0.7348635948882661 |  | AMPHENOL CORPORATION Consolidated Statements of Comprehensive Income (dollars in millions) |
| 5 | `chunk_q44d295:10-Q:chunk-90` | 0.7253478901853694 |  | AMPHENOL CORPORATION Consolidated Statements of Income (dollars and shares in millions, except per share data) |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q44d295`)._

### ex-eval-chunk-only-chunk-q5ebb5e

- **example_id**: `eval:chunk-only:chunk_q5ebb5e`
- **state**: `completed`
- **query**: How has investor sentiment shifted following The AES Corporation’s most recent earnings release?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q5ebb5e:Earnings:chunk-39` | 0.4961946811792711 |  | # EXECUTIVE COMPENSATION COMPENSATION DISCUSSION AND ANALYSIS ("CD&A") (cont.) ## Executive Summary 2023 was a strong y… |
| 2 | `chunk_q5ebb5e:Earnings:chunk-2` | 0.4437480062212296 |  | # Table of Contents (cont.) <table><tr><th>2023 Option Exercises and Stock Vested</th><th>57</th></tr><tr><td>2023 Non-… |
| 3 | `chunk_q5ebb5e:Earnings:chunk-36` | 0.37926951919592056 |  | # DIRECTOR COMPENSATION (cont.) ## Director Compensation (2023) The following table contains information concerning the… |
| 4 | `chunk_q5ebb5e:Earnings:chunk-100` | 0.36206642711808246 |  | # Reconciliation of Adjusted EBITDA <table><tr><th>$ in Millions</th><th></th><th>Year Ended Dec. 31, 2023</th></tr><tr… |
| 5 | `chunk_q5ebb5e:Earnings:chunk-107` | 0.35305364527762734 |  | # Growth Details: <table><tr><th>Goal Description</th><th>How it will be measured</th><th>Formula</th></tr><tr><td>Cont… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q5ebb5e`)._

### ex-eval-chunk-only-chunk-q829eae

- **example_id**: `eval:chunk-only:chunk_q829eae`
- **state**: `completed`
- **query**: What guidance was offered on Amazon’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q829eae:10-Q:chunk-89` | 0.9901047753086094 |  | Table of Contents Guidance We provided guidance on October 26, 2023, in our earnings release furnished on Form 8-K as s… |
| 2 | `chunk_q829eae:10-Q:chunk-35` | 0.7891239708439372 |  | 12 |
| 3 | `chunk_q829eae:10-Q:chunk-52` | 0.737870804129029 |  | 16 |
| 4 | `chunk_q829eae:10-Q:chunk-109` | 0.72034910233045 |  | Dated: October 26, 2023 47 |
| 5 | `chunk_q829eae:10-Q:chunk-59` | 0.6205387967896019 |  | 19 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q829eae`)._

### ex-eval-chunk-only-chunk-q8fc814

- **example_id**: `eval:chunk-only:chunk_q8fc814`
- **state**: `completed`
- **query**: What guidance was offered on Apollo Global Management’s fundraising targets for new investment vehicles?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '8-K', '10-Q', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=78

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q8fc814:Earnings:chunk-23` | 0.9177334652862431 |  | All right, cool. And then my violation part B is you said $200 billion to $250 billion. I kind of remember $100 billion… |
| 2 | `chunk_q8fc814:Earnings:chunk-25` | 0.82337320929896 |  | So we -- when we set out our 5-year targets a little over 2 years ago, we -- the 5-year target was to get to $150 billi… |
| 3 | `chunk_q8fc814:Earnings:chunk-63` | 0.815459412650186 |  | Sure. So ADIP 2 fundraising, going quite well. We expect to wrap it up this summer in the $4 billion to $5 billion rang… |
| 4 | `chunk_q8fc814:Earnings:chunk-0` | 0.760329575183515 |  | Operator |
| 5 | `chunk_q8fc814:Earnings:chunk-10` | 0.760329575183515 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q8fc814`)._

### ex-eval-chunk-only-chunk-q9fad72

- **example_id**: `eval:chunk-only:chunk_q9fad72`
- **state**: `completed`
- **query**: What guidance was offered on CDW Corporation’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q9fad72:10-Q:chunk-63` | 1.3718367980096067 |  | ####December 31,## (in days)##2023####2022 Days of sales outstanding (DSO)(1)##77####71 Days of supply in inventory (DI… |
| 2 | `chunk_q9fad72:10-Q:chunk-14` | 1.2927752068812355 |  | •keep pace with changes and innovation and compete effectively; •effectuate comprehensive and reliable data collection,… |
| 3 | `chunk_q9fad72:10-Q:chunk-11` | 1.2096024375638172 |  | 9 |
| 4 | `chunk_q9fad72:10-Q:chunk-197` | 0.8427056741295031 |  | 80 |
| 5 | `chunk_q9fad72:10-Q:chunk-99` | 0.7904076484978172 |  | CDW CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (dollars in millions, except per share data… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q9fad72`)._

### ex-eval-doc-q0617ad

- **example_id**: `eval:doc_q0617ad`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did F5’s leadership say about F5’s share repurchase plans?
- **S1**: top1=`8-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['8-K', '10-K', 'DEF14A', 'Earnings', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:doc_q0617ad`)._

### ex-eval-doc-q48ce69

- **example_id**: `eval:doc_q48ce69`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did energy cost inflation impact theme park utility expenses
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:doc_q48ce69`)._

### ex-eval-doc-q737b56

- **example_id**: `eval:doc_q737b56`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Deckers Outdoor Corporation’s customer retention metrics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:doc_q737b56`)._

### ex-eval-doc-qa9fda3

- **example_id**: `eval:doc_qa9fda3`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does The AES Corporation account for currency and economic volatility in its risk management disclosures?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:doc_qa9fda3`)._
