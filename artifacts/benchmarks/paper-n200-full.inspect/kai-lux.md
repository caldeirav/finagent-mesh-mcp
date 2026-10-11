# Pair `kai-lux` — `paper-n200-full`

[← compact index](../paper-n200-full.inspect.md) · **Download full HTML**: [raw](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) · [`paper-n200-full.inspect.html`](../paper-n200-full.inspect.html)

- eval_run_id: `paper-n200-retry:kai-lux`
- S1=`decision20-kai` · S2=`decision20-lux`
- row status: `completed` · completed=94 · failed_retriable=106

## Examples

### ex-dev-chunk-only-q075970f6eb46

- **example_id**: `dev:chunk-only:q075970f6eb46`
- **state**: `completed`
- **query**: What did Fastenal Company’s leadership say about Fastenal Company’s dividend policy?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=105

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q075970f6eb46:10-K:chunk-24` | 1.5621106743751865 |  | 7 |
| 2 | `q075970f6eb46:10-K:chunk-17` | 1.502612597201757 |  | 6 |
| 3 | `q075970f6eb46:10-K:chunk-39` | 1.4707901475101004 |  | 12 |
| 4 | `q075970f6eb46:10-K:chunk-101` | 0.8540447598272327 |  | 28 |
| 5 | `q075970f6eb46:10-K:chunk-82` | 0.8437656367172357 |  | 21 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q075970f6eb46`)._

### ex-dev-chunk-only-q0fd4ca04c0a5

- **example_id**: `dev:chunk-only:q0fd4ca04c0a5`
- **state**: `completed`
- **query**: How does Molina Healthcare view the pace of innovation cycles in healthcare delivery and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0fd4ca04c0a5:10-K:chunk-95` | 0.7698605986907359 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 59 |
| 2 | `q0fd4ca04c0a5:10-K:chunk-65` | 0.7530352022756202 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 48 |
| 3 | `q0fd4ca04c0a5:10-K:chunk-49` | 0.7047880733105771 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 40 |
| 4 | `q0fd4ca04c0a5:10-K:chunk-56` | 0.6942299088228039 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 43 |
| 5 | `q0fd4ca04c0a5:10-K:chunk-138` | 0.6873030037396636 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 71 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q0fd4ca04c0a5`)._

### ex-dev-chunk-only-q299865e6e67e

- **example_id**: `dev:chunk-only:q299865e6e67e`
- **state**: `completed`
- **query**: What dependency risks exist for Consolidated Edison due to concentration of revenue in a limited number of service territories or customer segments?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=286

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q299865e6e67e:10-K:chunk-6` | 1.4667148450961507 |  | 4 |
| 2 | `q299865e6e67e:10-K:chunk-16` | 1.4667121828892233 |  | 8 |
| 3 | `q299865e6e67e:10-K:chunk-3` | 1.4468062436973532 |  | 3 |
| 4 | `q299865e6e67e:10-K:chunk-27` | 1.2631911608214876 |  | 12 |
| 5 | `q299865e6e67e:10-K:chunk-285` | 1.2089098580882645 |  | 95 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q299865e6e67e`)._

### ex-dev-chunk-only-q2a401c1edf73

- **example_id**: `dev:chunk-only:q2a401c1edf73`
- **state**: `completed`
- **query**: How often is Exxon Mobil Corporation’s executive compensation program reviewed and updated?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.3176588314705989 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2a401c1edf73:10-K:chunk-83` | 0.8827744597014815 |  | # EXECUTIVE COMPENSATION TABLES ## SUMMARY COMPENSATION TABLE FOR 2023 <table><tr><th>Name and Principal Position</th><… |
| 2 | `q2a401c1edf73:10-K:chunk-61` | 0.784936013488644 | 1.0 | # OVERVIEW (cont.) ## AWARD DETERMINATION DIRECTLY TIED TO INDIVIDUAL PERFORMANCE Annual performance assessment against… |
| 3 | `q2a401c1edf73:10-K:chunk-123` | 0.7409503607762401 | 1.0 | # PAY VERSUS PERFORMANCE Please refer to the Compensation Discussion and Analysis on pages 47 to 69 for a detailed desc… |
| 4 | `q2a401c1edf73:10-K:chunk-43` | 0.7150641738469498 | 2.0 | # Table of Contents ## Compensation Committee The Compensation Committee is comprised exclusively of non-employee, inde… |
| 5 | `q2a401c1edf73:10-K:chunk-125` | 0.6986753796687312 | 1.0 | # PAY VERSUS PERFORMANCE (cont.) ## 94 ExxonMobil 2024 Proxy Statement # Table of Contents While the charts below sugge… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q2a401c1edf73`)._

### ex-dev-chunk-only-q3a71644741b7

- **example_id**: `dev:chunk-only:q3a71644741b7`
- **state**: `completed`
- **query**: What questions were asked about Conagra Brands’ customer or user engagement metrics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5157051110116301 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3a71644741b7:10-K:chunk-77` | 1.859690165301862 | 2.0 | I just wanted to clarify on promotional activity and other types of brand building that you've referenced. How does the… |
| 2 | `q3a71644741b7:10-K:chunk-67` | 1.0932413199827893 | 1.0 | Maybe I can just follow up on Rob's question from a different angle. And Sean, I'd love to hear your perspective on thi… |
| 3 | `q3a71644741b7:10-K:chunk-29` | 0.9236648905480859 | 1.0 | Yes, David, sure. Today, in our material as an example, to your point, I shared the consumption trends for our Frozen b… |
| 4 | `q3a71644741b7:10-K:chunk-61` | 0.811368722014755 | 1.0 | Sean, you have a lot of brands that skew more heavily towards lower-income consumers. You have a lot of brands that ske… |
| 5 | `q3a71644741b7:10-K:chunk-5` | 0.7551459283568104 |  | [Operator Instructions] Our first question today comes from Andrew Lazar from Barclays. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q3a71644741b7`)._

### ex-dev-chunk-only-q40d417892141

- **example_id**: `dev:chunk-only:q40d417892141`
- **state**: `completed`
- **query**: What investor views emerged on D.R. Horton’s geographic expansion prospects within new U.S. housing markets?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=27

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q40d417892141:10-K:chunk-26` | 0.551800397325486 |  | <hr />D.R. HORTON, INC. AND SUBSIDIARIES LAND AND LOT POSITION AND HOMES IN INVENTORY HOMEBUILDING SEGMENT |
| 2 | `q40d417892141:10-K:chunk-5` | 0.5357870546406139 |  | Forward-looking statements in this release include that we are well-positioned to meet changing market conditions with … |
| 3 | `q40d417892141:10-K:chunk-13` | 0.42474374824258454 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 4 | `q40d417892141:10-K:chunk-17` | 0.42474374824258454 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 5 | `q40d417892141:10-K:chunk-21` | 0.42474374824258454 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q40d417892141`)._

### ex-dev-chunk-only-q504aef305d62

- **example_id**: `dev:chunk-only:q504aef305d62`
- **state**: `completed`
- **query**: How did management describe the performance of the China market in Q4 2023?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.5574297578579929 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q504aef305d62:10-Q:chunk-15` | 2.2625988923759213 | 2.0 | Thank you for the question. Let me start with the answer here. Our brand in China is known as [ Shing Baka ] and it upl… |
| 2 | `q504aef305d62:10-Q:chunk-29` | 0.9006714409516865 |  | David, I would start with saying our guidance on margin for next year is progressive margin expansion. And remember, on… |
| 3 | `q504aef305d62:10-Q:chunk-7` | 0.8418892152778521 | 2.0 | Thank you, Laxman, and good morning, everyone. I'm very pleased to discuss our strong Q4 and full fiscal year 2023 perf… |
| 4 | `q504aef305d62:10-Q:chunk-13` | 0.6950884127638679 | 1.0 | I had a question about China, please, which I think we've heard the competitive environment there very intense. And I w… |
| 5 | `q504aef305d62:10-Q:chunk-9` | 0.46483542959146085 |  | Thank you, Rachel. At this time, we'll proceed with our normal Q&A session, which will last until the top of the hour. … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q504aef305d62`)._

### ex-dev-chunk-only-q5bb4a350edd8

- **example_id**: `dev:chunk-only:q5bb4a350edd8`
- **state**: `completed`
- **query**: How has aircraft delivery volume trended across the last four quarters for the F 35 program?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', '10-K', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.11305340175787203 · skipped= · n_scored=98

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5bb4a350edd8:10-Q:chunk-85` | 1.3684134160608579 | 1.0 | Yes. So we delivered 5 aircraft in 2023. We would expect that to triple, potentially quadruple, here in 2024. And so we… |
| 2 | `q5bb4a350edd8:10-Q:chunk-41` | 0.9558416423484954 |  | So let me get into the deliveries. Jason, we do have a handful of deliveries we expect in the first half. But for the m… |
| 3 | `q5bb4a350edd8:10-Q:chunk-39` | 0.7136649241023099 |  | Jay, just a quick clarification then one for Jim and sorry if I missed this, but the deliveries that you're expecting f… |
| 4 | `q5bb4a350edd8:10-Q:chunk-11` | 0.707264078613169 |  | I was hoping to lead off with Aero and F-35 in particular, and the margins, number one, that you're looking for in '24 … |
| 5 | `q5bb4a350edd8:10-Q:chunk-63` | 0.5979343946184912 |  | Maybe one clarification and one question. Jay, on F-35, at the end of '24, should we think about there being maybe 120 … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q5bb4a350edd8`)._

### ex-dev-chunk-only-q7b219decf5da

- **example_id**: `dev:chunk-only:q7b219decf5da`
- **state**: `completed`
- **query**: What did Everest Group, Ltd.’s leadership say about Everest Group, Ltd.’s dividend policy?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=138

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7b219decf5da:10-K:chunk-136` | 0.9162271327113124 |  | Operator |
| 2 | `q7b219decf5da:10-K:chunk-0` | 0.9101964926879527 |  | Operator |
| 3 | `q7b219decf5da:10-K:chunk-10` | 0.9101964926879527 |  | Operator |
| 4 | `q7b219decf5da:10-K:chunk-104` | 0.9101964926879527 |  | Operator |
| 5 | `q7b219decf5da:10-K:chunk-110` | 0.9101964926879527 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q7b219decf5da`)._

### ex-dev-chunk-only-q7ca4de540868

- **example_id**: `dev:chunk-only:q7ca4de540868`
- **state**: `completed`
- **query**: How does Hologic view the pace of innovation cycles in women's health diagnostics and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.11506378074895644 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ca4de540868:10-K:chunk-3` | 0.44094737273884316 |  | # Dear Fellow Stockholders: (cont.) Moving first to the Hologic Global Women's Health Index, a partnership with Gallup,… |
| 2 | `q7ca4de540868:10-K:chunk-32` | 0.436262962097014 | 1.0 | # Our Board's Role and Responsibilities (cont.) ## A Champion for Women's Health We are committed to improving women's … |
| 3 | `q7ca4de540868:10-K:chunk-2` | 0.40092490564691874 |  | # Dear Fellow Stockholders: (cont.) Moving next to Breast Health, the division grew constant currency revenue more than… |
| 4 | `q7ca4de540868:10-K:chunk-57` | 0.36976237842731274 |  | # Executive Officers (cont.) ## MR. ANDERSON ## Division President, Breast and Skeletal Health Solutions <figure descri… |
| 5 | `q7ca4de540868:10-K:chunk-8` | 0.36822770525361187 | 1.0 | # Performance Highlights (cont.) 15.6% WORLDWIDE ORGANIC REVENUE GROWTH EX. COVID-19 15.6% organic growth in constant c… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q7ca4de540868`)._

### ex-dev-chunk-only-q7ff47a7d2a20

- **example_id**: `dev:chunk-only:q7ff47a7d2a20`
- **state**: `completed`
- **query**: How does Consolidated Edison, Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5=0.5634608948312462 · skipped= · n_scored=212

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ff47a7d2a20:10-K:chunk-129` | 1.2018329914445585 | 1.0 | # OUTSTANDING EQUITY AWARDS TABLE (cont.) <table><tr><th></th><th colspan="2">STOCK AWARDS</th></tr><tr><td></td><td>Eq… |
| 2 | `q7ff47a7d2a20:10-K:chunk-164` | 1.0661284452775355 | 2.0 | # Equity Compensation Plan Information <table><tr><th>Plan category</th><th>Number of securities to be issued upon exer… |
| 3 | `q7ff47a7d2a20:10-K:chunk-78` | 0.7796349537941212 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Features of the Executive Compensation Program <table><tr><th>Type</t… |
| 4 | `q7ff47a7d2a20:10-K:chunk-127` | 0.7280799308737552 | 1.0 | # GRANTS OF PLAN-BASED AWARDS TABLE (cont.) <table><tr><th rowspan="2">Name &amp; Principal Position</th><th colspan="4… |
| 5 | `q7ff47a7d2a20:10-K:chunk-189` | 0.6946680281506156 | 2.0 | # APPENDIX D (cont.) ## ARTICLE 2. SHARES SUBJECT TO PLAN AND DURATION (a) Term. The Plan shall continue until 10 years… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q7ff47a7d2a20`)._

### ex-dev-chunk-only-q853c16a74704

- **example_id**: `dev:chunk-only:q853c16a74704`
- **state**: `completed`
- **query**: What did Tapestry’s management say about Tapestry’s margin outlook and initiatives to improve profitability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.5800690628219334 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q853c16a74704:10-K:chunk-7` | 1.200635512448199 | 2.0 | Thanks, Joanne, and good morning, everyone. Looking back at our results for the fiscal year, our commitment to discipli… |
| 2 | `q853c16a74704:10-K:chunk-47` | 1.1318474650587738 | 1.0 | Well, we are building and continue to drive a healthy business. That's been our focus, not only in China, but around th… |
| 3 | `q853c16a74704:10-K:chunk-35` | 0.9409776062075931 | 2.0 | A very brief add to your specific question as it relates to what's driving gross margin. It's really the structural dri… |
| 4 | `q853c16a74704:10-K:chunk-0` | 0.7532337860471944 |  | Operator |
| 5 | `q853c16a74704:10-K:chunk-12` | 0.7532337860471944 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q853c16a74704`)._

### ex-dev-chunk-only-q90faabe2b483

- **example_id**: `dev:chunk-only:q90faabe2b483`
- **state**: `completed`
- **query**: What operational risks related to technology or IT systems has UDR, Inc. highlighted, and how are these managed?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=31

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q90faabe2b483:10-K:chunk-0` | 0.3618501384911422 |  | # Exhibit 99.1 Vision on Wilshire I Los Angeles, CA INVESTOR PRESENTATION UDR® November 2023 Opening GRESB KUAL sector … |
| 2 | `q90faabe2b483:10-K:chunk-3` | 0.3089236592482199 |  | # UDR AT A GLANCE - DIVERSIFIED PORTFOLIO COMPOSITION UDR is diversified across markets and price points to generate ro… |
| 3 | `q90faabe2b483:10-K:chunk-29` | 0.3032685649867439 |  | # DEFINITIONS AND RECONCILIATIONS (cont.) <table><tr><th rowspan="2">In thousands, except per share and unit amounts</t… |
| 4 | `q90faabe2b483:10-K:chunk-2` | 0.30275724979379537 |  | # UDR AT A GLANCE (1)(2) UDR is a full-cycle investment that consistently generates strong total shareholder return ("T… |
| 5 | `q90faabe2b483:10-K:chunk-6` | 0.20557707941877312 |  | # ACCRETIVE CAPITAL ALLOCATION UDR has a track record of being a proficient steward of capital and can utilize various … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q90faabe2b483`)._

### ex-dev-chunk-only-q9ee9b517f484

- **example_id**: `dev:chunk-only:q9ee9b517f484`
- **state**: `completed`
- **query**: What feedback have investors provided regarding Valero Energy Corporation’s refining margin outlook?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=203

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9ee9b517f484:10-K:chunk-29` | 1.4267356115305754 |  | 10 |
| 2 | `q9ee9b517f484:10-K:chunk-24` | 1.4185812760060614 |  | 9 |
| 3 | `q9ee9b517f484:10-K:chunk-41` | 1.1532477540791306 |  | 13 |
| 4 | `q9ee9b517f484:10-K:chunk-44` | 1.1193786348410282 |  | 14 |
| 5 | `q9ee9b517f484:10-K:chunk-197` | 1.0531723900728789 |  | ________________________ |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q9ee9b517f484`)._

### ex-dev-chunk-only-qa431f3f55a5e

- **example_id**: `dev:chunk-only:qa431f3f55a5e`
- **state**: `completed`
- **query**: How are scenario analyses conducted by EPAM Systems, Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=252

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa431f3f55a5e:10-K:chunk-4` | 1.230030579490208 |  | 4 |
| 2 | `qa431f3f55a5e:10-K:chunk-63` | 1.0212641714353454 |  | 40 |
| 3 | `qa431f3f55a5e:10-K:chunk-90` | 0.97774908377648 |  | F-1 |
| 4 | `qa431f3f55a5e:10-K:chunk-86` | 0.9521374755577837 |  | 51 |
| 5 | `qa431f3f55a5e:10-K:chunk-78` | 0.9063129588154925 |  | 49 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qa431f3f55a5e`)._

### ex-dev-chunk-only-qaf2d41946676

- **example_id**: `dev:chunk-only:qaf2d41946676`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Occidental Petroleum Corporation for oil price volatility risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=126

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qaf2d41946676:10-K:chunk-124` | 0.6787077031356826 |  | Operator |
| 2 | `qaf2d41946676:10-K:chunk-0` | 0.6753641030293076 |  | Operator |
| 3 | `qaf2d41946676:10-K:chunk-10` | 0.6753641030293076 |  | Operator |
| 4 | `qaf2d41946676:10-K:chunk-100` | 0.6753641030293076 |  | Operator |
| 5 | `qaf2d41946676:10-K:chunk-110` | 0.6753641030293076 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qaf2d41946676`)._

### ex-dev-chunk-only-qb3a6bec7aedc

- **example_id**: `dev:chunk-only:qb3a6bec7aedc`
- **state**: `completed`
- **query**: What exposure to foreign exchange fluctuations did Citizens Financial Group, Inc. disclose and how is Citizens Financial Group, Inc. managing it?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.5800690628219334 · skipped= · n_scored=423

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb3a6bec7aedc:10-K:chunk-306` | 1.7661218788693858 | 2.0 | NOTE 14 - DERIVATIVES In the normal course of business, Citizens enters into derivative transactions to meet the financ… |
| 2 | `qb3a6bec7aedc:10-K:chunk-111` | 1.2653349368500304 | 1.0 | Our principal non-market risks include credit, operational, regulatory, reputational, liquidity and strategic risks. We… |
| 3 | `qb3a6bec7aedc:10-K:chunk-113` | 1.0778667550653542 | 2.0 | Non-Trading Risk Our non-trading banking activities expose us to market risk. This market risk is composed of interest … |
| 4 | `qb3a6bec7aedc:10-K:chunk-315` | 1.0606766097500275 |  | ####Year Ended December 31,## (dollars in millions)##2023##2022##2021 Amount of pre-tax net gains (losses) recognized i… |
| 5 | `qb3a6bec7aedc:10-K:chunk-137` | 1.0273050288498378 |  | ITEM 7A. QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK Quantitative and qualitative disclosures about mark… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qb3a6bec7aedc`)._

### ex-dev-chunk-only-qb7d1dfae8271

- **example_id**: `dev:chunk-only:qb7d1dfae8271`
- **state**: `completed`
- **query**: What guidance was offered on International Flavors & Fragrances Inc.’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.6992148198508501 · skipped= · n_scored=304

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb7d1dfae8271:10-K:chunk-4` | 1.1138600648219925 | 1.0 | •evaluating the profitability of whether to buy or make an ingredient; •sourcing from local countries with our own proc… |
| 2 | `qb7d1dfae8271:10-K:chunk-22` | 1.0767246446328638 | 1.0 | Our performance may be adversely impacted if we are not successful in managing our inventory and/or working capital bal… |
| 3 | `qb7d1dfae8271:10-K:chunk-296` | 0.9430431090007947 |  | ##INTERNATIONAL FLAVORS & FRAGRANCES INC.## By:####/s/ Glenn Richter Name:####Glenn Richter Title:####Executive Vice Pr… |
| 4 | `qb7d1dfae8271:10-K:chunk-85` | 0.8513109105360622 | 1.0 | ######December 31,#### (DOLLARS IN MILLIONS)####2023######2022 Raw materials##$##779####$##1,073 Work in process####406… |
| 5 | `qb7d1dfae8271:10-K:chunk-33` | 0.805360284615448 |  | SOURCE: S&P Capital IQ |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qb7d1dfae8271`)._

### ex-dev-chunk-only-qbcda53de470c

- **example_id**: `dev:chunk-only:qbcda53de470c`
- **state**: `completed`
- **query**: Which competitive advantages has Apple emphasized compared to peers?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbcda53de470c:Earnings:chunk-107` | 1.8178234413242689 |  | Sure. It's a number of things, Richard. It's the -- some things I can't talk about. It's Vision Pro. It's AI and ML. It… |
| 2 | `qbcda53de470c:Earnings:chunk-37` | 1.640804219807973 |  | Okay, very clear. And then maybe for you and Tim, you guys have been on the leading edge of innovation across hardware,… |
| 3 | `qbcda53de470c:Earnings:chunk-71` | 1.454544925192339 |  | It's really enabled us to build products that we could not build without doing it ourselves. And as you know, we like t… |
| 4 | `qbcda53de470c:Earnings:chunk-69` | 1.172577750258697 |  | Very clear. And for my follow-up, I had a philosophical question. So you guys always try to provide the best experience… |
| 5 | `qbcda53de470c:Earnings:chunk-67` | 0.9211241881965714 |  | If you kind of zoom out and look at what we've done on AI and machine learning and how we've used it, we view AI and ma… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qbcda53de470c`)._

### ex-dev-chunk-only-qd7ede96b88aa

- **example_id**: `dev:chunk-only:qd7ede96b88aa`
- **state**: `completed`
- **query**: What observations were made about TransDigm Group’s market share trends or competitive positioning in the aerospace components sector?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.07132875491150918 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd7ede96b88aa:10-K:chunk-30` | 0.5278207371135824 |  | # Corporate Governance (cont.) ## 2024 Feedback and Actions (cont.) <table><tr><th>What We Heard</th><th>What We Did</t… |
| 2 | `qd7ede96b88aa:10-K:chunk-8` | 0.5032950554237187 | 1.0 | # 2025 Annual Meeting of Shareholders (cont.) ## Composition of our Board (cont.) 31 Years of Growth and Improving Marg… |
| 3 | `qd7ede96b88aa:10-K:chunk-53` | 0.48237869074005923 |  | # Compensation Discussion and Analysis ("CD&A") (cont.) ## 31-Year Overview Over the past thirty-one years, TransDigm h… |
| 4 | `qd7ede96b88aa:10-K:chunk-52` | 0.4174036463691634 |  | # Compensation Discussion and Analysis ("CD&A") (cont.) ## 2024 Business Highlights (cont.) Executive Compensation Net … |
| 5 | `qd7ede96b88aa:10-K:chunk-47` | 0.3969543288159811 |  | # Beneficial Ownership of Equity Securities of TransDigm (cont.) <table><tr><th></th><th colspan="4">Amount and Nature … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qd7ede96b88aa`)._

### ex-dev-chunk-only-qddfea8300793

- **example_id**: `dev:chunk-only:qddfea8300793`
- **state**: `completed`
- **query**: How does Chesapeake Energy view the pace of technological advancements in drilling techniques and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=345

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qddfea8300793:10-K:chunk-138` | 1.4679494490236644 |  | 80 |
| 2 | `qddfea8300793:10-K:chunk-180` | 1.4030477982616854 |  | 102 |
| 3 | `qddfea8300793:10-K:chunk-190` | 1.366157462715562 |  | 104 |
| 4 | `qddfea8300793:10-K:chunk-183` | 1.3493317581823068 |  | 103 |
| 5 | `qddfea8300793:10-K:chunk-208` | 1.3067042497283161 |  | 108 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qddfea8300793`)._

### ex-dev-chunk-only-qed0361d5a9ae

- **example_id**: `dev:chunk-only:qed0361d5a9ae`
- **state**: `completed`
- **query**: How does Apple currently project its growth rate based on the latest management commentary?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=83

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qed0361d5a9ae:10-K:chunk-81` | 0.9423811415880511 |  | Date: August 3, 2023####Apple Inc.## ##By:####/s/ Luca Maestri ######Luca Maestri ######Senior Vice President, Chief Fi… |
| 2 | `qed0361d5a9ae:10-K:chunk-56` | 0.7892996704513815 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations This section and other pa… |
| 3 | `qed0361d5a9ae:10-K:chunk-55` | 0.7398881749231594 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 13 |
| 4 | `qed0361d5a9ae:10-K:chunk-82` | 0.7165483345104974 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 23 |
| 5 | `qed0361d5a9ae:10-K:chunk-22` | 0.7059418582554957 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 7 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qed0361d5a9ae`)._

### ex-dev-chunk-only-qeeb1c1a41ae3

- **example_id**: `dev:chunk-only:qeeb1c1a41ae3`
- **state**: `completed`
- **query**: What dependency risks exist for DuPont de Nemours, Inc. due to concentration of revenue in a limited number of end-use industries such as automotive or electronics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.3629374413984796 · skipped= · n_scored=112

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeeb1c1a41ae3:10-K:chunk-105` | 0.7794669770563871 |  | # Table of Contents Appendix A <table><tr><th rowspan="3">In Millions, Except per Share Amounts (Unaudited)</th><th></t… |
| 2 | `qeeb1c1a41ae3:10-K:chunk-43` | 0.6124695018976312 | 2.0 | # Compensation Discussion & Analysis ## Executive Summary We experienced significant volume pressure throughout 2023 as… |
| 3 | `qeeb1c1a41ae3:10-K:chunk-53` | 0.5546080674080444 | 1.0 | # Compensation Discussion & Analysis (cont.) ## Business Segment <table><tr><th rowspan="2" colspan="3">Metric / Weight… |
| 4 | `qeeb1c1a41ae3:10-K:chunk-4` | 0.4661035088800598 | 1.0 | # Proxy Statement Summary # About DuPont We are a global innovation leader with technology-based materials and solution… |
| 5 | `qeeb1c1a41ae3:10-K:chunk-108` | 0.43861437742447384 | 1.0 | # Reconciliation of "Income (loss) from continuing operations, net of tax" to "Operating EBITDA" (cont.) ## Reconciliat… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qeeb1c1a41ae3`)._

### ex-dev-chunk-only-qf3b87e3d287f

- **example_id**: `dev:chunk-only:qf3b87e3d287f`
- **state**: `completed`
- **query**: How has Bio-Techne Corporation’s leverage (e.g., debt-to-equity) changed over time?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.07132875491150918 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf3b87e3d287f:10-K:chunk-7` | 0.8616715949651577 |  | CONSOLIDATED CONDENSED BALANCE SHEETS (In thousands) (Unaudited) |
| 2 | `qf3b87e3d287f:10-K:chunk-24` | 0.5014223536038884 | 1.0 | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td colspan="5">NI… |
| 3 | `qf3b87e3d287f:10-K:chunk-0` | 0.49285090125616593 |  | Exhibit 99.1 BIO-TECHNE RELEASES THIRD QUARTER FISCAL 2024 RESULTS Minneapolis/May 1, 2024/ Bio-Techne Corporation (NAS… |
| 4 | `qf3b87e3d287f:10-K:chunk-22` | 0.4216011316302836 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 5 | `qf3b87e3d287f:10-K:chunk-14` | 0.3960398573577317 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qf3b87e3d287f`)._

### ex-dev-chunk-only-qf59bea60dc8d

- **example_id**: `dev:chunk-only:qf59bea60dc8d`
- **state**: `completed`
- **query**: How does Aon manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=145

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf59bea60dc8d:10-K:chunk-11` | 1.3418897119326842 |  | 9 |
| 2 | `qf59bea60dc8d:10-K:chunk-19` | 1.0608972964102987 |  | 12 |
| 3 | `qf59bea60dc8d:10-K:chunk-31` | 1.0383878244645692 |  | 14 |
| 4 | `qf59bea60dc8d:10-K:chunk-50` | 0.9313469099471318 |  | 17 |
| 5 | `qf59bea60dc8d:10-K:chunk-119` | 0.9196928751929759 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qf59bea60dc8d`)._

### ex-dev-q00e75b32eb34

- **example_id**: `dev:q00e75b32eb34`
- **state**: `completed`
- **query**: How has International Flavors & Fragrances Inc.’s ingredients segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9979470946084208 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.6096731708870796 · skipped= · n_scored=154

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q00e75b32eb34:chunk-135` | 1.4533967141181765 | 2.0 | ########Nine Months Ended September 30,###### (DOLLARS IN MILLIONS)####2023########2022## Segment Adjusted Operating EB… |
| 2 | `q00e75b32eb34:chunk-128` | 1.3507392385116794 | 2.0 | ########Three Months Ended September 30,###### (DOLLARS IN MILLIONS)####2023########2022## Segment Adjusted Operating E… |
| 3 | `q00e75b32eb34:chunk-44` | 1.2153616714612072 | 1.0 | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### (DOLLARS IN MILLIONS)####2023######… |
| 4 | `q00e75b32eb34:chunk-76` | 1.1134045684377787 |  | _______________________ |
| 5 | `q00e75b32eb34:chunk-60` | 1.0822031441074118 |  | 17 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q00e75b32eb34`)._

### ex-dev-q01b84969979c

- **example_id**: `dev:q01b84969979c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How many markets were mentioned as now offering ad tier pricing for Disney Plus
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.6968778680746041 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['8-K', '10-Q', 'DEF14A', '10-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q01b84969979c`)._

### ex-dev-q0346b2bc5a8b

- **example_id**: `dev:q0346b2bc5a8b`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Packaging Corporation of America’s geographic expansion prospects within the packaging industry?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7578930246759503 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q0346b2bc5a8b`)._

### ex-dev-q03a704904653

- **example_id**: `dev:q03a704904653`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did IBM’s leadership say about IBM’s dividend policy or share repurchase plans?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8457874621189229 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q03a704904653`)._

### ex-dev-q044bb2c8810c

- **example_id**: `dev:q044bb2c8810c`
- **state**: `completed`
- **query**: What investor views emerged on EQT Corporation’s geographic expansion prospects within the U.S. natural gas markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9199642183398656 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=108

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q044bb2c8810c:chunk-102` | 0.8230517820741428 |  | 41 |
| 2 | `q044bb2c8810c:chunk-107` | 0.8187166125456831 |  | Date: October 26, 2023 43 |
| 3 | `q044bb2c8810c:chunk-70` | 0.7428351565886355 |  | 27 |
| 4 | `q044bb2c8810c:chunk-61` | 0.7317111714916352 |  | 22 |
| 5 | `q044bb2c8810c:chunk-65` | 0.621207526191083 |  | EQT CORPORATION AND SUBSIDIARIES Management's Discussion and Analysis of Financial Condition and Results of Operations |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q044bb2c8810c`)._

### ex-dev-q05bfc5cb3e17

- **example_id**: `dev:q05bfc5cb3e17`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Northern Trust Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9840990003623115 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=315

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q05bfc5cb3e17:chunk-311` | 1.3217012310938003 |  | 87 |
| 2 | `q05bfc5cb3e17:chunk-14` | 1.3184165371372734 |  | 5 |
| 3 | `q05bfc5cb3e17:chunk-296` | 1.3179184752413247 |  | 82 |
| 4 | `q05bfc5cb3e17:chunk-314` | 1.2635170732688543 |  | 88 |
| 5 | `q05bfc5cb3e17:chunk-23` | 1.2524298474654612 |  | 6 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q05bfc5cb3e17`)._

### ex-dev-q09b8cfa51b60

- **example_id**: `dev:q09b8cfa51b60`
- **state**: `completed`
- **query**: How does CBRE Group, Inc. view the pace of technological innovation in real estate services and its effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=141

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q09b8cfa51b60:chunk-31` | 1.6651013153368335 |  | 10 |
| 2 | `q09b8cfa51b60:chunk-26` | 1.656811564300256 |  | 9 |
| 3 | `q09b8cfa51b60:chunk-40` | 1.4668300482036951 |  | 12 |
| 4 | `q09b8cfa51b60:chunk-53` | 1.3106502127152135 |  | 17 |
| 5 | `q09b8cfa51b60:chunk-137` | 1.2727390715323996 |  | 58 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q09b8cfa51b60`)._

### ex-dev-q0b8d55d58be2

- **example_id**: `dev:q0b8d55d58be2`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Chubb Limited’s customer retention metrics?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.708583264987264 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q0b8d55d58be2`)._

### ex-dev-q0d51e9ef12aa

- **example_id**: `dev:q0d51e9ef12aa`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did leadership measure the installed base of RTX PCs and relate it to AI‑application adoption?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5=0.5420365387171266 · gold=['8-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-Q', '10-K', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q0d51e9ef12aa`)._

### ex-dev-q0e5327ae1aff

- **example_id**: `dev:q0e5327ae1aff`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What concerns have institutional investors raised regarding regulatory risk?
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.43067655807339306 · gold=['Earnings']
- **S1 ordered**: `['8-K', '10-K', '10-Q', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q0e5327ae1aff`)._

### ex-dev-q0faf9d780cdc

- **example_id**: `dev:q0faf9d780cdc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did aeronautics sustainment hours compare with prior year levels?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6590018048024133 · gold=['10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q0faf9d780cdc`)._

### ex-dev-q11ef281af9cd

- **example_id**: `dev:q11ef281af9cd`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does United Rentals select the peer group for benchmarking executive pay?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5860880558992709 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q11ef281af9cd`)._

### ex-dev-q140516364bb4

- **example_id**: `dev:q140516364bb4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Principal Financial Group’s international expansion prospects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8498932729020808 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q140516364bb4`)._

### ex-dev-q1463bdfd6910

- **example_id**: `dev:q1463bdfd6910`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Equifax’s Workforce Solutions segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1463bdfd6910`)._

### ex-dev-q1ab49a3f086f

- **example_id**: `dev:q1ab49a3f086f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What outlook was given for Welltower Inc.’s free cash flow generation over the next year?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6995639930447636 · gold=['8-K', 'Earnings', '10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1ab49a3f086f`)._

### ex-dev-q1cfcd01ac3a1

- **example_id**: `dev:q1cfcd01ac3a1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does GE HealthCare Technologies manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7118306928082477 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1cfcd01ac3a1`)._

### ex-dev-q1ded233d05aa

- **example_id**: `dev:q1ded233d05aa`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about IDEXX Laboratories’ customer or user engagement metrics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.568268330147156 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1ded233d05aa`)._

### ex-dev-q1f722f19a821

- **example_id**: `dev:q1f722f19a821`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What answers were given about progress on Clover Vertica installations?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.43067655807339306 · gold=['Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1f722f19a821`)._

### ex-dev-q1ff3eed25e64

- **example_id**: `dev:q1ff3eed25e64`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did wage inflation trends affect labor costs in park operations
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6321922161264945 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1ff3eed25e64`)._

### ex-dev-q2173e7c263c1

- **example_id**: `dev:q2173e7c263c1`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Realty Income Corporation for recessionary or downturn risks in the commercial real estate sector?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9196027125796398 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=171

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2173e7c263c1:chunk-24` | 0.7310402917528922 |  | -9- |
| 2 | `q2173e7c263c1:chunk-20` | 0.7122115820428702 |  | -8- |
| 3 | `q2173e7c263c1:chunk-98` | 0.68578298327091 |  | experience increased costs of financing, make it difficult to refinance debt at attractive rates or at all, and may adv… |
| 4 | `q2173e7c263c1:chunk-131` | 0.665766369357222 |  | -41- |
| 5 | `q2173e7c263c1:chunk-34` | 0.6351355335265475 |  | -11- |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2173e7c263c1`)._

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

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q238a8429d152`)._

### ex-dev-q2451f8377cf4

- **example_id**: `dev:q2451f8377cf4`
- **state**: `completed`
- **query**: What dependency risks exist for Pool Corporation due to concentration of revenue in specific geographic regions or major pool supply distributors?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.515157140670655 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2451f8377cf4:chunk-121` | 0.9478042986432751 | 2.0 | Yes. I think you really -- you have to go deeper than just seasonal and year-round. Garik, I think you got to look at s… |
| 2 | `q2451f8377cf4:chunk-0` | 0.5956739503197965 |  | Operator |
| 3 | `q2451f8377cf4:chunk-102` | 0.5956739503197965 |  | Operator |
| 4 | `q2451f8377cf4:chunk-112` | 0.5956739503197965 |  | Operator |
| 5 | `q2451f8377cf4:chunk-122` | 0.5956739503197965 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2451f8377cf4`)._

### ex-dev-q24d0f908cfe3

- **example_id**: `dev:q24d0f908cfe3`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Fox Corporation’s advertising revenue growth targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8490348899399066 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q24d0f908cfe3`)._

### ex-dev-q25119b32a2f9

- **example_id**: `dev:q25119b32a2f9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What performance metrics does Snap-on Incorporated use to establish annual cash incentives or bonuses?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.5691606193790729 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q25119b32a2f9`)._

### ex-dev-q27a01443f529

- **example_id**: `dev:q27a01443f529`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Fox Corporation’s international or geographic expansion prospects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6891229721937404 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q27a01443f529`)._

### ex-dev-q28b06421804c

- **example_id**: `dev:q28b06421804c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Bio-Techne’s executives discuss plans for new product development or expansion for Bio-Techne?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6898217095818122 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q28b06421804c`)._

### ex-dev-q29a452be41cd

- **example_id**: `dev:q29a452be41cd`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Fox Corporation’s cable network programming segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7085011369669131 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q29a452be41cd`)._

### ex-dev-q29d3cb8df822

- **example_id**: `dev:q29d3cb8df822`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are investors interpreting guidance on SLB’s customer engagement metrics within its oilfield services operations?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6005469443603763 · gold=['Earnings', 'DEF14A', '8-K', '10-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q29d3cb8df822`)._

### ex-dev-q2aae5e2ea500

- **example_id**: `dev:q2aae5e2ea500`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Mondelez International’s snack foods segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2aae5e2ea500`)._

### ex-dev-q2c832749ca0b

- **example_id**: `dev:q2c832749ca0b`
- **state**: `completed`
- **query**: What dependency risks exist for Newmont Corporation due to concentration of revenue in a limited number of geographic regions or gold buyers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2c832749ca0b:chunk-209` | 1.3543881355011327 |  | 79 |
| 2 | `q2c832749ca0b:chunk-206` | 1.2918833071621791 |  | 78 |
| 3 | `q2c832749ca0b:chunk-134` | 1.1233896668889118 |  | 41 |
| 4 | `q2c832749ca0b:chunk-71` | 1.085718985459497 |  | 25 |
| 5 | `q2c832749ca0b:chunk-122` | 1.0758661866418389 |  | 38 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2c832749ca0b`)._

### ex-dev-q2d8eb319367a

- **example_id**: `dev:q2d8eb319367a`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did UDR, Inc.’s leadership address potential risks or uncertainties in forward-looking statements for its multifamily property portfolio?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.708583264987264 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2d8eb319367a`)._

### ex-dev-q2ec971ec73f9

- **example_id**: `dev:q2ec971ec73f9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What was United Rentals’ Cost of Goods Sold (COGS) in the most recent quarter?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7118306928082477 · gold=['8-K', '10-Q', '10-K', 'Earnings']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2ec971ec73f9`)._

### ex-dev-q2fe5769567d7

- **example_id**: `dev:q2fe5769567d7`
- **state**: `completed`
- **query**: How does Align Technology manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9840990003623115 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.27051296561346355 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2fe5769567d7:chunk-26` | 1.1747758291306822 |  | 10 |
| 2 | `q2fe5769567d7:chunk-68` | 0.9612493091280299 | 2.0 | 1 Includes MSUs vested during the period below 100% of the original grant as actual shares released is based on Align’s… |
| 3 | `q2fe5769567d7:chunk-66` | 0.9499244087175118 | 1.0 | As of September 30, 2023, we expect to recognize $202.1 million of total unamortized compensation costs, net of estimat… |
| 4 | `q2fe5769567d7:chunk-34` | 0.8847961266743635 |  | 12 |
| 5 | `q2fe5769567d7:chunk-39` | 0.8572643245065403 |  | 14 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2fe5769567d7`)._

### ex-dev-q318eb902f451

- **example_id**: `dev:q318eb902f451`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Franklin Resources, Inc.’s client retention and engagement metrics?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.5301648954431413 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q318eb902f451`)._

### ex-dev-q31f6fd1f392c

- **example_id**: `dev:q31f6fd1f392c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What governance processes are in place for approving changes to Targa Resources Corp.’s compensation policies?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7373239404693707 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q31f6fd1f392c`)._

### ex-dev-q33197856c996

- **example_id**: `dev:q33197856c996`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Trane Technologies’ quality metric for its HVAC system manufacturing process changed recently?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.815216305619192 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q33197856c996`)._

### ex-dev-q359aee1441c1

- **example_id**: `dev:q359aee1441c1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered regarding annual capital expenditure levels for park expansions and technology
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8497189268078151 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q359aee1441c1`)._

### ex-dev-q3ef7ce37ae77

- **example_id**: `dev:q3ef7ce37ae77`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did investors respond to Tapestry, Inc.’s discussion of supply chain risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.5733678953342115 · gold=['Earnings', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q3ef7ce37ae77`)._

### ex-dev-q3f9446fe3b94

- **example_id**: `dev:q3f9446fe3b94`
- **state**: `completed`
- **query**: How are scenario analyses conducted by American Tower Corporation for risks related to fluctuations in mobile data demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9254610488275604 · gold=['10-K', 'Earnings', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=342

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3f9446fe3b94:chunk-139` | 1.3375369989914037 |  | 75 |
| 2 | `q3f9446fe3b94:chunk-142` | 1.2820489741723602 |  | 76 |
| 3 | `q3f9446fe3b94:chunk-129` | 1.2791892743098523 |  | 70 |
| 4 | `q3f9446fe3b94:chunk-133` | 1.265220764489435 |  | 72 |
| 5 | `q3f9446fe3b94:chunk-3` | 1.258559708028957 |  | 2 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q3f9446fe3b94`)._

### ex-dev-q41a18ce876e2

- **example_id**: `dev:q41a18ce876e2`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Kellanova’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.708583264987264 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q41a18ce876e2`)._

### ex-dev-q430300b97e2f

- **example_id**: `dev:q430300b97e2f`
- **state**: `completed`
- **query**: What guidance was offered on Ingersoll Rand’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9840990003623115 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.5087403079104241 · skipped= · n_scored=152

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q430300b97e2f:chunk-141` | 1.112627998467657 | 1.0 | Sure. I think, Nicole, I think broad strokes here, we still see an opportunity here. I think is the long and short of i… |
| 2 | `q430300b97e2f:chunk-139` | 0.8700833525779103 |  | Maybe just starting with the free cash question. So conversion of 100%, all the CapEx plans. How are you guys thinking … |
| 3 | `q430300b97e2f:chunk-105` | 0.7958925440139628 | 1.0 | I appreciate that. And then maybe just follow up on productivity and efficiency of the business. Obviously, margins hav… |
| 4 | `q430300b97e2f:chunk-0` | 0.7441095010755272 |  | Operator |
| 5 | `q430300b97e2f:chunk-10` | 0.7441095010755272 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q430300b97e2f`)._

### ex-dev-q44cfaf358c37

- **example_id**: `dev:q44cfaf358c37`
- **state**: `completed`
- **query**: How do global economic or geopolitical trends shape regional market prospects for Molson Coors Beverage Company's alcoholic beverage portfolio?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.41607037852292533 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q44cfaf358c37:chunk-63` | 1.2143001954023753 | 2.0 | Yes. From a -- from an overall portfolio outside of the U.S., Chris, Canada, we do continue to see softness in the beer… |
| 2 | `q44cfaf358c37:chunk-0` | 0.9298794377219834 |  | Operator |
| 3 | `q44cfaf358c37:chunk-104` | 0.9298794377219834 |  | Operator |
| 4 | `q44cfaf358c37:chunk-110` | 0.9298794377219834 |  | Operator |
| 5 | `q44cfaf358c37:chunk-114` | 0.9298794377219834 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q44cfaf358c37`)._

### ex-dev-q4acd5677c3da

- **example_id**: `dev:q4acd5677c3da`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Hasbro’s customer or user engagement metrics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.5773534652239384 · gold=['Earnings', '8-K', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4acd5677c3da`)._

### ex-dev-q4bf1699a63fe

- **example_id**: `dev:q4bf1699a63fe`
- **state**: `completed`
- **query**: What dependency risks exist for Boston Properties, Inc. due to concentration of revenue in a limited number of geographic markets or key tenants?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.11305340175787203 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4bf1699a63fe:chunk-117` | 1.009111985090955 | 1.0 | The one other thing I would add is the performance of Reston Town Center. I mean again, the majority of our portfolio i… |
| 2 | `q4bf1699a63fe:chunk-56` | 0.6251580113481314 |  | Unknown Analyst - Analysts |
| 3 | `q4bf1699a63fe:chunk-80` | 0.5534193741428117 |  | Jing Xian Tan - Analysts |
| 4 | `q4bf1699a63fe:chunk-94` | 0.534112515249233 |  | Blaine Heck - Analysts |
| 5 | `q4bf1699a63fe:chunk-130` | 0.5249934658052947 |  | Dylan Burzinski - Analysts |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4bf1699a63fe`)._

### ex-dev-q4d8ac905167b

- **example_id**: `dev:q4d8ac905167b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Citigroup Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=894

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4d8ac905167b:chunk-220` | 1.438496334612462 |  | 95 |
| 2 | `q4d8ac905167b:chunk-2` | 1.3308173277208408 |  | 3 |
| 3 | `q4d8ac905167b:chunk-179` | 1.3097969251630361 |  | 84 |
| 4 | `q4d8ac905167b:chunk-149` | 1.2438128295059574 |  | 74 |
| 5 | `q4d8ac905167b:chunk-25` | 1.1575438235792914 |  | 14 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4d8ac905167b`)._

### ex-dev-q4e3318b7d0e9

- **example_id**: `dev:q4e3318b7d0e9`
- **state**: `completed`
- **query**: How are data privacy or cybersecurity concerns affecting industry practices relevant to water technology solutions at Xylem Inc.?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.42502676863708405 · skipped= · n_scored=329

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4e3318b7d0e9:chunk-20` | 1.096806090006126 | 2.0 | Cybersecurity incidents and related data breaches or other disruptions to our enterprise information technology and ope… |
| 2 | `q4e3318b7d0e9:chunk-209` | 1.0600637765619796 |  | 94 |
| 3 | `q4e3318b7d0e9:chunk-200` | 1.0312355149625108 |  | 93 |
| 4 | `q4e3318b7d0e9:chunk-21` | 1.0299641520910738 | 1.0 | We have implemented processes, procedures and technologies designed to detect and respond to cybersecurity incidents an… |
| 5 | `q4e3318b7d0e9:chunk-182` | 1.0272298981060064 |  | 90 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4e3318b7d0e9`)._

### ex-dev-q4f1cc6ea4ba6

- **example_id**: `dev:q4f1cc6ea4ba6`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What sentiment trends are visible around Agilent Technologies’ free cash flow outlook and capital spending plans?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7363636171343382 · gold=['Earnings', '10-Q', '10-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4f1cc6ea4ba6`)._

### ex-dev-q536ce4006bf6

- **example_id**: `dev:q536ce4006bf6`
- **state**: `completed`
- **query**: What did AutoZone’s leadership say about AutoZone’s share repurchase plans?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9840990003623115 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=7

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q536ce4006bf6:chunk-1` | 0.7316966161150957 | 1.0 | Under its share repurchase program, AutoZone repurchased 580 thousand shares of its common stock at an average price pe… |
| 2 | `q536ce4006bf6:chunk-4` | 0.3089874536415378 |  | <table><tr><td colspan="11">AutoZone's 1st Quarter Highlights - Fiscal 2024</td><td></td><td colspan="3"></td><td></td>… |
| 3 | `q536ce4006bf6:chunk-5` | 0.27164700557785626 |  | [Chunk Index 6] <table><tr><td>AutoZone's 1st Quarter Highlights - Fiscal 2024</td><td></td><td></td><td></td><td></td>… |
| 4 | `q536ce4006bf6:chunk-0` | 0.22205652640763732 |  | EXHIBIT 99.1 AutoZone 1st Quarter Domestic Same Store Sales Increase 1.2%; EPS Increases to $32.55 MEMPHIS, Tenn., Dec.… |
| 5 | `q536ce4006bf6:chunk-7` | 0.21542478594311984 |  | [Chunk Index 8] <table><tr><td colspan="23">AutoZone's 1st Quarter Highlights - Fiscal 2024</td><td></td></tr><tr><td c… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q536ce4006bf6`)._

### ex-dev-q53994e82efbb

- **example_id**: `dev:q53994e82efbb`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are scenario analyses conducted by Builders FirstSource for recessionary or downturn risks in the residential construction market?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5=0.5292991962953502 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '8-K', '10-Q', '10-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q53994e82efbb`)._

### ex-dev-q56c2aa1b3aa2

- **example_id**: `dev:q56c2aa1b3aa2`
- **state**: `completed`
- **query**: How are scenario analyses conducted by FedEx Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.19519002499605084 · skipped= · n_scored=165

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q56c2aa1b3aa2:chunk-22` | 0.40490281647129883 |  | # Corporate Governance Matters-Nominees for Election to the Board # Summary of Director Nominee Experience, Qualificati… |
| 2 | `q56c2aa1b3aa2:chunk-160` | 0.366136974521323 |  | # Fiscal 2023 Reconciliations for Fiscal 2023 AIC Plan and FY21-FY23, FY22-FY24, FY23-FY25, and FY24-FY26 LTI Plans (co… |
| 3 | `q56c2aa1b3aa2:chunk-28` | 0.36547034140202295 | 1.0 | # Corporate Governance Matters - Nominees for Election to the Board (cont.) ## Board Risk Oversight The Board of Direct… |
| 4 | `q56c2aa1b3aa2:chunk-153` | 0.3233163491617796 |  | # ADDITIONAL INFORMATION ## General Information The principal executive offices of FedEx Corporation are located at 942… |
| 5 | `q56c2aa1b3aa2:chunk-2` | 0.2892072141707349 |  | # A MESSAGE FROM OUR EXECUTIVE CHAIRMAN AND LEAD INDEPENDENT DIRECTOR To our stockholders, In connection with our 2023 … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q56c2aa1b3aa2`)._

### ex-dev-q57e9d5635f56

- **example_id**: `dev:q57e9d5635f56`
- **state**: `completed`
- **query**: What quarter did guidance point to for streaming breakeven achievement
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q57e9d5635f56:chunk-19` | 0.7411111132304748 |  | So first on DTC. I mean, pricing is about to step up. You announced the cost-cutting program, some of which might be a … |
| 2 | `q57e9d5635f56:chunk-3` | 0.5011332157325377 |  | Good afternoon. It's my pleasure to welcome everybody to the Walt Disney Company's Fourth Quarter 2023 Earnings Call. O… |
| 3 | `q57e9d5635f56:chunk-12` | 0.473399780326064 |  | Michael Nathanson - Analysts |
| 4 | `q57e9d5635f56:chunk-0` | 0.46447064721130915 |  | Operator |
| 5 | `q57e9d5635f56:chunk-10` | 0.46447064721130915 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q57e9d5635f56`)._

### ex-dev-q587ea3fc913d

- **example_id**: `dev:q587ea3fc913d`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance did Textron’s leadership give on cost structure optimization efforts?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7631679915955182 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q587ea3fc913d`)._

### ex-dev-q5ce8ea5bf1b9

- **example_id**: `dev:q5ce8ea5bf1b9`
- **state**: `completed`
- **query**: What dependency risks exist for Global Payments Inc. due to concentration of revenue in a limited number of payment processing partners or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9437153337836448 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '8-K', 'Earnings', '10-Q', 'DEF14A']`
- **S2**: nDCG@5=0.05652670087893601 · skipped= · n_scored=119

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5ce8ea5bf1b9:chunk-41` | 1.2003903478831766 |  | 17 |
| 2 | `q5ce8ea5bf1b9:chunk-49` | 1.1464057748410845 |  | 19 |
| 3 | `q5ce8ea5bf1b9:chunk-36` | 1.1094499485031153 | 1.0 | NOTE 4—REVENUES The following tables present a disaggregation of our revenues from contracts with customers by geograph… |
| 4 | `q5ce8ea5bf1b9:chunk-118` | 1.0420838987093244 |  | 49 |
| 5 | `q5ce8ea5bf1b9:chunk-99` | 1.0062998071925535 |  | NM = Not meaningful 36 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q5ce8ea5bf1b9`)._

### ex-dev-q5d75c4f1ac86

- **example_id**: `dev:q5d75c4f1ac86`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What progress was reported in international park attendance recovery relative to pre pandemic levels
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5301648954431413 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', 'DEF14A', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q5d75c4f1ac86`)._

### ex-dev-q5d883a6e3ff1

- **example_id**: `dev:q5d883a6e3ff1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How have investors reacted to The TJX Companies, Inc.’s updated guidance or forward-looking projections?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7432143929694833 · gold=['Earnings', '8-K', '10-K', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q5d883a6e3ff1`)._

### ex-dev-q5fca8aed3bbc

- **example_id**: `dev:q5fca8aed3bbc`
- **state**: `completed`
- **query**: How has the ratio of Camden Property Trust’s recurring rental income to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9416116958060755 · gold=['10-K', '8-K', 'Earnings', '10-Q']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=103

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5fca8aed3bbc:chunk-21` | 0.7468346940428784 |  | See Notes to Condensed Consolidated Financial Statements (Unaudited). 7 |
| 2 | `q5fca8aed3bbc:chunk-6` | 0.7462837773135682 |  | See Notes to Condensed Consolidated Financial Statements (Unaudited). 2 |
| 3 | `q5fca8aed3bbc:chunk-3` | 0.7451136114916477 |  | CAMDEN PROPERTY TRUST CONDENSED CONSOLIDATED STATEMENTS OF INCOME AND COMPREHENSIVE INCOME (Unaudited) |
| 4 | `q5fca8aed3bbc:chunk-9` | 0.743940990158214 |  | See Notes to Condensed Consolidated Financial Statements (Unaudited). 3 |
| 5 | `q5fca8aed3bbc:chunk-18` | 0.7434974238419637 |  | See Notes to Condensed Consolidated Financial Statements (Unaudited). 6 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q5fca8aed3bbc`)._

### ex-dev-q60107966eba4

- **example_id**: `dev:q60107966eba4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Kellanova view the pace of innovation cycles in product development and their effect on market competitiveness?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5=0.5626657637371053 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-Q', '10-K', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q60107966eba4`)._

### ex-dev-q63259a02ade0

- **example_id**: `dev:q63259a02ade0`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What does Apple's executive compensation structure look like?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.43067655807339306 · gold=['DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q63259a02ade0`)._

### ex-dev-q636b07dd9c11

- **example_id**: `dev:q636b07dd9c11`
- **state**: `completed`
- **query**: What impact could proposed legislative changes in the U.S. Credit Card Competition Act have on Mastercard?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9437153337836448 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.28911556581624914 · skipped= · n_scored=312

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q636b07dd9c11:chunk-33` | 1.2147436402822596 | 1.0 | Legal and Regulatory Payments Industry Regulation Global regulatory and legislative activity related to the payments in… |
| 2 | `q636b07dd9c11:chunk-38` | 0.9235611567235841 |  | PART I ITEM 1A. RISK FACTORS Disintermediation from stakeholders both within and outside of the payments value chain co… |
| 3 | `q636b07dd9c11:chunk-42` | 0.918561739726066 |  | PART I ITEM 1A. RISK FACTORS Stakeholder Relationships Losing a significant portion of business from one or more of our… |
| 4 | `q636b07dd9c11:chunk-279` | 0.8794549010260688 | 1.0 | PART II ITEM 8. FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA - NOTES TO CONSOLIDATED FINANCIAL STATEMENTS Interchange Li… |
| 5 | `q636b07dd9c11:chunk-31` | 0.8684174752696812 |  | PART I ITEM 1A. RISK FACTORS Item 1A. Risk factors |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q636b07dd9c11`)._

### ex-dev-q645be3b7875e

- **example_id**: `dev:q645be3b7875e`
- **state**: `completed`
- **query**: How has the ratio of Merck & Co., Inc.’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9199642183398656 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q645be3b7875e:chunk-0` | 0.781379660323389 |  | Part I - Financial Information Item 1. Financial Statements MERCK & CO., INC. AND SUBSIDIARIES CONDENSED CONSOLIDATED S… |
| 2 | `q645be3b7875e:chunk-2` | 0.7431575749987577 |  | MERCK & CO., INC. AND SUBSIDIARIES CONDENSED CONSOLIDATED STATEMENT OF COMPREHENSIVE INCOME (Unaudited, $ in millions) |
| 3 | `q645be3b7875e:chunk-45` | 0.6776256999984154 |  | ################Three Months Ended September 30,##############################Nine Months Ended September 30,##########… |
| 4 | `q645be3b7875e:chunk-15` | 0.6343526923528002 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ($ in millions)####2023######2022##… |
| 5 | `q645be3b7875e:chunk-87` | 0.6087584161268661 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ($ in millions)####2023######2022##… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q645be3b7875e`)._

### ex-dev-q64898e5ba36c

- **example_id**: `dev:q64898e5ba36c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What clarifications did analysts seek regarding Waters Corporation’s investment in chromatography and mass spectrometry innovation projects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6058748243961013 · gold=['Earnings', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q64898e5ba36c`)._

### ex-dev-q69d1505292c8

- **example_id**: `dev:q69d1505292c8`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How might global inflationary trends affect Walgreens Boots Alliance’s input costs and pricing strategies?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.8596355563650325 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q69d1505292c8`)._

### ex-dev-q6c95b5e5930d

- **example_id**: `dev:q6c95b5e5930d`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Medtronic’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.708583264987264 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q6c95b5e5930d`)._

### ex-dev-q6cdb93e02e5f

- **example_id**: `dev:q6cdb93e02e5f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What clawback or recoupment policies apply to SBA Communications Corporation’s incentive compensation in case of restatements or misconduct?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7373239404693707 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q6cdb93e02e5f`)._

### ex-dev-q6d2cc453ca8c

- **example_id**: `dev:q6d2cc453ca8c`
- **state**: `completed`
- **query**: How did analysts probe the outlook for Roper Technologies’ free cash flow generation?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9134693626978977 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3031246624382913 · skipped= · n_scored=130

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q6d2cc453ca8c:chunk-111` | 1.4263260198341645 | 1.0 | Absolutely. Yes. We're looking forward to the accretion after '24, and it will come, like I said, it's grown mid-teens,… |
| 2 | `q6d2cc453ca8c:chunk-107` | 1.1392892790122573 |  | Correct. |
| 3 | `q6d2cc453ca8c:chunk-59` | 1.0962807827358039 | 1.0 | Got it. And then just following up on the M&A side of things, leverage at 3x, obviously, strong cash flow generator. Bu… |
| 4 | `q6d2cc453ca8c:chunk-51` | 0.8242791132507964 |  | I think just more longer term on the SaaS migration. We have a little bit over $900 million in on-premise maintenance. … |
| 5 | `q6d2cc453ca8c:chunk-109` | 0.78114119955649 |  | Okay. Now going forward, if you're growing at double digits, mid-teens, that implies that you're going to get some pret… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q6d2cc453ca8c`)._

### ex-dev-q70b3e2802bf7

- **example_id**: `dev:q70b3e2802bf7`
- **state**: `completed`
- **query**: How did Tyson Foods’ average cost per pound of processed chicken trend compared to the prior period?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.515157140670655 · skipped= · n_scored=165

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q70b3e2802bf7:chunk-106` | 1.7780155725637172 | 2.0 | Third quarter – Fiscal 2024 vs Fiscal 2023 •Cost of sales increased $12 million. Higher sales volume increased cost of … |
| 2 | `q70b3e2802bf7:chunk-27` | 1.2733446105118547 |  | 8 |
| 3 | `q70b3e2802bf7:chunk-58` | 1.0567787772475719 |  | 15 |
| 4 | `q70b3e2802bf7:chunk-22` | 1.043891300979376 |  | ####June 29, 2024####September 30, 2023 Processed products##$##2,785##$##2,847 Livestock####1,429####1,594 Supplies and… |
| 5 | `q70b3e2802bf7:chunk-5` | 0.9655116087187848 |  | ######Three Months Ended##########Nine Months Ended#### ####June 29, 2024######July 1, 2023####June 29, 2024######July … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q70b3e2802bf7`)._

### ex-dev-q70e4aac30ddb

- **example_id**: `dev:q70e4aac30ddb`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did leadership respond to analyst questions about AI and personalization initiatives?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7503846658256149 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q70e4aac30ddb`)._

### ex-dev-q719082ac2068

- **example_id**: `dev:q719082ac2068`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did management characterize the evolution and strategic importance of AI factories?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6935890634491111 · gold=['Earnings', '10-K', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q719082ac2068`)._

### ex-dev-q76caada13eca

- **example_id**: `dev:q76caada13eca`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What causes differences between Weyerhaeuser Company’s cash flow and net income (e.g., timberland harvest cycles or non-cash depreciation)?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6606300841335122 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q76caada13eca`)._

### ex-dev-q78d98dc75a82

- **example_id**: `dev:q78d98dc75a82`
- **state**: `completed`
- **query**: How has Humana’s Medicare Advantage segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9416116958060755 · gold=['Earnings', '8-K', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.12389007283034911 · skipped= · n_scored=283

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q78d98dc75a82:chunk-78` | 2.0538256908667565 | 1.0 | ####################Change## ####2023####2022######2021####2023####2022 ##########(in millions)############ Medicare##$… |
| 2 | `q78d98dc75a82:chunk-128` | 1.4681566481370851 |  | ####2023####2022####2021 ########(in millions)#### Health care cost payments##$##(7,073)##$##(7,110)##$##(6,943) Health… |
| 3 | `q78d98dc75a82:chunk-176` | 1.2870552021733261 |  | ####(in millions) 2024##$##60 2025####58 2026####43 2027####33 2028####28 |
| 4 | `q78d98dc75a82:chunk-47` | 1.2262758398686475 |  | ####12/31/2018####12/31/2019####12/31/2020####12/31/2021####12/31/2022####12/31/2023 HUM##$##100##$##129##$##145##$##16… |
| 5 | `q78d98dc75a82:chunk-142` | 1.0896139633821638 |  | Statements of income######## ####For the year ended December 31, 2023####August 11, 2022 through December 31, 2022 ####… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q78d98dc75a82`)._

### ex-dev-q79acb772ca6b

- **example_id**: `dev:q79acb772ca6b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Ingersoll Rand Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9411655511901171 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=290

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q79acb772ca6b:chunk-258` | 1.281069247181919 |  | 93 |
| 2 | `q79acb772ca6b:chunk-289` | 1.1927103441164835 |  | 105 |
| 3 | `q79acb772ca6b:chunk-280` | 1.1765057070369735 |  | 102 |
| 4 | `q79acb772ca6b:chunk-242` | 1.1717054345205529 |  | 88 |
| 5 | `q79acb772ca6b:chunk-282` | 1.1657382607151237 |  | 103 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q79acb772ca6b`)._

### ex-dev-q79ae686681b7

- **example_id**: `dev:q79ae686681b7`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Best Buy’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7363636171343382 · gold=['10-K', '10-Q', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q79ae686681b7`)._

### ex-dev-q7b42f1295dc1

- **example_id**: `dev:q7b42f1295dc1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are scenario analyses conducted by Fiserv for recessionary or downturn risks?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7373239404693707 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-Q', '8-K', '10-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7b42f1295dc1`)._

### ex-dev-q7c284aabbba4

- **example_id**: `dev:q7c284aabbba4`
- **state**: `completed`
- **query**: What dependency risks exist for Moderna, Inc. due to concentration of revenue in a limited number of vaccine products or geographic markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9411655511901171 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7c284aabbba4:chunk-80` | 0.9759168388794501 |  | Operator |
| 2 | `q7c284aabbba4:chunk-0` | 0.9720175907217132 |  | Operator |
| 3 | `q7c284aabbba4:chunk-12` | 0.9720175907217132 |  | Operator |
| 4 | `q7c284aabbba4:chunk-18` | 0.9720175907217132 |  | Operator |
| 5 | `q7c284aabbba4:chunk-26` | 0.9720175907217132 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7c284aabbba4`)._

### ex-dev-q7e2586950d8e

- **example_id**: `dev:q7e2586950d8e`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Ball Corporation’s beverage packaging segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7e2586950d8e`)._

### ex-dev-q7eb4e8a11956

- **example_id**: `dev:q7eb4e8a11956`
- **state**: `completed`
- **query**: Summarize Luca Maestri's recent commentary on the gross margin outlook given current FX headwinds.
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7eb4e8a11956:chunk-7` | 1.0852068852200978 |  | Thank you, Tim, and good afternoon, everyone. Revenue for the September quarter was $89.5 billion, down less than 1% fr… |
| 2 | `q7eb4e8a11956:chunk-29` | 0.8653576572912288 |  | As you've seen from our results in Q4 and the guidance for Q1, we're obviously experiencing very strong levels of gross… |
| 3 | `q7eb4e8a11956:chunk-85` | 0.8468814447583746 |  | I have 2 of them, too. First one, Luca, thanks for the color on gross margin. And when I look at it over the last 4 qua… |
| 4 | `q7eb4e8a11956:chunk-25` | 0.8027611892349297 |  | Yes. If you look at how we did in Greater China for the quarter, we came in at, on revenue basis, minus 2. But one thin… |
| 5 | `q7eb4e8a11956:chunk-109` | 0.7852092730427053 |  | And I would add, Richard, on this front, some of the investments that we're making in R&D are also one of the drivers f… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7eb4e8a11956`)._

### ex-dev-q7eb5b91e2366

- **example_id**: `dev:q7eb5b91e2366`
- **state**: `completed`
- **query**: What dependency risks exist for Becton, Dickinson and Company due to concentration of revenue in a limited number of healthcare providers or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=76

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7eb5b91e2366:chunk-69` | 0.7429330177353237 |  | Thanks for the question, Rich. |
| 2 | `q7eb5b91e2366:chunk-0` | 0.5938324939741508 |  | Operator |
| 3 | `q7eb5b91e2366:chunk-16` | 0.5938324939741508 |  | Operator |
| 4 | `q7eb5b91e2366:chunk-26` | 0.5938324939741508 |  | Operator |
| 5 | `q7eb5b91e2366:chunk-32` | 0.5938324939741508 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7eb5b91e2366`)._

### ex-dev-q7ebef55d671d

- **example_id**: `dev:q7ebef55d671d`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Chipotle’s supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6681681713476765 · gold=['DEF14A', '10-Q', '10-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7ebef55d671d`)._

### ex-dev-q7ed5279a28b4

- **example_id**: `dev:q7ed5279a28b4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did Teradyne’s management note about Teradyne’s operational scalability as test equipment demand volumes grow or contract?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6394274958655697 · gold=['Earnings', '10-Q', '10-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7ed5279a28b4`)._

### ex-dev-q811679c2d742

- **example_id**: `dev:q811679c2d742`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What challenges are noted regarding scaling infrastructure or capacity for renewable energy integration to meet growth?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.6734685045602393 · gold=['10-K', '8-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-Q', '8-K', 'Earnings', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q811679c2d742`)._

### ex-dev-q84038a74fd59

- **example_id**: `dev:q84038a74fd59`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How many organizations were reported to be using Azure OpenAI Service
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.7091346207140341 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['8-K', '10-K', '10-Q', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q84038a74fd59`)._

### ex-dev-q86f79f57d973

- **example_id**: `dev:q86f79f57d973`
- **state**: `completed`
- **query**: What did Linde’s leadership say about Linde’s dividend policy or share repurchase plans?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9278143341459562 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5=0.3716702184910473 · skipped= · n_scored=287

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q86f79f57d973:chunk-15` | 1.6046224629003538 | 2.0 | (1)On February 28, 2022 the company's board of directors approved the repurchase of $10.0 billion of its ordinary share… |
| 2 | `q86f79f57d973:chunk-225` | 1.4206118556704102 |  | 90 |
| 3 | `q86f79f57d973:chunk-195` | 1.4031137804497367 |  | 80 |
| 4 | `q86f79f57d973:chunk-241` | 1.3295503555523422 |  | 94 |
| 5 | `q86f79f57d973:chunk-247` | 1.2667907148228528 |  | 97 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q86f79f57d973`)._

### ex-dev-q88819064dbb7

- **example_id**: `dev:q88819064dbb7`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Dollar Tree, Inc.’s geographic expansion prospects within the domestic discount retail market?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8596355563650325 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q88819064dbb7`)._

### ex-dev-q88db5d96c8dd

- **example_id**: `dev:q88db5d96c8dd`
- **state**: `completed`
- **query**: How does Bristol-Myers Squibb manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9359826917490579 · gold=['10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=176

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88db5d96c8dd:chunk-27` | 1.3014167254206102 |  | 10 |
| 2 | `q88db5d96c8dd:chunk-38` | 1.0101375470775589 |  | 13 |
| 3 | `q88db5d96c8dd:chunk-149` | 0.9311775042776194 |  | 50 |
| 4 | `q88db5d96c8dd:chunk-86` | 0.9084669097964354 |  | Note 16. EQUITY The following table summarizes changes in equity for the nine months ended September 30, 2023: |
| 5 | `q88db5d96c8dd:chunk-175` | 0.8530255172023011 |  | 58 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q88db5d96c8dd`)._

### ex-dev-q89953a08e494

- **example_id**: `dev:q89953a08e494`
- **state**: `completed`
- **query**: How does Globe Life Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9416116958060755 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5=0.14115639177619477 · skipped= · n_scored=125

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89953a08e494:chunk-100` | 1.1296458351633374 |  | # PAY VERSUS PERFORMANCE (cont.) <table><tr><th></th><th></th><th colspan="5">PEO-2</th></tr><tr><td rowspan="2">Year</… |
| 2 | `q89953a08e494:chunk-80` | 1.1211953634467058 | 1.0 | # 2023 GRANTS OF PLAN-BASED AWARDS <table><tr><th></th><th rowspan="2">Award Type</th><th rowspan="2">Grant Date</th><t… |
| 3 | `q89953a08e494:chunk-85` | 1.0030594057882374 |  | # OUTSTANDING EQUITY AWARDS AT FISCAL YEAR-END 2023 (continued) (cont.) <table><tr><th></th><th colspan="5">Option Awar… |
| 4 | `q89953a08e494:chunk-76` | 0.8715999558618129 |  | # EXECUTIVE COMPENSATION SUMMARY COMPENSATION TABLE (cont.) <table><tr><th>Name and Principal Position</th><th>Year</th… |
| 5 | `q89953a08e494:chunk-66` | 0.7314244564154995 | 1.0 | # Assessment of 2023 Advisory Vote on Executive Compensation (cont.) ## Long-Term Equity Incentives We award long-term … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q89953a08e494`)._

### ex-dev-q89fb186f5e49

- **example_id**: `dev:q89fb186f5e49`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Linde’s international or geographic expansion prospects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.788088263175707 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q89fb186f5e49`)._

### ex-dev-q8b55a229e784

- **example_id**: `dev:q8b55a229e784`
- **state**: `completed`
- **query**: How has the ratio of C.H. Robinson Worldwide’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9639404333166532 · gold=['10-K', '10-Q']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=112

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8b55a229e784:chunk-41` | 1.1607700167315917 | 1.0 | NOTE 9. REVENUE FROM CONTRACTS WITH CUSTOMERS A summary of our total revenues disaggregated by major service line and t… |
| 2 | `q8b55a229e784:chunk-8` | 0.9945479493297713 |  | 5 |
| 3 | `q8b55a229e784:chunk-51` | 0.6693882293848646 |  | 17 |
| 4 | `q8b55a229e784:chunk-35` | 0.6550225677204741 |  | 13 |
| 5 | `q8b55a229e784:chunk-22` | 0.636134786441783 |  | ####NAST####Global Forwarding####All Other and Corporate####Total Remainder of 2023##$##2,021##$##1,007##$##266##$##3,2… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q8b55a229e784`)._

### ex-dev-q8ba6a388d681

- **example_id**: `dev:q8ba6a388d681`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Broadcom’s customer retention metrics?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.5431546067270766 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q8ba6a388d681`)._

### ex-dev-q8cc1033cf552

- **example_id**: `dev:q8cc1033cf552`
- **state**: `completed`
- **query**: What guidance did The Sherwin-Williams Company’s leadership provide on debt reduction or leverage targets for The Sherwin-Williams Company?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9499797323370371 · gold=['10-K', 'Earnings', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=114

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8cc1033cf552:chunk-14` | 1.1631454554308542 |  | 6 |
| 2 | `q8cc1033cf552:chunk-113` | 0.7338941356511107 |  | ####THE SHERWIN-WILLIAMS COMPANY October 24, 2023##By:##/s/ Jane M. Cronin ####Jane M. Cronin ####Senior Vice President… |
| 3 | `q8cc1033cf552:chunk-67` | 0.6835773294078243 |  | 23 |
| 4 | `q8cc1033cf552:chunk-54` | 0.6831456531720725 |  | 20 |
| 5 | `q8cc1033cf552:chunk-78` | 0.6607433083105119 |  | 26 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q8cc1033cf552`)._

### ex-dev-q8e053e02a010

- **example_id**: `dev:q8e053e02a010`
- **state**: `completed`
- **query**: What dependency risks exist for International Paper Company due to concentration of revenue in a limited number of end-use paper and packaging markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=225

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8e053e02a010:chunk-0` | 0.4421696421440676 |  | # UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 SCHEDULE 14A (Rule 14a-101) INFORMATION REQUI… |
| 2 | `q8e053e02a010:chunk-6` | 0.3894736016673248 |  | # Table of Contents (cont.) ## Index of Frequently Requested Information <table><tr><th>Our Commitment to Sustainabilit… |
| 3 | `q8e053e02a010:chunk-140` | 0.3407479885323588 |  | # Supplemental (cont.) ## Most Important Performance Measures (cont.) Table of Contents The image shows a close-up view… |
| 4 | `q8e053e02a010:chunk-217` | 0.3379198691741175 |  | # Table of Contents (cont.) ## Appendix -Reconciliations of Non-GAAP Measures (cont.) <table><tr><th>In millions, for t… |
| 5 | `q8e053e02a010:chunk-67` | 0.3330212625109516 |  | # Overview of Our CD&A <table><tr><th>Introduction</th><th>47</th><th>Short-Term Incentive</th><th>63</th></tr><tr><td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q8e053e02a010`)._

### ex-dev-q8e26f08be2bc

- **example_id**: `dev:q8e26f08be2bc`
- **state**: `completed`
- **query**: What challenges arise for Vertex Pharmaceuticals from data privacy regulations and handling of patient data?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9767362801495987 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.33916020527361607 · skipped= · n_scored=285

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8e26f08be2bc:chunk-52` | 1.190112727681014 | 2.0 | research institution that has not complied with HIPAA’s requirements for disclosing such information. In addition, the … |
| 2 | `q8e26f08be2bc:chunk-111` | 1.0590309096186519 |  | 80 |
| 3 | `q8e26f08be2bc:chunk-125` | 1.0352473243003926 |  | 90 |
| 4 | `q8e26f08be2bc:chunk-134` | 0.9622980148995901 |  | 93 |
| 5 | `q8e26f08be2bc:chunk-127` | 0.9612524125715507 |  | 91 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q8e26f08be2bc`)._

### ex-dev-q909c4baef1ee

- **example_id**: `dev:q909c4baef1ee`
- **state**: `completed`
- **query**: How did analysts frame queries about Truist Financial Corporation’s shareholder returns, including dividends?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9979470946084208 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=124

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q909c4baef1ee:chunk-110` | 0.6927340483411522 |  | Manan Gosalia - Analysts |
| 2 | `q909c4baef1ee:chunk-114` | 0.6927340483411522 |  | Manan Gosalia - Analysts |
| 3 | `q909c4baef1ee:chunk-46` | 0.6918716513226673 |  | Elyse Greenspan - Analysts |
| 4 | `q909c4baef1ee:chunk-40` | 0.6673759732652054 |  | Michael Mayo - Analysts |
| 5 | `q909c4baef1ee:chunk-44` | 0.6673759732652054 |  | Michael Mayo - Analysts |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q909c4baef1ee`)._

### ex-dev-q93fb2b2861c4

- **example_id**: `dev:q93fb2b2861c4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Church & Dwight view the pace of product innovation cycles and their effect on market competitiveness?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5855572724275795 · gold=['10-K', '8-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q93fb2b2861c4`)._

### ex-dev-q95535bca90c9

- **example_id**: `dev:q95535bca90c9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Wells Fargo’s average cost per loan origination trend compared to the prior period?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6775575206537102 · gold=['10-Q', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q95535bca90c9`)._

### ex-dev-q95790ca7c1f5

- **example_id**: `dev:q95790ca7c1f5`
- **state**: `completed`
- **query**: What did Dayforce Inc.’s leadership say about Dayforce Inc.’s share repurchase plans?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9327783893101107 · gold=['10-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q95790ca7c1f5:chunk-0` | 1.1031195274402505 |  | Operator |
| 2 | `q95790ca7c1f5:chunk-73` | 0.7075403095107385 |  | Brad, good to speak with you again. The answer to the question is really no changes. The guidance philosophy I have is … |
| 3 | `q95790ca7c1f5:chunk-123` | 0.7040191682684812 |  | We always look at the float as a really nice piece of our business, and we'll take it when it's here. But as it goes aw… |
| 4 | `q95790ca7c1f5:chunk-107` | 0.5194658510474647 |  | Mark, good to speak with you again. And thanks for the question. Yes. So float, it steps up slightly from -- in our gui… |
| 5 | `q95790ca7c1f5:chunk-10` | 0.5152953216807202 |  | Matthew Wells - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q95790ca7c1f5`)._

### ex-dev-q9597b3e4d1b2

- **example_id**: `dev:q9597b3e4d1b2`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has investor sentiment shifted following Archer-Daniels-Midland Company’s most recent earnings release?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.8307820888596468 · gold=['10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9597b3e4d1b2`)._

### ex-dev-q98c606bb3ce7

- **example_id**: `dev:q98c606bb3ce7`
- **state**: `completed`
- **query**: What litigation or dispute risks did Williams-Sonoma, Inc. identify and what is the potential financial impact for Williams-Sonoma, Inc.?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5=0.1843821566693812 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q98c606bb3ce7:chunk-30` | 1.3482676115783672 | 1.0 | Table of Contents ITEM 3. LEGAL PROCEEDINGS We are involved in lawsuits, claims and proceedings incident to the ordinar… |
| 2 | `q98c606bb3ce7:chunk-7` | 1.2492437357043515 | 1.0 | Table of Contents Risks Related to Technology •We are exposed to cybersecurity risks and costs associated with credit c… |
| 3 | `q98c606bb3ce7:chunk-146` | 1.0422493102386177 |  | 76 |
| 4 | `q98c606bb3ce7:chunk-134` | 1.0025739459854284 |  | 72 |
| 5 | `q98c606bb3ce7:chunk-137` | 0.9418653298072981 |  | 73 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q98c606bb3ce7`)._

### ex-dev-q99a077efaab0

- **example_id**: `dev:q99a077efaab0`
- **state**: `completed`
- **query**: What dependency risks exist for Align Technology due to concentration of revenue in a limited number of orthodontic practices or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99a077efaab0:chunk-106` | 0.7448169196160263 |  | Operator |
| 2 | `q99a077efaab0:chunk-112` | 0.7448169196160263 |  | Operator |
| 3 | `q99a077efaab0:chunk-122` | 0.7448169196160263 |  | Operator |
| 4 | `q99a077efaab0:chunk-126` | 0.7448169196160263 |  | Operator |
| 5 | `q99a077efaab0:chunk-22` | 0.7448169196160263 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q99a077efaab0`)._

### ex-dev-q99ec5f1aeea5

- **example_id**: `dev:q99ec5f1aeea5`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Federal Realty Investment Trust’s tenant retention metrics?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.5964940466933754 · gold=['Earnings', '8-K', '10-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q99ec5f1aeea5`)._

### ex-dev-q9a5cfe35fecd

- **example_id**: `dev:q9a5cfe35fecd`
- **state**: `completed`
- **query**: What dependency risks exist for CMS Energy Corporation due to concentration of revenue in a limited number of geographic regions or key utility customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '8-K', '10-Q', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=194

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9a5cfe35fecd:chunk-9` | 1.6270952043414848 |  | 4 |
| 2 | `q9a5cfe35fecd:chunk-15` | 1.6207804061732036 |  | 7 |
| 3 | `q9a5cfe35fecd:chunk-11` | 1.6126065518927488 |  | 5 |
| 4 | `q9a5cfe35fecd:chunk-7` | 1.6110327751140814 |  | 3 |
| 5 | `q9a5cfe35fecd:chunk-13` | 1.5635851291413707 |  | 6 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9a5cfe35fecd`)._

### ex-dev-q9c255237096a

- **example_id**: `dev:q9c255237096a`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What perquisites or fringe benefits are included in The AES Corporation’s executive compensation disclosures?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.43067655807339306 · gold=['DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9c255237096a`)._

### ex-dev-q9dd3907388e3

- **example_id**: `dev:q9dd3907388e3`
- **state**: `completed`
- **query**: How does Duke Energy view the pace of innovation cycles in renewable energy technologies and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9935051443580323 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9dd3907388e3:chunk-29` | 0.5754089222351394 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 2 | `q9dd3907388e3:chunk-43` | 0.5274771726588062 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 3 | `q9dd3907388e3:chunk-45` | 0.5274771726588062 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 4 | `q9dd3907388e3:chunk-47` | 0.5274771726588062 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 5 | `q9dd3907388e3:chunk-49` | 0.5274771726588062 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9dd3907388e3`)._

### ex-dev-q9f32df79b0d7

- **example_id**: `dev:q9f32df79b0d7`
- **state**: `completed`
- **query**: How does Capital One view the pace of digital banking innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9196027125796398 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=4

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9f32df79b0d7:chunk-0` | 0.2745235196167059 | 1.0 | Exhibit 99.1 News Release <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><… |
| 2 | `q9f32df79b0d7:chunk-3` | 0.22324074098527197 |  | Capital One Financial Corporation (www.capitalone.com) is a financial holding company which, along with its subsidiarie… |
| 3 | `q9f32df79b0d7:chunk-1` | 0.19648055190954095 |  | •Total net revenue increased 4 percent to $9.4 billion. •Total non-interest expense increased 1 percent to $4.9 billion… |
| 4 | `q9f32df79b0d7:chunk-2` | 0.10998739010475625 |  | •Auto average loans decreased $493 million, or 1 percent, to $75.7 billion. ◦Commercial Banking average loans decreased… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9f32df79b0d7`)._

### ex-dev-qa057a3d428a2

- **example_id**: `dev:qa057a3d428a2`
- **state**: `completed`
- **query**: What dependency risks exist for McKesson Corporation due to concentration of revenue in a limited number of pharmaceutical manufacturers or healthcare providers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa057a3d428a2:chunk-24` | 1.4714304192766945 |  | 11 |
| 2 | `qa057a3d428a2:chunk-27` | 1.4096642435795117 |  | 12 |
| 3 | `qa057a3d428a2:chunk-135` | 1.1757726338789962 |  | 57 |
| 4 | `qa057a3d428a2:chunk-85` | 1.0800799721522703 |  | 32 |
| 5 | `qa057a3d428a2:chunk-19` | 0.9538427242315316 |  | See Financial Notes 8 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa057a3d428a2`)._

### ex-dev-qa33b36ffd2c1

- **example_id**: `dev:qa33b36ffd2c1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Garmin’s fitness segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6594343379129768 · gold=['10-Q', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa33b36ffd2c1`)._

### ex-dev-qa5c748248a5b

- **example_id**: `dev:qa5c748248a5b`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of MSCI’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6594343379129768 · gold=['10-Q', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa5c748248a5b`)._

### ex-dev-qa602975e3d19

- **example_id**: `dev:qa602975e3d19`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Mondelez International’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6368704287129855 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa602975e3d19`)._

### ex-dev-qa9744c8552ed

- **example_id**: `dev:qa9744c8552ed`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did analysts question TJX Companies’ management on their strategies for responsible sourcing and sustainable supply chain practices?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7426242736819336 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa9744c8552ed`)._

### ex-dev-qab00fabe02dc

- **example_id**: `dev:qab00fabe02dc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Rockwell Automation’s executives address regulatory or policy developments and their potential implications for industrial automation solutions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6898217095818122 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qab00fabe02dc`)._

### ex-dev-qaf55b76bfcad

- **example_id**: `dev:qaf55b76bfcad`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: Which partnership with a major telecommunications provider was highlighted for bundling offers
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.5967557363289646 · gold=['Earnings', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '8-K', 'DEF14A', '10-Q', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qaf55b76bfcad`)._

### ex-dev-qb00e9c27fd32

- **example_id**: `dev:qb00e9c27fd32`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Monster Beverage Corporation’s segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7659463877163701 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb00e9c27fd32`)._

### ex-dev-qb2123a701a82

- **example_id**: `dev:qb2123a701a82`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Atmos Energy view the pace of pipeline technology innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6252347221754821 · gold=['DEF14A', '8-K', '10-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb2123a701a82`)._

### ex-dev-qb22cbf2f4782

- **example_id**: `dev:qb22cbf2f4782`
- **state**: `completed`
- **query**: How has Apple management recently commented on services attach rates and other value-added offerings?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.944847956559586 · gold=['10-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=156

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb22cbf2f4782:chunk-152` | 0.8628314674823323 |  | Date: November 2, 2023####Apple Inc.## ##By:####/s/ Luca Maestri ######Luca Maestri ######Senior Vice President, Chief … |
| 2 | `qb22cbf2f4782:chunk-155` | 0.7944393352699639 |  | Apple Inc. \| 2023 Form 10-K \| 58 |
| 3 | `qb22cbf2f4782:chunk-144` | 0.7839041174569956 |  | Apple Inc. \| 2023 Form 10-K \| 54 |
| 4 | `qb22cbf2f4782:chunk-92` | 0.7722482160221577 |  | Apple Inc. \| 2023 Form 10-K \| 39 |
| 5 | `qb22cbf2f4782:chunk-148` | 0.7716063047520817 |  | Apple Inc. \| 2023 Form 10-K \| 56 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb22cbf2f4782`)._

### ex-dev-qb26bf8457b0f

- **example_id**: `dev:qb26bf8457b0f`
- **state**: `completed`
- **query**: What risks are associated with opening new healthcare facilities for Universal Health Services, Inc. when patient demand is uncertain?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9411655511901171 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=290

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb26bf8457b0f:chunk-143` | 1.4779163483205684 |  | 80 |
| 2 | `qb26bf8457b0f:chunk-147` | 1.424522906058973 |  | 82 |
| 3 | `qb26bf8457b0f:chunk-153` | 1.4217971075328455 |  | 85 |
| 4 | `qb26bf8457b0f:chunk-151` | 1.4120035334133587 |  | 84 |
| 5 | `qb26bf8457b0f:chunk-145` | 1.3953575354138876 |  | 81 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb26bf8457b0f`)._

### ex-dev-qb35a5efa65ce

- **example_id**: `dev:qb35a5efa65ce`
- **state**: `completed`
- **query**: What dependency risks exist for Evergy, Inc. due to concentration of revenue in a limited number of service territories or key industrial customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9882048111454694 · gold=['10-K', 'Earnings', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '8-K', '10-Q', 'DEF14A']`
- **S2**: nDCG@5=0.41607037852292533 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb35a5efa65ce:chunk-41` | 0.8811005799614829 | 2.0 | In terms of earnings sensitivity, I wouldn't call it linear from that perspective. These are obviously large industrial… |
| 2 | `qb35a5efa65ce:chunk-43` | 0.8385999341179398 |  | I would just echo Kirk's comment, though, on -- this is David, that the -- these are industrial customers, which, as yo… |
| 3 | `qb35a5efa65ce:chunk-20` | 0.4873657248875085 |  | Michael Sullivan - Analysts |
| 4 | `qb35a5efa65ce:chunk-24` | 0.4873657248875085 |  | Michael Sullivan - Analysts |
| 5 | `qb35a5efa65ce:chunk-28` | 0.4873657248875085 |  | Michael Sullivan - Analysts |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb35a5efa65ce`)._

### ex-dev-qb500a9b42ef8

- **example_id**: `dev:qb500a9b42ef8`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of CMS Energy Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6327646179298274 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb500a9b42ef8`)._

### ex-dev-qb590e4e6d1ec

- **example_id**: `dev:qb590e4e6d1ec`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of PG&E Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.788088263175707 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb590e4e6d1ec`)._

### ex-dev-qba0102803c57

- **example_id**: `dev:qba0102803c57`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Kimco Realty Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=332

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba0102803c57:chunk-242` | 1.4315370516733399 |  | 95 |
| 2 | `qba0102803c57:chunk-158` | 1.4129772057327912 |  | 80 |
| 3 | `qba0102803c57:chunk-181` | 1.2910743562431068 |  | 84 |
| 4 | `qba0102803c57:chunk-276` | 1.2720939489894314 |  | 102 |
| 5 | `qba0102803c57:chunk-148` | 1.2671224666851857 |  | 78 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qba0102803c57`)._

### ex-dev-qba50bc033945

- **example_id**: `dev:qba50bc033945`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What commentary is provided by Teledyne Technologies on demand forecasts in light of government defense spending trends?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6901832153420377 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qba50bc033945`)._

### ex-dev-qbd63044fc6b3

- **example_id**: `dev:qbd63044fc6b3`
- **state**: `completed`
- **query**: What risk is associated with franchisee financial health amid rapid expansion requirements
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'Earnings', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=94

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbd63044fc6b3:chunk-26` | 1.4885516176350653 |  | 12 |
| 2 | `qbd63044fc6b3:chunk-93` | 1.2172161400120065 |  | 44 |
| 3 | `qbd63044fc6b3:chunk-88` | 1.1539835603432493 |  | 42 |
| 4 | `qbd63044fc6b3:chunk-42` | 1.1480738028179158 |  | 21 |
| 5 | `qbd63044fc6b3:chunk-46` | 1.140412502240365 |  | 22 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qbd63044fc6b3`)._

### ex-dev-qbdbd002b0a41

- **example_id**: `dev:qbdbd002b0a41`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Caterpillar Inc.’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7591919243197319 · gold=['10-Q', 'Earnings', '10-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qbdbd002b0a41`)._

### ex-dev-qc03648d89328

- **example_id**: `dev:qc03648d89328`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Moderna’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7363636171343382 · gold=['10-K', '10-Q', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc03648d89328`)._

### ex-dev-qc187429e2dc5

- **example_id**: `dev:qc187429e2dc5`
- **state**: `completed`
- **query**: What dependency risks exist for Huntington Ingalls Industries, Inc. due to concentration of revenue in a limited number of government defense contracts?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9452713619732751 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=249

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc187429e2dc5:chunk-12` | 1.7101375442164528 | 2.0 | Current U.S. Government spending levels for defense-related or other programs may not be sustained, and future spending… |
| 2 | `qc187429e2dc5:chunk-73` | 1.5858651754679738 | 2.0 | We expect approximately 22% of the $48.1 billion total backlog as of December 31, 2023, to be converted into sales in 2… |
| 3 | `qc187429e2dc5:chunk-235` | 1.5112393338918897 |  | 107 |
| 4 | `qc187429e2dc5:chunk-197` | 1.4606122871174054 |  | 91 |
| 5 | `qc187429e2dc5:chunk-237` | 1.4564160796881052 |  | 108 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc187429e2dc5`)._

### ex-dev-qc20017b12da3

- **example_id**: `dev:qc20017b12da3`
- **state**: `completed`
- **query**: How does Moderna view the pace of mRNA vaccine development cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.6093559763921439 · skipped= · n_scored=11

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc20017b12da3:chunk-7` | 0.6609331863354807 |  | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## About Moderna (cont.) M… |
| 2 | `qc20017b12da3:chunk-4` | 0.5504677026751177 | 2.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## Clinical Updates Modern… |
| 3 | `qc20017b12da3:chunk-6` | 0.48313858818822114 | 1.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## About Moderna In over 1… |
| 4 | `qc20017b12da3:chunk-0` | 0.46766493751354626 |  | Exhibit 99.1 # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates Third quarter 2023 re… |
| 5 | `qc20017b12da3:chunk-1` | 0.40498253725716327 | 1.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## 2023 Commercial Updates… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc20017b12da3`)._

### ex-dev-qc20e5c5b254e

- **example_id**: `dev:qc20e5c5b254e`
- **state**: `completed`
- **query**: How does Evergy manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9199642183398656 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=186

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc20e5c5b254e:chunk-185` | 1.1398513932725587 |  | 80 |
| 2 | `qc20e5c5b254e:chunk-10` | 0.9993853208593363 |  | 12 |
| 3 | `qc20e5c5b254e:chunk-167` | 0.8766836113356842 |  | 72 |
| 4 | `qc20e5c5b254e:chunk-89` | 0.8344433324068907 |  | 40 |
| 5 | `qc20e5c5b254e:chunk-129` | 0.8316659542433824 |  | 54 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc20e5c5b254e`)._

### ex-dev-qc28e5aa0181b

- **example_id**: `dev:qc28e5aa0181b`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are scenario analyses conducted by Humana Inc. for potential shifts in Medicare Advantage enrollment?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6609293020771597 · gold=['Earnings', '10-K', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc28e5aa0181b`)._

### ex-dev-qc4efe3f0f342

- **example_id**: `dev:qc4efe3f0f342`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How could global geopolitical tensions affect Mastercard's cross?border revenues?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6859372277669218 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc4efe3f0f342`)._

### ex-dev-qc6c8c1f4ddfe

- **example_id**: `dev:qc6c8c1f4ddfe`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has CMS Energy Corporation’s electric utility segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7146598531416503 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc6c8c1f4ddfe`)._

### ex-dev-qc8e6b0d72c52

- **example_id**: `dev:qc8e6b0d72c52`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Caesars Entertainment, Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9416116958060755 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc8e6b0d72c52:chunk-37` | 0.6352721394167753 |  | Yes. We expect to do both. |
| 2 | `qc8e6b0d72c52:chunk-51` | 0.6342741680154566 |  | Yes. I mean we're $4 billion now with digital doing de minimis EBITDA by 25%, we'd expect to be in the neighborhood of … |
| 3 | `qc8e6b0d72c52:chunk-0` | 0.6044968146919171 |  | Operator |
| 4 | `qc8e6b0d72c52:chunk-104` | 0.6044968146919171 |  | Operator |
| 5 | `qc8e6b0d72c52:chunk-114` | 0.6044968146919171 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc8e6b0d72c52`)._

### ex-dev-qcbbca1138c08

- **example_id**: `dev:qcbbca1138c08`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Freeport-McMoRan’s international or geographic expansion prospects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7373239404693707 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qcbbca1138c08`)._

### ex-dev-qcdb8bc16cf2f

- **example_id**: `dev:qcdb8bc16cf2f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Jack Henry & Associates’ technology platform modernization targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.674868692170694 · gold=['Earnings', '10-K', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qcdb8bc16cf2f`)._

### ex-dev-qcf796a17c330

- **example_id**: `dev:qcf796a17c330`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are scenario analyses conducted by FirstEnergy Corp. for fluctuations in electricity demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8490348899399066 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qcf796a17c330`)._

### ex-dev-qd08d64c0654c

- **example_id**: `dev:qd08d64c0654c`
- **state**: `completed`
- **query**: How has Fortive Corporation’s segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.819876640193745 · skipped= · n_scored=16

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd08d64c0654c:chunk-6` | 1.2729356000741632 | 2.0 | # FORTIVE CORPORATION AND SUBSIDIARIES SEGMENT INFORMATION ($ in millions) <table><tr><th></th><th colspan="2">Three Mo… |
| 2 | `qd08d64c0654c:chunk-1` | 1.1614960622262953 |  | # Fortive Reports Strong Fourth Quarter and Full Year 2023 Results Introduces First Quarter and Full Year 2024 Outlook … |
| 3 | `qd08d64c0654c:chunk-5` | 0.9955745211262726 |  | # FORTIVE CORPORATION AND SUBSIDIARIES CONSOLIDATED STATEMENTS OF EARNINGS ($ and shares in millions, except per share … |
| 4 | `qd08d64c0654c:chunk-14` | 0.9704603144857595 |  | # Adjusted Net Earnings and Adjusted Diluted Net Earnings Per Share (unaudited) <table><tr><th rowspan="2">($ in millio… |
| 5 | `qd08d64c0654c:chunk-2` | 0.844584662189201 | 1.0 | # Fortive Reports Strong Fourth Quarter and Full Year 2023 Results Introduces First Quarter and Full Year 2024 Outlook … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd08d64c0654c`)._

### ex-dev-qd177bdad4bdd

- **example_id**: `dev:qd177bdad4bdd`
- **state**: `completed`
- **query**: What pension discount rate assumption was used for year end valuation?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd177bdad4bdd:chunk-173` | 2.3260009270620037 | 2.0 | (a)A pension discount rate of 4.75% was used for the applicable plans following the transaction and remeasurement recog… |
| 2 | `qd177bdad4bdd:chunk-172` | 2.1823060956137286 | 2.0 | ######Qualified Defined Benefit Pension Plans############Retiree Medical and Life Insurance Plans###### ##2023####2022#… |
| 3 | `qd177bdad4bdd:chunk-207` | 0.6639895776316045 |  | 101 |
| 4 | `qd177bdad4bdd:chunk-171` | 0.6468685713229438 |  | Assumptions Used to Determine Benefit Obligations and FAS (Expense) Income We measure the fair value of each plan’s ass… |
| 5 | `qd177bdad4bdd:chunk-160` | 0.6057698778821355 |  | 82 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd177bdad4bdd`)._

### ex-dev-qd2e3bd55f2ee

- **example_id**: `dev:qd2e3bd55f2ee`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about HCA Healthcare’s patient engagement metrics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.5292991962953502 · gold=['DEF14A', 'Earnings', '8-K', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd2e3bd55f2ee`)._

### ex-dev-qd422350b37cb

- **example_id**: `dev:qd422350b37cb`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Martin Marietta Materials’ geographic expansion prospects within domestic markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7537872138927924 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd422350b37cb`)._

### ex-dev-qd483c94f1ec6

- **example_id**: `dev:qd483c94f1ec6`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How do investors view American International Group, Inc.’s valuation relative to peers based on recent disclosures?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6901832153420377 · gold=['DEF14A', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd483c94f1ec6`)._

### ex-dev-qd5c685de4d7a

- **example_id**: `dev:qd5c685de4d7a`
- **state**: `completed`
- **query**: What themes emerged regarding the convergence of technology and biotechnology in the company operating model
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9134693626978977 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5=0.156848790217105 · skipped= · n_scored=176

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd5c685de4d7a:chunk-64` | 0.9582770738397808 |  | # 2021 Activities Supporting Execution of Our Strategy (cont.) <table><tr><th>Strategic Priorities</th><th>Importance</… |
| 2 | `qd5c685de4d7a:chunk-75` | 0.9183562072668034 | 1.0 | # Compensation Discussion and Analysis (cont.) ## b. We successfully achieved our digital transformation goal. To drive… |
| 3 | `qd5c685de4d7a:chunk-66` | 0.8356879512101834 | 1.0 | # Compensation Discussion and Analysis <table><tr><th>Strategic Priorities</th><th colspan="2">Importance Select 2021 A… |
| 4 | `qd5c685de4d7a:chunk-54` | 0.5185214197738525 |  | # Corporate Governance (cont.) ## Amgen Values <table><tr><th>Be Science-Based</th><th>Trust and Respect Each Other</th… |
| 5 | `qd5c685de4d7a:chunk-94` | 0.4805054846431141 |  | # Compensation Discussion and Analysis (cont.) ## Weighted Score Achieved 53.6% (cont.) <table><tr><th rowspan="9">Goal… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd5c685de4d7a`)._

### ex-dev-qd639a486b106

- **example_id**: `dev:qd639a486b106`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: Which general medicine candidate in obesity was identified for upcoming mid stage data readout
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.5196610607458307 · gold=['Earnings', '10-K']
- **S1 ordered**: `['8-K', 'DEF14A', 'Earnings', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd639a486b106`)._

### ex-dev-qd87c2da5e7da

- **example_id**: `dev:qd87c2da5e7da`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Kenvue manage equity award burn rate or share pool availability?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6859372277669218 · gold=['10-K', '10-Q', '8-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd87c2da5e7da`)._

### ex-dev-qdb9da6a1e373

- **example_id**: `dev:qdb9da6a1e373`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Packaging Corporation of America manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7118306928082477 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qdb9da6a1e373`)._

### ex-dev-qdbaa829dd4cc

- **example_id**: `dev:qdbaa829dd4cc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Gen Digital Inc.’s customer retention and renewal rates?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6836883597000701 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qdbaa829dd4cc`)._

### ex-dev-qdec70f55027f

- **example_id**: `dev:qdec70f55027f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Mettler-Toledo International Inc.’s international or geographic expansion prospects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7426242736819336 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qdec70f55027f`)._

### ex-dev-qdfe52ef66df5

- **example_id**: `dev:qdfe52ef66df5`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of IDEXX Laboratories’ recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6327646179298274 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qdfe52ef66df5`)._

### ex-dev-qe1811f4fd3dc

- **example_id**: `dev:qe1811f4fd3dc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Digital Realty Trust’s customer or tenant engagement metrics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.5258656644466531 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qe1811f4fd3dc`)._

### ex-dev-qe2edf9d38872

- **example_id**: `dev:qe2edf9d38872`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Charter Communications’ broadband segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qe2edf9d38872`)._

### ex-dev-qe8a08fb7bfff

- **example_id**: `dev:qe8a08fb7bfff`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Meta Platforms, Inc.’s advertising segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qe8a08fb7bfff`)._

### ex-dev-qe93fa46ab352

- **example_id**: `dev:qe93fa46ab352`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Philip Morris International view the pace of innovation cycles in reduced-risk products and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6426749236865535 · gold=['Earnings', '10-Q', '10-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qe93fa46ab352`)._

### ex-dev-qe99b7fb80e2c

- **example_id**: `dev:qe99b7fb80e2c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Intercontinental Exchange’s data services segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7085011369669131 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qe99b7fb80e2c`)._

### ex-dev-qeccd6f3b9d06

- **example_id**: `dev:qeccd6f3b9d06`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What feedback surfaced on Akamai Technologies' innovation or new product pipeline prospects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6898217095818122 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qeccd6f3b9d06`)._

### ex-dev-qf13afdfcadcf

- **example_id**: `dev:qf13afdfcadcf`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did Howmet Aerospace Inc.’s leadership say about Howmet Aerospace Inc.’s dividend policy?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7578930246759503 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf13afdfcadcf`)._

### ex-dev-qf25e1308bae4

- **example_id**: `dev:qf25e1308bae4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: Which investor concerns about the company’s China exposure did management acknowledge?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.6068373752823822 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf25e1308bae4`)._

### ex-dev-qf38450369367

- **example_id**: `dev:qf38450369367`
- **state**: `completed`
- **query**: What investor views emerged on Nordson Corporation’s international or geographic expansion prospects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9840990003623115 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf38450369367:chunk-55` | 0.7435330503770113 |  | # 2023 Actions and Analysis (cont.) ## Currency Neutral: <table><tr><th>Named Executive Officer</th><th>Company Factor … |
| 2 | `qf38450369367:chunk-3` | 0.4548505194404274 |  | # TABLE OF CONTENTS (cont.) ## Table of Contents # Nordson Corporation NOTICE OF ANNUAL MEETING OF SHAREHOLDERS To Be H… |
| 3 | `qf38450369367:chunk-78` | 0.44726205109328854 |  | # Table of Contents <table><tr><th></th><th colspan="4">Option Awards</th><th colspan="4">Stock Awards</th></tr><tr><td… |
| 4 | `qf38450369367:chunk-90` | 0.40571114088243865 |  | # Table of Contents <table><tr><th>Benefit or Payment</th><th>Termination for Cause or Voluntary Termination</th><th>Te… |
| 5 | `qf38450369367:chunk-7` | 0.372094937990166 |  | # NORDSON CORPORATION PROXY STATEMENT FOR THE ANNUAL MEETING OF SHAREHOLDERS March 5, 2024 The accompanying proxy is so… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf38450369367`)._

### ex-dev-qf5b4bbe60015

- **example_id**: `dev:qf5b4bbe60015`
- **state**: `completed`
- **query**: How has Cadence Design Systems’ IP segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9734136950814526 · gold=['Earnings', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf5b4bbe60015:chunk-1` | 0.7641833778892128 | 1.0 | For fiscal year 2024, the company expects: •Revenue in the range of $4.60 billion to $4.66 billion •GAAP operating marg… |
| 2 | `qf5b4bbe60015:chunk-15` | 0.6475535660756556 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 3 | `qf5b4bbe60015:chunk-12` | 0.6308530041879853 |  | Condensed Consolidated Income Statements For the Three and Six Months Ended June 30, 2024 and June 30, 2023 (In thousan… |
| 4 | `qf5b4bbe60015:chunk-4` | 0.5825547927674963 |  | [Chunk Index 5] <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><t… |
| 5 | `qf5b4bbe60015:chunk-20` | 0.469407128664721 |  | Impact of Non-GAAP Adjustments on Forward Looking Operating Margin As of July 22, 2024 (Unaudited) |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf5b4bbe60015`)._

### ex-dev-qf7a3126727b8

- **example_id**: `dev:qf7a3126727b8`
- **state**: `completed`
- **query**: How does Sysco Corporation’s debt maturity profile affect liquidity and cost structure?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=148

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf7a3126727b8:chunk-145` | 0.4173281493273819 |  | # NET DEBT TO ADJUSTED EBITDA (LETTER FROM CEO AND CHAIR) (cont.) ## ADJUSTED EBITDA NON-GAAP RECONCILIATION (LETTER FR… |
| 2 | `qf7a3126727b8:chunk-77` | 0.30351675480259616 |  | # COMPENSATION DISCUSSION AND ANALYSIS <table><tr><th>Recipe For Growth SBO</th><th>Committee's Assessment of Performan… |
| 3 | `qf7a3126727b8:chunk-7` | 0.29298137812703473 |  | # PROXY STATEMENT SUMMARY (cont.) ## MEETING AGENDA The matters we will act upon at the Annual Meeting are: <table><tr>… |
| 4 | `qf7a3126727b8:chunk-121` | 0.2827918033348042 |  | # GREG D. BERTRAND (cont.) ## NEIL A. RUSSELL, II <table><tr><th>Termination Scenario</th><th>Severance Payment ($)</th… |
| 5 | `qf7a3126727b8:chunk-120` | 0.2588933530877102 |  | # GREG D. BERTRAND (cont.) ## THOMAS R. PECK, JR. <table><tr><th>Termination Scenario</th><th>Severance Payment ($)</th… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf7a3126727b8`)._

### ex-dev-qf8cbcec9fec6

- **example_id**: `dev:qf8cbcec9fec6`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Ingersoll Rand’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6946088014820204 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf8cbcec9fec6`)._

### ex-dev-qf8e3e71e08c9

- **example_id**: `dev:qf8e3e71e08c9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Principal Financial Group’s retirement solutions segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf8e3e71e08c9`)._

### ex-dev-qf9c15fa46d48

- **example_id**: `dev:qf9c15fa46d48`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Live Nation Entertainment’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.8596355563650325 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf9c15fa46d48`)._

### ex-dev-qfa38830206fb

- **example_id**: `dev:qfa38830206fb`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does The Clorox Company manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6426749236865535 · gold=['DEF14A', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qfa38830206fb`)._

### ex-dev-qfbef9973c7fb

- **example_id**: `dev:qfbef9973c7fb`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What clarification did management provide on margin durability in the face of potential memory‑cost inflation?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.5505005291456017 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qfbef9973c7fb`)._

### ex-dev-qfd572ccfcb0f

- **example_id**: `dev:qfd572ccfcb0f`
- **state**: `completed`
- **query**: What investor views emerged on Hasbro’s international or geographic expansion prospects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.3191471544989227 · skipped= · n_scored=154

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qfd572ccfcb0f:chunk-80` | 0.8310454521710956 |  | ######Quarter Ended##########Nine Months Ended#### ####October 1, 2023######September 25, 2022####October 1, 2023######… |
| 2 | `qfd572ccfcb0f:chunk-119` | 0.7712620805932984 |  | Consumer Products Segment The following table presents the Consumer Products segment net revenues by major geographic r… |
| 3 | `qfd572ccfcb0f:chunk-109` | 0.7695747718203263 |  | Consumer Products Segment The following table presents the Consumer Products segment net revenues by major geographic r… |
| 4 | `qfd572ccfcb0f:chunk-110` | 0.6922723567986261 | 1.0 | ######Quarter Ended#### ####October 1, 2023######September 25, 2022 North America##$##573.6####$##693.3 Europe####208.7… |
| 5 | `qfd572ccfcb0f:chunk-79` | 0.6615686695112295 | 1.0 | Condensed Notes to Consolidated Financial Statements (Millions of Dollars and Shares Except Per Share Data) The followi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qfd572ccfcb0f`)._

### ex-dev-qff56bedc2f87

- **example_id**: `dev:qff56bedc2f87`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Globe Life Inc.’s customer retention metrics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.5258656644466531 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qff56bedc2f87`)._

### ex-dev-qff73996028bf

- **example_id**: `dev:qff73996028bf`
- **state**: `completed`
- **query**: How has Williams-Sonoma’s management addressed supply-chain risks and efforts to enhance Williams-Sonoma’s resilience?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9416116958060755 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5=0.27727342735504823 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff73996028bf:chunk-146` | 1.5061580195613002 |  | 76 |
| 2 | `qff73996028bf:chunk-134` | 1.471366111652333 |  | 72 |
| 3 | `qff73996028bf:chunk-137` | 1.3469066063390054 |  | 73 |
| 4 | `qff73996028bf:chunk-15` | 1.1255717462978785 | 2.0 | Table of Contents In addition, in the past, we have insourced certain aspects of our business, including certain techno… |
| 5 | `qff73996028bf:chunk-39` | 1.0595751756790306 | 2.0 | Table of Contents Elevating our World-Class Customer Service We are continuing to improve our world-class customer serv… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qff73996028bf`)._

### ex-eval-chunk-only-chunk-q0b530d

- **example_id**: `eval:chunk-only:chunk_q0b530d`
- **state**: `completed`
- **query**: How does Brown-Forman view the pace of product innovation cycles and their effect on market competitiveness in the spirits industry?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'DEF14A', '8-K', '10-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=90

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q0b530d:10-Q:chunk-0` | 0.8832777441269155 |  | Operator |
| 2 | `chunk_q0b530d:10-Q:chunk-18` | 0.8832777441269155 |  | Operator |
| 3 | `chunk_q0b530d:10-Q:chunk-28` | 0.8832777441269155 |  | Operator |
| 4 | `chunk_q0b530d:10-Q:chunk-40` | 0.8832777441269155 |  | Operator |
| 5 | `chunk_q0b530d:10-Q:chunk-58` | 0.8832777441269155 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q0b530d`)._

### ex-eval-chunk-only-chunk-q29280e

- **example_id**: `eval:chunk-only:chunk_q29280e`
- **state**: `completed`
- **query**: How does Atmos Energy Corporation manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=83

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q29280e:10-K:chunk-52` | 0.8800019222190829 |  | # Grants of Plan-Based Awards (cont.) ## Grants of Plan-Based Awards for Fiscal Year 2023(a) <table><tr><th rowspan="2"… |
| 2 | `chunk_q29280e:10-K:chunk-51` | 0.7362619481833189 |  | # Named Executive Officer Compensation and Related Matters (cont.) ## All Other Compensation for Fiscal Year 2023 <tabl… |
| 3 | `chunk_q29280e:10-K:chunk-7` | 0.735581849830486 |  | # Compensation Highlights (cont.) ## Key Features of Our Executive Compensation Program ## What We Do ## What We Don't … |
| 4 | `chunk_q29280e:10-K:chunk-49` | 0.7226172562168127 |  | # Named Executive Officer Compensation and Related Matters (cont.) ## Summary Compensation Table for Fiscal Year 2023(a… |
| 5 | `chunk_q29280e:10-K:chunk-65` | 0.5883286019411129 |  | # Named Executive Officer Compensation and Related Matters (cont.) <table><tr><th></th><th>Termination Upon Death</th><… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q29280e`)._

### ex-eval-chunk-only-chunk-q2ccba5

- **example_id**: `eval:chunk-only:chunk_q2ccba5`
- **state**: `completed`
- **query**: What questions were asked about Boston Scientific’s customer or user engagement metrics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q2ccba5:10-K:chunk-11` | 0.9867115767258268 |  | [Operator Instructions] The first question comes from Robbie Marcus with JPMorgan. |
| 2 | `chunk_q2ccba5:10-K:chunk-17` | 0.8325855601383668 |  | The next question comes from Joanne Wuensch with Citi. |
| 3 | `chunk_q2ccba5:10-K:chunk-45` | 0.8175971392366088 |  | The next question comes from Danielle Antalffy with UBS. |
| 4 | `chunk_q2ccba5:10-K:chunk-73` | 0.7739549873067485 |  | The next question comes from Josh Jennings with TD Cowen. |
| 5 | `chunk_q2ccba5:10-K:chunk-81` | 0.7734653235265212 |  | The next question comes from Richard Newitter with Truist Securities. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q2ccba5`)._

### ex-eval-chunk-only-chunk-q44d295

- **example_id**: `eval:chunk-only:chunk_q44d295`
- **state**: `completed`
- **query**: How has the ratio of Amphenol Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=235

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q44d295:Earnings:chunk-38` | 1.2444678154709221 |  | ####2023####2022 First Quarter##$##0.21##$##0.20 Second Quarter####0.21####0.20 Third Quarter####0.21####0.20 Fourth Qu… |
| 2 | `chunk_q44d295:Earnings:chunk-154` | 1.0436948753437276 |  | ####2023####2022####2021 First Quarter##$##0.21##$##0.20##$##0.145 Second Quarter####0.21####0.20####0.145 Third Quarte… |
| 3 | `chunk_q44d295:Earnings:chunk-78` | 1.0436948753437276 |  | ####2023####2022####2021 First Quarter##$##0.21##$##0.20##$##0.145 Second Quarter####0.21####0.20####0.145 Third Quarte… |
| 4 | `chunk_q44d295:Earnings:chunk-93` | 0.7348635948882661 |  | AMPHENOL CORPORATION Consolidated Statements of Comprehensive Income (dollars in millions) |
| 5 | `chunk_q44d295:Earnings:chunk-90` | 0.7253478901853694 |  | AMPHENOL CORPORATION Consolidated Statements of Income (dollars and shares in millions, except per share data) |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q44d295`)._

### ex-eval-chunk-only-chunk-q5ebb5e

- **example_id**: `eval:chunk-only:chunk_q5ebb5e`
- **state**: `completed`
- **query**: How has investor sentiment shifted following The AES Corporation’s most recent earnings release?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q5ebb5e:Earnings:chunk-39` | 0.4961946811792711 |  | # EXECUTIVE COMPENSATION COMPENSATION DISCUSSION AND ANALYSIS ("CD&A") (cont.) ## Executive Summary 2023 was a strong y… |
| 2 | `chunk_q5ebb5e:Earnings:chunk-2` | 0.4437480062212296 |  | # Table of Contents (cont.) <table><tr><th>2023 Option Exercises and Stock Vested</th><th>57</th></tr><tr><td>2023 Non-… |
| 3 | `chunk_q5ebb5e:Earnings:chunk-36` | 0.37926951919592056 |  | # DIRECTOR COMPENSATION (cont.) ## Director Compensation (2023) The following table contains information concerning the… |
| 4 | `chunk_q5ebb5e:Earnings:chunk-100` | 0.36206642711808246 |  | # Reconciliation of Adjusted EBITDA <table><tr><th>$ in Millions</th><th></th><th>Year Ended Dec. 31, 2023</th></tr><tr… |
| 5 | `chunk_q5ebb5e:Earnings:chunk-107` | 0.35305364527762734 |  | # Growth Details: <table><tr><th>Goal Description</th><th>How it will be measured</th><th>Formula</th></tr><tr><td>Cont… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q5ebb5e`)._

### ex-eval-chunk-only-chunk-q829eae

- **example_id**: `eval:chunk-only:chunk_q829eae`
- **state**: `completed`
- **query**: What guidance was offered on Amazon’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', '8-K', '10-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q829eae:10-Q:chunk-89` | 0.9901047753086094 |  | Table of Contents Guidance We provided guidance on October 26, 2023, in our earnings release furnished on Form 8-K as s… |
| 2 | `chunk_q829eae:10-Q:chunk-35` | 0.7891239708439372 |  | 12 |
| 3 | `chunk_q829eae:10-Q:chunk-52` | 0.737870804129029 |  | 16 |
| 4 | `chunk_q829eae:10-Q:chunk-109` | 0.72034910233045 |  | Dated: October 26, 2023 47 |
| 5 | `chunk_q829eae:10-Q:chunk-59` | 0.6205387967896019 |  | 19 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q829eae`)._

### ex-eval-chunk-only-chunk-q8fc814

- **example_id**: `eval:chunk-only:chunk_q8fc814`
- **state**: `completed`
- **query**: What guidance was offered on Apollo Global Management’s fundraising targets for new investment vehicles?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '8-K', '10-Q', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=78

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q8fc814:10-K:chunk-23` | 0.9177334652862431 |  | All right, cool. And then my violation part B is you said $200 billion to $250 billion. I kind of remember $100 billion… |
| 2 | `chunk_q8fc814:10-K:chunk-25` | 0.82337320929896 |  | So we -- when we set out our 5-year targets a little over 2 years ago, we -- the 5-year target was to get to $150 billi… |
| 3 | `chunk_q8fc814:10-K:chunk-63` | 0.815459412650186 |  | Sure. So ADIP 2 fundraising, going quite well. We expect to wrap it up this summer in the $4 billion to $5 billion rang… |
| 4 | `chunk_q8fc814:10-K:chunk-0` | 0.760329575183515 |  | Operator |
| 5 | `chunk_q8fc814:10-K:chunk-10` | 0.760329575183515 |  | Operator |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q8fc814`)._

### ex-eval-chunk-only-chunk-q9fad72

- **example_id**: `eval:chunk-only:chunk_q9fad72`
- **state**: `completed`
- **query**: What guidance was offered on CDW Corporation’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q9fad72:10-K:chunk-63` | 1.3718367980096067 |  | ####December 31,## (in days)##2023####2022 Days of sales outstanding (DSO)(1)##77####71 Days of supply in inventory (DI… |
| 2 | `chunk_q9fad72:10-K:chunk-14` | 1.2927752068812355 |  | •keep pace with changes and innovation and compete effectively; •effectuate comprehensive and reliable data collection,… |
| 3 | `chunk_q9fad72:10-K:chunk-11` | 1.2096024375638172 |  | 9 |
| 4 | `chunk_q9fad72:10-K:chunk-197` | 0.8427056741295031 |  | 80 |
| 5 | `chunk_q9fad72:10-K:chunk-99` | 0.7904076484978172 |  | CDW CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (dollars in millions, except per share data… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q9fad72`)._

### ex-eval-doc-q0617ad

- **example_id**: `eval:doc_q0617ad`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did F5’s leadership say about F5’s share repurchase plans?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:doc_q0617ad`)._

### ex-eval-doc-q48ce69

- **example_id**: `eval:doc_q48ce69`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did energy cost inflation impact theme park utility expenses
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:doc_q48ce69`)._

### ex-eval-doc-q737b56

- **example_id**: `eval:doc_q737b56`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Deckers Outdoor Corporation’s customer retention metrics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:doc_q737b56`)._

### ex-eval-doc-qa9fda3

- **example_id**: `eval:doc_qa9fda3`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does The AES Corporation account for currency and economic volatility in its risk management disclosures?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:doc_qa9fda3`)._
