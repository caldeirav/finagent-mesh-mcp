# Pair `anyjev-l0-bm25` — `paper-p1-ceilings-n200`

[← compact index](../paper-p1-ceilings-n200.inspect.md) · **Download full HTML**: [raw](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) · [`paper-p1-ceilings-n200.inspect.html`](../paper-p1-ceilings-n200.inspect.html)

- eval_run_id: `paper-p1-ceilings-n200:anyjev-l0-bm25`
- S1=`anyjev-l0` · S2=`bm25-stage2`
- row status: `completed` · completed=128 · failed_retriable=72

## Examples

### ex-dev-chunk-only-q075970f6eb46

- **example_id**: `dev:chunk-only:q075970f6eb46`
- **state**: `completed`
- **query**: What did Fastenal Company’s leadership say about Fastenal Company’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5=0.16958010263680806 · skipped= · n_scored=105

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q075970f6eb46:DEF14A:chunk-103` | 17.84491678602162 |  | ####FASTENAL COMPANY Date: October 17, 2023##By:##/s/ Holden Lewis ####Holden Lewis ####Senior Executive Vice President… |
| 2 | `q075970f6eb46:DEF14A:chunk-100` | 17.613722849712424 |  | Exhibit Number##Description of Document 3.1##Restated Articles of Incorporation of Fastenal Company, as amended (incorp… |
| 3 | `q075970f6eb46:DEF14A:chunk-36` | 12.154775690094953 | 1.0 | FASTENAL COMPANY AND SUBSIDIARIES Notes to Condensed Consolidated Financial Statements (Amounts in millions except shar… |
| 4 | `q075970f6eb46:DEF14A:chunk-12` | 11.642689581569385 |  | FASTENAL COMPANY AND SUBSIDIARIES Condensed Consolidated Statements of Cash Flows (Amounts in millions) |
| 5 | `q075970f6eb46:DEF14A:chunk-6` | 11.642689581569385 |  | FASTENAL COMPANY AND SUBSIDIARIES Condensed Consolidated Statements of Comprehensive Income (Amounts in millions) |

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
| 1 | `q0fd4ca04c0a5:10-K:chunk-91` | 15.896372254357136 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS 1. Organization and Basis of Presentation Organization and Operations Molina… |
| 2 | `q0fd4ca04c0a5:10-K:chunk-32` | 15.316698987572629 |  | Our use and disclosure of personally identifiable information and other non-public information, including protected hea… |
| 3 | `q0fd4ca04c0a5:10-K:chunk-8` | 15.29015520513182 |  | continue to focus on driving market share gains through improved execution of enrollment and retention. Approximately $… |
| 4 | `q0fd4ca04c0a5:10-K:chunk-108` | 15.245020278014287 |  | Bright Health Medicare. We closed on this acquisition effective January 1, 2024 for $441 million, which will be part of… |
| 5 | `q0fd4ca04c0a5:10-K:chunk-17` | 15.073177802082379 | 1.0 | insight into the needs of both our members and our providers. Physicians We contract with both primary care physicians … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q0fd4ca04c0a5`)._

### ex-dev-chunk-only-q299865e6e67e

- **example_id**: `dev:chunk-only:q299865e6e67e`
- **state**: `completed`
- **query**: What dependency risks exist for Consolidated Edison due to concentration of revenue in a limited number of service territories or customer segments?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.21826955258437686 · skipped= · n_scored=286

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q299865e6e67e:10-K:chunk-114` | 18.961157256651905 |  | are invoiced to customers according to contractual billing terms, that generally occur when deliveries or other perform… |
| 2 | `q299865e6e67e:10-K:chunk-7` | 17.85806539967404 |  | FORWARD-LOOKING STATEMENTS This report contains forward-looking statements that are intended to qualify for the safe-ha… |
| 3 | `q299865e6e67e:10-K:chunk-166` | 17.685130811820848 | 2.0 | and gas businesses may impact the Companies’ future financial condition. The Utilities expect electric usage to increas… |
| 4 | `q299865e6e67e:10-K:chunk-262` | 17.632578911430922 | 1.0 | Cash Flows from Operating Activities The Utilities’ cash flows from operating activities primarily reflect their energy… |
| 5 | `q299865e6e67e:10-K:chunk-273` | 15.507956283961866 |  | transmission planning process. For local transmission upgrades, CECONY proposed the return on equity to be the lower of… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q299865e6e67e`)._

### ex-dev-chunk-only-q2a401c1edf73

- **example_id**: `dev:chunk-only:q2a401c1edf73`
- **state**: `completed`
- **query**: How often is Exxon Mobil Corporation’s executive compensation program reviewed and updated?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.5000306091488957 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2a401c1edf73:DEF14A:chunk-45` | 17.262666575883614 | 1.0 | # Table of Contents (cont.) ## DIRECTOR COMPENSATION Director compensation elements are designed to: - Ensure alignment… |
| 2 | `q2a401c1edf73:DEF14A:chunk-75` | 15.64153353893406 | 1.0 | # 2023 COMPENSATION ACTIONS MANAGEMENT COMMITTEE (cont.) ## JACK P. WILLIAMS, JR., SENIOR VICE PRESIDENT (cont.) Angela… |
| 3 | `q2a401c1edf73:DEF14A:chunk-58` | 15.360771439265903 | 2.0 | # COMPENSATION DESIGN (cont.) ## PROMOTE RETENTION Long-term orientation also underpins how the Company develops talent… |
| 4 | `q2a401c1edf73:DEF14A:chunk-43` | 15.25390640549288 | 2.0 | # Table of Contents ## Compensation Committee The Compensation Committee is comprised exclusively of non-employee, inde… |
| 5 | `q2a401c1edf73:DEF14A:chunk-77` | 14.382309352928326 |  | # OTHER COMPENSATION ELEMENTS (cont.) ## TAX MATTERS The Company does not provide tax assistance for either bonus or pe… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q2a401c1edf73`)._

### ex-dev-chunk-only-q3a71644741b7

- **example_id**: `dev:chunk-only:q3a71644741b7`
- **state**: `completed`
- **query**: What questions were asked about Conagra Brands’ customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.18773177839127778 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3a71644741b7:Earnings:chunk-1` | 9.678858332906223 |  | Good morning, everyone, and welcome to the Conagra Brands Q4 and Fiscal Year 2024 Earnings Conference Call. [Operator I… |
| 2 | `q3a71644741b7:Earnings:chunk-43` | 7.782922543516077 |  | That's helpful. And then Sean, just kind of thinking about the productivity number, and it's a question being asked of … |
| 3 | `q3a71644741b7:Earnings:chunk-61` | 7.360811482970191 | 1.0 | Sean, you have a lot of brands that skew more heavily towards lower-income consumers. You have a lot of brands that ske… |
| 4 | `q3a71644741b7:Earnings:chunk-101` | 6.831352888711425 |  | Got it. Yes, fair enough. And then just maybe quickly for Dave. I normally don't ask about impairments, but clearly cal… |
| 5 | `q3a71644741b7:Earnings:chunk-7` | 6.005283381538791 | 2.0 | Sean, you talked in the prepared remarks about expecting a sort of a gradual transition in fiscal '25 to a more normal … |

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
| 1 | `q40d417892141:Earnings:chunk-4` | 13.311308481040456 |  | •Consolidated revenues of approximately $36.0 billion to $37.3 billion •Homes closed by homebuilding operations of 87,0… |
| 2 | `q40d417892141:Earnings:chunk-1` | 9.65889097146325 |  | The Company's return on equity (ROE) was 21.8% for the trailing twelve months ended December 31, 2023, and homebuilding… |
| 3 | `q40d417892141:Earnings:chunk-5` | 9.484846909352566 |  | Forward-looking statements in this release include that we are well-positioned to meet changing market conditions with … |
| 4 | `q40d417892141:Earnings:chunk-3` | 5.353474661623474 |  | Forestar Group Inc. (NYSE:FOR) (“Forestar”) is a publicly traded residential lot development company that is a majority… |
| 5 | `q40d417892141:Earnings:chunk-0` | 5.019780317750246 |  | Exhibit 99.1 D.R. HORTON, INC., AMERICA’S BUILDER, REPORTS FISCAL 2024 FIRST QUARTER EARNINGS AND DECLARES QUARTERLY DI… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q40d417892141`)._

### ex-dev-chunk-only-q504aef305d62

- **example_id**: `dev:chunk-only:q504aef305d62`
- **state**: `completed`
- **query**: How did management describe the performance of the China market in Q4 2023?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.7227265726449517 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q504aef305d62:10-Q:chunk-5` | 15.69510162385353 | 2.0 | Thank you, Tiffany. Good morning, everyone. Welcome to Starbucks' Fourth Quarter and Fiscal Year 2023 Earnings Conferen… |
| 2 | `q504aef305d62:10-Q:chunk-7` | 13.941354609867503 | 2.0 | Thank you, Laxman, and good morning, everyone. I'm very pleased to discuss our strong Q4 and full fiscal year 2023 perf… |
| 3 | `q504aef305d62:10-Q:chunk-15` | 11.454927129412406 | 2.0 | Thank you for the question. Let me start with the answer here. Our brand in China is known as [ Shing Baka ] and it upl… |
| 4 | `q504aef305d62:10-Q:chunk-27` | 10.92349867387708 |  | The Americas operating margin, 23.2%, up over 4 points, could you provide a bridge or describe the biggest contributors… |
| 5 | `q504aef305d62:10-Q:chunk-23` | 10.753478959979576 |  | Thank you for the question. The way I'd look at the comp guidance is as we look at a very strong fiscal year 2023, and … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q504aef305d62`)._

### ex-dev-chunk-only-q5bb4a350edd8

- **example_id**: `dev:chunk-only:q5bb4a350edd8`
- **state**: `completed`
- **query**: How has aircraft delivery volume trended across the last four quarters for the F 35 program?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.04373502583744726 · skipped= · n_scored=98

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5bb4a350edd8:10-Q:chunk-13` | 13.605425604262035 |  | Okay. Thanks, Myles. On the margins for F-35, what we're seeing in 2024 are lower favorable profit adjustments, and so … |
| 2 | `q5bb4a350edd8:10-Q:chunk-7` | 13.020255530856657 |  | Thanks, Jim, and good morning, everyone. Today, I will recap our fourth quarter and full year 2023 financial results an… |
| 3 | `q5bb4a350edd8:10-Q:chunk-11` | 11.75540026537136 |  | I was hoping to lead off with Aero and F-35 in particular, and the margins, number one, that you're looking for in '24 … |
| 4 | `q5bb4a350edd8:10-Q:chunk-35` | 11.390897869551994 |  | Well, just some key things that we're talking about from a sales perspective. Lot 18, 19 is a big one for the F-35 prog… |
| 5 | `q5bb4a350edd8:10-Q:chunk-65` | 9.959486420532706 | 1.0 | Yes. Let me start with that question first, and I'll come back to the F-35. Just on the 2025 margins going forward, yes… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q5bb4a350edd8`)._

### ex-dev-chunk-only-q7b219decf5da

- **example_id**: `dev:chunk-only:q7b219decf5da`
- **state**: `completed`
- **query**: What did Everest Group, Ltd.’s leadership say about Everest Group, Ltd.’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=138

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7b219decf5da:DEF14A:chunk-3` | 24.194727816329827 |  | Good morning, everyone, and welcome to the Everest Group, Ltd. Fourth Quarter of 2023 Earnings Conference Call. The Eve… |
| 2 | `q7b219decf5da:DEF14A:chunk-1` | 17.086922028830013 |  | Good day, and welcome to the Everest Group Fourth Quarter 2023 Earnings Conference Call. [Operator Instructions] Please… |
| 3 | `q7b219decf5da:DEF14A:chunk-107` | 13.693624480332504 |  | Just one for me. If we think about your 2024, 2026 objectives, let's say, social inflation continues to kind of nag. So… |
| 4 | `q7b219decf5da:DEF14A:chunk-83` | 8.517634201619579 |  | Sure. Greg, this is Jim Williamson. Thanks for the question. Everest did have another excellent Jan 1 renewals. You've … |
| 5 | `q7b219decf5da:DEF14A:chunk-5` | 7.602121658337953 |  | Thank you, Matt. Good morning, everyone. Thank you for joining us. 2023 was the most profitable year in our history. We… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q7b219decf5da`)._

### ex-dev-chunk-only-q7ca4de540868

- **example_id**: `dev:chunk-only:q7ca4de540868`
- **state**: `completed`
- **query**: How does Hologic view the pace of innovation cycles in women's health diagnostics and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.23307160661695003 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ca4de540868:10-K:chunk-67` | 26.536912664760635 | 1.0 | # Compensation Discussion and Analysis (cont.) ## 2023 Business Strategy & Performance Highlights (cont.) Finally, our … |
| 2 | `q7ca4de540868:10-K:chunk-32` | 23.755025664028658 | 1.0 | # Our Board's Role and Responsibilities (cont.) ## A Champion for Women's Health We are committed to improving women's … |
| 3 | `q7ca4de540868:10-K:chunk-11` | 22.033062841761968 |  | # PERCENT OF WOMEN ON HOLOGIC BOARD (cont.) ## Board Practices ## Stockholder Matters - Annual election of directors - … |
| 4 | `q7ca4de540868:10-K:chunk-8` | 21.27201681331833 | 1.0 | # Performance Highlights (cont.) 15.6% WORLDWIDE ORGANIC REVENUE GROWTH EX. COVID-19 15.6% organic growth in constant c… |
| 5 | `q7ca4de540868:10-K:chunk-31` | 20.742456813137558 |  | # Our Board's Role and Responsibilities (cont.) ## Philanthropy and Community Support Our Company's response to the COV… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q7ca4de540868`)._

### ex-dev-chunk-only-q7ff47a7d2a20

- **example_id**: `dev:chunk-only:q7ff47a7d2a20`
- **state**: `completed`
- **query**: How does Consolidated Edison, Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.05652670087893601 · skipped= · n_scored=212

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ff47a7d2a20:10-K:chunk-168` | 16.62631018644358 |  | # QUESTIONS AND ANSWERS ABOUT THE 2024 ANNUAL MEETING AND VOTING (cont.) ## Why Did / Receive a Notice of Internet Avai… |
| 2 | `q7ff47a7d2a20:10-K:chunk-170` | 15.301316268060924 |  | # Can I Request A Paper Copy Of The Proxy Statement And Annual Report? (cont.) ## How Many Votes Must Be Present to Hol… |
| 3 | `q7ff47a7d2a20:10-K:chunk-105` | 15.147691460499683 | 1.0 | # Long-Term Incentive Compensation (cont.) ## 2023 LTIP Awards (cont.) The share price for the performance-based awards… |
| 4 | `q7ff47a7d2a20:10-K:chunk-169` | 14.0134981046555 |  | # Can I Request A Paper Copy Of The Proxy Statement And Annual Report? The Company's Proxy Statement and Annual Report … |
| 5 | `q7ff47a7d2a20:10-K:chunk-186` | 12.779062268596107 |  | # APPENDIX D (cont.) ## ARTICLE 1. DEFINITIONS (a) "Account" means a custodian account established with the Agent to ho… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q7ff47a7d2a20`)._

### ex-dev-chunk-only-q853c16a74704

- **example_id**: `dev:chunk-only:q853c16a74704`
- **state**: `completed`
- **query**: What did Tapestry’s management say about Tapestry’s margin outlook and initiatives to improve profitability?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.42080338500822784 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q853c16a74704:Earnings:chunk-3` | 12.411992101479026 |  | Good morning. Thank you for joining us. With me today to discuss our fourth quarter and year-end results as well as our… |
| 2 | `q853c16a74704:Earnings:chunk-47` | 12.37233492558887 | 1.0 | Well, we are building and continue to drive a healthy business. That's been our focus, not only in China, but around th… |
| 3 | `q853c16a74704:Earnings:chunk-33` | 11.475303193992007 | 2.0 | Yes. Thanks. First, in North America, Coach delivered slight growth in the fourth quarter and it was at incredible marg… |
| 4 | `q853c16a74704:Earnings:chunk-83` | 11.278256038321246 | 1.0 | So I'll start with Michael Kors. And what we're seeing in our business and what our platform has been delivering is del… |
| 5 | `q853c16a74704:Earnings:chunk-35` | 11.254134124165708 | 2.0 | A very brief add to your specific question as it relates to what's driving gross margin. It's really the structural dri… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q853c16a74704`)._

### ex-dev-chunk-only-q90faabe2b483

- **example_id**: `dev:chunk-only:q90faabe2b483`
- **state**: `completed`
- **query**: What operational risks related to technology or IT systems has UDR, Inc. highlighted, and how are these managed?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=31

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q90faabe2b483:10-K:chunk-30` | 12.829322331629532 | 1.0 | # FORWARD LOOKING STATEMENTS Certain statements made in this presentation may constitute "forward-looking statements." … |
| 2 | `q90faabe2b483:10-K:chunk-15` | 12.36802938469248 | 1.0 | # FORWARD LOOKING STATEMENTS Certain statements made in this presentation may constitute "forward-looking statements. W… |
| 3 | `q90faabe2b483:10-K:chunk-9` | 10.501853002881402 |  | # RECENT EXTERNAL GROWTH ACTIVITY (cont.) ## Texas Acquisitions (cont.) Investment Thesis Ability to increase operating… |
| 4 | `q90faabe2b483:10-K:chunk-7` | 10.489733127073785 |  | # ACCRETIVE CAPITAL ALLOCATION Our wide variety of value creation drivers provides UDR the latitude to pivot toward inv… |
| 5 | `q90faabe2b483:10-K:chunk-22` | 9.502598381778052 |  | # DEFINITIONS AND RECONCILIATIONS (cont.) Net Operating Income ("NOI"): The Company defines NOI as rental income less d… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:q90faabe2b483`)._

### ex-dev-chunk-only-q9ee9b517f484

- **example_id**: `dev:chunk-only:q9ee9b517f484`
- **state**: `completed`
- **query**: What feedback have investors provided regarding Valero Energy Corporation’s refining margin outlook?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.14606834984270645 · skipped= · n_scored=203

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9ee9b517f484:Earnings:chunk-83` | 9.694390433394526 |  | VALERO ENERGY CORPORATION CONDENSED NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Continued) •Investments in AFS debt sec… |
| 2 | `q9ee9b517f484:Earnings:chunk-42` | 9.589780231256615 |  | VALERO ENERGY CORPORATION CONDENSED NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Continued) 6. VARIABLE INTEREST ENTITIE… |
| 3 | `q9ee9b517f484:Earnings:chunk-69` | 9.38054474738056 |  | VALERO ENERGY CORPORATION CONDENSED NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Continued) 10. SUPPLEMENTAL CASH FLOW I… |
| 4 | `q9ee9b517f484:Earnings:chunk-19` | 8.00137526902101 | 1.0 | VALERO ENERGY CORPORATION CONDENSED NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Continued) California Energy Commission… |
| 5 | `q9ee9b517f484:Earnings:chunk-183` | 7.959162366108139 |  | As previously noted, our operations generated $8.5 billion of cash in the first nine months of 2022, driven primarily b… |

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
| 1 | `qa431f3f55a5e:10-K:chunk-77` | 14.422148806772409 |  | Exhibit Number##Description 3.1##Certificate of Incorporation (incorporated herein by reference to Exhibit 3.1 to the C… |
| 2 | `qa431f3f55a5e:10-K:chunk-80` | 13.933213406373627 |  | 10.19†##Consultancy Agreement by and between Landmark Business Development Limited, Balazs Fejes and EPAM Systems, Inc.… |
| 3 | `qa431f3f55a5e:10-K:chunk-91` | 13.888882128094705 |  | Table of Contents REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM To the Stockholders and the Board of Director… |
| 4 | `qa431f3f55a5e:10-K:chunk-9` | 12.849025210844374 |  | Table of Contents We also enter into confidentiality agreements with our customers and suppliers to protect information… |
| 5 | `qa431f3f55a5e:10-K:chunk-93` | 12.48964214654673 |  | Table of Contents REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM To the Stockholders and the Board of Director… |

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
| 1 | `qaf2d41946676:10-K:chunk-119` | 6.917865010713681 |  | The Crown Rock acquisition stood on its own in terms of quality and how it fit within our portfolio in the Midland Basi… |
| 2 | `qaf2d41946676:10-K:chunk-37` | 6.58399871378194 |  | So if you look at our -- what we've said we'll spend in oil and gas is $4.8 billion to $5 billion in 2024. That -- part… |
| 3 | `qaf2d41946676:10-K:chunk-3` | 6.396574586458392 |  | Thank you, Gary. Good afternoon, everyone, and thank you for participating in Occidental's Fourth Quarter 2023 earnings… |
| 4 | `qaf2d41946676:10-K:chunk-15` | 5.6501747599323195 |  | Well, as you noted, by virtue of all the M&A that's happening, there's a lot of appetite for companies to try to get in… |
| 5 | `qaf2d41946676:10-K:chunk-5` | 5.648790572726347 |  | Thank you, Jordan, and good afternoon, everyone. 2023 was a great year for us, thanks to the performance of all of our … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qaf2d41946676`)._

### ex-dev-chunk-only-qb3a6bec7aedc

- **example_id**: `dev:chunk-only:qb3a6bec7aedc`
- **state**: `completed`
- **query**: What exposure to foreign exchange fluctuations did Citizens Financial Group, Inc. disclose and how is Citizens Financial Group, Inc. managing it?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.6843515475204854 · skipped= · n_scored=423

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb3a6bec7aedc:10-K:chunk-306` | 22.163329064328156 | 2.0 | NOTE 14 - DERIVATIVES In the normal course of business, Citizens enters into derivative transactions to meet the financ… |
| 2 | `qb3a6bec7aedc:10-K:chunk-125` | 19.329954631682085 | 2.0 | Capital Markets A key component of our capital markets activities is the underwriting and distribution of corporate cre… |
| 3 | `qb3a6bec7aedc:10-K:chunk-18` | 18.317773473557626 |  | Our framework for managing risks may not be effective in mitigating risk and loss. Our risk management framework is mad… |
| 4 | `qb3a6bec7aedc:10-K:chunk-116` | 17.86618846188663 |  | We continue to manage asset sensitivity within the scope of our policy, changing market conditions and changes in our b… |
| 5 | `qb3a6bec7aedc:10-K:chunk-112` | 17.37746966792677 | 2.0 | Lending authority is granted by the second line of defense credit risk function to each underwriter to ensure proper ov… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qb3a6bec7aedc`)._

### ex-dev-chunk-only-qb7d1dfae8271

- **example_id**: `dev:chunk-only:qb7d1dfae8271`
- **state**: `completed`
- **query**: What guidance was offered on International Flavors & Fragrances Inc.’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=304

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb7d1dfae8271:10-K:chunk-291` | 20.517334832807393 |  | Exhibit Number##Description 10.22(vi)##Third Amended and Restated Credit Agreement, dated as of July 28, 2021 among Int… |
| 2 | `qb7d1dfae8271:10-K:chunk-293` | 19.396610090044923 |  | Exhibit Number##Description 10.26(i)##Amendment No. 1 to Credit Agreement, dated as of August 25, 2020, by and among Nu… |
| 3 | `qb7d1dfae8271:10-K:chunk-285` | 19.085688525008557 |  | Exhibit Number##Description 2.1##Agreement and Plan of Merger, dated May 7, 2018, by and among the Registrant, Frutarom… |
| 4 | `qb7d1dfae8271:10-K:chunk-289` | 18.485966020763897 |  | Exhibit Number##Description *10.12##Form of Restricted Stock Units Award Agreement under the 2015 Stock Award and Incen… |
| 5 | `qb7d1dfae8271:10-K:chunk-296` | 17.296906492453864 |  | ##INTERNATIONAL FLAVORS & FRAGRANCES INC.## By:####/s/ Glenn Richter Name:####Glenn Richter Title:####Executive Vice Pr… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qb7d1dfae8271`)._

### ex-dev-chunk-only-qbcda53de470c

- **example_id**: `dev:chunk-only:qbcda53de470c`
- **state**: `completed`
- **query**: Which competitive advantages has Apple emphasized compared to peers?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5=0.13120507751234178 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbcda53de470c:10-K:chunk-79` | 6.214085910611805 |  | Okay. And as a follow-up, you obviously had a great Services quarter. And part of your Services business has these lice… |
| 2 | `qbcda53de470c:10-K:chunk-37` | 5.697796558759526 |  | Okay, very clear. And then maybe for you and Tim, you guys have been on the leading edge of innovation across hardware,… |
| 3 | `qbcda53de470c:10-K:chunk-3` | 5.267092433445796 |  | Thank you. Good afternoon, and thank you for joining us. Speaking first today is Apple's CEO, Tim Cook; and he'll be fo… |
| 4 | `qbcda53de470c:10-K:chunk-59` | 5.2391852410949795 |  | Got it, that's really helpful. And then maybe if I could ask you about Vision Pro, which I believe is supposed to be la… |
| 5 | `qbcda53de470c:10-K:chunk-5` | 5.2203982751805045 | 2.0 | Thank you, Suhasini. Good afternoon, everyone, and thanks for joining the call. Today, Apple is reporting revenue of $8… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qbcda53de470c`)._

### ex-dev-chunk-only-qd7ede96b88aa

- **example_id**: `dev:chunk-only:qd7ede96b88aa`
- **state**: `completed`
- **query**: What observations were made about TransDigm Group’s market share trends or competitive positioning in the aerospace components sector?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.4670156610640613 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd7ede96b88aa:10-K:chunk-59` | 24.14296172843977 | 2.0 | # Summary of Key NEO Compensation Decisions and Actions in 2024 (cont.) ## 2024 Peer Group Ametek, Inc. Aptiv PLC* Dove… |
| 2 | `qd7ede96b88aa:10-K:chunk-51` | 22.55215162501022 | 1.0 | # Compensation Discussion and Analysis ("CD&A") (cont.) ## Introduction Our compensation program closely aligns NEO com… |
| 3 | `qd7ede96b88aa:10-K:chunk-8` | 20.533591293493693 | 1.0 | # 2025 Annual Meeting of Shareholders (cont.) ## Composition of our Board (cont.) 31 Years of Growth and Improving Marg… |
| 4 | `qd7ede96b88aa:10-K:chunk-49` | 19.357608400195836 |  | # Other Named Executive Officers (cont.) ## Joel B. Reiss Joel B. Reiss, 54, was appointed Co-COO in May 2023. Prior to… |
| 5 | `qd7ede96b88aa:10-K:chunk-77` | 17.392712941414025 |  | # Shareholder Outreach Efforts (cont.) ## 2024 Feedback and Actions We received valuable feedback in our conversations … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qd7ede96b88aa`)._

### ex-dev-chunk-only-qddfea8300793

- **example_id**: `dev:chunk-only:qddfea8300793`
- **state**: `completed`
- **query**: How does Chesapeake Energy view the pace of technological advancements in drilling techniques and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.21398626473452756 · skipped= · n_scored=345

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qddfea8300793:10-K:chunk-135` | 20.842366636145826 |  | Item 7A. Quantitative and Qualitative Disclosures About Market Risk The primary objective of the following information … |
| 2 | `qddfea8300793:10-K:chunk-36` | 20.15096575973831 | 1.0 | Our development and exploratory drilling efforts and our well operations may not be profitable or achieve our targeted … |
| 3 | `qddfea8300793:10-K:chunk-37` | 19.114590756487924 |  | Most of our natural gas, oil and NGL derivative contracts are with counterparties under bilateral hedging arrangements.… |
| 4 | `qddfea8300793:10-K:chunk-44` | 19.05588071072149 |  | affecting the results of operations of Southwestern. Accordingly, the market price and performance of Chesapeake common… |
| 5 | `qddfea8300793:10-K:chunk-47` | 19.052827825048162 |  | The market price for Chesapeake common stock following the closing may be affected by factors different from those that… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qddfea8300793`)._

### ex-dev-chunk-only-qed0361d5a9ae

- **example_id**: `dev:chunk-only:qed0361d5a9ae`
- **state**: `completed`
- **query**: How does Apple currently project its growth rate based on the latest management commentary?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=83

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qed0361d5a9ae:Earnings:chunk-71` | 10.152835117489298 |  | The Company’s effective tax rate for the third quarter and first nine months of 2023 was lower than the statutory feder… |
| 2 | `qed0361d5a9ae:Earnings:chunk-56` | 8.372520790974075 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations This section and other pa… |
| 3 | `qed0361d5a9ae:Earnings:chunk-72` | 7.914771664047464 |  | Liquidity and Capital Resources The Company believes its balances of cash, cash equivalents and unrestricted marketable… |
| 4 | `qed0361d5a9ae:Earnings:chunk-69` | 7.886727478360263 |  | Research and Development The growth in research and development (“R&D”) expense during the third quarter and first nine… |
| 5 | `qed0361d5a9ae:Earnings:chunk-73` | 7.787852909218859 |  | PART II — OTHER INFORMATION Item 1. Legal Proceedings Epic Games Epic Games, Inc. (“Epic”) filed a lawsuit in the U.S. … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qed0361d5a9ae`)._

### ex-dev-chunk-only-qeeb1c1a41ae3

- **example_id**: `dev:chunk-only:qeeb1c1a41ae3`
- **state**: `completed`
- **query**: What dependency risks exist for DuPont de Nemours, Inc. due to concentration of revenue in a limited number of end-use industries such as automotive or electronics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.05652670087893601 · skipped= · n_scored=112

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeeb1c1a41ae3:10-K:chunk-1` | 29.445654590654943 |  | # NOTICE OF THE ANNUAL MEETING OF STOCKHOLDERS (cont.) ## How to Vote Your vote is important. Whether or not you plan o… |
| 2 | `qeeb1c1a41ae3:10-K:chunk-109` | 25.884819917700526 |  | # Reconciliation of "Cash provided by operating activities - continuing operations" to "Segment Adjusted Free Cash Flow… |
| 3 | `qeeb1c1a41ae3:10-K:chunk-4` | 25.323196604735244 | 1.0 | # Proxy Statement Summary # About DuPont We are a global innovation leader with technology-based materials and solution… |
| 4 | `qeeb1c1a41ae3:10-K:chunk-7` | 24.38627053120766 |  | # Executive Compensation Governance Practices (cont.) ## Key Executive Compensation Practices ## What We Do ## What We … |
| 5 | `qeeb1c1a41ae3:10-K:chunk-111` | 24.22990032650116 |  | # Important Notice Regarding the Availability of Proxy Materials for the Annual Meeting of Stockholders to be held May … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qeeb1c1a41ae3`)._

### ex-dev-chunk-only-qf3b87e3d287f

- **example_id**: `dev:chunk-only:qf3b87e3d287f`
- **state**: `completed`
- **query**: How has Bio-Techne Corporation’s leverage (e.g., debt-to-equity) changed over time?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.13120507751234178 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf3b87e3d287f:10-K:chunk-4` | 8.102012195434483 |  | Costs related to restructuring and restructuring-related activities, including reducing overhead and consolidating faci… |
| 2 | `qf3b87e3d287f:10-K:chunk-2` | 7.381025162382864 |  | Management uses adjusted operating results to monitor and evaluate performance of the Company’s business segments, as h… |
| 3 | `qf3b87e3d287f:10-K:chunk-0` | 6.347410175226145 |  | Exhibit 99.1 BIO-TECHNE RELEASES THIRD QUARTER FISCAL 2024 RESULTS Minneapolis/May 1, 2024/ Bio-Techne Corporation (NAS… |
| 4 | `qf3b87e3d287f:10-K:chunk-1` | 4.784271545207572 |  | Bio-Techne will host an earnings conference call today, May 1, 2024 at 8:00 a.m. CDT. To listen, please dial 1-877-407-… |
| 5 | `qf3b87e3d287f:10-K:chunk-8` | 4.0322508177876095 | 2.0 | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td colspan="2">3/… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qf3b87e3d287f`)._

### ex-dev-chunk-only-qf59bea60dc8d

- **example_id**: `dev:chunk-only:qf59bea60dc8d`
- **state**: `completed`
- **query**: How does Aon manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=145

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf59bea60dc8d:10-K:chunk-56` | 9.478452406823473 |  | 10. Income Taxes The effective tax rate on Net income was 16.6% and 17.1% for the three and nine months ended September… |
| 2 | `qf59bea60dc8d:10-K:chunk-93` | 8.553734768049026 |  | Income before Income Taxes Due to the factors discussed above, Income before income taxes for the third quarter of 2023… |
| 3 | `qf59bea60dc8d:10-K:chunk-77` | 7.45437242608992 |  | During the three and nine months ended September 30, 2022, the Company recorded a loss of $28 million and $11 million, … |
| 4 | `qf59bea60dc8d:10-K:chunk-107` | 7.2369967506878305 |  | (1)Adjusted items are generally taxed at the estimated annual effective tax rate, except for the applicable tax impact … |
| 5 | `qf59bea60dc8d:10-K:chunk-88` | 7.10171496485016 |  | •Adjusted diluted earnings per share, a non-GAAP measure defined under the caption “Review of Consolidated Results — Ad… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:chunk-only:qf59bea60dc8d`)._

### ex-dev-q00e75b32eb34

- **example_id**: `dev:q00e75b32eb34`
- **state**: `completed`
- **query**: How has International Flavors & Fragrances Inc.’s ingredients segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=154

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q00e75b32eb34:chunk-149` | 19.61784178225825 |  | 10.1##Amendment No. 5 to Term Loan Credit Agreement, dated as of September 19, 2023, among International Flavors & Frag… |
| 2 | `q00e75b32eb34:chunk-6` | 18.69255225799444 |  | INTERNATIONAL FLAVORS & FRAGRANCES INC. CONSOLIDATED STATEMENTS OF CASH FLOWS (Unaudited) |
| 3 | `q00e75b32eb34:chunk-9` | 18.69255225799444 |  | INTERNATIONAL FLAVORS & FRAGRANCES INC. CONSOLIDATED STATEMENTS OF SHAREHOLDERS’ EQUITY (Unaudited) |
| 4 | `q00e75b32eb34:chunk-3` | 18.46620812647886 |  | INTERNATIONAL FLAVORS & FRAGRANCES INC. CONSOLIDATED STATEMENTS OF INCOME (LOSS) AND COMPREHENSIVE LOSS (Unaudited) |
| 5 | `q00e75b32eb34:chunk-0` | 18.245279920376344 |  | PART I. FINANCIAL INFORMATION ITEM 1. FINANCIAL STATEMENTS. INTERNATIONAL FLAVORS & FRAGRANCES INC. CONSOLIDATED BALANC… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q00e75b32eb34`)._

### ex-dev-q01b84969979c

- **example_id**: `dev:q01b84969979c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How many markets were mentioned as now offering ad tier pricing for Disney Plus
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.6968778680746041 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['8-K', '10-Q', 'Earnings', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q01b84969979c`)._

### ex-dev-q0346b2bc5a8b

- **example_id**: `dev:q0346b2bc5a8b`
- **state**: `completed`
- **query**: What investor views emerged on Packaging Corporation of America’s geographic expansion prospects within the packaging industry?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9873464281832952 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', 'DEF14A', '10-Q', '8-K']`
- **S2**: nDCG@5=0.23719771276929622 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0346b2bc5a8b:chunk-1` | 14.903827648721421 |  | Thank you for joining Packaging Corporation of America's Fourth Quarter and Full Year 2023 Earnings Results Conference … |
| 2 | `q0346b2bc5a8b:chunk-107` | 11.237054939616531 |  | One good example of that, and we don't talk about a lot, our transportation capability. Over the last decade, we've bui… |
| 3 | `q0346b2bc5a8b:chunk-3` | 8.62391224138671 |  | Thank you, Jamie. Good morning, everyone, and thank you all for participating in Packaging Corporation of America's Fou… |
| 4 | `q0346b2bc5a8b:chunk-131` | 7.925964180885311 |  | Tom, Mark, I'm going to try one more time. So I apologize in advance, but it's more trying to understand the thought pr… |
| 5 | `q0346b2bc5a8b:chunk-51` | 7.906127779498914 | 1.0 | Yes, Mike, obviously, you don't know what the future is going to hold, but we've got a lot of optionality in what we're… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q0346b2bc5a8b`)._

### ex-dev-q03a704904653

- **example_id**: `dev:q03a704904653`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did IBM’s leadership say about IBM’s dividend policy or share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.6058748243961013 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '8-K', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q03a704904653`)._

### ex-dev-q044bb2c8810c

- **example_id**: `dev:q044bb2c8810c`
- **state**: `completed`
- **query**: What investor views emerged on EQT Corporation’s geographic expansion prospects within the U.S. natural gas markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=108

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q044bb2c8810c:chunk-18` | 10.927670692223282 |  | EQT CORPORATION AND SUBSIDIARIES Notes to the Condensed Consolidated Financial Statements (Unaudited) 1. Financial Stat… |
| 2 | `q044bb2c8810c:chunk-20` | 10.435042500190347 |  | 2. Revenue from Contracts with Customers Under the Company's natural gas, natural gas liquids (NGLs) and oil sales cont… |
| 3 | `q044bb2c8810c:chunk-59` | 9.556266372930681 |  | Unaudited Pro Forma Information. The table below summarizes the Company's results as though the Tug Hill and XcL Midstr… |
| 4 | `q044bb2c8810c:chunk-30` | 9.535118357725349 |  | EQT CORPORATION AND SUBSIDIARIES Notes to the Condensed Consolidated Financial Statements (Unaudited) 4. Fair Value Mea… |
| 5 | `q044bb2c8810c:chunk-88` | 8.780892492269498 |  | EQT CORPORATION AND SUBSIDIARIES Management's Discussion and Analysis of Financial Condition and Results of Operations … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q044bb2c8810c`)._

### ex-dev-q05bfc5cb3e17

- **example_id**: `dev:q05bfc5cb3e17`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Northern Trust Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.27727342735504823 · skipped= · n_scored=315

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q05bfc5cb3e17:chunk-305` | 13.679795458163731 |  | Notes to Consolidated Financial Statements (unaudited) (continued) lives of the instruments as interest rates, foreign … |
| 2 | `q05bfc5cb3e17:chunk-104` | 13.580564198337074 |  | FORWARD-LOOKING STATEMENTS (continued) •Northern Trust’s success in maintaining existing business and continuing to gen… |
| 3 | `q05bfc5cb3e17:chunk-103` | 13.13617923598091 |  | FORWARD-LOOKING STATEMENTS This report may include statements which constitute “forward-looking statements” within the … |
| 4 | `q05bfc5cb3e17:chunk-204` | 12.252441249244315 | 2.0 | Allowance Related to Credit Exposure Evaluated on a Collective Basis. Expected credit losses are measured on a collecti… |
| 5 | `q05bfc5cb3e17:chunk-87` | 12.122726380606563 | 2.0 | CAPITAL RATIOS The capital ratios of Northern Trust Corporation and its principal subsidiary, The Northern Trust Compan… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q05bfc5cb3e17`)._

### ex-dev-q09b8cfa51b60

- **example_id**: `dev:q09b8cfa51b60`
- **state**: `completed`
- **query**: How does CBRE Group, Inc. view the pace of technological innovation in real estate services and its effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=141

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q09b8cfa51b60:chunk-78` | 18.170507997168304 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations Management’s Discussion a… |
| 2 | `q09b8cfa51b60:chunk-125` | 17.156616516741153 |  | •the ability of our investment management business to maintain and grow assets under management and achieve desired inv… |
| 3 | `q09b8cfa51b60:chunk-136` | 16.320779240279546 |  | ########Incorporated by Reference#### Exhibit No.##Exhibit Description##Form##SEC File No.##Exhibit##Filing Date##Filed… |
| 4 | `q09b8cfa51b60:chunk-93` | 16.141225867142676 |  | Segment Operations We organize our operations around, and publicly report our financial results on, three global busine… |
| 5 | `q09b8cfa51b60:chunk-116` | 15.811619888648789 |  | Liquidity and Capital Resources We believe that we can satisfy our working capital and funding requirements with intern… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q09b8cfa51b60`)._

### ex-dev-q0b8d55d58be2

- **example_id**: `dev:q0b8d55d58be2`
- **state**: `completed`
- **query**: What questions were asked about Chubb Limited’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9979470946084208 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=370

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0b8d55d58be2:chunk-33` | 8.595722253102535 |  | (in millions of U.S. dollars)####Amount##Weighted-average useful life Definite life###### Agency distribution relations… |
| 2 | `q0b8d55d58be2:chunk-194` | 7.447115950356953 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – continued (Unaudited) Chubb Limited and Subsidiaries repurchased, 14,925,0… |
| 3 | `q0b8d55d58be2:chunk-239` | 6.280663215720223 |  | (1)Commercial multiple peril represents retail package business (property and general liability). The increase in conso… |
| 4 | `q0b8d55d58be2:chunk-205` | 6.188027072773134 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – continued (Unaudited) Chubb Limited and Subsidiaries 16. Postretirement be… |
| 5 | `q0b8d55d58be2:chunk-209` | 6.092162461479976 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – continued (Unaudited) Chubb Limited and Subsidiaries The line items in whi… |

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
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.38685280723454163 · gold=['Earnings']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q0e5327ae1aff`)._

### ex-dev-q0faf9d780cdc

- **example_id**: `dev:q0faf9d780cdc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did aeronautics sustainment hours compare with prior year levels?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7967075809905066 · gold=['10-Q', '10-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

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
| 1 | `q11ef281af9cd:chunk-215` | 13.328456840693473 |  | Exhibit Number####Description of Exhibit 10##(nnn)##Amendment No. 15 to Third Amended and Restated Receivables Purchase… |
| 2 | `q11ef281af9cd:chunk-99` | 11.532359430925826 |  | Revenues by reportable segment and geographical market are presented in note 5 of the consolidated financial statements… |
| 3 | `q11ef281af9cd:chunk-209` | 11.003466809868911 |  | Exhibit Number####Description of Exhibit 10##(jj)##Employment Agreement, effective as of January 20, 2016 between Unite… |
| 4 | `q11ef281af9cd:chunk-163` | 10.25638566089919 |  | _________________ (1) Reflects payments for non-cancelable operating leases with initial or remaining terms of one year… |
| 5 | `q11ef281af9cd:chunk-100` | 10.18255342953509 |  | of 28 days. This daily rate assumes that the equipment will be on rent for the full 28 days, as we are unsure of when t… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q11ef281af9cd`)._

### ex-dev-q140516364bb4

- **example_id**: `dev:q140516364bb4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Principal Financial Group’s international expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
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
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7303575739184495 · gold=['8-K', 'Earnings', '10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q1ab49a3f086f`)._

### ex-dev-q1cfcd01ac3a1

- **example_id**: `dev:q1cfcd01ac3a1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does GE HealthCare Technologies manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8596355563650325 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q1cfcd01ac3a1`)._

### ex-dev-q1ded233d05aa

- **example_id**: `dev:q1ded233d05aa`
- **state**: `completed`
- **query**: What questions were asked about IDEXX Laboratories’ customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9216809842642141 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.14115639177619477 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1ded233d05aa:chunk-1` | 11.027186626951906 |  | Good morning, and welcome to the IDEXX Laboratories Fourth Quarter 2023 Earnings Conference Call. As a reminder, today'… |
| 2 | `q1ded233d05aa:chunk-45` | 9.535668122141345 | 1.0 | Yes. Our markets have been very competitive for a long time. I think new ownership hasn't really changed that dynamic. … |
| 3 | `q1ded233d05aa:chunk-5` | 8.235976505941592 |  | Thank you, Brian, and good morning. IDEXX delivered strong performance in the fourth quarter, capping a year where we a… |
| 4 | `q1ded233d05aa:chunk-57` | 8.163598562099429 |  | So we don't have further questions. So with that, thank you for your questions. We'll now conclude our Q&A portion of t… |
| 5 | `q1ded233d05aa:chunk-27` | 8.143926396630363 | 1.0 | Yes. Just some follow-up commentary on the inVue launch. Customers, I think, very excited to learn more about that, as … |

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
- **state**: `completed`
- **query**: How did wage inflation trends affect labor costs in park operations
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9484971533659527 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.624105567784388 · skipped= · n_scored=475

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1ff3eed25e64:chunk-129` | 14.069764003269087 | 2.0 | The increase in operating labor was due to inflation, higher volumes and increased costs for new guest offerings. Highe… |
| 2 | `q1ff3eed25e64:chunk-24` | 12.187111301661192 |  | TABLE OF CONTENTS implementation or success of our business plans, such as our plans to increase investment in our Expe… |
| 3 | `q1ff3eed25e64:chunk-31` | 11.047143473531086 | 2.0 | TABLE OF CONTENTS productions and the pipeline for programming and theatrical releases, which could result in reduced r… |
| 4 | `q1ff3eed25e64:chunk-196` | 10.916797795248211 |  | The increases in operating labor, cost of goods sold and distribution costs and other operating expenses were due to hi… |
| 5 | `q1ff3eed25e64:chunk-22` | 9.551631042587099 |  | TABLE OF CONTENTS Retail The Company sells Disney-, Marvel-, Pixar- and Lucasfilm-branded products through shopDisney b… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q1ff3eed25e64`)._

### ex-dev-q2173e7c263c1

- **example_id**: `dev:q2173e7c263c1`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Realty Income Corporation for recessionary or downturn risks in the commercial real estate sector?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.16812753627111746 · skipped= · n_scored=171

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2173e7c263c1:chunk-90` | 21.485098379329333 |  | Item 2: Management’s Discussion and Analysis of Financial Condition and Results of Operations FORWARD-LOOKING STATEMENT… |
| 2 | `q2173e7c263c1:chunk-12` | 16.703290749941136 |  | REALTY INCOME CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS September 30, 2023 (unaudited) 1.… |
| 3 | `q2173e7c263c1:chunk-98` | 15.504198194821587 |  | experience increased costs of financing, make it difficult to refinance debt at attractive rates or at all, and may adv… |
| 4 | `q2173e7c263c1:chunk-155` | 14.893584965637999 | 1.0 | IMPACT OF RECENT ACCOUNTING PRONOUNCEMENTS For information on the impact of new accounting standards on our business, s… |
| 5 | `q2173e7c263c1:chunk-15` | 14.505513918218789 |  | The portion of a consolidated entity not owned by us is recorded as a noncontrolling interest. Noncontrolling interests… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2173e7c263c1`)._

### ex-dev-q238a8429d152

- **example_id**: `dev:q238a8429d152`
- **state**: `completed`
- **query**: How does Dominion Energy view the pace of innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=209

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q238a8429d152:chunk-172` | 24.52463108998423 |  | # Questions and Answers About the 2024 Annual Meeting and Voting (cont.) ## How can I receive future proxy materials an… |
| 2 | `q238a8429d152:chunk-163` | 20.03817962058955 |  | # Your Board of Directors recommends that you vote AGAINST this item. (cont.) ## Proponent's request could create unnec… |
| 3 | `q238a8429d152:chunk-92` | 19.985986986766015 |  | # 2023 Companywide Operating & Stewardship Goals (cont.) ## The Compensation Peer Group The CTD Committee uses the Comp… |
| 4 | `q238a8429d152:chunk-168` | 18.79168005597453 |  | # Questions and Answers About the 2024 Annual Meeting and Voting (cont.) ## What are the matters on which I will be cas… |
| 5 | `q238a8429d152:chunk-1` | 18.25828950864106 |  | # Notice of 2024 Annual Meeting of Shareholders (cont.) ## VOTING By Order of the Board of Directors, Each share of Dom… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q238a8429d152`)._

### ex-dev-q2451f8377cf4

- **example_id**: `dev:q2451f8377cf4`
- **state**: `completed`
- **query**: What dependency risks exist for Pool Corporation due to concentration of revenue in specific geographic regions or major pool supply distributors?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.2575785703353275 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2451f8377cf4:chunk-1` | 14.140034053290846 |  | Good day, and welcome to the Pool Corporation Fourth Quarter 2023 Conference Call. [Operator Instructions] Please note … |
| 2 | `q2451f8377cf4:chunk-21` | 12.845967415445008 |  | Yes. Thanks for the question, Ryan. As we were trying to put together our guidance for the year, obviously, the beginni… |
| 3 | `q2451f8377cf4:chunk-5` | 12.261718683335166 | 2.0 | Thank you, Melanie, and good morning to everyone on the call. For the full year 2023, we generated over $5.5 billion in… |
| 4 | `q2451f8377cf4:chunk-31` | 11.210269102433896 |  | Yes. I think what we have on our hands is -- and our advantage is time, right? And that is that we're not in it for the… |
| 5 | `q2451f8377cf4:chunk-29` | 10.366873771959089 |  | Okay. That's very helpful color. And then I wanted to dig a little deeper into the semi discretionary products and the … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2451f8377cf4`)._

### ex-dev-q24d0f908cfe3

- **example_id**: `dev:q24d0f908cfe3`
- **state**: `completed`
- **query**: What guidance was offered on Fox Corporation’s advertising revenue growth targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=111

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q24d0f908cfe3:chunk-54` | 14.56433807970808 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Fiscal 2023 Business and Management Review (cont.) offerings to suppl… |
| 2 | `q24d0f908cfe3:chunk-7` | 14.557701073217787 |  | # Board Nominees (cont.) ## Fiscal 2023 Business Highlights (cont.) - In fiscal 2023, Tubi delivered record revenues, w… |
| 3 | `q24d0f908cfe3:chunk-53` | 14.264408575514791 |  | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Fiscal 2023 Business and Management Review (cont.) - FOX Entertainmen… |
| 4 | `q24d0f908cfe3:chunk-6` | 14.030096438535475 |  | # Board Nominees (cont.) ## Fiscal 2023 Business Highlights (cont.) all-time record as the most-watched program in U.S.… |
| 5 | `q24d0f908cfe3:chunk-65` | 11.238898241051722 |  | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Long-Term Equity-Based Incentive Awards The Compensation Committee be… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q24d0f908cfe3`)._

### ex-dev-q25119b32a2f9

- **example_id**: `dev:q25119b32a2f9`
- **state**: `completed`
- **query**: What performance metrics does Snap-on Incorporated use to establish annual cash incentives or bonuses?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9882048111454694 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=21

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q25119b32a2f9:chunk-3` | 9.378336930704233 | 1.0 | References in this release to “organic sales” refer to sales from continuing operations calculated in accordance with g… |
| 2 | `q25119b32a2f9:chunk-14` | 8.1408411467368 |  | <hr />Non-GAAP Supplemental Data The following non-GAAP supplemental data is presented for informational purposes to pr… |
| 3 | `q25119b32a2f9:chunk-4` | 7.909724088232685 |  | Factors that may cause the company’s actual results to differ materially from those contained in the forward-looking st… |
| 4 | `q25119b32a2f9:chunk-1` | 7.249387290058958 |  | “Achieved in a period of variability, we believe our performance confirms the resilience of our markets and illustrates… |
| 5 | `q25119b32a2f9:chunk-0` | 6.533125779671051 |  | Exhibit 99 Snap-on Announces Third Quarter 2023 Results Sales of $1,159.3 million up 5.2% from Q3 2022, organic sales u… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q25119b32a2f9`)._

### ex-dev-q27a01443f529

- **example_id**: `dev:q27a01443f529`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Fox Corporation’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7434607313710785 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-K', '10-Q', '8-K']`
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
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6594343379129768 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q29a452be41cd`)._

### ex-dev-q29d3cb8df822

- **example_id**: `dev:q29d3cb8df822`
- **state**: `completed`
- **query**: How are investors interpreting guidance on SLB’s customer engagement metrics within its oilfield services operations?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9323478402140176 · gold=['Earnings', 'DEF14A', '8-K', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=47

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q29d3cb8df822:chunk-19` | 15.722842033025318 | 1.0 | This project includes the provision of CO2 removal membranes from natural gas, commissioning, and field service, with f… |
| 2 | `q29d3cb8df822:chunk-36` | 11.837082453244065 |  | (1) Excludes amounts which are included in the segments results. (2) See section entitled Charges & Credits for deta… |
| 3 | `q29d3cb8df822:chunk-47` | 10.65674927130541 |  | <hr /><hr />About SLB SLB (NYSE: SLB) is a global technology company driving energy innovation for a balanced planet. W… |
| 4 | `q29d3cb8df822:chunk-18` | 9.916308552472048 |  |  In the Republic of the Congo, a successful five-well, eight-stage acid stimulation campaign was performed for Perenco… |
| 5 | `q29d3cb8df822:chunk-21` | 9.494911078768425 |  | SLB continues to participate in the global transition to low-carbon energy systems through innovative technology and st… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q29d3cb8df822`)._

### ex-dev-q2aae5e2ea500

- **example_id**: `dev:q2aae5e2ea500`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Mondelez International’s snack foods segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7659463877163701 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2aae5e2ea500`)._

### ex-dev-q2c832749ca0b

- **example_id**: `dev:q2c832749ca0b`
- **state**: `completed`
- **query**: What dependency risks exist for Newmont Corporation due to concentration of revenue in a limited number of geographic regions or gold buyers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.14606834984270645 · skipped= · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2c832749ca0b:chunk-199` | 21.01064399882944 |  | subject to risks of tidal surge and tsunamis. For instance, a large seismic event in April 2017 impacted Cadia resultin… |
| 2 | `q2c832749ca0b:chunk-200` | 20.260976786975768 |  | Newcrest is subject to risks associated with the transportation of gold doré, including fluctuating transportation cha… |
| 3 | `q2c832749ca0b:chunk-101` | 20.244619576412966 |  | NEWMONT CORPORATION NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS (unaudited, dollars in millions, except per sh… |
| 4 | `q2c832749ca0b:chunk-192` | 19.832027104808557 | 2.0 | operations at Lihir and Wafi-Golpu in PNG are subject to political and regulatory risks and other uncertainties” and “—… |
| 5 | `q2c832749ca0b:chunk-205` | 19.20829115971445 |  | Exhibit Number######Description## 2.1##-####First Letter Deed, by and among Newmont Corporation, Newmont Overseas Holdi… |

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
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2fe5769567d7:chunk-60` | 10.69088058875744 |  | 2 of the Sherman Act. Plaintiff filed an amended complaint on July 30, 2021 adding new plaintiffs and various state law… |
| 2 | `q2fe5769567d7:chunk-13` | 10.167891635425928 |  | ALIGN TECHNOLOGY, INC. CONDENSED CONSOLIDATED STATEMENTS OF STOCKHOLDERS’ EQUITY (in thousands) (unaudited) |
| 3 | `q2fe5769567d7:chunk-9` | 10.167891635425928 |  | ALIGN TECHNOLOGY, INC. CONDENSED CONSOLIDATED STATEMENTS OF STOCKHOLDERS’ EQUITY (in thousands) (unaudited) |
| 4 | `q2fe5769567d7:chunk-142` | 9.910227068661088 |  | Exhibit Number##Description##Filing##Date##Exhibit Number##Filed herewith 3.1##Amended Certificate of Incorporation of … |
| 5 | `q2fe5769567d7:chunk-6` | 9.269494737260715 |  | ALIGN TECHNOLOGY, INC. CONDENSED CONSOLIDATED BALANCE SHEETS (in thousands, except per share data) (unaudited) |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q2fe5769567d7`)._

### ex-dev-q318eb902f451

- **example_id**: `dev:q318eb902f451`
- **state**: `completed`
- **query**: What questions were asked about Franklin Resources, Inc.’s client retention and engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9196027125796398 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.23463936301137822 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q318eb902f451:chunk-3` | 10.61840732261458 |  | Good morning, and thank you for joining us today to discuss our quarterly and fiscal year results. Please note that the… |
| 2 | `q318eb902f451:chunk-17` | 10.000906855877808 |  | And Bill, I would add one thing you asked about institutional flows in general. We have really worked hard over the las… |
| 3 | `q318eb902f451:chunk-15` | 9.06113397519697 | 1.0 | Yes, yes. Okay. Thank you. Thanks, Jenny. Thanks, Bill. So maybe I think your question gets to a couple of things. Firs… |
| 4 | `q318eb902f451:chunk-13` | 8.57435065785393 |  | Great. Well, thanks, Bill. So, so far, the outflows even within Western, I think it's like 72% are focused on essential… |
| 5 | `q318eb902f451:chunk-5` | 8.401909134613701 |  | Thank you, Selene. Hello, everyone, and thank you for joining us today to discuss Franklin Templeton's fourth quarter a… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q318eb902f451`)._

### ex-dev-q31f6fd1f392c

- **example_id**: `dev:q31f6fd1f392c`
- **state**: `completed`
- **query**: What governance processes are in place for approving changes to Targa Resources Corp.’s compensation policies?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9979470946084208 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '8-K', '10-Q', 'Earnings']`
- **S2**: nDCG@5=0.3869772073910237 · skipped= · n_scored=99

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q31f6fd1f392c:chunk-28` | 17.923560772724645 |  | # MEETINGS AND COMMITTEES OF DIRECTORS (cont.) ## Nominating and Governance Committee The members of our Nominating and… |
| 2 | `q31f6fd1f392c:chunk-73` | 17.48516352255055 | 1.0 | # EXECUTIVE COMPENSATION (cont.) ## Narrative to Director Compensation Table For 2023, the annual cash retainer for all… |
| 3 | `q31f6fd1f392c:chunk-36` | 15.885343049256281 | 2.0 | # CORPORATE GOVERNANCE (cont.) ## What We Heard: After thorough engagement and discussing the views of many shareholder… |
| 4 | `q31f6fd1f392c:chunk-41` | 15.826391652395731 | 2.0 | # Track Record of Growth Driving an Increasing Return of Capital to Shareholders (cont.) ## Good Governance Foundation … |
| 5 | `q31f6fd1f392c:chunk-9` | 15.532110174390422 |  | # SUSTAINABILITY AT TARGA (cont.) ## Our Performance We continue to engage with our stakeholders regarding our ESG effo… |

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
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7449030210206331 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
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
| 1 | `q3ef7ce37ae77:chunk-35` | 10.79886037578925 |  | A very brief add to your specific question as it relates to what's driving gross margin. It's really the structural dri… |
| 2 | `q3ef7ce37ae77:chunk-3` | 9.547021552254401 |  | Good morning. Thank you for joining us. With me today to discuss our fourth quarter and year-end results as well as our… |
| 3 | `q3ef7ce37ae77:chunk-83` | 8.793243259039048 |  | So I'll start with Michael Kors. And what we're seeing in our business and what our platform has been delivering is del… |
| 4 | `q3ef7ce37ae77:chunk-47` | 7.212125693841591 |  | Well, we are building and continue to drive a healthy business. That's been our focus, not only in China, but around th… |
| 5 | `q3ef7ce37ae77:chunk-31` | 5.721751463916211 |  | Matt, I'll touch on the consumer, but then toss it to Todd, maybe for a few comments on Coach. We couldn't be more conf… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q3ef7ce37ae77`)._

### ex-dev-q3f9446fe3b94

- **example_id**: `dev:q3f9446fe3b94`
- **state**: `completed`
- **query**: How are scenario analyses conducted by American Tower Corporation for risks related to fluctuations in mobile data demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9484971533659527 · gold=['10-K', 'Earnings', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3391602052736161 · skipped= · n_scored=342

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3f9446fe3b94:chunk-37` | 17.239093250014886 | 1.0 | •In less advanced wireless markets where network deployments are in earlier stages, we expect these deployments to driv… |
| 2 | `q3f9446fe3b94:chunk-175` | 17.058963493598654 |  | AMERICAN TOWER CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Tabular amounts in millions, un… |
| 3 | `q3f9446fe3b94:chunk-5` | 16.839788107085386 |  | communications equipment in locations where towers are generally not a viable solution based on area characteristics. I… |
| 4 | `q3f9446fe3b94:chunk-45` | 16.792059309949803 |  | ◦$43.6 million generated from newly acquired or constructed sites; ◦$35.1 million resulting from contractual escalation… |
| 5 | `q3f9446fe3b94:chunk-1` | 16.729802843081853 |  | Products and Services Property Operations Our property operations accounted for 99%, 98% and 97% of our total revenues … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q3f9446fe3b94`)._

### ex-dev-q41a18ce876e2

- **example_id**: `dev:q41a18ce876e2`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Kellanova’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.788088263175707 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q41a18ce876e2`)._

### ex-dev-q430300b97e2f

- **example_id**: `dev:q430300b97e2f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Ingersoll Rand’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.8616884617566115 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q430300b97e2f`)._

### ex-dev-q44cfaf358c37

- **example_id**: `dev:q44cfaf358c37`
- **state**: `completed`
- **query**: How do global economic or geopolitical trends shape regional market prospects for Molson Coors Beverage Company's alcoholic beverage portfolio?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.1791917585385473 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q44cfaf358c37:chunk-1` | 19.379866599962536 |  | Good day, and welcome to the Molson Coors Beverage Company Fourth Quarter and Fiscal Year 2023 Earnings Conference Call… |
| 2 | `q44cfaf358c37:chunk-103` | 11.327738302591735 |  | Yes. Well, we operate in the beverage market, and it certainly hasn't -- it hasn't performed as one would expect for ca… |
| 3 | `q44cfaf358c37:chunk-99` | 11.314809082816442 |  | From a cannabis point of view, I think it's fair to say that the cannabis beverage market hasn't grown anywhere like wh… |
| 4 | `q44cfaf358c37:chunk-63` | 10.709766218385482 | 2.0 | Yes. From a -- from an overall portfolio outside of the U.S., Chris, Canada, we do continue to see softness in the beer… |
| 5 | `q44cfaf358c37:chunk-107` | 10.661434770735381 |  | In the U.S., I think third-party data has shown weakness in industry about draft volume. So understanding that you were… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q44cfaf358c37`)._

### ex-dev-q4acd5677c3da

- **example_id**: `dev:q4acd5677c3da`
- **state**: `completed`
- **query**: What questions were asked about Hasbro’s customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9359826917490579 · gold=['Earnings', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.08703245752405495 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4acd5677c3da:chunk-3` | 8.57759384785738 |  | Thank you, and good morning, everyone. Joining me today are Chris Cocks, Hasbro's Chief Executive Officer; and Gina Goe… |
| 2 | `q4acd5677c3da:chunk-21` | 7.768862526635802 |  | Yes, for sure. So last year, we were fortunate in that, both MAGIC and D&D were growers for us. The MAGIC tabletop busi… |
| 3 | `q4acd5677c3da:chunk-15` | 7.764884517845006 |  | Sure. I think perhaps Gina and I will answer this question. Eric, generally speaking, we're feeling pretty good about w… |
| 4 | `q4acd5677c3da:chunk-85` | 6.960129613922056 | 1.0 | Yes, in Q4, we were down around 12% or 13% on our internal point-of-sale measurements. When you factor out some of the … |
| 5 | `q4acd5677c3da:chunk-9` | 6.30547430954171 |  | Thanks, Gina. Turnarounds take time, and for our toy business, we are still in the early innings. While we're likely to… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4acd5677c3da`)._

### ex-dev-q4bf1699a63fe

- **example_id**: `dev:q4bf1699a63fe`
- **state**: `completed`
- **query**: What dependency risks exist for Boston Properties, Inc. due to concentration of revenue in a limited number of geographic markets or key tenants?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.21398626473452753 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4bf1699a63fe:chunk-137` | 17.643317589088067 |  | I guess following up on the last question a little bit, Owen, maybe I'd love to get your thoughts on cap rates, and wha… |
| 2 | `q4bf1699a63fe:chunk-75` | 14.740432505432391 | 2.0 | Maybe just a question. Google announced last night meaningful office optimization charges, 1.2 billion in the quarter. … |
| 3 | `q4bf1699a63fe:chunk-15` | 11.780731037816604 |  | So that's, unfortunately, the technical question that keeps everybody up at night here at BXP, which is what will the a… |
| 4 | `q4bf1699a63fe:chunk-25` | 11.142221374380856 |  | Yes. And just lastly, John, to the second question that you asked, never say never. There might be other opportunities … |
| 5 | `q4bf1699a63fe:chunk-23` | 10.764443266258786 |  | Yes. And John, I would just say the following, which is there are institutional investors who have just had a perspecti… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4bf1699a63fe`)._

### ex-dev-q4d8ac905167b

- **example_id**: `dev:q4d8ac905167b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Citigroup Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.8304198973631919 · skipped= · n_scored=894

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4d8ac905167b:chunk-200` | 14.1118090229545 | 2.0 | LIQUIDITY RISK Overview Adequate and diverse sources of funding and liquidity are essential to Citi’s businesses. Fundi… |
| 2 | `q4d8ac905167b:chunk-61` | 13.565372314265995 | 2.0 | firms’ capital planning practices, focusing on six areas of capital planning: governance, risk management, internal con… |
| 3 | `q4d8ac905167b:chunk-275` | 11.669769568163876 |  | (5) Investment securities include debt securities AFS, recorded at fair market value, and debt securities HTM, recorded… |
| 4 | `q4d8ac905167b:chunk-294` | 11.546331616965732 | 2.0 | U.S. real GDP contraction in 2024 of 1.9%, with a peak quarter-over-quarter difference to the base scenario of 1.2% in … |
| 5 | `q4d8ac905167b:chunk-293` | 11.254864859600211 | 2.0 | (1) The year-over-year growth rate is the percentage change in the real (inflation adjusted) GDP level. Under the base … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4d8ac905167b`)._

### ex-dev-q4e3318b7d0e9

- **example_id**: `dev:q4e3318b7d0e9`
- **state**: `completed`
- **query**: How are data privacy or cybersecurity concerns affecting industry practices relevant to water technology solutions at Xylem Inc.?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.8761099271696507 · skipped= · n_scored=329

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4e3318b7d0e9:chunk-31` | 21.065077314364206 | 2.0 | Our Chief Information Security Officer ("CISO"), who has extensive cybersecurity knowledge and skills gained from over … |
| 2 | `q4e3318b7d0e9:chunk-20` | 19.89160439811405 | 2.0 | Cybersecurity incidents and related data breaches or other disruptions to our enterprise information technology and ope… |
| 3 | `q4e3318b7d0e9:chunk-2` | 19.048938826569096 | 1.0 | improve safety and conserve resources to customers in the water sector. Delivering value in these areas creates signifi… |
| 4 | `q4e3318b7d0e9:chunk-30` | 18.724242840650394 | 2.0 | an adverse effect on our reputation, our business, results of operations and financial condition. Additionally, we may … |
| 5 | `q4e3318b7d0e9:chunk-32` | 16.886969827944533 | 1.0 | Board of Directors Our Board recognizes the importance of maintaining the trust and confidence of our customers, suppli… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4e3318b7d0e9`)._

### ex-dev-q4f1cc6ea4ba6

- **example_id**: `dev:q4f1cc6ea4ba6`
- **state**: `completed`
- **query**: What sentiment trends are visible around Agilent Technologies’ free cash flow outlook and capital spending plans?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.23919165939156042 · skipped= · n_scored=170

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4f1cc6ea4ba6:chunk-169` | 10.55173099001103 |  | Thank you. Again, ladies and gentlemen, that will conclude the Agilent Technologies Q4 2023 Earnings Call. Again, thank… |
| 2 | `q4f1cc6ea4ba6:chunk-1` | 9.210457652945575 |  | Ladies and gentlemen, welcome to the Agilent Technologies Q4 2023 Earnings Conference Call. My name is Bo and I will be… |
| 3 | `q4f1cc6ea4ba6:chunk-7` | 9.043379347705663 | 2.0 | Thanks, Mike, and good afternoon, everyone. In my remarks today, I'll provide some additional details on revenue in the… |
| 4 | `q4f1cc6ea4ba6:chunk-147` | 7.964619175555533 | 1.0 | So how about Bob lead here a few comments. And then I've been dying to pull Phil in on here as well. And maybe talk abo… |
| 5 | `q4f1cc6ea4ba6:chunk-3` | 7.647772682381859 |  | Thank you, Bo, and welcome, everyone, to Agilent's conference call for the fourth quarter of fiscal year 2023. With me … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q4f1cc6ea4ba6`)._

### ex-dev-q536ce4006bf6

- **example_id**: `dev:q536ce4006bf6`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did AutoZone’s leadership say about AutoZone’s share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.5465881385757737 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['DEF14A', '8-K', 'Earnings', '10-K', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q536ce4006bf6`)._

### ex-dev-q53994e82efbb

- **example_id**: `dev:q53994e82efbb`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Builders FirstSource for recessionary or downturn risks in the residential construction market?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.2640681225725909 · skipped= · n_scored=64

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q53994e82efbb:chunk-39` | 14.549556240922168 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations The following discussion … |
| 2 | `q53994e82efbb:chunk-12` | 13.24070202189334 |  | BUILDERS FIRSTSOURCE, INC. AND SUBSIDIARIES NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS (Unaudited) 1. Basis o… |
| 3 | `q53994e82efbb:chunk-54` | 13.073394050232618 |  | PART II — OTHER INFORMATION Item 1. Legal Proceedings The Company has a number of known and threatened construction def… |
| 4 | `q53994e82efbb:chunk-40` | 12.486954306568004 | 1.0 | weighted average price of $97.43 per share, for a total cost of approximately $1.6 billion, inclusive of fees and taxes… |
| 5 | `q53994e82efbb:chunk-38` | 12.25540857395482 |  | We base our estimate of deferred tax assets and liabilities on current tax laws and rates. In certain cases, we also ba… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q53994e82efbb`)._

### ex-dev-q56c2aa1b3aa2

- **example_id**: `dev:q56c2aa1b3aa2`
- **state**: `completed`
- **query**: How are scenario analyses conducted by FedEx Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=165

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q56c2aa1b3aa2:chunk-150` | 14.83216280138982 |  | # How do I vote? (cont.) ## Who can attend the meeting? Stockholders of record and "street name" holders at the close o… |
| 2 | `q56c2aa1b3aa2:chunk-148` | 14.755474380765362 |  | # What is the difference between holding shares as a stockholder of record and as a beneficial owner? Am \| entitled to … |
| 3 | `q56c2aa1b3aa2:chunk-85` | 14.287504754646758 |  | # Executive Compensation - Compensation Discussion and Analysis (cont.) ## Limitation on Severance Benefits In June 202… |
| 4 | `q56c2aa1b3aa2:chunk-3` | 14.197136395470674 |  | # NOTICE OF ANNUAL MEETING OF STOCKHOLDERS ## Items of Business <table><tr><th colspan="2">Voting Proposal</th><th>Boar… |
| 5 | `q56c2aa1b3aa2:chunk-9` | 14.076126684405375 |  | # Advisory Vote to Approve Named Executive Officer Compensation (cont.) ## Proposal 3 ## Advisory Vote on the Frequency… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q56c2aa1b3aa2`)._

### ex-dev-q57e9d5635f56

- **example_id**: `dev:q57e9d5635f56`
- **state**: `completed`
- **query**: What quarter did guidance point to for streaming breakeven achievement
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.5706417189553201 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q57e9d5635f56:chunk-19` | 14.031396486547182 |  | So first on DTC. I mean, pricing is about to step up. You announced the cost-cutting program, some of which might be a … |
| 2 | `q57e9d5635f56:chunk-15` | 10.35437809935544 |  | Thanks, Michael. Regarding Charter, first of all, as we said when we did the deal, we think it's a great deal for us. I… |
| 3 | `q57e9d5635f56:chunk-7` | 9.843049550123363 | 2.0 | Thank you, Bob. I appreciate your kind words at the outset of the call. It's been an honor serving as Interim CFO these… |
| 4 | `q57e9d5635f56:chunk-21` | 7.657039646813911 | 2.0 | I'll take the second part first. Our plan when we bring ESPN direct to consumer, which is inevitable, which is going to… |
| 5 | `q57e9d5635f56:chunk-5` | 6.819486958150832 |  | Thanks, Alexia, and good afternoon, everyone. Before we begin, this week, we announced that Hugh Johnston will be joini… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q57e9d5635f56`)._

### ex-dev-q587ea3fc913d

- **example_id**: `dev:q587ea3fc913d`
- **state**: `completed`
- **query**: What guidance did Textron’s leadership give on cost structure optimization efforts?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9935051443580323 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=174

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q587ea3fc913d:chunk-113` | 7.030355196137954 | 2.0 | Well, Kristine, as we kind of put out there, there's a sizable piece that's going into Bell, and that's really aligning… |
| 2 | `q587ea3fc913d:chunk-123` | 6.551759246799749 | 2.0 | Look, George, as you know, it takes many months to build an aircraft. So the improvements in both the labor side and th… |
| 3 | `q587ea3fc913d:chunk-41` | 5.64336023204975 |  | Okay. And Frank, free cash flow. The guidance were flat. I know you had a pretty big inventory build in '23, but you al… |
| 4 | `q587ea3fc913d:chunk-51` | 5.620790200890285 |  | Okay. Great. And then just quickly on eAviation. We've got widening profitability losses they're projected for '24 on h… |
| 5 | `q587ea3fc913d:chunk-29` | 5.569646906110754 |  | Got it. That's helpful. And then just Frank quickly, the interest expense increase, just maybe what's going on there sp… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q587ea3fc913d`)._

### ex-dev-q5ce8ea5bf1b9

- **example_id**: `dev:q5ce8ea5bf1b9`
- **state**: `completed`
- **query**: What dependency risks exist for Global Payments Inc. due to concentration of revenue in a limited number of payment processing partners or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.11305340175787203 · skipped= · n_scored=119

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5ce8ea5bf1b9:chunk-25` | 23.18511695906659 | 1.0 | NOTE 2—ACQUISITION EVO Payments, Inc. On March 24, 2023, we acquired all of the outstanding common stock of EVO Payment… |
| 2 | `q5ce8ea5bf1b9:chunk-107` | 19.855953967477777 |  | Forward-Looking Statements Some of the statements we use in this report, and in some of the documents we incorporate by… |
| 3 | `q5ce8ea5bf1b9:chunk-114` | 19.380430852543544 |  | 2.1##Agreement and Plan of Merger, dated as of August 1, 2022, by and among EVO Payments, Inc., Global Payments Inc. an… |
| 4 | `q5ce8ea5bf1b9:chunk-92` | 18.514862761483073 |  | ITEM 2—MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following discussion a… |
| 5 | `q5ce8ea5bf1b9:chunk-93` | 18.034494323136784 |  | Highlights related to our financial condition at September 30, 2023 and results of operations for the three and nine mo… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q5ce8ea5bf1b9`)._

### ex-dev-q5d75c4f1ac86

- **example_id**: `dev:q5d75c4f1ac86`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What progress was reported in international park attendance recovery relative to pre pandemic levels
- **S1**: top1=`10-Q` in_gold=False · nDCG@5=0.568268330147156 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
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
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=134

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q63259a02ade0:chunk-91` | 11.75175307392503 |  | # Apple's Statement in Opposition to Proposal No. 4 (cont.) ## The Board recommends a vote AGAINST Proposal No. 4 becau… |
| 2 | `q63259a02ade0:chunk-4` | 11.546483875704222 |  | # Message from our Chief Executive Officer (cont.) ## To our shareholders, Around the world, teams across Apple continu… |
| 3 | `q63259a02ade0:chunk-39` | 11.527969006106217 |  | # Message from the People and Compensation Committee (cont.) ## Dear Fellow Shareholders, (cont.) As we look ahead, we'… |
| 4 | `q63259a02ade0:chunk-45` | 11.12018288308369 |  | # The Role of the Compensation Consultant (cont.) ## Actions Taken in Response (cont.) - The 2023 time-based RSUs grant… |
| 5 | `q63259a02ade0:chunk-93` | 10.984778287097303 |  | # Proposal No. 5 Shareholder Proposal (cont.) ## Supporting Statement: (cont.) As shareholders of Apple Inc., we believ… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q63259a02ade0`)._

### ex-dev-q636b07dd9c11

- **example_id**: `dev:q636b07dd9c11`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What impact could proposed legislative changes in the U.S. Credit Card Competition Act have on Mastercard?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7144565742807608 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '8-K', 'Earnings', '10-K', '10-Q']`
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
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What clarifications did analysts seek regarding Waters Corporation’s investment in chromatography and mass spectrometry innovation projects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7659463877163701 · gold=['Earnings', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q64898e5ba36c`)._

### ex-dev-q69d1505292c8

- **example_id**: `dev:q69d1505292c8`
- **state**: `completed`
- **query**: How might global inflationary trends affect Walgreens Boots Alliance’s input costs and pricing strategies?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.12750024571574825 · skipped= · n_scored=202

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q69d1505292c8:chunk-190` | 10.690668371284527 |  | WALGREENS BOOTS ALLIANCE, INC. AND SUBSIDIARIES ITEM 4. CONTROLS AND PROCEDURES Item 4. Controls and procedures Evaluat… |
| 2 | `q69d1505292c8:chunk-180` | 10.321233060646028 | 1.0 | WALGREENS BOOTS ALLIANCE, INC. AND SUBSIDIARIES MANAGEMENT'S DISCUSSION AND ANALYSIS 17 The Company reconciles Adjusted… |
| 3 | `q69d1505292c8:chunk-200` | 10.258266381949127 |  | ##Walgreens Boots Alliance, Inc. ##(Registrant) Dated: June 27, 2024##/s/ Manmohan Mahajan ##Manmohan Mahajan ##Executi… |
| 4 | `q69d1505292c8:chunk-121` | 9.771915929573884 |  | WALGREENS BOOTS ALLIANCE, INC. AND SUBSIDIARIES MANAGEMENT'S DISCUSSION AND ANALYSIS U.S. Healthcare The Company’s U.S.… |
| 5 | `q69d1505292c8:chunk-29` | 9.62987481389186 |  | WALGREENS BOOTS ALLIANCE, INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED CONDENSED FINANCIAL STATEMENTS (UNAUDITED) On Oct… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q69d1505292c8`)._

### ex-dev-q6c95b5e5930d

- **example_id**: `dev:q6c95b5e5930d`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Medtronic’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.788088263175707 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q6c95b5e5930d`)._

### ex-dev-q6cdb93e02e5f

- **example_id**: `dev:q6cdb93e02e5f`
- **state**: `completed`
- **query**: What clawback or recoupment policies apply to SBA Communications Corporation’s incentive compensation in case of restatements or misconduct?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9882048111454694 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.9218235822624828 · skipped= · n_scored=121

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q6cdb93e02e5f:chunk-33` | 36.05385126882577 | 2.0 | # Compensation Risks (cont.) ## Executive Compensation "No Fault" Recoupment or "Clawback" Policies Our Board has maint… |
| 2 | `q6cdb93e02e5f:chunk-56` | 23.087204304820443 | 1.0 | # Executive Summary (cont.) ## Our Strong Corporate Governance Policies Further Align our Executives' Interests with Th… |
| 3 | `q6cdb93e02e5f:chunk-87` | 20.504908637937366 | 1.0 | # Outstanding Equity Awards at Fiscal Year-End (cont.) ## Employment Agreements (cont.) - involving moral turpitude or … |
| 4 | `q6cdb93e02e5f:chunk-1` | 19.959045958940013 | 1.0 | # TABLE OF CONTENTS <table><tr><th>PROXY SUMMARY</th><th></th><th>1</th></tr><tr><td>PROPOSAL 1: ELECTION OF DIRECTORS.… |
| 5 | `q6cdb93e02e5f:chunk-2` | 18.250835478927726 |  | # PROXY SUMMARY (cont.) ## Ratification of Ernst & Young LLP as Our Independent Registered Public Accounting Firm for t… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q6cdb93e02e5f`)._

### ex-dev-q6d2cc453ca8c

- **example_id**: `dev:q6d2cc453ca8c`
- **state**: `completed`
- **query**: How did analysts probe the outlook for Roper Technologies’ free cash flow generation?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9134693626978977 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.08703245752405495 · skipped= · n_scored=130

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q6d2cc453ca8c:chunk-7` | 10.854287196305208 |  | Great. Thanks, Neil. I'll walk through the enterprise and segment results for Q4 and enterprise results for the full ye… |
| 2 | `q6d2cc453ca8c:chunk-9` | 10.696084586390974 |  | Thanks, Jason. As we turn to Page 12, let's look back on the year for Application Software segment. Total revenues grew… |
| 3 | `q6d2cc453ca8c:chunk-1` | 9.207642636824032 |  | Good morning. The Roper Technologies Conference Call will now begin. Today's call is being recorded. [Operator Instruct… |
| 4 | `q6d2cc453ca8c:chunk-59` | 8.185488978949177 | 1.0 | Got it. And then just following up on the M&A side of things, leverage at 3x, obviously, strong cash flow generator. Bu… |
| 5 | `q6d2cc453ca8c:chunk-5` | 8.027665292982897 |  | Thank you, Zack, and thanks to everyone for joining our call. We're looking forward to sharing our quite good 2023 4th … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q6d2cc453ca8c`)._

### ex-dev-q70b3e2802bf7

- **example_id**: `dev:q70b3e2802bf7`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Tyson Foods’ average cost per pound of processed chicken trend compared to the prior period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q70b3e2802bf7`)._

### ex-dev-q70e4aac30ddb

- **example_id**: `dev:q70e4aac30ddb`
- **state**: `completed`
- **query**: How did leadership respond to analyst questions about AI and personalization initiatives?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9903929125301808 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', 'DEF14A', '10-K']`
- **S2**: nDCG@5=0.11861329943102608 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q70e4aac30ddb:chunk-69` | 7.009536275615217 |  | I want to thank you all for joining us this morning. I want to appreciate all your questions, and I look forward to see… |
| 2 | `q70e4aac30ddb:chunk-9` | 6.4157747066468644 |  | Thank you, Rachel. At this time, we'll proceed with our normal Q&A session, which will last until the top of the hour. … |
| 3 | `q70e4aac30ddb:chunk-39` | 6.035821221935498 |  | If I can just add one thing to it. I think what has happened over the last several years is how much this business has … |
| 4 | `q70e4aac30ddb:chunk-53` | 5.944803726376355 | 1.0 | John, if I could take that on. Thank you for your question. We have more opportunities than what we have realized, but … |
| 5 | `q70e4aac30ddb:chunk-5` | 5.293773324405983 |  | Thank you, Tiffany. Good morning, everyone. Welcome to Starbucks' Fourth Quarter and Fiscal Year 2023 Earnings Conferen… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q70e4aac30ddb`)._

### ex-dev-q719082ac2068

- **example_id**: `dev:q719082ac2068`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did management characterize the evolution and strategic importance of AI factories?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8307820888596468 · gold=['Earnings', '10-K', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', 'DEF14A', '10-Q', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q719082ac2068`)._

### ex-dev-q76caada13eca

- **example_id**: `dev:q76caada13eca`
- **state**: `completed`
- **query**: What causes differences between Weyerhaeuser Company’s cash flow and net income (e.g., timberland harvest cycles or non-cash depreciation)?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9199642183398656 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5548459574357494 · skipped= · n_scored=86

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q76caada13eca:chunk-67` | 15.349890511240126 | 1.0 | Perfect. And then just one quick question on Timberland, especially on pulpwood. I want to get your thoughts around the… |
| 2 | `q76caada13eca:chunk-53` | 13.537428026899505 |  | Great. And maybe next, has there been any change at all in your confidence level or appetite around the target of acqui… |
| 3 | `q76caada13eca:chunk-5` | 11.268681743374591 |  | Thanks, Andy. Good morning, everyone, and thank you for joining us. Yesterday, Weyerhaeuser reported full year GAAP ear… |
| 4 | `q76caada13eca:chunk-7` | 9.488661715947426 | 2.0 | Thank you, Devin, and good morning, everyone. I'll be covering key financial items and fourth quarter financial perform… |
| 5 | `q76caada13eca:chunk-3` | 8.479779144545656 |  | Thank you, Rob. Good morning, everyone. Thank you for joining us to discuss Weyerhaeuser's fourth quarter 2023 earnings… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q76caada13eca`)._

### ex-dev-q78d98dc75a82

- **example_id**: `dev:q78d98dc75a82`
- **state**: `completed`
- **query**: How has Humana’s Medicare Advantage segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '8-K', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.18803819199888902 · skipped= · n_scored=283

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q78d98dc75a82:chunk-59` | 12.702654232067584 |  | Regulatory Environment We are and will continue to be regularly subject to new laws and regulations, changes to existin… |
| 2 | `q78d98dc75a82:chunk-55` | 12.518272881463556 | 1.0 | this segment are designed to enhance the overall healthcare experience. These services may lead to lower utilization as… |
| 3 | `q78d98dc75a82:chunk-225` | 11.510791084000665 | 1.0 | Humana Inc. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS—(Continued) On September 1, 2023, Humana Inc. and Humana Benefit… |
| 4 | `q78d98dc75a82:chunk-34` | 11.006760820849113 |  | “Families First Act”), the Coronavirus Aid, Relief, and Economic Security Act (the “CARES Act”), and the Inflation Redu… |
| 5 | `q78d98dc75a82:chunk-53` | 10.525198371241153 | 1.0 | ITEM 7. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS For discussion of 2021 it… |

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
| 1 | `q79acb772ca6b:chunk-281` | 15.511404766503407 |  | 10.27†##Offer Letter, dated November 25, 2013, between Gardner Denver, Inc. and Andy Schiesl (incorporated by reference… |
| 2 | `q79acb772ca6b:chunk-283` | 14.98046408689487 |  | 10.49†##Form of Performance Stock Unit Grant Notice and Agreement under the Ingersoll Rand Inc. Amended and Restated 20… |
| 3 | `q79acb772ca6b:chunk-276` | 14.659575329762326 |  | Exhibits Exhibit Number Exhibit Description 2.1 Agreement and Plan of Merger, dated as of April 30, 2019, by and among … |
| 4 | `q79acb772ca6b:chunk-0` | 14.522380163209313 |  | PART I SPECIAL NOTE REGARDING FORWARD-LOOKING STATEMENTS In addition to historical information, this Annual Report on F… |
| 5 | `q79acb772ca6b:chunk-277` | 14.301079713274799 |  | 2.2##Separation and Distribution Agreement, dated as of April 30, 2019, by and between Ingersoll-Rand plc and Ingersoll… |

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
- **state**: `completed`
- **query**: How are scenario analyses conducted by Fiserv for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3391602052736161 · skipped= · n_scored=256

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7b42f1295dc1:chunk-15` | 10.226202694466972 | 1.0 | Global Market Risks Our business may be adversely affected by geopolitical and other risks associated with operations o… |
| 2 | `q7b42f1295dc1:chunk-236` | 9.350401715078357 |  | performing audit procedures to evaluate the reasonableness of management’s estimates and assumptions related to revenue… |
| 3 | `q7b42f1295dc1:chunk-239` | 8.723403465315076 |  | Item 9B. Other Information (b) Except as set forth below, during the three months ended December 31, 2023, none of the … |
| 4 | `q7b42f1295dc1:chunk-234` | 8.717210843844713 |  | REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM To the Shareholders and the Board of Directors of Fiserv, Inc. … |
| 5 | `q7b42f1295dc1:chunk-242` | 8.147451309704923 |  | (1)Columns (a) and (c) of the table above do not include 5,241,872 unvested restricted stock units outstanding under th… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7b42f1295dc1`)._

### ex-dev-q7c284aabbba4

- **example_id**: `dev:q7c284aabbba4`
- **state**: `completed`
- **query**: What dependency risks exist for Moderna, Inc. due to concentration of revenue in a limited number of vaccine products or geographic markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9882048111454694 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.7241842264347773 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7c284aabbba4:chunk-21` | 15.75208869012469 |  | I have 2 very quick questions. First one is regarding the RSV vaccine. What portion of 35,000 to 36,000 participants th… |
| 2 | `q7c284aabbba4:chunk-11` | 15.33046298760575 | 2.0 | Thank you, Stephen and Jamey. For Moderna and the patients we serve, 2024 is all about execution: execution in commerci… |
| 3 | `q7c284aabbba4:chunk-7` | 14.664725203506448 | 2.0 | Thanks, Stéphane, and hello, everyone. Today, I will review our financial performance for both the fourth quarter and t… |
| 4 | `q7c284aabbba4:chunk-25` | 14.263385554949156 | 2.0 | Thanks, Stephen. And Gena, it's Stéphane. On the upside and downside on the sales for this year, I think on the upside,… |
| 5 | `q7c284aabbba4:chunk-5` | 13.610020401856683 | 2.0 | Thank you, Lavina. Good morning or good afternoon, everyone. Thank you for joining us today. I will start with a review… |

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
| 1 | `q7eb4e8a11956:chunk-29` | 13.096341473893599 |  | As you've seen from our results in Q4 and the guidance for Q1, we're obviously experiencing very strong levels of gross… |
| 2 | `q7eb4e8a11956:chunk-3` | 9.999462818344409 |  | Thank you. Good afternoon, and thank you for joining us. Speaking first today is Apple's CEO, Tim Cook; and he'll be fo… |
| 3 | `q7eb4e8a11956:chunk-85` | 9.687738100692998 |  | I have 2 of them, too. First one, Luca, thanks for the color on gross margin. And when I look at it over the last 4 qua… |
| 4 | `q7eb4e8a11956:chunk-109` | 9.058194870541548 |  | And I would add, Richard, on this front, some of the investments that we're making in R&D are also one of the drivers f… |
| 5 | `q7eb4e8a11956:chunk-27` | 8.160005443522891 |  | Yes. And then as a quick follow-up, I'm curious as we move towards more of an inflationary component pricing environmen… |

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
| 1 | `q7eb5b91e2366:chunk-37` | 13.349098365827755 |  | Yes. Thanks for the question, Robbie. We feel really good about the -- how we've been moving BD into higher growth spac… |
| 2 | `q7eb5b91e2366:chunk-7` | 12.999864427530985 | 1.0 | *Thanks, Tom, and good morning, everyone. As Tom noted, we delivered competitive organic revenue growth for the fourth … |
| 3 | `q7eb5b91e2366:chunk-65` | 12.019821375065142 |  | Maybe we can turn to capital allocation. Your $1 billion share repurchase announcement over the next 12 to 18 months ce… |
| 4 | `q7eb5b91e2366:chunk-13` | 11.043842090256438 |  | Okay. Vijay, I appreciate the comments there. So I'll start off with just some comments on some of our assumptions for … |
| 5 | `q7eb5b91e2366:chunk-53` | 11.041904533322887 |  | Tom, I just wanted to circle back. You mentioned -- and congrats on the quarter and the kind of really well thought and… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7eb5b91e2366`)._

### ex-dev-q7ebef55d671d

- **example_id**: `dev:q7ebef55d671d`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Chipotle’s supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6366684052697871 · gold=['DEF14A', '10-Q', '10-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7ebef55d671d`)._

### ex-dev-q7ed5279a28b4

- **example_id**: `dev:q7ed5279a28b4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did Teradyne’s management note about Teradyne’s operational scalability as test equipment demand volumes grow or contract?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7679992931079491 · gold=['Earnings', '10-Q', '10-K', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q7ed5279a28b4`)._

### ex-dev-q811679c2d742

- **example_id**: `dev:q811679c2d742`
- **state**: `completed`
- **query**: What challenges are noted regarding scaling infrastructure or capacity for renewable energy integration to meet growth?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9416116958060755 · gold=['10-K', '8-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.6646072001486268 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q811679c2d742:chunk-107` | 11.69211881013246 | 2.0 | New Technology and Government Grants Hydrogen Hub Grant In October 2023, the DOE selected the Heartland Hydrogen Hub, i… |
| 2 | `q811679c2d742:chunk-82` | 10.801790905233755 |  | (a)Amounts may not add due to rounding. Summary of Earnings Xcel Energy — Xcel Energy’s third quarter GAAP diluted earn… |
| 3 | `q811679c2d742:chunk-129` | 10.669247325878558 | 1.0 | The base plan does not include any potential renewable generation assets associated with the Colorado recommended Prefe… |
| 4 | `q811679c2d742:chunk-106` | 10.41586030957809 | 2.0 | Colorado Legislation — In May 2023, Colorado Senate Bill 23-291 passed and was signed into law. The bill includes a num… |
| 5 | `q811679c2d742:chunk-134` | 9.871632980802968 |  | Financing plans are subject to change, depending on legislative initiatives (e.g., federal tax law changes), capital ex… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q811679c2d742`)._

### ex-dev-q84038a74fd59

- **example_id**: `dev:q84038a74fd59`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How many organizations were reported to be using Azure OpenAI Service
- **S1**: top1=`10-K` in_gold=False · nDCG@5=0.6936542675401631 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['10-K', 'Earnings', '8-K', '10-Q', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

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
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3392737903096821 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88819064dbb7:chunk-29` | 11.348581152278697 |  | If I may add just one additional point. If you think about the Family Dollar segment, one of the things that we're real… |
| 2 | `q88819064dbb7:chunk-1` | 11.231138513954846 |  | Hello, and welcome to the Dollar Tree Q4 2023 Earnings Call. [Operator Instructions] At this time, I'd like to turn the… |
| 3 | `q88819064dbb7:chunk-73` | 11.070563077936667 |  | Two questions. Just curious what's driving the average ticket lower at Dollar Tree, even as you add the higher price po… |
| 4 | `q88819064dbb7:chunk-25` | 10.646501167733696 | 2.0 | So two questions. Maybe, could you elaborate on the traffic trends and market share by demographic that you're seeing a… |
| 5 | `q88819064dbb7:chunk-5` | 10.282219666778937 | 1.0 | Thanks, Bob. Good morning, everyone. This past year, our organization made meaningful progress in the ongoing transform… |

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
| 1 | `q88db5d96c8dd:chunk-170` | 16.70678139564491 |  | SUMMARY OF ABBREVIATED TERMS Bristol-Myers Squibb Company and its consolidated subsidiaries may be referred to as Brist… |
| 2 | `q88db5d96c8dd:chunk-0` | 16.67576889308185 |  | PART I—FINANCIAL INFORMATION Item 1. FINANCIAL STATEMENTS BRISTOL-MYERS SQUIBB COMPANY CONSOLIDATED STATEMENTS OF EARNI… |
| 3 | `q88db5d96c8dd:chunk-5` | 14.290336986646748 |  | BRISTOL-MYERS SQUIBB COMPANY CONSOLIDATED BALANCE SHEETS Dollars in millions (UNAUDITED) |
| 4 | `q88db5d96c8dd:chunk-8` | 14.156478369195561 |  | BRISTOL-MYERS SQUIBB COMPANY CONSOLIDATED STATEMENTS OF CASH FLOWS Dollars in millions (UNAUDITED) |
| 5 | `q88db5d96c8dd:chunk-174` | 12.463635643413511 |  | ######BRISTOL-MYERS SQUIBB COMPANY (REGISTRANT)## Date:##October 26, 2023##By:####/s/ Giovanni Caforio, M.D. ########Gi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q88db5d96c8dd`)._

### ex-dev-q89953a08e494

- **example_id**: `dev:q89953a08e494`
- **state**: `completed`
- **query**: How does Globe Life Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=125

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89953a08e494:chunk-124` | 11.61795869040086 |  | # GLOBE LIFE INC. ANNUAL MEETING OF SHAREHOLDERS Thursday, April 25, 2024 10:00 a.m. (CDT) Virtual Meeting Online via l… |
| 2 | `q89953a08e494:chunk-122` | 11.113100975333353 |  | # APPENDIX A NON-GAAP RECONCILIATION The chart below reflects non-GAAP financial measures utilized by Management which … |
| 3 | `q89953a08e494:chunk-52` | 10.986755149157604 |  | # Risk Reporting Structure (cont.) ## Mosaic@Globe Life Mission Statement We are committed to maintaining a diverse wor… |
| 4 | `q89953a08e494:chunk-64` | 9.768901269513687 |  | # Assessment of 2023 Advisory Vote on Executive Compensation (cont.) ## Base Salaries The Compensation Committee sets (… |
| 5 | `q89953a08e494:chunk-73` | 9.551547973759034 |  | # Stock Ownership/Retention Guidelines (cont.) ## Clawback Policy On November 8, 2023, our Board of Directors adopted t… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q89953a08e494`)._

### ex-dev-q89fb186f5e49

- **example_id**: `dev:q89fb186f5e49`
- **state**: `completed`
- **query**: What investor views emerged on Linde’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9882048111454694 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-K', 'DEF14A', '10-Q', '8-K']`
- **S2**: nDCG@5=0.3391602052736161 · skipped= · n_scored=287

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89fb186f5e49:chunk-5` | 11.627440956446055 | 1.0 | Table of Contents ITEM 1A. RISK FACTORS Due to the size and geographic reach of the company’s operations, a wide range … |
| 2 | `q89fb186f5e49:chunk-8` | 7.902481402838893 |  | Table of Contents •cultural challenges associated with integrating employees from the acquired company into the existin… |
| 3 | `q89fb186f5e49:chunk-36` | 7.620408667890185 |  | Table of Contents SEGMENT DISCUSSION Linde’s operations consist of two major product lines: industrial gases and engine… |
| 4 | `q89fb186f5e49:chunk-244` | 7.529510395639377 |  | Table of Contents NOTE 18. SEGMENT INFORMATION Linde’s operations consist of two major product lines: industrial gases … |
| 5 | `q89fb186f5e49:chunk-2` | 7.001881860153137 |  | Table of Contents Patents and Trademarks – Linde owns or licenses a large number of patents that relate to a wide varie… |

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
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9134693626978977 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.24630238874073 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8ba6a388d681:chunk-11` | 11.29886305002425 |  | Hock, so yesterday, one of your peers suggested that the market for AI accelerators could be as large as $400 billion. … |
| 2 | `q8ba6a388d681:chunk-95` | 6.969527413346453 | 1.0 | Hock, I guess I'll caveat my question saying that I'm a semiconductor guy rather than a software expert. But I wanted t… |
| 3 | `q8ba6a388d681:chunk-17` | 6.1258618904314295 |  | Just a quick clarification, then a question. The clarification is, is the fiscal year guidance going to be the new prot… |
| 4 | `q8ba6a388d681:chunk-3` | 6.047844683764547 |  | Thank you, operator, and good afternoon, everyone. Joining me on today's call are Hock Tan, President and CEO; Kirsten … |
| 5 | `q8ba6a388d681:chunk-1` | 5.264617495328622 |  | Welcome to Broadcom Inc.'s Fourth Quarter and Fiscal Year 2023 Financial Results Conference Call. At this time, for ope… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q8ba6a388d681`)._

### ex-dev-q8cc1033cf552

- **example_id**: `dev:q8cc1033cf552`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance did The Sherwin-Williams Company’s leadership provide on debt reduction or leverage targets for The Sherwin-Williams Company?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5=0.6757507974357403 · gold=['10-K', 'Earnings', '10-Q']
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
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
| 1 | `q8e053e02a010:chunk-77` | 28.834772420189008 |  | # Current CEO Pay-for-Performance Alignment (cont.) ## Peer Group Benchmarking Consistent with the Company's compensati… |
| 2 | `q8e053e02a010:chunk-1` | 27.92570636225678 |  | # Dear Shareowner, The image shows a professional headshot of a middle-aged man with gray hair and a full gray beard. H… |
| 3 | `q8e053e02a010:chunk-11` | 27.68745672753048 |  | # Proxy Summary / Our Commitment to Sustainability (cont.) ## Our Approach to Climate We recognize the impacts of clima… |
| 4 | `q8e053e02a010:chunk-38` | 24.76571913579461 |  | # Corporate Governance / How the Board Operates (cont.) ## Responsibilities - Assisting our Board in monitoring the int… |
| 5 | `q8e053e02a010:chunk-83` | 24.34720764057131 |  | # How and Why We Chose Our Performance Metrics (cont.) ## Adjusted EBITDA Adjusted EBITDA¹ is commonly used as a proxy … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q8e053e02a010`)._

### ex-dev-q8e26f08be2bc

- **example_id**: `dev:q8e26f08be2bc`
- **state**: `completed`
- **query**: What challenges arise for Vertex Pharmaceuticals from data privacy regulations and handling of patient data?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9404457547956446 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.9125299483251055 · skipped= · n_scored=285

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8e26f08be2bc:chunk-51` | 28.61787059242998 | 2.0 | governing cell and genetic therapy products have changed frequently and may continue to change in the future. For examp… |
| 2 | `q8e26f08be2bc:chunk-52` | 23.681098107423804 | 2.0 | research institution that has not complied with HIPAA’s requirements for disclosing such information. In addition, the … |
| 3 | `q8e26f08be2bc:chunk-62` | 18.938537962632612 | 2.0 | If our facilities were to experience a catastrophic loss, our operations would be seriously harmed. Most of our operati… |
| 4 | `q8e26f08be2bc:chunk-29` | 18.08733285196609 | 2.0 | Many of these laws and regulations contain requirements that are subject to interpretation. Outside the U.S., other cou… |
| 5 | `q8e26f08be2bc:chunk-45` | 16.960957910547293 | 1.0 | approved for sale by the FDA or comparable foreign regulatory authorities. To satisfy these standards, we must allocate… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=208

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q93fb2b2861c4:chunk-8` | 15.571952274110842 |  | environmentally responsible packaging, reducing greenhouse gas emission, reducing water usage, recycling solid waste an… |
| 2 | `q93fb2b2861c4:chunk-110` | 15.452107142633805 |  | CHURCH & DWIGHT CO., INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS - (Continued) (In millions, excep… |
| 3 | `q93fb2b2861c4:chunk-24` | 15.120734756958502 |  | Major developments in trade relations, including the imposition of new or increased tariffs or sanctions by the U.S. an… |
| 4 | `q93fb2b2861c4:chunk-42` | 14.565913707783167 |  | CHURCH & DWIGHT CO., INC AND SUBSIDIARIES (Dollars in millions, except share and per share data) ITEM 7. MANAGEMENT’S D… |
| 5 | `q93fb2b2861c4:chunk-101` | 14.214175389336418 |  | CHURCH & DWIGHT CO., INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS - (Continued) (In millions, excep… |

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
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.4935456744811716 · gold=['10-K', 'Earnings']
- **S1 ordered**: `['8-K', 'DEF14A', 'Earnings', '10-K', '10-Q']`
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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q98c606bb3ce7:chunk-0` | 28.355456932566085 |  | PART I ITEM 1. BUSINESS OVERVIEW Williams-Sonoma, Inc., (the "Company”, "we", or "us") incorporated in 1973, is an omni… |
| 2 | `q98c606bb3ce7:chunk-136` | 23.56163786765949 |  | ##STOCK PLANS## 10.3+####Williams-Sonoma, Inc. 2001 Long-Term Incentive Plan, as amended (incorporated by reference to … |
| 3 | `q98c606bb3ce7:chunk-73` | 22.25683474128193 |  | Table of Contents Williams-Sonoma, Inc. Notes to Consolidated Financial Statements Note A: Summary of Significant Accou… |
| 4 | `q98c606bb3ce7:chunk-139` | 20.586084529694684 |  | 10.16####Lease for an additional Company distribution facility located in Olive Branch, Mississippi between Williams-So… |
| 5 | `q98c606bb3ce7:chunk-114` | 19.914572921659595 |  | 1Intrinsic value for releases is based on the market value on the date of release. 2Includes 208,670 incremental shares… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q98c606bb3ce7`)._

### ex-dev-q99a077efaab0

- **example_id**: `dev:q99a077efaab0`
- **state**: `completed`
- **query**: What dependency risks exist for Align Technology due to concentration of revenue in a limited number of orthodontic practices or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.38685280723454163 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99a077efaab0:chunk-7` | 14.276844582691629 |  | Thanks, John. In closing, while I'm pleased with our better-than-expected fourth quarter results and start to the year,… |
| 2 | `q99a077efaab0:chunk-3` | 13.348988928909321 | 1.0 | Thanks, Shirley. Good afternoon, and thanks for joining us. On our call today, I'll provide an overview of our fourth q… |
| 3 | `q99a077efaab0:chunk-45` | 13.16078871132561 |  | So Joe, maybe this one's for you. Video 1Q '24 IPE some markets today, but more in the common IPE should have longer te… |
| 4 | `q99a077efaab0:chunk-5` | 12.355899558322127 |  | Thanks, Joe. Now for our Q4 financial results. Total revenues for the fourth quarter were $956.7 million, down 0.4% fro… |
| 5 | `q99a077efaab0:chunk-1` | 11.109521452590135 |  | Good afternoon, and thank you for joining us. I'm Shirley Stacy, Vice President of Corporate Communications and Investo… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q99a077efaab0`)._

### ex-dev-q99ec5f1aeea5

- **example_id**: `dev:q99ec5f1aeea5`
- **state**: `completed`
- **query**: What questions were asked about Federal Realty Investment Trust’s tenant retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9199642183398656 · gold=['Earnings', '8-K', '10-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=64

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99ec5f1aeea5:chunk-8` | 11.847836535492412 |  | (1)Does not assume the impact of potential acquisitions or dispositions which have not closed as of January 31, 2024. (… |
| 2 | `q99ec5f1aeea5:chunk-38` | 6.29104694813916 |  | (2)The interest rate is effectively fixed at 5.03% through the initial maturity date, as a result of three interest rat… |
| 3 | `q99ec5f1aeea5:chunk-6` | 4.726999425477229 |  | Occupancy The portfolio was 92.2% occupied and 94.2% leased as of December 31, 2023. Additionally, our comparable resid… |
| 4 | `q99ec5f1aeea5:chunk-30` | 4.601839518116062 |  | Notes: (1)There is no guarantee that the Trust will ultimately complete any or all of these opportunities, that the ROI… |
| 5 | `q99ec5f1aeea5:chunk-16` | 3.7237359988504384 |  | Notes: (1)See Glossary of Terms. (2)For the three months and year ended December 31, 2023 and 2022, dividends on our Se… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q99ec5f1aeea5`)._

### ex-dev-q9a5cfe35fecd

- **example_id**: `dev:q9a5cfe35fecd`
- **state**: `completed`
- **query**: What dependency risks exist for CMS Energy Corporation due to concentration of revenue in a limited number of geographic regions or key utility customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.7557415207297861 · skipped= · n_scored=194

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9a5cfe35fecd:chunk-19` | 22.32919725953079 | 2.0 | •the investment performance of the assets of CMS Energy’s and Consumers’ pension and benefit plans, the discount rates,… |
| 2 | `q9a5cfe35fecd:chunk-116` | 20.60314545209694 | 2.0 | CMS Energy Corporation Consumers Energy Company Notes to the Unaudited Consolidated Financial Statements These interim … |
| 3 | `q9a5cfe35fecd:chunk-167` | 20.373192710621126 | 1.0 | product comprising the commodity, electricity or natural gas, and the service of delivering such commodity. In some ins… |
| 4 | `q9a5cfe35fecd:chunk-166` | 20.05356456926662 | 2.0 | 1Amounts represent NorthStar Clean Energy’s operating revenue from independent power production and its sales of energy… |
| 5 | `q9a5cfe35fecd:chunk-14` | 18.607763271017312 |  | PSCR Power supply cost recovery RCRA Federal Resource Conservation and Recovery Act of 1976 REC Renewable energy credit… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9a5cfe35fecd`)._

### ex-dev-q9c255237096a

- **example_id**: `dev:q9c255237096a`
- **state**: `completed`
- **query**: What perquisites or fringe benefits are included in The AES Corporation’s executive compensation disclosures?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=1.0 · gold=['DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.7227265726449517 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9c255237096a:chunk-40` | 24.322179015025828 | 2.0 | # EXECUTIVE COMPENSATION COMPENSATION DISCUSSION AND ANALYSIS ("CD&A") (cont.) ## What AES Does ## What AES Doesn't Do … |
| 2 | `q9c255237096a:chunk-54` | 18.948429840479797 | 2.0 | # Three-Year CEO LTC Realizable Pay <table> <tr> <th>Year</th> <th>Type</th> <th>RSU</th> <th>PSU</th> <th>PCU</th> <th… |
| 3 | `q9c255237096a:chunk-9` | 17.580145491835587 | 2.0 | # Compensation and Benefits Best Practices Target Total Compensation at Approximately the 50th Percentile Independent C… |
| 4 | `q9c255237096a:chunk-56` | 15.547210325533602 |  | # Three-Year CEO LTC Realizable Pay (cont.) ## Severance and Change-in-Control Arrangements The Company maintains certa… |
| 5 | `q9c255237096a:chunk-8` | 15.201239267354293 |  | # PROXY STATEMENT SUMMARY (cont.) ## Corporate Governance Our Corporate Governance Policies Reflect Best Practices Annu… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9c255237096a`)._

### ex-dev-q9dd3907388e3

- **example_id**: `dev:q9dd3907388e3`
- **state**: `completed`
- **query**: How does Duke Energy view the pace of innovation cycles in renewable energy technologies and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9dd3907388e3:chunk-6` | 28.74128373196052 | 1.0 | ◦The ability to implement our business strategy, including our carbon emission reduction goals; ◦State, federal and for… |
| 2 | `q9dd3907388e3:chunk-7` | 22.663150609248433 |  | ◦The influence of weather and other natural phenomena on operations, including the economic, operational and other effe… |
| 3 | `q9dd3907388e3:chunk-0` | 18.154332411051588 |  | News Release Media Contact: Gillian Moore 24-Hour: 800.559.3853 Analyst Contact: Abby Motsinger Office: 704.382.7624 Au… |
| 4 | `q9dd3907388e3:chunk-8` | 18.08290832787318 |  | ◦Changes in rules for regional transmission organizations, including changes in rate designs and new and evolving capac… |
| 5 | `q9dd3907388e3:chunk-5` | 13.000855702875754 |  | The most directly comparable GAAP measure for adjusted segment income or adjusted other net loss is segment income and … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9dd3907388e3`)._

### ex-dev-q9f32df79b0d7

- **example_id**: `dev:q9f32df79b0d7`
- **state**: `completed`
- **query**: How does Capital One view the pace of digital banking innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.43067655807339306 · skipped= · n_scored=4

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9f32df79b0d7:chunk-2` | 2.95297117929592 |  | •Auto average loans decreased $493 million, or 1 percent, to $75.7 billion. ◦Commercial Banking average loans decreased… |
| 2 | `q9f32df79b0d7:chunk-3` | 1.4705198746339565 |  | Capital One Financial Corporation (www.capitalone.com) is a financial holding company which, along with its subsidiarie… |
| 3 | `q9f32df79b0d7:chunk-1` | 1.1969005681083469 |  | •Total net revenue increased 4 percent to $9.4 billion. •Total non-interest expense increased 1 percent to $4.9 billion… |
| 4 | `q9f32df79b0d7:chunk-0` | 1.0730940166792824 | 1.0 | Exhibit 99.1 News Release <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:q9f32df79b0d7`)._

### ex-dev-qa057a3d428a2

- **example_id**: `dev:qa057a3d428a2`
- **state**: `completed`
- **query**: What dependency risks exist for McKesson Corporation due to concentration of revenue in a limited number of pharmaceutical manufacturers or healthcare providers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.07816593312080208 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa057a3d428a2:chunk-95` | 20.661402367757855 |  | GENERAL Management’s discussion and analysis of financial condition and results of operations, referred to as the “Fina… |
| 2 | `qa057a3d428a2:chunk-102` | 18.990165202538254 | 1.0 | MD&A Index McKESSON CORPORATION FINANCIAL REVIEW (CONTINUED) (UNAUDITED) Revenues Revenues increased for the three and … |
| 3 | `qa057a3d428a2:chunk-110` | 17.689776027835826 |  | Any percentage changes displayed above which are not meaningful are displayed as zero percent. U.S. Pharmaceutical Thre… |
| 4 | `qa057a3d428a2:chunk-72` | 16.98138482816774 |  | McKESSON CORPORATION FINANCIAL NOTES (CONTINUED) (UNAUDITED) 10. Commitments and Contingent Liabilities In addition to … |
| 5 | `qa057a3d428a2:chunk-20` | 16.777376531089853 |  | McKESSON CORPORATION FINANCIAL NOTES (UNAUDITED) 1. Significant Accounting Policies Nature of Operations: McKesson Corp… |

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
- **S2**: nDCG@5=0.16958010263680803 · skipped= · n_scored=255

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa5c748248a5b:chunk-133` | 28.22498070306171 | 1.0 | For services where the transaction price is variable such as based upon assets under management (“AUM”), volume of trad… |
| 2 | `qa5c748248a5b:chunk-147` | 26.03727495273377 |  | The amount of revenue recognized in the period that was included in the opening current deferred revenue, which reflect… |
| 3 | `qa5c748248a5b:chunk-115` | 23.853040624770998 | 1.0 | Because of its inherent limitations, internal control over financial reporting may not prevent or detect misstatements.… |
| 4 | `qa5c748248a5b:chunk-18` | 23.687639299241376 |  | Errors and other actions by MSCI competitors could also damage the reputation of the industries that we operate in and,… |
| 5 | `qa5c748248a5b:chunk-222` | 23.501001530301 |  | The total amount of unrecognized tax benefits was $33.8 million, $32.5 million and $33.0 million as of December 31, 202… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qa5c748248a5b`)._

### ex-dev-qa602975e3d19

- **example_id**: `dev:qa602975e3d19`
- **state**: `completed`
- **query**: How has the ratio of Mondelez International’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9411655511901171 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.38685280723454163 · skipped= · n_scored=189

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa602975e3d19:chunk-107` | 24.76572242957112 |  | # PEOPLE AND COMPENSATION COMMITTEE REPORT FOR THE YEAR ENDED DECEMBER 31, 2023 (cont.) Our CEO pay ratio was calculate… |
| 2 | `qa602975e3d19:chunk-144` | 20.559605573427206 |  | # THIRD-PARTY REPORT ASSESSING EFFECTIVENESS OF IMPLEMENTATION OF HUMAN RIGHTS POLICY (cont.) The Ukrainian National Ag… |
| 3 | `qa602975e3d19:chunk-160` | 19.288700398932455 |  | # Back to Contents (cont.) (1) Divestitures include completed sales of businesses, exits of major product lines upon co… |
| 4 | `qa602975e3d19:chunk-157` | 19.187214115486356 |  | # ANNEX A: FINANCIAL MEASURES DEFINITIONS We report our financial results in accordance with U.S. GAAP. However, we use… |
| 5 | `qa602975e3d19:chunk-163` | 19.069138587970404 | 2.0 | # Back to Contents (cont.) ## Back to Contents tax obligations under the enacted tax law changes. Refer to Note 16, Inc… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qa602975e3d19`)._

### ex-dev-qa9744c8552ed

- **example_id**: `dev:qa9744c8552ed`
- **state**: `completed`
- **query**: How did analysts question TJX Companies’ management on their strategies for responsible sourcing and sustainable supply chain practices?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9452713619732751 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '10-Q', '8-K']`
- **S2**: nDCG@5=0.7227265726449519 · skipped= · n_scored=119

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa9744c8552ed:chunk-105` | 19.669521917609114 | 1.0 | # REPORT ON EFFECTIVENESS OF SOCIAL COMPLIANCE EFFORTS IN TJX'S SUPPLY CHAIN (cont.) ## Assessing Due Diligence on Huma… |
| 2 | `qa9744c8552ed:chunk-21` | 19.54572729686629 | 1.0 | # ENGAGING WITH SHAREHOLDERS (cont.) ## ONGOING SHAREHOLDER ENGAGEMENT ## Topics of engagement ## Role of engagement ##… |
| 3 | `qa9744c8552ed:chunk-9` | 19.174229970997867 | 1.0 | # CORPORATE RESPONSIBILITY HIGHLIGHTS (cont.) ## In FY24: - audited, or received audit reports from, more than 3,100 fa… |
| 4 | `qa9744c8552ed:chunk-104` | 17.294375062662727 |  | # SHAREHOLDER PROPOSALS ## SHAREHOLDER PROPOSAL ENGAGEMENT We value year-round engagement with our shareholders and oth… |
| 5 | `qa9744c8552ed:chunk-110` | 16.95101206594922 |  | # STATEMENT OF THE BOARD OF DIRECTORS IN RESPONSE TO PROPOSAL 4 (cont.) ## Shareholder Proposals (cont.) - Training: We… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qa9744c8552ed`)._

### ex-dev-qab00fabe02dc

- **example_id**: `dev:qab00fabe02dc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Rockwell Automation’s executives address regulatory or policy developments and their potential implications for industrial automation solutions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.708583264987264 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qab00fabe02dc`)._

### ex-dev-qaf55b76bfcad

- **example_id**: `dev:qaf55b76bfcad`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: Which partnership with a major telecommunications provider was highlighted for bundling offers
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.7711718900041457 · gold=['Earnings', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['8-K', '10-Q', 'Earnings', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

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
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7308969606200091 · gold=['DEF14A', '8-K', '10-K', 'Earnings']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
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
- **state**: `completed`
- **query**: What risks are associated with opening new healthcare facilities for Universal Health Services, Inc. when patient demand is uncertain?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.39769728514363656 · skipped= · n_scored=290

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb26bf8457b0f:chunk-1` | 17.246194837825477 | 1.0 | Our Mission Our company mission is: To provide superior quality healthcare services that PATIENTS recommend to families… |
| 2 | `qb26bf8457b0f:chunk-28` | 16.918054725531757 | 1.0 | we are particularly susceptible to revenue loss, cost increase, or damage caused by severe weather conditions or natura… |
| 3 | `qb26bf8457b0f:chunk-21` | 16.01104331985534 | 2.0 | The impact of the COVID-19 pandemic, which began during the second half of March, 2020, has had a material effect on ou… |
| 4 | `qb26bf8457b0f:chunk-3` | 15.981863037595547 |  | to a for-profit entity. The adoption of new or expanded conversion legislation and the increased review of not-for-prof… |
| 5 | `qb26bf8457b0f:chunk-19` | 15.863100799101177 | 1.0 | fully or partially owned by physicians, in the geographic areas in which we operate has increased significantly. As a r… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb26bf8457b0f`)._

### ex-dev-qb35a5efa65ce

- **example_id**: `dev:qb35a5efa65ce`
- **state**: `completed`
- **query**: What dependency risks exist for Evergy, Inc. due to concentration of revenue in a limited number of service territories or key industrial customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'Earnings', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.7322342245590217 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb35a5efa65ce:chunk-7` | 13.284310713088278 | 2.0 | Thanks, David, and good morning, everyone. Turning to Slide 14, I'll start with a review of our results for the fourth … |
| 2 | `qb35a5efa65ce:chunk-5` | 12.595168174816452 | 2.0 | Thanks, Pete, and good morning, everyone. Before we begin, we'd like to extend our deepest sympathies to the family of … |
| 3 | `qb35a5efa65ce:chunk-39` | 12.091836272002363 |  | Just in terms of the base demand, kind of the new incremental load customers, the 2% to 3% versus the base of 50 basis … |
| 4 | `qb35a5efa65ce:chunk-1` | 11.95734455145626 |  | Thank you for standing by, and welcome to the Q4 2023 Evergy, Inc. Earnings Conference Call. [Operator Instructions] Pl… |
| 5 | `qb35a5efa65ce:chunk-73` | 10.571351046903748 | 1.0 | Very -- just one quick follow-up question from Paul Fremont's on the Slide 9, just as opposed to the earnings impact as… |

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
| 1 | `qb500a9b42ef8:chunk-275` | 26.707403270384308 |  | Table of Contents •Level 3 inputs are unobservable inputs that reflect CMS Energy’s or Consumers’ own assumptions about… |
| 2 | `qb500a9b42ef8:chunk-425` | 22.45538992670262 |  | Table of Contents Report of Independent Registered Public Accounting Firm To the Board of Directors and Stockholders of… |
| 3 | `qb500a9b42ef8:chunk-432` | 22.123731584808333 |  | Table of Contents Item 9. Changes in and Disagreements with Accountants on Accounting and Financial Disclosure None. It… |
| 4 | `qb500a9b42ef8:chunk-19` | 20.308519910117443 |  | GCR Gas cost recovery Genesee Genesee Power Station Limited Partnership, a VIE in which HYDRA‐CO Enterprises, Inc., a w… |
| 5 | `qb500a9b42ef8:chunk-144` | 20.290236045073986 |  | Table of Contents As a result of requests for proposals, Consumers has entered into PPAs to purchase renewable capacity… |

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
| 1 | `qb590e4e6d1ec:chunk-96` | 23.183951526722602 | 1.0 | NOTES TO THE CONDENSED CONSOLIDATED FINANCIAL STATEMENTS NOTE 1: ORGANIZATION AND BASIS OF PRESENTATION Organization an… |
| 2 | `qb590e4e6d1ec:chunk-207` | 21.227338240327448 |  | The execution of the Amendment to Office Lease Agreement on July 11, 2023 triggered a modification of the Lease, which … |
| 3 | `qb590e4e6d1ec:chunk-188` | 20.411536220733012 |  | 2022 Mosquito Fire On September 6, 2022, at approximately 6:17 p.m. Pacific Time, the Utility was notified that a wildf… |
| 4 | `qb590e4e6d1ec:chunk-2` | 20.136166148538354 |  | The Utility will be permitted to recover its wildfire-related claims in excess of insurance and legal fees through rate… |
| 5 | `qb590e4e6d1ec:chunk-11` | 19.851030698347532 | 1.0 | The Utility’s electric and natural gas operating revenues that impacted earnings increased by $977 million, or 9%, in t… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qb590e4e6d1ec`)._

### ex-dev-qba0102803c57

- **example_id**: `dev:qba0102803c57`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Kimco Realty Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5087403079104241 · skipped= · n_scored=332

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba0102803c57:chunk-105` | 13.259059878827593 | 1.0 | Report of Independent Registered Public Accounting Firm To the Member of Kimco Realty OP, LLC Opinion on the Financial … |
| 2 | `qba0102803c57:chunk-198` | 11.993043070316393 |  | KIMCO REALTY CORPORATION AND SUBSIDIARIES AND KIMCO REALTY OP, LLC AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STA… |
| 3 | `qba0102803c57:chunk-12` | 11.642720389412432 | 1.0 | Item 1A. Risk Factors We are subject to certain business and legal risks including, but not limited to, the following: … |
| 4 | `qba0102803c57:chunk-103` | 11.570823498755557 |  | Report of Independent Registered Public Accounting Firm To the Board of Directors and Stockholders of Kimco Realty Corp… |
| 5 | `qba0102803c57:chunk-15` | 11.569615749413988 |  | We do not have exclusive control over our joint venture and preferred equity investments, such that we are unable to en… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qba0102803c57`)._

### ex-dev-qba50bc033945

- **example_id**: `dev:qba50bc033945`
- **state**: `completed`
- **query**: What commentary is provided by Teledyne Technologies on demand forecasts in light of government defense spending trends?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.33957710413001896 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba50bc033945:chunk-89` | 8.691149589754094 | 1.0 | Yes. Okay. And then in past quarters, you sort of broke out [indiscernible] book-to-bill versus legacy Teledyne book-to… |
| 2 | `qba50bc033945:chunk-91` | 8.479416410837224 | 1.0 | Sure. If you look at Instrumentation, which is all legacy Teledyne in some ways, which is marine, environmental and tes… |
| 3 | `qba50bc033945:chunk-115` | 7.586784159781462 |  | Last one, some of your commentary makes it sound like the M&A pipeline is pretty full and pretty active and you're pret… |
| 4 | `qba50bc033945:chunk-7` | 7.561174778616833 | 1.0 | Thank you, Robert. This is Edwin and I will report on the Digital Imaging segment, which is 56% of Teledyne's portfolio… |
| 5 | `qba50bc033945:chunk-39` | 7.071523998767612 | 1.0 | This is Jordan [indiscernible] on for Ron. I wanted to ask, so for the backlog growth in the defense wins that you guys… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qba50bc033945`)._

### ex-dev-qbd63044fc6b3

- **example_id**: `dev:qbd63044fc6b3`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What risk is associated with franchisee financial health amid rapid expansion requirements
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.8596355563650325 · gold=['10-K', 'Earnings', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
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
| 1 | `qbdbd002b0a41:chunk-53` | 14.49805084205563 |  | And that is part of the reason why we've upped the bottom end of the range because we are now more confident that, that… |
| 2 | `qbdbd002b0a41:chunk-21` | 12.836855815032708 |  | All right. Well, thanks for your question. Maybe just talk about some of the areas that we're most excited about as we … |
| 3 | `qbdbd002b0a41:chunk-73` | 12.023051233352273 |  | Well, certainly, that's what we're driving our teams to do. And one of the things we talked about, of course, is we hav… |
| 4 | `qbdbd002b0a41:chunk-33` | 10.906569136323355 |  | Yes, David, let me start on the backlog and then talk about margin guidance afterwards. On backlog, obviously, backlog … |
| 5 | `qbdbd002b0a41:chunk-3` | 10.379957390557863 |  | Thanks, Abby. Good morning, everyone, and welcome to Caterpillar's Fourth Quarter of 2023 Earnings Call. I'm Ryan Fiedl… |

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
- **S2**: nDCG@5=0.24090885754831726 · skipped= · n_scored=249

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc187429e2dc5:chunk-236` | 27.715581657607526 |  | 10.4##Intellectual Property License Agreement, dated as of March 29, 2011, between Northrop Grumman Systems Corporation… |
| 2 | `qc187429e2dc5:chunk-90` | 27.58025665853529 | 1.0 | ITEM 8. FINANCIAL STATEMENTS AND SUPPLEMENTARY DATA REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM To the Shar… |
| 3 | `qc187429e2dc5:chunk-109` | 27.335842482804235 | 2.0 | HUNTINGTON INGALLS INDUSTRIES, INC. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS 1. DESCRIPTION OF BUSINESS Huntington In… |
| 4 | `qc187429e2dc5:chunk-29` | 26.01295466803586 |  | PART II ITEM 5. MARKET FOR REGISTRANT'S COMMON EQUITY, RELATED STOCKHOLDER MATTERS AND ISSUER PURCHASES OF EQUITY SECUR… |
| 5 | `qc187429e2dc5:chunk-232` | 24.520225796038055 |  | 2.1##Separation and Distribution Agreement, dated as of March 29, 2011, among Titan II Inc. (formerly Northrop Grumman … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc187429e2dc5`)._

### ex-dev-qc20017b12da3

- **example_id**: `dev:qc20017b12da3`
- **state**: `completed`
- **query**: How does Moderna view the pace of mRNA vaccine development cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.35753408824606947 · skipped= · n_scored=11

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc20017b12da3:chunk-10` | 6.600180616177036 | 1.0 | # (Unaudited, in millions) (cont.) ## Forward-Looking Statements This press release contains forward-looking statements… |
| 2 | `qc20017b12da3:chunk-1` | 6.437706568437262 | 1.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## 2023 Commercial Updates… |
| 3 | `qc20017b12da3:chunk-2` | 6.371776053017549 |  | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## Third Quarter 2023 Fina… |
| 4 | `qc20017b12da3:chunk-3` | 6.104488622472286 |  | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## 2023 Financial Framewor… |
| 5 | `qc20017b12da3:chunk-0` | 5.857656472500697 |  | Exhibit 99.1 # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates Third quarter 2023 re… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc20017b12da3`)._

### ex-dev-qc20e5c5b254e

- **example_id**: `dev:qc20e5c5b254e`
- **state**: `completed`
- **query**: How does Evergy manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=186

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc20e5c5b254e:chunk-117` | 12.964991280306586 |  | Money Pool Evergy Kansas Central, Evergy Metro and Evergy Missouri West are authorized to participate in the Evergy, In… |
| 2 | `qc20e5c5b254e:chunk-137` | 10.952303366914728 |  | purchased power costs and amounts billed by the SPP for network transmission costs. Expenses for fuel and purchased pow… |
| 3 | `qc20e5c5b254e:chunk-114` | 9.247260306279163 |  | Regulation of Coal Combustion Residuals In the course of operating their coal generation plants, the Evergy Companies p… |
| 4 | `qc20e5c5b254e:chunk-180` | 9.158641370524808 |  | Copies of any of the exhibits filed with the SEC in connection with this document may be obtained from Evergy, Evergy K… |
| 5 | `qc20e5c5b254e:chunk-174` | 8.065805579226591 |  | ######Issuer Purchases of Equity Securities#### Month##Total Number of Shares (or Units) Purchased(a)####Average Price … |

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
- **state**: `completed`
- **query**: How could global geopolitical tensions affect Mastercard's cross?border revenues?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9411655511901171 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.5230198891268198 · skipped= · n_scored=104

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc4efe3f0f342:chunk-7` | 8.954550119079098 | 1.0 | Thanks, Michael. Turning now to Page 3, which shows our financial performance for the fourth quarter on a currency-neut… |
| 2 | `qc4efe3f0f342:chunk-73` | 8.198085584976981 |  | Look, I mean, I'll comment on the Europe piece because what you're seeing effectively in the fourth quarter of 2023, wh… |
| 3 | `qc4efe3f0f342:chunk-3` | 8.146438348218448 |  | Thank you, Brianna. Good morning, everyone, and thank you for joining us for our fourth quarter 2023 earnings call. Wit… |
| 4 | `qc4efe3f0f342:chunk-99` | 7.602478976717553 |  | Well, as always, thank you for your support to Mastercard. Thank you for listening to Sachin and me, and thank you to e… |
| 5 | `qc4efe3f0f342:chunk-5` | 7.408850754502982 | 2.0 | Thank you, Devin. Good morning, everyone. Here's the headline. We closed out 2023 with another quarter of strong earnin… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc4efe3f0f342`)._

### ex-dev-qc6c8c1f4ddfe

- **example_id**: `dev:qc6c8c1f4ddfe`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has CMS Energy Corporation’s electric utility segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.665593054087714 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
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
| 1 | `qc8e6b0d72c52:chunk-1` | 14.260336359774547 |  | Good day, and thank you for standing by. Welcome to the Caesars Entertainment, Inc. 2023 Fourth Quarter and Full Year E… |
| 2 | `qc8e6b0d72c52:chunk-111` | 7.436986336840819 |  | Great. And then as my follow-up for you or for Eric. Just how should we think about, let's call it, EBITDA flow through… |
| 3 | `qc8e6b0d72c52:chunk-127` | 6.771602525787783 |  | With respect to the North Carolina launch, this one seems kind of as fair as it gets. You have a database with the Cher… |
| 4 | `qc8e6b0d72c52:chunk-149` | 6.30981643733866 |  | Yes, that's been a big lift for us in by gaming. That table dominant player that we had is typically 100 to 150 basis p… |
| 5 | `qc8e6b0d72c52:chunk-131` | 5.853998363542677 |  | And then a follow-up to the last question, just in terms of the Vegas portfolio. So following the Versailles Tower and … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qc8e6b0d72c52`)._

### ex-dev-qcbbca1138c08

- **example_id**: `dev:qcbbca1138c08`
- **state**: `completed`
- **query**: What investor views emerged on Freeport-McMoRan’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9935051443580323 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', 'DEF14A', '10-Q', '8-K']`
- **S2**: nDCG@5=0.24153350098894139 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcbbca1138c08:chunk-51` | 10.989384869421897 | 1.0 | With regard to your proposed investments in the U.S., maybe even looking in Latin America, maybe could you remind us on… |
| 2 | `qcbbca1138c08:chunk-1` | 9.17439140729543 |  | Ladies and gentlemen, thank you for standing by. Welcome to the Freeport-McMoRan Fourth Quarter Conference Call. [Opera… |
| 3 | `qcbbca1138c08:chunk-13` | 7.797075075063945 | 1.0 | Thank you, Alex. I think it is somewhat of a new normal for the cost of a concentrator and related mining infrastructur… |
| 4 | `qcbbca1138c08:chunk-3` | 7.466453123078506 |  | Thank you, and good morning. Welcome to the Freeport-McMoRan conference call. Earlier this morning, we reported our fou… |
| 5 | `qcbbca1138c08:chunk-67` | 7.105311104194187 |  | Correct. And your $4 is absolutely right. I mean you just look at recent projects and look at how costs escalate and th… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qcbbca1138c08`)._

### ex-dev-qcdb8bc16cf2f

- **example_id**: `dev:qcdb8bc16cf2f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Jack Henry & Associates’ technology platform modernization targets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7591919243197319 · gold=['Earnings', '10-K', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

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
- **state**: `completed`
- **query**: How has Fortive Corporation’s segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.24207625393180188 · skipped= · n_scored=16

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd08d64c0654c:chunk-2` | 7.527790778209791 | 1.0 | # Fortive Reports Strong Fourth Quarter and Full Year 2023 Results Introduces First Quarter and Full Year 2024 Outlook … |
| 2 | `qd08d64c0654c:chunk-10` | 4.725975337138806 |  | # FORTIVE CORPORATION AND SUBSIDIARIES RECONCILIATION OF GAAP TO NON-GAAP FINANCIAL MEASURES AND OTHER INFORMATION (con… |
| 3 | `qd08d64c0654c:chunk-13` | 4.7207377370521995 |  | # FORTIVE CORPORATION AND SUBSIDIARIES RECONCILIATION OF GAAP TO NON-GAAP FINANCIAL MEASURES AND OTHER INFORMATION (con… |
| 4 | `qd08d64c0654c:chunk-12` | 4.301982772936303 |  | # FORTIVE CORPORATION AND SUBSIDIARIES RECONCILIATION OF GAAP TO NON-GAAP FINANCIAL MEASURES AND OTHER INFORMATION (con… |
| 5 | `qd08d64c0654c:chunk-3` | 4.09999684997177 |  | # Fortive Reports Strong Fourth Quarter and Full Year 2023 Results Introduces First Quarter and Full Year 2024 Outlook … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd08d64c0654c`)._

### ex-dev-qd177bdad4bdd

- **example_id**: `dev:qd177bdad4bdd`
- **state**: `completed`
- **query**: What pension discount rate assumption was used for year end valuation?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9751957567060058 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd177bdad4bdd:chunk-77` | 27.827882903058523 | 2.0 | Notwithstanding these actions, the impact of our postretirement benefit plans on our earnings may be volatile in that t… |
| 2 | `qd177bdad4bdd:chunk-173` | 23.27137486256122 | 2.0 | (a)A pension discount rate of 4.75% was used for the applicable plans following the transaction and remeasurement recog… |
| 3 | `qd177bdad4bdd:chunk-83` | 18.489076338689856 | 2.0 | ##Revenue recognition based on the percentage of completion method Description of the Matter##For the year ended Decemb… |
| 4 | `qd177bdad4bdd:chunk-85` | 18.017085818869838 | 2.0 | How We Addressed the Matter in Our Audit We obtained an understanding, evaluated the design and tested the operating ef… |
| 5 | `qd177bdad4bdd:chunk-163` | 17.349237824764895 | 2.0 | (a)Benefit obligation balances represent the projected benefit obligation for our qualified defined benefit pension pla… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd177bdad4bdd`)._

### ex-dev-qd2e3bd55f2ee

- **example_id**: `dev:qd2e3bd55f2ee`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about HCA Healthcare’s patient engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7083232243990188 · gold=['DEF14A', 'Earnings', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd2e3bd55f2ee`)._

### ex-dev-qd422350b37cb

- **example_id**: `dev:qd422350b37cb`
- **state**: `completed`
- **query**: What investor views emerged on Martin Marietta Materials’ geographic expansion prospects within domestic markets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9882048111454694 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3295833540079424 · skipped= · n_scored=312

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd422350b37cb:chunk-48` | 15.866758418472156 | 1.0 | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations Magnesia Speci… |
| 2 | `qd422350b37cb:chunk-46` | 13.705727390916413 | 1.0 | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations ITEM 7 – MANAG… |
| 3 | `qd422350b37cb:chunk-301` | 12.172161153181243 |  | Exhibit No.## 10.34##Form of Directors’ Restricted Stock Unit Award Agreement under the Martin Marietta Materials, Inc.… |
| 4 | `qd422350b37cb:chunk-298` | 11.717649839676866 |  | Exhibit No.## 10.20##Martin Marietta Materials, Inc. Incentive Stock Plan, as Amended (incorporated by reference to Exh… |
| 5 | `qd422350b37cb:chunk-295` | 11.467321579645665 |  | Exhibit No.## 10.10##Tenth Amendment to Credit and Security Agreement, dated as of September 28, 2018, among Martin Mar… |

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
- **state**: `completed`
- **query**: What themes emerged regarding the convergence of technology and biotechnology in the company operating model
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=176

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd5c685de4d7a:chunk-22` | 21.072772969992624 |  | # Item 1 - Election of Directors (cont.) ## Qualifications Dr. Jacks has been a director of Thermo Fisher Scientific, I… |
| 2 | `qd5c685de4d7a:chunk-17` | 20.49920390943144 |  | # Item 1 - Election of Directors (cont.) ## Other Public Company Boards: Vincerx Pharma, Inc. Brian J. Druker joined Or… |
| 3 | `qd5c685de4d7a:chunk-117` | 19.72857789928711 |  | # Executive Compensation Tables (cont.) (6) Reflects the grant date fair values of performance units granted to our NEO… |
| 4 | `qd5c685de4d7a:chunk-26` | 17.755988483405822 |  | # Item 1 - Election of Directors (cont.) ## Qualifications The Board concluded that Dr. Sugar should serve on our Board… |
| 5 | `qd5c685de4d7a:chunk-20` | 17.597361886990658 |  | # Item 1 - Election of Directors (cont.) ## Committees: - Compensation and Management Development - Corporate Responsib… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd5c685de4d7a`)._

### ex-dev-qd639a486b106

- **example_id**: `dev:qd639a486b106`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: Which general medicine candidate in obesity was identified for upcoming mid stage data readout
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.4623836304746291 · gold=['Earnings', '10-K']
- **S1 ordered**: `['8-K', '10-Q', 'DEF14A', 'Earnings', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd639a486b106`)._

### ex-dev-qd87c2da5e7da

- **example_id**: `dev:qd87c2da5e7da`
- **state**: `completed`
- **query**: How does Kenvue manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', '8-K', 'DEF14A']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.36005461457723403 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd87c2da5e7da:chunk-113` | 12.49208384249473 |  | # 2024 Proxy Materials ## Why am I receiving these proxy materials? Our Board of Directors has made these materials ava… |
| 2 | `qd87c2da5e7da:chunk-56` | 12.30503614663786 | 1.0 | # 2024 Incentive Compensation (cont.) ## 2024 Long-Term Incentive Award Design Annual long-term incentive awards grante… |
| 3 | `qd87c2da5e7da:chunk-110` | 11.414458028352485 |  | # Information About the Annual Meeting (cont.) ## How do \| vote? If you hold your shares in a brokerage account in your… |
| 4 | `qd87c2da5e7da:chunk-9` | 10.68447505752855 | 1.0 | # Executive Compensation Highlights (page 35) Kenvue's executive compensation program is designed to align behaviors wi… |
| 5 | `qd87c2da5e7da:chunk-31` | 10.638065183133314 |  | # Board Oversight Responsibilities (cont.) ## Oversight of Human Capital and Succession Planning The Board considers ef… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qd87c2da5e7da`)._

### ex-dev-qdb9da6a1e373

- **example_id**: `dev:qdb9da6a1e373`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Packaging Corporation of America manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8616884617566115 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdb9da6a1e373`)._

### ex-dev-qdbaa829dd4cc

- **example_id**: `dev:qdbaa829dd4cc`
- **state**: `completed`
- **query**: What questions were asked about Gen Digital Inc.’s customer retention and renewal rates?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9452713619732751 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=227

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdbaa829dd4cc:chunk-80` | 17.051310948129537 |  | GEN DIGITAL INC. Notes to the Consolidated Financial Statements Note 1. Description of Business and Significant Account… |
| 2 | `qdbaa829dd4cc:chunk-0` | 15.929423931253778 |  | PART I Item 1. Business Purpose and Mission Purpose: Powering Digital Freedom. Mission: We create technology solutions … |
| 3 | `qdbaa829dd4cc:chunk-223` | 15.484382816051157 |  | ##GEN DIGITAL INC.## By:####/s/ Vincent Pilette ####Vincent Pilette Chief Executive Officer and Director |
| 4 | `qdbaa829dd4cc:chunk-36` | 14.486713203364845 |  | (1) Non-GAAP Direct customer revenue differs from U.S. GAAP direct customer revenue in fiscal 2023 because it excludes … |
| 5 | `qdbaa829dd4cc:chunk-1` | 14.315709307161324 |  | Seasonality As is typical for many consumer technology companies, portions of our business are impacted by seasonality.… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdbaa829dd4cc`)._

### ex-dev-qdec70f55027f

- **example_id**: `dev:qdec70f55027f`
- **state**: `completed`
- **query**: What investor views emerged on Mettler-Toledo International Inc.’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9979470946084208 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdec70f55027f:chunk-1` | 14.154986658129195 |  | Good morning. My name is Audra, and I will be your conference operator today. At this time, I would like to welcome eve… |
| 2 | `qdec70f55027f:chunk-75` | 6.670760264022843 |  | No. I mean I'll start and let Patrick jump in if he wants to. I think the challenge with pipettes right now is that the… |
| 3 | `qdec70f55027f:chunk-39` | 5.776083097256064 |  | Derik, maybe I'll start off. So maybe I'll start off with the latter part of the question with the Red Sea and the Midd… |
| 4 | `qdec70f55027f:chunk-65` | 5.594975258030797 |  | Yes. So our share buyback assumption is $850 million, which I think is the same or similar number as we're thinking fre… |
| 5 | `qdec70f55027f:chunk-49` | 5.560914916831718 |  | Patrick, just wondering if -- Patrick, I'll start with you. Wondering if you could give an update on just how you perce… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdec70f55027f`)._

### ex-dev-qdfe52ef66df5

- **example_id**: `dev:qdfe52ef66df5`
- **state**: `completed`
- **query**: How has the ratio of IDEXX Laboratories’ recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9452713619732751 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.4682601310708423 · skipped= · n_scored=271

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdfe52ef66df5:chunk-46` | 25.480245490988004 | 1.0 | The prevalence of in-clinic testing, as opposed to outside reference laboratories such as IDEXX Reference Laboratories,… |
| 2 | `qdfe52ef66df5:chunk-45` | 25.37967337356396 | 2.0 | Our long-term success in the continuing growth of our CAG recurring diagnostic products and services is dependent upon:… |
| 3 | `qdfe52ef66df5:chunk-131` | 22.299938983701843 | 1.0 | Major Categories of Revenue for our Products and Services Diagnostic Products and Accessories. Diagnostic products and … |
| 4 | `qdfe52ef66df5:chunk-134` | 21.999744008809195 |  | instruments of $14.6 million compared to $17.4 million during the year ended December 31, 2022, from inventory to prope… |
| 5 | `qdfe52ef66df5:chunk-42` | 21.83097336682381 | 1.0 | ITEM 7. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following discussion … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qdfe52ef66df5`)._

### ex-dev-qe1811f4fd3dc

- **example_id**: `dev:qe1811f4fd3dc`
- **state**: `completed`
- **query**: What questions were asked about Digital Realty Trust’s customer or tenant engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9196027125796398 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=108

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qe1811f4fd3dc:chunk-1` | 9.987253644772064 |  | Good afternoon, and welcome to the Digital Realty Fourth Quarter 2023 Earnings Call. Please note, this event is being r… |
| 2 | `qe1811f4fd3dc:chunk-105` | 9.762986086357907 |  | Thank you, Betsy. Digital Realty capped off a transformative 2023 with a strong fourth quarter that was highlighted by … |
| 3 | `qe1811f4fd3dc:chunk-11` | 9.10807287508392 |  | Thanks, and good afternoon. A couple of questions. First, in terms of -- you were just describing the shift in same cap… |
| 4 | `qe1811f4fd3dc:chunk-3` | 7.200975950031606 |  | Thank you, operator, and welcome, everyone, to Digital Realty's Fourth Quarter 2023 Earnings Conference Call. Joining m… |
| 5 | `qe1811f4fd3dc:chunk-5` | 6.9486636214659345 |  | Thanks, Jordan, and thanks to everyone for joining our call. 2023 was a milestone year for Digital Realty as we made st… |

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
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9873464281832952 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.5087403079104241 · skipped= · n_scored=140

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeccd6f3b9d06:chunk-101` | 10.210574354255243 | 2.0 | So the new product, Gecko, it is primarily a serverless product, it sounds like. And do you have all the support there … |
| 2 | `qeccd6f3b9d06:chunk-1` | 9.095291966579731 |  | Good afternoon, and welcome to the Akamai Technologies, Inc. Fourth Quarter 2023 Earnings Conference Call. [Operator In… |
| 3 | `qeccd6f3b9d06:chunk-67` | 8.975480222898096 | 2.0 | Yes. Compute is an enormous marketplace and growing rapidly, and there's always new applications that are being created… |
| 4 | `qeccd6f3b9d06:chunk-127` | 7.680270126406768 |  | Just one question from me. How important is the global load balancing capability? And what does that maybe mean for you… |
| 5 | `qeccd6f3b9d06:chunk-3` | 7.570954052966892 |  | Thank you, operator. Good afternoon, everyone, and thank you for joining Akamai's Fourth Quarter 2023 Earnings Call. Sp… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qeccd6f3b9d06`)._

### ex-dev-qf13afdfcadcf

- **example_id**: `dev:qf13afdfcadcf`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did Howmet Aerospace Inc.’s leadership say about Howmet Aerospace Inc.’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7146598531416503 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '8-K', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf13afdfcadcf`)._

### ex-dev-qf25e1308bae4

- **example_id**: `dev:qf25e1308bae4`
- **state**: `completed`
- **query**: Which investor concerns about the company’s China exposure did management acknowledge?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9750432864211677 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.3065735963827292 · skipped= · n_scored=74

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf25e1308bae4:chunk-33` | 8.120777886494748 |  | Congrats on the results. I wanted to ask, I guess, a 2-part question, and it comes at what Stacy was getting at on your… |
| 2 | `qf25e1308bae4:chunk-59` | 7.601767514845278 |  | I wanted to ask about the China business. I know that in the prepared comments, you said that you started shipping some… |
| 3 | `qf25e1308bae4:chunk-61` | 7.369890206044037 | 1.0 | At the core, remember, the U.S. government wants to limit the latest capabilities of NVIDIA's accelerated computing and… |
| 4 | `qf25e1308bae4:chunk-3` | 5.840470439494608 |  | Thank you. Good afternoon, everyone, and welcome to NVIDIA's conference call for the fourth quarter and fiscal 2024. Wi… |
| 5 | `qf25e1308bae4:chunk-67` | 5.3891456682650585 |  | Let me take a step back and explain the fundamental reason why NVIDIA will be very successful in software. So first, as… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf25e1308bae4`)._

### ex-dev-qf38450369367

- **example_id**: `dev:qf38450369367`
- **state**: `completed`
- **query**: What investor views emerged on Nordson Corporation’s international or geographic expansion prospects?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf38450369367:chunk-17` | 13.19740399926541 |  | # Present Directors with Terms Expiring in 2026 (cont.) ## Committees: - Invacare Corporation (NYSE: IVC) (2014-2018), … |
| 2 | `qf38450369367:chunk-24` | 10.587336073567108 |  | # Table of Contents (cont.) ## Consideration of Director Candidates Recommended by Shareholders Under its charter, the … |
| 3 | `qf38450369367:chunk-22` | 9.74679741598322 |  | # Table of Contents (cont.) ## Table of Contents As part of our commitment to ensuring director independence, and in ac… |
| 4 | `qf38450369367:chunk-105` | 9.600186836654707 |  | # QUESTIONS AND ANSWERS ABOUT THE ANNUAL MEETING AND THESE PROXY MATERIALS (cont.) ## Table of Contents obtain a valid … |
| 5 | `qf38450369367:chunk-95` | 9.327666240548563 |  | # CEO PAY RATIO As required by Section 953(b) of the Dodd-Frank Wall Street Reform and Consumer Protection Act of 2010 … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf38450369367`)._

### ex-dev-qf5b4bbe60015

- **example_id**: `dev:qf5b4bbe60015`
- **state**: `completed`
- **query**: How has Cadence Design Systems’ IP segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.3065735963827292 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf5b4bbe60015:chunk-2` | 10.861666960230204 |  | •Major long-term development partner broadly deployed Palladium Z3 to deliver to its next generation AI product roadmap… |
| 2 | `qf5b4bbe60015:chunk-3` | 7.414849827863877 |  | In addition, the timing and amount of Cadence’s repurchases of its common stock are subject to business and market cond… |
| 3 | `qf5b4bbe60015:chunk-1` | 5.8555295738758435 | 1.0 | For fiscal year 2024, the company expects: •Revenue in the range of $4.60 billion to $4.66 billion •GAAP operating marg… |
| 4 | `qf5b4bbe60015:chunk-10` | 5.153393555835331 |  | * Includes, as applicable, equity in losses or income from investments, write-down of investments, gains or losses on i… |
| 5 | `qf5b4bbe60015:chunk-22` | 4.779762187219795 |  | † The non-GAAP measures presented in the table above should not be considered a substitute for financial results and me… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qf5b4bbe60015`)._

### ex-dev-qf7a3126727b8

- **example_id**: `dev:qf7a3126727b8`
- **state**: `completed`
- **query**: How does Sysco Corporation’s debt maturity profile affect liquidity and cost structure?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9840990003623115 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=148

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf7a3126727b8:chunk-17` | 16.988084807058662 |  | # BOARD LEADERSHIP STRUCTURE (cont.) ## BOARD COMMITTEES The Board has six standing committees: Audit Committee, Compen… |
| 2 | `qf7a3126727b8:chunk-15` | 13.16455080115089 |  | # BOARD LEADERSHIP STRUCTURE (cont.) ## DIRECTOR INDEPENDENCE Our Guidelines require that at least a majority of our di… |
| 3 | `qf7a3126727b8:chunk-137` | 12.530628754159821 |  | # QUESTIONS AND ANSWERS ABOUT THE MEETING AND VOTING (cont.) ## 12. What votes are necessary for action to be taken? Sy… |
| 4 | `qf7a3126727b8:chunk-3` | 11.368161573214136 |  | # LETTER FROM OUR CEO AND CHAIRMAN (cont.) ## Dear Sysco Stockholder, Throughout our rich 54-year history, Sysco has ma… |
| 5 | `qf7a3126727b8:chunk-14` | 11.302630631952344 |  | # BOARD LEADERSHIP STRUCTURE The Corporate Governance Guidelines provide that the roles of Chairman and CEO may be sepa… |

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
| 1 | `qf8cbcec9fec6:chunk-111` | 25.732607292902422 |  | # Annex A (cont.) ## RECONCILIATION OF GAAP MEASURES TO NON-GAAP MEASURES In addition to consolidated GAAP financial me… |
| 2 | `qf8cbcec9fec6:chunk-52` | 24.14120580801232 |  | # Compensation Discussion and Analysis (cont.) ## ACCELERATE GROWTH <figure description="This image shows a stylized lo… |
| 3 | `qf8cbcec9fec6:chunk-98` | 23.651144752691454 |  | # DIRECTOR COMPENSATION IN FISCAL 2023 (cont.) ## CEO PAY RATIO As required by Section 953(b) of the Dodd-Frank Wall St… |
| 4 | `qf8cbcec9fec6:chunk-55` | 21.40205285864111 |  | # Compensation Discussion and Analysis (cont.) ## ALLOCATE CAPITAL EFFECTIVELY (cont.) - 7 The use by Ingersoll Rand of… |
| 5 | `qf8cbcec9fec6:chunk-70` | 19.93712294994569 |  | # Components of Performance-Based Award (cont.) ## The Decision-Making Process (cont.) directly to the Committee and th… |

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
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7659463877163701 · gold=['DEF14A', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qfa38830206fb`)._

### ex-dev-qfbef9973c7fb

- **example_id**: `dev:qfbef9973c7fb`
- **state**: `completed`
- **query**: What clarification did management provide on margin durability in the face of potential memory‑cost inflation?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=74

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qfbef9973c7fb:chunk-49` | 12.022862592905694 | 1.0 | Yes, thanks for the question. We highlighted in our opening remarks, really about our Q4 results and our outlook for Q1… |
| 2 | `qfbef9973c7fb:chunk-35` | 6.485889667688881 |  | Let me first start with your question, thanks, about how we are working with our customers as they look into how they a… |
| 3 | `qfbef9973c7fb:chunk-47` | 5.915139033857061 |  | Congratulations on the results. Colette, I wanted to talk about your comment regarding gross margins and that it should… |
| 4 | `qfbef9973c7fb:chunk-71` | 5.361246333776237 |  | The computer industry is making two simultaneous platform shifts at the same time. The trillion-dollar installed base o… |
| 5 | `qfbef9973c7fb:chunk-33` | 5.1991861083497275 |  | Congrats on the results. I wanted to ask, I guess, a 2-part question, and it comes at what Stacy was getting at on your… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qfbef9973c7fb`)._

### ex-dev-qfd572ccfcb0f

- **example_id**: `dev:qfd572ccfcb0f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Hasbro’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7085011369669131 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qfd572ccfcb0f`)._

### ex-dev-qff56bedc2f87

- **example_id**: `dev:qff56bedc2f87`
- **state**: `completed`
- **query**: What questions were asked about Globe Life Inc.’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9134693626978977 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=114

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff56bedc2f87:chunk-1` | 11.835533643408723 |  | Hello, and welcome to Globe Life Inc.'s Fourth Quarter 2023 Earnings Release. My name is Melissa, and I will be your op… |
| 2 | `qff56bedc2f87:chunk-7` | 8.776880800064804 |  | Thank you, Frank. At American Income Life, life premiums were up 7% over the year ago quarter to $406 million, and life… |
| 3 | `qff56bedc2f87:chunk-67` | 8.17319972510784 |  | I'd say it would be more of a shift toward -- we're still not going to take our foot off the gas from a recruiting pers… |
| 4 | `qff56bedc2f87:chunk-105` | 7.10292077031456 |  | And then just one more, if I could. The -- so when I look at the dividends and share repo guidance for '24, $440 millio… |
| 5 | `qff56bedc2f87:chunk-39` | 7.0833070965461875 |  | Yes. For 2024, we have about $70 million of our total direct commercial mortgage loans maturing. Of that is about $4 mi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qff56bedc2f87`)._

### ex-dev-qff73996028bf

- **example_id**: `dev:qff73996028bf`
- **state**: `completed`
- **query**: How has Williams-Sonoma’s management addressed supply-chain risks and efforts to enhance Williams-Sonoma’s resilience?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.24090885754831726 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff73996028bf:chunk-4` | 24.39217643709933 | 1.0 | Table of Contents caregiver benefits; tax-free commuter benefits; wellness programs including telehealth visits; time o… |
| 2 | `qff73996028bf:chunk-0` | 21.42752096295411 | 1.0 | PART I ITEM 1. BUSINESS OVERVIEW Williams-Sonoma, Inc., (the "Company”, "we", or "us") incorporated in 1973, is an omni… |
| 3 | `qff73996028bf:chunk-37` | 19.12148036977184 | 1.0 | Table of Contents ITEM 7. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The fol… |
| 4 | `qff73996028bf:chunk-136` | 16.803072607754537 |  | ##STOCK PLANS## 10.3+####Williams-Sonoma, Inc. 2001 Long-Term Incentive Plan, as amended (incorporated by reference to … |
| 5 | `qff73996028bf:chunk-139` | 16.299258060261234 |  | 10.16####Lease for an additional Company distribution facility located in Olive Branch, Mississippi between Williams-So… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `dev:qff73996028bf`)._

### ex-eval-chunk-only-chunk-q0b530d

- **example_id**: `eval:chunk-only:chunk_q0b530d`
- **state**: `completed`
- **query**: How does Brown-Forman view the pace of product innovation cycles and their effect on market competitiveness in the spirits industry?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=90

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q0b530d:10-K:chunk-87` | 12.929824700856214 |  | Thank you, and thank you to Lawson and Leanne and to everyone for joining us today for Brown-Forman's Fourth Quarter an… |
| 2 | `chunk_q0b530d:10-K:chunk-5` | 11.838187738875765 |  | Thank you, Sue, and good morning, everyone. Thank you for joining us today as we share Brown-Forman's fiscal 2024 resul… |
| 3 | `chunk_q0b530d:10-K:chunk-35` | 11.139072624952968 |  | That's helpful. And then maybe just one quick follow-up. You've sort of talked about your excitement about a return to … |
| 4 | `chunk_q0b530d:10-K:chunk-71` | 10.808003234281147 |  | I'll start with your last one first because it's the most succinct which is about what we will be comping in the second… |
| 5 | `chunk_q0b530d:10-K:chunk-21` | 10.611203976961036 |  | One short term and one long term for me. On the short term, coming back to inventories, obviously, large headwind in th… |

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
| 1 | `chunk_q29280e:10-K:chunk-25` | 9.767380792223758 |  | # Director Compensation (cont.) ## Long-Term Compensation Each non-employee director is also eligible to participate in… |
| 2 | `chunk_q29280e:10-K:chunk-27` | 9.398491132776583 |  | # Director Compensation (cont.) ## Summary of Cash and Other Compensation (cont.) (c) The amounts in this column repres… |
| 3 | `chunk_q29280e:10-K:chunk-3` | 8.881854094757074 |  | # Notice of Annual Meeting of Shareholders (cont.) ## Annual Meeting Business Atmos Energy Corporation's annual meeting… |
| 4 | `chunk_q29280e:10-K:chunk-36` | 8.453141573321037 |  | # Fiscal 2023 Executive Compensation Program The following table summarizes the various elements of compensation that w… |
| 5 | `chunk_q29280e:10-K:chunk-34` | 8.228973057436107 |  | # Compensation Discussion & Analysis (cont.) ## Fiscal 2023 Business and Performance Highlights Over the past twelve ye… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q29280e`)._

### ex-eval-chunk-only-chunk-q2ccba5

- **example_id**: `eval:chunk-only:chunk_q2ccba5`
- **state**: `completed`
- **query**: What questions were asked about Boston Scientific’s customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q2ccba5:Earnings:chunk-113` | 12.628378925819405 |  | Thanks for joining us today. We appreciate your interest in Boston Scientific. If we were unable to get to your questio… |
| 2 | `chunk_q2ccba5:Earnings:chunk-9` | 9.299980577091691 |  | Thanks so much, Dan. Drew, let's open it up to questions for the next 30 minutes or so. [Operator Instructions] Drew, p… |
| 3 | `chunk_q2ccba5:Earnings:chunk-75` | 8.195090886408627 |  | Congratulations for a strong end of the year. I wanted to ask about the international cardiac ablation market. Boston h… |
| 4 | `chunk_q2ccba5:Earnings:chunk-1` | 7.3509845074916225 |  | Good morning, and welcome to the Boston Scientific Fourth Quarter 2023 Earnings Call. [Operator Instructions] Please no… |
| 5 | `chunk_q2ccba5:Earnings:chunk-63` | 6.085102140100204 |  | Maybe one more follow-up on TAVR. Could you remind us what the interim look was? Was that just like a 6-month look at t… |

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
| 1 | `chunk_q44d295:10-Q:chunk-109` | 27.035982371661838 |  | control of the goods transfers, rather than when the goods are delivered, and title, risk and reward of ownership are p… |
| 2 | `chunk_q44d295:10-Q:chunk-85` | 24.17737826439567 |  | Critical Accounting Estimates The preparation of consolidated financial statements in conformity with accounting princi… |
| 3 | `chunk_q44d295:10-Q:chunk-105` | 24.12562914101179 |  | AMPHENOL CORPORATION Notes to Consolidated Financial Statements (All amounts included in the following Notes to Consoli… |
| 4 | `chunk_q44d295:10-Q:chunk-114` | 23.46295368473986 |  | entities to provide more detailed disclosures regarding supplier finance programs used in connection with the purchase … |
| 5 | `chunk_q44d295:10-Q:chunk-215` | 22.611872211681405 |  | Item 9. Changes in and Disagreements with Accountants on Accounting and Financial Disclosure None. Item 9A. Controls an… |

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
| 1 | `chunk_q5ebb5e:Earnings:chunk-90` | 15.452749845717548 |  | # IMPORTANT INFORMATION ABOUT AES' VIRTUAL ANNUAL MEETING (cont.) ## Where can I find additional information? Additiona… |
| 2 | `chunk_q5ebb5e:Earnings:chunk-92` | 13.536115975821723 |  | # QUESTIONS AND ANSWERS REGARDING THE PROXY STATEMENT AND ANNUAL MEETING (cont.) ## How does the Company solicit proxie… |
| 3 | `chunk_q5ebb5e:Earnings:chunk-96` | 12.036518251883422 |  | # QUESTIONS AND ANSWERS REGARDING THE PROXY STATEMENT AND ANNUAL MEETING (cont.) ## What is Householding? The SEC has a… |
| 4 | `chunk_q5ebb5e:Earnings:chunk-3` | 11.234125754128724 |  | # Table of Contents (cont.) <figure description="This image shows a headshot of an older gentleman with gray hair weari… |
| 5 | `chunk_q5ebb5e:Earnings:chunk-101` | 11.010512762888911 |  | # Reconciliation of Parent Free Cash Flow1 (cont.) 1 Parent Free Cash Flow (a non-GAAP financial measure that was used … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q5ebb5e`)._

### ex-eval-chunk-only-chunk-q829eae

- **example_id**: `eval:chunk-only:chunk_q829eae`
- **state**: `completed`
- **query**: What guidance was offered on Amazon’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q829eae:10-K:chunk-89` | 12.005159478173535 |  | Table of Contents Guidance We provided guidance on October 26, 2023, in our earnings release furnished on Form 8-K as s… |
| 2 | `chunk_q829eae:10-K:chunk-68` | 10.586276665379879 |  | Table of Contents Results of Operations We have organized our operations into three segments: North America, Internatio… |
| 3 | `chunk_q829eae:10-K:chunk-97` | 9.776220169504793 |  | Table of Contents effect on our operating results, there can be no assurance that future incidents will not have materi… |
| 4 | `chunk_q829eae:10-K:chunk-42` | 9.11643852845403 |  | Table of Contents Other Contingencies We are disputing claims and denials of refunds or credits, and monitoring or eval… |
| 5 | `chunk_q829eae:10-K:chunk-63` | 8.238258350678258 |  | Table of Contents Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations Forward… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q829eae`)._

### ex-eval-chunk-only-chunk-q8fc814

- **example_id**: `eval:chunk-only:chunk_q8fc814`
- **state**: `completed`
- **query**: What guidance was offered on Apollo Global Management’s fundraising targets for new investment vehicles?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', 'Earnings', '8-K', '10-Q']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=78

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q8fc814:10-K:chunk-1` | 15.227046381345398 |  | Good morning, and welcome to Apollo Global Management's Fourth Quarter and Full Year 2023 Earnings Conference Call. [Op… |
| 2 | `chunk_q8fc814:10-K:chunk-7` | 12.508739659452237 |  | Thanks, Marc. Echoing Marc's sentiment. We entered 2023 focused squarely on executing the growth plan we set forth, and… |
| 3 | `chunk_q8fc814:10-K:chunk-39` | 10.549466301410886 |  | I think you're hearing from us. In a week or 2, on the fixed income call, you'll hear from Jim Belardi. And if you look… |
| 4 | `chunk_q8fc814:10-K:chunk-13` | 8.645860104289312 |  | So Marc, a lot of really good big picture type of views as you sort of think through the new order here. One thing I so… |
| 5 | `chunk_q8fc814:10-K:chunk-25` | 8.620590898679916 |  | So we -- when we set out our 5-year targets a little over 2 years ago, we -- the 5-year target was to get to $150 billi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q8fc814`)._

### ex-eval-chunk-only-chunk-q9fad72

- **example_id**: `eval:chunk-only:chunk_q9fad72`
- **state**: `completed`
- **query**: What guidance was offered on CDW Corporation’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q9fad72:10-K:chunk-18` | 12.81579096843208 |  | and revenue levels. An adverse change in government spending policies (such as budget cuts or limitations), shifts in b… |
| 2 | `chunk_q9fad72:10-K:chunk-16` | 12.247476976469407 |  | If we are unable to attract, develop, engage and retain key personnel, or if our approach to workforce management is in… |
| 3 | `chunk_q9fad72:10-K:chunk-14` | 9.617199887444984 |  | •keep pace with changes and innovation and compete effectively; •effectuate comprehensive and reliable data collection,… |
| 4 | `chunk_q9fad72:10-K:chunk-131` | 9.52690780654004 |  | As of December 31, 2023, the Company is in compliance with the covenants under its credit agreements and indentures. Cr… |
| 5 | `chunk_q9fad72:10-K:chunk-202` | 8.17929580429667 |  | Exhibit Number##Description 10.19§##Form of Restricted Stock Unit Award Agreement under the CDW Corporation Amended and… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:chunk-only:chunk_q9fad72`)._

### ex-eval-doc-q0617ad

- **example_id**: `eval:doc_q0617ad`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did F5’s leadership say about F5’s share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '8-K', 'Earnings', '10-K', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:doc_q0617ad`)._

### ex-eval-doc-q48ce69

- **example_id**: `eval:doc_q48ce69`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did energy cost inflation impact theme park utility expenses
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:doc_q48ce69`)._

### ex-eval-doc-q737b56

- **example_id**: `eval:doc_q737b56`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about Deckers Outdoor Corporation’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:doc_q737b56`)._

### ex-eval-doc-qa9fda3

- **example_id**: `eval:doc_qa9fda3`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does The AES Corporation account for currency and economic volatility in its risk management disclosures?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-p1-ceilings-n200.inspect.html) (search for `eval:doc_qa9fda3`)._
