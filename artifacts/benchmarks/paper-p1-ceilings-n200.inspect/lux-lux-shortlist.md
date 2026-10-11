# Pair `lux-lux-shortlist` — `paper-p1-ceilings-n200`

[← compact index](../paper-p1-ceilings-n200.inspect.md) · **Download full HTML**: [raw](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) · [`paper-p1-ceilings-n200.inspect.html`](../paper-p1-ceilings-n200.inspect.html)

- eval_run_id: `paper-p1-ceilings-n200:lux-lux-shortlist`
- S1=`decision20-lux` · S2=`lux-score-shortlist-32`
- row status: `completed` · completed=119 · failed_retriable=81

## Examples

### ex-dev-chunk-only-q075970f6eb46

- **example_id**: `dev:chunk-only:q075970f6eb46`
- **state**: `completed`
- **query**: What did Fastenal Company’s leadership say about Fastenal Company’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '10-Q', '8-K']`
- **S2**: nDCG@5=0.21398626473452756 · skipped= · n_scored=105

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q075970f6eb46:DEF14A:chunk-101` | 0.8540447598272327 |  | 28 |
| 2 | `q075970f6eb46:DEF14A:chunk-22` | 0.8186664025141022 | 1.0 | (1) The fasteners product line represents fasteners and miscellaneous supplies. (3) Stockholders' Equity Dividends On O… |
| 3 | `q075970f6eb46:DEF14A:chunk-103` | 0.7328579563496281 |  | ####FASTENAL COMPANY Date: October 17, 2023##By:##/s/ Holden Lewis ####Holden Lewis ####Senior Executive Vice President… |
| 4 | `q075970f6eb46:DEF14A:chunk-37` | 0.43283409747114143 |  | ITEM 2 — MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following is managem… |
| 5 | `q075970f6eb46:DEF14A:chunk-15` | 0.42014880346607886 |  | FASTENAL COMPANY AND SUBSIDIARIES Notes to Condensed Consolidated Financial Statements (Amounts in millions except shar… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q075970f6eb46`)._

### ex-dev-chunk-only-q0fd4ca04c0a5

- **example_id**: `dev:chunk-only:q0fd4ca04c0a5`
- **state**: `completed`
- **query**: How does Molina Healthcare view the pace of innovation cycles in healthcare delivery and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.13120507751234178 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0fd4ca04c0a5:10-K:chunk-91` | 0.36430812174384875 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS 1. Organization and Basis of Presentation Organization and Operations Molina… |
| 2 | `q0fd4ca04c0a5:10-K:chunk-42` | 0.3194590256335267 |  | Item 7. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS (“MD&A”) Management’s dis… |
| 3 | `q0fd4ca04c0a5:10-K:chunk-8` | 0.318339952342097 |  | continue to focus on driving market share gains through improved execution of enrollment and retention. Approximately $… |
| 4 | `q0fd4ca04c0a5:10-K:chunk-34` | 0.3030916300053751 |  | relationships with providers, requiring us to implement additional or different programs and systems, or making it more… |
| 5 | `q0fd4ca04c0a5:10-K:chunk-18` | 0.295353093555465 | 1.0 | Medical Cost Management We use various strategies to mitigate the negative effects of healthcare cost inflation. Specif… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q0fd4ca04c0a5`)._

### ex-dev-chunk-only-q299865e6e67e

- **example_id**: `dev:chunk-only:q299865e6e67e`
- **state**: `completed`
- **query**: What dependency risks exist for Consolidated Edison due to concentration of revenue in a limited number of service territories or customer segments?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.43071223322847096 · skipped= · n_scored=286

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q299865e6e67e:10-K:chunk-117` | 0.8984196954277498 | 1.0 | Note M – Financial Information by Business Segment Con Edison’s principal business segments are CECONY’s regulated util… |
| 2 | `q299865e6e67e:10-K:chunk-189` | 0.6687021629869108 | 1.0 | (a)Revenues from electric sales are subject to a revenue decoupling mechanism, as a result of which delivery revenues g… |
| 3 | `q299865e6e67e:10-K:chunk-228` | 0.6687021629869108 | 1.0 | (a)Revenues from electric sales are subject to a revenue decoupling mechanism, as a result of which delivery revenues g… |
| 4 | `q299865e6e67e:10-K:chunk-166` | 0.6235623311813789 | 2.0 | and gas businesses may impact the Companies’ future financial condition. The Utilities expect electric usage to increas… |
| 5 | `q299865e6e67e:10-K:chunk-262` | 0.5071680263566313 | 1.0 | Cash Flows from Operating Activities The Utilities’ cash flows from operating activities primarily reflect their energy… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q299865e6e67e`)._

### ex-dev-chunk-only-q2a401c1edf73

- **example_id**: `dev:chunk-only:q2a401c1edf73`
- **state**: `completed`
- **query**: How often is Exxon Mobil Corporation’s executive compensation program reviewed and updated?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.7330409974680542 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2a401c1edf73:DEF14A:chunk-43` | 0.7150641738469498 | 2.0 | # Table of Contents ## Compensation Committee The Compensation Committee is comprised exclusively of non-employee, inde… |
| 2 | `q2a401c1edf73:DEF14A:chunk-54` | 0.6289180715368339 | 2.0 | # Table of Contents (cont.) ## COMPENSATION COMMITTEE REPORT The Compensation Committee of the Board of Directors has r… |
| 3 | `q2a401c1edf73:DEF14A:chunk-0` | 0.5883902952329858 |  | # UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 # SCHEDULE 14A Proxy Statement Pursuant to Se… |
| 4 | `q2a401c1edf73:DEF14A:chunk-75` | 0.5331026322396712 | 1.0 | # 2023 COMPENSATION ACTIONS MANAGEMENT COMMITTEE (cont.) ## JACK P. WILLIAMS, JR., SENIOR VICE PRESIDENT (cont.) Angela… |
| 5 | `q2a401c1edf73:DEF14A:chunk-56` | 0.5269643304630268 | 2.0 | # EXECUTIVE SUMMARY (cont.) ## Shareholder Engagement <table><tr><th>Say-on-Pay</th><th>2023</th><th>2022</th><th>2021<… |

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
| 5 | `q3a71644741b7:Earnings:chunk-91` | 0.6574808073225777 |  | Okay, great. I said it would be a quick follow-up. Maybe it'd be a bit more than that, but we'll see. About 80% holding… |

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
- **S2**: nDCG@5=0.2577212905719748 · skipped= · n_scored=138

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7b219decf5da:DEF14A:chunk-17` | 0.533445948707657 |  | Yaron, in addition to that -- this is the Juan Andrade. Look, I would say there is no change in the messaging from our … |
| 2 | `q7b219decf5da:DEF14A:chunk-119` | 0.47066912496977675 | 2.0 | Mike, it's Mark. The first point that I would make is we have ample capital. There's a lot of capital that we have at o… |
| 3 | `q7b219decf5da:DEF14A:chunk-95` | 0.45977821815240905 |  | Yes. We're definitely, I think, ahead of the curve on that. That's something that we've had in our vision for quite som… |
| 4 | `q7b219decf5da:DEF14A:chunk-43` | 0.4417654389570073 |  | Yes. And again, Josh, this is Juan. Just to add a little bit more color on that. Look, the bottom line is the factors y… |
| 5 | `q7b219decf5da:DEF14A:chunk-7` | 0.4080293140082525 | 1.0 | Thank you, Juan, and good morning, everyone. Everest had a strong finish to 2023. For the full year, Everest delivered … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q7b219decf5da`)._

### ex-dev-chunk-only-q7ca4de540868

- **example_id**: `dev:chunk-only:q7ca4de540868`
- **state**: `completed`
- **query**: How does Hologic view the pace of innovation cycles in women's health diagnostics and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.12001820485907799 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ca4de540868:10-K:chunk-3` | 0.44094737273884316 |  | # Dear Fellow Stockholders: (cont.) Moving first to the Hologic Global Women's Health Index, a partnership with Gallup,… |
| 2 | `q7ca4de540868:10-K:chunk-32` | 0.436262962097014 | 1.0 | # Our Board's Role and Responsibilities (cont.) ## A Champion for Women's Health We are committed to improving women's … |
| 3 | `q7ca4de540868:10-K:chunk-57` | 0.36976237842731274 |  | # Executive Officers (cont.) ## MR. ANDERSON ## Division President, Breast and Skeletal Health Solutions <figure descri… |
| 4 | `q7ca4de540868:10-K:chunk-8` | 0.36822770525361187 | 1.0 | # Performance Highlights (cont.) 15.6% WORLDWIDE ORGANIC REVENUE GROWTH EX. COVID-19 15.6% organic growth in constant c… |
| 5 | `q7ca4de540868:10-K:chunk-9` | 0.31867168632692716 |  | # Performance Highlights (cont.) ## Financial highlights from fiscal 2023 - We drove top-line growth through a combinat… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q7ca4de540868`)._

### ex-dev-chunk-only-q7ff47a7d2a20

- **example_id**: `dev:chunk-only:q7ff47a7d2a20`
- **state**: `completed`
- **query**: How does Consolidated Edison, Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.1278554557904452 · skipped= · n_scored=212

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ff47a7d2a20:10-K:chunk-103` | 0.6174619661509073 |  | # Long-Term Incentive Compensation (cont.) ## Equity Awards It is the Compensation Committee's practice in the first qu… |
| 2 | `q7ff47a7d2a20:10-K:chunk-66` | 0.40113133382113475 | 1.0 | # Stock Ownership Guidelines (cont.) ## Long Term Incentive Plan Non-employee Directors participate in the Company's lo… |
| 3 | `q7ff47a7d2a20:10-K:chunk-108` | 0.39768650741888645 | 1.0 | # Long-Term Incentive Compensation (cont.) ## Footnote: (1) The MD&C Committee approves the annual work plan objectives… |
| 4 | `q7ff47a7d2a20:10-K:chunk-40` | 0.3955814063000633 |  | # THE BOARD OF DIRECTORS (cont.) ## Board Oversight of Human Capital Management The MD&C Committee provides oversight o… |
| 5 | `q7ff47a7d2a20:10-K:chunk-107` | 0.36417141414337295 |  | # Long-Term Incentive Compensation (cont.) ## Footnote: (1) Interpolated for actual performance between minimum, target… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q7ff47a7d2a20`)._

### ex-dev-chunk-only-q853c16a74704

- **example_id**: `dev:chunk-only:q853c16a74704`
- **state**: `completed`
- **query**: What did Tapestry’s management say about Tapestry’s margin outlook and initiatives to improve profitability?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.7261374126646398 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q853c16a74704:Earnings:chunk-7` | 1.200635512448199 | 2.0 | Thanks, Joanne, and good morning, everyone. Looking back at our results for the fiscal year, our commitment to discipli… |
| 2 | `q853c16a74704:Earnings:chunk-47` | 1.1318474650587738 | 1.0 | Well, we are building and continue to drive a healthy business. That's been our focus, not only in China, but around th… |
| 3 | `q853c16a74704:Earnings:chunk-35` | 0.9409776062075931 | 2.0 | A very brief add to your specific question as it relates to what's driving gross margin. It's really the structural dri… |
| 4 | `q853c16a74704:Earnings:chunk-33` | 0.6498354549964214 | 2.0 | Yes. Thanks. First, in North America, Coach delivered slight growth in the fourth quarter and it was at incredible marg… |
| 5 | `q853c16a74704:Earnings:chunk-3` | 0.6079729094692681 |  | Good morning. Thank you for joining us. With me today to discuss our fourth quarter and year-end results as well as our… |

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
| 1 | `q9ee9b517f484:Earnings:chunk-110` | 0.6238981020462917 |  | discounts on crude oils and other feedstocks, an increase in throughput volumes, and lower operating expenses (excludin… |
| 2 | `q9ee9b517f484:Earnings:chunk-129` | 0.4988449576698868 |  | Refining segment operating income decreased by $365 million in the third quarter of 2023 compared to the third quarter … |
| 3 | `q9ee9b517f484:Earnings:chunk-100` | 0.41655323049096304 |  | ITEM 2. MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS CAUTIONARY STATEMENT FOR … |
| 4 | `q9ee9b517f484:Earnings:chunk-163` | 0.33329379931937664 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |
| 5 | `q9ee9b517f484:Earnings:chunk-45` | 0.30650804776823826 |  | VALERO ENERGY CORPORATION CONDENSED NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Continued) |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q9ee9b517f484`)._

### ex-dev-chunk-only-qa431f3f55a5e

- **example_id**: `dev:chunk-only:qa431f3f55a5e`
- **state**: `completed`
- **query**: How are scenario analyses conducted by EPAM Systems, Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.48522855511632257 · skipped= · n_scored=252

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa431f3f55a5e:10-K:chunk-17` | 0.8081852811014054 | 1.0 | Table of Contents Our revenues are highly dependent on a limited number of industries, and any decrease in demand for o… |
| 2 | `qa431f3f55a5e:10-K:chunk-14` | 0.6373937863010737 |  | Table of Contents The economies of certain emerging market countries where we operate have experienced periods of consi… |
| 3 | `qa431f3f55a5e:10-K:chunk-114` | 0.5297233152719968 |  | Table of Contents EPAM SYSTEMS, INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (In thousands, except … |
| 4 | `qa431f3f55a5e:10-K:chunk-24` | 0.4733844428858496 | 1.0 | Table of Contents War, terrorism, other acts of violence or natural or man-made disasters may affect the markets in whi… |
| 5 | `qa431f3f55a5e:10-K:chunk-83` | 0.42059299325005306 |  | ##EPAM SYSTEMS, INC.## By:####/s/ Arkadiy Dobkin ####Name: Arkadiy Dobkin ####Title: Chairman, Chief Executive Officer … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qa431f3f55a5e`)._

### ex-dev-chunk-only-qaf2d41946676

- **example_id**: `dev:chunk-only:qaf2d41946676`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Occidental Petroleum Corporation for oil price volatility risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.3391602052736161 · skipped= · n_scored=126

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qaf2d41946676:10-K:chunk-87` | 0.43318453833678316 | 1.0 | Yes. So when we think about capital allocation in the oil and gas segment, what you're trying to do is we're trying to … |
| 2 | `qaf2d41946676:10-K:chunk-3` | 0.2716727001252186 |  | Thank you, Gary. Good afternoon, everyone, and thank you for participating in Occidental's Fourth Quarter 2023 earnings… |
| 3 | `qaf2d41946676:10-K:chunk-1` | 0.2557702410734579 |  | Good afternoon, and welcome to the Occidental's Fourth Quarter 2023 Earnings Conference Call. [Operator Instructions] P… |
| 4 | `qaf2d41946676:10-K:chunk-29` | 0.2325292686546931 |  | Well, depending on what actually is divested, we can't really give you an estimate of what that is today. Some things a… |
| 5 | `qaf2d41946676:10-K:chunk-53` | 0.22455362055278008 |  | Yes. I mean just to add to that. I mean, obviously, the focus, while near term, some of these highlights that we're put… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qaf2d41946676`)._

### ex-dev-chunk-only-qb3a6bec7aedc

- **example_id**: `dev:chunk-only:qb3a6bec7aedc`
- **state**: `completed`
- **query**: What exposure to foreign exchange fluctuations did Citizens Financial Group, Inc. disclose and how is Citizens Financial Group, Inc. managing it?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.7261374126646398 · skipped= · n_scored=423

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb3a6bec7aedc:10-K:chunk-306` | 1.7679687304539378 | 2.0 | NOTE 14 - DERIVATIVES In the normal course of business, Citizens enters into derivative transactions to meet the financ… |
| 2 | `qb3a6bec7aedc:10-K:chunk-111` | 1.2653349368500304 | 1.0 | Our principal non-market risks include credit, operational, regulatory, reputational, liquidity and strategic risks. We… |
| 3 | `qb3a6bec7aedc:10-K:chunk-113` | 1.0778667550653542 | 2.0 | Non-Trading Risk Our non-trading banking activities expose us to market risk. This market risk is composed of interest … |
| 4 | `qb3a6bec7aedc:10-K:chunk-317` | 0.897110288408254 | 2.0 | Derivatives not designated as hedging instruments The Company offers derivatives to customers in connection with their … |
| 5 | `qb3a6bec7aedc:10-K:chunk-18` | 0.5710386173708278 |  | Our framework for managing risks may not be effective in mitigating risk and loss. Our risk management framework is mad… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qb3a6bec7aedc`)._

### ex-dev-chunk-only-qb7d1dfae8271

- **example_id**: `dev:chunk-only:qb7d1dfae8271`
- **state**: `completed`
- **query**: What guidance was offered on International Flavors & Fragrances Inc.’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=304

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb7d1dfae8271:10-Q:chunk-4` | 1.1138600648219925 | 1.0 | •evaluating the profitability of whether to buy or make an ingredient; •sourcing from local countries with our own proc… |
| 2 | `qb7d1dfae8271:10-Q:chunk-22` | 1.076431879150214 | 1.0 | Our performance may be adversely impacted if we are not successful in managing our inventory and/or working capital bal… |
| 3 | `qb7d1dfae8271:10-Q:chunk-296` | 0.9430431090007947 |  | ##INTERNATIONAL FLAVORS & FRAGRANCES INC.## By:####/s/ Glenn Richter Name:####Glenn Richter Title:####Executive Vice Pr… |
| 4 | `qb7d1dfae8271:10-Q:chunk-291` | 0.37191040266302217 |  | Exhibit Number##Description 10.22(vi)##Third Amended and Restated Credit Agreement, dated as of July 28, 2021 among Int… |
| 5 | `qb7d1dfae8271:10-Q:chunk-58` | 0.3315127377521597 |  | •changes in demand from large multi-national customers due to increased competition and our ability to maintain “core l… |

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
- **S2**: nDCG@5=0.24090885754831726 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd7ede96b88aa:Earnings:chunk-30` | 0.5278207371135824 |  | # Corporate Governance (cont.) ## 2024 Feedback and Actions (cont.) <table><tr><th>What We Heard</th><th>What We Did</t… |
| 2 | `qd7ede96b88aa:Earnings:chunk-8` | 0.5032950554237187 | 1.0 | # 2025 Annual Meeting of Shareholders (cont.) ## Composition of our Board (cont.) 31 Years of Growth and Improving Marg… |
| 3 | `qd7ede96b88aa:Earnings:chunk-59` | 0.33753831724235145 | 2.0 | # Summary of Key NEO Compensation Decisions and Actions in 2024 (cont.) ## 2024 Peer Group Ametek, Inc. Aptiv PLC* Dove… |
| 4 | `qd7ede96b88aa:Earnings:chunk-31` | 0.3317733889145201 |  | # Corporate Governance (cont.) ## 2024 Feedback and Actions (cont.) 22 2025 Proxy Statement TransDigm Group Incorporate… |
| 5 | `qd7ede96b88aa:Earnings:chunk-112` | 0.25342255588196916 |  | # Appendix A (cont.) ## Non-GAAP Supplemental Information (cont.) TransDigm Group presents these non-GAAP financial mea… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qd7ede96b88aa`)._

### ex-dev-chunk-only-qddfea8300793

- **example_id**: `dev:chunk-only:qddfea8300793`
- **state**: `completed`
- **query**: How does Chesapeake Energy view the pace of technological advancements in drilling techniques and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.16958010263680806 · skipped= · n_scored=345

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qddfea8300793:10-K:chunk-32` | 0.7991438213346901 |  | Risks Related to Operating our Business Conservation measures and technological advances could reduce demand for natura… |
| 2 | `qddfea8300793:10-K:chunk-30` | 0.3684017794004501 |  | Item 1A. Risk Factors There are numerous factors that affect our business and results of operations, many of which are … |
| 3 | `qddfea8300793:10-K:chunk-36` | 0.31889848568491774 | 1.0 | Our development and exploratory drilling efforts and our well operations may not be profitable or achieve our targeted … |
| 4 | `qddfea8300793:10-K:chunk-35` | 0.2505871847695258 |  | unable to fund our capital expenditures as planned, we could experience a curtailment of our exploration and developmen… |
| 5 | `qddfea8300793:10-K:chunk-166` | 0.23455854196355255 |  | CHESAPEAKE ENERGY CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – (Continued) suspended explo… |

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
| 1 | `qed0361d5a9ae:Earnings:chunk-56` | 0.7892996704513815 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations This section and other pa… |
| 2 | `qed0361d5a9ae:Earnings:chunk-55` | 0.7402438632971435 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 13 |
| 3 | `qed0361d5a9ae:Earnings:chunk-22` | 0.7059418582554957 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 7 |
| 4 | `qed0361d5a9ae:Earnings:chunk-40` | 0.6961322999002444 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 10 |
| 5 | `qed0361d5a9ae:Earnings:chunk-33` | 0.6921713565875346 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 9 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qed0361d5a9ae`)._

### ex-dev-chunk-only-qeeb1c1a41ae3

- **example_id**: `dev:chunk-only:qeeb1c1a41ae3`
- **state**: `completed`
- **query**: What dependency risks exist for DuPont de Nemours, Inc. due to concentration of revenue in a limited number of end-use industries such as automotive or electronics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.4104889601851253 · skipped= · n_scored=112

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeeb1c1a41ae3:10-K:chunk-43` | 0.6124695018976312 | 2.0 | # Compensation Discussion & Analysis ## Executive Summary We experienced significant volume pressure throughout 2023 as… |
| 2 | `qeeb1c1a41ae3:10-K:chunk-4` | 0.4661035088800598 | 1.0 | # Proxy Statement Summary # About DuPont We are a global innovation leader with technology-based materials and solution… |
| 3 | `qeeb1c1a41ae3:10-K:chunk-0` | 0.4092498421628234 |  | # UNITED STATES SECURITIES AND EXCHANGE COMMISSION WASHINGTON, D.C. 20549 SCHEDULE (RULE 14a-101) # SCHEDULE 14A INFORM… |
| 4 | `qeeb1c1a41ae3:10-K:chunk-15` | 0.33232278980429464 |  | # Table of Contents (cont.) ## Board's Role in the Oversight of Risk Management The Board is responsible for overseeing… |
| 5 | `qeeb1c1a41ae3:10-K:chunk-109` | 0.23644373337723412 |  | # Reconciliation of "Cash provided by operating activities - continuing operations" to "Segment Adjusted Free Cash Flow… |

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
| 1 | `qf59bea60dc8d:DEF14A:chunk-9` | 0.531847812289926 |  | Aon plc Condensed Consolidated Statements of Shareholders’ Equity (Deficit) (Unaudited) |
| 2 | `qf59bea60dc8d:DEF14A:chunk-138` | 0.44613980096561817 |  | (1)Does not include commissions paid to repurchase shares. (2)The Repurchase Program was established in April 2012 with… |
| 3 | `qf59bea60dc8d:DEF14A:chunk-137` | 0.40152905792461285 |  | Period##Total Number of Shares Purchased####Average Price Paid per Share (1)##Total Number of Shares Purchased as Part … |
| 4 | `qf59bea60dc8d:DEF14A:chunk-134` | 0.3760395247989674 |  | CRITICAL ACCOUNTING POLICIES AND ESTIMATES There have been no changes in our critical accounting policies, which includ… |
| 5 | `qf59bea60dc8d:DEF14A:chunk-87` | 0.3652395461943975 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations EXECUTIVE SUMMARY OF THIR… |

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
- **S2**: nDCG@5=0.6509209298071326 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0346b2bc5a8b:chunk-49` | 0.7959652926015615 |  | Got it. And last question is before turning it over. Can you help us just think about what's next for PKG from a growth… |
| 2 | `q0346b2bc5a8b:chunk-87` | 0.7882495258113247 | 1.0 | I mean we're probably spending close to $250 million just in the box plants alone this year. And that's all of the 30 s… |
| 3 | `q0346b2bc5a8b:chunk-53` | 0.7181058333884378 |  | Our next question comes from George Staphos from Bank of America Securities. |
| 4 | `q0346b2bc5a8b:chunk-51` | 0.7174692086342556 | 1.0 | Yes, Mike, obviously, you don't know what the future is going to hold, but we've got a lot of optionality in what we're… |
| 5 | `q0346b2bc5a8b:chunk-111` | 0.5583206847781905 |  | I'll let you know when it happens. That's the beauty of having that firepower. We can not only continue to look at shar… |

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
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6252347221754821 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q044bb2c8810c`)._

### ex-dev-q05bfc5cb3e17

- **example_id**: `dev:q05bfc5cb3e17`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Northern Trust Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.33132295434224884 · skipped= · n_scored=315

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q05bfc5cb3e17:chunk-92` | 0.6368225782418652 | 1.0 | RISK MANAGEMENT (continued) Market Risk (continued) The NII sensitivity analysis incorporates certain critical assumpti… |
| 2 | `q05bfc5cb3e17:chunk-0` | 0.4577332838234482 |  | PART I – FINANCIAL INFORMATION Items 2. and 3. Management’s Discussion and Analysis of Financial Condition and Results … |
| 3 | `q05bfc5cb3e17:chunk-204` | 0.3642344026348658 | 2.0 | Allowance Related to Credit Exposure Evaluated on a Collective Basis. Expected credit losses are measured on a collecti… |
| 4 | `q05bfc5cb3e17:chunk-126` | 0.34081804453716885 | 1.0 | (1) Weighted average of expected duration based on scenario probability. The following table presents assets and liabil… |
| 5 | `q05bfc5cb3e17:chunk-305` | 0.33132577151342857 |  | Notes to Consolidated Financial Statements (unaudited) (continued) lives of the instruments as interest rates, foreign … |

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
| 1 | `q09b8cfa51b60:chunk-93` | 0.547433462134603 |  | Segment Operations We organize our operations around, and publicly report our financial results on, three global busine… |
| 2 | `q09b8cfa51b60:chunk-78` | 0.38400681130195397 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations Management’s Discussion a… |
| 3 | `q09b8cfa51b60:chunk-24` | 0.2822349802198777 |  | CBRE GROUP, INC. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Continued) (Unaudited) guidance is effective for fiscal ye… |
| 4 | `q09b8cfa51b60:chunk-136` | 0.25050558204996 |  | ########Incorporated by Reference#### Exhibit No.##Exhibit Description##Form##SEC File No.##Exhibit##Filing Date##Filed… |
| 5 | `q09b8cfa51b60:chunk-61` | 0.23245598668788028 |  | CBRE GROUP, INC. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Continued) (Unaudited) 12. Revenue from Contracts with Cus… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q09b8cfa51b60`)._

### ex-dev-q0b8d55d58be2

- **example_id**: `dev:q0b8d55d58be2`
- **state**: `completed`
- **query**: What questions were asked about Chubb Limited’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9506817003345661 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=370

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0b8d55d58be2:chunk-335` | 0.49662083875290947 |  | (a) Ultimate retention will depend upon the nature of the loss and the interplay between the underlying per risk progra… |
| 2 | `q0b8d55d58be2:chunk-368` | 0.2994115193575016 |  | ##CHUBB LIMITED ##(Registrant) November 1, 2023##/s/ Evan G. Greenberg ##Evan G. Greenberg ##Chairman and Chief Executi… |
| 3 | `q0b8d55d58be2:chunk-290` | 0.27056874432970823 |  | We provide financial measures, including net premiums written, net premiums earned, and underwriting income on a consta… |
| 4 | `q0b8d55d58be2:chunk-261` | 0.25851363532291005 |  | Overseas General Insurance Overseas General Insurance segment comprises Chubb International and Chubb Global Markets (C… |
| 5 | `q0b8d55d58be2:chunk-33` | 0.24631791703240752 |  | (in millions of U.S. dollars)####Amount##Weighted-average useful life Definite life###### Agency distribution relations… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q0b8d55d58be2`)._

### ex-dev-q0d51e9ef12aa

- **example_id**: `dev:q0d51e9ef12aa`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did leadership measure the installed base of RTX PCs and relate it to AI‑application adoption?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5509858876386381 · gold=['8-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q0d51e9ef12aa`)._

### ex-dev-q0e5327ae1aff

- **example_id**: `dev:q0e5327ae1aff`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What concerns have institutional investors raised regarding regulatory risk?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5=0.6309297535714575 · gold=['Earnings']
- **S1 ordered**: `['DEF14A', 'Earnings', '8-K', '10-Q', '10-K']`
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
| 1 | `q0faf9d780cdc:chunk-55` | 0.81540011731032 |  | production. These increases were partially offset by lower net sales of $400 million on the F-35 program due to lower v… |
| 2 | `q0faf9d780cdc:chunk-0` | 0.4401829136815977 |  | PART I ITEM 1. Business General We are a global security and aerospace company principally engaged in the research, des… |
| 3 | `q0faf9d780cdc:chunk-125` | 0.3978083604262045 |  | ####2023####2022####2021 Capital expenditures############ Aeronautics##$##535##$##461##$##477 Missiles and Fire Control… |
| 4 | `q0faf9d780cdc:chunk-32` | 0.34372286355688675 |  | ITEM 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations The following Management’… |
| 5 | `q0faf9d780cdc:chunk-101` | 0.2772043447599729 |  | Lockheed Martin Corporation Notes to Consolidated Financial Statements Note 1 – Organization and Significant Accounting… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q0faf9d780cdc`)._

### ex-dev-q11ef281af9cd

- **example_id**: `dev:q11ef281af9cd`
- **state**: `completed`
- **query**: How does United Rentals select the peer group for benchmarking executive pay?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9840990003623115 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.6309297535714575 · skipped= · n_scored=223

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q11ef281af9cd:chunk-219` | 0.5978209774738954 |  | ######UNITED RENTALS, INC.## Date:##January 24, 2024##By:####/S/ MATTHEW J. FLANNERY ########Matthew J. Flannery, Chief… |
| 2 | `q11ef281af9cd:chunk-199` | 0.49097177463561864 | 1.0 | PART III Item 10. Directors, Executive Officers and Corporate Governance The information required by this Item is incor… |
| 3 | `q11ef281af9cd:chunk-92` | 0.3708361250966542 |  | UNITED RENTALS, INC. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (dollars in millions, except per share data and unless … |
| 4 | `q11ef281af9cd:chunk-0` | 0.25181967927537846 |  | PART I United Rentals, Inc., incorporated in Delaware in 1997, is principally a holding company. We primarily conduct o… |
| 5 | `q11ef281af9cd:chunk-111` | 0.20399055116990153 |  | For general rentals, the divisions discussed below, which are our operating segments, are aggregated into the reportabl… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q11ef281af9cd`)._

### ex-dev-q140516364bb4

- **example_id**: `dev:q140516364bb4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Principal Financial Group’s international expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
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
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7860353577841278 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q1cfcd01ac3a1`)._

### ex-dev-q1ded233d05aa

- **example_id**: `dev:q1ded233d05aa`
- **state**: `completed`
- **query**: What questions were asked about IDEXX Laboratories’ customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.36899318320019464 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1ded233d05aa:chunk-41` | 1.2315915391849979 | 1.0 | Yes. So with respect to the point-of-care platform launches, we have a very well-defined tried and true method of devel… |
| 2 | `q1ded233d05aa:chunk-19` | 1.1084535121414427 |  | Yes. And then -- and just to add some color to Brian's remarks. Yes, the end-market appears to be stabilized and health… |
| 3 | `q1ded233d05aa:chunk-27` | 1.0061205241426494 | 1.0 | Yes. Just some follow-up commentary on the inVue launch. Customers, I think, very excited to learn more about that, as … |
| 4 | `q1ded233d05aa:chunk-35` | 0.6834694038002342 |  | Yes. So let me talk a little bit about inVue and some of the key opinion leader feedback. We've had a number of key opi… |
| 5 | `q1ded233d05aa:chunk-53` | 0.6832947037583023 | 2.0 | Okay. Great. That was very helpful. And then just sort of a long second question, more clarification. So it seems like … |

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
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6321922161264945 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
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
| 1 | `q2173e7c263c1:chunk-98` | 0.68578298327091 |  | experience increased costs of financing, make it difficult to refinance debt at attractive rates or at all, and may adv… |
| 2 | `q2173e7c263c1:chunk-90` | 0.49699587792349526 |  | Item 2: Management’s Discussion and Analysis of Financial Condition and Results of Operations FORWARD-LOOKING STATEMENT… |
| 3 | `q2173e7c263c1:chunk-66` | 0.45686177594811195 |  | The valuation of impaired assets is determined using valuation techniques including discounted cash flow analysis, anal… |
| 4 | `q2173e7c263c1:chunk-137` | 0.3539845466598368 |  | We consider FFO and Normalized FFO to be appropriate supplemental measures of a REIT’s operating performance as they ar… |
| 5 | `q2173e7c263c1:chunk-12` | 0.3360704383294951 |  | REALTY INCOME CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS September 30, 2023 (unaudited) 1.… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2173e7c263c1`)._

### ex-dev-q238a8429d152

- **example_id**: `dev:q238a8429d152`
- **state**: `completed`
- **query**: How does Dominion Energy view the pace of innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.5088013258915567 · skipped= · n_scored=209

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q238a8429d152:chunk-4` | 0.4320259921043174 | 1.0 | # Dominion Energy R Dominion Energy, headquartered in Richmond, Virginia, is one of the nation's largest producers and … |
| 2 | `q238a8429d152:chunk-50` | 0.32435802963151344 | 1.0 | # Sustainability and Corporate Responsibility Committee (cont.) ## Oversight of Sustainability and Corporate Responsibi… |
| 3 | `q238a8429d152:chunk-24` | 0.22210822175756637 | 1.0 | # Robert M. Blue (cont.) ## Qualifications, Attributes and Skills Mr. Blue has in-depth knowledge of the company's indu… |
| 4 | `q238a8429d152:chunk-183` | 0.21220914655660364 |  | # Appendix B (cont.) ## Dominion Energy, Inc. 2024 Incentive Compensation Plan, Effective May 7, 2024 (cont.) (j) "Domi… |
| 5 | `q238a8429d152:chunk-43` | 0.21209521514195556 | 1.0 | # Compensation and Talent Development Committee (cont.) ## ROLE & RESPONSIBILITIES (cont.) # Sustainability and Corpora… |

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
| 2 | `q2451f8377cf4:chunk-61` | 0.376438996140936 |  | I guess, Melanie, probably more for you than Peter. On weather, it sounds like in the guidance, you said maybe 1 or 2 p… |
| 3 | `q2451f8377cf4:chunk-49` | 0.2713367435163269 |  | Yes. So when you look at the guide for next year, you will see kind of that similar formula as what we've always consis… |
| 4 | `q2451f8377cf4:chunk-107` | 0.2579219705267954 |  | Yes. So when you look at the first quarter, if you look kind of historically, you'll kind of see our contribution -- re… |
| 5 | `q2451f8377cf4:chunk-79` | 0.2395238912888304 |  | I think if you look at our history on operating margins, I mean, if new pool construction was back up to 120,000 units,… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2451f8377cf4`)._

### ex-dev-q24d0f908cfe3

- **example_id**: `dev:q24d0f908cfe3`
- **state**: `completed`
- **query**: What guidance was offered on Fox Corporation’s advertising revenue growth targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9278143341459562 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=111

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q24d0f908cfe3:chunk-62` | 0.5929310006102094 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS <table><tr><th>Qualitative Performance Factor</th><th>Fiscal 2023 Achievements</… |
| 2 | `q24d0f908cfe3:chunk-0` | 0.4275886331480543 |  | # UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 # SCHEDULE 14A Proxy Statement Pursuant to Se… |
| 3 | `q24d0f908cfe3:chunk-3` | 0.4183737036316859 |  | # TABLE OF CONTENTS (cont.) This proxy statement contains "forward-looking statements" within the meaning of Section 27… |
| 4 | `q24d0f908cfe3:chunk-61` | 0.406660581582936 |  | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Qualitative Element of Annual Incentive Compensation (cont.) <table><… |
| 5 | `q24d0f908cfe3:chunk-52` | 0.3800865033627336 |  | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Fiscal 2023 Business and Management Review FOX once again delivered s… |

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
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6289921088377346 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
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
- **S2**: nDCG@5=0.2640681225725909 · skipped= · n_scored=47

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q29d3cb8df822:chunk-5` | 1.2656786352749243 |  | On a year-to-date basis, the Core businesscomprising Reservoir Performance, Well Construction, and Production Systems… |
| 2 | `q29d3cb8df822:chunk-0` | 0.5598999054816166 |  | Exhibit 99 News Release SLB Announces Third-Quarter 2023 Results  Revenue of $8.31 billion increased 3% sequentially a… |
| 3 | `q29d3cb8df822:chunk-38` | 0.4524404707925339 |  | <table> <tr> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td></tr> <tr> <td></… |
| 4 | `q29d3cb8df822:chunk-20` | 0.4225052437454616 | 1.0 | Digital operations are gaining in maturity, transforming the way operators develop and utilize assets. From automation … |
| 5 | `q29d3cb8df822:chunk-2` | 0.40974803567405854 |  | * These are non-GAAP financial measures. See sections titled Divisions and Supplementary Information for details. n… |

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
- **S2**: nDCG@5=0.3494746300967186 · skipped= · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2c832749ca0b:chunk-130` | 0.5771373460639356 |  | ____________________________ (1)Represents income (loss) from continuing operations by geographic location before incom… |
| 2 | `q2c832749ca0b:chunk-132` | 0.5771373460639356 |  | ____________________________ (1)Represents income (loss) from continuing operations by geographic location before incom… |
| 3 | `q2c832749ca0b:chunk-192` | 0.44060489352414356 | 2.0 | operations at Lihir and Wafi-Golpu in PNG are subject to political and regulatory risks and other uncertainties” and “—… |
| 4 | `q2c832749ca0b:chunk-102` | 0.4303778450329835 | 1.0 | ITEM 2. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS (dollars in millions, exc… |
| 5 | `q2c832749ca0b:chunk-19` | 0.42039074295476075 | 2.0 | NEWMONT CORPORATION NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS (unaudited, dollars in millions, except per sh… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2c832749ca0b`)._

### ex-dev-q2d8eb319367a

- **example_id**: `dev:q2d8eb319367a`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did UDR, Inc.’s leadership address potential risks or uncertainties in forward-looking statements for its multifamily property portfolio?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.788088263175707 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
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
- **S2**: nDCG@5=0.37077469232984683 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2fe5769567d7:chunk-66` | 0.9499244087175118 | 1.0 | As of September 30, 2023, we expect to recognize $202.1 million of total unamortized compensation costs, net of estimat… |
| 2 | `q2fe5769567d7:chunk-70` | 0.8436172286362609 | 2.0 | As of September 30, 2023, we expect to recognize $11.6 million of total unamortized compensation costs related to futur… |
| 3 | `q2fe5769567d7:chunk-13` | 0.69863935307674 |  | ALIGN TECHNOLOGY, INC. CONDENSED CONSOLIDATED STATEMENTS OF STOCKHOLDERS’ EQUITY (in thousands) (unaudited) |
| 4 | `q2fe5769567d7:chunk-9` | 0.69863935307674 |  | ALIGN TECHNOLOGY, INC. CONDENSED CONSOLIDATED STATEMENTS OF STOCKHOLDERS’ EQUITY (in thousands) (unaudited) |
| 5 | `q2fe5769567d7:chunk-11` | 0.47724841324446804 | 1.0 | ####Common Stock#### Nine Months Ended September 30, 2023##Shares######Amount Balance as of December 31, 2022##77,267##… |

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
| 5 | `q318eb902f451:chunk-19` | 0.5968253665470569 |  | Our next question comes from the line of Benjamin Budish with Barclays. |

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
| 3 | `q31f6fd1f392c:chunk-53` | 0.9226110170943691 | 2.0 | # OTHER EXECUTIVE COMPENSATION PRACTICES AND POLICIES (cont.) ## Incentive Compensation Recovery Policy In September 20… |
| 4 | `q31f6fd1f392c:chunk-41` | 0.8780178525137687 | 2.0 | # Track Record of Growth Driving an Increasing Return of Capital to Shareholders (cont.) ## Good Governance Foundation … |
| 5 | `q31f6fd1f392c:chunk-44` | 0.8511496131223002 | 2.0 | # OUR DECISION MAKING PROCESS (cont.) ## Compensation Peer Group For purposes of setting compensation levels for 2023, … |

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
| 1 | `q3ef7ce37ae77:chunk-47` | 0.5654781665050612 |  | Well, we are building and continue to drive a healthy business. That's been our focus, not only in China, but around th… |
| 2 | `q3ef7ce37ae77:chunk-23` | 0.3773240481994623 |  | Well, maybe I'll kick it off, Ike, and then pass it to Scott again. We do have both strategic and financial strength an… |
| 3 | `q3ef7ce37ae77:chunk-17` | 0.3578669992040826 |  | Scott, Sorry about that technical glitch. I am back on the call, so I appreciate it. And to add, Bob, to the points tha… |
| 4 | `q3ef7ce37ae77:chunk-89` | 0.3406297211877683 |  | Thanks, Christina, and thank you all for joining us and for your continued interest in our story. As we shared today, w… |
| 5 | `q3ef7ce37ae77:chunk-49` | 0.334973614465875 |  | Thank you, Joanne, and good morning, Brooke. Building on what Joanne said, we are very, very bullish on the mid- and lo… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q3ef7ce37ae77`)._

### ex-dev-q3f9446fe3b94

- **example_id**: `dev:q3f9446fe3b94`
- **state**: `completed`
- **query**: How are scenario analyses conducted by American Tower Corporation for risks related to fluctuations in mobile data demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9484971533659527 · gold=['10-K', 'Earnings', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.639945385422766 · skipped= · n_scored=342

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3f9446fe3b94:chunk-15` | 0.7454705308975842 | 1.0 | The development and implementation of new technologies designed to enhance the efficiency of wireless networks or chang… |
| 2 | `q3f9446fe3b94:chunk-6` | 0.6388458025743133 |  | Strategy Operational Strategy As wireless communications technologies advance and the use of wireless services on hands… |
| 3 | `q3f9446fe3b94:chunk-12` | 0.6213387867364091 | 1.0 | ITEM 1A. RISK FACTORS Risks Related to Our Business Strategy A significant decrease in leasing demand for our communica… |
| 4 | `q3f9446fe3b94:chunk-163` | 0.4920953440362285 |  | AMERICAN TOWER CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Tabular amounts in millions, un… |
| 5 | `q3f9446fe3b94:chunk-37` | 0.38686256580134826 | 1.0 | •In less advanced wireless markets where network deployments are in earlier stages, we expect these deployments to driv… |

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
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q430300b97e2f`)._

### ex-dev-q44cfaf358c37

- **example_id**: `dev:q44cfaf358c37`
- **state**: `completed`
- **query**: How do global economic or geopolitical trends shape regional market prospects for Molson Coors Beverage Company's alcoholic beverage portfolio?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.8613098738256916 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q44cfaf358c37:chunk-63` | 1.2143001954023753 | 2.0 | Yes. From a -- from an overall portfolio outside of the U.S., Chris, Canada, we do continue to see softness in the beer… |
| 2 | `q44cfaf358c37:chunk-29` | 0.796534318501894 | 2.0 | Thanks, Bryan. Look, EMEA APAC last year had a tremendous year. We grew top and bottom line double digits. And I don't … |
| 3 | `q44cfaf358c37:chunk-45` | 0.6946532000047341 | 1.0 | Look, I mean, maybe just a comment around the overall industry, right? As I said, despite the headlines you might read,… |
| 4 | `q44cfaf358c37:chunk-27` | 0.6945045651499764 | 1.0 | This is actually Bryan Adams on for Peter. So just kind of rounding out the conversation on the top line. I wanted to t… |
| 5 | `q44cfaf358c37:chunk-57` | 0.6807979810861103 | 1.0 | Well, look, you're right. I mean, we do have regional differences in our cost of goods sold, all driven by -- all the f… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q44cfaf358c37`)._

### ex-dev-q4acd5677c3da

- **example_id**: `dev:q4acd5677c3da`
- **state**: `completed`
- **query**: What questions were asked about Hasbro’s customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9359826917490579 · gold=['Earnings', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.20208310829219417 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4acd5677c3da:chunk-67` | 1.341827121290792 | 1.0 | Well, I think it's, generally speaking, all of the above. However, I think the special emphasis for Universes Beyond is… |
| 2 | `q4acd5677c3da:chunk-21` | 0.8359950751788017 |  | Yes, for sure. So last year, we were fortunate in that, both MAGIC and D&D were growers for us. The MAGIC tabletop busi… |
| 3 | `q4acd5677c3da:chunk-25` | 0.6998319218914982 |  | So first, a clarification, did you say you expect consumer products to be flat in 3Q and then up in 4Q, in that mix, ho… |
| 4 | `q4acd5677c3da:chunk-31` | 0.5485358455563263 |  | Got it. And then on the MAGIC business, I guess how many of the larger releases that you mentioned, would you expect co… |
| 5 | `q4acd5677c3da:chunk-95` | 0.5461204904849576 |  | Next questions come from the line of Linda Bolton-Weiser with D.A. Davidson. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4acd5677c3da`)._

### ex-dev-q4bf1699a63fe

- **example_id**: `dev:q4bf1699a63fe`
- **state**: `completed`
- **query**: What dependency risks exist for Boston Properties, Inc. due to concentration of revenue in a limited number of geographic markets or key tenants?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3642766841292918 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4bf1699a63fe:chunk-99` | 0.47221579921612616 | 1.0 | And I would tell you that the most activity that we are having on a building-by-building basis is, in fact, in our CBD … |
| 2 | `q4bf1699a63fe:chunk-113` | 0.4378339249965967 | 1.0 | So I would tell you that the D.C. market is the most -- one of the most interesting markets from our perspective in the… |
| 3 | `q4bf1699a63fe:chunk-39` | 0.4139472701516288 |  | Yes. And Nick, this is Doug. On your answer to the other question. Without -- we're not going to get into the specifics… |
| 4 | `q4bf1699a63fe:chunk-107` | 0.38833947924929907 | 1.0 | We're seeing the same thing in Boston. And as noted in our discussions internally this last week, for our Boston portfo… |
| 5 | `q4bf1699a63fe:chunk-101` | 0.3774109461967148 | 2.0 | Thanks, Doug. Yes. So we have seen consistently since, at least 2019, gains in occupancy in Midtown Manhattan for Premi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4bf1699a63fe`)._

### ex-dev-q4d8ac905167b

- **example_id**: `dev:q4d8ac905167b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Citigroup Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=894

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4d8ac905167b:chunk-112` | 0.9466060023206386 | 2.0 | specifics and timing of such outcomes. For example, many models used by Citi include assumptions about correlation or l… |
| 2 | `q4d8ac905167b:chunk-294` | 0.9446271858725475 | 2.0 | U.S. real GDP contraction in 2024 of 1.9%, with a peak quarter-over-quarter difference to the base scenario of 1.2% in … |
| 3 | `q4d8ac905167b:chunk-289` | 0.7895522939575444 | 2.0 | Quantitative Component Citi estimates expected credit losses for its quantitative component using (i) its comprehensive… |
| 4 | `q4d8ac905167b:chunk-61` | 0.7062277747379143 | 2.0 | firms’ capital planning practices, focusing on six areas of capital planning: governance, risk management, internal con… |
| 5 | `q4d8ac905167b:chunk-293` | 0.6266058453830335 | 2.0 | (1) The year-over-year growth rate is the percentage change in the real (inflation adjusted) GDP level. Under the base … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4d8ac905167b`)._

### ex-dev-q4e3318b7d0e9

- **example_id**: `dev:q4e3318b7d0e9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are data privacy or cybersecurity concerns affecting industry practices relevant to water technology solutions at Xylem Inc.?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7146598531416503 · gold=['10-K', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['10-Q', '10-K', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4e3318b7d0e9`)._

### ex-dev-q4f1cc6ea4ba6

- **example_id**: `dev:q4f1cc6ea4ba6`
- **state**: `completed`
- **query**: What sentiment trends are visible around Agilent Technologies’ free cash flow outlook and capital spending plans?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.3716702184910473 · skipped= · n_scored=170

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4f1cc6ea4ba6:chunk-49` | 1.344688764226666 | 2.0 | I'll jump right into that one. So I tried to make that come out in the script. But our plans to continue to invest for … |
| 2 | `q4f1cc6ea4ba6:chunk-59` | 0.8329346824085783 |  | Yes. Matt, that's a great question. And we ended the Q4 at just a little under 3% and actually for the full year was gr… |
| 3 | `q4f1cc6ea4ba6:chunk-121` | 0.7211725875794573 |  | Yes. It has the potential to do that. And as we talked about it, we're at the beginning of the year, and so we want to … |
| 4 | `q4f1cc6ea4ba6:chunk-31` | 0.505813347453321 |  | Maybe kind of a follow-up on the 1Q guide. It seems like, again, the order's encouraging. Maybe a little bit prudent on… |
| 5 | `q4f1cc6ea4ba6:chunk-87` | 0.48318041979836984 |  | Yes. I think as we said earlier, Derik, there's reason to believe that [indiscernible] you have the comps working in ou… |

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
- **S2**: nDCG@5=0.38685280723454163 · skipped= · n_scored=64

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q53994e82efbb:chunk-48` | 0.7835429480196661 |  | We experienced decreased net sales in all of our product categories primarily due to a slowing economy, a decline in co… |
| 2 | `q53994e82efbb:chunk-45` | 0.7643878157856536 | 1.0 | We experienced decreased net sales in all of our product categories primarily due to a slow-down in single-family housi… |
| 3 | `q53994e82efbb:chunk-39` | 0.5188075091409956 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations The following discussion … |
| 4 | `q53994e82efbb:chunk-12` | 0.30690682023148436 |  | BUILDERS FIRSTSOURCE, INC. AND SUBSIDIARIES NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS (Unaudited) 1. Basis o… |
| 5 | `q53994e82efbb:chunk-62` | 0.28080318312880115 |  | BUILDERS FIRSTSOURCE, INC. /s/ DAVE RUSH Dave Rush President and Chief Executive Officer (Principal Executive Officer) |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q53994e82efbb`)._

### ex-dev-q56c2aa1b3aa2

- **example_id**: `dev:q56c2aa1b3aa2`
- **state**: `completed`
- **query**: How are scenario analyses conducted by FedEx Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.3903800499921017 · skipped= · n_scored=165

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q56c2aa1b3aa2:chunk-28` | 0.36547034140202295 | 1.0 | # Corporate Governance Matters - Nominees for Election to the Board (cont.) ## Board Risk Oversight The Board of Direct… |
| 2 | `q56c2aa1b3aa2:chunk-153` | 0.3233163491617796 |  | # ADDITIONAL INFORMATION ## General Information The principal executive offices of FedEx Corporation are located at 942… |
| 3 | `q56c2aa1b3aa2:chunk-2` | 0.2892072141707349 |  | # A MESSAGE FROM OUR EXECUTIVE CHAIRMAN AND LEAD INDEPENDENT DIRECTOR To our stockholders, In connection with our 2023 … |
| 4 | `q56c2aa1b3aa2:chunk-59` | 0.21097379789218612 |  | # Executive Compensation - Compensation Discussion and Analysis (cont.) ## Clawback Policies In June 2023, the Board of… |
| 5 | `q56c2aa1b3aa2:chunk-3` | 0.19828393114058626 |  | # NOTICE OF ANNUAL MEETING OF STOCKHOLDERS ## Items of Business <table><tr><th colspan="2">Voting Proposal</th><th>Boar… |

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
- **S2**: nDCG@5=0.6877623875401735 · skipped= · n_scored=174

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q587ea3fc913d:chunk-113` | 1.8892956448056373 | 2.0 | Well, Kristine, as we kind of put out there, there's a sizable piece that's going into Bell, and that's really aligning… |
| 2 | `q587ea3fc913d:chunk-67` | 1.4266276402440565 | 1.0 | Look, Noah. I think, look, the team is doing everything they can to manage costs, control -- do the right cost actions … |
| 3 | `q587ea3fc913d:chunk-111` | 0.7830734998097922 |  | On your restructuring actions, can you provide more details on what you're doing and what your expectations are for the… |
| 4 | `q587ea3fc913d:chunk-123` | 0.7536860264127435 | 2.0 | Look, George, as you know, it takes many months to build an aircraft. So the improvements in both the labor side and th… |
| 5 | `q587ea3fc913d:chunk-77` | 0.729292899057819 | 2.0 | Well, look, I mean we don't -- we're probably not going to break that all the way down, but certainly part of why the d… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q587ea3fc913d`)._

### ex-dev-q5ce8ea5bf1b9

- **example_id**: `dev:q5ce8ea5bf1b9`
- **state**: `completed`
- **query**: What dependency risks exist for Global Payments Inc. due to concentration of revenue in a limited number of payment processing partners or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=119

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5ce8ea5bf1b9:chunk-92` | 0.36371977667709166 |  | ITEM 2—MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following discussion a… |
| 2 | `q5ce8ea5bf1b9:chunk-24` | 0.36256645106317864 |  | NOTES TO UNAUDITED CONSOLIDATED FINANCIAL STATEMENTS NOTE 1—BASIS OF PRESENTATION AND SUMMARY OF SIGNIFICANT ACCOUNTING… |
| 3 | `q5ce8ea5bf1b9:chunk-0` | 0.3615638898209954 |  | PART I - FINANCIAL INFORMATION ITEM 1—FINANCIAL STATEMENTS GLOBAL PAYMENTS INC. UNAUDITED CONSOLIDATED STATEMENTS OF IN… |
| 4 | `q5ce8ea5bf1b9:chunk-93` | 0.30147646191847843 |  | Highlights related to our financial condition at September 30, 2023 and results of operations for the three and nine mo… |
| 5 | `q5ce8ea5bf1b9:chunk-6` | 0.28465986035478147 |  | GLOBAL PAYMENTS INC. UNAUDITED CONSOLIDATED STATEMENTS OF COMPREHENSIVE INCOME (in thousands) |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q5ce8ea5bf1b9`)._

### ex-dev-q5d75c4f1ac86

- **example_id**: `dev:q5d75c4f1ac86`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What progress was reported in international park attendance recovery relative to pre pandemic levels
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5465881385757737 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

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
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7189238908241445 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q60107966eba4`)._

### ex-dev-q63259a02ade0

- **example_id**: `dev:q63259a02ade0`
- **state**: `completed`
- **query**: What does Apple's executive compensation structure look like?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=1.0 · gold=['DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.24090885754831726 · skipped= · n_scored=134

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q63259a02ade0:chunk-50` | 1.486170366730806 | 1.0 | # The Role of the Compensation Consultant (cont.) ## Alignment with Shareholder Value Creation (cont.) The majority of … |
| 2 | `q63259a02ade0:chunk-51` | 1.2216201184102 | 1.0 | # Summary of Other Named Executive Officer Compensation The total target compensation of our four other named executive… |
| 3 | `q63259a02ade0:chunk-84` | 1.0801246112442406 | 1.0 | # Advisory Vote to Approve Executive Compensation (cont.) Motivating and retaining a talented and experienced leadershi… |
| 4 | `q63259a02ade0:chunk-42` | 1.0183870439196943 |  | # Guiding Compensation Principles Our executive compensation program is designed to motivate and reward outstanding per… |
| 5 | `q63259a02ade0:chunk-43` | 0.990097144697776 |  | # Guiding Compensation Principles (cont.) ## Executive Compensation Decision-Making Process (cont.) The People and Comp… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q63259a02ade0`)._

### ex-dev-q636b07dd9c11

- **example_id**: `dev:q636b07dd9c11`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What impact could proposed legislative changes in the U.S. Credit Card Competition Act have on Mastercard?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.6898217095818122 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '8-K', 'Earnings', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q636b07dd9c11`)._

### ex-dev-q645be3b7875e

- **example_id**: `dev:q645be3b7875e`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Merck & Co., Inc.’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.6512141447433527 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
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
| 1 | `q64898e5ba36c:chunk-0` | 0.7534979876415078 |  | PART I Item 1: Business General Waters Corporation (the “Company,” “Waters,” “we,” “our,” or “us”), a global leader in … |
| 2 | `q64898e5ba36c:chunk-92` | 0.7354169177571399 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS 1 Description of Business and Organization Waters Corporation (the “Company,… |
| 3 | `q64898e5ba36c:chunk-2` | 0.6565768194822766 |  | In 2019, the Company introduced the ACQUITY Advanced Polymer ChromatographyTM System, which is the first fully solvent-… |
| 4 | `q64898e5ba36c:chunk-4` | 0.5709907903749786 |  | (“Q-Tof”) instruments, such as the Company’s SYNAPTTM G2-S HDMS System, are often used to analyze the role of proteins … |
| 5 | `q64898e5ba36c:chunk-5` | 0.5657778100828975 |  | Based upon 2023 reports from independent marketing research firms and publicly disclosed sales figures from competitors… |

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
- **S2**: nDCG@5=0.3295833540079424 · skipped= · n_scored=130

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q6d2cc453ca8c:chunk-111` | 1.4263260198341645 | 1.0 | Absolutely. Yes. We're looking forward to the accretion after '24, and it will come, like I said, it's grown mid-teens,… |
| 2 | `q6d2cc453ca8c:chunk-59` | 1.0962807827358039 | 1.0 | Got it. And then just following up on the M&A side of things, leverage at 3x, obviously, strong cash flow generator. Bu… |
| 3 | `q6d2cc453ca8c:chunk-12` | 0.7378428235029568 |  | Deane Dray - Analysts |
| 4 | `q6d2cc453ca8c:chunk-18` | 0.7378428235029568 |  | Deane Dray - Analysts |
| 5 | `q6d2cc453ca8c:chunk-100` | 0.6725459007696653 |  | Alexander Blanton - Analysts |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q6d2cc453ca8c`)._

### ex-dev-q70b3e2802bf7

- **example_id**: `dev:q70b3e2802bf7`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Tyson Foods’ average cost per pound of processed chicken trend compared to the prior period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
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
| 1 | `q70e4aac30ddb:chunk-11` | 0.8566854270333912 |  | [Operator Instructions] Our first question today is coming from Sara Senatore from Bank of America. |
| 2 | `q70e4aac30ddb:chunk-12` | 0.7919891355724459 |  | Sara Senatore - Analysts |
| 3 | `q70e4aac30ddb:chunk-0` | 0.7183540765914684 |  | Operator |
| 4 | `q70e4aac30ddb:chunk-10` | 0.7183540765914684 |  | Operator |
| 5 | `q70e4aac30ddb:chunk-47` | 0.6075745458770341 |  | The only thing I would add to that, Sharon, is that's all part of our reinvention. So it's all about finding ways to be… |

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
- **S2**: nDCG@5=0.12103812696590094 · skipped= · n_scored=86

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q76caada13eca:chunk-15` | 0.39003136290710494 |  | Sure. Well, I'll start with the first question and sort of go product by product. On the lumber side, that's the busine… |
| 2 | `q76caada13eca:chunk-5` | 0.30203464470029145 |  | Thanks, Andy. Good morning, everyone, and thank you for joining us. Yesterday, Weyerhaeuser reported full year GAAP ear… |
| 3 | `q76caada13eca:chunk-55` | 0.2655562454483135 | 1.0 | No. We still have a high degree of conviction about the value of timberlands over time and our ability to generate stro… |
| 4 | `q76caada13eca:chunk-25` | 0.2383735398158306 |  | Sure. Good question. George, candidly, Q4 was a very challenging quarter in the lumber markets. The product pricing, re… |
| 5 | `q76caada13eca:chunk-35` | 0.22434299386195375 |  | Sure. Well, when we look back at 2023, I think the year as a whole is pretty typical in terms of transaction volume, so… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q76caada13eca`)._

### ex-dev-q78d98dc75a82

- **example_id**: `dev:q78d98dc75a82`
- **state**: `completed`
- **query**: How has Humana’s Medicare Advantage segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '8-K', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.7693968268775773 · skipped= · n_scored=283

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q78d98dc75a82:chunk-70` | 0.9805634792886988 | 2.0 | Benefits expense The Insurance segment benefit ratio increased 140 basis points from 86.6% in the 2022 period to 88.0% … |
| 2 | `q78d98dc75a82:chunk-63` | 0.7833894261711135 | 2.0 | Premiums Revenue Consolidated premiums revenue increased $13.6 billion, or 15.5%, from $87.7 billion in the 2022 period… |
| 3 | `q78d98dc75a82:chunk-3` | 0.6183693743748024 | 1.0 | ####Insurance Segment Premiums and Services Revenue####Percent of Consolidated Premiums and Services Revenue## ######(d… |
| 4 | `q78d98dc75a82:chunk-230` | 0.5562703480202347 | 1.0 | ####Insurance####CenterWell######Eliminations/ Corporate####Consolidated ##########(in millions)######## 2023##########… |
| 5 | `q78d98dc75a82:chunk-233` | 0.549894346635778 | 1.0 | ####Insurance####CenterWell######Eliminations/ Corporate####Consolidated ##########(in millions)######## 2022##########… |

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
| 1 | `q79acb772ca6b:chunk-8` | 0.5651595536663916 |  | ITEM 1A. RISK FACTORS The following risk factors as well as the other information included in this Form 10-K, including… |
| 2 | `q79acb772ca6b:chunk-90` | 0.5490549916041998 |  | INGERSOLL RAND INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (in millions, except share and per shar… |
| 3 | `q79acb772ca6b:chunk-286` | 0.5159799939692196 |  | ##Ingersoll Rand Inc.## By:####/s/ Vicente Reynal ####Name: Vicente Reynal ####Title: Chairman of the Board and Chief E… |
| 4 | `q79acb772ca6b:chunk-9` | 0.3775123426626565 |  | success will depend, in large part, on our ability to anticipate and effectively manage these risks associated with our… |
| 5 | `q79acb772ca6b:chunk-228` | 0.3369449850639104 |  | Note 19: Hedging Activities, Derivative Instruments and Credit Risk Hedging Activities The Company is exposed to certai… |

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
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7485147261820462 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7b42f1295dc1`)._

### ex-dev-q7c284aabbba4

- **example_id**: `dev:q7c284aabbba4`
- **state**: `completed`
- **query**: What dependency risks exist for Moderna, Inc. due to concentration of revenue in a limited number of vaccine products or geographic markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9882048111454694 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.42033290860792993 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7c284aabbba4:chunk-0` | 0.9720175907217132 |  | Operator |
| 2 | `q7c284aabbba4:chunk-25` | 0.5155489847366773 | 2.0 | Thanks, Stephen. And Gena, it's Stéphane. On the upside and downside on the sales for this year, I think on the upside,… |
| 3 | `q7c284aabbba4:chunk-11` | 0.3993416648463768 | 2.0 | Thank you, Stephen and Jamey. For Moderna and the patients we serve, 2024 is all about execution: execution in commerci… |
| 4 | `q7c284aabbba4:chunk-51` | 0.3166982359843348 |  | Our next question comes from Geoff Meacham with Bank of America. |
| 5 | `q7c284aabbba4:chunk-9` | 0.2661380621253364 |  | Thank you, Jamey. Good morning or good afternoon, everyone. Today, I'll do a quick review of our clinical highlights fr… |

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
- **S2**: nDCG@5=0.6309297535714575 · skipped= · n_scored=76

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7eb5b91e2366:chunk-69` | 0.7429330177353237 |  | Thanks for the question, Rich. |
| 2 | `q7eb5b91e2366:chunk-7` | 0.2910798445419621 | 1.0 | *Thanks, Tom, and good morning, everyone. As Tom noted, we delivered competitive organic revenue growth for the fourth … |
| 3 | `q7eb5b91e2366:chunk-31` | 0.26953843210664563 |  | Yes. Thanks, Travis. It's Chris. I'll try and give a little extra color. I think consistent with what I've said, again,… |
| 4 | `q7eb5b91e2366:chunk-37` | 0.24857734607659265 |  | Yes. Thanks for the question, Robbie. We feel really good about the -- how we've been moving BD into higher growth spac… |
| 5 | `q7eb5b91e2366:chunk-43` | 0.23725295719637646 |  | Yes. Thanks for the question, Patrick. From a tariff perspective, when we saw this dynamic that happened in the past, w… |

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
- **S2**: nDCG@5=0.17376534287144002 · skipped= · n_scored=156

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ed5279a28b4:chunk-16` | 0.49593195099070764 |  | TERADYNE, INC. NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS (Unaudited) A. THE COMPANY Teradyne, Inc. (“Teradyn… |
| 2 | `q7ed5279a28b4:chunk-104` | 0.4014294658880259 | 1.0 | Item 2: Management’s Discussion and Analysis of Financial Condition and Results of Operations Statements in this Quarte… |
| 3 | `q7ed5279a28b4:chunk-142` | 0.3834975721527798 |  | The decrease in income before income taxes in Semiconductor Test was driven primarily by lower tester sales for mobilit… |
| 4 | `q7ed5279a28b4:chunk-111` | 0.36426375993542015 |  | The decrease in Semiconductor Test revenues of $77.8 million, or 13.5%, was driven primarily by lower tester sales for … |
| 5 | `q7ed5279a28b4:chunk-127` | 0.364102475383112 |  | The decrease in Semiconductor Test revenues of $211.8 million or 13.2%, was driven primarily by lower tester sales for … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7ed5279a28b4`)._

### ex-dev-q811679c2d742

- **example_id**: `dev:q811679c2d742`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What challenges are noted regarding scaling infrastructure or capacity for renewable energy integration to meet growth?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.5831428296492145 · gold=['10-K', '8-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', 'DEF14A', '8-K', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

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
| 5 | `q84038a74fd59:chunk-59` | 0.25850461085845816 |  | I guess maybe just a multi-parter. You mentioned a couple of times that with the AI workload adoption that you're seein… |

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
- **S2**: nDCG@5=0.22854179986184534 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88819064dbb7:chunk-59` | 0.7452477210804127 |  | Yes, recapturing the sales. I think we feel pretty bullish about that. A lot of these stores that were rationalizing ou… |
| 2 | `q88819064dbb7:chunk-45` | 0.7284402322944546 | 1.0 | Yes. Great questions. First thing I'll say to you, John, is we will stagger the rollout. I like to spread an initiative… |
| 3 | `q88819064dbb7:chunk-89` | 0.6881903075670525 | 1.0 | Yes. Another really good question. I would look at you and say the initiatives have worked in every store. The problem … |
| 4 | `q88819064dbb7:chunk-21` | 0.6001235345082554 |  | Yes. I mean obviously, our guidance -- we're looking for a strong year, particularly on the Dollar Tree side. And I thi… |
| 5 | `q88819064dbb7:chunk-83` | 0.5765206815972544 |  | Yes. The way we're looking at this, once again, it depends on the -- your assumption on the penetration of our customer… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q88819064dbb7`)._

### ex-dev-q88db5d96c8dd

- **example_id**: `dev:q88db5d96c8dd`
- **state**: `completed`
- **query**: How does Bristol-Myers Squibb manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.6932817824006374 · skipped= · n_scored=176

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88db5d96c8dd:chunk-166` | 0.8246607717329292 | 2.0 | (a)Includes shares repurchased as part of publicly announced programs and shares of common stock surrendered to the Com… |
| 2 | `q88db5d96c8dd:chunk-102` | 0.6362960463539797 |  | Dollars in millions####Restricted Stock Units####Market Share Units####Performance Share Units Unrecognized compensatio… |
| 3 | `q88db5d96c8dd:chunk-101` | 0.5265376903152804 |  | Units in millions##Units####Weighted-Average Fair Value Restricted stock units##9.3##$##60.52 Market share units##1.0##… |
| 4 | `q88db5d96c8dd:chunk-87` | 0.44198587342113416 | 1.0 | ####Common Stock########Capital in Excess of Par Value of Stock####Accumulated Other Comprehensive Loss####Retained Ear… |
| 5 | `q88db5d96c8dd:chunk-174` | 0.3819857247600161 |  | ######BRISTOL-MYERS SQUIBB COMPANY (REGISTRANT)## Date:##October 26, 2023##By:####/s/ Giovanni Caforio, M.D. ########Gi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q88db5d96c8dd`)._

### ex-dev-q89953a08e494

- **example_id**: `dev:q89953a08e494`
- **state**: `completed`
- **query**: How does Globe Life Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.38722694780001 · skipped= · n_scored=125

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89953a08e494:chunk-66` | 0.7314244564154995 | 1.0 | # Assessment of 2023 Advisory Vote on Executive Compensation (cont.) ## Long-Term Equity Incentives We award long-term … |
| 2 | `q89953a08e494:chunk-88` | 0.6728417224208267 |  | # OPTION EXERCISES AND STOCK VESTED DURING FISCAL YEAR ENDED DECEMBER 31, 2023 (cont.) - 7 Executive acquired shares on… |
| 3 | `q89953a08e494:chunk-86` | 0.5629187669401816 | 1.0 | # OUTSTANDING EQUITY AWARDS AT FISCAL YEAR-END 2023 (continued) (cont.) - 1 Stock options vest at the rate of 50% on se… |
| 4 | `q89953a08e494:chunk-67` | 0.4694489028817919 | 2.0 | # Assessment of 2023 Advisory Vote on Executive Compensation (cont.) ## Long-Term Equity Incentives (cont.) The 2018 Pl… |
| 5 | `q89953a08e494:chunk-99` | 0.4411161157501378 |  | # PAY VERSUS PERFORMANCE (cont.) 2 Amounts shown represent compensation actually paid (CAP) and include adjustments for… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q89953a08e494`)._

### ex-dev-q89fb186f5e49

- **example_id**: `dev:q89fb186f5e49`
- **state**: `completed`
- **query**: What investor views emerged on Linde’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.21398626473452756 · skipped= · n_scored=287

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89fb186f5e49:chunk-36` | 0.7115197700483573 |  | Table of Contents SEGMENT DISCUSSION Linde’s operations consist of two major product lines: industrial gases and engine… |
| 2 | `q89fb186f5e49:chunk-5` | 0.6819682407400508 | 1.0 | Table of Contents ITEM 1A. RISK FACTORS Due to the size and geographic reach of the company’s operations, a wide range … |
| 3 | `q89fb186f5e49:chunk-0` | 0.5898851536217281 |  | PART I ITEM 1. BUSINESS General Linde plc is a public limited company formed under the laws of Ireland with its princip… |
| 4 | `q89fb186f5e49:chunk-31` | 0.5858184045155693 |  | 2023 Compared With 2022 Sales Linde sales decreased $510 million, or 2%, for the 2023 year versus 2022. Higher pricing … |
| 5 | `q89fb186f5e49:chunk-66` | 0.4193813189753483 |  | Table of Contents geographic locations in which it operates. Actual results in any given year will often differ from ac… |

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
- **S2**: nDCG@5=0.9828920819566879 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8ba6a388d681:chunk-101` | 1.0435262268949936 | 1.0 | Hock, in the past, I think we've all been aware that there's one major customer on the accelerated compute side, I susp… |
| 2 | `q8ba6a388d681:chunk-51` | 0.9170239037381489 | 1.0 | I mean you did say 65% on it. I think I recall you saying you were going to run VMware at 65%. So I guess, 65% is the r… |
| 3 | `q8ba6a388d681:chunk-49` | 0.9151767083931852 | 1.0 | It's somewhere between 60% and 65%. How does that sound, Stacy? |
| 4 | `q8ba6a388d681:chunk-23` | 0.6628877660702034 |  | Well, that's a good question. Well, we will -- just to give you an indication, in 2024 because it's an accelerating tre… |
| 5 | `q8ba6a388d681:chunk-95` | 0.6587959698785629 | 1.0 | Hock, I guess I'll caveat my question saying that I'm a semiconductor guy rather than a software expert. But I wanted t… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q8ba6a388d681`)._

### ex-dev-q8cc1033cf552

- **example_id**: `dev:q8cc1033cf552`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance did The Sherwin-Williams Company’s leadership provide on debt reduction or leverage targets for The Sherwin-Williams Company?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7378720384008995 · gold=['10-K', 'Earnings', '10-Q']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-K', '10-Q', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

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
| 1 | `q8e053e02a010:chunk-140` | 0.3407479885323588 |  | # Supplemental (cont.) ## Most Important Performance Measures (cont.) Table of Contents The image shows a close-up view… |
| 2 | `q8e053e02a010:chunk-31` | 0.16832211140529332 |  | # Table of Contents (cont.) ## Mark S. Sutton Mr. Sutton has been Chairman of International Paper since January 1, 2015… |
| 3 | `q8e053e02a010:chunk-85` | 0.14916175461929845 |  | # Table of Contents (cont.) ## The footnotes below explain the details of our performance metric calculations for purpo… |
| 4 | `q8e053e02a010:chunk-38` | 0.1457262030989994 |  | # Corporate Governance / How the Board Operates (cont.) ## Responsibilities - Assisting our Board in monitoring the int… |
| 5 | `q8e053e02a010:chunk-11` | 0.1452402314827073 |  | # Proxy Summary / Our Commitment to Sustainability (cont.) ## Our Approach to Climate We recognize the impacts of clima… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q8e053e02a010`)._

### ex-dev-q8e26f08be2bc

- **example_id**: `dev:q8e26f08be2bc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What challenges arise for Vertex Pharmaceuticals from data privacy regulations and handling of patient data?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5=0.5906415461191282 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'DEF14A', 'Earnings', '8-K', '10-K']`
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
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=208

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q93fb2b2861c4:chunk-11` | 1.5861781582903185 | 2.0 | COMPETITION We compete in the household and personal care consumer product categories, which are highly innovative cate… |
| 2 | `q93fb2b2861c4:chunk-131` | 0.5449714953207403 | 2.0 | CHURCH & DWIGHT CO., INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – (Continued) (In millions, excep… |
| 3 | `q93fb2b2861c4:chunk-42` | 0.5390996535290042 |  | CHURCH & DWIGHT CO., INC AND SUBSIDIARIES (Dollars in millions, except share and per share data) ITEM 7. MANAGEMENT’S D… |
| 4 | `q93fb2b2861c4:chunk-99` | 0.4378551016912389 |  | CHURCH & DWIGHT CO., INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (In millions, except share and pe… |
| 5 | `q93fb2b2861c4:chunk-20` | 0.3931598149626678 |  | •Decreases in demand for our products would decrease our sales and profitability. Factors that can affect demand includ… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q93fb2b2861c4`)._

### ex-dev-q95535bca90c9

- **example_id**: `dev:q95535bca90c9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Wells Fargo’s average cost per loan origination trend compared to the prior period?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6623468500578608 · gold=['10-Q', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
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
- **S2**: nDCG@5=0.2591217516005785 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q98c606bb3ce7:chunk-6` | 0.7862677917204209 | 1.0 | Table of Contents ITEM 1A. RISK FACTORS A description of the risks and uncertainties associated with our business is se… |
| 2 | `q98c606bb3ce7:chunk-5` | 0.6727008328728106 |  | Table of Contents domain names, trade secrets and other intellectual property and proprietary technology that we hold a… |
| 3 | `q98c606bb3ce7:chunk-61` | 0.5791301854112526 |  | See Notes to Consolidated Financial Statements. Williams-Sonoma, Inc. Consolidated Statements of Comprehensive Income |
| 4 | `q98c606bb3ce7:chunk-23` | 0.5733455954921082 | 2.0 | Table of Contents cause delays in locating and shipping products, and increases in costs associated with inventory that… |
| 5 | `q98c606bb3ce7:chunk-142` | 0.5677096898346843 |  | ####WILLIAMS-SONOMA, INC.## Date: March 20, 2024##By####/S/ LAURA ALBER ######Laura Alber ######Chief Executive Officer |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q98c606bb3ce7`)._

### ex-dev-q99a077efaab0

- **example_id**: `dev:q99a077efaab0`
- **state**: `completed`
- **query**: What dependency risks exist for Align Technology due to concentration of revenue in a limited number of orthodontic practices or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.2640681225725909 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99a077efaab0:chunk-117` | 0.5002706609288522 |  | Yes. I can't -- I really wouldn't break it out between Americas and International because we felt good about the geogra… |
| 2 | `q99a077efaab0:chunk-87` | 0.4499798903222344 |  | Michael, this is John. I would say as we look to expand this out, it's been successful every place that we've gone. We'… |
| 3 | `q99a077efaab0:chunk-33` | 0.28480006774481453 |  | All right. Fair enough. And then, Joe, I think we've talked for many years now how iTero has carved out such a commandi… |
| 4 | `q99a077efaab0:chunk-3` | 0.2715220645312076 | 1.0 | Thanks, Shirley. Good afternoon, and thanks for joining us. On our call today, I'll provide an overview of our fourth q… |
| 5 | `q99a077efaab0:chunk-45` | 0.25755500380086854 |  | So Joe, maybe this one's for you. Video 1Q '24 IPE some markets today, but more in the common IPE should have longer te… |

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
| 1 | `q99ec5f1aeea5:chunk-6` | 0.8885747530214517 |  | Occupancy The portfolio was 92.2% occupied and 94.2% leased as of December 31, 2023. Additionally, our comparable resid… |
| 2 | `q99ec5f1aeea5:chunk-49` | 0.7128416351751702 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="3">Notes:</td><td colspan="3"></… |
| 3 | `q99ec5f1aeea5:chunk-29` | 0.5607775737912686 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 4 | `q99ec5f1aeea5:chunk-64` | 0.5243463759164908 |  | The change in rental income on comparable space leases is impacted by numerous factors including current market rates, … |
| 5 | `q99ec5f1aeea5:chunk-52` | 0.4973740773426911 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="3">Notes:</td><td colspan="3"></… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q99ec5f1aeea5`)._

### ex-dev-q9a5cfe35fecd

- **example_id**: `dev:q9a5cfe35fecd`
- **state**: `completed`
- **query**: What dependency risks exist for CMS Energy Corporation due to concentration of revenue in a limited number of geographic regions or key utility customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5453092190767764 · skipped= · n_scored=194

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9a5cfe35fecd:chunk-167` | 0.6218762685069419 | 1.0 | product comprising the commodity, electricity or natural gas, and the service of delivering such commodity. In some ins… |
| 2 | `q9a5cfe35fecd:chunk-72` | 0.5657104565440844 | 2.0 | •gas price changes •Michigan’s economic conditions, including population trends and housing activity •the price or dema… |
| 3 | `q9a5cfe35fecd:chunk-24` | 0.5262744471426771 | 2.0 | CMS Energy Corporation Consumers Energy Company Management’s Discussion and Analysis of Financial Condition and Results… |
| 4 | `q9a5cfe35fecd:chunk-62` | 0.49292269589603355 | 1.0 | Outlook Several business trends and uncertainties may affect CMS Energy’s and Consumers’ financial condition and result… |
| 5 | `q9a5cfe35fecd:chunk-18` | 0.38287137104085994 |  | •potentially adverse regulatory treatment, effects of a failure to receive timely regulatory orders that are or could c… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9a5cfe35fecd`)._

### ex-dev-q9c255237096a

- **example_id**: `dev:q9c255237096a`
- **state**: `completed`
- **query**: What perquisites or fringe benefits are included in The AES Corporation’s executive compensation disclosures?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=1.0 · gold=['DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.3077499832503558 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9c255237096a:chunk-56` | 1.448388005181804 |  | # Three-Year CEO LTC Realizable Pay (cont.) ## Severance and Change-in-Control Arrangements The Company maintains certa… |
| 2 | `q9c255237096a:chunk-71` | 1.1264391222798038 | 1.0 | # 2023 Option Exercises and Stock Vested (cont.) ## Potential Payments upon Termination under the Executive Severance P… |
| 3 | `q9c255237096a:chunk-68` | 1.0650548809178324 | 1.0 | # 2023 Option Exercises and Stock Vested (cont.) ## Narrative Disclosure Relating to the Non-Qualified Deferred Compens… |
| 4 | `q9c255237096a:chunk-44` | 1.0221740073496788 | 1.0 | # Overview of AES Total Compensation ## Elements of Compensation The following table presents each element of compensat… |
| 5 | `q9c255237096a:chunk-54` | 0.7953802539382147 | 2.0 | # Three-Year CEO LTC Realizable Pay <table> <tr> <th>Year</th> <th>Type</th> <th>RSU</th> <th>PSU</th> <th>PCU</th> <th… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9c255237096a`)._

### ex-dev-q9dd3907388e3

- **example_id**: `dev:q9dd3907388e3`
- **state**: `completed`
- **query**: How does Duke Energy view the pace of innovation cycles in renewable energy technologies and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.5 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9dd3907388e3:chunk-43` | 0.5274771726588062 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 2 | `q9dd3907388e3:chunk-45` | 0.5274771726588062 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 3 | `q9dd3907388e3:chunk-6` | 0.3589862954159404 | 1.0 | ◦The ability to implement our business strategy, including our carbon emission reduction goals; ◦State, federal and for… |
| 4 | `q9dd3907388e3:chunk-31` | 0.29234780578129477 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3"></td><td></… |
| 5 | `q9dd3907388e3:chunk-33` | 0.29234780578129477 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3"></td><td></… |

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
- **S2**: nDCG@5=0.22201468685328482 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa057a3d428a2:chunk-20` | 0.4530043995050959 |  | McKESSON CORPORATION FINANCIAL NOTES (UNAUDITED) 1. Significant Accounting Policies Nature of Operations: McKesson Corp… |
| 2 | `qa057a3d428a2:chunk-89` | 0.41577864174512524 |  | McKESSON CORPORATION FINANCIAL NOTES (CONTINUED) (UNAUDITED) The RxTS segment helps solve medication access, affordabil… |
| 3 | `qa057a3d428a2:chunk-102` | 0.40309255901712926 | 1.0 | MD&A Index McKESSON CORPORATION FINANCIAL REVIEW (CONTINUED) (UNAUDITED) Revenues Revenues increased for the three and … |
| 4 | `qa057a3d428a2:chunk-96` | 0.36259226312631443 | 2.0 | MD&A Index McKESSON CORPORATION FINANCIAL REVIEW (CONTINUED) (UNAUDITED) The following summarizes our four reportable s… |
| 5 | `qa057a3d428a2:chunk-111` | 0.3572456734262045 |  | MD&A Index McKESSON CORPORATION FINANCIAL REVIEW (CONTINUED) (UNAUDITED) Nine Months Ended December 31, 2023 vs. 2022 M… |

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
- **S2**: nDCG@5=0.23307160661695003 · skipped= · n_scored=255

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa5c748248a5b:chunk-94` | 1.1220988746696372 | 1.0 | Total Run Rate increased 15.8% for the year ended December 31, 2023, driven by a 16.0% increase from recurring subscrip… |
| 2 | `qa5c748248a5b:chunk-42` | 0.4084048086134618 | 1.0 | Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations The following Management’… |
| 3 | `qa5c748248a5b:chunk-147` | 0.3850123074233071 |  | The amount of revenue recognized in the period that was included in the opening current deferred revenue, which reflect… |
| 4 | `qa5c748248a5b:chunk-43` | 0.3569148007441541 | 1.0 | Asset-based fees represent fees earned that are variable in nature, as they are primarily calculated based on the AUM l… |
| 5 | `qa5c748248a5b:chunk-135` | 0.31699641077709817 |  | Deferred Revenue Deferred revenues represent both cash received and the amounts billed to clients for products and serv… |

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
| 1 | `qa602975e3d19:chunk-62` | 0.3109193389297581 |  | # COMPENSATION DISCUSSION AND ANALYSIS (CD&A) (cont.) ## Net Revenues ## Cash Flow Reported Net Revenues Growth +14.4% … |
| 2 | `qa602975e3d19:chunk-161` | 0.2886265238224135 |  | # Back to Contents (cont.) (7) Acquisition integration costs and contingent consideration adjustments include one-time … |
| 3 | `qa602975e3d19:chunk-2` | 0.2861995043171238 |  | # LETTER FROM OUR CHAIR AND CHIEF EXECUTIVE OFFICER (cont.) ## April 5, 2024 (cont.) Our largest global brands, Oreo, M… |
| 4 | `qa602975e3d19:chunk-110` | 0.25914310511656724 |  | # PAY VERSUS PERFORMANCE (cont.) ## Back to Contents (cont.) <table><tr><th>Year</th><th>Plus Average Year End Fair Val… |
| 5 | `qa602975e3d19:chunk-160` | 0.24871121090381137 |  | # Back to Contents (cont.) (1) Divestitures include completed sales of businesses, exits of major product lines upon co… |

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
- **S2**: nDCG@5=0.5 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qaf55b76bfcad:chunk-0` | 0.6241026777684845 |  | Operator |
| 2 | `qaf55b76bfcad:chunk-10` | 0.6241026777684845 |  | Operator |
| 3 | `qaf55b76bfcad:chunk-15` | 0.6239855196432594 | 2.0 | Thanks, Michael. Regarding Charter, first of all, as we said when we did the deal, we think it's a great deal for us. I… |
| 4 | `qaf55b76bfcad:chunk-51` | 0.3342864065886289 |  | First question was on your conversation. |
| 5 | `qaf55b76bfcad:chunk-47` | 0.33130457789965745 |  | Bob, first follow-up on ESPN, clearly a big priority, can you give us some update on types of potential ESPN partners a… |

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
- **S2**: nDCG@5=0.47580096470244104 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb35a5efa65ce:chunk-41` | 0.8811005799614829 | 2.0 | In terms of earnings sensitivity, I wouldn't call it linear from that perspective. These are obviously large industrial… |
| 2 | `qb35a5efa65ce:chunk-43` | 0.8385999341179398 |  | I would just echo Kirk's comment, though, on -- this is David, that the -- these are industrial customers, which, as yo… |
| 3 | `qb35a5efa65ce:chunk-59` | 0.4332432667388116 |  | I would say marginally from that standpoint. Obviously, we had a little a little of a lower increase, obviously, commen… |
| 4 | `qb35a5efa65ce:chunk-73` | 0.428531526867581 | 1.0 | Very -- just one quick follow-up question from Paul Fremont's on the Slide 9, just as opposed to the earnings impact as… |
| 5 | `qb35a5efa65ce:chunk-75` | 0.37729495816604675 |  | What I'll expand is what rates negotiated, of course, very large loads get special contracts. I think the best way to d… |

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
| 1 | `qb500a9b42ef8:chunk-393` | 0.29040668353996013 |  | Table of Contents In some instances, Consumers has specific fixed-term contracts with large commercial and industrial c… |
| 2 | `qb500a9b42ef8:chunk-217` | 0.2508099273457183 |  | Table of Contents CMS Energy Corporation Consumers Energy Company Notes to the Consolidated Financial Statements 1: Sig… |
| 3 | `qb500a9b42ef8:chunk-38` | 0.248903275977034 |  | Table of Contents Part I Item 1. Business General CMS Energy CMS Energy was formed as a corporation in Michigan in 1987… |
| 4 | `qb500a9b42ef8:chunk-397` | 0.24452025350698192 |  | Table of Contents 16: Reportable Segments Reportable segments consist of business units defined by the products and ser… |
| 5 | `qb500a9b42ef8:chunk-429` | 0.22272383286641692 |  | Table of Contents Report of Independent Registered Public Accounting Firm To the Board of Directors and Stockholder of … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb500a9b42ef8`)._

### ex-dev-qb590e4e6d1ec

- **example_id**: `dev:qb590e4e6d1ec`
- **state**: `completed`
- **query**: How has the ratio of PG&E Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.2802595260297114 · skipped= · n_scored=213

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb590e4e6d1ec:chunk-11` | 0.4286737575972394 | 1.0 | The Utility’s electric and natural gas operating revenues that impacted earnings increased by $977 million, or 9%, in t… |
| 2 | `qb590e4e6d1ec:chunk-194` | 0.37102747381215184 |  | (1) For the nine months ended September 30, 2023, the accrued insurance recoveries decreased for the 2021 Dixie fire wi… |
| 3 | `qb590e4e6d1ec:chunk-145` | 0.36592435379865557 |  | Assets and liabilities measured at fair value on a recurring basis for PG&E Corporation and the Utility are summarized … |
| 4 | `qb590e4e6d1ec:chunk-36` | 0.34621946607013143 |  | 2023 General Rate Case Phase 1 On June 30, 2021, the Utility filed its 2023 GRC application with the CPUC (“the Origina… |
| 5 | `qb590e4e6d1ec:chunk-96` | 0.3274597689348585 | 1.0 | NOTES TO THE CONDENSED CONSOLIDATED FINANCIAL STATEMENTS NOTE 1: ORGANIZATION AND BASIS OF PRESENTATION Organization an… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb590e4e6d1ec`)._

### ex-dev-qba0102803c57

- **example_id**: `dev:qba0102803c57`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Kimco Realty Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3391602052736161 · skipped= · n_scored=332

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba0102803c57:chunk-12` | 0.667184867808521 | 1.0 | Item 1A. Risk Factors We are subject to certain business and legal risks including, but not limited to, the following: … |
| 2 | `qba0102803c57:chunk-22` | 0.6278288137607484 |  | To maintain our REIT status, we may be forced to borrow funds during unfavorable market conditions, and the unavailabil… |
| 3 | `qba0102803c57:chunk-8` | 0.5646436277211976 |  | The Company’s approach in mitigating these risks include but are not limited to (i) carrying additional insurance cover… |
| 4 | `qba0102803c57:chunk-169` | 0.5110354411216065 |  | KIMCO REALTY CORPORATION AND SUBSIDIARIES AND KIMCO REALTY OP, LLC AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STA… |
| 5 | `qba0102803c57:chunk-74` | 0.5108042985208793 |  | Based on the Company’s variable-rate debt balances, interest expense would have increased by $0.2 million for the year … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qba0102803c57`)._

### ex-dev-qba50bc033945

- **example_id**: `dev:qba50bc033945`
- **state**: `completed`
- **query**: What commentary is provided by Teledyne Technologies on demand forecasts in light of government defense spending trends?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.40892216721717317 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba50bc033945:chunk-89` | 0.9869496625282537 | 1.0 | Yes. Okay. And then in past quarters, you sort of broke out [indiscernible] book-to-bill versus legacy Teledyne book-to… |
| 2 | `qba50bc033945:chunk-93` | 0.897736545581024 | 1.0 | Okay. And then a question on you're feeling on incremental defense awards throughout the year. Is there still a lot you… |
| 3 | `qba50bc033945:chunk-21` | 0.8288752401302829 | 1.0 | Alright. Yes. We're right now expecting uptick in those businesses in the second half of the year. We think that what w… |
| 4 | `qba50bc033945:chunk-137` | 0.7241359288987653 | 1.0 | First point, backwards, in '23, we had some nice price increases. I'm going to say broadly 2% to 3%, let's say, 3%. We … |
| 5 | `qba50bc033945:chunk-39` | 0.7196565414985994 | 1.0 | This is Jordan [indiscernible] on for Ron. I wanted to ask, so for the backlog growth in the defense wins that you guys… |

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
| 2 | `qbdbd002b0a41:chunk-27` | 0.3627053262260603 |  | Well, thank you for your question. We've been pleased by the progress we've made. You recall, we started with that 2016… |
| 3 | `qbdbd002b0a41:chunk-5` | 0.33023479703657066 |  | Thanks, Ryan. Good morning, everyone. Thank you for joining us. As we close out 2023, I'd like to start by recognizing … |
| 4 | `qbdbd002b0a41:chunk-3` | 0.31498292990861626 |  | Thanks, Abby. Good morning, everyone, and welcome to Caterpillar's Fourth Quarter of 2023 Earnings Call. I'm Ryan Fiedl… |
| 5 | `qbdbd002b0a41:chunk-55` | 0.30486690951383727 |  | And really you asked the question, I think, honestly, that's one thing that maybe is underappreciated about our perform… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qbdbd002b0a41`)._

### ex-dev-qc03648d89328

- **example_id**: `dev:qc03648d89328`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Moderna’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7591919243197319 · gold=['10-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc03648d89328`)._

### ex-dev-qc187429e2dc5

- **example_id**: `dev:qc187429e2dc5`
- **state**: `completed`
- **query**: What dependency risks exist for Huntington Ingalls Industries, Inc. due to concentration of revenue in a limited number of government defense contracts?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.7994765465672333 · skipped= · n_scored=249

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc187429e2dc5:chunk-12` | 1.7101375442164528 | 2.0 | Current U.S. Government spending levels for defense-related or other programs may not be sustained, and future spending… |
| 2 | `qc187429e2dc5:chunk-11` | 0.7692157798459932 | 2.0 | Item 1A. Risk Factors Our consolidated financial position, results of operations and cash flows are subject to various … |
| 3 | `qc187429e2dc5:chunk-35` | 0.565627719105194 | 1.0 | Our contracts typically fall into one of four categories: firm fixed-price, fixed-price incentive, cost-type, and time … |
| 4 | `qc187429e2dc5:chunk-109` | 0.49107660451528345 | 2.0 | HUNTINGTON INGALLS INDUSTRIES, INC. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS 1. DESCRIPTION OF BUSINESS Huntington In… |
| 5 | `qc187429e2dc5:chunk-5` | 0.4890937831338431 | 1.0 | contractor is normally able to recover costs already incurred on the contract and profit on incurred costs up to the am… |

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
| 1 | `qc8e6b0d72c52:chunk-51` | 0.6342741680154566 |  | Yes. I mean we're $4 billion now with digital doing de minimis EBITDA by 25%, we'd expect to be in the neighborhood of … |
| 2 | `qc8e6b0d72c52:chunk-19` | 0.5511788352477456 |  | Great. And then just to get a sense of in Las Vegas, what type of operating expense growth you're anticipating? And may… |
| 3 | `qc8e6b0d72c52:chunk-99` | 0.37628353563184325 |  | Yes. We've said around 7.5% to 8% for us. We do have a lot of larger players that we know from the casino side that str… |
| 4 | `qc8e6b0d72c52:chunk-111` | 0.30638192191888697 |  | Great. And then as my follow-up for you or for Eric. Just how should we think about, let's call it, EBITDA flow through… |
| 5 | `qc8e6b0d72c52:chunk-131` | 0.27517175889202555 |  | And then a follow-up to the last question, just in terms of the Vegas portfolio. So following the Versailles Tower and … |

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
| 5 | `qcbbca1138c08:chunk-43` | 0.6486545758720014 |  | Yes. On the first part of the question, our current export license in Indonesia goes to May of 2024. And we are continu… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qcbbca1138c08`)._

### ex-dev-qcdb8bc16cf2f

- **example_id**: `dev:qcdb8bc16cf2f`
- **state**: `completed`
- **query**: What guidance was offered on Jack Henry & Associates’ technology platform modernization targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9499797323370371 · gold=['Earnings', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.5635781689741965 · skipped= · n_scored=126

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcdb8bc16cf2f:chunk-95` | 0.9765838528253594 | 2.0 | Sure, Chuck. I'll take it, and Mimi can add some commentary is -- yes, I think -- so it is up from where we were. I don… |
| 2 | `qcdb8bc16cf2f:chunk-43` | 0.8365851592637 |  | Yes, for sure. So I appreciate the question, JD. So I'll start with the first one. So yes, 15 is by far a historical nu… |
| 3 | `qcdb8bc16cf2f:chunk-89` | 0.7475092655834424 | 1.0 | Yes. I think you hit on all of them. I think it is a combination of much of what you described. We continue to look at … |
| 4 | `qcdb8bc16cf2f:chunk-115` | 0.6256903050787299 |  | Yes, it's a great question, James. And so I have a couple of different reference points for you, too. So I know Northco… |
| 5 | `qcdb8bc16cf2f:chunk-63` | 0.6194985788930737 |  | No, Chris. I'll take that. This is Greg. So no, I mean typical -- and just as a reminder really for everybody that typi… |

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
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7659463877163701 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd08d64c0654c`)._

### ex-dev-qd177bdad4bdd

- **example_id**: `dev:qd177bdad4bdd`
- **state**: `completed`
- **query**: What pension discount rate assumption was used for year end valuation?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9751957567060058 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.5968814958455909 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd177bdad4bdd:chunk-173` | 2.3260009270620037 | 2.0 | (a)A pension discount rate of 4.75% was used for the applicable plans following the transaction and remeasurement recog… |
| 2 | `qd177bdad4bdd:chunk-172` | 2.1823060956137286 | 2.0 | ######Qualified Defined Benefit Pension Plans############Retiree Medical and Life Insurance Plans###### ##2023####2022#… |
| 3 | `qd177bdad4bdd:chunk-171` | 0.6468685713229438 |  | Assumptions Used to Determine Benefit Obligations and FAS (Expense) Income We measure the fair value of each plan’s ass… |
| 4 | `qd177bdad4bdd:chunk-19` | 0.5424116624262111 |  | For more information on how these factors could impact earnings, financial position, cash flow and stockholders’ equity… |
| 5 | `qd177bdad4bdd:chunk-78` | 0.5213105854603327 | 1.0 | pension income projected for 2024 would be higher or lower by approximately $60 million. Each year, differences between… |

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
- **S2**: nDCG@5=0.6688571443176244 · skipped= · n_scored=312

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd422350b37cb:chunk-49` | 0.9777655429680203 | 1.0 | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations Generally, the… |
| 2 | `qd422350b37cb:chunk-46` | 0.8472878399348748 | 1.0 | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations ITEM 7 – MANAG… |
| 3 | `qd422350b37cb:chunk-5` | 0.7638486386228335 |  | Part I ♦ Item 1 – Business Due to the localized nature of the industry resulting from the high cost of transportation r… |
| 4 | `qd422350b37cb:chunk-14` | 0.7008200478851891 | 2.0 | Part I ♦ Item 1A – Risk Factors While our business operations cover a wide geographic area, our earnings depend on the … |
| 5 | `qd422350b37cb:chunk-1` | 0.5968755539756023 | 1.0 | Part I ♦ Item 1 – Business Building Materials Business The profitability of the Building Materials business, which serv… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd422350b37cb`)._

### ex-dev-qd483c94f1ec6

- **example_id**: `dev:qd483c94f1ec6`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How do investors view American International Group, Inc.’s valuation relative to peers based on recent disclosures?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7373239404693707 · gold=['DEF14A', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
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
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.5196610607458307 · gold=['Earnings', '10-K']
- **S1 ordered**: `['8-K', '10-Q', 'Earnings', 'DEF14A', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd639a486b106`)._

### ex-dev-qd87c2da5e7da

- **example_id**: `dev:qd87c2da5e7da`
- **state**: `completed`
- **query**: How does Kenvue manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.8539316501572937 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd87c2da5e7da:chunk-56` | 0.6424650199849221 | 1.0 | # 2024 Incentive Compensation (cont.) ## 2024 Long-Term Incentive Award Design Annual long-term incentive awards grante… |
| 2 | `qd87c2da5e7da:chunk-51` | 0.4813966469248465 | 1.0 | # Executive Compensation (cont.) ## Annual Long-Term Incentive Grants Our long-term incentive plan is intended to motiv… |
| 3 | `qd87c2da5e7da:chunk-9` | 0.4486270533964754 | 1.0 | # Executive Compensation Highlights (page 35) Kenvue's executive compensation program is designed to align behaviors wi… |
| 4 | `qd87c2da5e7da:chunk-60` | 0.4365266161541247 |  | # Compensation Clawback Policies (cont.) ## Compensation Risk Management Kenvue is committed to effective risk manageme… |
| 5 | `qd87c2da5e7da:chunk-34` | 0.42443856482121245 | 1.0 | # 2023 Director Compensation Table Fees Earned or Paid in <table><tr><th></th><th colspan="2">or</th><th></th><th rowsp… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd87c2da5e7da`)._

### ex-dev-qdb9da6a1e373

- **example_id**: `dev:qdb9da6a1e373`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Packaging Corporation of America manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8596355563650325 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdb9da6a1e373`)._

### ex-dev-qdbaa829dd4cc

- **example_id**: `dev:qdbaa829dd4cc`
- **state**: `completed`
- **query**: What questions were asked about Gen Digital Inc.’s customer retention and renewal rates?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.4776237035032179 · skipped= · n_scored=227

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdbaa829dd4cc:chunk-18` | 1.440893870711367 |  | •The number, severity and timing of threat outbreaks and cyber security incidents; •Loss of customers or strategic part… |
| 2 | `qdbaa829dd4cc:chunk-9` | 0.6942085211668224 | 1.0 | •Our customers’ dissatisfaction with our efforts to market additional products and services; •Our customer service and … |
| 3 | `qdbaa829dd4cc:chunk-25` | 0.5706424519508619 |  | Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations Please read the following… |
| 4 | `qdbaa829dd4cc:chunk-223` | 0.5061252000156812 |  | ##GEN DIGITAL INC.## By:####/s/ Vincent Pilette ####Vincent Pilette Chief Executive Officer and Director |
| 5 | `qdbaa829dd4cc:chunk-35` | 0.3506896067226492 | 1.0 | ########Fiscal Year###### (In millions, except for per user amounts and percentages)####2024########2023## Direct custo… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdbaa829dd4cc`)._

### ex-dev-qdec70f55027f

- **example_id**: `dev:qdec70f55027f`
- **state**: `completed`
- **query**: What investor views emerged on Mettler-Toledo International Inc.’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9734136950814526 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.850834274847108 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdec70f55027f:chunk-51` | 1.1955624162305432 | 1.0 | Sure, absolutely. And again, I'll probably give you some insights into the different regions, but also in different end… |
| 2 | `qdec70f55027f:chunk-83` | 1.0967724451700707 | 2.0 | Got it. And then just on Europe, you've talked pretty cautiously about it, but I still think, unless I misheard, that y… |
| 3 | `qdec70f55027f:chunk-33` | 1.057676360874274 | 1.0 | I'll take that. Look, Shawn and I had been in China in December. And of course, we're in continued conversations with t… |
| 4 | `qdec70f55027f:chunk-101` | 0.9937621334989603 | 1.0 | Yes. Thanks, Rachel. And I'll start and then Shawn if you have some additional comments, feel free to chime in. So I th… |
| 5 | `qdec70f55027f:chunk-129` | 0.6428651049065923 | 1.0 | Yes. I mean, this has been a very important balancing act for us, something that we've been spending a lot of time as a… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdec70f55027f`)._

### ex-dev-qdfe52ef66df5

- **example_id**: `dev:qdfe52ef66df5`
- **state**: `completed`
- **query**: How has the ratio of IDEXX Laboratories’ recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9452713619732751 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.4869718050522586 · skipped= · n_scored=271

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdfe52ef66df5:chunk-45` | 0.49559787139852385 | 2.0 | Our long-term success in the continuing growth of our CAG recurring diagnostic products and services is dependent upon:… |
| 2 | `qdfe52ef66df5:chunk-48` | 0.447114583600889 |  | consumables strategy, a substantial portion of the revenues from this product line is derived from the sale of consumab… |
| 3 | `qdfe52ef66df5:chunk-42` | 0.4206094724466241 | 1.0 | ITEM 7. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following discussion … |
| 4 | `qdfe52ef66df5:chunk-131` | 0.3695576452051126 | 1.0 | Major Categories of Revenue for our Products and Services Diagnostic Products and Accessories. Diagnostic products and … |
| 5 | `qdfe52ef66df5:chunk-121` | 0.3493774820473646 |  | IDEXX LABORATORIES, INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS NOTE 1. NATURE OF BUSINESS, BASIS … |

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
| 3 | `qe1811f4fd3dc:chunk-7` | 0.8532433913802495 |  | Thank you, Andy. Let me jump right into our fourth quarter results. We signed a total of $110 million of new leases in … |
| 4 | `qe1811f4fd3dc:chunk-95` | 0.820735864307044 |  | Yes. So thanks, Nick. With regard to -- I think I'll go back to some of the comments I had, I think, from one of the fi… |
| 5 | `qe1811f4fd3dc:chunk-41` | 0.5972319937058715 |  | Thanks, Irvin. The -- we certainly have a really great opportunity to intersect with these large capacity block needs o… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qe1811f4fd3dc`)._

### ex-dev-qe2edf9d38872

- **example_id**: `dev:qe2edf9d38872`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Charter Communications’ broadband segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7659463877163701 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qe2edf9d38872`)._

### ex-dev-qe8a08fb7bfff

- **example_id**: `dev:qe8a08fb7bfff`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Meta Platforms, Inc.’s advertising segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
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
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.6857691422200264 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-Q', '10-K', '8-K']`
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
| 1 | `qf25e1308bae4:chunk-59` | 1.0162787841982857 |  | I wanted to ask about the China business. I know that in the prepared comments, you said that you started shipping some… |
| 2 | `qf25e1308bae4:chunk-45` | 0.9589995312354846 |  | Your next question comes from the line of Ben Reitzes from Melius Research. |
| 3 | `qf25e1308bae4:chunk-39` | 0.9582900854118264 |  | Your next question comes from the line of Timothy Arcuri from UBS. |
| 4 | `qf25e1308bae4:chunk-63` | 0.9223694291820232 |  | Your next question comes from the line of Harsh Kumar from Piper Sandler. |
| 5 | `qf25e1308bae4:chunk-57` | 0.9010289484948355 |  | Your next question comes from the line of Aaron Rakers from Wells Fargo. |

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
| 2 | `qf7a3126727b8:chunk-3` | 0.22826402970486837 |  | # LETTER FROM OUR CEO AND CHAIRMAN (cont.) ## Dear Sysco Stockholder, Throughout our rich 54-year history, Sysco has ma… |
| 3 | `qf7a3126727b8:chunk-20` | 0.22231190840593085 |  | # CORPORATE GOVERNANCE (cont.) ## Corporate Governance and Nominating (cont.) <table><tr><th>Technology Committee</th><… |
| 4 | `qf7a3126727b8:chunk-146` | 0.20115710613435114 |  | # ADJUSTED OPERATING INCOME AND ADJUSTED EARNINGS PER SHARE NON-GAAP RECONCILIATIONS (PAY VERSUS PERFORMANCE) <table><t… |
| 5 | `qf7a3126727b8:chunk-19` | 0.18909760461984834 |  | # CORPORATE GOVERNANCE (cont.) ## Corporate Governance and Nominating <table><tr><th>and Nominating Committee</th><th>P… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf7a3126727b8`)._

### ex-dev-qf8cbcec9fec6

- **example_id**: `dev:qf8cbcec9fec6`
- **state**: `completed`
- **query**: How has the ratio of Ingersoll Rand’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9688823411593558 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=117

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf8cbcec9fec6:chunk-116` | 0.3220966842222893 |  | # INGERSOLL RAND INC. AND SUBSIDIARIES UNAUDITED SUPPLEMENTAL ADJUSTED COMBINED FINANCIAL INFORMATION RECONCILIATION OF… |
| 2 | `qf8cbcec9fec6:chunk-0` | 0.3126137858688192 |  | # 2024 Proxy Statement # Notice of Annual Meeting of Stockholders <figure description="The image shows the logo of Inge… |
| 3 | `qf8cbcec9fec6:chunk-111` | 0.2650592430220263 |  | # Annex A (cont.) ## RECONCILIATION OF GAAP MEASURES TO NON-GAAP MEASURES In addition to consolidated GAAP financial me… |
| 4 | `qf8cbcec9fec6:chunk-51` | 0.26061153186380076 |  | # Compensation Discussion and Analysis (cont.) ## RECORD ORDERS OF $6,822M UP 7% OVER 2022 REVENUES OF $6,876M UP 16% O… |
| 5 | `qf8cbcec9fec6:chunk-52` | 0.22606370563992434 |  | # Compensation Discussion and Analysis (cont.) ## ACCELERATE GROWTH <figure description="This image shows a stylized lo… |

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
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
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
- **S2**: nDCG@5=0.43067655807339306 · skipped= · n_scored=114

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff56bedc2f87:chunk-61` | 0.6767025785641501 |  | One thing I would add to that is that I think we're generally pleased clearly with the -- what we were seeing here in t… |
| 2 | `qff56bedc2f87:chunk-47` | 0.6556878138584777 |  | Okay. Yes, we're taking -- over the course of 2024, we kind of see basically the benchmark, we kind of rely mostly on 3… |
| 3 | `qff56bedc2f87:chunk-55` | 0.45108949737863213 |  | Yes. And I think 1 of the things to look at is just really the agent count growth accelerated in the last half of the y… |
| 4 | `qff56bedc2f87:chunk-19` | 0.4469458412194476 | 1.0 | Jimmy, you reflect the full difference between what we had expected in our valuation assumptions versus what we actuall… |
| 5 | `qff56bedc2f87:chunk-1` | 0.33749902199565046 |  | Hello, and welcome to Globe Life Inc.'s Fourth Quarter 2023 Earnings Release. My name is Melissa, and I will be your op… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qff56bedc2f87`)._

### ex-dev-qff73996028bf

- **example_id**: `dev:qff73996028bf`
- **state**: `completed`
- **query**: How has Williams-Sonoma’s management addressed supply-chain risks and efforts to enhance Williams-Sonoma’s resilience?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.7557415207297861 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff73996028bf:chunk-15` | 1.1255717462978785 | 2.0 | Table of Contents In addition, in the past, we have insourced certain aspects of our business, including certain techno… |
| 2 | `qff73996028bf:chunk-39` | 1.0590349048889416 | 2.0 | Table of Contents Elevating our World-Class Customer Service We are continuing to improve our world-class customer serv… |
| 3 | `qff73996028bf:chunk-18` | 0.9098344891242677 | 1.0 | Table of Contents Risks Related to our Suppliers and Global Operations Our dependence on foreign suppliers and our incr… |
| 4 | `qff73996028bf:chunk-2` | 0.7721310665815765 | 2.0 | Table of Contents SUPPLIERS We purchase most of our merchandise from numerous foreign and domestic manufacturers and im… |
| 5 | `qff73996028bf:chunk-142` | 0.7703709690094698 |  | ####WILLIAMS-SONOMA, INC.## Date: March 20, 2024##By####/S/ LAURA ALBER ######Laura Alber ######Chief Executive Officer |

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
| 1 | `chunk_q0b530d:10-K:chunk-15` | 0.49944388342450124 |  | All right. Leanne. And then, Lawson, maybe can you just give us a perspective as you're looking forward, I guess, this … |
| 2 | `chunk_q0b530d:10-K:chunk-17` | 0.4576038138025606 |  | Yes. All right. Bryan. A few things. One, U.S. whiskey and tequila, which are our two biggest categories continue to be… |
| 3 | `chunk_q0b530d:10-K:chunk-27` | 0.43379353612363847 |  | And then the only thing I'll add is, and we've said it in our prepared remarks, again, but just to emphasize it, in the… |
| 4 | `chunk_q0b530d:10-K:chunk-61` | 0.41314093490563386 |  | Lawson, I had two questions. First was just on Jack Daniel's, given all the kind of line extension over the years and d… |
| 5 | `chunk_q0b530d:10-K:chunk-45` | 0.37538719508522017 |  | And this goes back, Lauren, to what we've been saying for quite some time now with all the disruption that has been in … |

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
| 1 | `chunk_q29280e:10-K:chunk-7` | 0.735581849830486 |  | # Compensation Highlights (cont.) ## Key Features of Our Executive Compensation Program ## What We Do ## What We Don't … |
| 2 | `chunk_q29280e:10-K:chunk-0` | 0.5723396676622604 |  | # UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 # SCHEDULE 14A # Proxy Statement Pursuant to … |
| 3 | `chunk_q29280e:10-K:chunk-25` | 0.47359526799136087 |  | # Director Compensation (cont.) ## Long-Term Compensation Each non-employee director is also eligible to participate in… |
| 4 | `chunk_q29280e:10-K:chunk-53` | 0.4732632347669169 |  | # Grants of Plan-Based Awards (cont.) ## Grants of Plan-Based Awards for Fiscal Year 2023(a) (cont.) (c) - The amounts … |
| 5 | `chunk_q29280e:10-K:chunk-47` | 0.42552172016927026 |  | # Roles and Responsibilities (cont.) ## Compensation Risk Assessment The HR Committee reviews our compensation programs… |

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
| 1 | `chunk_q2ccba5:Earnings:chunk-85` | 0.6059693606740816 |  | Yes. Just a few clarifying points. Again, in Europe, where we set 70,000 valves and physicians use it routinely on an e… |
| 2 | `chunk_q2ccba5:Earnings:chunk-0` | 0.5902551597211894 |  | Operator |
| 3 | `chunk_q2ccba5:Earnings:chunk-15` | 0.5111546224290533 |  | Sure. Thanks, Robbie, for the comments. I'll start with WATCHMAN. It's just an excellent platform. With growth of 23% f… |
| 4 | `chunk_q2ccba5:Earnings:chunk-63` | 0.4985131190649963 |  | Maybe one more follow-up on TAVR. Could you remind us what the interim look was? Was that just like a 6-month look at t… |
| 5 | `chunk_q2ccba5:Earnings:chunk-47` | 0.474223148499325 |  | Just a follow-up question on ACURATE neo2, Mike, if I could. So appreciate the comments that you did provide. Just curi… |

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
| 1 | `chunk_q44d295:10-Q:chunk-105` | 0.6452264009779497 |  | AMPHENOL CORPORATION Notes to Consolidated Financial Statements (All amounts included in the following Notes to Consoli… |
| 2 | `chunk_q44d295:10-Q:chunk-44` | 0.4716231626498933 |  | Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations (amounts in millions, exc… |
| 3 | `chunk_q44d295:10-Q:chunk-46` | 0.4443474129720174 |  | Income from continuing operations attributable to Amphenol Corporation are both non-GAAP financial measures, each as de… |
| 4 | `chunk_q44d295:10-Q:chunk-88` | 0.348021935864097 |  | Item 8. Financial Statements and Supplementary Data REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM To the stoc… |
| 5 | `chunk_q44d295:10-Q:chunk-210` | 0.3425192706833739 |  | (1) Long-lived assets included in this table are comprised of property, plant and equipment, net, and operating lease r… |

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
| 2 | `chunk_q5ebb5e:Earnings:chunk-107` | 0.35305364527762734 |  | # Growth Details: <table><tr><th>Goal Description</th><th>How it will be measured</th><th>Formula</th></tr><tr><td>Cont… |
| 3 | `chunk_q5ebb5e:Earnings:chunk-97` | 0.2907589235626792 |  | # QUESTIONS AND ANSWERS REGARDING THE PROXY STATEMENT AND ANNUAL MEETING (cont.) ## Adjusted EPS We define Adjusted EPS… |
| 4 | `chunk_q5ebb5e:Earnings:chunk-99` | 0.24413512490181358 |  | # QUESTIONS AND ANSWERS REGARDING THE PROXY STATEMENT AND ANNUAL MEETING (cont.) ## Adjusted EBITDA We define EBITDA as… |
| 5 | `chunk_q5ebb5e:Earnings:chunk-68` | 0.23796521798490589 |  | # 2023 Option Exercises and Stock Vested (cont.) ## Narrative Disclosure Relating to the Non-Qualified Deferred Compens… |

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
| 2 | `chunk_q829eae:10-Q:chunk-77` | 0.6069833856018859 |  | Table of Contents and related transaction costs are included in “Fulfillment,” AWS costs are primarily classified as “T… |
| 3 | `chunk_q829eae:10-Q:chunk-108` | 0.5394294855378049 |  | ##AMAZON.COM, INC. (REGISTRANT)## By:####/s/ Shelley L. Reynolds ####Shelley L. Reynolds ####Vice President, Worldwide … |
| 4 | `chunk_q829eae:10-Q:chunk-96` | 0.5286305454695553 |  | Table of Contents •the extent to which we invest in technology and infrastructure, fulfillment, and other expense categ… |
| 5 | `chunk_q829eae:10-Q:chunk-63` | 0.451589391386376 |  | Table of Contents Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations Forward… |

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
| 1 | `chunk_q8fc814:Earnings:chunk-25` | 0.82337320929896 |  | So we -- when we set out our 5-year targets a little over 2 years ago, we -- the 5-year target was to get to $150 billi… |
| 2 | `chunk_q8fc814:Earnings:chunk-63` | 0.815459412650186 |  | Sure. So ADIP 2 fundraising, going quite well. We expect to wrap it up this summer in the $4 billion to $5 billion rang… |
| 3 | `chunk_q8fc814:Earnings:chunk-0` | 0.760329575183515 |  | Operator |
| 4 | `chunk_q8fc814:Earnings:chunk-10` | 0.760329575183515 |  | Operator |
| 5 | `chunk_q8fc814:Earnings:chunk-61` | 0.72217228882069 |  | I was wondering if you can give an update on ADIP specifically and then maybe speak a little bit more generally about s… |

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
| 3 | `chunk_q9fad72:10-Q:chunk-99` | 0.7904076484978172 |  | CDW CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (dollars in millions, except per share data… |
| 4 | `chunk_q9fad72:10-Q:chunk-206` | 0.7199602715114815 |  | ######CDW CORPORATION## Date:##February 26, 2024##By:####/s/ Christine A. Leahy ########Christine A. Leahy ########Chai… |
| 5 | `chunk_q9fad72:10-Q:chunk-128` | 0.623793553509704 |  | 7. Inventory Financing Agreements The Company has entered into agreements with financial institutions to facilitate the… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q9fad72`)._

### ex-eval-doc-q0617ad

- **example_id**: `eval:doc_q0617ad`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did F5’s leadership say about F5’s share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '8-K', '10-Q', '10-K']`
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
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:doc_q737b56`)._

### ex-eval-doc-qa9fda3

- **example_id**: `eval:doc_qa9fda3`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does The AES Corporation account for currency and economic volatility in its risk management disclosures?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:doc_qa9fda3`)._
