# Pair `lux-unsloth-score-yield` — `yield-unsloth-score-paper-n200`

[← compact index](../yield-unsloth-score-paper-n200.inspect.md) · **Download full HTML**: [raw](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) · [`yield-unsloth-score-paper-n200.inspect.html`](../yield-unsloth-score-paper-n200.inspect.html)

- eval_run_id: `yield-unsloth-score-paper-n200:lux-unsloth-score-yield`
- S1=`frozen-lux-choice` · S2=`bm25-unsloth-score-shortlist-32`
- row status: `completed` · completed=196 · failed_retriable=4

## Examples

### ex-dev-chunk-only-q075970f6eb46

- **example_id**: `dev:chunk-only:q075970f6eb46`
- **state**: `completed`
- **query**: What did Fastenal Company’s leadership say about Fastenal Company’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '10-Q', '8-K']`
- **yield**: original=`DEF14A` · effective=`DEF14A` · used=False
- **S2**: nDCG@5=0.7227265726449519 · skipped= · n_scored=105

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q075970f6eb46:DEF14A:chunk-22` | 0.876 | 1.0 | (1) The fasteners product line represents fasteners and miscellaneous supplies. (3) Stockholders' Equity Dividends On O… |
| 2 | `q075970f6eb46:DEF14A:chunk-93` | 0.6612 | 1.0 | Net Cash Provided by Operating Activities Net cash provided by operating activities increased by $439.6 in the first ni… |
| 3 | `q075970f6eb46:DEF14A:chunk-70` | 0.6088 | 1.0 | The increase in our accounts receivable balance in the third quarter of 2023 is primarily attributable to two factors. … |
| 4 | `q075970f6eb46:DEF14A:chunk-28` | 0.2011 |  | All of the options in the tables above vest and become exercisable over a period of up to eight years. Generally, each … |
| 5 | `q075970f6eb46:DEF14A:chunk-10` | 0.14459999999999998 |  | ######(Unaudited)########(Unaudited)## ######Nine Months Ended September 30,########Three Months Ended September 30,## … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q075970f6eb46`)._

### ex-dev-chunk-only-q0fd4ca04c0a5

- **example_id**: `dev:chunk-only:q0fd4ca04c0a5`
- **state**: `completed`
- **query**: How does Molina Healthcare view the pace of innovation cycles in healthcare delivery and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.36005461457723403 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0fd4ca04c0a5:10-K:chunk-27` | 0.46430000000000005 |  | or 89.1%, our net income per diluted share for the year ended December 31, 2023 would have been approximately $14.51 ra… |
| 2 | `q0fd4ca04c0a5:10-K:chunk-18` | 0.3361 | 1.0 | Medical Cost Management We use various strategies to mitigate the negative effects of healthcare cost inflation. Specif… |
| 3 | `q0fd4ca04c0a5:10-K:chunk-8` | 0.30369999999999997 |  | continue to focus on driving market share gains through improved execution of enrollment and retention. Approximately $… |
| 4 | `q0fd4ca04c0a5:10-K:chunk-29` | 0.1676 | 1.0 | regulators, and implementing our data security measures. Our members and providers also depend upon our information sys… |
| 5 | `q0fd4ca04c0a5:10-K:chunk-100` | 0.07129999999999999 |  | established when management determines it is more likely than not that some portion, or all, of the deferred tax assets… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q0fd4ca04c0a5`)._

### ex-dev-chunk-only-q299865e6e67e

- **example_id**: `dev:chunk-only:q299865e6e67e`
- **state**: `completed`
- **query**: What dependency risks exist for Consolidated Edison due to concentration of revenue in a limited number of service territories or customer segments?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.4759908431563516 · skipped= · n_scored=286

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q299865e6e67e:10-K:chunk-48` | 0.6733 | 1.0 | NOTES TO THE FINANCIAL STATEMENTS (UNAUDITED) General These combined notes accompany and form an integral part of the s… |
| 2 | `q299865e6e67e:10-K:chunk-166` | 0.662 | 2.0 | and gas businesses may impact the Companies’ future financial condition. The Utilities expect electric usage to increas… |
| 3 | `q299865e6e67e:10-K:chunk-262` | 0.6062000000000001 | 1.0 | Cash Flows from Operating Activities The Utilities’ cash flows from operating activities primarily reflect their energy… |
| 4 | `q299865e6e67e:10-K:chunk-208` | 0.5376 | 1.0 | (a)O&R’s New York electric delivery revenues are subject to a revenue decoupling mechanism, as a result of which delive… |
| 5 | `q299865e6e67e:10-K:chunk-228` | 0.3129 | 1.0 | (a)Revenues from electric sales are subject to a revenue decoupling mechanism, as a result of which delivery revenues g… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q299865e6e67e`)._

### ex-dev-chunk-only-q2a401c1edf73

- **example_id**: `dev:chunk-only:q2a401c1edf73`
- **state**: `completed`
- **query**: How often is Exxon Mobil Corporation’s executive compensation program reviewed and updated?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **yield**: original=`DEF14A` · effective=`DEF14A` · used=False
- **S2**: nDCG@5=0.9125299483251055 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2a401c1edf73:DEF14A:chunk-56` | 0.9245000000000001 | 2.0 | # EXECUTIVE SUMMARY (cont.) ## Shareholder Engagement <table><tr><th>Say-on-Pay</th><th>2023</th><th>2022</th><th>2021<… |
| 2 | `q2a401c1edf73:DEF14A:chunk-43` | 0.8446 | 2.0 | # Table of Contents ## Compensation Committee The Compensation Committee is comprised exclusively of non-employee, inde… |
| 3 | `q2a401c1edf73:DEF14A:chunk-55` | 0.8018000000000001 | 2.0 | # EXECUTIVE COMPENSATION (cont.) ## EXECUTIVE COMPENSATION TABLES <table><tr><th>Summary Compensation Table</th><th>70<… |
| 4 | `q2a401c1edf73:DEF14A:chunk-54` | 0.5137 | 2.0 | # Table of Contents (cont.) ## COMPENSATION COMMITTEE REPORT The Compensation Committee of the Board of Directors has r… |
| 5 | `q2a401c1edf73:DEF14A:chunk-105` | 0.35040000000000004 | 1.0 | # Table of Contents (cont.) ## Our executive compensation program is designed to drive sustainable growth in shareholde… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q2a401c1edf73`)._

### ex-dev-chunk-only-q3a71644741b7

- **example_id**: `dev:chunk-only:q3a71644741b7`
- **state**: `completed`
- **query**: What questions were asked about Conagra Brands’ customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.43225581731890433 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3a71644741b7:Earnings:chunk-67` | 0.8583 | 1.0 | Maybe I can just follow up on Rob's question from a different angle. And Sean, I'd love to hear your perspective on thi… |
| 2 | `q3a71644741b7:Earnings:chunk-77` | 0.851 | 2.0 | I just wanted to clarify on promotional activity and other types of brand building that you've referenced. How does the… |
| 3 | `q3a71644741b7:Earnings:chunk-29` | 0.40559999999999996 | 1.0 | Yes, David, sure. Today, in our material as an example, to your point, I shared the consumption trends for our Frozen b… |
| 4 | `q3a71644741b7:Earnings:chunk-9` | 0.294 | 1.0 | Sure, Andrew. Here's how I think about that. The operative word is transition. It's a process. It's not an event. And a… |
| 5 | `q3a71644741b7:Earnings:chunk-63` | 0.2938 |  | Yes. I think any large diversified food company is going to sell products to pretty much every income level. And I thin… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q3a71644741b7`)._

### ex-dev-chunk-only-q40d417892141

- **example_id**: `dev:chunk-only:q40d417892141`
- **state**: `completed`
- **query**: What investor views emerged on D.R. Horton’s geographic expansion prospects within new U.S. housing markets?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.3391602052736161 · skipped= · n_scored=27

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q40d417892141:Earnings:chunk-27` | 0.0421 | 1.0 | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 2 | `q40d417892141:Earnings:chunk-22` | 0.0393 |  | [Chunk Index 23] <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><… |
| 3 | `q40d417892141:Earnings:chunk-1` | 0.023299999999999998 |  | The Company's return on equity (ROE) was 21.8% for the trailing twelve months ended December 31, 2023, and homebuilding… |
| 4 | `q40d417892141:Earnings:chunk-4` | 0.0222 |  | •Consolidated revenues of approximately $36.0 billion to $37.3 billion •Homes closed by homebuilding operations of 87,0… |
| 5 | `q40d417892141:Earnings:chunk-29` | 0.0221 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q40d417892141`)._

### ex-dev-chunk-only-q504aef305d62

- **example_id**: `dev:chunk-only:q504aef305d62`
- **state**: `completed`
- **query**: How did management describe the performance of the China market in Q4 2023?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.7714160225925204 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q504aef305d62:Earnings:chunk-15` | 1.2282000000000002 | 2.0 | Thank you for the question. Let me start with the answer here. Our brand in China is known as [ Shing Baka ] and it upl… |
| 2 | `q504aef305d62:Earnings:chunk-7` | 1.1894 | 2.0 | Thank you, Laxman, and good morning, everyone. I'm very pleased to discuss our strong Q4 and full fiscal year 2023 perf… |
| 3 | `q504aef305d62:Earnings:chunk-5` | 1.1726999999999999 | 2.0 | Thank you, Tiffany. Good morning, everyone. Welcome to Starbucks' Fourth Quarter and Fiscal Year 2023 Earnings Conferen… |
| 4 | `q504aef305d62:Earnings:chunk-13` | 0.1206 | 1.0 | I had a question about China, please, which I think we've heard the competitive environment there very intense. And I w… |
| 5 | `q504aef305d62:Earnings:chunk-21` | 0.0597 |  | I'll take the first question and hand over to Rachel for the second. On the first question, clearly, we're reading all … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q504aef305d62`)._

### ex-dev-chunk-only-q5bb4a350edd8

- **example_id**: `dev:chunk-only:q5bb4a350edd8`
- **state**: `completed`
- **query**: How has aircraft delivery volume trended across the last four quarters for the F 35 program?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5=0.4315846810586321 · skipped= · n_scored=98

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5bb4a350edd8:10-Q:chunk-5` | 0.8734 | 2.0 | Thanks, Maria. Good morning, everyone, and thank you for joining us on our fourth quarter and full year 2023 earnings c… |
| 2 | `q5bb4a350edd8:10-Q:chunk-7` | 0.6019 |  | Thanks, Jim, and good morning, everyone. Today, I will recap our fourth quarter and full year 2023 financial results an… |
| 3 | `q5bb4a350edd8:10-Q:chunk-13` | 0.5477 |  | Okay. Thanks, Myles. On the margins for F-35, what we're seeing in 2024 are lower favorable profit adjustments, and so … |
| 4 | `q5bb4a350edd8:10-Q:chunk-85` | 0.5001 | 1.0 | Yes. So we delivered 5 aircraft in 2023. We would expect that to triple, potentially quadruple, here in 2024. And so we… |
| 5 | `q5bb4a350edd8:10-Q:chunk-65` | 0.4602 | 1.0 | Yes. Let me start with that question first, and I'll come back to the F-35. Just on the 2025 margins going forward, yes… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q5bb4a350edd8`)._

### ex-dev-chunk-only-q7b219decf5da

- **example_id**: `dev:chunk-only:q7b219decf5da`
- **state**: `completed`
- **query**: What did Everest Group, Ltd.’s leadership say about Everest Group, Ltd.’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '10-Q', '8-K']`
- **yield**: original=`DEF14A` · effective=`DEF14A` · used=False
- **S2**: nDCG@5=0.4104889601851253 · skipped= · n_scored=138

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7b219decf5da:DEF14A:chunk-119` | 0.9315 | 2.0 | Mike, it's Mark. The first point that I would make is we have ample capital. There's a lot of capital that we have at o… |
| 2 | `q7b219decf5da:DEF14A:chunk-7` | 0.2372 | 1.0 | Thank you, Juan, and good morning, everyone. Everest had a strong finish to 2023. For the full year, Everest delivered … |
| 3 | `q7b219decf5da:DEF14A:chunk-5` | 0.0308 |  | Thank you, Matt. Good morning, everyone. Thank you for joining us. 2023 was the most profitable year in our history. We… |
| 4 | `q7b219decf5da:DEF14A:chunk-99` | 0.0097 |  | Makes sense. And then second question, just curious, capital management. I mean, obviously, you've had a lot of fantast… |
| 5 | `q7b219decf5da:DEF14A:chunk-83` | 0.0039 |  | Sure. Greg, this is Jim Williamson. Thanks for the question. Everest did have another excellent Jan 1 renewals. You've … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q7b219decf5da`)._

### ex-dev-chunk-only-q7ca4de540868

- **example_id**: `dev:chunk-only:q7ca4de540868`
- **state**: `completed`
- **query**: How does Hologic view the pace of innovation cycles in women's health diagnostics and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.2846438833857645 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ca4de540868:10-K:chunk-67` | 0.7358 | 1.0 | # Compensation Discussion and Analysis (cont.) ## 2023 Business Strategy & Performance Highlights (cont.) Finally, our … |
| 2 | `q7ca4de540868:10-K:chunk-8` | 0.6348 | 1.0 | # Performance Highlights (cont.) 15.6% WORLDWIDE ORGANIC REVENUE GROWTH EX. COVID-19 15.6% organic growth in constant c… |
| 3 | `q7ca4de540868:10-K:chunk-1` | 0.5818 | 1.0 | # Dear Fellow Stockholders: (cont.) Fiscal 2023 was a year in which Hologic lived up to its commitments. Once again, we… |
| 4 | `q7ca4de540868:10-K:chunk-9` | 0.33490000000000003 |  | # Performance Highlights (cont.) ## Financial highlights from fiscal 2023 - We drove top-line growth through a combinat… |
| 5 | `q7ca4de540868:10-K:chunk-32` | 0.2134 | 1.0 | # Our Board's Role and Responsibilities (cont.) ## A Champion for Women's Health We are committed to improving women's … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q7ca4de540868`)._

### ex-dev-chunk-only-q7ff47a7d2a20

- **example_id**: `dev:chunk-only:q7ff47a7d2a20`
- **state**: `completed`
- **query**: How does Consolidated Edison, Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.4443763561001209 · skipped= · n_scored=212

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ff47a7d2a20:10-K:chunk-195` | 0.925 | 2.0 | # APPENDIX D (cont.) ## ARTICLE 6. PURCHASE OF SHARES (cont.) (d) Promptly after the end of each Purchase Period, the A… |
| 2 | `q7ff47a7d2a20:10-K:chunk-103` | 0.6748000000000001 |  | # Long-Term Incentive Compensation (cont.) ## Equity Awards It is the Compensation Committee's practice in the first qu… |
| 3 | `q7ff47a7d2a20:10-K:chunk-66` | 0.4727 | 1.0 | # Stock Ownership Guidelines (cont.) ## Long Term Incentive Plan Non-employee Directors participate in the Company's lo… |
| 4 | `q7ff47a7d2a20:10-K:chunk-65` | 0.3988 | 1.0 | # DIRECTOR COMPENSATION (cont.) ## Elements of Compensation In 2023, non-employee Directors were eligible to receive th… |
| 5 | `q7ff47a7d2a20:10-K:chunk-144` | 0.3221 |  | # POTENTIAL PAYMENTS UPON TERMINATION OF EMPLOYMENT OR CHANGE IN CONTROL (cont.) ## Payments & Benefits to Mr. Noyes Mr… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q7ff47a7d2a20`)._

### ex-dev-chunk-only-q853c16a74704

- **example_id**: `dev:chunk-only:q853c16a74704`
- **state**: `completed`
- **query**: What did Tapestry’s management say about Tapestry’s margin outlook and initiatives to improve profitability?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.8869465982421278 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q853c16a74704:Earnings:chunk-57` | 1.3113000000000001 | 2.0 | Yes. You touched on so many important things. I understand when you look at it, and we love celebrating that we had the… |
| 2 | `q853c16a74704:Earnings:chunk-7` | 1.2764 | 2.0 | Thanks, Joanne, and good morning, everyone. Looking back at our results for the fiscal year, our commitment to discipli… |
| 3 | `q853c16a74704:Earnings:chunk-5` | 1.2709000000000001 | 1.0 | Good morning. Thank you, Christina, and welcome, everyone. As noted in our press release, our fourth quarter results ex… |
| 4 | `q853c16a74704:Earnings:chunk-41` | 1.2590000000000001 | 2.0 | Lorraine, we expect to build on the foundation that we've set over the last few years. And our focus is really to accel… |
| 5 | `q853c16a74704:Earnings:chunk-77` | 1.2551999999999999 | 2.0 | Yes. Let me hit the last part of that real quick because it is a quick one, right? So remember, we had some timing betw… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q853c16a74704`)._

### ex-dev-chunk-only-q90faabe2b483

- **example_id**: `dev:chunk-only:q90faabe2b483`
- **state**: `completed`
- **query**: What operational risks related to technology or IT systems has UDR, Inc. highlighted, and how are these managed?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=31

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q90faabe2b483:10-K:chunk-30` | 0.6374000000000001 | 1.0 | # FORWARD LOOKING STATEMENTS Certain statements made in this presentation may constitute "forward-looking statements." … |
| 2 | `q90faabe2b483:10-K:chunk-15` | 0.6221 | 1.0 | # FORWARD LOOKING STATEMENTS Certain statements made in this presentation may constitute "forward-looking statements. W… |
| 3 | `q90faabe2b483:10-K:chunk-5` | 0.0698 |  | # INNOVATION = REPEATABLE, CONSISTENT VALUE CREATION (cont.) ## Given a Cost of Capital to Grow >$20M NOI realized sinc… |
| 4 | `q90faabe2b483:10-K:chunk-7` | 0.0557 |  | # ACCRETIVE CAPITAL ALLOCATION Our wide variety of value creation drivers provides UDR the latitude to pivot toward inv… |
| 5 | `q90faabe2b483:10-K:chunk-3` | 0.0179 |  | # UDR AT A GLANCE - DIVERSIFIED PORTFOLIO COMPOSITION UDR is diversified across markets and price points to generate ro… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q90faabe2b483`)._

### ex-dev-chunk-only-q9ee9b517f484

- **example_id**: `dev:chunk-only:q9ee9b517f484`
- **state**: `completed`
- **query**: What feedback have investors provided regarding Valero Energy Corporation’s refining margin outlook?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.14606834984270645 · skipped= · n_scored=203

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9ee9b517f484:Earnings:chunk-110` | 0.613 |  | discounts on crude oils and other feedstocks, an increase in throughput volumes, and lower operating expenses (excludin… |
| 2 | `q9ee9b517f484:Earnings:chunk-129` | 0.0864 |  | Refining segment operating income decreased by $365 million in the third quarter of 2023 compared to the third quarter … |
| 3 | `q9ee9b517f484:Earnings:chunk-162` | 0.0571 |  | (d)“Other income, net” includes the following: ◦a net gain of $11 million in the nine months ended September 30, 2023 r… |
| 4 | `q9ee9b517f484:Earnings:chunk-19` | 0.0444 | 1.0 | VALERO ENERGY CORPORATION CONDENSED NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Continued) California Energy Commission… |
| 5 | `q9ee9b517f484:Earnings:chunk-163` | 0.025 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:q9ee9b517f484`)._

### ex-dev-chunk-only-qa431f3f55a5e

- **example_id**: `dev:chunk-only:qa431f3f55a5e`
- **state**: `completed`
- **query**: How are scenario analyses conducted by EPAM Systems, Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.5087403079104241 · skipped= · n_scored=252

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa431f3f55a5e:10-K:chunk-17` | 0.3891 | 1.0 | Table of Contents Our revenues are highly dependent on a limited number of industries, and any decrease in demand for o… |
| 2 | `qa431f3f55a5e:10-K:chunk-11` | 0.22139999999999999 |  | Table of Contents Events in the regions where we operate have and could continue to pose security risks to our people, … |
| 3 | `qa431f3f55a5e:10-K:chunk-13` | 0.0789 | 1.0 | Table of Contents If we fail to integrate or manage acquired companies efficiently and effectively, or if acquisitions … |
| 4 | `qa431f3f55a5e:10-K:chunk-69` | 0.0718 |  | Table of Contents We have cash in several countries, including Ukraine and Belarus, where the banking sector remains su… |
| 5 | `qa431f3f55a5e:10-K:chunk-23` | 0.06470000000000001 |  | Table of Contents Undetected software design defects, errors or failures may result in loss of business or in liabiliti… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qa431f3f55a5e`)._

### ex-dev-chunk-only-qaf2d41946676

- **example_id**: `dev:chunk-only:qaf2d41946676`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Occidental Petroleum Corporation for oil price volatility risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.5087403079104241 · skipped= · n_scored=126

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qaf2d41946676:10-K:chunk-87` | 0.6765000000000001 | 1.0 | Yes. So when we think about capital allocation in the oil and gas segment, what you're trying to do is we're trying to … |
| 2 | `qaf2d41946676:10-K:chunk-5` | 0.1091 |  | Thank you, Jordan, and good afternoon, everyone. 2023 was a great year for us, thanks to the performance of all of our … |
| 3 | `qaf2d41946676:10-K:chunk-109` | 0.0821 | 1.0 | I think there's -- the projects there were pushed out a bit just like many other things because of supply chain issues … |
| 4 | `qaf2d41946676:10-K:chunk-37` | 0.0449 |  | So if you look at our -- what we've said we'll spend in oil and gas is $4.8 billion to $5 billion in 2024. That -- part… |
| 5 | `qaf2d41946676:10-K:chunk-47` | 0.036199999999999996 |  | Yes. So one of the main drivers for the relatively lower guidance for this year is an assumption on the spread for the … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qaf2d41946676`)._

### ex-dev-chunk-only-qb3a6bec7aedc

- **example_id**: `dev:chunk-only:qb3a6bec7aedc`
- **state**: `completed`
- **query**: What exposure to foreign exchange fluctuations did Citizens Financial Group, Inc. disclose and how is Citizens Financial Group, Inc. managing it?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.9125299483251055 · skipped= · n_scored=423

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb3a6bec7aedc:10-K:chunk-125` | 1.2419 | 2.0 | Capital Markets A key component of our capital markets activities is the underwriting and distribution of corporate cre… |
| 2 | `qb3a6bec7aedc:10-K:chunk-306` | 1.1944 | 2.0 | NOTE 14 - DERIVATIVES In the normal course of business, Citizens enters into derivative transactions to meet the financ… |
| 3 | `qb3a6bec7aedc:10-K:chunk-317` | 0.8305 | 2.0 | Derivatives not designated as hedging instruments The Company offers derivatives to customers in connection with their … |
| 4 | `qb3a6bec7aedc:10-K:chunk-129` | 0.7839 | 2.0 | Stressed VaR SVaR is an extension of VaR and utilizes a longer historical look-back horizon, fixed from January 3, 2005… |
| 5 | `qb3a6bec7aedc:10-K:chunk-111` | 0.7325 | 1.0 | Our principal non-market risks include credit, operational, regulatory, reputational, liquidity and strategic risks. We… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qb3a6bec7aedc`)._

### ex-dev-chunk-only-qb7d1dfae8271

- **example_id**: `dev:chunk-only:qb7d1dfae8271`
- **state**: `completed`
- **query**: What guidance was offered on International Flavors & Fragrances Inc.’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5=0.830419897363192 · skipped= · n_scored=304

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb7d1dfae8271:10-Q:chunk-4` | 1.0086 | 1.0 | •evaluating the profitability of whether to buy or make an ingredient; •sourcing from local countries with our own proc… |
| 2 | `qb7d1dfae8271:10-Q:chunk-22` | 0.7946 | 1.0 | Our performance may be adversely impacted if we are not successful in managing our inventory and/or working capital bal… |
| 3 | `qb7d1dfae8271:10-Q:chunk-57` | 0.7161 |  | These non-GAAP financial measures are intended to provide additional information regarding our underlying operating res… |
| 4 | `qb7d1dfae8271:10-Q:chunk-90` | 0.7051000000000001 | 1.0 | debt outstanding on the Consolidated Balance Sheets. Unamortized deferred financing costs relating to the revolving cre… |
| 5 | `qb7d1dfae8271:10-Q:chunk-3` | 0.6842 | 1.0 | Creative Application Through our global network of creative centers and application laboratories, we create or adapt th… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qb7d1dfae8271`)._

### ex-dev-chunk-only-qbcda53de470c

- **example_id**: `dev:chunk-only:qbcda53de470c`
- **state**: `completed`
- **query**: Which competitive advantages has Apple emphasized compared to peers?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-Q', '10-K', '8-K']`
- **yield**: original=`DEF14A` · effective=`DEF14A` · used=False
- **S2**: nDCG@5=0.360054614577234 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbcda53de470c:DEF14A:chunk-107` | 1.2528 |  | Sure. It's a number of things, Richard. It's the -- some things I can't talk about. It's Vision Pro. It's AI and ML. It… |
| 2 | `qbcda53de470c:DEF14A:chunk-5` | 1.2067 | 2.0 | Thank you, Suhasini. Good afternoon, everyone, and thanks for joining the call. Today, Apple is reporting revenue of $8… |
| 3 | `qbcda53de470c:DEF14A:chunk-71` | 1.1543999999999999 |  | It's really enabled us to build products that we could not build without doing it ourselves. And as you know, we like t… |
| 4 | `qbcda53de470c:DEF14A:chunk-7` | 1.0728 | 2.0 | Thank you, Tim, and good afternoon, everyone. Revenue for the September quarter was $89.5 billion, down less than 1% fr… |
| 5 | `qbcda53de470c:DEF14A:chunk-57` | 0.9647 |  | We had a really strong quarter across the border, I mean, because both geographically and from a product category stand… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qbcda53de470c`)._

### ex-dev-chunk-only-qd7ede96b88aa

- **example_id**: `dev:chunk-only:qd7ede96b88aa`
- **state**: `completed`
- **query**: What observations were made about TransDigm Group’s market share trends or competitive positioning in the aerospace components sector?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.3869772073910237 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd7ede96b88aa:Earnings:chunk-51` | 0.33559999999999995 | 1.0 | # Compensation Discussion and Analysis ("CD&A") (cont.) ## Introduction Our compensation program closely aligns NEO com… |
| 2 | `qd7ede96b88aa:Earnings:chunk-7` | 0.252 | 1.0 | # 2025 Annual Meeting of Shareholders (cont.) ## Composition of our Board Board Independence 80% 8 of our 10 Directors … |
| 3 | `qd7ede96b88aa:Earnings:chunk-8` | 0.2306 | 1.0 | # 2025 Annual Meeting of Shareholders (cont.) ## Composition of our Board (cont.) 31 Years of Growth and Improving Marg… |
| 4 | `qd7ede96b88aa:Earnings:chunk-59` | 0.0803 | 2.0 | # Summary of Key NEO Compensation Decisions and Actions in 2024 (cont.) ## 2024 Peer Group Ametek, Inc. Aptiv PLC* Dove… |
| 5 | `qd7ede96b88aa:Earnings:chunk-49` | 0.0489 |  | # Other Named Executive Officers (cont.) ## Joel B. Reiss Joel B. Reiss, 54, was appointed Co-COO in May 2023. Prior to… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qd7ede96b88aa`)._

### ex-dev-chunk-only-qddfea8300793

- **example_id**: `dev:chunk-only:qddfea8300793`
- **state**: `completed`
- **query**: How does Chesapeake Energy view the pace of technological advancements in drilling techniques and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.14606834984270645 · skipped= · n_scored=345

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qddfea8300793:10-K:chunk-23` | 0.2479 |  | Major Customers For the 2023 Successor Period, sales to Valero Energy Corporation and Shell Energy North America accoun… |
| 2 | `qddfea8300793:10-K:chunk-33` | 0.2143 |  | •any investment, acquisition, or disposition will not divert management resources from the operation of our business; a… |
| 3 | `qddfea8300793:10-K:chunk-30` | 0.1914 |  | Item 1A. Risk Factors There are numerous factors that affect our business and results of operations, many of which are … |
| 4 | `qddfea8300793:10-K:chunk-36` | 0.185 | 1.0 | Our development and exploratory drilling efforts and our well operations may not be profitable or achieve our targeted … |
| 5 | `qddfea8300793:10-K:chunk-32` | 0.1511 |  | Risks Related to Operating our Business Conservation measures and technological advances could reduce demand for natura… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qddfea8300793`)._

### ex-dev-chunk-only-qed0361d5a9ae

- **example_id**: `dev:chunk-only:qed0361d5a9ae`
- **state**: `completed`
- **query**: How does Apple currently project its growth rate based on the latest management commentary?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=83

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qed0361d5a9ae:Earnings:chunk-56` | 0.1486 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations This section and other pa… |
| 2 | `qed0361d5a9ae:Earnings:chunk-62` | 0.11359999999999999 |  | iPhone iPhone net sales decreased during the third quarter and first nine months of 2023 compared to the same periods i… |
| 3 | `qed0361d5a9ae:Earnings:chunk-59` | 0.0211 |  | Americas Americas net sales decreased during the third quarter and first nine months of 2023 compared to the same perio… |
| 4 | `qed0361d5a9ae:Earnings:chunk-4` | 0.0044 |  | ######Three Months Ended##########Nine Months Ended#### ####July 1, 2023######June 25, 2022####July 1, 2023######June 2… |
| 5 | `qed0361d5a9ae:Earnings:chunk-57` | 0.0036 |  | The Company repurchased $18.0 billion of its common stock and paid dividends and dividend equivalents of $3.8 billion d… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qed0361d5a9ae`)._

### ex-dev-chunk-only-qeeb1c1a41ae3

- **example_id**: `dev:chunk-only:qeeb1c1a41ae3`
- **state**: `completed`
- **query**: What dependency risks exist for DuPont de Nemours, Inc. due to concentration of revenue in a limited number of end-use industries such as automotive or electronics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.4104889601851253 · skipped= · n_scored=112

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeeb1c1a41ae3:10-K:chunk-43` | 0.7037 | 2.0 | # Compensation Discussion & Analysis ## Executive Summary We experienced significant volume pressure throughout 2023 as… |
| 2 | `qeeb1c1a41ae3:10-K:chunk-4` | 0.2418 | 1.0 | # Proxy Statement Summary # About DuPont We are a global innovation leader with technology-based materials and solution… |
| 3 | `qeeb1c1a41ae3:10-K:chunk-15` | 0.004 |  | # Table of Contents (cont.) ## Board's Role in the Oversight of Risk Management The Board is responsible for overseeing… |
| 4 | `qeeb1c1a41ae3:10-K:chunk-45` | 0.0027 |  | # Compensation Discussion & Analysis (cont.) ## STIP - Taking into consideration that business conditions were expected… |
| 5 | `qeeb1c1a41ae3:10-K:chunk-101` | 0.0014 |  | # NON-GAAP RECONCILIATION (cont.) ## Appendix A ## Compensation Performance Measures Discussed in the Compensation Disc… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qeeb1c1a41ae3`)._

### ex-dev-chunk-only-qf3b87e3d287f

- **example_id**: `dev:chunk-only:qf3b87e3d287f`
- **state**: `completed`
- **query**: How has Bio-Techne Corporation’s leverage (e.g., debt-to-equity) changed over time?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.4104889601851253 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf3b87e3d287f:10-K:chunk-8` | 1.167 | 2.0 | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td colspan="2">3/… |
| 2 | `qf3b87e3d287f:10-K:chunk-24` | 0.6699999999999999 | 1.0 | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td colspan="5">NI… |
| 3 | `qf3b87e3d287f:10-K:chunk-22` | 0.36060000000000003 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 4 | `qf3b87e3d287f:10-K:chunk-7` | 0.13219999999999998 |  | CONSOLIDATED CONDENSED BALANCE SHEETS (In thousands) (Unaudited) |
| 5 | `qf3b87e3d287f:10-K:chunk-0` | 0.041699999999999994 |  | Exhibit 99.1 BIO-TECHNE RELEASES THIRD QUARTER FISCAL 2024 RESULTS Minneapolis/May 1, 2024/ Bio-Techne Corporation (NAS… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qf3b87e3d287f`)._

### ex-dev-chunk-only-qf59bea60dc8d

- **example_id**: `dev:chunk-only:qf59bea60dc8d`
- **state**: `completed`
- **query**: How does Aon manage equity award burn rate or share pool availability?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-Q', '10-K', 'Earnings', '8-K']`
- **yield**: original=`DEF14A` · effective=`DEF14A` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=145

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf59bea60dc8d:DEF14A:chunk-137` | 0.5586 |  | Period##Total Number of Shares Purchased####Average Price Paid per Share (1)##Total Number of Shares Purchased as Part … |
| 2 | `qf59bea60dc8d:DEF14A:chunk-138` | 0.2705 |  | (1)Does not include commissions paid to repurchase shares. (2)The Repurchase Program was established in April 2012 with… |
| 3 | `qf59bea60dc8d:DEF14A:chunk-56` | 0.16899999999999998 |  | 10. Income Taxes The effective tax rate on Net income was 16.6% and 17.1% for the three and nine months ended September… |
| 4 | `qf59bea60dc8d:DEF14A:chunk-116` | 0.1422 |  | Acquisitions and Dispositions of Businesses During the first nine months of 2023, we completed two acquisitions. Cash c… |
| 5 | `qf59bea60dc8d:DEF14A:chunk-7` | 0.0983 |  | ####(Unaudited)#### (millions, except nominal value)####September 30, 2023####December 31, 2022 Assets######## Current … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:chunk-only:qf59bea60dc8d`)._

### ex-dev-q00e75b32eb34

- **example_id**: `dev:q00e75b32eb34`
- **state**: `completed`
- **query**: How has International Flavors & Fragrances Inc.’s ingredients segment profitability trended over recent periods?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.5755814336124626 · skipped= · n_scored=154

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q00e75b32eb34:chunk-137` | 0.2095 | 2.0 | Nourish Segment Adjusted Operating EBITDA Nourish Segment Adjusted Operating EBITDA decreased $414 million, or 42% on a… |
| 2 | `q00e75b32eb34:chunk-132` | 0.1854 |  | _______________________ (1)Currency neutral sales growth is calculated by translating current year invoiced sale amount… |
| 3 | `q00e75b32eb34:chunk-126` | 0.1668 | 1.0 | Research and Development (R&D) Expenses R&D expenses increased $12 million to $157 million (5.6% of sales) in the third… |
| 4 | `q00e75b32eb34:chunk-73` | 0.1519 | 1.0 | As of September 30, 2023, there was approximately $90 million of total unrecognized compensation cost related to non-ve… |
| 5 | `q00e75b32eb34:chunk-118` | 0.1437 | 2.0 | ITEM 2. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS. (UNLESS INDICATED OTHERW… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q00e75b32eb34`)._

### ex-dev-q01b84969979c

- **example_id**: `dev:q01b84969979c`
- **state**: `completed`
- **query**: How many markets were mentioned as now offering ad tier pricing for Disney Plus
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.7063662475919823 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['8-K', 'Earnings', '10-Q', 'DEF14A', '10-K']`
- **yield**: original=`8-K` · effective=`10-K` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=475

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q01b84969979c:chunk-11` | 0.9331 | 1.0 | (1)Based on Nielsen Media Research estimates as of September 2023. Estimates include traditional MVPD and the majority … |
| 2 | `q01b84969979c:chunk-90` | 0.1266 |  | Revenues The increase in subscription fees reflected increases of 11% from more subscribers, due to growth at Disney+ C… |
| 3 | `q01b84969979c:chunk-27` | 0.11 |  | TABLE OF CONTENTS We face risks related to changes in our business strategy or restructuring of our businesses, which h… |
| 4 | `q01b84969979c:chunk-154` | 0.0417 |  | Revenues Higher subscription fees reflected increases of 18% from subscriber growth and 9% from higher average rates du… |
| 5 | `q01b84969979c:chunk-95` | 0.0193 |  | (1)See discussion on page 66—DTC Product Descriptions, Key Definitions and Supplemental Information (2)Total may not eq… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q01b84969979c`)._

### ex-dev-q0346b2bc5a8b

- **example_id**: `dev:q0346b2bc5a8b`
- **state**: `completed`
- **query**: What investor views emerged on Packaging Corporation of America’s geographic expansion prospects within the packaging industry?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9216809842642141 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.8772153153380493 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0346b2bc5a8b:chunk-51` | 1.1448 | 1.0 | Yes, Mike, obviously, you don't know what the future is going to hold, but we've got a lot of optionality in what we're… |
| 2 | `q0346b2bc5a8b:chunk-111` | 0.6614 |  | I'll let you know when it happens. That's the beauty of having that firepower. We can not only continue to look at shar… |
| 3 | `q0346b2bc5a8b:chunk-49` | 0.391 |  | Got it. And last question is before turning it over. Can you help us just think about what's next for PKG from a growth… |
| 4 | `q0346b2bc5a8b:chunk-87` | 0.382 | 1.0 | I mean we're probably spending close to $250 million just in the box plants alone this year. And that's all of the 30 s… |
| 5 | `q0346b2bc5a8b:chunk-67` | 0.1055 |  | Gabe, the majority of our increase in volume came from our existing customers. As we've said many, many times, I mean, … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q0346b2bc5a8b`)._

### ex-dev-q03a704904653

- **example_id**: `dev:q03a704904653`
- **state**: `completed`
- **query**: What did IBM’s leadership say about IBM’s dividend policy or share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.5831428296492145 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['DEF14A', 'Earnings', '8-K', '10-K', '10-Q']`
- **yield**: original=`DEF14A` · effective=`10-Q` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=305

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q03a704904653:chunk-250` | 1.2119 | 2.0 | Management Discussion – (continued) Actual shares outstanding at September 30, 2023 were 913.1 million. The weighted-av… |
| 2 | `q03a704904653:chunk-274` | 1.2076 | 2.0 | *Includes immaterial cash flows from discontinued operations. **Recast to conform to current-year presentation. In the … |
| 3 | `q03a704904653:chunk-268` | 1.1552 | 2.0 | Management Discussion – (continued) We are driving productivity initiatives which range from simplifying our applicatio… |
| 4 | `q03a704904653:chunk-162` | 1.0412 | 2.0 | *Amounts reported net of refunds. During the nine months ended September 30, 2023 and 2022, the company contributed $18… |
| 5 | `q03a704904653:chunk-298` | 1.0307 | 2.0 | *On October 30, 2018, the Board of Directors authorized $4.0 billion in funds for use in the company’s common stock rep… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q03a704904653`)._

### ex-dev-q044bb2c8810c

- **example_id**: `dev:q044bb2c8810c`
- **state**: `completed`
- **query**: What investor views emerged on EQT Corporation’s geographic expansion prospects within the U.S. natural gas markets?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.5937688939938958 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['8-K', '10-Q', '10-K', 'DEF14A', 'Earnings']`
- **yield**: original=`8-K` · effective=`10-K` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=108

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q044bb2c8810c:chunk-53` | 0.5257999999999999 | 1.0 | EQT CORPORATION AND SUBSIDIARIES Notes to the Condensed Consolidated Financial Statements (Unaudited) Because the Mount… |
| 2 | `q044bb2c8810c:chunk-96` | 0.18910000000000002 |  | We are exposed to the risk of nonperformance by credit customers on physical sales of natural gas, NGLs and oil. Revenu… |
| 3 | `q044bb2c8810c:chunk-63` | 0.11829999999999999 |  | EQT CORPORATION AND SUBSIDIARIES Management's Discussion and Analysis of Financial Condition and Results of Operations … |
| 4 | `q044bb2c8810c:chunk-73` | 0.0934 |  | Sales of natural gas, NGLs and oil. Sales of natural gas, NGLs and oil decreased for the three months ended September 3… |
| 5 | `q044bb2c8810c:chunk-29` | 0.085 |  | Henry Hub Cash Bonus. The Consolidated GGA (defined in Note 8) executed in connection with the Equitrans Share Exchange… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q044bb2c8810c`)._

### ex-dev-q05bfc5cb3e17

- **example_id**: `dev:q05bfc5cb3e17`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Northern Trust Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.9125299483251055 · skipped= · n_scored=315

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q05bfc5cb3e17:chunk-198` | 1.2714 | 2.0 | Notes to Consolidated Financial Statements (unaudited) (continued) The Provision for Credit Losses, excluding the relea… |
| 2 | `q05bfc5cb3e17:chunk-188` | 1.097 | 2.0 | Note: Period-end balances reflect all pay downs and charge-offs during the year. There were no residential real estate … |
| 3 | `q05bfc5cb3e17:chunk-204` | 1.0507 | 2.0 | Allowance Related to Credit Exposure Evaluated on a Collective Basis. Expected credit losses are measured on a collecti… |
| 4 | `q05bfc5cb3e17:chunk-87` | 0.8593999999999999 | 2.0 | CAPITAL RATIOS The capital ratios of Northern Trust Corporation and its principal subsidiary, The Northern Trust Compan… |
| 5 | `q05bfc5cb3e17:chunk-78` | 0.8027 | 1.0 | Nonaccrual assets of $69.1 million as of September 30, 2023 increased $23.2 million or 51% from December 31, 2022, prim… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q05bfc5cb3e17`)._

### ex-dev-q09b8cfa51b60

- **example_id**: `dev:q09b8cfa51b60`
- **state**: `completed`
- **query**: How does CBRE Group, Inc. view the pace of technological innovation in real estate services and its effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=141

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q09b8cfa51b60:chunk-124` | 0.4813 | 1.0 | Cautionary Note on Forward-Looking Statements This Quarterly Report contains forward-looking statements within the mean… |
| 2 | `q09b8cfa51b60:chunk-125` | 0.4743 |  | •the ability of our investment management business to maintain and grow assets under management and achieve desired inv… |
| 3 | `q09b8cfa51b60:chunk-78` | 0.0407 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations Management’s Discussion a… |
| 4 | `q09b8cfa51b60:chunk-80` | 0.013000000000000001 |  | Compensation is our largest expense and our capital markets and leasing professionals generally are paid on a commissio… |
| 5 | `q09b8cfa51b60:chunk-90` | 0.0022 |  | Three Months Ended September 30, 2023 Compared to the Three Months Ended September 30, 2022 We reported consolidated ne… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q09b8cfa51b60`)._

### ex-dev-q0b8d55d58be2

- **example_id**: `dev:q0b8d55d58be2`
- **state**: `completed`
- **query**: What questions were asked about Chubb Limited’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9506817003345661 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=370

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0b8d55d58be2:chunk-254` | 0.1812 |  | Catastrophe losses through September 30, 2023 and 2022, were primarily from the following events: •2023: U.S. flooding,… |
| 2 | `q0b8d55d58be2:chunk-239` | 0.087 |  | (1)Commercial multiple peril represents retail package business (property and general liability). The increase in conso… |
| 3 | `q0b8d55d58be2:chunk-290` | 0.0007999999999999999 |  | We provide financial measures, including net premiums written, net premiums earned, and underwriting income on a consta… |
| 4 | `q0b8d55d58be2:chunk-261` | 0.0004 |  | Overseas General Insurance Overseas General Insurance segment comprises Chubb International and Chubb Global Markets (C… |
| 5 | `q0b8d55d58be2:chunk-12` | 0.0003 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Unaudited) Chubb Limited and Subsidiaries 1. General and significant accoun… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q0b8d55d58be2`)._

### ex-dev-q0d51e9ef12aa

- **example_id**: `dev:q0d51e9ef12aa`
- **state**: `completed`
- **query**: How did leadership measure the installed base of RTX PCs and relate it to AI‑application adoption?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5509858876386381 · gold=['8-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`8-K` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=113

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0d51e9ef12aa:chunk-6` | 1.1038000000000001 | 2.0 | # Business Highlights - NVIDIA accelerated computing reached the tipping point, with Data Center revenue more than trip… |
| 2 | `q0d51e9ef12aa:chunk-52` | 0.0007999999999999999 |  | # Compensation, Benefits, and Well-Being (cont.) ## Product Value Chain We seek to promote human rights throughout our … |
| 3 | `q0d51e9ef12aa:chunk-49` | 0.0003 |  | # Corporate Sustainability INVIDIA invents computing technologies that improve lives and address global challenges. Our… |
| 4 | `q0d51e9ef12aa:chunk-12` | 0.0002 |  | # Nominee Skills, Competencies, and Attributes (cont.) ## Financial Performance and Link to Executive Pay As described … |
| 5 | `q0d51e9ef12aa:chunk-24` | 0.0002 |  | # Proposal 1-Election of Directors (cont.) ## Director Qualifications and Nomination of Directors (cont.) Our Board bel… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q0d51e9ef12aa`)._

### ex-dev-q0e5327ae1aff

- **example_id**: `dev:q0e5327ae1aff`
- **state**: `completed`
- **query**: What concerns have institutional investors raised regarding regulatory risk?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5=0.38685280723454163 · gold=['Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **yield**: original=`DEF14A` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.38685280723454163 · skipped= · n_scored=104

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0e5327ae1aff:chunk-15` | 0.1963 |  | Sure, Harshita. Let me take both of those questions. First, on Reg II, let me just kind of share with everybody that fr… |
| 2 | `q0e5327ae1aff:chunk-41` | 0.1515 | 1.0 | Dan, you just touched on some of the key things to watch out for. But this is no different than us monitoring fiscal mo… |
| 3 | `q0e5327ae1aff:chunk-19` | 0.1092 |  | So 2 questions. One, to what degree are conversions of new wins contributing to fiscal year '24 guidance? And secondly,… |
| 4 | `q0e5327ae1aff:chunk-5` | 0.0445 |  | Thank you, Devin. Good morning, everyone. Here's the headline. We closed out 2023 with another quarter of strong earnin… |
| 5 | `q0e5327ae1aff:chunk-7` | 0.042 |  | Thanks, Michael. Turning now to Page 3, which shows our financial performance for the fourth quarter on a currency-neut… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q0e5327ae1aff`)._

### ex-dev-q0faf9d780cdc

- **example_id**: `dev:q0faf9d780cdc`
- **state**: `completed`
- **query**: How did aeronautics sustainment hours compare with prior year levels?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9639404333166532 · gold=['10-Q', '10-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0faf9d780cdc:chunk-43` | 1.047 | 2.0 | (a)Effective January 1, 2023, we reclassified intangible asset amortization expense out of the business segment operati… |
| 2 | `q0faf9d780cdc:chunk-40` | 1.0350000000000001 | 1.0 | Substantially all of our contracts are accounted for using the percentage-of-completion cost-to-cost method. Under the … |
| 3 | `q0faf9d780cdc:chunk-0` | 0.2204 |  | PART I ITEM 1. Business General We are a global security and aerospace company principally engaged in the research, des… |
| 4 | `q0faf9d780cdc:chunk-55` | 0.07819999999999999 |  | production. These increases were partially offset by lower net sales of $400 million on the F-35 program due to lower v… |
| 5 | `q0faf9d780cdc:chunk-52` | 0.0732 |  | schedule and cost aspects of the contract, which decreases the estimated total costs to complete the contract. Converse… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q0faf9d780cdc`)._

### ex-dev-q11ef281af9cd

- **example_id**: `dev:q11ef281af9cd`
- **state**: `completed`
- **query**: How does United Rentals select the peer group for benchmarking executive pay?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9840990003623115 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **yield**: original=`DEF14A` · effective=`DEF14A` · used=False
- **S2**: nDCG@5=0.6309297535714575 · skipped= · n_scored=223

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q11ef281af9cd:chunk-17` | 0.0068 |  | One of the reasons some of our customers find it more attractive to rent equipment than own that equipment is the need … |
| 2 | `q11ef281af9cd:chunk-199` | 0.0014 | 1.0 | PART III Item 10. Directors, Executive Officers and Corporate Governance The information required by this Item is incor… |
| 3 | `q11ef281af9cd:chunk-205` | 0.0012000000000000001 |  | Exhibit Number####Description of Exhibit 10##(c)##United Rentals, Inc. Deferred Compensation Plan, as amended and resta… |
| 4 | `q11ef281af9cd:chunk-207` | 0.0012000000000000001 |  | Exhibit Number####Description of Exhibit 10##(s)##Form of Restricted Stock Unit Agreement (Performance Based) for Micha… |
| 5 | `q11ef281af9cd:chunk-31` | 0.001 |  | Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations (dollars in millions, exc… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q11ef281af9cd`)._

### ex-dev-q140516364bb4

- **example_id**: `dev:q140516364bb4`
- **state**: `completed`
- **query**: What investor views emerged on Principal Financial Group’s international expansion prospects?
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.5292991962953502 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['8-K', 'DEF14A', 'Earnings', '10-Q', '10-K']`
- **yield**: original=`8-K` · effective=`10-Q` · used=True
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=103

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q140516364bb4:chunk-1` | 0.6873 | 1.0 | # From our CEO (cont.) ## Evolving our asset management business In 2023, we integrated our global capabilities across … |
| 2 | `q140516364bb4:chunk-8` | 0.30269999999999997 |  | # Proxy Summary (cont.) ## Corporate Snapshot Full year 2023 net income attributable to Principal Financial Group, Inc.… |
| 3 | `q140516364bb4:chunk-3` | 0.10880000000000001 |  | # From our CEO (cont.) ## Achieving strong results We delivered strong results in 2023, ending the year with momentum a… |
| 4 | `q140516364bb4:chunk-51` | 0.09230000000000001 |  | # Summary of Our Compensation Elements: (cont.) ## Individual Performance Modifier The Individual Performance Modifier … |
| 5 | `q140516364bb4:chunk-14` | 0.0771 |  | # Proposal One-Election of Directors (cont.) ## Alfredo Rivera Age: 62 Director Since: 2020 Committees: Audit and Human… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q140516364bb4`)._

### ex-dev-q1463bdfd6910

- **example_id**: `dev:q1463bdfd6910`
- **state**: `completed`
- **query**: How has Equifax’s Workforce Solutions segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.521616681216879 · skipped= · n_scored=282

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1463bdfd6910:chunk-43` | 1.0516 | 1.0 | Revenue for 2023 increased by 3% compared to 2022, due to revenue growth in International and USIS. International reven… |
| 2 | `q1463bdfd6910:chunk-16` | 0.5857 | 2.0 | all. Market acceptance of cloud-based offerings is affected by a variety of factors, including information security, re… |
| 3 | `q1463bdfd6910:chunk-242` | 0.4332 | 1.0 | ########Twelve Months Ended December 31,#### Operating revenue:####2023####2022####2021 ########(In millions)#### Workf… |
| 4 | `q1463bdfd6910:chunk-38` | 0.2071 | 1.0 | Segment and Geographic Information Segments. The Workforce Solutions segment consists of the Verification Services and … |
| 5 | `q1463bdfd6910:chunk-118` | 0.1339 | 1.0 | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS 1. SUMMARY OF SIGNIFICANT ACCOUNTING POLICIES As used herein, the terms Equi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q1463bdfd6910`)._

### ex-dev-q1ab49a3f086f

- **example_id**: `dev:q1ab49a3f086f`
- **state**: `completed`
- **query**: What outlook was given for Welltower Inc.’s free cash flow generation over the next year?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7426242736819336 · gold=['8-K', 'Earnings', '10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`8-K` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=346

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1ab49a3f086f:chunk-68` | 0.37420000000000003 | 1.0 | Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations housing properties genera… |
| 2 | `q1ab49a3f086f:chunk-44` | 0.0613 |  | Welltower is the initial member and majority owner of Welltower OP, with an approximate ownership interest of 99.765% a… |
| 3 | `q1ab49a3f086f:chunk-109` | 0.0093 |  | (1) See Non-GAAP Financial Measures below. Rental income has increased primarily due to acquisitions and annual rent in… |
| 4 | `q1ab49a3f086f:chunk-41` | 0.0087 |  | and the necessary provider agreements or contracts. We have experienced such delays in obtaining necessary licensing fo… |
| 5 | `q1ab49a3f086f:chunk-0` | 0.0037 |  | PART I Item 1. Business General Welltower Inc. (NYSE:WELL), an S&P 500 company headquartered in Toledo, Ohio, is drivin… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q1ab49a3f086f`)._

### ex-dev-q1cfcd01ac3a1

- **example_id**: `dev:q1cfcd01ac3a1`
- **state**: `completed`
- **query**: How does GE HealthCare Technologies manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7118306928082477 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **yield**: original=`10-K` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=26

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1cfcd01ac3a1:chunk-6` | 0.21239999999999998 | 1.0 | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3"></td></tr><… |
| 2 | `q1cfcd01ac3a1:chunk-17` | 0.0535 |  | [Chunk Index 18] <table><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="3">(1)</td><td … |
| 3 | `q1cfcd01ac3a1:chunk-14` | 0.0443 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="3">(1)</td><td colspan="3">Consi… |
| 4 | `q1cfcd01ac3a1:chunk-21` | 0.030699999999999998 |  | [Chunk Index 22] <table><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="3">(1)</td><td … |
| 5 | `q1cfcd01ac3a1:chunk-4` | 0.020399999999999998 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="6">Co… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q1cfcd01ac3a1`)._

### ex-dev-q1ded233d05aa

- **example_id**: `dev:q1ded233d05aa`
- **state**: `completed`
- **query**: What questions were asked about IDEXX Laboratories’ customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.47054637065131494 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1ded233d05aa:chunk-27` | 0.16570000000000001 | 1.0 | Yes. Just some follow-up commentary on the inVue launch. Customers, I think, very excited to learn more about that, as … |
| 2 | `q1ded233d05aa:chunk-53` | 0.08710000000000001 | 2.0 | Okay. Great. That was very helpful. And then just sort of a long second question, more clarification. So it seems like … |
| 3 | `q1ded233d05aa:chunk-41` | 0.08420000000000001 | 1.0 | Yes. So with respect to the point-of-care platform launches, we have a very well-defined tried and true method of devel… |
| 4 | `q1ded233d05aa:chunk-3` | 0.0707 |  | Good morning, everyone. I'm pleased to take you through our fourth quarter and full year 2023 results and to provide an… |
| 5 | `q1ded233d05aa:chunk-35` | 0.0672 |  | Yes. So let me talk a little bit about inVue and some of the key opinion leader feedback. We've had a number of key opi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q1ded233d05aa`)._

### ex-dev-q1f722f19a821

- **example_id**: `dev:q1f722f19a821`
- **state**: `completed`
- **query**: What answers were given about progress on Clover Vertica installations?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5=0.6309297535714575 · gold=['Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`Earnings` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1f722f19a821:chunk-5` | 1.2549000000000001 | 2.0 | Thank you, Tiffany. Good morning, everyone. Welcome to Starbucks' Fourth Quarter and Fiscal Year 2023 Earnings Conferen… |
| 2 | `q1f722f19a821:chunk-59` | 0.8051999999999999 | 2.0 | Brian, thank you for the question. Our CapEx will increase to around approximately $3 billion, and the majority of that… |
| 3 | `q1f722f19a821:chunk-65` | 0.0362 |  | I'm very pleased with the way that the reinvention plan is being implemented. A couple of highlights. I think the progr… |
| 4 | `q1f722f19a821:chunk-45` | 0.006999999999999999 |  | Let me start and then Rachel can add to it. One of the things that the team has worked on incredibly hard over the last… |
| 5 | `q1f722f19a821:chunk-53` | 0.0034000000000000002 |  | John, if I could take that on. Thank you for your question. We have more opportunities than what we have realized, but … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q1f722f19a821`)._

### ex-dev-q1ff3eed25e64

- **example_id**: `dev:q1ff3eed25e64`
- **state**: `completed`
- **query**: How did wage inflation trends affect labor costs in park operations
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6855052752796292 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.7383121460922933 · skipped= · n_scored=475

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1ff3eed25e64:chunk-31` | 1.1909 | 2.0 | TABLE OF CONTENTS productions and the pipeline for programming and theatrical releases, which could result in reduced r… |
| 2 | `q1ff3eed25e64:chunk-129` | 0.9905 | 2.0 | The increase in operating labor was due to inflation, higher volumes and increased costs for new guest offerings. Highe… |
| 3 | `q1ff3eed25e64:chunk-43` | 0.7027 |  | TABLE OF CONTENTS CONSOLIDATED RESULTS AND NON-SEGMENT ITEMS In fiscal 2023, the Company reorganized into three busines… |
| 4 | `q1ff3eed25e64:chunk-128` | 0.6608 | 1.0 | ($ in millions)####2023####2022##% Change Better (Worse) Operating labor##$##(7,550)##$##(6,577)##(15) % Infrastructure… |
| 5 | `q1ff3eed25e64:chunk-23` | 0.6179 |  | TABLE OF CONTENTS •Regulation of programming. The FCC regulates broadcast programming by, among other things, banning “… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q1ff3eed25e64`)._

### ex-dev-q2173e7c263c1

- **example_id**: `dev:q2173e7c263c1`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Realty Income Corporation for recessionary or downturn risks in the commercial real estate sector?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=171

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2173e7c263c1:chunk-98` | 0.48269999999999996 |  | experience increased costs of financing, make it difficult to refinance debt at attractive rates or at all, and may adv… |
| 2 | `q2173e7c263c1:chunk-97` | 0.1339 |  | Agreement and Plan of Merger On October 29, 2023, we entered into an Agreement and Plan of Merger (the “Merger Agreemen… |
| 3 | `q2173e7c263c1:chunk-115` | 0.1272 |  | For purposes of determining the same store rent property pool, we include all properties that were owned for the entire… |
| 4 | `q2173e7c263c1:chunk-90` | 0.07150000000000001 |  | Item 2: Management’s Discussion and Analysis of Financial Condition and Results of Operations FORWARD-LOOKING STATEMENT… |
| 5 | `q2173e7c263c1:chunk-66` | 0.019799999999999998 |  | The valuation of impaired assets is determined using valuation techniques including discounted cash flow analysis, anal… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q2173e7c263c1`)._

### ex-dev-q238a8429d152

- **example_id**: `dev:q238a8429d152`
- **state**: `completed`
- **query**: How does Dominion Energy view the pace of innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.4166158115319974 · skipped= · n_scored=209

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q238a8429d152:chunk-4` | 0.7037 | 1.0 | # Dominion Energy R Dominion Energy, headquartered in Richmond, Virginia, is one of the nation's largest producers and … |
| 2 | `q238a8429d152:chunk-50` | 0.4039 | 1.0 | # Sustainability and Corporate Responsibility Committee (cont.) ## Oversight of Sustainability and Corporate Responsibi… |
| 3 | `q238a8429d152:chunk-160` | 0.3014 |  | # Your Board of Directors recommends that you vote AGAINST this item. (cont.) ## Your Board of Directors recommends tha… |
| 4 | `q238a8429d152:chunk-43` | 0.2912 | 1.0 | # Compensation and Talent Development Committee (cont.) ## ROLE & RESPONSIBILITIES (cont.) # Sustainability and Corpora… |
| 5 | `q238a8429d152:chunk-28` | 0.17729999999999999 |  | # Kristin G. Lovejoy (cont.) ## Qualifications, Attributes and Skills Ms. Lovejoy is a recognized thought leader in the… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q238a8429d152`)._

### ex-dev-q2451f8377cf4

- **example_id**: `dev:q2451f8377cf4`
- **state**: `completed`
- **query**: What dependency risks exist for Pool Corporation due to concentration of revenue in specific geographic regions or major pool supply distributors?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.9260446319296772 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2451f8377cf4:chunk-5` | 1.2015 | 2.0 | Thank you, Melanie, and good morning to everyone on the call. For the full year 2023, we generated over $5.5 billion in… |
| 2 | `q2451f8377cf4:chunk-121` | 0.7266 | 2.0 | Yes. I think you really -- you have to go deeper than just seasonal and year-round. Garik, I think you got to look at s… |
| 3 | `q2451f8377cf4:chunk-7` | 0.622 | 1.0 | Thank you, Pete. Good morning, everyone. I'll begin our fourth quarter results, move into how we finished out 2023 and … |
| 4 | `q2451f8377cf4:chunk-89` | 0.23979999999999999 |  | Sure. Now just keep in mind that that's the smallest part of our business. So the beginning of the year is always show … |
| 5 | `q2451f8377cf4:chunk-21` | 0.17420000000000002 |  | Yes. Thanks for the question, Ryan. As we were trying to put together our guidance for the year, obviously, the beginni… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q2451f8377cf4`)._

### ex-dev-q24d0f908cfe3

- **example_id**: `dev:q24d0f908cfe3`
- **state**: `completed`
- **query**: What guidance was offered on Fox Corporation’s advertising revenue growth targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9278143341459562 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.5706417189553201 · skipped= · n_scored=111

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q24d0f908cfe3:chunk-7` | 0.6418999999999999 |  | # Board Nominees (cont.) ## Fiscal 2023 Business Highlights (cont.) - In fiscal 2023, Tubi delivered record revenues, w… |
| 2 | `q24d0f908cfe3:chunk-53` | 0.46709999999999996 |  | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Fiscal 2023 Business and Management Review (cont.) - FOX Entertainmen… |
| 3 | `q24d0f908cfe3:chunk-62` | 0.4621 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS <table><tr><th>Qualitative Performance Factor</th><th>Fiscal 2023 Achievements</… |
| 4 | `q24d0f908cfe3:chunk-54` | 0.44689999999999996 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Fiscal 2023 Business and Management Review (cont.) offerings to suppl… |
| 5 | `q24d0f908cfe3:chunk-6` | 0.3931 |  | # Board Nominees (cont.) ## Fiscal 2023 Business Highlights (cont.) all-time record as the most-watched program in U.S.… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q24d0f908cfe3`)._

### ex-dev-q25119b32a2f9

- **example_id**: `dev:q25119b32a2f9`
- **state**: `completed`
- **query**: What performance metrics does Snap-on Incorporated use to establish annual cash incentives or bonuses?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9882048111454694 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
- **yield**: original=`DEF14A` · effective=`DEF14A` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=21

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q25119b32a2f9:chunk-3` | 0.0212 | 1.0 | References in this release to “organic sales” refer to sales from continuing operations calculated in accordance with g… |
| 2 | `q25119b32a2f9:chunk-0` | 0.0088 |  | Exhibit 99 Snap-on Announces Third Quarter 2023 Results Sales of $1,159.3 million up 5.2% from Q3 2022, organic sales u… |
| 3 | `q25119b32a2f9:chunk-1` | 0.0053 |  | “Achieved in a period of variability, we believe our performance confirms the resilience of our markets and illustrates… |
| 4 | `q25119b32a2f9:chunk-14` | 0.0032 |  | <hr />Non-GAAP Supplemental Data The following non-GAAP supplemental data is presented for informational purposes to pr… |
| 5 | `q25119b32a2f9:chunk-5` | 0.0021 |  | <table> <tr> <td colspan="16">SNAP-ON INCORPORATED Condensed Consolidated Statements of Earnings (Amounts in millions, … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q25119b32a2f9`)._

### ex-dev-q27a01443f529

- **example_id**: `dev:q27a01443f529`
- **state**: `completed`
- **query**: What investor views emerged on Fox Corporation’s international or geographic expansion prospects?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.7204246268326864 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['8-K', 'DEF14A', 'Earnings', '10-Q', '10-K']`
- **yield**: original=`8-K` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=317

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q27a01443f529:chunk-16` | 0.5730999999999999 |  | Entertainment develops and produces unscripted and alternative programming primarily for the FOX Network, including The… |
| 2 | `q27a01443f529:chunk-3` | 0.30269999999999997 |  | its content library through the premiere of over 140 new original titles and the launch of over 60 sports, entertainmen… |
| 3 | `q27a01443f529:chunk-27` | 0.1127 |  | ITEM 1A. RISK FACTORS Prospective investors should consider carefully the risk factors set forth below before making an… |
| 4 | `q27a01443f529:chunk-18` | 0.065 |  | obligation to commit capital towards this opportunity unless and until it exercises the option. In addition, Flutter ca… |
| 5 | `q27a01443f529:chunk-36` | 0.0341 |  | be owned by a corporation if more than 25% of its stock is owned or voted by non-U.S. persons, their representatives, o… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q27a01443f529`)._

### ex-dev-q28b06421804c

- **example_id**: `dev:q28b06421804c`
- **state**: `completed`
- **query**: How did Bio-Techne’s executives discuss plans for new product development or expansion for Bio-Techne?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7189324940540128 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
- **yield**: original=`DEF14A` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.6092364968256234 · skipped= · n_scored=132

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q28b06421804c:chunk-94` | 1.0208 | 1.0 | ITEM 2. MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following management … |
| 2 | `q28b06421804c:chunk-48` | 0.8455999999999999 | 2.0 | Fiscal year 2024 Acquisitions Lunaphore Technologies SA. On July 7, 2023, the Company acquired all of the ownership int… |
| 3 | `q28b06421804c:chunk-95` | 0.7902 | 2.0 | RECENT ACQUISITIONS A key component of the Company's strategy is to augment internal growth at existing businesses with… |
| 4 | `q28b06421804c:chunk-9` | 0.49979999999999997 |  | NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS Bio-Techne Corporation and Subsidiaries (unaudited) Note 1. Basis … |
| 5 | `q28b06421804c:chunk-113` | 0.15969999999999998 |  | FORWARD LOOKING INFORMATION AND CAUTIONARY STATEMENTS This quarterly report contains forward-looking statements within … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q28b06421804c`)._

### ex-dev-q29a452be41cd

- **example_id**: `dev:q29a452be41cd`
- **state**: `completed`
- **query**: How has Fox Corporation’s cable network programming segment profitability trended over recent periods?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7693267077702551 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.8687949224876581 · skipped= · n_scored=107

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q29a452be41cd:chunk-74` | 1.2059 | 2.0 | For the three months ended March 31, 2024 and 2023 Revenues at the Cable Network Programming segment decreased $98 mill… |
| 2 | `q29a452be41cd:chunk-75` | 1.2045000000000001 | 2.0 | For the nine months ended March 31, 2024 and 2023 Revenues at the Cable Network Programming segment decreased $116 mill… |
| 3 | `q29a452be41cd:chunk-39` | 1.1736 | 2.0 | ######For the three months ended March 31,############For the nine months ended March 31,#### ####2024######2023######2… |
| 4 | `q29a452be41cd:chunk-71` | 1.1129 | 2.0 | ##########For the three months ended March 31,####################For the nine months ended March 31,########## ####202… |
| 5 | `q29a452be41cd:chunk-77` | 1.1122999999999998 |  | For the three months ended March 31, 2024 and 2023 Revenues at the Television segment decreased $537 million or 22% for… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q29a452be41cd`)._

### ex-dev-q29d3cb8df822

- **example_id**: `dev:q29d3cb8df822`
- **state**: `completed`
- **query**: How are investors interpreting guidance on SLB’s customer engagement metrics within its oilfield services operations?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9323478402140176 · gold=['Earnings', 'DEF14A', '8-K', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.6934264036172708 · skipped= · n_scored=47

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q29d3cb8df822:chunk-5` | 0.7337 |  | On a year-to-date basis, the Core businesscomprising Reservoir Performance, Well Construction, and Production Systems… |
| 2 | `q29d3cb8df822:chunk-19` | 0.6605 | 1.0 | This project includes the provision of CO2 removal membranes from natural gas, commissioning, and field service, with f… |
| 3 | `q29d3cb8df822:chunk-20` | 0.6585 | 1.0 | Digital operations are gaining in maturity, transforming the way operators develop and utilize assets. From automation … |
| 4 | `q29d3cb8df822:chunk-16` | 0.5293 |  | n/m = not meaningful Production Systems revenue of $2.37 billion increased 2% sequentially driven by strong sales of co… |
| 5 | `q29d3cb8df822:chunk-4` | 0.2983 |  | n/m = not meaningful International Markets Driving Profitable Growth SLB CEO Olivier Le Peuch commented, Our third-qua… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q29d3cb8df822`)._

### ex-dev-q2aae5e2ea500

- **example_id**: `dev:q2aae5e2ea500`
- **state**: `completed`
- **query**: How has Mondelez International’s snack foods segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-Q` · used=True
- **S2**: nDCG@5=0.9125299483251055 · skipped= · n_scored=178

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2aae5e2ea500:chunk-158` | 1.2366000000000001 | 2.0 | Three Months Ended September 30: Net revenues increased $350 million (14.0%), due to higher net pricing (6.8 pp), favor… |
| 2 | `q2aae5e2ea500:chunk-152` | 1.2167999999999999 | 2.0 | Three Months Ended September 30: Net revenues increased $87 million (5.1%), due to higher net pricing (8.6 pp) and favo… |
| 3 | `q2aae5e2ea500:chunk-155` | 1.2103 | 2.0 | Three Months Ended September 30: Net revenues increased $437 million (16.5%), due to higher net pricing (12.1 pp), favo… |
| 4 | `q2aae5e2ea500:chunk-149` | 1.1831 | 2.0 | Three Months Ended September 30: Net revenues increased $392 million (42.9%), due to higher net pricing (31.5 pp), the … |
| 5 | `q2aae5e2ea500:chunk-138` | 1.1745 | 1.0 | During the first nine months of 2023, we realized higher net pricing and favorable volume/mix, which was partially offs… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q2aae5e2ea500`)._

### ex-dev-q2c832749ca0b

- **example_id**: `dev:q2c832749ca0b`
- **state**: `completed`
- **query**: What dependency risks exist for Newmont Corporation due to concentration of revenue in a limited number of geographic regions or gold buyers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.8869465982421278 · skipped= · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2c832749ca0b:chunk-192` | 0.8667 | 2.0 | operations at Lihir and Wafi-Golpu in PNG are subject to political and regulatory risks and other uncertainties” and “—… |
| 2 | `q2c832749ca0b:chunk-144` | 0.6412 | 2.0 | Variations in the local currency exchange rates in relation to the USD at our foreign mining operations decreased Costs… |
| 3 | `q2c832749ca0b:chunk-102` | 0.4793 | 1.0 | ITEM 2. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS (dollars in millions, exc… |
| 4 | `q2c832749ca0b:chunk-141` | 0.4574 | 2.0 | Boddington, Australia. Gold production was generally in line with the prior year. Gold equivalent ounces – other metals… |
| 5 | `q2c832749ca0b:chunk-106` | 0.3788 | 2.0 | The decrease in Net income (loss) from continuing operations attributable to Newmont stockholders for the three months … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q2c832749ca0b`)._

### ex-dev-q2d8eb319367a

- **example_id**: `dev:q2d8eb319367a`
- **state**: `completed`
- **query**: How did UDR, Inc.’s leadership address potential risks or uncertainties in forward-looking statements for its multifamily property portfolio?
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.5873006284360539 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['8-K', '10-K', 'DEF14A', 'Earnings', '10-Q']`
- **yield**: original=`8-K` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.44638673509120536 · skipped= · n_scored=169

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2d8eb319367a:chunk-106` | 1.2614999999999998 | 1.0 | Item 2. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following discussion … |
| 2 | `q2d8eb319367a:chunk-107` | 1.2155 | 1.0 | ● risks that third parties who have an interest in or are otherwise involved in projects in which we have an interest, … |
| 3 | `q2d8eb319367a:chunk-141` | 1.1848 | 2.0 | PART II — OTHER INFORMATION Item 1. LEGAL PROCEEDINGS The Company is a party to various claims and routine litigation a… |
| 4 | `q2d8eb319367a:chunk-142` | 1.0835 | 1.0 | impacted by regional or local economic conditions or real estate market conditions, such conditions may have a greater … |
| 5 | `q2d8eb319367a:chunk-153` | 1.0808 | 1.0 | capital constrained, tighten their lending standards or become insolvent or if they experience excessive volumes of bor… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q2d8eb319367a`)._

### ex-dev-q2ec971ec73f9

- **example_id**: `dev:q2ec971ec73f9`
- **state**: `completed`
- **query**: What was United Rentals’ Cost of Goods Sold (COGS) in the most recent quarter?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7303575739184495 · gold=['8-K', '10-Q', '10-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`8-K` · used=True
- **S2**: nDCG@5=0.49479222926951455 · skipped= · n_scored=122

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2ec971ec73f9:chunk-93` | 0.3919 | 1.0 | General rentals. For the three months ended September 30, 2023, equipment rentals gross profit increased by $75, and eq… |
| 2 | `q2ec971ec73f9:chunk-83` | 0.1724 | 1.0 | increase in 2023 reflects charges associated with a restructuring program initiated following the closing of the Ahern … |
| 3 | `q2ec971ec73f9:chunk-95` | 0.1245 |  | For the three months ended September 30, 2023, total gross margin decreased 270 basis points from the same period in 20… |
| 4 | `q2ec971ec73f9:chunk-96` | 0.1002 | 1.0 | profit (gross profit for these revenue types represented 3 percent of total gross profit for the three months ended Sep… |
| 5 | `q2ec971ec73f9:chunk-87` | 0.07880000000000001 | 1.0 | revenues from the sale of used rental equipment. Sales of new equipment represent our revenues from the sale of new equ… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q2ec971ec73f9`)._

### ex-dev-q2fe5769567d7

- **example_id**: `dev:q2fe5769567d7`
- **state**: `completed`
- **query**: How does Align Technology manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.4759908431563516 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2fe5769567d7:chunk-66` | 0.7307 | 1.0 | As of September 30, 2023, we expect to recognize $202.1 million of total unamortized compensation costs, net of estimat… |
| 2 | `q2fe5769567d7:chunk-15` | 0.7281 | 2.0 | ####Common Stock#### Nine Months Ended September 30, 2022##Shares######Amount Balance as of December 31, 2021##78,710##… |
| 3 | `q2fe5769567d7:chunk-11` | 0.7091 | 1.0 | ####Common Stock#### Nine Months Ended September 30, 2023##Shares######Amount Balance as of December 31, 2022##77,267##… |
| 4 | `q2fe5769567d7:chunk-14` | 0.6893 | 1.0 | ####Common Stock#### Three Months Ended September 30, 2022##Shares######Amount Balance as of June 30, 2022##78,059####$… |
| 5 | `q2fe5769567d7:chunk-10` | 0.6547 | 1.0 | ####Common Stock#### Three Months Ended September 30, 2023##Shares######Amount Balance as of June 30, 2023##76,532####$… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q2fe5769567d7`)._

### ex-dev-q318eb902f451

- **example_id**: `dev:q318eb902f451`
- **state**: `completed`
- **query**: What questions were asked about Franklin Resources, Inc.’s client retention and engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9199642183398656 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.18154179253735267 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q318eb902f451:chunk-13` | 0.4351 |  | Great. Well, thanks, Bill. So, so far, the outflows even within Western, I think it's like 72% are focused on essential… |
| 2 | `q318eb902f451:chunk-41` | 0.3011 |  | Well, I was just going to say -- no, I think you hit it right, but just one addition. Without Western's outflows, I thi… |
| 3 | `q318eb902f451:chunk-17` | 0.215 |  | And Bill, I would add one thing you asked about institutional flows in general. We have really worked hard over the las… |
| 4 | `q318eb902f451:chunk-5` | 0.1182 |  | Thank you, Selene. Hello, everyone, and thank you for joining us today to discuss Franklin Templeton's fourth quarter a… |
| 5 | `q318eb902f451:chunk-15` | 0.10239999999999999 | 1.0 | Yes, yes. Okay. Thank you. Thanks, Jenny. Thanks, Bill. So maybe I think your question gets to a couple of things. Firs… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q318eb902f451`)._

### ex-dev-q31f6fd1f392c

- **example_id**: `dev:q31f6fd1f392c`
- **state**: `completed`
- **query**: What governance processes are in place for approving changes to Targa Resources Corp.’s compensation policies?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9979470946084208 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '8-K', '10-Q', 'Earnings']`
- **yield**: original=`DEF14A` · effective=`DEF14A` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=99

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q31f6fd1f392c:chunk-42` | 1.1983 | 2.0 | # Track Record of Growth Driving an Increasing Return of Capital to Shareholders (cont.) ## CEO Pay at a Glance Realiza… |
| 2 | `q31f6fd1f392c:chunk-27` | 1.1879 | 2.0 | # MEETINGS AND COMMITTEES OF DIRECTORS (cont.) ## Compensation Committee The members of our Compensation Committee are … |
| 3 | `q31f6fd1f392c:chunk-88` | 1.1763 | 2.0 | # PROPOSAL THREE ADVISORY VOTE ON EXECUTIVE COMPENSATION (cont.) ## Introduction (cont.) - annual base salary, which is… |
| 4 | `q31f6fd1f392c:chunk-44` | 1.1469 | 2.0 | # OUR DECISION MAKING PROCESS (cont.) ## Compensation Peer Group For purposes of setting compensation levels for 2023, … |
| 5 | `q31f6fd1f392c:chunk-41` | 0.9476 | 2.0 | # Track Record of Growth Driving an Increasing Return of Capital to Shareholders (cont.) ## Good Governance Foundation … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q31f6fd1f392c`)._

### ex-dev-q33197856c996

- **example_id**: `dev:q33197856c996`
- **state**: `completed`
- **query**: How has Trane Technologies’ quality metric for its HVAC system manufacturing process changed recently?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.742039158611126 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=297

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q33197856c996:chunk-4` | 0.0124 |  | Operations by Geographic Area Approximately 28% of our net revenues in 2023 were derived outside the U.S. and we sold p… |
| 2 | `q33197856c996:chunk-3` | 0.0106 |  | These products are sold primarily under our tradenames including Trane® and Thermo King®. Competitive Conditions Our pr… |
| 3 | `q33197856c996:chunk-0` | 0.01 |  | PART I Item 1. BUSINESS Overview Trane Technologies plc, a public limited company, incorporated in Ireland in 2009, and… |
| 4 | `q33197856c996:chunk-40` | 0.0036 |  | Item 7. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following Management’… |
| 5 | `q33197856c996:chunk-282` | 0.0034000000000000002 |  | NOTE 19. BUSINESS SEGMENT INFORMATION The Company operates under four regional operating segments designed to create de… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q33197856c996`)._

### ex-dev-q359aee1441c1

- **example_id**: `dev:q359aee1441c1`
- **state**: `completed`
- **query**: What guidance was offered regarding annual capital expenditure levels for park expansions and technology
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.5914218405396885 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`10-Q` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=475

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q359aee1441c1:chunk-215` | 1.1480000000000001 | 2.0 | Capital expenditures at Entertainment primarily reflect investments in technology and in facilities and equipment for e… |
| 2 | `q359aee1441c1:chunk-18` | 0.5781000000000001 |  | TABLE OF CONTENTS •Aulani, a Disney Resort & Spa in Hawaii ◦International: ▪Theme parks and resorts: •Disneyland Paris … |
| 3 | `q359aee1441c1:chunk-220` | 0.38120000000000004 |  | (1)Borrowings and reductions of borrowings are reported net. (2)The other activity is primarily due to the amortization… |
| 4 | `q359aee1441c1:chunk-213` | 0.3584 |  | TABLE OF CONTENTS The Company currently expects its fiscal 2024 spend on produced and licensed content to be approximat… |
| 5 | `q359aee1441c1:chunk-196` | 0.31849999999999995 |  | The increases in operating labor, cost of goods sold and distribution costs and other operating expenses were due to hi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q359aee1441c1`)._

### ex-dev-q3ef7ce37ae77

- **example_id**: `dev:q3ef7ce37ae77`
- **state**: `completed`
- **query**: How did investors respond to Tapestry, Inc.’s discussion of supply chain risks?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9734136950814526 · gold=['Earnings', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3ef7ce37ae77:chunk-7` | 0.4062 |  | Thanks, Joanne, and good morning, everyone. Looking back at our results for the fiscal year, our commitment to discipli… |
| 2 | `q3ef7ce37ae77:chunk-83` | 0.14020000000000002 |  | So I'll start with Michael Kors. And what we're seeing in our business and what our platform has been delivering is del… |
| 3 | `q3ef7ce37ae77:chunk-47` | 0.1043 |  | Well, we are building and continue to drive a healthy business. That's been our focus, not only in China, but around th… |
| 4 | `q3ef7ce37ae77:chunk-35` | 0.040299999999999996 |  | A very brief add to your specific question as it relates to what's driving gross margin. It's really the structural dri… |
| 5 | `q3ef7ce37ae77:chunk-5` | 0.0366 |  | Good morning. Thank you, Christina, and welcome, everyone. As noted in our press release, our fourth quarter results ex… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q3ef7ce37ae77`)._

### ex-dev-q3f9446fe3b94

- **example_id**: `dev:q3f9446fe3b94`
- **state**: `completed`
- **query**: How are scenario analyses conducted by American Tower Corporation for risks related to fluctuations in mobile data demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9484971533659527 · gold=['10-K', 'Earnings', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.5296347172140421 · skipped= · n_scored=342

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3f9446fe3b94:chunk-36` | 0.4295 |  | We will continue to evaluate the carrying value of our Indian assets, which may result in the realization of additional… |
| 2 | `q3f9446fe3b94:chunk-37` | 0.3475 | 1.0 | •In less advanced wireless markets where network deployments are in earlier stages, we expect these deployments to driv… |
| 3 | `q3f9446fe3b94:chunk-15` | 0.1777 | 1.0 | The development and implementation of new technologies designed to enhance the efficiency of wireless networks or chang… |
| 4 | `q3f9446fe3b94:chunk-12` | 0.1578 | 1.0 | ITEM 1A. RISK FACTORS Risks Related to Our Business Strategy A significant decrease in leasing demand for our communica… |
| 5 | `q3f9446fe3b94:chunk-13` | 0.13440000000000002 |  | Due to the long-term nature of our customer leases, we depend on the continued financial strength of our customers. Man… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q3f9446fe3b94`)._

### ex-dev-q41a18ce876e2

- **example_id**: `dev:q41a18ce876e2`
- **state**: `completed`
- **query**: What guidance was offered on Kellanova’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`10-Q` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.7227265726449519 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q41a18ce876e2:chunk-127` | 0.6709 | 1.0 | # Shareowner Proposals (cont.) ## Our Response - Statement in Opposition to Proposal: (cont.) We have implemented and m… |
| 2 | `q41a18ce876e2:chunk-34` | 0.4137 | 1.0 | # Manufacturing Committee Zack Gund (Chair) Rod Gillum Carter Cast La June Montgomery Tabron Carolyn Tastad 2023 Meetin… |
| 3 | `q41a18ce876e2:chunk-25` | 0.1018 | 1.0 | # Corporate Governance (cont.) ## RISK ASSESSMENT The risk assessment process is global in nature and has been develope… |
| 4 | `q41a18ce876e2:chunk-57` | 0.0324 |  | # 2021-2023 Performance Share Unit Plan Payouts (Pay for Performance) (cont.) ## 2023 AIP Payouts The 2023 Corporate AI… |
| 5 | `q41a18ce876e2:chunk-10` | 0.0271 |  | # Nominees for Election for a Three-Year Term Expiring at the 2027 Annual Meeting (cont.) ## ZACK GUND I 53 Qualificati… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q41a18ce876e2`)._

### ex-dev-q430300b97e2f

- **example_id**: `dev:q430300b97e2f`
- **state**: `completed`
- **query**: What guidance was offered on Ingersoll Rand’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9840990003623115 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.7227265726449519 · skipped= · n_scored=152

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q430300b97e2f:chunk-141` | 1.1448 | 1.0 | Sure. I think, Nicole, I think broad strokes here, we still see an opportunity here. I think is the long and short of i… |
| 2 | `q430300b97e2f:chunk-107` | 0.7251000000000001 | 1.0 | I don't think so. Only because -- I mean I think still there's a little bit of supply chain disruption here and there t… |
| 3 | `q430300b97e2f:chunk-79` | 0.3972 | 1.0 | Joe, I'd say that -- I mean even when you think about our guidance, I mean, it just shows that lower growth but still g… |
| 4 | `q430300b97e2f:chunk-5` | 0.0583 |  | Thanks, Matthew, and good morning to all. I would like to begin by acknowledging and thanking our employees for their h… |
| 5 | `q430300b97e2f:chunk-9` | 0.055299999999999995 |  | Thanks, Vik. On Slide 15, our Industrial Technologies and Services segment delivered solid year-over-year organic reven… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q430300b97e2f`)._

### ex-dev-q44cfaf358c37

- **example_id**: `dev:q44cfaf358c37`
- **state**: `completed`
- **query**: How do global economic or geopolitical trends shape regional market prospects for Molson Coors Beverage Company's alcoholic beverage portfolio?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q44cfaf358c37:chunk-63` | 1.2250999999999999 | 2.0 | Yes. From a -- from an overall portfolio outside of the U.S., Chris, Canada, we do continue to see softness in the beer… |
| 2 | `q44cfaf358c37:chunk-29` | 1.2124000000000001 | 2.0 | Thanks, Bryan. Look, EMEA APAC last year had a tremendous year. We grew top and bottom line double digits. And I don't … |
| 3 | `q44cfaf358c37:chunk-7` | 1.1985 | 2.0 | Thank you, Gavin. 2023 was an incredible year for our company. Our net sales revenue grew an impressive 9.3% with stron… |
| 4 | `q44cfaf358c37:chunk-5` | 1.125 | 1.0 | Thank you, Traci, and thank you, everybody, for joining us today. Before we get started, I want to mention that Tracey … |
| 5 | `q44cfaf358c37:chunk-57` | 0.9069 | 1.0 | Well, look, you're right. I mean, we do have regional differences in our cost of goods sold, all driven by -- all the f… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q44cfaf358c37`)._

### ex-dev-q4acd5677c3da

- **example_id**: `dev:q4acd5677c3da`
- **state**: `completed`
- **query**: What questions were asked about Hasbro’s customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9359826917490579 · gold=['Earnings', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.12750024571574825 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4acd5677c3da:chunk-21` | 0.053200000000000004 |  | Yes, for sure. So last year, we were fortunate in that, both MAGIC and D&D were growers for us. The MAGIC tabletop busi… |
| 2 | `q4acd5677c3da:chunk-67` | 0.0402 | 1.0 | Well, I think it's, generally speaking, all of the above. However, I think the special emphasis for Universes Beyond is… |
| 3 | `q4acd5677c3da:chunk-5` | 0.019200000000000002 |  | Thanks, [ Karan ] and good morning, everyone. For more than a year now, you've heard me outline Hasbro's strategy to re… |
| 4 | `q4acd5677c3da:chunk-7` | 0.0171 |  | Thanks, Chris, and good morning, everyone. 2023 marks an important milestone in our transformation towards a more strea… |
| 5 | `q4acd5677c3da:chunk-25` | 0.0064 |  | So first, a clarification, did you say you expect consumer products to be flat in 3Q and then up in 4Q, in that mix, ho… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q4acd5677c3da`)._

### ex-dev-q4bf1699a63fe

- **example_id**: `dev:q4bf1699a63fe`
- **state**: `completed`
- **query**: What dependency risks exist for Boston Properties, Inc. due to concentration of revenue in a limited number of geographic markets or key tenants?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.8304198973631919 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4bf1699a63fe:chunk-7` | 1.2355 | 2.0 | Thanks, Owen. Good morning, everybody. After a moment of silence to Bob, I'm going to start. In early 2023, we establis… |
| 2 | `q4bf1699a63fe:chunk-9` | 0.8383 | 2.0 | Great. Thanks, Doug. Good morning, everybody. So this morning, I plan to cover the details of the fourth quarter and ou… |
| 3 | `q4bf1699a63fe:chunk-77` | 0.7468 |  | With regards to your first question about Google, the answer is absolutely not. We have -- Google is in only one asset … |
| 4 | `q4bf1699a63fe:chunk-53` | 0.6779 | 2.0 | I would say, Michael, that the technology demand on the West Coast is lower than we would like it to be, largely becaus… |
| 5 | `q4bf1699a63fe:chunk-75` | 0.645 | 2.0 | Maybe just a question. Google announced last night meaningful office optimization charges, 1.2 billion in the quarter. … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q4bf1699a63fe`)._

### ex-dev-q4d8ac905167b

- **example_id**: `dev:q4d8ac905167b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Citigroup Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=894

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4d8ac905167b:chunk-334` | 1.2654999999999998 | 2.0 | The following are the main factors and interpretations that Citi considers when estimating the ACL under the CECL metho… |
| 2 | `q4d8ac905167b:chunk-333` | 1.2459 | 2.0 | Corporate Loans Corporate loans represent loans and leases managed by Services, Markets and Banking and the Mexico SBMM… |
| 3 | `q4d8ac905167b:chunk-294` | 1.2202 | 2.0 | U.S. real GDP contraction in 2024 of 1.9%, with a peak quarter-over-quarter difference to the base scenario of 1.2% in … |
| 4 | `q4d8ac905167b:chunk-289` | 1.2162 | 2.0 | Quantitative Component Citi estimates expected credit losses for its quantitative component using (i) its comprehensive… |
| 5 | `q4d8ac905167b:chunk-61` | 1.1881 | 2.0 | firms’ capital planning practices, focusing on six areas of capital planning: governance, risk management, internal con… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q4d8ac905167b`)._

### ex-dev-q4e3318b7d0e9

- **example_id**: `dev:q4e3318b7d0e9`
- **state**: `completed`
- **query**: How are data privacy or cybersecurity concerns affecting industry practices relevant to water technology solutions at Xylem Inc.?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-K', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['8-K', '10-K', 'DEF14A', '10-Q', 'Earnings']`
- **yield**: original=`8-K` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.8932868997079263 · skipped= · n_scored=329

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4e3318b7d0e9:chunk-20` | 1.1522999999999999 | 2.0 | Cybersecurity incidents and related data breaches or other disruptions to our enterprise information technology and ope… |
| 2 | `q4e3318b7d0e9:chunk-30` | 1.1315 | 2.0 | an adverse effect on our reputation, our business, results of operations and financial condition. Additionally, we may … |
| 3 | `q4e3318b7d0e9:chunk-31` | 1.1245 | 2.0 | Our Chief Information Security Officer ("CISO"), who has extensive cybersecurity knowledge and skills gained from over … |
| 4 | `q4e3318b7d0e9:chunk-32` | 1.0737 | 1.0 | Board of Directors Our Board recognizes the importance of maintaining the trust and confidence of our customers, suppli… |
| 5 | `q4e3318b7d0e9:chunk-21` | 0.9595 | 1.0 | We have implemented processes, procedures and technologies designed to detect and respond to cybersecurity incidents an… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q4e3318b7d0e9`)._

### ex-dev-q4f1cc6ea4ba6

- **example_id**: `dev:q4f1cc6ea4ba6`
- **state**: `completed`
- **query**: What sentiment trends are visible around Agilent Technologies’ free cash flow outlook and capital spending plans?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.7160402767315405 · skipped= · n_scored=170

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4f1cc6ea4ba6:chunk-7` | 1.2075 | 2.0 | Thanks, Mike, and good afternoon, everyone. In my remarks today, I'll provide some additional details on revenue in the… |
| 2 | `q4f1cc6ea4ba6:chunk-49` | 1.1009 | 2.0 | I'll jump right into that one. So I tried to make that come out in the script. But our plans to continue to invest for … |
| 3 | `q4f1cc6ea4ba6:chunk-163` | 1.0388 | 1.0 | Yes, I think first of all, just to remind the audience, when we talk about the genomics business, what are we talking a… |
| 4 | `q4f1cc6ea4ba6:chunk-121` | 1.0367 |  | Yes. It has the potential to do that. And as we talked about it, we're at the beginning of the year, and so we want to … |
| 5 | `q4f1cc6ea4ba6:chunk-33` | 1.0018 | 1.0 | Yes, sure, Patrick. [ How about ] if I lead off, Bob, and then you can add any additional comments you'd like to make h… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q4f1cc6ea4ba6`)._

### ex-dev-q536ce4006bf6

- **example_id**: `dev:q536ce4006bf6`
- **state**: `completed`
- **query**: What did AutoZone’s leadership say about AutoZone’s share repurchase plans?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5770094797674725 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '8-K', 'DEF14A', '10-Q', '10-K']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=7

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q536ce4006bf6:chunk-1` | 1.1189 | 1.0 | Under its share repurchase program, AutoZone repurchased 580 thousand shares of its common stock at an average price pe… |
| 2 | `q536ce4006bf6:chunk-2` | 0.5415 | 1.0 | AutoZone does not derive revenue from automotive repair or installation services. AutoZone will host a conference call … |
| 3 | `q536ce4006bf6:chunk-5` | 0.3396 |  | [Chunk Index 6] <table><tr><td>AutoZone's 1st Quarter Highlights - Fiscal 2024</td><td></td><td></td><td></td><td></td>… |
| 4 | `q536ce4006bf6:chunk-4` | 0.0054 |  | <table><tr><td colspan="11">AutoZone's 1st Quarter Highlights - Fiscal 2024</td><td></td><td colspan="3"></td><td></td>… |
| 5 | `q536ce4006bf6:chunk-7` | 0.003 |  | [Chunk Index 8] <table><tr><td colspan="23">AutoZone's 1st Quarter Highlights - Fiscal 2024</td><td></td></tr><tr><td c… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q536ce4006bf6`)._

### ex-dev-q53994e82efbb

- **example_id**: `dev:q53994e82efbb`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Builders FirstSource for recessionary or downturn risks in the residential construction market?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.8503449055347546 · skipped= · n_scored=64

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q53994e82efbb:chunk-40` | 0.1752 | 1.0 | weighted average price of $97.43 per share, for a total cost of approximately $1.6 billion, inclusive of fees and taxes… |
| 2 | `q53994e82efbb:chunk-51` | 0.1023 |  | As of September 30, 2023, we had $0.7 billion in outstanding borrowings under our Revolving Facility, and our net exces… |
| 3 | `q53994e82efbb:chunk-38` | 0.0945 |  | We base our estimate of deferred tax assets and liabilities on current tax laws and rates. In certain cases, we also ba… |
| 4 | `q53994e82efbb:chunk-48` | 0.0775 |  | We experienced decreased net sales in all of our product categories primarily due to a slowing economy, a decline in co… |
| 5 | `q53994e82efbb:chunk-45` | 0.0382 | 1.0 | We experienced decreased net sales in all of our product categories primarily due to a slow-down in single-family housi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q53994e82efbb`)._

### ex-dev-q56c2aa1b3aa2

- **example_id**: `dev:q56c2aa1b3aa2`
- **state**: `completed`
- **query**: How are scenario analyses conducted by FedEx Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.5855700749881525 · skipped= · n_scored=165

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q56c2aa1b3aa2:chunk-28` | 0.712 | 1.0 | # Corporate Governance Matters - Nominees for Election to the Board (cont.) ## Board Risk Oversight The Board of Direct… |
| 2 | `q56c2aa1b3aa2:chunk-29` | 0.0059 |  | # Compensation and Human Resources Committee (cont.) ## Governance, Safety, and Public Policy Committee The Compensatio… |
| 3 | `q56c2aa1b3aa2:chunk-39` | 0.0053 | 1.0 | # CYBER AND TECHNOLOGY OVERSIGHT COMMITTEE (cont.) ## FY23 MEETINGS HELD 6 V. James Vena served as a member of the GSPP… |
| 4 | `q56c2aa1b3aa2:chunk-137` | 0.0052 |  | # Board of Directors' Statement in Opposition (cont.) ## Your Board of Directors recommends that you vote "AGAINST" thi… |
| 5 | `q56c2aa1b3aa2:chunk-2` | 0.0045000000000000005 |  | # A MESSAGE FROM OUR EXECUTIVE CHAIRMAN AND LEAD INDEPENDENT DIRECTOR To our stockholders, In connection with our 2023 … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q56c2aa1b3aa2`)._

### ex-dev-q57e9d5635f56

- **example_id**: `dev:q57e9d5635f56`
- **state**: `completed`
- **query**: What quarter did guidance point to for streaming breakeven achievement
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.9197207891481876 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q57e9d5635f56:chunk-7` | 1.2777 | 2.0 | Thank you, Bob. I appreciate your kind words at the outset of the call. It's been an honor serving as Interim CFO these… |
| 2 | `q57e9d5635f56:chunk-5` | 1.2734 |  | Thanks, Alexia, and good afternoon, everyone. Before we begin, this week, we announced that Hugh Johnston will be joini… |
| 3 | `q57e9d5635f56:chunk-21` | 1.1549 | 2.0 | I'll take the second part first. Our plan when we bring ESPN direct to consumer, which is inevitable, which is going to… |
| 4 | `q57e9d5635f56:chunk-19` | 0.0864 |  | So first on DTC. I mean, pricing is about to step up. You announced the cost-cutting program, some of which might be a … |
| 5 | `q57e9d5635f56:chunk-15` | 0.0349 |  | Thanks, Michael. Regarding Charter, first of all, as we said when we did the deal, we think it's a great deal for us. I… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q57e9d5635f56`)._

### ex-dev-q587ea3fc913d

- **example_id**: `dev:q587ea3fc913d`
- **state**: `completed`
- **query**: What guidance did Textron’s leadership give on cost structure optimization efforts?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=174

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q587ea3fc913d:chunk-113` | 1.2847000000000002 | 2.0 | Well, Kristine, as we kind of put out there, there's a sizable piece that's going into Bell, and that's really aligning… |
| 2 | `q587ea3fc913d:chunk-131` | 1.2793 | 2.0 | George, I think look, we're continuing to see good margins on our military business, obviously outside of the FLRAA sid… |
| 3 | `q587ea3fc913d:chunk-77` | 1.2349 | 2.0 | Well, look, I mean we don't -- we're probably not going to break that all the way down, but certainly part of why the d… |
| 4 | `q587ea3fc913d:chunk-73` | 1.2141000000000002 | 2.0 | Well, I wouldn't say nonmaterial. I would say, Myles -- and look in 2023, we had pretty significant price over inflatio… |
| 5 | `q587ea3fc913d:chunk-123` | 1.1667 | 2.0 | Look, George, as you know, it takes many months to build an aircraft. So the improvements in both the labor side and th… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q587ea3fc913d`)._

### ex-dev-q5ce8ea5bf1b9

- **example_id**: `dev:q5ce8ea5bf1b9`
- **state**: `completed`
- **query**: What dependency risks exist for Global Payments Inc. due to concentration of revenue in a limited number of payment processing partners or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.07132875491150918 · skipped= · n_scored=119

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5ce8ea5bf1b9:chunk-107` | 0.2109 |  | Forward-Looking Statements Some of the statements we use in this report, and in some of the documents we incorporate by… |
| 2 | `q5ce8ea5bf1b9:chunk-25` | 0.1676 | 1.0 | NOTE 2—ACQUISITION EVO Payments, Inc. On March 24, 2023, we acquired all of the outstanding common stock of EVO Payment… |
| 3 | `q5ce8ea5bf1b9:chunk-93` | 0.1471 |  | Highlights related to our financial condition at September 30, 2023 and results of operations for the three and nine mo… |
| 4 | `q5ce8ea5bf1b9:chunk-92` | 0.049300000000000004 |  | ITEM 2—MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following discussion a… |
| 5 | `q5ce8ea5bf1b9:chunk-100` | 0.036199999999999996 |  | (1) Percentage amounts may not sum to the total due to rounding. (2) Revenues, consolidated operating expenses, operati… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q5ce8ea5bf1b9`)._

### ex-dev-q5d75c4f1ac86

- **example_id**: `dev:q5d75c4f1ac86`
- **state**: `completed`
- **query**: What progress was reported in international park attendance recovery relative to pre pandemic levels
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.93228165068934 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.13770577618809332 · skipped= · n_scored=155

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5d75c4f1ac86:chunk-60` | 0.6002 |  | # EXECUTIVE COMPENSATION (cont.) ## Financial Performance (cont.) For purposes of the annual performance-based bonuses,… |
| 2 | `q5d75c4f1ac86:chunk-3` | 0.4274 |  | # Letter to the Shareholders (cont.) ## Dear Fellow Shareholders, (cont.) Our parks, experiences and products business,… |
| 3 | `q5d75c4f1ac86:chunk-48` | 0.2541 | 1.0 | # Executive Compensation (cont.) ## Letter from the Compensation Committee (cont.) We are pleased with the investor sup… |
| 4 | `q5d75c4f1ac86:chunk-66` | 0.23070000000000002 |  | # MR. CHAPEK <table><tr><td>Salary</td><td>Mr. Chapek's 2021 annual salary was unchanged from the annual salary set at … |
| 5 | `q5d75c4f1ac86:chunk-11` | 0.22219999999999998 |  | # Table of Contents (cont.) ## COVID-19 Response Throughout these challenging times, the Company has continued to suppo… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q5d75c4f1ac86`)._

### ex-dev-q5d883a6e3ff1

- **example_id**: `dev:q5d883a6e3ff1`
- **state**: `completed`
- **query**: How have investors reacted to The TJX Companies, Inc.’s updated guidance or forward-looking projections?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.8498932729020808 · gold=['Earnings', '8-K', '10-K', 'DEF14A']
- **S1 ordered**: `['8-K', 'Earnings', '10-Q', '10-K', 'DEF14A']`
- **yield**: original=`8-K` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.3903800499921017 · skipped= · n_scored=215

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5d883a6e3ff1:chunk-16` | 0.4474 | 1.0 | As with our current operations, risks are inherent in opening and developing operations in new countries, including tho… |
| 2 | `q5d883a6e3ff1:chunk-36` | 0.0411 |  | ITEM 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations TJX provides projections … |
| 3 | `q5d883a6e3ff1:chunk-39` | 0.011300000000000001 |  | Net Sales Net sales for fiscal 2024 totaled $54.2 billion, a 9% increase versus net sales of $49.9 billion for fiscal 2… |
| 4 | `q5d883a6e3ff1:chunk-10` | 0.008 |  | ITEM 1A. Risk Factors The statements in this section describe the major risks to our business and should be considered … |
| 5 | `q5d883a6e3ff1:chunk-15` | 0.0066 |  | Damage to our corporate reputation or those of our retail banners could adversely affect our sales and operating result… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q5d883a6e3ff1`)._

### ex-dev-q5fca8aed3bbc

- **example_id**: `dev:q5fca8aed3bbc`
- **state**: `completed`
- **query**: How has the ratio of Camden Property Trust’s recurring rental income to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.6280699432768105 · gold=['10-K', '8-K', 'Earnings', '10-Q']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.7227265726449519 · skipped= · n_scored=103

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5fca8aed3bbc:chunk-74` | 0.8074999999999999 | 1.0 | (1) Same store communities are communities we wholly-owned and were stabilized since January 1, 2022, excluding communi… |
| 2 | `q5fca8aed3bbc:chunk-56` | 0.6670999999999999 | 1.0 | These forward-looking statements represent our estimates and assumptions as of the date of this report, and we assume n… |
| 3 | `q5fca8aed3bbc:chunk-26` | 0.4382 | 1.0 | Deferred Compensation Plan Investments. The estimated fair values of investment securities classified as deferred compe… |
| 4 | `q5fca8aed3bbc:chunk-90` | 0.3327 |  | Liquidity and Capital Resources Financial Condition and Sources of Liquidity We intend to maintain a strong balance she… |
| 5 | `q5fca8aed3bbc:chunk-20` | 0.2126 |  | ######Nine Months Ended September 30,#### (in thousands)####2023######2022 Cash flows from operating activities########… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q5fca8aed3bbc`)._

### ex-dev-q60107966eba4

- **example_id**: `dev:q60107966eba4`
- **state**: `completed`
- **query**: How does Kellanova view the pace of innovation cycles in product development and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7083232243990188 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **yield**: original=`10-K` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.8613098738256916 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q60107966eba4:chunk-9` | 1.2149 | 2.0 | Thanks, Amit. Slide #22 splits our portfolio into category groups to help remind you of their relative sizes and growth… |
| 2 | `q60107966eba4:chunk-29` | 1.1883 | 2.0 | Yes. It's going to -- Rob, thanks for the question. It's going to be throughout the year. Really, we started with displ… |
| 3 | `q60107966eba4:chunk-43` | 0.679 | 1.0 | Yes, that's right because I mean, the comparisons are going to be against a year where we really didn't innovate and no… |
| 4 | `q60107966eba4:chunk-5` | 0.6502 | 1.0 | Thanks, John, and good morning, everyone. It's a real pleasure to be able to present to you results for Kellanova for t… |
| 5 | `q60107966eba4:chunk-41` | 0.6016 | 1.0 | Okay. So really, we should be looking at the strength of additional innovation, adding to market share performance with… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q60107966eba4`)._

### ex-dev-q63259a02ade0

- **example_id**: `dev:q63259a02ade0`
- **state**: `completed`
- **query**: What does Apple's executive compensation structure look like?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=1.0 · gold=['DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **yield**: original=`DEF14A` · effective=`DEF14A` · used=False
- **S2**: nDCG@5=0.16174285170544084 · skipped= · n_scored=134

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q63259a02ade0:chunk-47` | 1.2424 | 1.0 | # The Role of the Compensation Consultant (cont.) ## Annual Base Salary Base salary is a customary, fixed element of co… |
| 2 | `q63259a02ade0:chunk-8` | 1.2064 |  | # Executive Compensation (cont.) ## Aligned with Shareholder Interests and Company Performance (cont.) - Shareholders h… |
| 3 | `q63259a02ade0:chunk-42` | 1.1842000000000001 |  | # Guiding Compensation Principles Our executive compensation program is designed to motivate and reward outstanding per… |
| 4 | `q63259a02ade0:chunk-51` | 1.1834 | 1.0 | # Summary of Other Named Executive Officer Compensation The total target compensation of our four other named executive… |
| 5 | `q63259a02ade0:chunk-39` | 1.1812 |  | # Message from the People and Compensation Committee (cont.) ## Dear Fellow Shareholders, (cont.) As we look ahead, we'… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q63259a02ade0`)._

### ex-dev-q636b07dd9c11

- **example_id**: `dev:q636b07dd9c11`
- **state**: `completed`
- **query**: What impact could proposed legislative changes in the U.S. Credit Card Competition Act have on Mastercard?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.5860880558992709 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['8-K', 'DEF14A', 'Earnings', '10-Q', '10-K']`
- **yield**: original=`8-K` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.9129675424759451 · skipped= · n_scored=312

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q636b07dd9c11:chunk-27` | 1.2214 | 2.0 | Payments Oversight and Regulation. Central banks and other regulators around the world either have, or are seeking to e… |
| 2 | `q636b07dd9c11:chunk-34` | 0.7947 | 1.0 | PART I ITEM 1A. RISK FACTORS we charge our customers could also materially and adversely impact our results of operatio… |
| 3 | `q636b07dd9c11:chunk-33` | 0.7527 | 1.0 | Legal and Regulatory Payments Industry Regulation Global regulatory and legislative activity related to the payments in… |
| 4 | `q636b07dd9c11:chunk-43` | 0.7091 |  | PART I ITEM 1A. RISK FACTORS Merchants’ continued focus on acceptance costs may lead to additional litigation and regul… |
| 5 | `q636b07dd9c11:chunk-37` | 0.5811999999999999 | 1.0 | PART I ITEM 1A. RISK FACTORS Litigation Liabilities we may incur or limitations on our business related to any litigati… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q636b07dd9c11`)._

### ex-dev-q645be3b7875e

- **example_id**: `dev:q645be3b7875e`
- **state**: `completed`
- **query**: How has the ratio of Merck & Co., Inc.’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.5993473179020821 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.46067715488476185 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q645be3b7875e:chunk-24` | 0.6304000000000001 |  | (1) Includes royalty expense, amortization of capitalized milestone payments and inventory reserves. (2) Expenses inclu… |
| 2 | `q645be3b7875e:chunk-85` | 0.5845 | 2.0 | U.S. plus international may not equal total due to rounding. (1) Alliance revenue for Lynparza and Lenvima represents M… |
| 3 | `q645be3b7875e:chunk-13` | 0.11539999999999999 |  | Notes to Condensed Consolidated Financial Statements (unaudited) (continued) development of the investigational ADC. Me… |
| 4 | `q645be3b7875e:chunk-99` | 0.105 |  | Lynparza (olaparib) is an oral poly (ADP-ribose) polymerase (PARP) inhibitor being developed as part of a collaboration… |
| 5 | `q645be3b7875e:chunk-19` | 0.104 | 1.0 | (1) Represents amortization of capitalized milestone payments. Amounts in the third quarter and first nine months of 20… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q645be3b7875e`)._

### ex-dev-q64898e5ba36c

- **example_id**: `dev:q64898e5ba36c`
- **state**: `completed`
- **query**: What clarifications did analysts seek regarding Waters Corporation’s investment in chromatography and mass spectrometry innovation projects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9873464281832952 · gold=['Earnings', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', 'DEF14A', '10-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=274

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q64898e5ba36c:chunk-6` | 0.1035 |  | System and is five times more sensitive and five times faster than discovery-based imaging systems at precisely determi… |
| 2 | `q64898e5ba36c:chunk-3` | 0.0898 |  | speed of measuring the potency and safety of AAVs. Combining the columns with light scattering technologies from its Wy… |
| 3 | `q64898e5ba36c:chunk-4` | 0.0697 |  | (“Q-Tof”) instruments, such as the Company’s SYNAPTTM G2-S HDMS System, are often used to analyze the role of proteins … |
| 4 | `q64898e5ba36c:chunk-1` | 0.0431 |  | and regulatory environments. Because of these similarities, the two segments have been aggregated into one reporting se… |
| 5 | `q64898e5ba36c:chunk-5` | 0.0383 |  | Based upon 2023 reports from independent marketing research firms and publicly disclosed sales figures from competitors… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q64898e5ba36c`)._

### ex-dev-q69d1505292c8

- **example_id**: `dev:q69d1505292c8`
- **state**: `completed`
- **query**: How might global inflationary trends affect Walgreens Boots Alliance’s input costs and pricing strategies?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.3295833540079424 · skipped= · n_scored=202

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q69d1505292c8:chunk-120` | 0.702 | 1.0 | WALGREENS BOOTS ALLIANCE, INC. AND SUBSIDIARIES MANAGEMENT'S DISCUSSION AND ANALYSIS Item 2. Management’s discussion an… |
| 2 | `q69d1505292c8:chunk-180` | 0.6921 | 1.0 | WALGREENS BOOTS ALLIANCE, INC. AND SUBSIDIARIES MANAGEMENT'S DISCUSSION AND ANALYSIS 17 The Company reconciles Adjusted… |
| 3 | `q69d1505292c8:chunk-29` | 0.5034 |  | WALGREENS BOOTS ALLIANCE, INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED CONDENSED FINANCIAL STATEMENTS (UNAUDITED) On Oct… |
| 4 | `q69d1505292c8:chunk-122` | 0.2419 |  | WALGREENS BOOTS ALLIANCE, INC. AND SUBSIDIARIES MANAGEMENT'S DISCUSSION AND ANALYSIS Sale of Cencora common stock On No… |
| 5 | `q69d1505292c8:chunk-178` | 0.1899 |  | 3##Acquisition-related amortization includes amortization of acquisition-related intangible assets, inventory valuation… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q69d1505292c8`)._

### ex-dev-q6c95b5e5930d

- **example_id**: `dev:q6c95b5e5930d`
- **state**: `completed`
- **query**: What guidance was offered on Medtronic’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`10-Q` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.6309297535714575 · skipped= · n_scored=161

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q6c95b5e5930d:chunk-11` | 0.5216999999999999 |  | # Director Selection Process (cont.) ## Fiscal Year 2023 Performance Highlights (cont.) The image is a blank white page… |
| 2 | `q6c95b5e5930d:chunk-10` | 0.3712 | 1.0 | # Director Selection Process (cont.) ## Shareholder Outreach on Governance The Company recognizes the value of sharehol… |
| 3 | `q6c95b5e5930d:chunk-53` | 0.3497 |  | # Executive Summary (cont.) ## Fiscal Year 2023 Financial Performance Summary Medtronic financial results fell below it… |
| 4 | `q6c95b5e5930d:chunk-16` | 0.0069 |  | # Sustainability and ESG Highlights (cont.) ## Performance and Disclosure Medtronic has set public targets to reduce th… |
| 5 | `q6c95b5e5930d:chunk-15` | 0.0067 |  | # Sustainability and ESG Highlights (cont.) ## INNOVATION & ACCESS Increasing the availability of treatments to address… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q6c95b5e5930d`)._

### ex-dev-q6cdb93e02e5f

- **example_id**: `dev:q6cdb93e02e5f`
- **state**: `completed`
- **query**: What clawback or recoupment policies apply to SBA Communications Corporation’s incentive compensation in case of restatements or misconduct?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8498932729020808 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **yield**: original=`10-K` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=121

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q6cdb93e02e5f:chunk-33` | 1.1269 | 2.0 | # Compensation Risks (cont.) ## Executive Compensation "No Fault" Recoupment or "Clawback" Policies Our Board has maint… |
| 2 | `q6cdb93e02e5f:chunk-56` | 0.7739 | 1.0 | # Executive Summary (cont.) ## Our Strong Corporate Governance Policies Further Align our Executives' Interests with Th… |
| 3 | `q6cdb93e02e5f:chunk-21` | 0.6974 | 1.0 | # Compensation Committee (cont.) ## Responsibilities > Establishes salaries, incentives and other forms of compensation… |
| 4 | `q6cdb93e02e5f:chunk-6` | 0.55 | 1.0 | # Governance Highlights (cont.) ## COMPREHENSIVE, INTEGRATED CORPORATE GOVERNANCE <figure description={The image shows … |
| 5 | `q6cdb93e02e5f:chunk-1` | 0.27490000000000003 | 1.0 | # TABLE OF CONTENTS <table><tr><th>PROXY SUMMARY</th><th></th><th>1</th></tr><tr><td>PROPOSAL 1: ELECTION OF DIRECTORS.… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q6cdb93e02e5f`)._

### ex-dev-q6d2cc453ca8c

- **example_id**: `dev:q6d2cc453ca8c`
- **state**: `completed`
- **query**: How did analysts probe the outlook for Roper Technologies’ free cash flow generation?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9278143341459562 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.16520887526157216 · skipped= · n_scored=130

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q6d2cc453ca8c:chunk-7` | 1.0019 |  | Great. Thanks, Neil. I'll walk through the enterprise and segment results for Q4 and enterprise results for the full ye… |
| 2 | `q6d2cc453ca8c:chunk-9` | 0.6644 |  | Thanks, Jason. As we turn to Page 12, let's look back on the year for Application Software segment. Total revenues grew… |
| 3 | `q6d2cc453ca8c:chunk-5` | 0.6572 |  | Thank you, Zack, and thanks to everyone for joining our call. We're looking forward to sharing our quite good 2023 4th … |
| 4 | `q6d2cc453ca8c:chunk-59` | 0.3816 | 1.0 | Got it. And then just following up on the M&A side of things, leverage at 3x, obviously, strong cash flow generator. Bu… |
| 5 | `q6d2cc453ca8c:chunk-111` | 0.3803 | 1.0 | Absolutely. Yes. We're looking forward to the accretion after '24, and it will come, like I said, it's grown mid-teens,… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q6d2cc453ca8c`)._

### ex-dev-q70b3e2802bf7

- **example_id**: `dev:q70b3e2802bf7`
- **state**: `completed`
- **query**: How did Tyson Foods’ average cost per pound of processed chicken trend compared to the prior period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.788088263175707 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.6234997966086261 · skipped= · n_scored=165

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q70b3e2802bf7:chunk-106` | 1.1799 | 2.0 | Third quarter – Fiscal 2024 vs Fiscal 2023 •Cost of sales increased $12 million. Higher sales volume increased cost of … |
| 2 | `q70b3e2802bf7:chunk-107` | 0.7355 | 1.0 | •Increase of $42 million in our Beef segment from insurance proceeds received in the first quarter of fiscal 2023 relat… |
| 3 | `q70b3e2802bf7:chunk-139` | 0.6501 |  | •Non-cash items in net income primarily included depreciation and amortization of $1,082 million and $943 million for t… |
| 4 | `q70b3e2802bf7:chunk-97` | 0.4635 |  | We operate in four reportable segments: Beef, Pork, Chicken, and Prepared Foods. We measure segment profit as operating… |
| 5 | `q70b3e2802bf7:chunk-132` | 0.2641 |  | •Operating Income (Loss) - Operating income increased in the third quarter of fiscal 2024 primarily due to improved ope… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q70b3e2802bf7`)._

### ex-dev-q70e4aac30ddb

- **example_id**: `dev:q70e4aac30ddb`
- **state**: `completed`
- **query**: How did leadership respond to analyst questions about AI and personalization initiatives?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9903929125301808 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', 'DEF14A', '10-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.6885288809404666 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q70e4aac30ddb:chunk-53` | 0.38060000000000005 | 1.0 | John, if I could take that on. Thank you for your question. We have more opportunities than what we have realized, but … |
| 2 | `q70e4aac30ddb:chunk-39` | 0.3667 |  | If I can just add one thing to it. I think what has happened over the last several years is how much this business has … |
| 3 | `q70e4aac30ddb:chunk-7` | 0.1359 | 2.0 | Thank you, Laxman, and good morning, everyone. I'm very pleased to discuss our strong Q4 and full fiscal year 2023 perf… |
| 4 | `q70e4aac30ddb:chunk-47` | 0.07830000000000001 |  | The only thing I would add to that, Sharon, is that's all part of our reinvention. So it's all about finding ways to be… |
| 5 | `q70e4aac30ddb:chunk-5` | 0.0402 |  | Thank you, Tiffany. Good morning, everyone. Welcome to Starbucks' Fourth Quarter and Fiscal Year 2023 Earnings Conferen… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q70e4aac30ddb`)._

### ex-dev-q719082ac2068

- **example_id**: `dev:q719082ac2068`
- **state**: `completed`
- **query**: How did management characterize the evolution and strategic importance of AI factories?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9239941662222116 · gold=['Earnings', '10-K', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=15

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q719082ac2068:chunk-0` | 0.2846 | 1.0 | # FOR IMMEDIATE RELEASE: NVIDIA Announces Financial Results for Fourth Quarter and Fiscal 2024 - Record quarterly reven… |
| 2 | `q719082ac2068:chunk-3` | 0.0895 |  | # Q4 Fiscal 2024 Summary (cont.) ## Data Center (cont.) - Introduced NVIDIA MONAITM cloud APIs to help developers and p… |
| 3 | `q719082ac2068:chunk-2` | 0.02 |  | # Q4 Fiscal 2024 Summary (cont.) ## Fiscal 2024 Summary <table><tr><td>GAAP</td></tr></table> <table><tr><td>($ in mill… |
| 4 | `q719082ac2068:chunk-6` | 0.0049 |  | # Q4 Fiscal 2024 Summary (cont.) ## About NVIDIA (cont.) Certain statements in this press release including, but not li… |
| 5 | `q719082ac2068:chunk-1` | 0.0016 |  | # Q4 Fiscal 2024 Summary <table><tr><td>GAAP</td></tr></table> <table><tr><td>($ in millions, except earnings per share… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q719082ac2068`)._

### ex-dev-q76caada13eca

- **example_id**: `dev:q76caada13eca`
- **state**: `completed`
- **query**: What causes differences between Weyerhaeuser Company’s cash flow and net income (e.g., timberland harvest cycles or non-cash depreciation)?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9199642183398656 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.9832184408687481 · skipped= · n_scored=86

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q76caada13eca:chunk-7` | 0.8715999999999999 | 2.0 | Thank you, Devin, and good morning, everyone. I'll be covering key financial items and fourth quarter financial perform… |
| 2 | `q76caada13eca:chunk-67` | 0.7201 | 1.0 | Perfect. And then just one quick question on Timberland, especially on pulpwood. I want to get your thoughts around the… |
| 3 | `q76caada13eca:chunk-5` | 0.4722 |  | Thanks, Andy. Good morning, everyone, and thank you for joining us. Yesterday, Weyerhaeuser reported full year GAAP ear… |
| 4 | `q76caada13eca:chunk-55` | 0.1749 | 1.0 | No. We still have a high degree of conviction about the value of timberlands over time and our ability to generate stro… |
| 5 | `q76caada13eca:chunk-69` | 0.0702 |  | Yes, that's a great question. We've seen over the last several years, generally speaking, the pulpwood market has been … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q76caada13eca`)._

### ex-dev-q78d98dc75a82

- **example_id**: `dev:q78d98dc75a82`
- **state**: `completed`
- **query**: How has Humana’s Medicare Advantage segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '8-K', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.7693968268775773 · skipped= · n_scored=283

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q78d98dc75a82:chunk-70` | 1.1564 | 2.0 | Benefits expense The Insurance segment benefit ratio increased 140 basis points from 86.6% in the 2022 period to 88.0% … |
| 2 | `q78d98dc75a82:chunk-63` | 1.1238 | 2.0 | Premiums Revenue Consolidated premiums revenue increased $13.6 billion, or 15.5%, from $87.7 billion in the 2022 period… |
| 3 | `q78d98dc75a82:chunk-230` | 1.0641 | 1.0 | ####Insurance####CenterWell######Eliminations/ Corporate####Consolidated ##########(in millions)######## 2023##########… |
| 4 | `q78d98dc75a82:chunk-233` | 1.0564 | 1.0 | ####Insurance####CenterWell######Eliminations/ Corporate####Consolidated ##########(in millions)######## 2022##########… |
| 5 | `q78d98dc75a82:chunk-236` | 1.0422 | 1.0 | ####Insurance####CenterWell######Eliminations/ Corporate####Consolidated ##########(in millions)######## 2021##########… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q78d98dc75a82`)._

### ex-dev-q79acb772ca6b

- **example_id**: `dev:q79acb772ca6b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Ingersoll Rand Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.93228165068934 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=290

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q79acb772ca6b:chunk-8` | 0.1379 |  | ITEM 1A. RISK FACTORS The following risk factors as well as the other information included in this Form 10-K, including… |
| 2 | `q79acb772ca6b:chunk-9` | 0.0322 |  | success will depend, in large part, on our ability to anticipate and effectively manage these risks associated with our… |
| 3 | `q79acb772ca6b:chunk-10` | 0.018000000000000002 |  | Acquisitions, including integrating such acquisitions, and dispositions create certain risks and may affect our operati… |
| 4 | `q79acb772ca6b:chunk-0` | 0.0085 |  | PART I SPECIAL NOTE REGARDING FORWARD-LOOKING STATEMENTS In addition to historical information, this Annual Report on F… |
| 5 | `q79acb772ca6b:chunk-90` | 0.0058000000000000005 |  | INGERSOLL RAND INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (in millions, except share and per shar… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q79acb772ca6b`)._

### ex-dev-q79ae686681b7

- **example_id**: `dev:q79ae686681b7`
- **state**: `completed`
- **query**: How has the ratio of Best Buy’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7591919243197319 · gold=['10-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=102

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q79ae686681b7:chunk-78` | 0.276 |  | Notable comparable sales changes by revenue category were as follows: Computing and Mobile Phones: The 1.0% comparable… |
| 2 | `q79ae686681b7:chunk-71` | 0.1779 |  | Notable comparable sales changes by revenue category were as follows: Computing and Mobile Phones: The 8.3% comparable… |
| 3 | `q79ae686681b7:chunk-45` | 0.0345 |  | (1)Receivables are recorded net of allowances for doubtful accounts of $19 million, $22 million and $20 million as of O… |
| 4 | `q79ae686681b7:chunk-43` | 0.0197 |  | 7. Revenue We generate substantially all of our revenue from contracts with customers from the sale of products and ser… |
| 5 | `q79ae686681b7:chunk-60` | 0.0148 |  | Non-GAAP Financial Measures This MD&A includes financial information prepared in accordance with accounting principles … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q79ae686681b7`)._

### ex-dev-q7b42f1295dc1

- **example_id**: `dev:q7b42f1295dc1`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Fiserv for recessionary or downturn risks?
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.6859372277669218 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['8-K', '10-K', 'DEF14A', '10-Q', 'Earnings']`
- **yield**: original=`8-K` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.8687949224876582 · skipped= · n_scored=256

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7b42f1295dc1:chunk-35` | 0.30619999999999997 | 1.0 | Our focus on long-term client relationships and recurring, transaction-oriented products and services has reduced the i… |
| 2 | `q7b42f1295dc1:chunk-15` | 0.2378 | 1.0 | Global Market Risks Our business may be adversely affected by geopolitical and other risks associated with operations o… |
| 3 | `q7b42f1295dc1:chunk-235` | 0.166 | 1.0 | including the allocation of consideration to the remaining performance obligations and the period of recognition for ea… |
| 4 | `q7b42f1295dc1:chunk-63` | 0.0753 | 1.0 | Item 7A. Quantitative and Qualitative Disclosures About Market Risk Market risk refers to the risk that a change in the… |
| 5 | `q7b42f1295dc1:chunk-20` | 0.059800000000000006 |  | and disclosures made or actions taken by the companies we acquire or their representatives, as well as the limited amou… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q7b42f1295dc1`)._

### ex-dev-q7c284aabbba4

- **example_id**: `dev:q7c284aabbba4`
- **state**: `completed`
- **query**: What dependency risks exist for Moderna, Inc. due to concentration of revenue in a limited number of vaccine products or geographic markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9882048111454694 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.9520727775370875 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7c284aabbba4:chunk-7` | 1.1777 | 2.0 | Thanks, Stéphane, and hello, everyone. Today, I will review our financial performance for both the fourth quarter and t… |
| 2 | `q7c284aabbba4:chunk-5` | 1.1401 | 2.0 | Thank you, Lavina. Good morning or good afternoon, everyone. Thank you for joining us today. I will start with a review… |
| 3 | `q7c284aabbba4:chunk-11` | 0.9598 | 2.0 | Thank you, Stephen and Jamey. For Moderna and the patients we serve, 2024 is all about execution: execution in commerci… |
| 4 | `q7c284aabbba4:chunk-25` | 0.9076 | 2.0 | Thanks, Stephen. And Gena, it's Stéphane. On the upside and downside on the sales for this year, I think on the upside,… |
| 5 | `q7c284aabbba4:chunk-9` | 0.49260000000000004 |  | Thank you, Jamey. Good morning or good afternoon, everyone. Today, I'll do a quick review of our clinical highlights fr… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q7c284aabbba4`)._

### ex-dev-q7e2586950d8e

- **example_id**: `dev:q7e2586950d8e`
- **state**: `completed`
- **query**: How has Ball Corporation’s beverage packaging segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.6985436835905778 · skipped= · n_scored=138

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7e2586950d8e:chunk-117` | 1.1249 | 2.0 | Okay. And then I feel like we've hit each segment sort of in different answers to questions. But I think I heard you in… |
| 2 | `q7e2586950d8e:chunk-5` | 1.04 |  | Thanks, Dan. Over the first few months of my onboarding and immersion, I have learned more about the business by visiti… |
| 3 | `q7e2586950d8e:chunk-91` | 0.9998 | 2.0 | Yes. I would add just a couple of comments. Obviously, the volatile -- when you're in more volatile emerging markets "c… |
| 4 | `q7e2586950d8e:chunk-121` | 0.9246 | 2.0 | Yes, Gabe. I think I've got it, sorry. Let me start with South America. No, we should see an inflection in earnings yea… |
| 5 | `q7e2586950d8e:chunk-3` | 0.8584 | 1.0 | Thank you, Christina. Good morning, everyone. This is Ball Corporation's Conference Call regarding the company's fourth… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q7e2586950d8e`)._

### ex-dev-q7eb4e8a11956

- **example_id**: `dev:q7eb4e8a11956`
- **state**: `completed`
- **query**: Summarize Luca Maestri's recent commentary on the gross margin outlook given current FX headwinds.
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7eb4e8a11956:chunk-29` | 1.2304000000000002 |  | As you've seen from our results in Q4 and the guidance for Q1, we're obviously experiencing very strong levels of gross… |
| 2 | `q7eb4e8a11956:chunk-87` | 1.2288000000000001 |  | Well, on the products side, as you know, we -- when we launch new products, the cost structures of those products tend … |
| 3 | `q7eb4e8a11956:chunk-47` | 1.2216 |  | On the margin side, if I understood your question correctly about the December quarter guidance, keep in mind that actu… |
| 4 | `q7eb4e8a11956:chunk-7` | 1.2143 |  | Thank you, Tim, and good afternoon, everyone. Revenue for the September quarter was $89.5 billion, down less than 1% fr… |
| 5 | `q7eb4e8a11956:chunk-43` | 0.5751000000000001 |  | I know you covered China. I want to pivot to the U.S. for a second. Obviously, iPhone and the business looks like it re… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q7eb4e8a11956`)._

### ex-dev-q7eb5b91e2366

- **example_id**: `dev:q7eb5b91e2366`
- **state**: `completed`
- **query**: What dependency risks exist for Becton, Dickinson and Company due to concentration of revenue in a limited number of healthcare providers or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9935051443580323 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=76

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7eb5b91e2366:chunk-7` | 0.6553 | 1.0 | *Thanks, Tom, and good morning, everyone. As Tom noted, we delivered competitive organic revenue growth for the fourth … |
| 2 | `q7eb5b91e2366:chunk-13` | 0.3523 |  | Okay. Vijay, I appreciate the comments there. So I'll start off with just some comments on some of our assumptions for … |
| 3 | `q7eb5b91e2366:chunk-5` | 0.2515 |  | Thanks, Greg, and good morning, everyone. First, I'd like to take a moment to welcome Mike Feld, President of our Life … |
| 4 | `q7eb5b91e2366:chunk-43` | 0.2156 |  | Yes. Thanks for the question, Patrick. From a tariff perspective, when we saw this dynamic that happened in the past, w… |
| 5 | `q7eb5b91e2366:chunk-37` | 0.0256 |  | Yes. Thanks for the question, Robbie. We feel really good about the -- how we've been moving BD into higher growth spac… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q7eb5b91e2366`)._

### ex-dev-q7ebef55d671d

- **example_id**: `dev:q7ebef55d671d`
- **state**: `completed`
- **query**: What guidance was offered on Chipotle’s supply chain efficiency targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6266239202359082 · gold=['DEF14A', '10-Q', '10-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`Earnings` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=130

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ebef55d671d:chunk-5` | 0.5338 | 1.0 | Thanks, Cindy, and good afternoon, everyone. We delivered outstanding results this year driven by our focus on exceptio… |
| 2 | `q7ebef55d671d:chunk-61` | 0.4012 |  | Yes. So great question. Here's what I'll tell you is, for sure, you've got to be staffed, you got to have stability in … |
| 3 | `q7ebef55d671d:chunk-59` | 0.3425 |  | A couple of follow-up questions. The first is I wanted to go back to your comment about restaurants that for the makeli… |
| 4 | `q7ebef55d671d:chunk-35` | 0.1973 |  | Yes. Well, obviously, we're really delighted to see over 7 points of transaction growth in the fourth quarter. I think … |
| 5 | `q7ebef55d671d:chunk-53` | 0.08360000000000001 |  | I was thinking about the amount of time, attention, labor hours that you spend in morning prep every day at the store l… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q7ebef55d671d`)._

### ex-dev-q7ed5279a28b4

- **example_id**: `dev:q7ed5279a28b4`
- **state**: `completed`
- **query**: What did Teradyne’s management note about Teradyne’s operational scalability as test equipment demand volumes grow or contract?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-Q', '10-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.27541155237618664 · skipped= · n_scored=156

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ed5279a28b4:chunk-104` | 0.1455 | 1.0 | Item 2: Management’s Discussion and Analysis of Financial Condition and Results of Operations Statements in this Quarte… |
| 2 | `q7ed5279a28b4:chunk-127` | 0.0041 |  | The decrease in Semiconductor Test revenues of $211.8 million or 13.2%, was driven primarily by lower tester sales for … |
| 3 | `q7ed5279a28b4:chunk-125` | 0.004 |  | (1)Included in Corporate and Eliminations are interest income, interest expense, net foreign exchange gains (losses), i… |
| 4 | `q7ed5279a28b4:chunk-142` | 0.0025 |  | The decrease in income before income taxes in Semiconductor Test was driven primarily by lower tester sales for mobilit… |
| 5 | `q7ed5279a28b4:chunk-16` | 0.0019 |  | TERADYNE, INC. NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS (Unaudited) A. THE COMPANY Teradyne, Inc. (“Teradyn… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q7ed5279a28b4`)._

### ex-dev-q811679c2d742

- **example_id**: `dev:q811679c2d742`
- **state**: `completed`
- **query**: What challenges are noted regarding scaling infrastructure or capacity for renewable energy integration to meet growth?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', '8-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q811679c2d742:chunk-105` | 0.9338 | 2.0 | If approved by the CPUC, Xcel Energy expects to invest $7.9 billion in generation resources. In addition, the plan requ… |
| 2 | `q811679c2d742:chunk-107` | 0.8971 | 2.0 | New Technology and Government Grants Hydrogen Hub Grant In October 2023, the DOE selected the Heartland Hydrogen Hub, i… |
| 3 | `q811679c2d742:chunk-106` | 0.8872 | 2.0 | Colorado Legislation — In May 2023, Colorado Senate Bill 23-291 passed and was signed into law. The bill includes a num… |
| 4 | `q811679c2d742:chunk-103` | 0.6894 | 1.0 | In September 2023, NSP-Wisconsin filed rebuttal testimony and updated its request for depreciation life extensions and … |
| 5 | `q811679c2d742:chunk-129` | 0.36429999999999996 | 1.0 | The base plan does not include any potential renewable generation assets associated with the Colorado recommended Prefe… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q811679c2d742`)._

### ex-dev-q84038a74fd59

- **example_id**: `dev:q84038a74fd59`
- **state**: `completed`
- **query**: How many organizations were reported to be using Azure OpenAI Service
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9871901582936081 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '8-K', '10-Q', 'DEF14A', '10-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=76

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q84038a74fd59:chunk-5` | 1.2127 | 2.0 | Thank you very much, Brett. We had a solid close to our fiscal year. The Microsoft Cloud surpassed $110 billion in annu… |
| 2 | `q84038a74fd59:chunk-61` | 0.1043 |  | Yes. I mean the thing that we are both seeing and excited about is both the new workloads. I mean if you think about Az… |
| 3 | `q84038a74fd59:chunk-33` | 0.0628 |  | Yes. And I think just for perspective, I think it's sort of always good to think about it, right, where we have, what, … |
| 4 | `q84038a74fd59:chunk-15` | 0.0597 |  | Thank you, Keith, for the question. The fundamental guidance and conversation that we have with customers is twofold. O… |
| 5 | `q84038a74fd59:chunk-7` | 0.045 |  | Thank you, Satya, and good afternoon, everyone. This quarter, revenue was $56.2 billion, up 8% and 10% in constant curr… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q84038a74fd59`)._

### ex-dev-q86f79f57d973

- **example_id**: `dev:q86f79f57d973`
- **state**: `completed`
- **query**: What did Linde’s leadership say about Linde’s dividend policy or share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '8-K', '10-Q']`
- **yield**: original=`DEF14A` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.8453596772450139 · skipped= · n_scored=287

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q86f79f57d973:chunk-64` | 1.1334 | 2.0 | Table of Contents Investing Net cash used for investing activities was $4,670 million in 2023 compared to $3,088 millio… |
| 2 | `q86f79f57d973:chunk-15` | 1.0393 | 2.0 | (1)On February 28, 2022 the company's board of directors approved the repurchase of $10.0 billion of its ordinary share… |
| 3 | `q86f79f57d973:chunk-202` | 1.035 | 2.0 | Table of Contents valuation, Linde uses the net asset value received as part of the fund's quarterly reporting, which f… |
| 4 | `q86f79f57d973:chunk-107` | 0.6151 | 1.0 | ##################Linde plc Shareholders’ Equity######################## ####Ordinary shares########Additional Paid-in … |
| 5 | `q86f79f57d973:chunk-204` | 0.0363 |  | Table of Contents NOTE 15. SHARE-BASED COMPENSATION Share-based compensation expense was $141 million in 2023 ($107 mil… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q86f79f57d973`)._

### ex-dev-q88819064dbb7

- **example_id**: `dev:q88819064dbb7`
- **state**: `completed`
- **query**: What investor views emerged on Dollar Tree, Inc.’s geographic expansion prospects within the domestic discount retail market?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.5958337834156117 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88819064dbb7:chunk-27` | 1.252 | 1.0 | Yes. Dollar Tree, the fastest-growing demographic is north of $125,000 a year in income, which brings a lot more firepo… |
| 2 | `q88819064dbb7:chunk-45` | 1.0442 | 1.0 | Yes. Great questions. First thing I'll say to you, John, is we will stagger the rollout. I like to spread an initiative… |
| 3 | `q88819064dbb7:chunk-5` | 0.985 | 1.0 | Thanks, Bob. Good morning, everyone. This past year, our organization made meaningful progress in the ongoing transform… |
| 4 | `q88819064dbb7:chunk-7` | 0.7839 | 1.0 | Thank you, Rick, and good morning. I will first discuss our fourth quarter results. After which, I'll provide some deta… |
| 5 | `q88819064dbb7:chunk-55` | 0.7411 | 1.0 | Two great questions. As far as rebannering, we've already looked at a modest number of stores that we intend to do that… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q88819064dbb7`)._

### ex-dev-q88db5d96c8dd

- **example_id**: `dev:q88db5d96c8dd`
- **state**: `completed`
- **query**: How does Bristol-Myers Squibb manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.8347911247384279 · skipped= · n_scored=176

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88db5d96c8dd:chunk-166` | 1.0043 | 2.0 | (a)Includes shares repurchased as part of publicly announced programs and shares of common stock surrendered to the Com… |
| 2 | `q88db5d96c8dd:chunk-87` | 0.9582999999999999 | 1.0 | ####Common Stock########Capital in Excess of Par Value of Stock####Accumulated Other Comprehensive Loss####Retained Ear… |
| 3 | `q88db5d96c8dd:chunk-40` | 0.631 | 1.0 | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### Dollars in millions, except per sha… |
| 4 | `q88db5d96c8dd:chunk-102` | 0.1371 |  | Dollars in millions####Restricted Stock Units####Market Share Units####Performance Share Units Unrecognized compensatio… |
| 5 | `q88db5d96c8dd:chunk-101` | 0.0886 |  | Units in millions##Units####Weighted-Average Fair Value Restricted stock units##9.3##$##60.52 Market share units##1.0##… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q88db5d96c8dd`)._

### ex-dev-q89953a08e494

- **example_id**: `dev:q89953a08e494`
- **state**: `completed`
- **query**: How does Globe Life Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.7919648107385373 · skipped= · n_scored=125

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89953a08e494:chunk-8` | 1.0112 | 2.0 | # Executive Compensation Highlights Our executive compensation programs are designed to motivate the achievement of our… |
| 2 | `q89953a08e494:chunk-67` | 0.8591 | 2.0 | # Assessment of 2023 Advisory Vote on Executive Compensation (cont.) ## Long-Term Equity Incentives (cont.) The 2018 Pl… |
| 3 | `q89953a08e494:chunk-69` | 0.611 |  | # Stock Ownership/Retention Guidelines (cont.) The directors, Co-CEOs and other officers who are subject to the above-d… |
| 4 | `q89953a08e494:chunk-86` | 0.5136 | 1.0 | # OUTSTANDING EQUITY AWARDS AT FISCAL YEAR-END 2023 (continued) (cont.) - 1 Stock options vest at the rate of 50% on se… |
| 5 | `q89953a08e494:chunk-66` | 0.4602 | 1.0 | # Assessment of 2023 Advisory Vote on Executive Compensation (cont.) ## Long-Term Equity Incentives We award long-term … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q89953a08e494`)._

### ex-dev-q89fb186f5e49

- **example_id**: `dev:q89fb186f5e49`
- **state**: `completed`
- **query**: What investor views emerged on Linde’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.34519134224686937 · skipped= · n_scored=287

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89fb186f5e49:chunk-113` | 0.6704 |  | Table of Contents NOTE 2. Acquisitions and Divestitures Acquisitions Acquisitions were $953 million, $110 million and $… |
| 2 | `q89fb186f5e49:chunk-1` | 0.6578999999999999 | 1.0 | Table of Contents adjacent to these customers’ sites and supplies the product directly to customers by pipeline. On-sit… |
| 3 | `q89fb186f5e49:chunk-22` | 0.2767 |  | Table of Contents BUSINESS OVERVIEW The company's primary products in its industrial gases business are atmospheric gas… |
| 4 | `q89fb186f5e49:chunk-31` | 0.1763 |  | 2023 Compared With 2022 Sales Linde sales decreased $510 million, or 2%, for the 2023 year versus 2022. Higher pricing … |
| 5 | `q89fb186f5e49:chunk-5` | 0.1649 | 1.0 | Table of Contents ITEM 1A. RISK FACTORS Due to the size and geographic reach of the company’s operations, a wide range … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q89fb186f5e49`)._

### ex-dev-q8b55a229e784

- **example_id**: `dev:q8b55a229e784`
- **state**: `completed`
- **query**: How has the ratio of C.H. Robinson Worldwide’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.6885288809404666 · gold=['10-K', '10-Q']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-K` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=112

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8b55a229e784:chunk-41` | 0.384 | 1.0 | NOTE 9. REVENUE FROM CONTRACTS WITH CUSTOMERS A summary of our total revenues disaggregated by major service line and t… |
| 2 | `q8b55a229e784:chunk-80` | 0.0615 |  | MARKET TRENDS Carrier capacity during the third quarter of 2023 in the North America surface transportation market cont… |
| 3 | `q8b55a229e784:chunk-84` | 0.0453 |  | A reconciliation of our reportable segments to our consolidated results can be found in Note 8, Segment Reporting, in P… |
| 4 | `q8b55a229e784:chunk-95` | 0.0348 |  | ________________________________ (1) Adjusted gross profit margin is a non-GAAP financial measure explained above. Thre… |
| 5 | `q8b55a229e784:chunk-93` | 0.0276 |  | Nine Months Ended September 30, 2023, Compared to the Nine Months Ended September 30, 2022 Total revenues and direct co… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q8b55a229e784`)._

### ex-dev-q8ba6a388d681

- **example_id**: `dev:q8ba6a388d681`
- **state**: `completed`
- **query**: What questions were asked about Broadcom’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '8-K', '10-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.8318724637288826 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8ba6a388d681:chunk-101` | 0.6567 | 1.0 | Hock, in the past, I think we've all been aware that there's one major customer on the accelerated compute side, I susp… |
| 2 | `q8ba6a388d681:chunk-95` | 0.5825 | 1.0 | Hock, I guess I'll caveat my question saying that I'm a semiconductor guy rather than a software expert. But I wanted t… |
| 3 | `q8ba6a388d681:chunk-51` | 0.4135 | 1.0 | I mean you did say 65% on it. I think I recall you saying you were going to run VMware at 65%. So I guess, 65% is the r… |
| 4 | `q8ba6a388d681:chunk-5` | 0.161 |  | Thank you, Ji, and thank you, everyone, for joining us today. In our fiscal Q4 '23, consolidated net revenue was $9.3 b… |
| 5 | `q8ba6a388d681:chunk-109` | 0.0756 |  | Well, over the past 18 months almost, we had on the journey of closing this deal from the date of announcement. You're … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q8ba6a388d681`)._

### ex-dev-q8cc1033cf552

- **example_id**: `dev:q8cc1033cf552`
- **state**: `completed`
- **query**: What guidance did The Sherwin-Williams Company’s leadership provide on debt reduction or leverage targets for The Sherwin-Williams Company?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9461356536981058 · gold=['10-K', 'Earnings', '10-Q']
- **S1 ordered**: `['10-K', 'DEF14A', 'Earnings', '8-K', '10-Q']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.8539316501572937 · skipped= · n_scored=114

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8cc1033cf552:chunk-100` | 0.8509 | 1.0 | During the first nine months of 2023, the Company purchased 3.8 million shares of its common stock for treasury purpose… |
| 2 | `q8cc1033cf552:chunk-81` | 0.6298 | 1.0 | Item 2. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS (dollars in millions, exc… |
| 3 | `q8cc1033cf552:chunk-93` | 0.3787 | 1.0 | FINANCIAL CONDITION, LIQUIDITY AND CASH FLOW Overview The Company’s financial condition and liquidity remained strong a… |
| 4 | `q8cc1033cf552:chunk-89` | 0.13440000000000002 |  | Nine Months Ended September 30, 2023 Consolidated cost of goods sold decreased $236.8 million, or 2.4%, in the first ni… |
| 5 | `q8cc1033cf552:chunk-88` | 0.0886 | 1.0 | Three Months Ended September 30, 2023 Consolidated cost of goods sold decreased $257.5 million, or 7.4%, in the third q… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q8cc1033cf552`)._

### ex-dev-q8e053e02a010

- **example_id**: `dev:q8e053e02a010`
- **state**: `completed`
- **query**: What dependency risks exist for International Paper Company due to concentration of revenue in a limited number of end-use paper and packaging markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=225

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8e053e02a010:chunk-1` | 0.0618 |  | # Dear Shareowner, The image shows a professional headshot of a middle-aged man with gray hair and a full gray beard. H… |
| 2 | `q8e053e02a010:chunk-42` | 0.0157 |  | # Corporate Governance / How the Board Operates (cont.) ## Oversight of Succession Planning and Talent Management Our B… |
| 3 | `q8e053e02a010:chunk-23` | 0.004699999999999999 |  | # Our Nominees (cont.) ## Other Affiliations Mr. Connor serves on the board of directors of the Rock & Roll Hall of Fam… |
| 4 | `q8e053e02a010:chunk-140` | 0.0038 |  | # Supplemental (cont.) ## Most Important Performance Measures (cont.) Table of Contents The image shows a close-up view… |
| 5 | `q8e053e02a010:chunk-11` | 0.0027 |  | # Proxy Summary / Our Commitment to Sustainability (cont.) ## Our Approach to Climate We recognize the impacts of clima… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q8e053e02a010`)._

### ex-dev-q8e26f08be2bc

- **example_id**: `dev:q8e26f08be2bc`
- **state**: `completed`
- **query**: What challenges arise for Vertex Pharmaceuticals from data privacy regulations and handling of patient data?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.8403399529073962 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['8-K', '10-K', '10-Q', 'DEF14A', 'Earnings']`
- **yield**: original=`8-K` · effective=`10-K` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=285

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8e26f08be2bc:chunk-52` | 1.1572 | 2.0 | research institution that has not complied with HIPAA’s requirements for disclosing such information. In addition, the … |
| 2 | `q8e26f08be2bc:chunk-61` | 1.1171 | 2.0 | available pool of skilled employees would be further reduced if immigration laws change in a manner that increases rest… |
| 3 | `q8e26f08be2bc:chunk-51` | 1.1134 | 2.0 | governing cell and genetic therapy products have changed frequently and may continue to change in the future. For examp… |
| 4 | `q8e26f08be2bc:chunk-29` | 0.9586 | 2.0 | Many of these laws and regulations contain requirements that are subject to interpretation. Outside the U.S., other cou… |
| 5 | `q8e26f08be2bc:chunk-62` | 0.917 | 2.0 | If our facilities were to experience a catastrophic loss, our operations would be seriously harmed. Most of our operati… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q8e26f08be2bc`)._

### ex-dev-q909c4baef1ee

- **example_id**: `dev:q909c4baef1ee`
- **state**: `completed`
- **query**: How did analysts frame queries about Truist Financial Corporation’s shareholder returns, including dividends?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.6266239202359082 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **yield**: original=`DEF14A` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=124

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q909c4baef1ee:chunk-5` | 0.5465 |  | Thanks, Brad, and good morning, everybody, and thank you for joining our call today. Before we discuss our fourth quart… |
| 2 | `q909c4baef1ee:chunk-9` | 0.1539 |  | Thanks, Mike. So looking back at 2023, I'm really proud of the work our teammates accomplished, which helped accelerate… |
| 3 | `q909c4baef1ee:chunk-63` | 0.0412 |  | The first question is for Bill. Bill, Mike is not saying anything too different about loan growth from the rest of your… |
| 4 | `q909c4baef1ee:chunk-91` | 0.0399 |  | Sorry, I missed it, but have you guys talked about what your targeted capital level is? Obviously, you said going from … |
| 5 | `q909c4baef1ee:chunk-95` | 0.030699999999999998 |  | Okay. And as you think about kind of the 10-plus medium term, is that including AOCI? Because obviously, you're already… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q909c4baef1ee`)._

### ex-dev-q93fb2b2861c4

- **example_id**: `dev:q93fb2b2861c4`
- **state**: `completed`
- **query**: How does Church & Dwight view the pace of product innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9134693626978977 · gold=['10-K', '8-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=208

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q93fb2b2861c4:chunk-21` | 1.2365 | 2.0 | dilutive issuances of new equity by us or the incurrence of additional debt or business acquisition liabilities, or the… |
| 2 | `q93fb2b2861c4:chunk-11` | 1.1999 | 2.0 | COMPETITION We compete in the household and personal care consumer product categories, which are highly innovative cate… |
| 3 | `q93fb2b2861c4:chunk-131` | 0.8698999999999999 | 2.0 | CHURCH & DWIGHT CO., INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – (Continued) (In millions, excep… |
| 4 | `q93fb2b2861c4:chunk-18` | 0.806 | 2.0 | ITEM 1A. RISK FACTORS The following risks and uncertainties, as well as other factors described elsewhere in this Annua… |
| 5 | `q93fb2b2861c4:chunk-43` | 0.7803 | 2.0 | CHURCH & DWIGHT CO., INC AND SUBSIDIARIES (Dollars in millions, except share and per share data) 2023 Financial Highlig… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q93fb2b2861c4`)._

### ex-dev-q95535bca90c9

- **example_id**: `dev:q95535bca90c9`
- **state**: `completed`
- **query**: How did Wells Fargo’s average cost per loan origination trend compared to the prior period?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7085011369669131 · gold=['10-Q', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **yield**: original=`10-K` · effective=`10-Q` · used=True
- **S2**: nDCG@5=0.38685280723454163 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q95535bca90c9:chunk-13` | 0.043199999999999995 |  | Fourth Quarter 2023 vs. Fourth Quarter 2022 ◦Revenue increased 1% ▪Consumer, Small and Business Banking was up 1% drive… |
| 2 | `q95535bca90c9:chunk-12` | 0.0392 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 3 | `q95535bca90c9:chunk-16` | 0.0371 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 4 | `q95535bca90c9:chunk-18` | 0.030600000000000002 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 5 | `q95535bca90c9:chunk-14` | 0.0221 | 1.0 | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q95535bca90c9`)._

### ex-dev-q95790ca7c1f5

- **example_id**: `dev:q95790ca7c1f5`
- **state**: `completed`
- **query**: What did Dayforce Inc.’s leadership say about Dayforce Inc.’s share repurchase plans?
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.4933965394160924 · gold=['10-K', 'Earnings']
- **S1 ordered**: `['8-K', 'Earnings', 'DEF14A', '10-Q', '10-K']`
- **yield**: original=`8-K` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q95790ca7c1f5:chunk-123` | 0.768 |  | We always look at the float as a really nice piece of our business, and we'll take it when it's here. But as it goes aw… |
| 2 | `q95790ca7c1f5:chunk-19` | 0.0379 |  | Yes. Thanks, Scott. It's good to talk to you again. And as I said, it's good to be back. It does kind of feel like comi… |
| 3 | `q95790ca7c1f5:chunk-9` | 0.0086 |  | Thanks, Joe. It feels good to be back. I'm proud of the way our team closed out the year. In Q4, we delivered Dayforce … |
| 4 | `q95790ca7c1f5:chunk-3` | 0.006500000000000001 |  | Thanks, Matt, and thank you all for joining us. Next to me, I have Steve who will review key customer go-lives and sale… |
| 5 | `q95790ca7c1f5:chunk-25` | 0.0025 |  | Thanks, again. Great to speak with you. It's a very valid question. So when I look at the overall company, what I can s… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q95790ca7c1f5`)._

### ex-dev-q9597b3e4d1b2

- **example_id**: `dev:q9597b3e4d1b2`
- **state**: `completed`
- **query**: How has investor sentiment shifted following Archer-Daniels-Midland Company’s most recent earnings release?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.68154288742782 · gold=['10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=158

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9597b3e4d1b2:chunk-3` | 0.0215 |  | # A Letter from the Lead Director (cont.) ## Strong Corporate Governance ADM is governed by a highly engaged and divers… |
| 2 | `q9597b3e4d1b2:chunk-86` | 0.005399999999999999 |  | # COMPENSATION DISCUSSION AND ANALYSIS - Equity-Based Long-Term Incentives (cont.) ## Equity Awards Granted in 2021 wit… |
| 3 | `q9597b3e4d1b2:chunk-148` | 0.0019 |  | # Definition and Reconciliation of Non-GAAP Measures We use Adjusted ROIC to mean "Adjusted ROIC Earnings" divided by "… |
| 4 | `q9597b3e4d1b2:chunk-53` | 0.0019 |  | # CORPORATE GOVERNANCE - Information Concerning Committees and Meetings (cont.) ## EXECUTIVE COMMITTEE The Executive Co… |
| 5 | `q9597b3e4d1b2:chunk-50` | 0.0018000000000000002 |  | # CORPORATE GOVERNANCE - Sustainability and Corporate Responsibility (cont.) ## The Audit Committee reviews: 1. the ove… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q9597b3e4d1b2`)._

### ex-dev-q98c606bb3ce7

- **example_id**: `dev:q98c606bb3ce7`
- **state**: `completed`
- **query**: What litigation or dispute risks did Williams-Sonoma, Inc. identify and what is the potential financial impact for Williams-Sonoma, Inc.?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.6864231448093613 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q98c606bb3ce7:chunk-115` | 1.1896 | 1.0 | Table of Contents contributions were vested immediately. Effective July 2022, all matching contributions become vested … |
| 2 | `q98c606bb3ce7:chunk-15` | 1.1404 | 2.0 | Table of Contents In addition, in the past, we have insourced certain aspects of our business, including certain techno… |
| 3 | `q98c606bb3ce7:chunk-11` | 0.9745 | 2.0 | Table of Contents losses, government-mandated shutdowns, telecommunications failures, hardware and software failures, c… |
| 4 | `q98c606bb3ce7:chunk-23` | 0.7899 | 2.0 | Table of Contents cause delays in locating and shipping products, and increases in costs associated with inventory that… |
| 5 | `q98c606bb3ce7:chunk-6` | 0.7009 | 1.0 | Table of Contents ITEM 1A. RISK FACTORS A description of the risks and uncertainties associated with our business is se… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q98c606bb3ce7`)._

### ex-dev-q99a077efaab0

- **example_id**: `dev:q99a077efaab0`
- **state**: `completed`
- **query**: What dependency risks exist for Align Technology due to concentration of revenue in a limited number of orthodontic practices or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99a077efaab0:chunk-3` | 0.6428 | 1.0 | Thanks, Shirley. Good afternoon, and thanks for joining us. On our call today, I'll provide an overview of our fourth q… |
| 2 | `q99a077efaab0:chunk-117` | 0.191 |  | Yes. I can't -- I really wouldn't break it out between Americas and International because we felt good about the geogra… |
| 3 | `q99a077efaab0:chunk-87` | 0.1252 |  | Michael, this is John. I would say as we look to expand this out, it's been successful every place that we've gone. We'… |
| 4 | `q99a077efaab0:chunk-5` | 0.1009 |  | Thanks, Joe. Now for our Q4 financial results. Total revenues for the fourth quarter were $956.7 million, down 0.4% fro… |
| 5 | `q99a077efaab0:chunk-7` | 0.0454 |  | Thanks, John. In closing, while I'm pleased with our better-than-expected fourth quarter results and start to the year,… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q99a077efaab0`)._

### ex-dev-q99ec5f1aeea5

- **example_id**: `dev:q99ec5f1aeea5`
- **state**: `completed`
- **query**: What questions were asked about Federal Realty Investment Trust’s tenant retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9134693626978977 · gold=['Earnings', '8-K', '10-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=64

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99ec5f1aeea5:chunk-6` | 0.3566 |  | Occupancy The portfolio was 92.2% occupied and 94.2% leased as of December 31, 2023. Additionally, our comparable resid… |
| 2 | `q99ec5f1aeea5:chunk-4` | 0.0383 |  | Federal Realty Investment Trust Announces Operating Results for the Year and Quarter Ended December 31, 2023 NORTH BETH… |
| 3 | `q99ec5f1aeea5:chunk-51` | 0.0315 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 4 | `q99ec5f1aeea5:chunk-63` | 0.0154 |  | Funds From Operations (FFO): FFO is a supplemental measure of real estate companies' operating performances. NAREIT def… |
| 5 | `q99ec5f1aeea5:chunk-56` | 0.0126 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q99ec5f1aeea5`)._

### ex-dev-q9a5cfe35fecd

- **example_id**: `dev:q9a5cfe35fecd`
- **state**: `completed`
- **query**: What dependency risks exist for CMS Energy Corporation due to concentration of revenue in a limited number of geographic regions or key utility customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.9125299483251055 · skipped= · n_scored=194

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9a5cfe35fecd:chunk-19` | 0.8137 | 2.0 | •the investment performance of the assets of CMS Energy’s and Consumers’ pension and benefit plans, the discount rates,… |
| 2 | `q9a5cfe35fecd:chunk-24` | 0.7692 | 2.0 | CMS Energy Corporation Consumers Energy Company Management’s Discussion and Analysis of Financial Condition and Results… |
| 3 | `q9a5cfe35fecd:chunk-64` | 0.6509 | 2.0 | •purchase of a 166‐MW wind generation project in Hillsdale, Michigan; the project became operational and Consumers took… |
| 4 | `q9a5cfe35fecd:chunk-166` | 0.5811000000000001 | 2.0 | 1Amounts represent NorthStar Clean Energy’s operating revenue from independent power production and its sales of energy… |
| 5 | `q9a5cfe35fecd:chunk-167` | 0.43720000000000003 | 1.0 | product comprising the commodity, electricity or natural gas, and the service of delivering such commodity. In some ins… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q9a5cfe35fecd`)._

### ex-dev-q9c255237096a

- **example_id**: `dev:q9c255237096a`
- **state**: `completed`
- **query**: What perquisites or fringe benefits are included in The AES Corporation’s executive compensation disclosures?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=1.0 · gold=['DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **yield**: original=`DEF14A` · effective=`DEF14A` · used=False
- **S2**: nDCG@5=0.6534081967245269 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9c255237096a:chunk-54` | 1.2027 | 2.0 | # Three-Year CEO LTC Realizable Pay <table> <tr> <th>Year</th> <th>Type</th> <th>RSU</th> <th>PSU</th> <th>PCU</th> <th… |
| 2 | `q9c255237096a:chunk-40` | 1.1821 | 2.0 | # EXECUTIVE COMPENSATION COMPENSATION DISCUSSION AND ANALYSIS ("CD&A") (cont.) ## What AES Does ## What AES Doesn't Do … |
| 3 | `q9c255237096a:chunk-44` | 1.1383 | 1.0 | # Overview of AES Total Compensation ## Elements of Compensation The following table presents each element of compensat… |
| 4 | `q9c255237096a:chunk-67` | 1.0758 |  | # 2023 Option Exercises and Stock Vested (cont.) ## 2023 Non-Qualified Deferred Compensation The following table contai… |
| 5 | `q9c255237096a:chunk-68` | 1.0426 | 1.0 | # 2023 Option Exercises and Stock Vested (cont.) ## Narrative Disclosure Relating to the Non-Qualified Deferred Compens… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q9c255237096a`)._

### ex-dev-q9dd3907388e3

- **example_id**: `dev:q9dd3907388e3`
- **state**: `completed`
- **query**: How does Duke Energy view the pace of innovation cycles in renewable energy technologies and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9dd3907388e3:chunk-6` | 0.276 | 1.0 | ◦The ability to implement our business strategy, including our carbon emission reduction goals; ◦State, federal and for… |
| 2 | `q9dd3907388e3:chunk-5` | 0.0908 |  | The most directly comparable GAAP measure for adjusted segment income or adjusted other net loss is segment income and … |
| 3 | `q9dd3907388e3:chunk-0` | 0.06 |  | News Release Media Contact: Gillian Moore 24-Hour: 800.559.3853 Analyst Contact: Abby Motsinger Office: 704.382.7624 Au… |
| 4 | `q9dd3907388e3:chunk-7` | 0.003 |  | ◦The influence of weather and other natural phenomena on operations, including the economic, operational and other effe… |
| 5 | `q9dd3907388e3:chunk-33` | 0.0016 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3"></td><td></… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q9dd3907388e3`)._

### ex-dev-q9f32df79b0d7

- **example_id**: `dev:q9f32df79b0d7`
- **state**: `completed`
- **query**: How does Capital One view the pace of digital banking innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=4

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9f32df79b0d7:chunk-0` | 0.2719 | 1.0 | Exhibit 99.1 News Release <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><… |
| 2 | `q9f32df79b0d7:chunk-1` | 0.0023 |  | •Total net revenue increased 4 percent to $9.4 billion. •Total non-interest expense increased 1 percent to $4.9 billion… |
| 3 | `q9f32df79b0d7:chunk-3` | 0.0011 |  | Capital One Financial Corporation (www.capitalone.com) is a financial holding company which, along with its subsidiarie… |
| 4 | `q9f32df79b0d7:chunk-2` | 0.0002 |  | •Auto average loans decreased $493 million, or 1 percent, to $75.7 billion. ◦Commercial Banking average loans decreased… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:q9f32df79b0d7`)._

### ex-dev-qa057a3d428a2

- **example_id**: `dev:qa057a3d428a2`
- **state**: `completed`
- **query**: What dependency risks exist for McKesson Corporation due to concentration of revenue in a limited number of pharmaceutical manufacturers or healthcare providers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.6061680178534535 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa057a3d428a2:chunk-92` | 0.7384000000000001 | 2.0 | McKESSON CORPORATION FINANCIAL NOTES (CONCLUDED) (UNAUDITED) (3)The Company’s U.S. Pharmaceutical segment’s operating p… |
| 2 | `qa057a3d428a2:chunk-114` | 0.5257000000000001 | 2.0 | MD&A Index McKESSON CORPORATION FINANCIAL REVIEW (CONTINUED) (UNAUDITED) •cash receipts for our share of antitrust lega… |
| 3 | `qa057a3d428a2:chunk-98` | 0.3713 |  | MD&A Index McKESSON CORPORATION FINANCIAL REVIEW (CONTINUED) (UNAUDITED) Opioid-Related Litigation and Claims As descri… |
| 4 | `qa057a3d428a2:chunk-89` | 0.2699 |  | McKESSON CORPORATION FINANCIAL NOTES (CONTINUED) (UNAUDITED) The RxTS segment helps solve medication access, affordabil… |
| 5 | `qa057a3d428a2:chunk-110` | 0.2696 |  | Any percentage changes displayed above which are not meaningful are displayed as zero percent. U.S. Pharmaceutical Thre… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qa057a3d428a2`)._

### ex-dev-qa33b36ffd2c1

- **example_id**: `dev:qa33b36ffd2c1`
- **state**: `completed`
- **query**: How has Garmin’s fitness segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7146598531416503 · gold=['10-Q', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-Q` · used=True
- **S2**: nDCG@5=0.9125299483251055 · skipped= · n_scored=169

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa33b36ffd2c1:chunk-51` | 1.2097 | 2.0 | Operating Income (Loss)####52-Weeks Ended December 30, 2023####Year-over-Year Change######53-Weeks Ended December 31, 2… |
| 2 | `qa33b36ffd2c1:chunk-46` | 1.1944 | 2.0 | Gross Profit####52-Weeks Ended December 30, 2023####Year-over-Year Change######53-Weeks Ended December 31, 2022####Year… |
| 3 | `qa33b36ffd2c1:chunk-47` | 1.1112 | 2.0 | Gross profit dollars in fiscal year 2023 increased 7%, primarily due to the increase in net sales compared to the year-… |
| 4 | `qa33b36ffd2c1:chunk-147` | 0.3225 | 2.0 | As indicated in Note 1 of the Notes to Consolidated Financial Statements, the Company announced an organization realign… |
| 5 | `qa33b36ffd2c1:chunk-146` | 0.084 | 1.0 | The weighted-average remaining contract life of restricted stock units at December 30, 2023 was 1.36 years. The total f… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qa33b36ffd2c1`)._

### ex-dev-qa5c748248a5b

- **example_id**: `dev:qa5c748248a5b`
- **state**: `completed`
- **query**: How has the ratio of MSCI’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-Q', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5=0.21826955258437686 · skipped= · n_scored=255

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa5c748248a5b:chunk-94` | 1.0728 | 1.0 | Total Run Rate increased 15.8% for the year ended December 31, 2023, driven by a 16.0% increase from recurring subscrip… |
| 2 | `qa5c748248a5b:chunk-4` | 0.7424999999999999 |  | •MSCI Global Thematic Rotation Index. The MSCI Global Thematic Rotation Index aims to represent the performance of the … |
| 3 | `qa5c748248a5b:chunk-115` | 0.5979000000000001 | 1.0 | Because of its inherent limitations, internal control over financial reporting may not prevent or detect misstatements.… |
| 4 | `qa5c748248a5b:chunk-42` | 0.5153 | 1.0 | Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations The following Management’… |
| 5 | `qa5c748248a5b:chunk-139` | 0.4949 |  | Accrued Compensation A significant portion of the Company’s employee incentive compensation programs are discretionary.… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qa5c748248a5b`)._

### ex-dev-qa602975e3d19

- **example_id**: `dev:qa602975e3d19`
- **state**: `completed`
- **query**: How has the ratio of Mondelez International’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9411655511901171 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5=0.6309297535714574 · skipped= · n_scored=189

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa602975e3d19:chunk-62` | 0.1076 |  | # COMPENSATION DISCUSSION AND ANALYSIS (CD&A) (cont.) ## Net Revenues ## Cash Flow Reported Net Revenues Growth +14.4% … |
| 2 | `qa602975e3d19:chunk-163` | 0.0708 | 2.0 | # Back to Contents (cont.) ## Back to Contents tax obligations under the enacted tax law changes. Refer to Note 16, Inc… |
| 3 | `qa602975e3d19:chunk-157` | 0.0497 |  | # ANNEX A: FINANCIAL MEASURES DEFINITIONS We report our financial results in accordance with U.S. GAAP. However, we use… |
| 4 | `qa602975e3d19:chunk-161` | 0.029199999999999997 |  | # Back to Contents (cont.) (7) Acquisition integration costs and contingent consideration adjustments include one-time … |
| 5 | `qa602975e3d19:chunk-160` | 0.007500000000000001 |  | # Back to Contents (cont.) (1) Divestitures include completed sales of businesses, exits of major product lines upon co… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qa602975e3d19`)._

### ex-dev-qa9744c8552ed

- **example_id**: `dev:qa9744c8552ed`
- **state**: `completed`
- **query**: How did analysts question TJX Companies’ management on their strategies for responsible sourcing and sustainable supply chain practices?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6729475164829866 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=0.6843515475204855 · skipped= · n_scored=119

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa9744c8552ed:chunk-105` | 0.8498 | 1.0 | # REPORT ON EFFECTIVENESS OF SOCIAL COMPLIANCE EFFORTS IN TJX'S SUPPLY CHAIN (cont.) ## Assessing Due Diligence on Huma… |
| 2 | `qa9744c8552ed:chunk-21` | 0.7935 | 1.0 | # ENGAGING WITH SHAREHOLDERS (cont.) ## ONGOING SHAREHOLDER ENGAGEMENT ## Topics of engagement ## Role of engagement ##… |
| 3 | `qa9744c8552ed:chunk-110` | 0.6462 |  | # STATEMENT OF THE BOARD OF DIRECTORS IN RESPONSE TO PROPOSAL 4 (cont.) ## Shareholder Proposals (cont.) - Training: We… |
| 4 | `qa9744c8552ed:chunk-104` | 0.5683 |  | # SHAREHOLDER PROPOSALS ## SHAREHOLDER PROPOSAL ENGAGEMENT We value year-round engagement with our shareholders and oth… |
| 5 | `qa9744c8552ed:chunk-106` | 0.5552 | 1.0 | # STATEMENT OF THE BOARD OF DIRECTORS IN RESPONSE TO PROPOSAL 4 The Board of Directors carefully considered this shareh… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qa9744c8552ed`)._

### ex-dev-qab00fabe02dc

- **example_id**: `dev:qab00fabe02dc`
- **state**: `completed`
- **query**: How did Rockwell Automation’s executives address regulatory or policy developments and their potential implications for industrial automation solutions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7083232243990188 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **yield**: original=`10-K` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.8318724637288826 · skipped= · n_scored=112

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qab00fabe02dc:chunk-9` | 0.8645 | 1.0 | # PROXY STATEMENT (cont.) ## ROCKWELL AUTOMATION OVERVIEW We are a global leader in industrial automation and digital t… |
| 2 | `qab00fabe02dc:chunk-31` | 0.5763 | 1.0 | # ELECTION OF DIRECTORS BOARD OF DIRECTORS (cont.) ## Relevance to Rockwell Automation's Strategy (cont.) Relevant Tech… |
| 3 | `qab00fabe02dc:chunk-25` | 0.4752 | 1.0 | # BOARD PROCESSES (cont.) ## CORPORATE GOVERNANCE REVIEW The Board reviewed its Guidelines on Corporate Governance, inc… |
| 4 | `qab00fabe02dc:chunk-1` | 0.1612 |  | # MESSAGE FROM OUR CHAIRMAN, PRESIDENT AND CHIEF EXECUTIVE OFFICER (cont.) ## Dear Fellow Shareowners: Our focus on sup… |
| 5 | `qab00fabe02dc:chunk-13` | 0.1248 |  | # BOARD'S ROLE AND RESPONSIBILITIES (cont.) ## TECHNOLOGY COMMITTEE - Receives regular reports on management policies a… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qab00fabe02dc`)._

### ex-dev-qaf55b76bfcad

- **example_id**: `dev:qaf55b76bfcad`
- **state**: `completed`
- **query**: Which partnership with a major telecommunications provider was highlighted for bundling offers
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '8-K', '10-Q', 'DEF14A', '10-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qaf55b76bfcad:chunk-15` | 0.7046 | 2.0 | Thanks, Michael. Regarding Charter, first of all, as we said when we did the deal, we think it's a great deal for us. I… |
| 2 | `qaf55b76bfcad:chunk-27` | 0.0851 |  | I'll take the question about ESPN first. Interesting, I just saw statistics. ESPN is the #1 brand on TikTok, not the #1… |
| 3 | `qaf55b76bfcad:chunk-53` | 0.0784 |  | Sorry. Sorry, Phil. I was listening to your second question. I forgot your first one. Senior moment. What basically we'… |
| 4 | `qaf55b76bfcad:chunk-5` | 0.039599999999999996 |  | Thanks, Alexia, and good afternoon, everyone. Before we begin, this week, we announced that Hugh Johnston will be joini… |
| 5 | `qaf55b76bfcad:chunk-21` | 0.0297 |  | I'll take the second part first. Our plan when we bring ESPN direct to consumer, which is inevitable, which is going to… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qaf55b76bfcad`)._

### ex-dev-qb00e9c27fd32

- **example_id**: `dev:qb00e9c27fd32`
- **state**: `completed`
- **query**: How has Monster Beverage Corporation’s segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.9322978750325865 · skipped= · n_scored=64

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb00e9c27fd32:chunk-7` | 1.1897 | 2.0 | Thank you, Tom. The company achieved record fourth quarter net sales of $1.73 billion in the 2023 fourth quarter, 14.4%… |
| 2 | `qb00e9c27fd32:chunk-13` | 1.1206 | 1.0 | So I think at the investor meeting, as I recall, we already spoke about 2023 Q4. As you know, we don't give guidance, a… |
| 3 | `qb00e9c27fd32:chunk-53` | 0.9264 | 2.0 | We've always spoken about the fact that internationally, we compete very strongly against -- in the main Red Bull. And … |
| 4 | `qb00e9c27fd32:chunk-25` | 0.789 | 1.0 | No, the only structural reason is we don't give guidance. So that's the only structural reason I can think of. Obviousl… |
| 5 | `qb00e9c27fd32:chunk-51` | 0.7354 | 2.0 | I wanted to go back to international because I feel like it's one of those things that doesn't get the credit that's du… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qb00e9c27fd32`)._

### ex-dev-qb2123a701a82

- **example_id**: `dev:qb2123a701a82`
- **state**: `completed`
- **query**: How does Atmos Energy view the pace of pipeline technology innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6388967123938784 · gold=['DEF14A', '8-K', '10-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=83

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb2123a701a82:chunk-4` | 0.0738 |  | # About Atmos Energy Atmos Energy Corporation, an S&P 500 company headquartered in Dallas, is the country's largest nat… |
| 2 | `qb2123a701a82:chunk-10` | 0.0007 |  | # Nominees for Director (cont.) ## QUALIFICATIONS Mr. Akers has more than 35 years' experience in the natural gas indus… |
| 3 | `qb2123a701a82:chunk-13` | 0.0007 |  | # Nominees for Director (cont.) ## PROFESSIONAL BACKGROUND - Founder and Managing Member of Amichel, LLC, a natural res… |
| 4 | `qb2123a701a82:chunk-19` | 0.0007 |  | # Board Succession Planning ## Identifying and Evaluating Nominees for Directors The Nominating Committee is primarily … |
| 5 | `qb2123a701a82:chunk-21` | 0.0002 |  | # Risk Management (cont.) ## CEO and Management Succession Planning The Board is actively engaged and involved in succe… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qb2123a701a82`)._

### ex-dev-qb22cbf2f4782

- **example_id**: `dev:qb22cbf2f4782`
- **state**: `completed`
- **query**: How has Apple management recently commented on services attach rates and other value-added offerings?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.631251450669265 · gold=['10-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=156

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb22cbf2f4782:chunk-23` | 0.196 |  | Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations The following discussion … |
| 2 | `qb22cbf2f4782:chunk-1` | 0.1349 |  | Services Advertising The Company’s advertising services include third-party licensing arrangements and the Company’s ow… |
| 3 | `qb22cbf2f4782:chunk-29` | 0.1271 |  | (1)Products net sales include amortization of the deferred value of unspecified software upgrade rights, which are bund… |
| 4 | `qb22cbf2f4782:chunk-2` | 0.0863 |  | The Company’s ability to compete successfully depends heavily on ensuring the continuing and timely introduction of inn… |
| 5 | `qb22cbf2f4782:chunk-9` | 0.0736 |  | The Company distributes third-party applications for its products through the App Store. For the vast majority of appli… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qb22cbf2f4782`)._

### ex-dev-qb26bf8457b0f

- **example_id**: `dev:qb26bf8457b0f`
- **state**: `completed`
- **query**: What risks are associated with opening new healthcare facilities for Universal Health Services, Inc. when patient demand is uncertain?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7860353577841278 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.7020976466720956 · skipped= · n_scored=290

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb26bf8457b0f:chunk-2` | 0.8012 | 2.0 | general and local economic conditions, market penetration of managed care programs, the degree of outpatient use, the a… |
| 2 | `qb26bf8457b0f:chunk-21` | 0.7702 | 2.0 | The impact of the COVID-19 pandemic, which began during the second half of March, 2020, has had a material effect on ou… |
| 3 | `qb26bf8457b0f:chunk-28` | 0.7475999999999999 | 1.0 | we are particularly susceptible to revenue loss, cost increase, or damage caused by severe weather conditions or natura… |
| 4 | `qb26bf8457b0f:chunk-1` | 0.7396 | 1.0 | Our Mission Our company mission is: To provide superior quality healthcare services that PATIENTS recommend to families… |
| 5 | `qb26bf8457b0f:chunk-18` | 0.6576 | 1.0 | levels of reimbursement for healthcare services. Payments from federal and state government programs are subject to sta… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qb26bf8457b0f`)._

### ex-dev-qb35a5efa65ce

- **example_id**: `dev:qb35a5efa65ce`
- **state**: `completed`
- **query**: What dependency risks exist for Evergy, Inc. due to concentration of revenue in a limited number of service territories or key industrial customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'Earnings', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.9402694138204842 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb35a5efa65ce:chunk-7` | 1.178 | 2.0 | Thanks, David, and good morning, everyone. Turning to Slide 14, I'll start with a review of our results for the fourth … |
| 2 | `qb35a5efa65ce:chunk-5` | 0.6910000000000001 | 2.0 | Thanks, Pete, and good morning, everyone. Before we begin, we'd like to extend our deepest sympathies to the family of … |
| 3 | `qb35a5efa65ce:chunk-41` | 0.5909 | 2.0 | In terms of earnings sensitivity, I wouldn't call it linear from that perspective. These are obviously large industrial… |
| 4 | `qb35a5efa65ce:chunk-75` | 0.5623 |  | What I'll expand is what rates negotiated, of course, very large loads get special contracts. I think the best way to d… |
| 5 | `qb35a5efa65ce:chunk-73` | 0.2034 | 1.0 | Very -- just one quick follow-up question from Paul Fremont's on the Slide 9, just as opposed to the earnings impact as… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qb35a5efa65ce`)._

### ex-dev-qb500a9b42ef8

- **example_id**: `dev:qb500a9b42ef8`
- **state**: `completed`
- **query**: How has the ratio of CMS Energy Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9452713619732751 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=488

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb500a9b42ef8:chunk-38` | 0.1059 |  | Table of Contents Part I Item 1. Business General CMS Energy CMS Energy was formed as a corporation in Michigan in 1987… |
| 2 | `qb500a9b42ef8:chunk-393` | 0.0839 |  | Table of Contents In some instances, Consumers has specific fixed-term contracts with large commercial and industrial c… |
| 3 | `qb500a9b42ef8:chunk-224` | 0.0364 |  | Table of Contents 1The MPSC has provided a specific return on these regulatory assets. 2These regulatory assets have ar… |
| 4 | `qb500a9b42ef8:chunk-144` | 0.0133 |  | Table of Contents As a result of requests for proposals, Consumers has entered into PPAs to purchase renewable capacity… |
| 5 | `qb500a9b42ef8:chunk-392` | 0.0066 |  | 1Amounts represent NorthStar Clean Energy’s operating revenue from independent power production and its sales of energy… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qb500a9b42ef8`)._

### ex-dev-qb590e4e6d1ec

- **example_id**: `dev:qb590e4e6d1ec`
- **state**: `completed`
- **query**: How has the ratio of PG&E Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5=0.3295833540079424 · skipped= · n_scored=213

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb590e4e6d1ec:chunk-11` | 0.9304 | 1.0 | The Utility’s electric and natural gas operating revenues that impacted earnings increased by $977 million, or 9%, in t… |
| 2 | `qb590e4e6d1ec:chunk-96` | 0.1023 | 1.0 | NOTES TO THE CONDENSED CONSOLIDATED FINANCIAL STATEMENTS NOTE 1: ORGANIZATION AND BASIS OF PRESENTATION Organization an… |
| 3 | `qb590e4e6d1ec:chunk-37` | 0.09830000000000001 |  | Between August 2021 and January 2022, the Utility served various updates to its 2023 GRC testimony. On February 25, 202… |
| 4 | `qb590e4e6d1ec:chunk-2` | 0.0684 |  | The Utility will be permitted to recover its wildfire-related claims in excess of insurance and legal fees through rate… |
| 5 | `qb590e4e6d1ec:chunk-97` | 0.030000000000000002 |  | The Utility also collects additional revenue requirements to recover costs that the CPUC has authorized the Utility to … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qb590e4e6d1ec`)._

### ex-dev-qba0102803c57

- **example_id**: `dev:qba0102803c57`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Kimco Realty Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.7860137352654724 · skipped= · n_scored=332

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba0102803c57:chunk-105` | 0.3163 | 1.0 | Report of Independent Registered Public Accounting Firm To the Member of Kimco Realty OP, LLC Opinion on the Financial … |
| 2 | `qba0102803c57:chunk-103` | 0.2203 |  | Report of Independent Registered Public Accounting Firm To the Board of Directors and Stockholders of Kimco Realty Corp… |
| 3 | `qba0102803c57:chunk-18` | 0.20270000000000002 | 1.0 | Natural disasters, severe weather conditions and the effects of climate change could have an adverse impact on our fina… |
| 4 | `qba0102803c57:chunk-12` | 0.1696 | 1.0 | Item 1A. Risk Factors We are subject to certain business and legal risks including, but not limited to, the following: … |
| 5 | `qba0102803c57:chunk-14` | 0.0398 | 1.0 | Newly acquired or re-developed properties may have characteristics or deficiencies currently unknown to us that affect … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qba0102803c57`)._

### ex-dev-qba50bc033945

- **example_id**: `dev:qba50bc033945`
- **state**: `completed`
- **query**: What commentary is provided by Teledyne Technologies on demand forecasts in light of government defense spending trends?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.7242626857711238 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba50bc033945:chunk-127` | 1.1714 | 2.0 | Let's stay with Aerospace first. A significant amount of our revenue in Aerospace is in the aftermarket. Because we hav… |
| 2 | `qba50bc033945:chunk-35` | 1.127 | 1.0 | Sure. Let me start with Q4, please, and then I'll go to some of the others. In health care, we had really nice Q4. Reve… |
| 3 | `qba50bc033945:chunk-95` | 1.1238000000000001 |  | Yes. The answer is yes. We have a pretty good read on what's coming. We have some new products. I mentioned the Black H… |
| 4 | `qba50bc033945:chunk-9` | 0.4794 | 1.0 | Thanks, Evan. The Instrumentation segment consists of our marine, test and measurement and environmental businesses, wh… |
| 5 | `qba50bc033945:chunk-5` | 0.36150000000000004 | 2.0 | Thank you, Jason, and good morning, and thank you for joining our earnings call. In the fourth quarter, we achieved all… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qba50bc033945`)._

### ex-dev-qbd63044fc6b3

- **example_id**: `dev:qbd63044fc6b3`
- **state**: `completed`
- **query**: What risk is associated with franchisee financial health amid rapid expansion requirements
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'Earnings', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=94

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbd63044fc6b3:chunk-76` | 1.2207999999999999 | 2.0 | OPERATIONS The global scope of our business subjects us to risks that could negatively affect our business. We encounte… |
| 2 | `qbd63044fc6b3:chunk-33` | 0.78 | 2.0 | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations Overview The Company fran… |
| 3 | `qbd63044fc6b3:chunk-37` | 0.6607000000000001 |  | The Following Definitions Apply to these Terms as Used Throughout this Report: •Constant currency results exclude the e… |
| 4 | `qbd63044fc6b3:chunk-73` | 0.5263 |  | Outlook Based on current conditions, the following is provided to assist in forecasting the Company's future results fo… |
| 5 | `qbd63044fc6b3:chunk-55` | 0.47709999999999997 |  | Franchised sales are not recorded as revenues by the Company, but are the basis on which the Company calculates and rec… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qbd63044fc6b3`)._

### ex-dev-qbdbd002b0a41

- **example_id**: `dev:qbdbd002b0a41`
- **state**: `completed`
- **query**: How has the ratio of Caterpillar Inc.’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=1.0 · gold=['10-Q', 'Earnings', '10-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5=0.43067655807339306 · skipped= · n_scored=94

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbdbd002b0a41:chunk-27` | 0.4218 |  | Well, thank you for your question. We've been pleased by the progress we've made. You recall, we started with that 2016… |
| 2 | `qbdbd002b0a41:chunk-5` | 0.2988 |  | Thanks, Ryan. Good morning, everyone. Thank you for joining us. As we close out 2023, I'd like to start by recognizing … |
| 3 | `qbdbd002b0a41:chunk-39` | 0.2625 |  | Yes. So as we talked about, I mentioned part of the decline in part sales in Resource Industries was relating to dealer… |
| 4 | `qbdbd002b0a41:chunk-7` | 0.15639999999999998 | 1.0 | Thanks, Jim, and good morning, everyone. I'll begin with commentary on the fourth quarter results, including the perfor… |
| 5 | `qbdbd002b0a41:chunk-45` | 0.0923 |  | Yes, there's going to be a couple of things, Mig, which are going to happen as we go through 2024. The one that's a lit… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qbdbd002b0a41`)._

### ex-dev-qc03648d89328

- **example_id**: `dev:qc03648d89328`
- **state**: `completed`
- **query**: How has the ratio of Moderna’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6806060567602009 · gold=['10-K', '10-Q', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc03648d89328:chunk-7` | 0.8231999999999999 | 2.0 | Thanks, Stéphane, and hello, everyone. Today, I will review our financial performance for both the fourth quarter and t… |
| 2 | `qc03648d89328:chunk-5` | 0.22 | 1.0 | Thank you, Lavina. Good morning or good afternoon, everyone. Thank you for joining us today. I will start with a review… |
| 3 | `qc03648d89328:chunk-11` | 0.0352 |  | Thank you, Stephen and Jamey. For Moderna and the patients we serve, 2024 is all about execution: execution in commerci… |
| 4 | `qc03648d89328:chunk-25` | 0.0064 |  | Thanks, Stephen. And Gena, it's Stéphane. On the upside and downside on the sales for this year, I think on the upside,… |
| 5 | `qc03648d89328:chunk-79` | 0.0049 |  | Thanks, Stephen. And on Australia, so a few things. First, I mean our team has delivered a strong performance on COVID … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qc03648d89328`)._

### ex-dev-qc187429e2dc5

- **example_id**: `dev:qc187429e2dc5`
- **state**: `completed`
- **query**: What dependency risks exist for Huntington Ingalls Industries, Inc. due to concentration of revenue in a limited number of government defense contracts?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.7698724385020871 · skipped= · n_scored=249

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc187429e2dc5:chunk-11` | 1.2310999999999999 | 2.0 | Item 1A. Risk Factors Our consolidated financial position, results of operations and cash flows are subject to various … |
| 2 | `qc187429e2dc5:chunk-127` | 1.2029999999999998 | 1.0 | 7. REVENUE The following is a description of principal activities from which the Company generates its revenues. For mo… |
| 3 | `qc187429e2dc5:chunk-12` | 1.165 | 2.0 | Current U.S. Government spending levels for defense-related or other programs may not be sustained, and future spending… |
| 4 | `qc187429e2dc5:chunk-13` | 1.1542 | 2.0 | experience a higher number of audits and/or lengthened periods of time required to close open audits. Moreover, the thr… |
| 5 | `qc187429e2dc5:chunk-142` | 1.1236 | 1.0 | For the year ended December 31, 2023, the Company recognized revenue of $690 million related to its contract liabilitie… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qc187429e2dc5`)._

### ex-dev-qc20017b12da3

- **example_id**: `dev:qc20017b12da3`
- **state**: `completed`
- **query**: How does Moderna view the pace of mRNA vaccine development cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.7285735751249806 · skipped= · n_scored=11

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc20017b12da3:chunk-1` | 0.7667999999999999 | 1.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## 2023 Commercial Updates… |
| 2 | `qc20017b12da3:chunk-4` | 0.738 | 2.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## Clinical Updates Modern… |
| 3 | `qc20017b12da3:chunk-0` | 0.5854999999999999 |  | Exhibit 99.1 # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates Third quarter 2023 re… |
| 4 | `qc20017b12da3:chunk-6` | 0.2604 | 1.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## About Moderna In over 1… |
| 5 | `qc20017b12da3:chunk-3` | 0.11739999999999999 |  | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## 2023 Financial Framewor… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qc20017b12da3`)._

### ex-dev-qc20e5c5b254e

- **example_id**: `dev:qc20e5c5b254e`
- **state**: `completed`
- **query**: How does Evergy manage equity award burn rate or share pool availability?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.8596355563650325 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **yield**: original=`DEF14A` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.6366824387328317 · skipped= · n_scored=186

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc20e5c5b254e:chunk-11` | 0.8707 | 1.0 | ##########EVERGY, INC.############ ##########Consolidated Statements of Changes in Equity############ ##########(Unaudi… |
| 2 | `qc20e5c5b254e:chunk-9` | 0.8556 | 1.0 | ##########EVERGY, INC.############ ##########Consolidated Statements of Changes in Equity############ ##########(Unaudi… |
| 3 | `qc20e5c5b254e:chunk-174` | 0.6008 |  | ######Issuer Purchases of Equity Securities#### Month##Total Number of Shares (or Units) Purchased(a)####Average Price … |
| 4 | `qc20e5c5b254e:chunk-42` | 0.1992 |  | Earnings Per Share To compute basic earnings per share (EPS), Evergy divides net income attributable to Evergy, Inc. by… |
| 5 | `qc20e5c5b254e:chunk-3` | 0.022 |  | ######EVERGY, INC.###### ######Consolidated Balance Sheets###### ######(Unaudited)###### ####September 30########Decemb… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qc20e5c5b254e`)._

### ex-dev-qc28e5aa0181b

- **example_id**: `dev:qc28e5aa0181b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Humana Inc. for potential shifts in Medicare Advantage enrollment?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7332063582049065 · gold=['Earnings', '10-K', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.49818925746641285 · skipped= · n_scored=66

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc28e5aa0181b:chunk-35` | 0.4685 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 2 | `qc28e5aa0181b:chunk-32` | 0.3148 | 1.0 | •If Humana does not design and price its products properly and competitively, if the premiums Humana receives are insuf… |
| 3 | `qc28e5aa0181b:chunk-10` | 0.28690000000000004 |  | Refer to the "Footnotes" section included herein for further explanation on disclosures for Adjusted (non-GAAP) financi… |
| 4 | `qc28e5aa0181b:chunk-15` | 0.27149999999999996 | 1.0 | The Adjusted (non-GAAP) metrics represent the exclusion of the company's employer group commercial medical products bus… |
| 5 | `qc28e5aa0181b:chunk-19` | 0.0956 |  | Refer to the "Footnotes" section included herein for further explanation on reasoning for Adjusted (non-GAAP) disclosur… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qc28e5aa0181b`)._

### ex-dev-qc4efe3f0f342

- **example_id**: `dev:qc4efe3f0f342`
- **state**: `completed`
- **query**: How could global geopolitical tensions affect Mastercard's cross?border revenues?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6327646179298274 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=104

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc4efe3f0f342:chunk-5` | 0.9498 | 2.0 | Thank you, Devin. Good morning, everyone. Here's the headline. We closed out 2023 with another quarter of strong earnin… |
| 2 | `qc4efe3f0f342:chunk-7` | 0.915 | 1.0 | Thanks, Michael. Turning now to Page 3, which shows our financial performance for the fourth quarter on a currency-neut… |
| 3 | `qc4efe3f0f342:chunk-41` | 0.8089999999999999 | 1.0 | Dan, you just touched on some of the key things to watch out for. But this is no different than us monitoring fiscal mo… |
| 4 | `qc4efe3f0f342:chunk-39` | 0.7781 |  | I heard you call out a couple of times geopolitical concerns, and I know that there's some, I don't know, 30 or 40 diff… |
| 5 | `qc4efe3f0f342:chunk-21` | 0.31179999999999997 |  | Right. Let me take the China question first and we come back to the conversion topic that you raised. So needless to sa… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qc4efe3f0f342`)._

### ex-dev-qc6c8c1f4ddfe

- **example_id**: `dev:qc6c8c1f4ddfe`
- **state**: `completed`
- **query**: How has CMS Energy Corporation’s electric utility segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6594343379129768 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=133

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc6c8c1f4ddfe:chunk-68` | 0.5575 |  | # 2023 TARGET TOTAL DIRECT COMPENSATION MIX TABLE (1) (cont.) ## Plan Performance Results The following is the payout t… |
| 2 | `qc6c8c1f4ddfe:chunk-109` | 0.16 |  | # 2023 Nonqualified Deferred Compensation (cont.) ## Compensation Actually Paid Versus Net Income Because a significant… |
| 3 | `qc6c8c1f4ddfe:chunk-67` | 0.0953 |  | # 2023 TARGET TOTAL DIRECT COMPENSATION MIX TABLE (1) (cont.) ## Cash Compensation (cont.) The Target Award Percentages… |
| 4 | `qc6c8c1f4ddfe:chunk-56` | 0.0946 |  | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Program Design (cont.) BASE SALARY. Base salary is targeted to approx… |
| 5 | `qc6c8c1f4ddfe:chunk-65` | 0.0633 |  | # 2023 TARGET TOTAL DIRECT COMPENSATION MIX TABLE (1) (cont.) ## Cash Compensation (cont.) (1) Represents annual base s… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qc6c8c1f4ddfe`)._

### ex-dev-qc8e6b0d72c52

- **example_id**: `dev:qc8e6b0d72c52`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Caesars Entertainment, Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc8e6b0d72c52:chunk-31` | 0.0432 | 1.0 | No. We -- Carlo, you know that we're never standing still. Sean McBurney, Anthony and their team have lists of items th… |
| 2 | `qc8e6b0d72c52:chunk-11` | 0.0354 |  | Thanks, Bret. To touch briefly on the fourth quarter results. I know we pre-released about a month ago. So they've been… |
| 3 | `qc8e6b0d72c52:chunk-51` | 0.0134 |  | Yes. I mean we're $4 billion now with digital doing de minimis EBITDA by 25%, we'd expect to be in the neighborhood of … |
| 4 | `qc8e6b0d72c52:chunk-107` | 0.0069 |  | It's Shaun Kelley on for Julie. Two questions, if I could. First, on the regional side. Tom, you've been calling out fo… |
| 5 | `qc8e6b0d72c52:chunk-95` | 0.0067 |  | Yes. I would say the size of the market has consistently exceeded our expectations, growth in mature markets, markets t… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qc8e6b0d72c52`)._

### ex-dev-qcbbca1138c08

- **example_id**: `dev:qcbbca1138c08`
- **state**: `completed`
- **query**: What investor views emerged on Freeport-McMoRan’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.3689807742993011 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcbbca1138c08:chunk-7` | 1.2017 |  | Okay. Thank you, Richard, and I'll be covering the presentation materials, starting with Slide 3. Our achievements for … |
| 2 | `qcbbca1138c08:chunk-37` | 1.0624 | 1.0 | Well, we're constantly monitoring the market and you can be confident that opportunities are available are presented to… |
| 3 | `qcbbca1138c08:chunk-53` | 1.0437 | 1.0 | On the first part of the question, with respect to how we evaluate projects and returns, we don't target one number. We… |
| 4 | `qcbbca1138c08:chunk-5` | 0.9062000000000001 |  | Okay. Good morning, everyone. As you can see, our first quarter was really a sound quarter and outstanding in several r… |
| 5 | `qcbbca1138c08:chunk-35` | 0.7514 | 2.0 | Given the cost -- the capital costs involved and the timing of building new projects, and the strength of your balance … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qcbbca1138c08`)._

### ex-dev-qcdb8bc16cf2f

- **example_id**: `dev:qcdb8bc16cf2f`
- **state**: `completed`
- **query**: What guidance was offered on Jack Henry & Associates’ technology platform modernization targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9499797323370371 · gold=['Earnings', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.6779553320147448 · skipped= · n_scored=126

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcdb8bc16cf2f:chunk-89` | 1.3054000000000001 | 1.0 | Yes. I think you hit on all of them. I think it is a combination of much of what you described. We continue to look at … |
| 2 | `qcdb8bc16cf2f:chunk-95` | 1.1697 | 2.0 | Sure, Chuck. I'll take it, and Mimi can add some commentary is -- yes, I think -- so it is up from where we were. I don… |
| 3 | `qcdb8bc16cf2f:chunk-23` | 0.9407000000000001 | 1.0 | Yes. No. I mean, fortunately, I took over for an individual that did a pretty good job. So nothing significant. I mean,… |
| 4 | `qcdb8bc16cf2f:chunk-5` | 0.8773 | 1.0 | Thank you, Vance, and hello, everyone. I appreciate all of you joining this morning's call. We are very pleased to repo… |
| 5 | `qcdb8bc16cf2f:chunk-73` | 0.6246 | 1.0 | Yes. Kartik, yes, thanks for the question. For sure. I mean, I think as we have articulated throughout, I mean, it's a … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qcdb8bc16cf2f`)._

### ex-dev-qcf796a17c330

- **example_id**: `dev:qcf796a17c330`
- **state**: `completed`
- **query**: How are scenario analyses conducted by FirstEnergy Corp. for fluctuations in electricity demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8498932729020808 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-Q` · used=True
- **S2**: nDCG@5=0.8854598815714874 · skipped= · n_scored=140

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcf796a17c330:chunk-53` | 0.6328 | 1.0 | So like capital projects and other things, we don't want to put forecast growth in until we're seeing it. And we're see… |
| 2 | `qcf796a17c330:chunk-95` | 0.2281 |  | Thank you for the question, Angie. We absolutely do. And you're right, being mostly a wires company, certainly in 4 of … |
| 3 | `qcf796a17c330:chunk-7` | 0.19469999999999998 | 1.0 | Thank you, Brian, and good morning, everyone. I'm also very proud of our performance in 2023, and I'm excited to turn a… |
| 4 | `qcf796a17c330:chunk-99` | 0.14700000000000002 |  | So it's a good question, Angie. I think we've already seen some of that associated with things like the war in Ukraine … |
| 5 | `qcf796a17c330:chunk-51` | 0.0756 | 1.0 | Okay. And then just one last one, just on the load growth, 1% embedded in the plan. Places like PJM have just continued… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qcf796a17c330`)._

### ex-dev-qd08d64c0654c

- **example_id**: `dev:qd08d64c0654c`
- **state**: `completed`
- **query**: How has Fortive Corporation’s segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9979470946084208 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.7262287617954056 · skipped= · n_scored=16

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd08d64c0654c:chunk-6` | 1.2223 | 2.0 | # FORTIVE CORPORATION AND SUBSIDIARIES SEGMENT INFORMATION ($ in millions) <table><tr><th></th><th colspan="2">Three Mo… |
| 2 | `qd08d64c0654c:chunk-1` | 0.9773 |  | # Fortive Reports Strong Fourth Quarter and Full Year 2023 Results Introduces First Quarter and Full Year 2024 Outlook … |
| 3 | `qd08d64c0654c:chunk-5` | 0.758 |  | # FORTIVE CORPORATION AND SUBSIDIARIES CONSOLIDATED STATEMENTS OF EARNINGS ($ and shares in millions, except per share … |
| 4 | `qd08d64c0654c:chunk-14` | 0.4569 |  | # Adjusted Net Earnings and Adjusted Diluted Net Earnings Per Share (unaudited) <table><tr><th rowspan="2">($ in millio… |
| 5 | `qd08d64c0654c:chunk-15` | 0.3295 |  | # Adjusted Net Earnings and Adjusted Diluted Net Earnings Per Share (unaudited) (cont.) (a) Beginning with our adoption… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qd08d64c0654c`)._

### ex-dev-qd177bdad4bdd

- **example_id**: `dev:qd177bdad4bdd`
- **state**: `completed`
- **query**: What pension discount rate assumption was used for year end valuation?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9751957567060058 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd177bdad4bdd:chunk-77` | 1.247 | 2.0 | Notwithstanding these actions, the impact of our postretirement benefit plans on our earnings may be volatile in that t… |
| 2 | `qd177bdad4bdd:chunk-163` | 1.2086 | 2.0 | (a)Benefit obligation balances represent the projected benefit obligation for our qualified defined benefit pension pla… |
| 3 | `qd177bdad4bdd:chunk-172` | 1.152 | 2.0 | ######Qualified Defined Benefit Pension Plans############Retiree Medical and Life Insurance Plans###### ##2023####2022#… |
| 4 | `qd177bdad4bdd:chunk-173` | 1.0694000000000001 | 2.0 | (a)A pension discount rate of 4.75% was used for the applicable plans following the transaction and remeasurement recog… |
| 5 | `qd177bdad4bdd:chunk-83` | 0.4957 | 2.0 | ##Revenue recognition based on the percentage of completion method Description of the Matter##For the year ended Decemb… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qd177bdad4bdd`)._

### ex-dev-qd2e3bd55f2ee

- **example_id**: `dev:qd2e3bd55f2ee`
- **state**: `completed`
- **query**: What questions were asked about HCA Healthcare’s patient engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7631679915955182 · gold=['DEF14A', 'Earnings', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=0.5555260897275291 · skipped= · n_scored=135

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd2e3bd55f2ee:chunk-56` | 1.0662 | 1.0 | # PROPOSAL 6 - STOCKHOLDER PROPOSAL REGARDING REPORT ON PATIENT FEEDBACK REGARDING QUALITY OF CARE (cont.) ## Statement… |
| 2 | `qd2e3bd55f2ee:chunk-54` | 0.8325 | 2.0 | # PROPOSAL 6 - STOCKHOLDER PROPOSAL REGARDING REPORT ON PATIENT FEEDBACK REGARDING QUALITY OF CARE We have been advised… |
| 3 | `qd2e3bd55f2ee:chunk-58` | 0.7586 |  | # PROPOSAL 6 - STOCKHOLDER PROPOSAL REGARDING REPORT ON PATIENT FEEDBACK REGARDING QUALITY OF CARE (cont.) ## HCA Healt… |
| 4 | `qd2e3bd55f2ee:chunk-76` | 0.4052 | 1.0 | # Elements of Compensation (cont.) ## Quality and Care Measures (20% of 2023 PEP) The quality and care weighted portion… |
| 5 | `qd2e3bd55f2ee:chunk-55` | 0.39799999999999996 | 2.0 | # PROPOSAL 6 - STOCKHOLDER PROPOSAL REGARDING REPORT ON PATIENT FEEDBACK REGARDING QUALITY OF CARE (cont.) ## SUPPORTIN… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qd2e3bd55f2ee`)._

### ex-dev-qd422350b37cb

- **example_id**: `dev:qd422350b37cb`
- **state**: `completed`
- **query**: What investor views emerged on Martin Marietta Materials’ geographic expansion prospects within domestic markets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9452713619732751 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.5088013258915567 · skipped= · n_scored=312

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd422350b37cb:chunk-49` | 1.0695 | 1.0 | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations Generally, the… |
| 2 | `qd422350b37cb:chunk-48` | 1.0274 | 1.0 | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations Magnesia Speci… |
| 3 | `qd422350b37cb:chunk-0` | 0.9523 | 1.0 | PART I ITEM 1 – BUSINESS General Martin Marietta Materials, Inc. (the Company or Martin Marietta) is a natural resource… |
| 4 | `qd422350b37cb:chunk-2` | 0.8559 |  | Part I ♦ Item 1 – Business The Company generally acquires contiguous property around existing quarry locations. Such pa… |
| 5 | `qd422350b37cb:chunk-1` | 0.7912 | 1.0 | Part I ♦ Item 1 – Business Building Materials Business The profitability of the Building Materials business, which serv… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qd422350b37cb`)._

### ex-dev-qd483c94f1ec6

- **example_id**: `dev:qd483c94f1ec6`
- **state**: `completed`
- **query**: How do investors view American International Group, Inc.’s valuation relative to peers based on recent disclosures?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['DEF14A', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-K', 'DEF14A', '10-Q', '8-K']`
- **yield**: original=`Earnings` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=0.5958337834156117 · skipped= · n_scored=163

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd483c94f1ec6:chunk-87` | 0.7163999999999999 | 1.0 | # Compensation Discussion and Analysis 2023 Compensation Decisions and Outcomes (cont.) ## Separation of Life and Retir… |
| 2 | `qd483c94f1ec6:chunk-123` | 0.6572 | 1.0 | # 2023 Executive Compensation Pay Versus Performance (cont.) (4) The Peer Group TSR set forth in this table utilizes th… |
| 3 | `qd483c94f1ec6:chunk-86` | 0.6512 | 1.0 | # Assessment of 2021 Performance Share Units (cont.) ## General Insurance 1. Chubb Limited 2. CNA Financial Corporation… |
| 4 | `qd483c94f1ec6:chunk-84` | 0.5347000000000001 | 1.0 | # Compensation Discussion and Analysis 2023 Compensation Decisions and Outcomes <table><tr><th>Metric</th><th>Target</t… |
| 5 | `qd483c94f1ec6:chunk-162` | 0.45070000000000005 | 1.0 | # Appendix A - Non-GAAP Financial Measures (cont.) ## A-4 AIG 2024 PROXY STATEMENT (cont.) <table><tr><th rowspan="2">U… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qd483c94f1ec6`)._

### ex-dev-qd5c685de4d7a

- **example_id**: `dev:qd5c685de4d7a`
- **state**: `completed`
- **query**: What themes emerged regarding the convergence of technology and biotechnology in the company operating model
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7373239404693707 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-Q', '10-K', '8-K']`
- **yield**: original=`DEF14A` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.13869012617430843 · skipped= · n_scored=176

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd5c685de4d7a:chunk-66` | 1.0814 | 1.0 | # Compensation Discussion and Analysis <table><tr><th>Strategic Priorities</th><th colspan="2">Importance Select 2021 A… |
| 2 | `qd5c685de4d7a:chunk-52` | 0.15460000000000002 |  | # Corporate Governance 15 million users accessed Khan Academy's free biology lessons in 2021. Through an expanded, mult… |
| 3 | `qd5c685de4d7a:chunk-22` | 0.12110000000000001 |  | # Item 1 - Election of Directors (cont.) ## Qualifications Dr. Jacks has been a director of Thermo Fisher Scientific, I… |
| 4 | `qd5c685de4d7a:chunk-20` | 0.043000000000000003 |  | # Item 1 - Election of Directors (cont.) ## Committees: - Compensation and Management Development - Corporate Responsib… |
| 5 | `qd5c685de4d7a:chunk-26` | 0.0121 |  | # Item 1 - Election of Directors (cont.) ## Qualifications The Board concluded that Dr. Sugar should serve on our Board… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qd5c685de4d7a`)._

### ex-dev-qd639a486b106

- **example_id**: `dev:qd639a486b106`
- **state**: `completed`
- **query**: Which general medicine candidate in obesity was identified for upcoming mid stage data readout
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.5950427489208391 · gold=['Earnings', '10-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **yield**: original=`10-K` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.9520727775370875 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd639a486b106:chunk-5` | 1.2938 | 2.0 | Okay. Thank you, Justin, and let me thank all of you for joining our call. 2023 was another year of performance and pro… |
| 2 | `qd639a486b106:chunk-11` | 1.2398 | 2.0 | Thank you, Vikram, and good afternoon, everyone. I'd like to take a minute to convey how thrilled I am to join the Amge… |
| 3 | `qd639a486b106:chunk-153` | 1.1974 | 2.0 | Sure. No, thank you for your question. For the broader group, AMG 786 is an oral medicine being developed for obesity. … |
| 4 | `qd639a486b106:chunk-27` | 0.8116000000000001 | 2.0 | Yes. Thanks for the question. I'll take this one as well. As you may or may not know, the Phase II study, which is ongo… |
| 5 | `qd639a486b106:chunk-21` | 0.5863 |  | Yes. Thanks a lot, Michael. We really appreciate the consideration the Phase I paper is receiving from the community. I… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qd639a486b106`)._

### ex-dev-qd87c2da5e7da

- **example_id**: `dev:qd87c2da5e7da`
- **state**: `completed`
- **query**: How does Kenvue manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.4468535299918563 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd87c2da5e7da:chunk-95` | 0.5725 |  | # Certain Relationships and Related Person Transactions ## Defined Benefit Pension Plans The Employee Matters Agreement… |
| 2 | `qd87c2da5e7da:chunk-60` | 0.4996 |  | # Compensation Clawback Policies (cont.) ## Compensation Risk Management Kenvue is committed to effective risk manageme… |
| 3 | `qd87c2da5e7da:chunk-25` | 0.3033 | 1.0 | # Committees of the Board (cont.) ## Audit Committee ## Responsibilities: Vasant Prabhu (Chair) Richard E. Allison, Jr.… |
| 4 | `qd87c2da5e7da:chunk-34` | 0.2975 | 1.0 | # 2023 Director Compensation Table Fees Earned or Paid in <table><tr><th></th><th colspan="2">or</th><th></th><th rowsp… |
| 5 | `qd87c2da5e7da:chunk-51` | 0.2417 | 1.0 | # Executive Compensation (cont.) ## Annual Long-Term Incentive Grants Our long-term incentive plan is intended to motiv… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qd87c2da5e7da`)._

### ex-dev-qdb9da6a1e373

- **example_id**: `dev:qdb9da6a1e373`
- **state**: `completed`
- **query**: How does Packaging Corporation of America manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7118306928082477 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **yield**: original=`10-K` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=0.8347911247384279 · skipped= · n_scored=212

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdb9da6a1e373:chunk-166` | 1.1599 | 2.0 | We have additional asset retirement obligations with indeterminate settlement dates. The fair value of these asset reti… |
| 2 | `qdb9da6a1e373:chunk-19` | 1.0790000000000002 | 1.0 | PART II Item 5. MARKET FOR REGISTRANT’S COMMON EQUITY, RELATED STOCKHOLDER MATTERS, AND ISSUER PURCHASES OF EQUITY SECU… |
| 3 | `qdb9da6a1e373:chunk-197` | 0.4004 | 1.0 | (a)Assumes that outstanding performance units pay out at the target level. Does not include 1,044,500 shares of unveste… |
| 4 | `qdb9da6a1e373:chunk-176` | 0.3545 |  | We evaluate share-based compensation expense on a quarterly basis based on our estimate of expected forfeitures, review… |
| 5 | `qdb9da6a1e373:chunk-174` | 0.2309 |  | For performance unit awards made in 2023, 2022, and 2021, in terms of grant date value, 50% used total shareholder retu… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qdb9da6a1e373`)._

### ex-dev-qdbaa829dd4cc

- **example_id**: `dev:qdbaa829dd4cc`
- **state**: `completed`
- **query**: What questions were asked about Gen Digital Inc.’s customer retention and renewal rates?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.49818925746641285 · skipped= · n_scored=227

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdbaa829dd4cc:chunk-36` | 0.468 |  | (1) Non-GAAP Direct customer revenue differs from U.S. GAAP direct customer revenue in fiscal 2023 because it excludes … |
| 2 | `qdbaa829dd4cc:chunk-9` | 0.35869999999999996 | 1.0 | •Our customers’ dissatisfaction with our efforts to market additional products and services; •Our customer service and … |
| 3 | `qdbaa829dd4cc:chunk-18` | 0.3408 |  | •The number, severity and timing of threat outbreaks and cyber security incidents; •Loss of customers or strategic part… |
| 4 | `qdbaa829dd4cc:chunk-35` | 0.3282 | 1.0 | ########Fiscal Year###### (In millions, except for per user amounts and percentages)####2024########2023## Direct custo… |
| 5 | `qdbaa829dd4cc:chunk-8` | 0.2986 |  | The intellectual property ownership and license rights surrounding AI technologies, as well as data protection laws rel… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qdbaa829dd4cc`)._

### ex-dev-qdec70f55027f

- **example_id**: `dev:qdec70f55027f`
- **state**: `completed`
- **query**: What investor views emerged on Mettler-Toledo International Inc.’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9734136950814526 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.5088013258915567 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdec70f55027f:chunk-33` | 1.2229999999999999 | 1.0 | I'll take that. Look, Shawn and I had been in China in December. And of course, we're in continued conversations with t… |
| 2 | `qdec70f55027f:chunk-119` | 1.1829 | 1.0 | Yes. And just to read correctly, Brandon, that doesn't mean that the algorithm going forward, we're expecting double-di… |
| 3 | `qdec70f55027f:chunk-51` | 1.1604 | 1.0 | Sure, absolutely. And again, I'll probably give you some insights into the different regions, but also in different end… |
| 4 | `qdec70f55027f:chunk-9` | 1.0872 |  | Thanks, Shawn. Let me start with some comments on our operating businesses, starting with Lab. As we had expected, dema… |
| 5 | `qdec70f55027f:chunk-101` | 0.8066 | 1.0 | Yes. Thanks, Rachel. And I'll start and then Shawn if you have some additional comments, feel free to chime in. So I th… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qdec70f55027f`)._

### ex-dev-qdfe52ef66df5

- **example_id**: `dev:qdfe52ef66df5`
- **state**: `completed`
- **query**: How has the ratio of IDEXX Laboratories’ recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9452713619732751 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5=0.7693968268775773 · skipped= · n_scored=271

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdfe52ef66df5:chunk-45` | 1.0583 | 2.0 | Our long-term success in the continuing growth of our CAG recurring diagnostic products and services is dependent upon:… |
| 2 | `qdfe52ef66df5:chunk-62` | 0.8937 | 2.0 | CAG Diagnostics Recurring Revenue. The increase in CAG Diagnostics recurring revenue was primarily due to higher realiz… |
| 3 | `qdfe52ef66df5:chunk-56` | 0.8051 | 1.0 | (1)Reported revenue growth and organic revenue growth may not recalculate due to rounding. Total Company Revenue. The i… |
| 4 | `qdfe52ef66df5:chunk-46` | 0.7129000000000001 | 1.0 | The prevalence of in-clinic testing, as opposed to outside reference laboratories such as IDEXX Reference Laboratories,… |
| 5 | `qdfe52ef66df5:chunk-42` | 0.6115 | 1.0 | ITEM 7. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following discussion … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qdfe52ef66df5`)._

### ex-dev-qe1811f4fd3dc

- **example_id**: `dev:qe1811f4fd3dc`
- **state**: `completed`
- **query**: What questions were asked about Digital Realty Trust’s customer or tenant engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9293449960425915 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=108

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qe1811f4fd3dc:chunk-63` | 0.6398 | 1.0 | Yes. Thanks, Frank, for the question. Appreciate it. As Andy highlighted, the pipeline across the board is robust and t… |
| 2 | `qe1811f4fd3dc:chunk-5` | 0.21960000000000002 |  | Thanks, Jordan, and thanks to everyone for joining our call. 2023 was a milestone year for Digital Realty as we made st… |
| 3 | `qe1811f4fd3dc:chunk-47` | 0.2069 |  | Thanks, David. So the -- I think you heard me loud and clear on where rates have come from and where they've gone or wh… |
| 4 | `qe1811f4fd3dc:chunk-87` | 0.15009999999999998 |  | Yes. It's a great question and appreciate it, Erik. I think there are a couple of dynamics that you touched on. The tra… |
| 5 | `qe1811f4fd3dc:chunk-21` | 0.0632 |  | Thanks, Dave. This is Andy. I don't think we're experiencing the same exact dynamics on power as what you heard last ni… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qe1811f4fd3dc`)._

### ex-dev-qe2edf9d38872

- **example_id**: `dev:qe2edf9d38872`
- **state**: `completed`
- **query**: How has Charter Communications’ broadband segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-Q` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=181

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qe2edf9d38872:chunk-161` | 0.10060000000000001 |  | Charter Communications \| 79 \|<hr /><hr />December 31, 2019 (the beginning of the measurement period for this pay versus… |
| 2 | `qe2edf9d38872:chunk-32` | 0.0551 |  | Over an advanced communications network, we offer a full range of state-of-the-art residential and business services in… |
| 3 | `qe2edf9d38872:chunk-49` | 0.0070999999999999995 |  | • Over an approximately 5-year period, Charter achieved significant stock price growth, increasing 261% from $227.41 (t… |
| 4 | `qe2edf9d38872:chunk-155` | 0.0023 |  | Pay Versus Performance Results & Discussion An assessment of Charter’s pay versus performance alignment was conducted p… |
| 5 | `qe2edf9d38872:chunk-21` | 0.001 |  | Advance’s portfolio includes Condé Nast, which produces high quality award-winning journalism, content and entertainme… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qe2edf9d38872`)._

### ex-dev-qe8a08fb7bfff

- **example_id**: `dev:qe8a08fb7bfff`
- **state**: `completed`
- **query**: How has Meta Platforms, Inc.’s advertising segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **yield**: original=`Earnings` · effective=`10-Q` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=11

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qe8a08fb7bfff:chunk-9` | 1.1945999999999999 | 2.0 | # META PLATFORMS, INC. CONDENSED CONSOLIDATED STATEMENTS OF CASH FLOWS (In millions) (Unaudited) <table><tr><th rowspan… |
| 2 | `qe8a08fb7bfff:chunk-0` | 0.9563999999999999 | 1.0 | # Meta Reports Third Quarter 2023 Results MENLO PARK, Calif. - October 25, 2023 - Meta Platforms, Inc. (Nasdaq: META) t… |
| 3 | `qe8a08fb7bfff:chunk-1` | 0.9437 | 1.0 | # Meta Reports Third Quarter 2023 Results (cont.) ## Third Quarter 2023 Operational and Other Financial Highlights - Fa… |
| 4 | `qe8a08fb7bfff:chunk-10` | 0.9187 | 1.0 | # Reconciliation of GAAP to Non-GAAP Results (In millions, except percentages) (Unaudited) <table><tr><th rowspan="2"><… |
| 5 | `qe8a08fb7bfff:chunk-6` | 0.8172 | 1.0 | # META PLATFORMS, INC. CONDENSED CONSOLIDATED STATEMENTS OF INCOME (In millions, except per share amounts) (Unaudited) … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qe8a08fb7bfff`)._

### ex-dev-qe93fa46ab352

- **example_id**: `dev:qe93fa46ab352`
- **state**: `completed`
- **query**: How does Philip Morris International view the pace of innovation cycles in reduced-risk products and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7189324940540128 · gold=['Earnings', '10-Q', '10-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.21398626473452756 · skipped= · n_scored=115

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qe93fa46ab352:chunk-16` | 0.6929 |  | # BOARD OPERATIONS AND GOVERNANCE (cont.) ## KEY RESPONSIBILITIES: - review and report to the Board the overall researc… |
| 2 | `qe93fa46ab352:chunk-49` | 0.4898 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS In determining the individual component of Mr. Olczak's 2023 IC award, the Commi… |
| 3 | `qe93fa46ab352:chunk-5` | 0.0934 |  | # PROXY SUMMARY (cont.) ## Who We Are ## PMI at a Glance ## 2023 Annual Performance Targets and Results PMI, one of the… |
| 4 | `qe93fa46ab352:chunk-33` | 0.08510000000000001 |  | # ELECTION OF DIRECTORS (cont.) ## Other Directorships and Associations: Ms. Morparia currently sits on the board of di… |
| 5 | `qe93fa46ab352:chunk-112` | 0.0814 |  | # EXHIBIT C: GLOSSARY OF TERMS (cont.) ## Other (cont.) - Smoke-Free Products ("SFPs") is the term we primarily use to … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qe93fa46ab352`)._

### ex-dev-qe99b7fb80e2c

- **example_id**: `dev:qe99b7fb80e2c`
- **state**: `completed`
- **query**: How has Intercontinental Exchange’s data services segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.665593054087714 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.6843515475204855 · skipped= · n_scored=62

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qe99b7fb80e2c:chunk-5` | 1.2194 | 1.0 | Thanks, Katia. Good morning, everyone, and thank you for joining us today. I'll begin on Slide 4 with a summary of our … |
| 2 | `qe99b7fb80e2c:chunk-7` | 1.0463 | 1.0 | Thank you, Warren, and thank you all for joining us this morning. Please turn to Slide 9. We are pleased to report anot… |
| 3 | `qe99b7fb80e2c:chunk-55` | 0.6736 |  | Sure. Kyle, it's Warren. So as we said in the past, back in May, you're right, we did increase a couple of contracts ac… |
| 4 | `qe99b7fb80e2c:chunk-17` | 0.6379 |  | And Craig, let me just add too, on the flat guidance for recurring revenue. So on the implementation side, just to reit… |
| 5 | `qe99b7fb80e2c:chunk-9` | 0.5535 | 1.0 | Thank you, Ben. Good morning, everyone, and thank you for joining us. Please turn to Slide 10. 2023 was a unique year f… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qe99b7fb80e2c`)._

### ex-dev-qeccd6f3b9d06

- **example_id**: `dev:qeccd6f3b9d06`
- **state**: `completed`
- **query**: What feedback surfaced on Akamai Technologies' innovation or new product pipeline prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=140

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeccd6f3b9d06:chunk-47` | 1.2295 | 2.0 | Yes. So signing on compute customers is a big focus for us this year. We have the basic infrastructure in place. Of cou… |
| 2 | `qeccd6f3b9d06:chunk-41` | 1.2256 | 2.0 | Yes. I'll take this one, Tom. You broke up a little bit there, Keith, but I think I got the genesis of the question. So… |
| 3 | `qeccd6f3b9d06:chunk-5` | 1.2218 | 2.0 | Thanks, Tom, and thank you very much for the terrific job that you've done over the last 10 years at Akamai. It's truly… |
| 4 | `qeccd6f3b9d06:chunk-63` | 1.2146 | 2.0 | Yes. In web app firewall, we've been the market leader there for 10 years since we started that marketplace with web ap… |
| 5 | `qeccd6f3b9d06:chunk-7` | 1.2139 | 2.0 | Thank you, Tom. I would also like to thank Tom Barth for his incredible service for 10 years as our Head of Investor Re… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qeccd6f3b9d06`)._

### ex-dev-qf13afdfcadcf

- **example_id**: `dev:qf13afdfcadcf`
- **state**: `completed`
- **query**: What did Howmet Aerospace Inc.’s leadership say about Howmet Aerospace Inc.’s dividend policy?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.6734685045602393 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['8-K', '10-K', 'DEF14A', 'Earnings', '10-Q']`
- **yield**: original=`8-K` · effective=`Earnings` · used=True
- **S2**: nDCG@5=0.21398626473452756 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf13afdfcadcf:chunk-64` | 0.5069 |  | # Summary of Key 2023 Inputs and Decisions (cont.) ## What We Do ## What We Don't Do - PAY FOR PERFORMANCE We link comp… |
| 2 | `qf13afdfcadcf:chunk-10` | 0.0862 | 1.0 | # ENVIRONMENTAL, SOCIAL AND GOVERNANCE (ESG) HIGHLIGHTS (cont.) ## NO SUPERMAJORITY VOTING REQUIREMENTS - The Certifica… |
| 3 | `qf13afdfcadcf:chunk-101` | 0.0747 |  | # Item 4-Approval of the Howmet Aerospace Stock Incentive Plan, as Amended and Restated (cont.) ## Performance Awards A… |
| 4 | `qf13afdfcadcf:chunk-27` | 0.0347 |  | # DIRECTORS' ALIGNMENT WITH SHAREHOLDERS ## Stock Ownership Guideline for Directors In order to further align the inter… |
| 5 | `qf13afdfcadcf:chunk-119` | 0.014499999999999999 |  | # Questions and Answers about the Annual Meeting and Voting (cont.) ## 11. What is the voting requirement to approve ea… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qf13afdfcadcf`)._

### ex-dev-qf25e1308bae4

- **example_id**: `dev:qf25e1308bae4`
- **state**: `completed`
- **query**: Which investor concerns about the company’s China exposure did management acknowledge?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9629964747243054 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '8-K', '10-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=74

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf25e1308bae4:chunk-5` | 1.1248 | 1.0 | Thanks, Simona. Q4 was another record quarter. Revenue of $22.1 billion was up 22% sequentially and up 265% year-on-yea… |
| 2 | `qf25e1308bae4:chunk-61` | 1.0261 | 1.0 | At the core, remember, the U.S. government wants to limit the latest capabilities of NVIDIA's accelerated computing and… |
| 3 | `qf25e1308bae4:chunk-59` | 0.0573 |  | I wanted to ask about the China business. I know that in the prepared comments, you said that you started shipping some… |
| 4 | `qf25e1308bae4:chunk-17` | 0.0082 |  | Okay, yes. Well, you know we guide 1 quarter at a time. But fundamentally, the conditions are excellent for continued g… |
| 5 | `qf25e1308bae4:chunk-37` | 0.0021 |  | First, our CSPs have a very clear view of our product road map and transitions. And that transparency with our CSPs giv… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qf25e1308bae4`)._

### ex-dev-qf38450369367

- **example_id**: `dev:qf38450369367`
- **state**: `completed`
- **query**: What investor views emerged on Nordson Corporation’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.665593054087714 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf38450369367:chunk-17` | 0.0148 |  | # Present Directors with Terms Expiring in 2026 (cont.) ## Committees: - Invacare Corporation (NYSE: IVC) (2014-2018), … |
| 2 | `qf38450369367:chunk-11` | 0.0118 |  | # Nominee for Terms Expiring in 2026 (cont.) ## CHRISTOPHER L. MAPES Director Since: 2024 Other Public Directorships (c… |
| 3 | `qf38450369367:chunk-14` | 0.0071 |  | # Table of Contents (cont.) ## Committees: - Audit - Governance and Sustainability Other Public Directorships (current … |
| 4 | `qf38450369367:chunk-65` | 0.0018000000000000002 |  | # Table of Contents (cont.) ## Currency Fluctuation Policy The Compensation Committee believes that management should b… |
| 5 | `qf38450369367:chunk-12` | 0.0007999999999999999 |  | # Nominees for Terms Expiring in 2027 (cont.) ## FRANK M. JAEHNERT Director Since: 2012 Other Public Directorships (cur… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qf38450369367`)._

### ex-dev-qf5b4bbe60015

- **example_id**: `dev:qf5b4bbe60015`
- **state**: `completed`
- **query**: How has Cadence Design Systems’ IP segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf5b4bbe60015:chunk-19` | 0.3526 | 1.0 | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 2 | `qf5b4bbe60015:chunk-1` | 0.32999999999999996 | 1.0 | For fiscal year 2024, the company expects: •Revenue in the range of $4.60 billion to $4.66 billion •GAAP operating marg… |
| 3 | `qf5b4bbe60015:chunk-0` | 0.1648 |  | Exhibit 99.01 Cadence Reports Second Quarter 2024 Financial Results Second Quarter Backlog of $6.0 Billion Updating 202… |
| 4 | `qf5b4bbe60015:chunk-13` | 0.15189999999999998 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 5 | `qf5b4bbe60015:chunk-21` | 0.12380000000000001 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qf5b4bbe60015`)._

### ex-dev-qf7a3126727b8

- **example_id**: `dev:qf7a3126727b8`
- **state**: `completed`
- **query**: How does Sysco Corporation’s debt maturity profile affect liquidity and cost structure?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=148

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf7a3126727b8:chunk-144` | 0.9963 | 2.0 | # ADJUSTED OPERATING INCOME AND ADJUSTED EARNINGS PER SHARE NON-GAAP RECONCILIATIONS (LETTER FROM CEO AND CHAIR AND PAY… |
| 2 | `qf7a3126727b8:chunk-145` | 0.4102 |  | # NET DEBT TO ADJUSTED EBITDA (LETTER FROM CEO AND CHAIR) (cont.) ## ADJUSTED EBITDA NON-GAAP RECONCILIATION (LETTER FR… |
| 3 | `qf7a3126727b8:chunk-3` | 0.2757 |  | # LETTER FROM OUR CEO AND CHAIRMAN (cont.) ## Dear Sysco Stockholder, Throughout our rich 54-year history, Sysco has ma… |
| 4 | `qf7a3126727b8:chunk-17` | 0.2311 |  | # BOARD LEADERSHIP STRUCTURE (cont.) ## BOARD COMMITTEES The Board has six standing committees: Audit Committee, Compen… |
| 5 | `qf7a3126727b8:chunk-146` | 0.0072 |  | # ADJUSTED OPERATING INCOME AND ADJUSTED EARNINGS PER SHARE NON-GAAP RECONCILIATIONS (PAY VERSUS PERFORMANCE) <table><t… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qf7a3126727b8`)._

### ex-dev-qf8cbcec9fec6

- **example_id**: `dev:qf8cbcec9fec6`
- **state**: `completed`
- **query**: How has the ratio of Ingersoll Rand’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9688823411593558 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5=0.0 · skipped= · n_scored=117

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf8cbcec9fec6:chunk-52` | 0.8396 |  | # Compensation Discussion and Analysis (cont.) ## ACCELERATE GROWTH <figure description="This image shows a stylized lo… |
| 2 | `qf8cbcec9fec6:chunk-51` | 0.017499999999999998 |  | # Compensation Discussion and Analysis (cont.) ## RECORD ORDERS OF $6,822M UP 7% OVER 2022 REVENUES OF $6,876M UP 16% O… |
| 3 | `qf8cbcec9fec6:chunk-116` | 0.0173 |  | # INGERSOLL RAND INC. AND SUBSIDIARIES UNAUDITED SUPPLEMENTAL ADJUSTED COMBINED FINANCIAL INFORMATION RECONCILIATION OF… |
| 4 | `qf8cbcec9fec6:chunk-111` | 0.0067 |  | # Annex A (cont.) ## RECONCILIATION OF GAAP MEASURES TO NON-GAAP MEASURES In addition to consolidated GAAP financial me… |
| 5 | `qf8cbcec9fec6:chunk-55` | 0.0014 |  | # Compensation Discussion and Analysis (cont.) ## ALLOCATE CAPITAL EFFECTIVELY (cont.) - 7 The use by Ingersoll Rand of… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qf8cbcec9fec6`)._

### ex-dev-qf8e3e71e08c9

- **example_id**: `dev:qf8e3e71e08c9`
- **state**: `completed`
- **query**: How has Principal Financial Group’s retirement solutions segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-Q` · used=True
- **S2**: nDCG@5=0.9129675424759451 · skipped= · n_scored=103

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf8e3e71e08c9:chunk-2` | 1.1705 | 2.0 | # From our CEO (cont.) ## Delivering comprehensive retirement solutions Retirement is a significant and growing opportu… |
| 2 | `qf8e3e71e08c9:chunk-8` | 0.5930000000000001 | 1.0 | # Proxy Summary (cont.) ## Corporate Snapshot Full year 2023 net income attributable to Principal Financial Group, Inc.… |
| 3 | `qf8e3e71e08c9:chunk-1` | 0.28040000000000004 | 1.0 | # From our CEO (cont.) ## Evolving our asset management business In 2023, we integrated our global capabilities across … |
| 4 | `qf8e3e71e08c9:chunk-3` | 0.18460000000000001 |  | # From our CEO (cont.) ## Achieving strong results We delivered strong results in 2023, ending the year with momentum a… |
| 5 | `qf8e3e71e08c9:chunk-0` | 0.0876 | 1.0 | # UNITED STATES SECURITIES AND EXCHANGE COMMISSION Washington, D.C. 20549 # SCHEDULE 14A Proxy Statement Pursuant to Se… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qf8e3e71e08c9`)._

### ex-dev-qf9c15fa46d48

- **example_id**: `dev:qf9c15fa46d48`
- **state**: `completed`
- **query**: How has the ratio of Live Nation Entertainment’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.788088263175707 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=12

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf9c15fa46d48:chunk-3` | 0.35209999999999997 | 1.0 | # FINANCIAL HIGHLIGHTS - THIRD QUARTER (unaudited; $ in millions) (cont.) FINANCIAL HIGHLIGHTS - NINE MONTHS (unaudited… |
| 2 | `qf9c15fa46d48:chunk-2` | 0.3257 |  | # FINANCIAL HIGHLIGHTS - THIRD QUARTER (unaudited; $ in millions) <table><tr><th></th><th>Q3 2023 Reported</th><th>Q3 2… |
| 3 | `qf9c15fa46d48:chunk-0` | 0.2213 |  | # LIVE NATION ENTERTAINMENT REPORTS THIRD QUARTER 2023 RESULTS <figure description={The image shows Live Nation's Q3 20… |
| 4 | `qf9c15fa46d48:chunk-10` | 0.0473 |  | # LIVE NATION ENTERTAINMENT, INC. CONSOLIDATED STATEMENTS OF OPERATIONS (unaudited) <table><tr><th></th><th colspan="2"… |
| 5 | `qf9c15fa46d48:chunk-1` | 0.0249 |  | # ticketmaster (cont.) ## LIVE NATION SPONSORSHIP - Sponsorship performance driven by global platforms (vs 3Q22) - Reve… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qf9c15fa46d48`)._

### ex-dev-qfa38830206fb

- **example_id**: `dev:qfa38830206fb`
- **state**: `completed`
- **query**: How does The Clorox Company manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7168795886624337 · gold=['DEF14A', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`DEF14A` · used=True
- **S2**: nDCG@5=1.0 · skipped= · n_scored=50

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qfa38830206fb:chunk-30` | 0.9148000000000001 | 2.0 | PART II ITEM 5. MARKET FOR REGISTRANT’S COMMON EQUITY, RELATED STOCKHOLDER MATTERS AND ISSUER PURCHASES OF EQUITY SECUR… |
| 2 | `qfa38830206fb:chunk-31` | 0.2378 |  | ##[a]##[b]####[c]##[d] Period##Total Number of Shares Purchased##Average Price Paid per Share (1)####Total Number of Sh… |
| 3 | `qfa38830206fb:chunk-35` | 0.1301 |  | PART III ITEM 10. DIRECTORS, EXECUTIVE OFFICERS AND CORPORATE GOVERNANCE See “Information about our Executive Officers”… |
| 4 | `qfa38830206fb:chunk-41` | 0.0459 |  | ####Incorporated by Reference###### Exhibit Number##Exhibit Description##Form##File No.##Exhibit##Filing Date 10.24*##A… |
| 5 | `qfa38830206fb:chunk-39` | 0.0412 |  | ####Incorporated by Reference###### Exhibit Number##Exhibit Description##Form##File No.##Exhibit##Filing Date 10.2*##Th… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qfa38830206fb`)._

### ex-dev-qfbef9973c7fb

- **example_id**: `dev:qfbef9973c7fb`
- **state**: `completed`
- **query**: What clarification did management provide on margin durability in the face of potential memory‑cost inflation?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=1.0 · skipped= · n_scored=74

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qfbef9973c7fb:chunk-49` | 1.0226 | 1.0 | Yes, thanks for the question. We highlighted in our opening remarks, really about our Q4 results and our outlook for Q1… |
| 2 | `qfbef9973c7fb:chunk-5` | 0.6206 | 1.0 | Thanks, Simona. Q4 was another record quarter. Revenue of $22.1 billion was up 22% sequentially and up 265% year-on-yea… |
| 3 | `qfbef9973c7fb:chunk-47` | 0.5026 |  | Congratulations on the results. Colette, I wanted to talk about your comment regarding gross margins and that it should… |
| 4 | `qfbef9973c7fb:chunk-43` | 0.0373 |  | Yes. So let me highlight on those three different areas of how we look at our suppliers. You're correct. Our inventory … |
| 5 | `qfbef9973c7fb:chunk-29` | 0.018799999999999997 |  | Yes. The first thing is overall, our supply is improving. Overall, our supply chain is just doing an incredible job for… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qfbef9973c7fb`)._

### ex-dev-qfd572ccfcb0f

- **example_id**: `dev:qfd572ccfcb0f`
- **state**: `completed`
- **query**: What investor views emerged on Hasbro’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6107229205982195 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`10-K` · used=True
- **S2**: nDCG@5=0.0 · skipped= · n_scored=154

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qfd572ccfcb0f:chunk-95` | 0.3397 |  | Item 2. Management's Discussion and Analysis of Financial Condition and Results of Operations. OBJECTIVE Our objective … |
| 2 | `qfd572ccfcb0f:chunk-15` | 0.25389999999999996 |  | HASBRO, INC. AND SUBSIDIARIES Condensed Notes to Consolidated Financial Statements (Millions of Dollars and Shares Exce… |
| 3 | `qfd572ccfcb0f:chunk-103` | 0.1653 |  | FRANCHISE BRANDS: Net revenues in the Franchise Brands portfolio increased 8% in the third quarter of 2023 compared to … |
| 4 | `qfd572ccfcb0f:chunk-101` | 0.1014 |  | 2022 •Net charges of $49.4 million, or $0.36 per diluted share for both the quarter and nine-month periods ended Septem… |
| 5 | `qfd572ccfcb0f:chunk-145` | 0.07279999999999999 |  | and evaluating the Company's reported financial results include film and television production costs, recoverability of… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qfd572ccfcb0f`)._

### ex-dev-qff56bedc2f87

- **example_id**: `dev:qff56bedc2f87`
- **state**: `completed`
- **query**: What questions were asked about Globe Life Inc.’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9293449960425915 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5=0.43067655807339306 · skipped= · n_scored=114

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff56bedc2f87:chunk-67` | 0.2598 |  | I'd say it would be more of a shift toward -- we're still not going to take our foot off the gas from a recruiting pers… |
| 2 | `qff56bedc2f87:chunk-7` | 0.022099999999999998 |  | Thank you, Frank. At American Income Life, life premiums were up 7% over the year ago quarter to $406 million, and life… |
| 3 | `qff56bedc2f87:chunk-11` | 0.0058 |  | Thanks, Frank. First, let me spend a few minutes discussing our share repurchase program, available liquidity and capit… |
| 4 | `qff56bedc2f87:chunk-19` | 0.0042 | 1.0 | Jimmy, you reflect the full difference between what we had expected in our valuation assumptions versus what we actuall… |
| 5 | `qff56bedc2f87:chunk-85` | 0.003 |  | Well, on Family Heritage, for sure, it's driven based on agent count. We rolled out a CRM system in 2023. So that helpe… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qff56bedc2f87`)._

### ex-dev-qff73996028bf

- **example_id**: `dev:qff73996028bf`
- **state**: `completed`
- **query**: How has Williams-Sonoma’s management addressed supply-chain risks and efforts to enhance Williams-Sonoma’s resilience?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5=0.7020976466720956 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff73996028bf:chunk-2` | 1.1484 | 2.0 | Table of Contents SUPPLIERS We purchase most of our merchandise from numerous foreign and domestic manufacturers and im… |
| 2 | `qff73996028bf:chunk-39` | 1.045 | 2.0 | Table of Contents Elevating our World-Class Customer Service We are continuing to improve our world-class customer serv… |
| 3 | `qff73996028bf:chunk-0` | 0.764 | 1.0 | PART I ITEM 1. BUSINESS OVERVIEW Williams-Sonoma, Inc., (the "Company”, "we", or "us") incorporated in 1973, is an omni… |
| 4 | `qff73996028bf:chunk-37` | 0.6775 | 1.0 | Table of Contents ITEM 7. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The fol… |
| 5 | `qff73996028bf:chunk-10` | 0.6609 | 1.0 | Table of Contents particularly seasonal, such as the home furnishings business, face a higher risk of harm from operati… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `dev:qff73996028bf`)._

### ex-eval-chunk-only-chunk-q0b530d

- **example_id**: `eval:chunk-only:chunk_q0b530d`
- **state**: `completed`
- **query**: How does Brown-Forman view the pace of product innovation cycles and their effect on market competitiveness in the spirits industry?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=90

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q0b530d:10-K:chunk-5` | 1.048 |  | Thank you, Sue, and good morning, everyone. Thank you for joining us today as we share Brown-Forman's fiscal 2024 resul… |
| 2 | `chunk_q0b530d:10-K:chunk-63` | 1.0108000000000001 |  | All right. So first -- hit the Jack one first. Well, for one, in the short term, and then I'll take it a little bit lon… |
| 3 | `chunk_q0b530d:10-K:chunk-61` | 0.543 |  | Lawson, I had two questions. First was just on Jack Daniel's, given all the kind of line extension over the years and d… |
| 4 | `chunk_q0b530d:10-K:chunk-7` | 0.34900000000000003 |  | Thank you, Lawson, and good morning, everyone. As Lawson has thoroughly reviewed our top line growth and the performanc… |
| 5 | `chunk_q0b530d:10-K:chunk-65` | 0.1323 |  | And the one thing I'll add to that is for el Jimador specifically, when you look at Brown-Forman's pricing in tequila v… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:chunk-only:chunk_q0b530d`)._

### ex-eval-chunk-only-chunk-q29280e

- **example_id**: `eval:chunk-only:chunk_q29280e`
- **state**: `completed`
- **query**: How does Atmos Energy Corporation manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=83

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q29280e:10-K:chunk-24` | 0.6021000000000001 |  | # Director Compensation (cont.) ## Fiscal 2023 Annual Compensation The Board believes that the level of non-employee di… |
| 2 | `chunk_q29280e:10-K:chunk-25` | 0.5711 |  | # Director Compensation (cont.) ## Long-Term Compensation Each non-employee director is also eligible to participate in… |
| 3 | `chunk_q29280e:10-K:chunk-40` | 0.5256 |  | # 2023 Elements of Compensation (cont.) ## Performance Levels and Achievement The following table summarizes the perfor… |
| 4 | `chunk_q29280e:10-K:chunk-75` | 0.46609999999999996 |  | # Security Ownership of Directors, Nominees, and Executive Officers The following table lists the beneficial ownership … |
| 5 | `chunk_q29280e:10-K:chunk-47` | 0.4114 |  | # Roles and Responsibilities (cont.) ## Compensation Risk Assessment The HR Committee reviews our compensation programs… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:chunk-only:chunk_q29280e`)._

### ex-eval-chunk-only-chunk-q2ccba5

- **example_id**: `eval:chunk-only:chunk_q2ccba5`
- **state**: `completed`
- **query**: What questions were asked about Boston Scientific’s customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q2ccba5:Earnings:chunk-13` | 0.1547 |  | Great. Congrats on a really good quarter. And congratulations, Lauren, on the promotion. Wanted to ask on two of the bi… |
| 2 | `chunk_q2ccba5:Earnings:chunk-99` | 0.0701 |  | Congrats, Lauren. I'd like to stick with Axonics, if that's right. I appreciate it hasn't closed yet. But I'm just kind… |
| 3 | `chunk_q2ccba5:Earnings:chunk-63` | 0.0153 |  | Maybe one more follow-up on TAVR. Could you remind us what the interim look was? Was that just like a 6-month look at t… |
| 4 | `chunk_q2ccba5:Earnings:chunk-85` | 0.0152 |  | Yes. Just a few clarifying points. Again, in Europe, where we set 70,000 valves and physicians use it routinely on an e… |
| 5 | `chunk_q2ccba5:Earnings:chunk-101` | 0.0123 |  | Sure. Well, we haven't closed it yet. We hope to first half of this year. The team at Axonics has done an amazing job w… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:chunk-only:chunk_q2ccba5`)._

### ex-eval-chunk-only-chunk-q44d295

- **example_id**: `eval:chunk-only:chunk_q44d295`
- **state**: `completed`
- **query**: How has the ratio of Amphenol Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=235

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q44d295:10-Q:chunk-45` | 0.0524 |  | Reportable Business Segments The Company aligns its businesses into the following three reportable business segments: ●… |
| 2 | `chunk_q44d295:10-Q:chunk-109` | 0.0285 |  | control of the goods transfers, rather than when the goods are delivered, and title, risk and reward of ownership are p… |
| 3 | `chunk_q44d295:10-Q:chunk-85` | 0.0268 |  | Critical Accounting Estimates The preparation of consolidated financial statements in conformity with accounting princi… |
| 4 | `chunk_q44d295:10-Q:chunk-59` | 0.009300000000000001 |  | (1) Percentages in this table were calculated using actual, unrounded results; therefore, the sum of the components may… |
| 5 | `chunk_q44d295:10-Q:chunk-44` | 0.0073 |  | Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations (amounts in millions, exc… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:chunk-only:chunk_q44d295`)._

### ex-eval-chunk-only-chunk-q5ebb5e

- **example_id**: `eval:chunk-only:chunk_q5ebb5e`
- **state**: `completed`
- **query**: How has investor sentiment shifted following The AES Corporation’s most recent earnings release?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q5ebb5e:Earnings:chunk-39` | 0.6194999999999999 |  | # EXECUTIVE COMPENSATION COMPENSATION DISCUSSION AND ANALYSIS ("CD&A") (cont.) ## Executive Summary 2023 was a strong y… |
| 2 | `chunk_q5ebb5e:Earnings:chunk-78` | 0.1512 |  | # Pay Versus Performance Disclosure (cont.) ## Pay Versus Performance Relationship Descriptions <table><tr><th>Period</… |
| 3 | `chunk_q5ebb5e:Earnings:chunk-97` | 0.017599999999999998 |  | # QUESTIONS AND ANSWERS REGARDING THE PROXY STATEMENT AND ANNUAL MEETING (cont.) ## Adjusted EPS We define Adjusted EPS… |
| 4 | `chunk_q5ebb5e:Earnings:chunk-48` | 0.013 |  | # Overview of AES Total Compensation (cont.) ## Overall score is 127%1 (1) The AES Corporate Performance score is round… |
| 5 | `chunk_q5ebb5e:Earnings:chunk-13` | 0.009899999999999999 |  | # CORPORATE GOVERNANCE AT AES (cont.) ## Sustainable Operations Incorporate our business principles and practices in ou… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:chunk-only:chunk_q5ebb5e`)._

### ex-eval-chunk-only-chunk-q829eae

- **example_id**: `eval:chunk-only:chunk_q829eae`
- **state**: `completed`
- **query**: What guidance was offered on Amazon’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q829eae:10-Q:chunk-77` | 0.759 |  | Table of Contents and related transaction costs are included in “Fulfillment,” AWS costs are primarily classified as “T… |
| 2 | `chunk_q829eae:10-Q:chunk-96` | 0.4214 |  | Table of Contents •the extent to which we invest in technology and infrastructure, fulfillment, and other expense categ… |
| 3 | `chunk_q829eae:10-Q:chunk-99` | 0.3709 |  | Table of Contents •for foreign transactions, additional risks related to the integration of operations across different… |
| 4 | `chunk_q829eae:10-Q:chunk-94` | 0.1885 |  | Table of Contents fears or rising inflation, natural or human-caused disasters (including public health crises) or extr… |
| 5 | `chunk_q829eae:10-Q:chunk-66` | 0.1616 |  | Our principal sources of liquidity are cash flows generated from operations and our cash, cash equivalents, and marketa… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:chunk-only:chunk_q829eae`)._

### ex-eval-chunk-only-chunk-q8fc814

- **example_id**: `eval:chunk-only:chunk_q8fc814`
- **state**: `completed`
- **query**: What guidance was offered on Apollo Global Management’s fundraising targets for new investment vehicles?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '8-K', '10-Q', '10-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=78

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q8fc814:Earnings:chunk-7` | 1.2795 |  | Thanks, Marc. Echoing Marc's sentiment. We entered 2023 focused squarely on executing the growth plan we set forth, and… |
| 2 | `chunk_q8fc814:Earnings:chunk-63` | 1.2204000000000002 |  | Sure. So ADIP 2 fundraising, going quite well. We expect to wrap it up this summer in the $4 billion to $5 billion rang… |
| 3 | `chunk_q8fc814:Earnings:chunk-25` | 1.2125 |  | So we -- when we set out our 5-year targets a little over 2 years ago, we -- the 5-year target was to get to $150 billi… |
| 4 | `chunk_q8fc814:Earnings:chunk-31` | 0.575 |  | So some of it is more boots on the ground and building out what we call high-grade alpha or high-grade solutions. And t… |
| 5 | `chunk_q8fc814:Earnings:chunk-65` | 0.5573 |  | Yes. The color I would give in this -- and this is as you evaluate entering into this business. The reason we are succe… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:chunk-only:chunk_q8fc814`)._

### ex-eval-chunk-only-chunk-q9fad72

- **example_id**: `eval:chunk-only:chunk_q9fad72`
- **state**: `completed`
- **query**: What guidance was offered on CDW Corporation’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', 'DEF14A', '8-K']`
- **yield**: original=`10-Q` · effective=`10-Q` · used=False
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q9fad72:10-Q:chunk-64` | 0.7355 |  | (1)Represents the rolling three-month average of the balance of Accounts receivable, net at the end of the period, divi… |
| 2 | `chunk_q9fad72:10-Q:chunk-16` | 0.7098 |  | If we are unable to attract, develop, engage and retain key personnel, or if our approach to workforce management is in… |
| 3 | `chunk_q9fad72:10-Q:chunk-62` | 0.5388000000000001 |  | (1)Includes items such as depreciation and amortization, deferred income taxes, provision for credit losses and equity-… |
| 4 | `chunk_q9fad72:10-Q:chunk-3` | 0.5197999999999999 |  | In our US business, which represents approximately 90% of our Net sales, we currently have five dedicated customer chan… |
| 5 | `chunk_q9fad72:10-Q:chunk-14` | 0.4206 |  | •keep pace with changes and innovation and compete effectively; •effectuate comprehensive and reliable data collection,… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:chunk-only:chunk_q9fad72`)._

### ex-eval-doc-q0617ad

- **example_id**: `eval:doc_q0617ad`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did F5’s leadership say about F5’s share repurchase plans?
- **S1**: top1=`8-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['8-K', '10-K', 'DEF14A', 'Earnings', '10-Q']`
- **yield**: original=`8-K` · effective=`8-K` · used=False
- **S2**: nDCG@5= · skipped=empty_top1_chunks (routing/yield empty pool, not Score failure) · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:doc_q0617ad`)._

### ex-eval-doc-q48ce69

- **example_id**: `eval:doc_q48ce69`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did energy cost inflation impact theme park utility expenses
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **yield**: original=`Earnings` · effective=`Earnings` · used=False
- **S2**: nDCG@5= · skipped=empty_top1_chunks (routing/yield empty pool, not Score failure) · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:doc_q48ce69`)._

### ex-eval-doc-q737b56

- **example_id**: `eval:doc_q737b56`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Deckers Outdoor Corporation’s customer retention metrics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'DEF14A', 'Earnings']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5= · skipped=empty_top1_chunks (routing/yield empty pool, not Score failure) · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:doc_q737b56`)._

### ex-eval-doc-qa9fda3

- **example_id**: `eval:doc_qa9fda3`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does The AES Corporation account for currency and economic volatility in its risk management disclosures?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **yield**: original=`10-K` · effective=`10-K` · used=False
- **S2**: nDCG@5= · skipped=empty_top1_chunks (routing/yield empty pool, not Score failure) · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/yield-unsloth-score-paper-n200.inspect.html) (search for `eval:doc_qa9fda3`)._
