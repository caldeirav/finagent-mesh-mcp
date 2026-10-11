# Pair `lux-e5` — `paper-n200-full`

[← compact index](../paper-n200-full.inspect.md) · **Download full HTML**: [raw](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) · [`paper-n200-full.inspect.html`](../paper-n200-full.inspect.html)

- eval_run_id: `paper-n200-retry:lux-e5`
- S1=`decision20-lux` · S2=`e5-base`
- row status: `completed` · completed=119 · failed_retriable=81

## Examples

### ex-dev-chunk-only-q075970f6eb46

- **example_id**: `dev:chunk-only:q075970f6eb46`
- **state**: `completed`
- **query**: What did Fastenal Company’s leadership say about Fastenal Company’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '10-Q', '8-K']`
- **S2**: nDCG@5=0.4703652827859579 · skipped= · n_scored=105

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q075970f6eb46:DEF14A:chunk-22` | 0.8435002565383911 | 1.0 | (1) The fasteners product line represents fasteners and miscellaneous supplies. (3) Stockholders' Equity Dividends On O… |
| 2 | `q075970f6eb46:DEF14A:chunk-15` | 0.8293052911758423 |  | FASTENAL COMPANY AND SUBSIDIARIES Notes to Condensed Consolidated Financial Statements (Amounts in millions except shar… |
| 3 | `q075970f6eb46:DEF14A:chunk-103` | 0.8272388577461243 |  | ####FASTENAL COMPANY Date: October 17, 2023##By:##/s/ Holden Lewis ####Holden Lewis ####Senior Executive Vice President… |
| 4 | `q075970f6eb46:DEF14A:chunk-37` | 0.8248634338378906 |  | ITEM 2 — MANAGEMENT'S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The following is managem… |
| 5 | `q075970f6eb46:DEF14A:chunk-36` | 0.8215879201889038 | 1.0 | FASTENAL COMPANY AND SUBSIDIARIES Notes to Condensed Consolidated Financial Statements (Amounts in millions except shar… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q075970f6eb46`)._

### ex-dev-chunk-only-q0fd4ca04c0a5

- **example_id**: `dev:chunk-only:q0fd4ca04c0a5`
- **state**: `completed`
- **query**: How does Molina Healthcare view the pace of innovation cycles in healthcare delivery and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0fd4ca04c0a5:10-K:chunk-0` | 0.8348748087882996 |  | PART I Item 1. BUSINESS OVERVIEW ABOUT MOLINA HEALTHCARE Molina Healthcare, Inc., a FORTUNE 500 company, provides manag… |
| 2 | `q0fd4ca04c0a5:10-K:chunk-91` | 0.8292670249938965 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS 1. Organization and Basis of Presentation Organization and Operations Molina… |
| 3 | `q0fd4ca04c0a5:10-K:chunk-16` | 0.8133387565612793 |  | plans maintained, and one plan had an increase of 0.5 Stars. The decreases to the 2024 Star Ratings impact the 2025 bon… |
| 4 | `q0fd4ca04c0a5:10-K:chunk-211` | 0.8110613226890564 |  | ##MOLINA HEALTHCARE, INC.## By:####/s/ Joseph M. Zubretsky ####Joseph M. Zubretsky ####Chief Executive Officer (Princip… |
| 5 | `q0fd4ca04c0a5:10-K:chunk-206` | 0.8108983635902405 |  | REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM To the Stockholders and the Board of Directors of Molina Health… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q0fd4ca04c0a5`)._

### ex-dev-chunk-only-q299865e6e67e

- **example_id**: `dev:chunk-only:q299865e6e67e`
- **state**: `completed`
- **query**: What dependency risks exist for Consolidated Edison due to concentration of revenue in a limited number of service territories or customer segments?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.2054778775428881 · skipped= · n_scored=286

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q299865e6e67e:10-K:chunk-117` | 0.8206286430358887 | 1.0 | Note M – Financial Information by Business Segment Con Edison’s principal business segments are CECONY’s regulated util… |
| 2 | `q299865e6e67e:10-K:chunk-282` | 0.8133280873298645 |  | Pursuant to Item 601(b)(4)(iii)(A) of Regulation S-K, instruments defining the rights of holders of long-term debt of C… |
| 3 | `q299865e6e67e:10-K:chunk-132` | 0.8096174001693726 |  | (a)Volumes are reported net of long and short positions, except natural gas collars where the volumes of long positions… |
| 4 | `q299865e6e67e:10-K:chunk-108` | 0.8064161539077759 | 1.0 | (a) For the Utilities, this includes primarily revenue or negative revenue adjustments from alternative revenue program… |
| 5 | `q299865e6e67e:10-K:chunk-111` | 0.8062331676483154 | 1.0 | (a) For the Utilities, this includes primarily revenue or negative revenue adjustments from alternative revenue program… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q299865e6e67e`)._

### ex-dev-chunk-only-q2a401c1edf73

- **example_id**: `dev:chunk-only:q2a401c1edf73`
- **state**: `completed`
- **query**: How often is Exxon Mobil Corporation’s executive compensation program reviewed and updated?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.2611321305916629 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2a401c1edf73:DEF14A:chunk-77` | 0.8670871257781982 |  | # OTHER COMPENSATION ELEMENTS (cont.) ## TAX MATTERS The Company does not provide tax assistance for either bonus or pe… |
| 2 | `q2a401c1edf73:DEF14A:chunk-82` | 0.858396053314209 | 1.0 | # FREQUENTLY USED TERMS (cont.) ## Exxon Mobil 2024 Proxy Statement # Table of Contents # FOOTNOTES 1 Total Direct Comp… |
| 3 | `q2a401c1edf73:DEF14A:chunk-50` | 0.857643187046051 |  | # Table of Contents (cont.) ## Table of Contents - Payments under ExxonMobil plans and arrangements that are available … |
| 4 | `q2a401c1edf73:DEF14A:chunk-55` | 0.8556101322174072 | 2.0 | # EXECUTIVE COMPENSATION (cont.) ## EXECUTIVE COMPENSATION TABLES <table><tr><th>Summary Compensation Table</th><th>70<… |
| 5 | `q2a401c1edf73:DEF14A:chunk-75` | 0.8534670472145081 | 1.0 | # 2023 COMPENSATION ACTIONS MANAGEMENT COMMITTEE (cont.) ## JACK P. WILLIAMS, JR., SENIOR VICE PRESIDENT (cont.) Angela… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q2a401c1edf73`)._

### ex-dev-chunk-only-q3a71644741b7

- **example_id**: `dev:chunk-only:q3a71644741b7`
- **state**: `completed`
- **query**: What questions were asked about Conagra Brands’ customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.33132295434224884 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3a71644741b7:Earnings:chunk-67` | 0.8411605358123779 | 1.0 | Maybe I can just follow up on Rob's question from a different angle. And Sean, I'd love to hear your perspective on thi… |
| 2 | `q3a71644741b7:Earnings:chunk-1` | 0.8408032655715942 |  | Good morning, everyone, and welcome to the Conagra Brands Q4 and Fiscal Year 2024 Earnings Conference Call. [Operator I… |
| 3 | `q3a71644741b7:Earnings:chunk-7` | 0.8297687768936157 | 2.0 | Sean, you talked in the prepared remarks about expecting a sort of a gradual transition in fiscal '25 to a more normal … |
| 4 | `q3a71644741b7:Earnings:chunk-9` | 0.8291506767272949 | 1.0 | Sure, Andrew. Here's how I think about that. The operative word is transition. It's a process. It's not an event. And a… |
| 5 | `q3a71644741b7:Earnings:chunk-99` | 0.8079882860183716 |  | Yes. There's a bunch in there, Rob. Let me just mention real quick on the first part in terms of what we call our stapl… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q3a71644741b7`)._

### ex-dev-chunk-only-q40d417892141

- **example_id**: `dev:chunk-only:q40d417892141`
- **state**: `completed`
- **query**: What investor views emerged on D.R. Horton’s geographic expansion prospects within new U.S. housing markets?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=27

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q40d417892141:Earnings:chunk-0` | 0.8268579244613647 |  | Exhibit 99.1 D.R. HORTON, INC., AMERICA’S BUILDER, REPORTS FISCAL 2024 FIRST QUARTER EARNINGS AND DECLARES QUARTERLY DI… |
| 2 | `q40d417892141:Earnings:chunk-4` | 0.8223890066146851 |  | •Consolidated revenues of approximately $36.0 billion to $37.3 billion •Homes closed by homebuilding operations of 87,0… |
| 3 | `q40d417892141:Earnings:chunk-1` | 0.8149225115776062 |  | The Company's return on equity (ROE) was 21.8% for the trailing twelve months ended December 31, 2023, and homebuilding… |
| 4 | `q40d417892141:Earnings:chunk-26` | 0.8122576475143433 |  | <hr />D.R. HORTON, INC. AND SUBSIDIARIES LAND AND LOT POSITION AND HOMES IN INVENTORY HOMEBUILDING SEGMENT |
| 5 | `q40d417892141:Earnings:chunk-6` | 0.7910282611846924 |  | D.R. Horton, Inc. Jessica Hansen, 817-390-8200 Senior Vice President - Communications InvestorRelations@drhorton.com<hr… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q40d417892141`)._

### ex-dev-chunk-only-q504aef305d62

- **example_id**: `dev:chunk-only:q504aef305d62`
- **state**: `completed`
- **query**: How did management describe the performance of the China market in Q4 2023?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q504aef305d62:Earnings:chunk-15` | 0.8336093425750732 | 2.0 | Thank you for the question. Let me start with the answer here. Our brand in China is known as [ Shing Baka ] and it upl… |
| 2 | `q504aef305d62:Earnings:chunk-7` | 0.8209958076477051 | 2.0 | Thank you, Laxman, and good morning, everyone. I'm very pleased to discuss our strong Q4 and full fiscal year 2023 perf… |
| 3 | `q504aef305d62:Earnings:chunk-9` | 0.7958009243011475 |  | Thank you, Rachel. At this time, we'll proceed with our normal Q&A session, which will last until the top of the hour. … |
| 4 | `q504aef305d62:Earnings:chunk-23` | 0.7953482866287231 |  | Thank you for the question. The way I'd look at the comp guidance is as we look at a very strong fiscal year 2023, and … |
| 5 | `q504aef305d62:Earnings:chunk-59` | 0.7901667952537537 |  | Brian, thank you for the question. Our CapEx will increase to around approximately $3 billion, and the majority of that… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q504aef305d62`)._

### ex-dev-chunk-only-q5bb4a350edd8

- **example_id**: `dev:chunk-only:q5bb4a350edd8`
- **state**: `completed`
- **query**: How has aircraft delivery volume trended across the last four quarters for the F 35 program?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.12001820485907799 · skipped= · n_scored=98

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5bb4a350edd8:10-Q:chunk-11` | 0.8621619343757629 |  | I was hoping to lead off with Aero and F-35 in particular, and the margins, number one, that you're looking for in '24 … |
| 2 | `q5bb4a350edd8:10-Q:chunk-85` | 0.86118084192276 | 1.0 | Yes. So we delivered 5 aircraft in 2023. We would expect that to triple, potentially quadruple, here in 2024. And so we… |
| 3 | `q5bb4a350edd8:10-Q:chunk-39` | 0.8598344922065735 |  | Jay, just a quick clarification then one for Jim and sorry if I missed this, but the deliveries that you're expecting f… |
| 4 | `q5bb4a350edd8:10-Q:chunk-65` | 0.8574755191802979 | 1.0 | Yes. Let me start with that question first, and I'll come back to the F-35. Just on the 2025 margins going forward, yes… |
| 5 | `q5bb4a350edd8:10-Q:chunk-63` | 0.855265736579895 |  | Maybe one clarification and one question. Jay, on F-35, at the end of '24, should we think about there being maybe 120 … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q5bb4a350edd8`)._

### ex-dev-chunk-only-q7b219decf5da

- **example_id**: `dev:chunk-only:q7b219decf5da`
- **state**: `completed`
- **query**: What did Everest Group, Ltd.’s leadership say about Everest Group, Ltd.’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '10-Q', '8-K']`
- **S2**: nDCG@5=0.07132875491150918 · skipped= · n_scored=138

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7b219decf5da:DEF14A:chunk-5` | 0.8317071199417114 |  | Thank you, Matt. Good morning, everyone. Thank you for joining us. 2023 was the most profitable year in our history. We… |
| 2 | `q7b219decf5da:DEF14A:chunk-7` | 0.8289621472358704 | 1.0 | Thank you, Juan, and good morning, everyone. Everest had a strong finish to 2023. For the full year, Everest delivered … |
| 3 | `q7b219decf5da:DEF14A:chunk-3` | 0.8268179893493652 |  | Good morning, everyone, and welcome to the Everest Group, Ltd. Fourth Quarter of 2023 Earnings Conference Call. The Eve… |
| 4 | `q7b219decf5da:DEF14A:chunk-83` | 0.8146482706069946 |  | Sure. Greg, this is Jim Williamson. Thanks for the question. Everest did have another excellent Jan 1 renewals. You've … |
| 5 | `q7b219decf5da:DEF14A:chunk-113` | 0.8145387768745422 |  | So back to the reserving discussion. You said, I think, Juan, you might have said that you're making much higher loss -… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q7b219decf5da`)._

### ex-dev-chunk-only-q7ca4de540868

- **example_id**: `dev:chunk-only:q7ca4de540868`
- **state**: `completed`
- **query**: How does Hologic view the pace of innovation cycles in women's health diagnostics and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.24090885754831726 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ca4de540868:10-K:chunk-7` | 0.8471774458885193 | 1.0 | # Performance Highlights <figure description={The image shows a horizontal color gradient bar transitioning from light … |
| 2 | `q7ca4de540868:10-K:chunk-67` | 0.8391610383987427 | 1.0 | # Compensation Discussion and Analysis (cont.) ## 2023 Business Strategy & Performance Highlights (cont.) Finally, our … |
| 3 | `q7ca4de540868:10-K:chunk-8` | 0.8356725573539734 | 1.0 | # Performance Highlights (cont.) 15.6% WORLDWIDE ORGANIC REVENUE GROWTH EX. COVID-19 15.6% organic growth in constant c… |
| 4 | `q7ca4de540868:10-K:chunk-9` | 0.832693874835968 |  | # Performance Highlights (cont.) ## Financial highlights from fiscal 2023 - We drove top-line growth through a combinat… |
| 5 | `q7ca4de540868:10-K:chunk-3` | 0.8288006782531738 |  | # Dear Fellow Stockholders: (cont.) Moving first to the Hologic Global Women's Health Index, a partnership with Gallup,… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q7ca4de540868`)._

### ex-dev-chunk-only-q7ff47a7d2a20

- **example_id**: `dev:chunk-only:q7ff47a7d2a20`
- **state**: `completed`
- **query**: How does Consolidated Edison, Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.1843821566693812 · skipped= · n_scored=212

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ff47a7d2a20:10-K:chunk-185` | 0.8407167196273804 | 1.0 | # APPENDIX D (cont.) ## PREAMBLE The Stock Purchase Plan ("Plan") provides a means for employees of Consolidated Edison… |
| 2 | `q7ff47a7d2a20:10-K:chunk-105` | 0.8270483016967773 | 1.0 | # Long-Term Incentive Compensation (cont.) ## 2023 LTIP Awards (cont.) The share price for the performance-based awards… |
| 3 | `q7ff47a7d2a20:10-K:chunk-123` | 0.8256978988647461 |  | # SUMMARY COMPENSATION TABLE (cont.) ## Footnotes: (1) For 2022 and 2023, the stock awards included both time-based and… |
| 4 | `q7ff47a7d2a20:10-K:chunk-128` | 0.8248106837272644 |  | # GRANTS OF PLAN-BASED AWARDS TABLE (cont.) ## Footnotes: (1) (2) Represents the annual cash incentive award opportunit… |
| 5 | `q7ff47a7d2a20:10-K:chunk-70` | 0.821829080581665 |  | # STOCK OWNERSHIP (cont.) ## Footnotes: (1) The number of shares shown includes shares of Company Common Stock that are… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q7ff47a7d2a20`)._

### ex-dev-chunk-only-q853c16a74704

- **example_id**: `dev:chunk-only:q853c16a74704`
- **state**: `completed`
- **query**: What did Tapestry’s management say about Tapestry’s margin outlook and initiatives to improve profitability?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.17989452745991058 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q853c16a74704:Earnings:chunk-3` | 0.8540238738059998 |  | Good morning. Thank you for joining us. With me today to discuss our fourth quarter and year-end results as well as our… |
| 2 | `q853c16a74704:Earnings:chunk-11` | 0.8403043746948242 |  | And congratulations on the strong year at Tapestry. When you look at your results in comparison to Capris recently, giv… |
| 3 | `q853c16a74704:Earnings:chunk-23` | 0.8366750478744507 |  | Well, maybe I'll kick it off, Ike, and then pass it to Scott again. We do have both strategic and financial strength an… |
| 4 | `q853c16a74704:Earnings:chunk-71` | 0.8335577249526978 | 1.0 | Yes. We -- I appreciate the question. We evaluate our investment with any capital allocation decision we make with a lo… |
| 5 | `q853c16a74704:Earnings:chunk-77` | 0.8200880885124207 | 2.0 | Yes. Let me hit the last part of that real quick because it is a quick one, right? So remember, we had some timing betw… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q853c16a74704`)._

### ex-dev-chunk-only-q90faabe2b483

- **example_id**: `dev:chunk-only:q90faabe2b483`
- **state**: `completed`
- **query**: What operational risks related to technology or IT systems has UDR, Inc. highlighted, and how are these managed?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=31

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q90faabe2b483:10-K:chunk-2` | 0.8085728883743286 |  | # UDR AT A GLANCE (1)(2) UDR is a full-cycle investment that consistently generates strong total shareholder return ("T… |
| 2 | `q90faabe2b483:10-K:chunk-4` | 0.7861496806144714 |  | # INNOVATION ACCOMPLISHMENTS (cont.) ## Long-Term Same-Store Outperformance Controllable Operating Margin ("COM") Expan… |
| 3 | `q90faabe2b483:10-K:chunk-9` | 0.781538724899292 |  | # RECENT EXTERNAL GROWTH ACTIVITY (cont.) ## Texas Acquisitions (cont.) Investment Thesis Ability to increase operating… |
| 4 | `q90faabe2b483:10-K:chunk-0` | 0.7811890840530396 |  | # Exhibit 99.1 Vision on Wilshire I Los Angeles, CA INVESTOR PRESENTATION UDR® November 2023 Opening GRESB KUAL sector … |
| 5 | `q90faabe2b483:10-K:chunk-22` | 0.7803208827972412 |  | # DEFINITIONS AND RECONCILIATIONS (cont.) Net Operating Income ("NOI"): The Company defines NOI as rental income less d… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q90faabe2b483`)._

### ex-dev-chunk-only-q9ee9b517f484

- **example_id**: `dev:chunk-only:q9ee9b517f484`
- **state**: `completed`
- **query**: What feedback have investors provided regarding Valero Energy Corporation’s refining margin outlook?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.21398626473452756 · skipped= · n_scored=203

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9ee9b517f484:Earnings:chunk-104` | 0.8429225087165833 |  | OVERVIEW AND OUTLOOK Overview Business Operations Update Our results for the third quarter and first nine months of 202… |
| 2 | `q9ee9b517f484:Earnings:chunk-19` | 0.8366817235946655 | 1.0 | VALERO ENERGY CORPORATION CONDENSED NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Continued) California Energy Commission… |
| 3 | `q9ee9b517f484:Earnings:chunk-107` | 0.8349170088768005 |  | While our operating income decreased by $289 million in the third quarter of 2023 compared to the third quarter of 2022… |
| 4 | `q9ee9b517f484:Earnings:chunk-186` | 0.8286980390548706 |  | We have developed an extensive multi-year capital investment program, which we update and revise based on changing inte… |
| 5 | `q9ee9b517f484:Earnings:chunk-130` | 0.8262899518013 |  | The decrease in Refining segment margin was primarily due to the following: ◦A decrease in distillate (primarily diesel… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q9ee9b517f484`)._

### ex-dev-chunk-only-qa431f3f55a5e

- **example_id**: `dev:chunk-only:qa431f3f55a5e`
- **state**: `completed`
- **query**: How are scenario analyses conducted by EPAM Systems, Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.13120507751234178 · skipped= · n_scored=252

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa431f3f55a5e:10-K:chunk-114` | 0.8290805816650391 |  | Table of Contents EPAM SYSTEMS, INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (In thousands, except … |
| 2 | `qa431f3f55a5e:10-K:chunk-35` | 0.8115406036376953 |  | Table of Contents Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations You sho… |
| 3 | `qa431f3f55a5e:10-K:chunk-0` | 0.8110541105270386 |  | PART I Item 1. Business Overview EPAM has used its software engineering expertise to become a leading global provider o… |
| 4 | `qa431f3f55a5e:10-K:chunk-29` | 0.8029376268386841 |  | Company/Index####Base period 12/31/2018####12/31/2019####12/31/2020####12/31/2021####12/31/2022####12/31/2023 EPAM Syst… |
| 5 | `qa431f3f55a5e:10-K:chunk-38` | 0.8028576970100403 | 1.0 | Table of Contents We determine the fair value of contingent consideration using Monte Carlo simulations (which involve … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qa431f3f55a5e`)._

### ex-dev-chunk-only-qaf2d41946676

- **example_id**: `dev:chunk-only:qaf2d41946676`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Occidental Petroleum Corporation for oil price volatility risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.16958010263680806 · skipped= · n_scored=126

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qaf2d41946676:10-K:chunk-3` | 0.8228274583816528 |  | Thank you, Gary. Good afternoon, everyone, and thank you for participating in Occidental's Fourth Quarter 2023 earnings… |
| 2 | `qaf2d41946676:10-K:chunk-115` | 0.8078451752662659 |  | And in terms of drillships, we're only planning on 2 drillships this year. In terms of GoM overall, [indiscernible] pla… |
| 3 | `qaf2d41946676:10-K:chunk-87` | 0.7990388870239258 | 1.0 | Yes. So when we think about capital allocation in the oil and gas segment, what you're trying to do is we're trying to … |
| 4 | `qaf2d41946676:10-K:chunk-61` | 0.7970513105392456 |  | I would tell you that, over the next 5 to 10 years, it's going to be a significant part of our portfolio development. W… |
| 5 | `qaf2d41946676:10-K:chunk-7` | 0.7958411574363708 |  | Thank you, Vicki. I will begin today by reviewing our fourth quarter results. We announced an adjusted profit of $0.74 … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qaf2d41946676`)._

### ex-dev-chunk-only-qb3a6bec7aedc

- **example_id**: `dev:chunk-only:qb3a6bec7aedc`
- **state**: `completed`
- **query**: What exposure to foreign exchange fluctuations did Citizens Financial Group, Inc. disclose and how is Citizens Financial Group, Inc. managing it?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.04373502583744726 · skipped= · n_scored=423

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb3a6bec7aedc:10-K:chunk-38` | 0.8420554399490356 |  | INTRODUCTION Citizens Financial Group, Inc. is one of the nation’s oldest and largest financial institutions, with $222… |
| 2 | `qb3a6bec7aedc:10-K:chunk-252` | 0.8358709216117859 |  | (1) Includes $187 million of loans fully or partially government guaranteed by the FHA, VA, and USDA. Concentrations of… |
| 3 | `qb3a6bec7aedc:10-K:chunk-137` | 0.8330973386764526 |  | ITEM 7A. QUANTITATIVE AND QUALITATIVE DISCLOSURES ABOUT MARKET RISK Quantitative and qualitative disclosures about mark… |
| 4 | `qb3a6bec7aedc:10-K:chunk-116` | 0.8306964635848999 |  | We continue to manage asset sensitivity within the scope of our policy, changing market conditions and changes in our b… |
| 5 | `qb3a6bec7aedc:10-K:chunk-0` | 0.8305058479309082 | 1.0 | PART I ITEM 1. BUSINESS Citizens Financial Group, Inc. is headquartered in Providence, Rhode Island. We offer a broad r… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qb3a6bec7aedc`)._

### ex-dev-chunk-only-qb7d1dfae8271

- **example_id**: `dev:chunk-only:qb7d1dfae8271`
- **state**: `completed`
- **query**: What guidance was offered on International Flavors & Fragrances Inc.’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.48522855511632257 · skipped= · n_scored=304

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb7d1dfae8271:10-Q:chunk-22` | 0.8300168514251709 | 1.0 | Our performance may be adversely impacted if we are not successful in managing our inventory and/or working capital bal… |
| 2 | `qb7d1dfae8271:10-Q:chunk-64` | 0.8280397057533264 |  | REPORT OF INDEPENDENT REGISTERED PUBLIC ACCOUNTING FIRM To the Board of Directors and Shareholders of International Fla… |
| 3 | `qb7d1dfae8271:10-Q:chunk-78` | 0.822162389755249 |  | INTERNATIONAL FLAVORS & FRAGRANCES INC. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS NOTE 1. NATURE OF OPERATIONS AND SUM… |
| 4 | `qb7d1dfae8271:10-Q:chunk-4` | 0.8139480352401733 | 1.0 | •evaluating the profitability of whether to buy or make an ingredient; •sourcing from local countries with our own proc… |
| 5 | `qb7d1dfae8271:10-Q:chunk-13` | 0.810164749622345 |  | If we are unable to successfully execute the next phase of our strategic transformation, including our portfolio optimi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qb7d1dfae8271`)._

### ex-dev-chunk-only-qbcda53de470c

- **example_id**: `dev:chunk-only:qbcda53de470c`
- **state**: `completed`
- **query**: Which competitive advantages has Apple emphasized compared to peers?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbcda53de470c:DEF14A:chunk-107` | 0.8080469369888306 |  | Sure. It's a number of things, Richard. It's the -- some things I can't talk about. It's Vision Pro. It's AI and ML. It… |
| 2 | `qbcda53de470c:DEF14A:chunk-111` | 0.8009529709815979 |  | That's great. And Luca, you mentioned, or Tim mentioned college students choosing Macs and you mentioned the record Ser… |
| 3 | `qbcda53de470c:DEF14A:chunk-57` | 0.7964785099029541 |  | We had a really strong quarter across the border, I mean, because both geographically and from a product category stand… |
| 4 | `qbcda53de470c:DEF14A:chunk-79` | 0.7920396327972412 |  | Okay. And as a follow-up, you obviously had a great Services quarter. And part of your Services business has these lice… |
| 5 | `qbcda53de470c:DEF14A:chunk-69` | 0.7894736528396606 |  | Very clear. And for my follow-up, I had a philosophical question. So you guys always try to provide the best experience… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qbcda53de470c`)._

### ex-dev-chunk-only-qd7ede96b88aa

- **example_id**: `dev:chunk-only:qd7ede96b88aa`
- **state**: `completed`
- **query**: What observations were made about TransDigm Group’s market share trends or competitive positioning in the aerospace components sector?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.37572911643996837 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd7ede96b88aa:Earnings:chunk-8` | 0.832403302192688 | 1.0 | # 2025 Annual Meeting of Shareholders (cont.) ## Composition of our Board (cont.) 31 Years of Growth and Improving Marg… |
| 2 | `qd7ede96b88aa:Earnings:chunk-59` | 0.8224360942840576 | 2.0 | # Summary of Key NEO Compensation Decisions and Actions in 2024 (cont.) ## 2024 Peer Group Ametek, Inc. Aptiv PLC* Dove… |
| 3 | `qd7ede96b88aa:Earnings:chunk-43` | 0.8174214959144592 |  | # Kevin M. Stein Age 58 Director Since 2018 Committees None Kevin M. Stein has been Chief Executive Officer of TransDig… |
| 4 | `qd7ede96b88aa:Earnings:chunk-51` | 0.8155050277709961 | 1.0 | # Compensation Discussion and Analysis ("CD&A") (cont.) ## Introduction Our compensation program closely aligns NEO com… |
| 5 | `qd7ede96b88aa:Earnings:chunk-2` | 0.8110880255699158 |  | # Message from the Lead Independent Director Dear Fellow Shareholders, It has been a little over a year since I was sel… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qd7ede96b88aa`)._

### ex-dev-chunk-only-qddfea8300793

- **example_id**: `dev:chunk-only:qddfea8300793`
- **state**: `completed`
- **query**: How does Chesapeake Energy view the pace of technological advancements in drilling techniques and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.16958010263680806 · skipped= · n_scored=345

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qddfea8300793:10-K:chunk-33` | 0.826839804649353 |  | •any investment, acquisition, or disposition will not divert management resources from the operation of our business; a… |
| 2 | `qddfea8300793:10-K:chunk-313` | 0.8240963220596313 |  | CHESAPEAKE ENERGY CORPORATION AND SUBSIDIARIES SUPPLEMENTARY INFORMATION - (Continued) testing by a pilot project in an… |
| 3 | `qddfea8300793:10-K:chunk-36` | 0.8206841349601746 | 1.0 | Our development and exploratory drilling efforts and our well operations may not be profitable or achieve our targeted … |
| 4 | `qddfea8300793:10-K:chunk-301` | 0.8095086812973022 |  | 18. Investments Momentum Sustainable Ventures LLC. During the fourth quarter of 2022, Chesapeake entered into an agreem… |
| 5 | `qddfea8300793:10-K:chunk-166` | 0.8079400658607483 |  | CHESAPEAKE ENERGY CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – (Continued) suspended explo… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qddfea8300793`)._

### ex-dev-chunk-only-qed0361d5a9ae

- **example_id**: `dev:chunk-only:qed0361d5a9ae`
- **state**: `completed`
- **query**: How does Apple currently project its growth rate based on the latest management commentary?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=83

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qed0361d5a9ae:Earnings:chunk-56` | 0.8223398923873901 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations This section and other pa… |
| 2 | `qed0361d5a9ae:Earnings:chunk-71` | 0.8057137727737427 |  | The Company’s effective tax rate for the third quarter and first nine months of 2023 was lower than the statutory feder… |
| 3 | `qed0361d5a9ae:Earnings:chunk-11` | 0.8042103052139282 |  | See accompanying Notes to Condensed Consolidated Financial Statements. Apple Inc. \| Q3 2023 Form 10-Q \| 4 |
| 4 | `qed0361d5a9ae:Earnings:chunk-40` | 0.8037512302398682 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 10 |
| 5 | `qed0361d5a9ae:Earnings:chunk-14` | 0.8035897612571716 |  | See accompanying Notes to Condensed Consolidated Financial Statements. Apple Inc. \| Q3 2023 Form 10-Q \| 5 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qed0361d5a9ae`)._

### ex-dev-chunk-only-qeeb1c1a41ae3

- **example_id**: `dev:chunk-only:qeeb1c1a41ae3`
- **state**: `completed`
- **query**: What dependency risks exist for DuPont de Nemours, Inc. due to concentration of revenue in a limited number of end-use industries such as automotive or electronics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.2591217516005785 · skipped= · n_scored=112

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeeb1c1a41ae3:10-K:chunk-4` | 0.7887651920318604 | 1.0 | # Proxy Statement Summary # About DuPont We are a global innovation leader with technology-based materials and solution… |
| 2 | `qeeb1c1a41ae3:10-K:chunk-109` | 0.7833892107009888 |  | # Reconciliation of "Cash provided by operating activities - continuing operations" to "Segment Adjusted Free Cash Flow… |
| 3 | `qeeb1c1a41ae3:10-K:chunk-99` | 0.777983546257019 |  | # Appendix A # NON-GAAP RECONCILIATION ## Non-GAAP Financial Measures The tables below include information that does no… |
| 4 | `qeeb1c1a41ae3:10-K:chunk-43` | 0.7745680809020996 | 2.0 | # Compensation Discussion & Analysis ## Executive Summary We experienced significant volume pressure throughout 2023 as… |
| 5 | `qeeb1c1a41ae3:10-K:chunk-86` | 0.7710212469100952 |  | # Agenda Item 2: Advisory Resolution to Approve Executive Compensation As required by Section 14A of the Exchange Act, … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qeeb1c1a41ae3`)._

### ex-dev-chunk-only-qf3b87e3d287f

- **example_id**: `dev:chunk-only:qf3b87e3d287f`
- **state**: `completed`
- **query**: How has Bio-Techne Corporation’s leverage (e.g., debt-to-equity) changed over time?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf3b87e3d287f:10-K:chunk-0` | 0.8466249108314514 |  | Exhibit 99.1 BIO-TECHNE RELEASES THIRD QUARTER FISCAL 2024 RESULTS Minneapolis/May 1, 2024/ Bio-Techne Corporation (NAS… |
| 2 | `qf3b87e3d287f:10-K:chunk-23` | 0.8306107521057129 |  | 1) Net earnings attributable to Bio-Techne excludes non-controlling interest of approximately 43% of the GAAP net earni… |
| 3 | `qf3b87e3d287f:10-K:chunk-5` | 0.829257607460022 |  | Investors are cautioned not to place undue emphasis on these statements. Bio-Techne Corporation (NASDAQ: TECH) is a glo… |
| 4 | `qf3b87e3d287f:10-K:chunk-1` | 0.819202721118927 |  | Bio-Techne will host an earnings conference call today, May 1, 2024 at 8:00 a.m. CDT. To listen, please dial 1-877-407-… |
| 5 | `qf3b87e3d287f:10-K:chunk-13` | 0.8160317540168762 |  | 1) Includes the quarterly results of the partially-owned consolidated subsidiary prior to the sale of this partially-ow… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qf3b87e3d287f`)._

### ex-dev-chunk-only-qf59bea60dc8d

- **example_id**: `dev:chunk-only:qf59bea60dc8d`
- **state**: `completed`
- **query**: How does Aon manage equity award burn rate or share pool availability?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-Q', '10-K', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=145

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf59bea60dc8d:DEF14A:chunk-88` | 0.8381485939025879 |  | •Adjusted diluted earnings per share, a non-GAAP measure defined under the caption “Review of Consolidated Results — Ad… |
| 2 | `qf59bea60dc8d:DEF14A:chunk-100` | 0.8357958793640137 |  | (1)In the third quarter of 2023, Aon initiated the Accelerating Aon United Program. Total charges are expected to inclu… |
| 3 | `qf59bea60dc8d:DEF14A:chunk-138` | 0.8249580264091492 |  | (1)Does not include commissions paid to repurchase shares. (2)The Repurchase Program was established in April 2012 with… |
| 4 | `qf59bea60dc8d:DEF14A:chunk-136` | 0.820865273475647 |  | Part II Other Information Item 1. Legal Proceedings See Note 15 “Claims, Lawsuits, and Other Contingencies” to our Fina… |
| 5 | `qf59bea60dc8d:DEF14A:chunk-143` | 0.8205792307853699 |  | Exhibit Number####Description of Exhibit 3.1####Memorandum and Articles of Association of Aon plc (Incorporated by refe… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qf59bea60dc8d`)._

### ex-dev-q00e75b32eb34

- **example_id**: `dev:q00e75b32eb34`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has International Flavors & Fragrances Inc.’s ingredients segment profitability trended over recent periods?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q00e75b32eb34`)._

### ex-dev-q01b84969979c

- **example_id**: `dev:q01b84969979c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How many markets were mentioned as now offering ad tier pricing for Disney Plus
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.7063662475919823 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['8-K', 'Earnings', '10-Q', 'DEF14A', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q01b84969979c`)._

### ex-dev-q0346b2bc5a8b

- **example_id**: `dev:q0346b2bc5a8b`
- **state**: `completed`
- **query**: What investor views emerged on Packaging Corporation of America’s geographic expansion prospects within the packaging industry?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9216809842642141 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.3065735963827292 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0346b2bc5a8b:chunk-1` | 0.7999648451805115 |  | Thank you for joining Packaging Corporation of America's Fourth Quarter and Full Year 2023 Earnings Results Conference … |
| 2 | `q0346b2bc5a8b:chunk-3` | 0.7983527183532715 |  | Thank you, Jamie. Good morning, everyone, and thank you all for participating in Packaging Corporation of America's Fou… |
| 3 | `q0346b2bc5a8b:chunk-51` | 0.7969163656234741 | 1.0 | Yes, Mike, obviously, you don't know what the future is going to hold, but we've got a lot of optionality in what we're… |
| 4 | `q0346b2bc5a8b:chunk-11` | 0.7814662456512451 |  | Thank you, Bob. I'm very proud of the outstanding results PCA delivered in 2023 under very challenging demand condition… |
| 5 | `q0346b2bc5a8b:chunk-5` | 0.7775911092758179 |  | Thank you, Mark. As Mark mentioned, Packaging segment volume for the quarter exceeded our guidance estimates. Corrugate… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q0346b2bc5a8b`)._

### ex-dev-q03a704904653

- **example_id**: `dev:q03a704904653`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did IBM’s leadership say about IBM’s dividend policy or share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.5831428296492145 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['DEF14A', 'Earnings', '8-K', '10-K', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q03a704904653`)._

### ex-dev-q044bb2c8810c

- **example_id**: `dev:q044bb2c8810c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on EQT Corporation’s geographic expansion prospects within the U.S. natural gas markets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6252347221754821 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q044bb2c8810c`)._

### ex-dev-q05bfc5cb3e17

- **example_id**: `dev:q05bfc5cb3e17`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Northern Trust Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3869772073910237 · skipped= · n_scored=315

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q05bfc5cb3e17:chunk-97` | 0.8470355272293091 | 1.0 | The MVE simulations do not incorporate certain management actions that may be used to mitigate adverse effects of actua… |
| 2 | `q05bfc5cb3e17:chunk-94` | 0.8466019034385681 | 1.0 | The NII sensitivity analysis does not incorporate certain management actions that may be used to mitigate adverse effec… |
| 3 | `q05bfc5cb3e17:chunk-92` | 0.8396099805831909 | 1.0 | RISK MANAGEMENT (continued) Market Risk (continued) The NII sensitivity analysis incorporates certain critical assumpti… |
| 4 | `q05bfc5cb3e17:chunk-204` | 0.8345008492469788 | 2.0 | Allowance Related to Credit Exposure Evaluated on a Collective Basis. Expected credit losses are measured on a collecti… |
| 5 | `q05bfc5cb3e17:chunk-104` | 0.8281564116477966 |  | FORWARD-LOOKING STATEMENTS (continued) •Northern Trust’s success in maintaining existing business and continuing to gen… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q05bfc5cb3e17`)._

### ex-dev-q09b8cfa51b60

- **example_id**: `dev:q09b8cfa51b60`
- **state**: `completed`
- **query**: How does CBRE Group, Inc. view the pace of technological innovation in real estate services and its effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=141

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q09b8cfa51b60:chunk-125` | 0.8248977065086365 |  | •the ability of our investment management business to maintain and grow assets under management and achieve desired inv… |
| 2 | `q09b8cfa51b60:chunk-78` | 0.7910876274108887 |  | Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations Management’s Discussion a… |
| 3 | `q09b8cfa51b60:chunk-23` | 0.7808994054794312 |  | CBRE GROUP, INC. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Unaudited) 1. Basis of Presentation Readers of this Quarte… |
| 4 | `q09b8cfa51b60:chunk-73` | 0.7794036865234375 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |
| 5 | `q09b8cfa51b60:chunk-80` | 0.7773052453994751 |  | Compensation is our largest expense and our capital markets and leasing professionals generally are paid on a commissio… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q09b8cfa51b60`)._

### ex-dev-q0b8d55d58be2

- **example_id**: `dev:q0b8d55d58be2`
- **state**: `completed`
- **query**: What questions were asked about Chubb Limited’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9506817003345661 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=370

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0b8d55d58be2:chunk-229` | 0.8359917402267456 |  | ITEM 2. Management's Discussion and Analysis of Financial Condition and Results of Operations The following is a discus… |
| 2 | `q0b8d55d58be2:chunk-362` | 0.8319572806358337 |  | (1)This column represents open market share repurchases and the surrender to Chubb of Common Shares to satisfy tax with… |
| 3 | `q0b8d55d58be2:chunk-194` | 0.8294742107391357 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – continued (Unaudited) Chubb Limited and Subsidiaries repurchased, 14,925,0… |
| 4 | `q0b8d55d58be2:chunk-127` | 0.8292386531829834 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – continued (Unaudited) Chubb Limited and Subsidiaries Net favorable develop… |
| 5 | `q0b8d55d58be2:chunk-225` | 0.8264341354370117 |  | Underwriting assets are reviewed in total by management for purposes of decision-making. Other than Unpaid losses and l… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q0b8d55d58be2`)._

### ex-dev-q0d51e9ef12aa

- **example_id**: `dev:q0d51e9ef12aa`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did leadership measure the installed base of RTX PCs and relate it to AI‑application adoption?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5509858876386381 · gold=['8-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q0d51e9ef12aa`)._

### ex-dev-q0e5327ae1aff

- **example_id**: `dev:q0e5327ae1aff`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What concerns have institutional investors raised regarding regulatory risk?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5=0.6309297535714575 · gold=['Earnings']
- **S1 ordered**: `['DEF14A', 'Earnings', '8-K', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q0e5327ae1aff`)._

### ex-dev-q0faf9d780cdc

- **example_id**: `dev:q0faf9d780cdc`
- **state**: `completed`
- **query**: How did aeronautics sustainment hours compare with prior year levels?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9639404333166532 · gold=['10-Q', '10-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.639909328045346 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0faf9d780cdc:chunk-54` | 0.8016284704208374 |  | Aeronautics’ net sales in 2023 increased $487 million, or 2%, compared to 2022. Net sales increased by approximately $5… |
| 2 | `q0faf9d780cdc:chunk-43` | 0.8015393018722534 | 2.0 | (a)Effective January 1, 2023, we reclassified intangible asset amortization expense out of the business segment operati… |
| 3 | `q0faf9d780cdc:chunk-55` | 0.7977313995361328 |  | production. These increases were partially offset by lower net sales of $400 million on the F-35 program due to lower v… |
| 4 | `q0faf9d780cdc:chunk-40` | 0.7933147549629211 | 1.0 | Substantially all of our contracts are accounted for using the percentage-of-completion cost-to-cost method. Under the … |
| 5 | `q0faf9d780cdc:chunk-105` | 0.7922018766403198 |  | program, at this time we do not anticipate that additional losses, if any, would be material to our financial results o… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q0faf9d780cdc`)._

### ex-dev-q11ef281af9cd

- **example_id**: `dev:q11ef281af9cd`
- **state**: `completed`
- **query**: How does United Rentals select the peer group for benchmarking executive pay?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9840990003623115 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=223

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q11ef281af9cd:chunk-197` | 0.8071663975715637 |  | Report of Independent Registered Public Accounting Firm To the Stockholders and the Board of Directors of United Rental… |
| 2 | `q11ef281af9cd:chunk-209` | 0.7958706617355347 |  | Exhibit Number####Description of Exhibit 10##(jj)##Employment Agreement, effective as of January 20, 2016 between Unite… |
| 3 | `q11ef281af9cd:chunk-9` | 0.7957794666290283 |  | we negotiate are competitive and that there is sufficient product available to meet anticipated customer demand. We uti… |
| 4 | `q11ef281af9cd:chunk-205` | 0.7947455048561096 |  | Exhibit Number####Description of Exhibit 10##(c)##United Rentals, Inc. Deferred Compensation Plan, as amended and resta… |
| 5 | `q11ef281af9cd:chunk-17` | 0.7925503849983215 |  | One of the reasons some of our customers find it more attractive to rent equipment than own that equipment is the need … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q11ef281af9cd`)._

### ex-dev-q140516364bb4

- **example_id**: `dev:q140516364bb4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Principal Financial Group’s international expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q140516364bb4`)._

### ex-dev-q1463bdfd6910

- **example_id**: `dev:q1463bdfd6910`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Equifax’s Workforce Solutions segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1463bdfd6910`)._

### ex-dev-q1ab49a3f086f

- **example_id**: `dev:q1ab49a3f086f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What outlook was given for Welltower Inc.’s free cash flow generation over the next year?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7426242736819336 · gold=['8-K', 'Earnings', '10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1ab49a3f086f`)._

### ex-dev-q1cfcd01ac3a1

- **example_id**: `dev:q1cfcd01ac3a1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does GE HealthCare Technologies manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7860353577841278 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1cfcd01ac3a1`)._

### ex-dev-q1ded233d05aa

- **example_id**: `dev:q1ded233d05aa`
- **state**: `completed`
- **query**: What questions were asked about IDEXX Laboratories’ customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.06934506308715421 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1ded233d05aa:chunk-57` | 0.8463209867477417 |  | So we don't have further questions. So with that, thank you for your questions. We'll now conclude our Q&A portion of t… |
| 2 | `q1ded233d05aa:chunk-5` | 0.8321052193641663 |  | Thank you, Brian, and good morning. IDEXX delivered strong performance in the fourth quarter, capping a year where we a… |
| 3 | `q1ded233d05aa:chunk-27` | 0.8320742845535278 | 1.0 | Yes. Just some follow-up commentary on the inVue launch. Customers, I think, very excited to learn more about that, as … |
| 4 | `q1ded233d05aa:chunk-1` | 0.828633189201355 |  | Good morning, and welcome to the IDEXX Laboratories Fourth Quarter 2023 Earnings Conference Call. As a reminder, today'… |
| 5 | `q1ded233d05aa:chunk-3` | 0.8221158981323242 |  | Good morning, everyone. I'm pleased to take you through our fourth quarter and full year 2023 results and to provide an… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1ded233d05aa`)._

### ex-dev-q1f722f19a821

- **example_id**: `dev:q1f722f19a821`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What answers were given about progress on Clover Vertica installations?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5=0.6309297535714575 · gold=['Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1f722f19a821`)._

### ex-dev-q1ff3eed25e64

- **example_id**: `dev:q1ff3eed25e64`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did wage inflation trends affect labor costs in park operations
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6321922161264945 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q1ff3eed25e64`)._

### ex-dev-q2173e7c263c1

- **example_id**: `dev:q2173e7c263c1`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Realty Income Corporation for recessionary or downturn risks in the commercial real estate sector?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=171

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2173e7c263c1:chunk-90` | 0.8305173516273499 |  | Item 2: Management’s Discussion and Analysis of Financial Condition and Results of Operations FORWARD-LOOKING STATEMENT… |
| 2 | `q2173e7c263c1:chunk-137` | 0.8221755623817444 |  | We consider FFO and Normalized FFO to be appropriate supplemental measures of a REIT’s operating performance as they ar… |
| 3 | `q2173e7c263c1:chunk-64` | 0.810692310333252 |  | Although we have determined that the majority of the inputs used to value our derivatives fall within level two on the … |
| 4 | `q2173e7c263c1:chunk-66` | 0.8024571537971497 |  | The valuation of impaired assets is determined using valuation techniques including discounted cash flow analysis, anal… |
| 5 | `q2173e7c263c1:chunk-109` | 0.7976635694503784 |  | (1) The initial term of the credit facility expires in June 2026 and includes, at our option, two six-month extensions.… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2173e7c263c1`)._

### ex-dev-q238a8429d152

- **example_id**: `dev:q238a8429d152`
- **state**: `completed`
- **query**: How does Dominion Energy view the pace of innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.48354229129334175 · skipped= · n_scored=209

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q238a8429d152:chunk-6` | 0.8166437745094299 |  | # BUSINESS REVIEW PROCESS (cont.) ## November Dominion Energy initiates a business review to explore value-maximizing s… |
| 2 | `q238a8429d152:chunk-46` | 0.8144629001617432 | 2.0 | # Sustainability and Corporate Responsibility Committee (cont.) ## Oversight of Strategy (cont.) As part of its ongoing… |
| 3 | `q238a8429d152:chunk-4` | 0.8143504858016968 | 1.0 | # Dominion Energy R Dominion Energy, headquartered in Richmond, Virginia, is one of the nation's largest producers and … |
| 4 | `q238a8429d152:chunk-160` | 0.812383234500885 |  | # Your Board of Directors recommends that you vote AGAINST this item. (cont.) ## Your Board of Directors recommends tha… |
| 5 | `q238a8429d152:chunk-5` | 0.8123825788497925 |  | # Dominion Energy R (cont.) ## 2023 Performance Highlights 0.45 OSHA recordable injury rate, our second-best ever 15 da… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q238a8429d152`)._

### ex-dev-q2451f8377cf4

- **example_id**: `dev:q2451f8377cf4`
- **state**: `completed`
- **query**: What dependency risks exist for Pool Corporation due to concentration of revenue in specific geographic regions or major pool supply distributors?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.325027967813913 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2451f8377cf4:chunk-89` | 0.8022325038909912 |  | Sure. Now just keep in mind that that's the smallest part of our business. So the beginning of the year is always show … |
| 2 | `q2451f8377cf4:chunk-5` | 0.7959707975387573 | 2.0 | Thank you, Melanie, and good morning to everyone on the call. For the full year 2023, we generated over $5.5 billion in… |
| 3 | `q2451f8377cf4:chunk-77` | 0.7945959568023682 |  | Right. And if you think about the returns that you're anticipating on these investments, if you get back into an enviro… |
| 4 | `q2451f8377cf4:chunk-29` | 0.7941735982894897 |  | Okay. That's very helpful color. And then I wanted to dig a little deeper into the semi discretionary products and the … |
| 5 | `q2451f8377cf4:chunk-95` | 0.7884830236434937 |  | So let me try and answer the first part, I think I got it right. If not, come back, and tell me I didn't answer your qu… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2451f8377cf4`)._

### ex-dev-q24d0f908cfe3

- **example_id**: `dev:q24d0f908cfe3`
- **state**: `completed`
- **query**: What guidance was offered on Fox Corporation’s advertising revenue growth targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9278143341459562 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.5012658353418871 · skipped= · n_scored=111

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q24d0f908cfe3:chunk-52` | 0.8119204640388489 |  | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Fiscal 2023 Business and Management Review FOX once again delivered s… |
| 2 | `q24d0f908cfe3:chunk-53` | 0.810138463973999 |  | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Fiscal 2023 Business and Management Review (cont.) - FOX Entertainmen… |
| 3 | `q24d0f908cfe3:chunk-5` | 0.8095769286155701 |  | # Board Nominees (cont.) ## Fiscal 2023 Business Highlights FOX once again delivered strong operational and financial r… |
| 4 | `q24d0f908cfe3:chunk-54` | 0.8075695037841797 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Fiscal 2023 Business and Management Review (cont.) offerings to suppl… |
| 5 | `q24d0f908cfe3:chunk-62` | 0.8047744035720825 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS <table><tr><th>Qualitative Performance Factor</th><th>Fiscal 2023 Achievements</… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q24d0f908cfe3`)._

### ex-dev-q25119b32a2f9

- **example_id**: `dev:q25119b32a2f9`
- **state**: `completed`
- **query**: What performance metrics does Snap-on Incorporated use to establish annual cash incentives or bonuses?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9882048111454694 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=21

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q25119b32a2f9:chunk-3` | 0.8577236533164978 | 1.0 | References in this release to “organic sales” refer to sales from continuing operations calculated in accordance with g… |
| 2 | `q25119b32a2f9:chunk-14` | 0.8288992643356323 |  | <hr />Non-GAAP Supplemental Data The following non-GAAP supplemental data is presented for informational purposes to pr… |
| 3 | `q25119b32a2f9:chunk-0` | 0.8260608911514282 |  | Exhibit 99 Snap-on Announces Third Quarter 2023 Results Sales of $1,159.3 million up 5.2% from Q3 2022, organic sales u… |
| 4 | `q25119b32a2f9:chunk-4` | 0.8237765431404114 |  | Factors that may cause the company’s actual results to differ materially from those contained in the forward-looking st… |
| 5 | `q25119b32a2f9:chunk-2` | 0.8210105299949646 |  | Operating earnings of $104.9 million in the period, including $0.2 million of favorable foreign currency effects, compa… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q25119b32a2f9`)._

### ex-dev-q27a01443f529

- **example_id**: `dev:q27a01443f529`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Fox Corporation’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6289921088377346 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q27a01443f529`)._

### ex-dev-q28b06421804c

- **example_id**: `dev:q28b06421804c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Bio-Techne’s executives discuss plans for new product development or expansion for Bio-Techne?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7189324940540128 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q28b06421804c`)._

### ex-dev-q29a452be41cd

- **example_id**: `dev:q29a452be41cd`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Fox Corporation’s cable network programming segment profitability trended over recent periods?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7693267077702551 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q29a452be41cd`)._

### ex-dev-q29d3cb8df822

- **example_id**: `dev:q29d3cb8df822`
- **state**: `completed`
- **query**: How are investors interpreting guidance on SLB’s customer engagement metrics within its oilfield services operations?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9323478402140176 · gold=['Earnings', 'DEF14A', '8-K', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.2640681225725909 · skipped= · n_scored=47

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q29d3cb8df822:chunk-48` | 0.8379940390586853 |  | Such statements often contain words such as expect, may, can, believe, predict, plan, potential, project… |
| 2 | `q29d3cb8df822:chunk-47` | 0.834804356098175 |  | <hr /><hr />About SLB SLB (NYSE: SLB) is a global technology company driving energy innovation for a balanced planet. W… |
| 3 | `q29d3cb8df822:chunk-49` | 0.8346847295761108 |  | If one or more of these or other risks or uncertainties materialize (or the consequences of any such development change… |
| 4 | `q29d3cb8df822:chunk-19` | 0.8318372368812561 | 1.0 | This project includes the provision of CO2 removal membranes from natural gas, commissioning, and field service, with f… |
| 5 | `q29d3cb8df822:chunk-4` | 0.8171501755714417 |  | n/m = not meaningful International Markets Driving Profitable Growth SLB CEO Olivier Le Peuch commented, Our third-qua… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q29d3cb8df822`)._

### ex-dev-q2aae5e2ea500

- **example_id**: `dev:q2aae5e2ea500`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Mondelez International’s snack foods segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2aae5e2ea500`)._

### ex-dev-q2c832749ca0b

- **example_id**: `dev:q2c832749ca0b`
- **state**: `completed`
- **query**: What dependency risks exist for Newmont Corporation due to concentration of revenue in a limited number of geographic regions or gold buyers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.21398626473452753 · skipped= · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2c832749ca0b:chunk-200` | 0.8430022597312927 |  | Newcrest is subject to risks associated with the transportation of gold doré, including fluctuating transportation cha… |
| 2 | `q2c832749ca0b:chunk-192` | 0.8246585726737976 | 2.0 | operations at Lihir and Wafi-Golpu in PNG are subject to political and regulatory risks and other uncertainties” and “—… |
| 3 | `q2c832749ca0b:chunk-190` | 0.8156678080558777 |  | We will not control Newcrest and its subsidiaries until implementation of the Newcrest Transaction and the business and… |
| 4 | `q2c832749ca0b:chunk-203` | 0.8097480535507202 |  | In addition, we have established our “Rapid Response” crisis management process to mitigate and prevent the escalation … |
| 5 | `q2c832749ca0b:chunk-93` | 0.807686448097229 |  | _________________________ (1)Primarily consists of amounts due to NGM representing Barrick's 61.5% proportionate share … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2c832749ca0b`)._

### ex-dev-q2d8eb319367a

- **example_id**: `dev:q2d8eb319367a`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did UDR, Inc.’s leadership address potential risks or uncertainties in forward-looking statements for its multifamily property portfolio?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.788088263175707 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2d8eb319367a`)._

### ex-dev-q2ec971ec73f9

- **example_id**: `dev:q2ec971ec73f9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What was United Rentals’ Cost of Goods Sold (COGS) in the most recent quarter?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7303575739184495 · gold=['8-K', '10-Q', '10-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2ec971ec73f9`)._

### ex-dev-q2fe5769567d7

- **example_id**: `dev:q2fe5769567d7`
- **state**: `completed`
- **query**: How does Align Technology manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.4104889601851253 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2fe5769567d7:chunk-68` | 0.8315227031707764 | 2.0 | 1 Includes MSUs vested during the period below 100% of the original grant as actual shares released is based on Align’s… |
| 2 | `q2fe5769567d7:chunk-66` | 0.8282818794250488 | 1.0 | As of September 30, 2023, we expect to recognize $202.1 million of total unamortized compensation costs, net of estimat… |
| 3 | `q2fe5769567d7:chunk-145` | 0.8153588771820068 |  | ####ALIGN TECHNOLOGY, INC. November 3, 2023##By:##/s/ JOSEPH M. HOGAN ####Joseph M. Hogan President and Chief Executive… |
| 4 | `q2fe5769567d7:chunk-121` | 0.8149734735488892 |  | would have a material effect on our financial position and result of operations. This is because the contract considera… |
| 5 | `q2fe5769567d7:chunk-20` | 0.806388795375824 |  | ALIGN TECHNOLOGY, INC. NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS (unaudited) Note 1. Summary of Significant … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2fe5769567d7`)._

### ex-dev-q318eb902f451

- **example_id**: `dev:q318eb902f451`
- **state**: `completed`
- **query**: What questions were asked about Franklin Resources, Inc.’s client retention and engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9199642183398656 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.2960819109658652 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q318eb902f451:chunk-3` | 0.834140419960022 |  | Good morning, and thank you for joining us today to discuss our quarterly and fiscal year results. Please note that the… |
| 2 | `q318eb902f451:chunk-15` | 0.8267531394958496 | 1.0 | Yes, yes. Okay. Thank you. Thanks, Jenny. Thanks, Bill. So maybe I think your question gets to a couple of things. Firs… |
| 3 | `q318eb902f451:chunk-1` | 0.8228715062141418 |  | Welcome to Franklin Resources earnings conference call for the quarter and fiscal year ended September 30, 2024. Hello.… |
| 4 | `q318eb902f451:chunk-5` | 0.8178937435150146 |  | Thank you, Selene. Hello, everyone, and thank you for joining us today to discuss Franklin Templeton's fourth quarter a… |
| 5 | `q318eb902f451:chunk-55` | 0.814120888710022 |  | And this concludes today's Q&A session. I would now like to hand the call back over to Jenny Johnson, Franklin's Presid… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q318eb902f451`)._

### ex-dev-q31f6fd1f392c

- **example_id**: `dev:q31f6fd1f392c`
- **state**: `completed`
- **query**: What governance processes are in place for approving changes to Targa Resources Corp.’s compensation policies?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9979470946084208 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '8-K', '10-Q', 'Earnings']`
- **S2**: nDCG@5=0.21826955258437686 · skipped= · n_scored=99

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q31f6fd1f392c:chunk-34` | 0.8635156154632568 | 1.0 | # CORPORATE GOVERNANCE (cont.) ## Feedback Shared with Board - Review feedback internally - Provide updates to the full… |
| 2 | `q31f6fd1f392c:chunk-52` | 0.8452944755554199 |  | # OUR DECISION MAKING PROCESS (cont.) ## 2021 - 2023 PSU Plan Payout The PSUs granted to our NEOs in 2021 used a simila… |
| 3 | `q31f6fd1f392c:chunk-29` | 0.8446851968765259 | 1.0 | # CORPORATE GOVERNANCE ## Corporate Governance Guidelines The Board of Directors believes that sound governance practic… |
| 4 | `q31f6fd1f392c:chunk-30` | 0.8428840637207031 | 1.0 | # CORPORATE GOVERNANCE (cont.) ## Board Leadership Mr. Chung has served as Chairman of the Board of the Company's Board… |
| 5 | `q31f6fd1f392c:chunk-91` | 0.8421236872673035 |  | # STOCKHOLDER PROPOSALS AND NOMINATIONS FOR THE 2025 ANNUAL MEETING OF STOCKHOLDERS; IDENTIFICATION OF DIRECTOR CANDIDA… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q31f6fd1f392c`)._

### ex-dev-q33197856c996

- **example_id**: `dev:q33197856c996`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Trane Technologies’ quality metric for its HVAC system manufacturing process changed recently?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.742039158611126 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q33197856c996`)._

### ex-dev-q359aee1441c1

- **example_id**: `dev:q359aee1441c1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered regarding annual capital expenditure levels for park expansions and technology
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.5914218405396885 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q359aee1441c1`)._

### ex-dev-q3ef7ce37ae77

- **example_id**: `dev:q3ef7ce37ae77`
- **state**: `completed`
- **query**: How did investors respond to Tapestry, Inc.’s discussion of supply chain risks?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9734136950814526 · gold=['Earnings', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3ef7ce37ae77:chunk-3` | 0.8464956283569336 |  | Good morning. Thank you for joining us. With me today to discuss our fourth quarter and year-end results as well as our… |
| 2 | `q3ef7ce37ae77:chunk-23` | 0.8418323993682861 |  | Well, maybe I'll kick it off, Ike, and then pass it to Scott again. We do have both strategic and financial strength an… |
| 3 | `q3ef7ce37ae77:chunk-71` | 0.836358368396759 |  | Yes. We -- I appreciate the question. We evaluate our investment with any capital allocation decision we make with a lo… |
| 4 | `q3ef7ce37ae77:chunk-11` | 0.8361112475395203 |  | And congratulations on the strong year at Tapestry. When you look at your results in comparison to Capris recently, giv… |
| 5 | `q3ef7ce37ae77:chunk-83` | 0.8208082914352417 |  | So I'll start with Michael Kors. And what we're seeing in our business and what our platform has been delivering is del… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q3ef7ce37ae77`)._

### ex-dev-q3f9446fe3b94

- **example_id**: `dev:q3f9446fe3b94`
- **state**: `completed`
- **query**: How are scenario analyses conducted by American Tower Corporation for risks related to fluctuations in mobile data demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9484971533659527 · gold=['10-K', 'Earnings', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.21398626473452756 · skipped= · n_scored=342

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3f9446fe3b94:chunk-163` | 0.8146867752075195 |  | AMERICAN TOWER CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Tabular amounts in millions, un… |
| 2 | `q3f9446fe3b94:chunk-12` | 0.8134483098983765 | 1.0 | ITEM 1A. RISK FACTORS Risks Related to Our Business Strategy A significant decrease in leasing demand for our communica… |
| 3 | `q3f9446fe3b94:chunk-38` | 0.8123743534088135 |  | We believe that the network technology migration we have seen in the United States, which has led to significantly dens… |
| 4 | `q3f9446fe3b94:chunk-14` | 0.8117695450782776 |  | Our expansion initiatives involve a number of risks and uncertainties, including those related to integrating acquired … |
| 5 | `q3f9446fe3b94:chunk-289` | 0.8080609440803528 |  | AMERICAN TOWER CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (Tabular amounts in millions, un… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q3f9446fe3b94`)._

### ex-dev-q41a18ce876e2

- **example_id**: `dev:q41a18ce876e2`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Kellanova’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q41a18ce876e2`)._

### ex-dev-q430300b97e2f

- **example_id**: `dev:q430300b97e2f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Ingersoll Rand’s inventory or supply chain efficiency targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q430300b97e2f`)._

### ex-dev-q44cfaf358c37

- **example_id**: `dev:q44cfaf358c37`
- **state**: `completed`
- **query**: How do global economic or geopolitical trends shape regional market prospects for Molson Coors Beverage Company's alcoholic beverage portfolio?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5633046918323918 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q44cfaf358c37:chunk-63` | 0.8606552481651306 | 2.0 | Yes. From a -- from an overall portfolio outside of the U.S., Chris, Canada, we do continue to see softness in the beer… |
| 2 | `q44cfaf358c37:chunk-13` | 0.8423224687576294 | 1.0 | Thanks, Andrea. A couple of things I would say in response to your question. Firstly, we believe the changes in the U.S… |
| 3 | `q44cfaf358c37:chunk-51` | 0.8304755091667175 |  | Thanks, Nadine. Look, on your first question, not much surprised us in the fourth quarter. If I had to point to one thi… |
| 4 | `q44cfaf358c37:chunk-45` | 0.8196539282798767 | 1.0 | Look, I mean, maybe just a comment around the overall industry, right? As I said, despite the headlines you might read,… |
| 5 | `q44cfaf358c37:chunk-87` | 0.8192753791809082 |  | Thanks, Eric. Look, I mean, I'll say again, despite the headlines, you might read, the overall beer category grew dolla… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q44cfaf358c37`)._

### ex-dev-q4acd5677c3da

- **example_id**: `dev:q4acd5677c3da`
- **state**: `completed`
- **query**: What questions were asked about Hasbro’s customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9359826917490579 · gold=['Earnings', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.08703245752405495 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4acd5677c3da:chunk-9` | 0.8274117112159729 |  | Thanks, Gina. Turnarounds take time, and for our toy business, we are still in the early innings. While we're likely to… |
| 2 | `q4acd5677c3da:chunk-3` | 0.8235612511634827 |  | Thank you, and good morning, everyone. Joining me today are Chris Cocks, Hasbro's Chief Executive Officer; and Gina Goe… |
| 3 | `q4acd5677c3da:chunk-5` | 0.8186940550804138 |  | Thanks, [ Karan ] and good morning, everyone. For more than a year now, you've heard me outline Hasbro's strategy to re… |
| 4 | `q4acd5677c3da:chunk-85` | 0.8180249929428101 | 1.0 | Yes, in Q4, we were down around 12% or 13% on our internal point-of-sale measurements. When you factor out some of the … |
| 5 | `q4acd5677c3da:chunk-1` | 0.8148008584976196 |  | Good morning, and welcome to the Hasbro Fourth Quarter and Full Year 2023 Earnings Conference Call. [Operator Instructi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4acd5677c3da`)._

### ex-dev-q4bf1699a63fe

- **example_id**: `dev:q4bf1699a63fe`
- **state**: `completed`
- **query**: What dependency risks exist for Boston Properties, Inc. due to concentration of revenue in a limited number of geographic markets or key tenants?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.2054778775428881 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4bf1699a63fe:chunk-113` | 0.8079255223274231 | 1.0 | So I would tell you that the D.C. market is the most -- one of the most interesting markets from our perspective in the… |
| 2 | `q4bf1699a63fe:chunk-15` | 0.7918709516525269 |  | So that's, unfortunately, the technical question that keeps everybody up at night here at BXP, which is what will the a… |
| 3 | `q4bf1699a63fe:chunk-29` | 0.7913150191307068 |  | And first, Bob Pester, congrats on retirement. I guess now we can all look for Rod's steady hand. Just, Owen, and Doug,… |
| 4 | `q4bf1699a63fe:chunk-107` | 0.7848333716392517 | 1.0 | We're seeing the same thing in Boston. And as noted in our discussions internally this last week, for our Boston portfo… |
| 5 | `q4bf1699a63fe:chunk-117` | 0.7837749123573303 | 1.0 | The one other thing I would add is the performance of Reston Town Center. I mean again, the majority of our portfolio i… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4bf1699a63fe`)._

### ex-dev-q4d8ac905167b

- **example_id**: `dev:q4d8ac905167b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Citigroup Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.9026211001048622 · skipped= · n_scored=894

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4d8ac905167b:chunk-293` | 0.8550054430961609 | 2.0 | (1) The year-over-year growth rate is the percentage change in the real (inflation adjusted) GDP level. Under the base … |
| 2 | `q4d8ac905167b:chunk-266` | 0.846011757850647 | 2.0 | Stress Testing Citi performs market risk stress testing on a regular basis to estimate the impact of extreme market mov… |
| 3 | `q4d8ac905167b:chunk-289` | 0.8427531123161316 | 2.0 | Quantitative Component Citi estimates expected credit losses for its quantitative component using (i) its comprehensive… |
| 4 | `q4d8ac905167b:chunk-231` | 0.8335409164428711 | 1.0 | Scenario Analysis The following table presents the estimated impact to Citi’s net interest income, AOCI and CET1 Capita… |
| 5 | `q4d8ac905167b:chunk-334` | 0.8317070603370667 | 2.0 | The following are the main factors and interpretations that Citi considers when estimating the ACL under the CECL metho… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4d8ac905167b`)._

### ex-dev-q4e3318b7d0e9

- **example_id**: `dev:q4e3318b7d0e9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are data privacy or cybersecurity concerns affecting industry practices relevant to water technology solutions at Xylem Inc.?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7146598531416503 · gold=['10-K', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['10-Q', '10-K', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4e3318b7d0e9`)._

### ex-dev-q4f1cc6ea4ba6

- **example_id**: `dev:q4f1cc6ea4ba6`
- **state**: `completed`
- **query**: What sentiment trends are visible around Agilent Technologies’ free cash flow outlook and capital spending plans?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-Q', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.17724662297638585 · skipped= · n_scored=170

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4f1cc6ea4ba6:chunk-163` | 0.825287938117981 | 1.0 | Yes, I think first of all, just to remind the audience, when we talk about the genomics business, what are we talking a… |
| 2 | `q4f1cc6ea4ba6:chunk-3` | 0.8169934749603271 |  | Thank you, Bo, and welcome, everyone, to Agilent's conference call for the fourth quarter of fiscal year 2023. With me … |
| 3 | `q4f1cc6ea4ba6:chunk-51` | 0.8140972256660461 |  | Yes. I think, Matt, it's a great question. And so if we look at the details of kind of the mix, actually, I would say w… |
| 4 | `q4f1cc6ea4ba6:chunk-33` | 0.8122656941413879 | 1.0 | Yes, sure, Patrick. [ How about ] if I lead off, Bob, and then you can add any additional comments you'd like to make h… |
| 5 | `q4f1cc6ea4ba6:chunk-5` | 0.8072582483291626 |  | Thanks, Parmeet, and thanks, everyone, for joining our call today. Before we get into discussing our results and outloo… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4f1cc6ea4ba6`)._

### ex-dev-q536ce4006bf6

- **example_id**: `dev:q536ce4006bf6`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did AutoZone’s leadership say about AutoZone’s share repurchase plans?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5770094797674725 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '8-K', 'DEF14A', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q536ce4006bf6`)._

### ex-dev-q53994e82efbb

- **example_id**: `dev:q53994e82efbb`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Builders FirstSource for recessionary or downturn risks in the residential construction market?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=64

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q53994e82efbb:chunk-12` | 0.799027144908905 |  | BUILDERS FIRSTSOURCE, INC. AND SUBSIDIARIES NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS (Unaudited) 1. Basis o… |
| 2 | `q53994e82efbb:chunk-60` | 0.7909994125366211 |  | * Filed herewith. ** Builders FirstSource, Inc. is furnishing, but not filing, the written statement pursuant to Title … |
| 3 | `q53994e82efbb:chunk-62` | 0.7893019914627075 |  | BUILDERS FIRSTSOURCE, INC. /s/ DAVE RUSH Dave Rush President and Chief Executive Officer (Principal Executive Officer) |
| 4 | `q53994e82efbb:chunk-41` | 0.7890302538871765 |  | The composition and level of working capital typically change during periods of increasing sales as we carry more inven… |
| 5 | `q53994e82efbb:chunk-38` | 0.7886111736297607 |  | We base our estimate of deferred tax assets and liabilities on current tax laws and rates. In certain cases, we also ba… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q53994e82efbb`)._

### ex-dev-q56c2aa1b3aa2

- **example_id**: `dev:q56c2aa1b3aa2`
- **state**: `completed`
- **query**: How are scenario analyses conducted by FedEx Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.24630238874073 · skipped= · n_scored=165

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q56c2aa1b3aa2:chunk-144` | 0.8340051174163818 |  | # Proposal 8 Report on Assessing Systemic Climate Risk from Retirement Plan Options ## Your Board of Directors recommen… |
| 2 | `q56c2aa1b3aa2:chunk-28` | 0.8247755169868469 | 1.0 | # Corporate Governance Matters - Nominees for Election to the Board (cont.) ## Board Risk Oversight The Board of Direct… |
| 3 | `q56c2aa1b3aa2:chunk-138` | 0.8245056867599487 |  | # Board of Directors' Statement in Opposition The Board of Directors and its Governance, Safety, and Public Policy Comm… |
| 4 | `q56c2aa1b3aa2:chunk-145` | 0.8207472562789917 |  | # Proposal 8 Report on Assessing Systemic Climate Risk from Retirement Plan Options (cont.) ## Your Board of Directors … |
| 5 | `q56c2aa1b3aa2:chunk-31` | 0.8152387738227844 |  | # Corporate Governance Matters - The Board's Role and Responsibilities (cont.) ## ESG and CSR Highlights The success of… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q56c2aa1b3aa2`)._

### ex-dev-q57e9d5635f56

- **example_id**: `dev:q57e9d5635f56`
- **state**: `completed`
- **query**: What quarter did guidance point to for streaming breakeven achievement
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q57e9d5635f56:chunk-7` | 0.7978204488754272 | 2.0 | Thank you, Bob. I appreciate your kind words at the outset of the call. It's been an honor serving as Interim CFO these… |
| 2 | `q57e9d5635f56:chunk-57` | 0.7970813512802124 |  | Okay. Thanks for the question, and I want to thank everyone for joining us today. Note that a reconciliation of our non… |
| 3 | `q57e9d5635f56:chunk-19` | 0.7968676090240479 |  | So first on DTC. I mean, pricing is about to step up. You announced the cost-cutting program, some of which might be a … |
| 4 | `q57e9d5635f56:chunk-29` | 0.7930272817611694 |  | Yes. Ben, with respect to cash flow, we do feel good about where we are ending up in '24 from a content spend perspecti… |
| 5 | `q57e9d5635f56:chunk-5` | 0.7901068329811096 |  | Thanks, Alexia, and good afternoon, everyone. Before we begin, this week, we announced that Hugh Johnston will be joini… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q57e9d5635f56`)._

### ex-dev-q587ea3fc913d

- **example_id**: `dev:q587ea3fc913d`
- **state**: `completed`
- **query**: What guidance did Textron’s leadership give on cost structure optimization efforts?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.21826955258437686 · skipped= · n_scored=174

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q587ea3fc913d:chunk-89` | 0.8221473693847656 |  | Yes. Understood. And then secondly, there's been some press reports that Textron has been looking at some M&A competiti… |
| 2 | `q587ea3fc913d:chunk-3` | 0.8178116083145142 |  | Thanks, Leah, and good morning, everyone. Before we begin, I'd like to mention we will be discussing future estimates a… |
| 3 | `q587ea3fc913d:chunk-7` | 0.8049213886260986 | 2.0 | Thanks, Scott, and good morning, everyone. Let's review how each of the segments contributed, starting with Textron Avi… |
| 4 | `q587ea3fc913d:chunk-67` | 0.7922424077987671 | 1.0 | Look, Noah. I think, look, the team is doing everything they can to manage costs, control -- do the right cost actions … |
| 5 | `q587ea3fc913d:chunk-1` | 0.7887552976608276 |  | Thank you for standing by. Welcome to the Textron Fourth Quarter 2023 Earnings Call. [Operator Instructions] This confe… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q587ea3fc913d`)._

### ex-dev-q5ce8ea5bf1b9

- **example_id**: `dev:q5ce8ea5bf1b9`
- **state**: `completed`
- **query**: What dependency risks exist for Global Payments Inc. due to concentration of revenue in a limited number of payment processing partners or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=119

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5ce8ea5bf1b9:chunk-24` | 0.7999929189682007 |  | NOTES TO UNAUDITED CONSOLIDATED FINANCIAL STATEMENTS NOTE 1—BASIS OF PRESENTATION AND SUMMARY OF SIGNIFICANT ACCOUNTING… |
| 2 | `q5ce8ea5bf1b9:chunk-114` | 0.7889764308929443 |  | 2.1##Agreement and Plan of Merger, dated as of August 1, 2022, by and among EVO Payments, Inc., Global Payments Inc. an… |
| 3 | `q5ce8ea5bf1b9:chunk-103` | 0.7889256477355957 |  | Net Income (Loss) Attributable to Global Payments Net income attributable to Global Payments was $361.8 million and $62… |
| 4 | `q5ce8ea5bf1b9:chunk-0` | 0.7886349558830261 |  | PART I - FINANCIAL INFORMATION ITEM 1—FINANCIAL STATEMENTS GLOBAL PAYMENTS INC. UNAUDITED CONSOLIDATED STATEMENTS OF IN… |
| 5 | `q5ce8ea5bf1b9:chunk-117` | 0.7813653945922852 |  | ##Global Payments Inc. ##(Registrant) Date: October 31, 2023##/s/ Joshua J. Whipple ##Joshua J. Whipple ##Senior Execut… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q5ce8ea5bf1b9`)._

### ex-dev-q5d75c4f1ac86

- **example_id**: `dev:q5d75c4f1ac86`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What progress was reported in international park attendance recovery relative to pre pandemic levels
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.5465881385757737 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q5d75c4f1ac86`)._

### ex-dev-q5d883a6e3ff1

- **example_id**: `dev:q5d883a6e3ff1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How have investors reacted to The TJX Companies, Inc.’s updated guidance or forward-looking projections?
- **S1**: top1=`8-K` in_gold=True · nDCG@5=0.8498932729020808 · gold=['Earnings', '8-K', '10-K', 'DEF14A']
- **S1 ordered**: `['8-K', 'Earnings', '10-Q', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q5d883a6e3ff1`)._

### ex-dev-q5fca8aed3bbc

- **example_id**: `dev:q5fca8aed3bbc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Camden Property Trust’s recurring rental income to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.6280699432768105 · gold=['10-K', '8-K', 'Earnings', '10-Q']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q5fca8aed3bbc`)._

### ex-dev-q60107966eba4

- **example_id**: `dev:q60107966eba4`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Kellanova view the pace of innovation cycles in product development and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7189238908241445 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q60107966eba4`)._

### ex-dev-q63259a02ade0

- **example_id**: `dev:q63259a02ade0`
- **state**: `completed`
- **query**: What does Apple's executive compensation structure look like?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=1.0 · gold=['DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.05652670087893601 · skipped= · n_scored=134

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q63259a02ade0:chunk-42` | 0.8921669721603394 |  | # Guiding Compensation Principles Our executive compensation program is designed to motivate and reward outstanding per… |
| 2 | `q63259a02ade0:chunk-38` | 0.8781298398971558 |  | # Executive Compensation (cont.) "Apple's leadership plays a key role in fostering a culture of collaboration - driving… |
| 3 | `q63259a02ade0:chunk-51` | 0.8760194778442383 | 1.0 | # Summary of Other Named Executive Officer Compensation The total target compensation of our four other named executive… |
| 4 | `q63259a02ade0:chunk-39` | 0.8746036887168884 |  | # Message from the People and Compensation Committee (cont.) ## Dear Fellow Shareholders, (cont.) As we look ahead, we'… |
| 5 | `q63259a02ade0:chunk-67` | 0.8744466304779053 |  | # Executive Compensation Tables (cont.) (7) This amount represents: (i) Apple's contributions to Mr. Williams' account … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q63259a02ade0`)._

### ex-dev-q636b07dd9c11

- **example_id**: `dev:q636b07dd9c11`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What impact could proposed legislative changes in the U.S. Credit Card Competition Act have on Mastercard?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.6898217095818122 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '8-K', 'Earnings', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q636b07dd9c11`)._

### ex-dev-q645be3b7875e

- **example_id**: `dev:q645be3b7875e`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Merck & Co., Inc.’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.6512141447433527 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q645be3b7875e`)._

### ex-dev-q64898e5ba36c

- **example_id**: `dev:q64898e5ba36c`
- **state**: `completed`
- **query**: What clarifications did analysts seek regarding Waters Corporation’s investment in chromatography and mass spectrometry innovation projects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9873464281832952 · gold=['Earnings', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', 'DEF14A', '10-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=274

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q64898e5ba36c:chunk-92` | 0.8424524068832397 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS 1 Description of Business and Organization Waters Corporation (the “Company,… |
| 2 | `q64898e5ba36c:chunk-0` | 0.8412841558456421 |  | PART I Item 1: Business General Waters Corporation (the “Company,” “Waters,” “we,” “our,” or “us”), a global leader in … |
| 3 | `q64898e5ba36c:chunk-5` | 0.8290046453475952 |  | Based upon 2023 reports from independent marketing research firms and publicly disclosed sales figures from competitors… |
| 4 | `q64898e5ba36c:chunk-41` | 0.8261338472366333 |  | Item 6: Reserved Item 7: Management’s Discussion and Analysis of Financial Condition and Results of Operations Business… |
| 5 | `q64898e5ba36c:chunk-6` | 0.8221403360366821 |  | System and is five times more sensitive and five times faster than discovery-based imaging systems at precisely determi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q64898e5ba36c`)._

### ex-dev-q69d1505292c8

- **example_id**: `dev:q69d1505292c8`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How might global inflationary trends affect Walgreens Boots Alliance’s input costs and pricing strategies?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q69d1505292c8`)._

### ex-dev-q6c95b5e5930d

- **example_id**: `dev:q6c95b5e5930d`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Medtronic’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7679992931079491 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q6c95b5e5930d`)._

### ex-dev-q6cdb93e02e5f

- **example_id**: `dev:q6cdb93e02e5f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What clawback or recoupment policies apply to SBA Communications Corporation’s incentive compensation in case of restatements or misconduct?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8498932729020808 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q6cdb93e02e5f`)._

### ex-dev-q6d2cc453ca8c

- **example_id**: `dev:q6d2cc453ca8c`
- **state**: `completed`
- **query**: How did analysts probe the outlook for Roper Technologies’ free cash flow generation?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9278143341459562 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=130

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q6d2cc453ca8c:chunk-3` | 0.8128681778907776 |  | Good morning, and thank you all for joining us as we discuss the fourth quarter and full year 2023 financial results fo… |
| 2 | `q6d2cc453ca8c:chunk-19` | 0.7962355613708496 |  | And this might be more of a nuance. But at your Analyst Day, you talked about a willingness to look at businesses that … |
| 3 | `q6d2cc453ca8c:chunk-9` | 0.792750358581543 |  | Thanks, Jason. As we turn to Page 12, let's look back on the year for Application Software segment. Total revenues grew… |
| 4 | `q6d2cc453ca8c:chunk-1` | 0.7916122674942017 |  | Good morning. The Roper Technologies Conference Call will now begin. Today's call is being recorded. [Operator Instruct… |
| 5 | `q6d2cc453ca8c:chunk-54` | 0.7836354970932007 |  | Allison Poliniak-Cusic - Analysts |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q6d2cc453ca8c`)._

### ex-dev-q70b3e2802bf7

- **example_id**: `dev:q70b3e2802bf7`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Tyson Foods’ average cost per pound of processed chicken trend compared to the prior period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q70b3e2802bf7`)._

### ex-dev-q70e4aac30ddb

- **example_id**: `dev:q70e4aac30ddb`
- **state**: `completed`
- **query**: How did leadership respond to analyst questions about AI and personalization initiatives?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9903929125301808 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', 'DEF14A', '10-K']`
- **S2**: nDCG@5=0.13770577618809332 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q70e4aac30ddb:chunk-63` | 0.7880163788795471 |  | Laxman, in the press release, you were mentioning that the reinvention plan is moving ahead of schedule. So which aspec… |
| 2 | `q70e4aac30ddb:chunk-25` | 0.7797167897224426 |  | Next question is coming from David Palmer from Evercore ISI. |
| 3 | `q70e4aac30ddb:chunk-53` | 0.7773580551147461 | 1.0 | John, if I could take that on. Thank you for your question. We have more opportunities than what we have realized, but … |
| 4 | `q70e4aac30ddb:chunk-9` | 0.7753168940544128 |  | Thank you, Rachel. At this time, we'll proceed with our normal Q&A session, which will last until the top of the hour. … |
| 5 | `q70e4aac30ddb:chunk-51` | 0.7740819454193115 |  | There's been a lot of conversation this quarter about throughput, particularly at the drive-thru, but we can also talk … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q70e4aac30ddb`)._

### ex-dev-q719082ac2068

- **example_id**: `dev:q719082ac2068`
- **state**: `completed`
- **query**: How did management characterize the evolution and strategic importance of AI factories?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9239941662222116 · gold=['Earnings', '10-K', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=15

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q719082ac2068:chunk-3` | 0.7503910660743713 |  | # Q4 Fiscal 2024 Summary (cont.) ## Data Center (cont.) - Introduced NVIDIA MONAITM cloud APIs to help developers and p… |
| 2 | `q719082ac2068:chunk-6` | 0.7316737771034241 |  | # Q4 Fiscal 2024 Summary (cont.) ## About NVIDIA (cont.) Certain statements in this press release including, but not li… |
| 3 | `q719082ac2068:chunk-7` | 0.7122354507446289 |  | # Q4 Fiscal 2024 Summary (cont.) ## About NVIDIA (cont.) © 2024 NVIDIA Corporation. All rights reserved. INVIDIA, the N… |
| 4 | `q719082ac2068:chunk-5` | 0.7117297649383545 |  | # Q4 Fiscal 2024 Summary (cont.) ## About NVIDIA (cont.) Simona Jankowski Investor Relations NVIDIA Corporation sjankow… |
| 5 | `q719082ac2068:chunk-4` | 0.7063376307487488 |  | # Q4 Fiscal 2024 Summary (cont.) ## Conference Call and Webcast Information NVIDIA will conduct a conference call with … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q719082ac2068`)._

### ex-dev-q76caada13eca

- **example_id**: `dev:q76caada13eca`
- **state**: `completed`
- **query**: What causes differences between Weyerhaeuser Company’s cash flow and net income (e.g., timberland harvest cycles or non-cash depreciation)?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9199642183398656 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.2809436351950179 · skipped= · n_scored=86

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q76caada13eca:chunk-13` | 0.8359368443489075 |  | Just start with the outline that you gave, framing the housing outlook for this year was helpful. And when you think ab… |
| 2 | `q76caada13eca:chunk-5` | 0.8323430418968201 |  | Thanks, Andy. Good morning, everyone, and thank you for joining us. Yesterday, Weyerhaeuser reported full year GAAP ear… |
| 3 | `q76caada13eca:chunk-15` | 0.8248363733291626 |  | Sure. Well, I'll start with the first question and sort of go product by product. On the lumber side, that's the busine… |
| 4 | `q76caada13eca:chunk-79` | 0.821318507194519 |  | Sure. You bet, Ketan. I think we really have looked at that consistently over the last few years, and I really don't se… |
| 5 | `q76caada13eca:chunk-7` | 0.8183216452598572 | 2.0 | Thank you, Devin, and good morning, everyone. I'll be covering key financial items and fourth quarter financial perform… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q76caada13eca`)._

### ex-dev-q78d98dc75a82

- **example_id**: `dev:q78d98dc75a82`
- **state**: `completed`
- **query**: How has Humana’s Medicare Advantage segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '8-K', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.13152248326683885 · skipped= · n_scored=283

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q78d98dc75a82:chunk-166` | 0.8472502827644348 |  | Humana Inc. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS—(Continued) goodwill included in the carrying value is based on … |
| 2 | `q78d98dc75a82:chunk-79` | 0.8447691202163696 | 1.0 | The changes in Medicare receivables for both the 2023 period and the 2022 period reflect individual Medicare Advantage … |
| 3 | `q78d98dc75a82:chunk-6` | 0.8441658616065979 |  | refer to Note 17 to the audited Consolidated Financial Statements included in Part II, Item 8, "Financial Statements an… |
| 4 | `q78d98dc75a82:chunk-55` | 0.8384226560592651 | 1.0 | this segment are designed to enhance the overall healthcare experience. These services may lead to lower utilization as… |
| 5 | `q78d98dc75a82:chunk-227` | 0.8371481895446777 |  | Humana Inc. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS—(Continued) indeterminate; (ii) discovery is not complete; (iii)… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q78d98dc75a82`)._

### ex-dev-q79acb772ca6b

- **example_id**: `dev:q79acb772ca6b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Ingersoll Rand Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.93228165068934 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=290

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q79acb772ca6b:chunk-23` | 0.820610761642456 |  | (1)Typically includes shares of common stock surrendered to us to satisfy tax withholding obligations in connection wit… |
| 2 | `q79acb772ca6b:chunk-90` | 0.8160468339920044 |  | INGERSOLL RAND INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (in millions, except share and per shar… |
| 3 | `q79acb772ca6b:chunk-165` | 0.8043651580810547 |  | In 2024, the Company expects to contribute $5.1 million to the U.S. pension plans, $6.7 million to the non-U.S. pension… |
| 4 | `q79acb772ca6b:chunk-204` | 0.802740216255188 |  | The Company includes interest expense and penalties related to unrecognized tax benefits as part of the provision for i… |
| 5 | `q79acb772ca6b:chunk-111` | 0.7984765768051147 |  | Prior Year Actions Subsequent to the acquisition of and merger with the Industrial business of Ingersoll-Rand plc (“Ing… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q79acb772ca6b`)._

### ex-dev-q79ae686681b7

- **example_id**: `dev:q79ae686681b7`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Best Buy’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7591919243197319 · gold=['10-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q79ae686681b7`)._

### ex-dev-q7b42f1295dc1

- **example_id**: `dev:q7b42f1295dc1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are scenario analyses conducted by Fiserv for recessionary or downturn risks?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7485147261820462 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7b42f1295dc1`)._

### ex-dev-q7c284aabbba4

- **example_id**: `dev:q7c284aabbba4`
- **state**: `completed`
- **query**: What dependency risks exist for Moderna, Inc. due to concentration of revenue in a limited number of vaccine products or geographic markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9882048111454694 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.9520727775370875 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7c284aabbba4:chunk-25` | 0.8231649994850159 | 2.0 | Thanks, Stephen. And Gena, it's Stéphane. On the upside and downside on the sales for this year, I think on the upside,… |
| 2 | `q7c284aabbba4:chunk-5` | 0.8154656887054443 | 2.0 | Thank you, Lavina. Good morning or good afternoon, everyone. Thank you for joining us today. I will start with a review… |
| 3 | `q7c284aabbba4:chunk-7` | 0.8088434934616089 | 2.0 | Thanks, Stéphane, and hello, everyone. Today, I will review our financial performance for both the fourth quarter and t… |
| 4 | `q7c284aabbba4:chunk-11` | 0.8079410791397095 | 2.0 | Thank you, Stephen and Jamey. For Moderna and the patients we serve, 2024 is all about execution: execution in commerci… |
| 5 | `q7c284aabbba4:chunk-17` | 0.7986651062965393 |  | Great. Thank you, Michael. It's Stéphane. So in terms of contracting, obviously, we cannot start contracting now becaus… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7c284aabbba4`)._

### ex-dev-q7e2586950d8e

- **example_id**: `dev:q7e2586950d8e`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Ball Corporation’s beverage packaging segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7e2586950d8e`)._

### ex-dev-q7eb4e8a11956

- **example_id**: `dev:q7eb4e8a11956`
- **state**: `completed`
- **query**: Summarize Luca Maestri's recent commentary on the gross margin outlook given current FX headwinds.
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7eb4e8a11956:chunk-29` | 0.8293880224227905 |  | As you've seen from our results in Q4 and the guidance for Q1, we're obviously experiencing very strong levels of gross… |
| 2 | `q7eb4e8a11956:chunk-47` | 0.8201031684875488 |  | On the margin side, if I understood your question correctly about the December quarter guidance, keep in mind that actu… |
| 3 | `q7eb4e8a11956:chunk-100` | 0.8095911741256714 |  | Luca Maestri - Executives |
| 4 | `q7eb4e8a11956:chunk-108` | 0.8095911741256714 |  | Luca Maestri - Executives |
| 5 | `q7eb4e8a11956:chunk-112` | 0.8095911741256714 |  | Luca Maestri - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7eb4e8a11956`)._

### ex-dev-q7eb5b91e2366

- **example_id**: `dev:q7eb5b91e2366`
- **state**: `completed`
- **query**: What dependency risks exist for Becton, Dickinson and Company due to concentration of revenue in a limited number of healthcare providers or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9935051443580323 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5 · skipped= · n_scored=76

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7eb5b91e2366:chunk-65` | 0.7824710011482239 |  | Maybe we can turn to capital allocation. Your $1 billion share repurchase announcement over the next 12 to 18 months ce… |
| 2 | `q7eb5b91e2366:chunk-61` | 0.7756770253181458 |  | Yes. Thanks for the question, Matt. We couldn't be more excited about APMs coming into BD. We're really happy having Ka… |
| 3 | `q7eb5b91e2366:chunk-7` | 0.7753644585609436 | 1.0 | *Thanks, Tom, and good morning, everyone. As Tom noted, we delivered competitive organic revenue growth for the fourth … |
| 4 | `q7eb5b91e2366:chunk-31` | 0.7752763628959656 |  | Yes. Thanks, Travis. It's Chris. I'll try and give a little extra color. I think consistent with what I've said, again,… |
| 5 | `q7eb5b91e2366:chunk-11` | 0.7743218541145325 |  | Maybe on this guidance question here. Thanks for all the details. The 125 basis points of headwinds on pharma, bioscien… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7eb5b91e2366`)._

### ex-dev-q7ebef55d671d

- **example_id**: `dev:q7ebef55d671d`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance was offered on Chipotle’s supply chain efficiency targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6266239202359082 · gold=['DEF14A', '10-Q', '10-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7ebef55d671d`)._

### ex-dev-q7ed5279a28b4

- **example_id**: `dev:q7ed5279a28b4`
- **state**: `completed`
- **query**: What did Teradyne’s management note about Teradyne’s operational scalability as test equipment demand volumes grow or contract?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-Q', '10-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-K', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=156

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ed5279a28b4:chunk-16` | 0.825792670249939 |  | TERADYNE, INC. NOTES TO CONDENSED CONSOLIDATED FINANCIAL STATEMENTS (Unaudited) A. THE COMPANY Teradyne, Inc. (“Teradyn… |
| 2 | `q7ed5279a28b4:chunk-134` | 0.8183037042617798 |  | The increase of $19.6 million in selling and administrative expenses was primarily due to the charge of $5.9 million re… |
| 3 | `q7ed5279a28b4:chunk-98` | 0.8182910680770874 |  | nine months ended October 2, 2022, was $9.7 million, or $0.05 per diluted share. In November 2020, Teradyne entered int… |
| 4 | `q7ed5279a28b4:chunk-19` | 0.817855954170227 |  | (1)Includes $1.4 million and $1.8 million in 2023 and 2022, respectively, for leases of Teradyne’s systems recognized o… |
| 5 | `q7ed5279a28b4:chunk-20` | 0.8168578743934631 |  | performance obligation. As of October 1, 2023, Teradyne had $1,133 million of unsatisfied performance obligations. Tera… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7ed5279a28b4`)._

### ex-dev-q811679c2d742

- **example_id**: `dev:q811679c2d742`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What challenges are noted regarding scaling infrastructure or capacity for renewable energy integration to meet growth?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.5831428296492145 · gold=['10-K', '8-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', 'DEF14A', '8-K', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q811679c2d742`)._

### ex-dev-q84038a74fd59

- **example_id**: `dev:q84038a74fd59`
- **state**: `completed`
- **query**: How many organizations were reported to be using Azure OpenAI Service
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9871901582936081 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '8-K', '10-Q', 'DEF14A', '10-K']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=76

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q84038a74fd59:chunk-5` | 0.8349435329437256 | 2.0 | Thank you very much, Brett. We had a solid close to our fiscal year. The Microsoft Cloud surpassed $110 billion in annu… |
| 2 | `q84038a74fd59:chunk-33` | 0.8091570138931274 |  | Yes. And I think just for perspective, I think it's sort of always good to think about it, right, where we have, what, … |
| 3 | `q84038a74fd59:chunk-61` | 0.80607008934021 |  | Yes. I mean the thing that we are both seeing and excited about is both the new workloads. I mean if you think about Az… |
| 4 | `q84038a74fd59:chunk-31` | 0.7961514592170715 |  | Why don't I start on the CapEx question, Satya, then I'll turn it over to you. Mark, really, first of all, both in Q4 a… |
| 5 | `q84038a74fd59:chunk-15` | 0.7910134792327881 |  | Thank you, Keith, for the question. The fundamental guidance and conversation that we have with customers is twofold. O… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q84038a74fd59`)._

### ex-dev-q86f79f57d973

- **example_id**: `dev:q86f79f57d973`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did Linde’s leadership say about Linde’s dividend policy or share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7168795886624337 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '8-K', '10-Q']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q86f79f57d973`)._

### ex-dev-q88819064dbb7

- **example_id**: `dev:q88819064dbb7`
- **state**: `completed`
- **query**: What investor views emerged on Dollar Tree, Inc.’s geographic expansion prospects within the domestic discount retail market?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5833841884680027 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88819064dbb7:chunk-27` | 0.8461692333221436 | 1.0 | Yes. Dollar Tree, the fastest-growing demographic is north of $125,000 a year in income, which brings a lot more firepo… |
| 2 | `q88819064dbb7:chunk-37` | 0.8345758318901062 |  | Yes. So on Dollar Tree, for example, on the margin, we're guiding to 36% to 36.5%. That's a combination of a couple of … |
| 3 | `q88819064dbb7:chunk-25` | 0.8345641493797302 | 2.0 | So two questions. Maybe, could you elaborate on the traffic trends and market share by demographic that you're seeing a… |
| 4 | `q88819064dbb7:chunk-21` | 0.8296269774436951 |  | Yes. I mean obviously, our guidance -- we're looking for a strong year, particularly on the Dollar Tree side. And I thi… |
| 5 | `q88819064dbb7:chunk-55` | 0.8248261213302612 | 1.0 | Two great questions. As far as rebannering, we've already looked at a modest number of stores that we intend to do that… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q88819064dbb7`)._

### ex-dev-q88db5d96c8dd

- **example_id**: `dev:q88db5d96c8dd`
- **state**: `completed`
- **query**: How does Bristol-Myers Squibb manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.08703245752405495 · skipped= · n_scored=176

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88db5d96c8dd:chunk-11` | 0.8164718151092529 |  | Note 1. BASIS OF PRESENTATION AND RECENTLY ISSUED ACCOUNTING STANDARDS Basis of Consolidation Bristol-Myers Squibb Comp… |
| 2 | `q88db5d96c8dd:chunk-174` | 0.8073598146438599 |  | ######BRISTOL-MYERS SQUIBB COMPANY (REGISTRANT)## Date:##October 26, 2023##By:####/s/ Giovanni Caforio, M.D. ########Gi… |
| 3 | `q88db5d96c8dd:chunk-0` | 0.8012599945068359 |  | PART I—FINANCIAL INFORMATION Item 1. FINANCIAL STATEMENTS BRISTOL-MYERS SQUIBB COMPANY CONSOLIDATED STATEMENTS OF EARNI… |
| 4 | `q88db5d96c8dd:chunk-40` | 0.7916234731674194 | 1.0 | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### Dollars in millions, except per sha… |
| 5 | `q88db5d96c8dd:chunk-119` | 0.7869395017623901 |  | (a) Other revenues include royalties and alliance-related revenues for products not sold by our regional commercial org… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q88db5d96c8dd`)._

### ex-dev-q89953a08e494

- **example_id**: `dev:q89953a08e494`
- **state**: `completed`
- **query**: How does Globe Life Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.053652664646244 · skipped= · n_scored=125

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89953a08e494:chunk-103` | 0.8340206742286682 |  | # PAY VERSUS PERFORMANCE (cont.) <table> <tr> <th>Year</th> <th>Globe Life Inc.</th> <th>S&P Life and Health Insurance … |
| 2 | `q89953a08e494:chunk-71` | 0.8310223817825317 |  | # Stock Ownership/Retention Guidelines (cont.) ## Savings Plans Eligible executives and employees may choose to partici… |
| 3 | `q89953a08e494:chunk-38` | 0.830022931098938 |  | # Risk Reporting Structure (cont.) ## Governance Guidelines and Codes of Ethics The Company has adopted Corporate Gover… |
| 4 | `q89953a08e494:chunk-122` | 0.8300037384033203 |  | # APPENDIX A NON-GAAP RECONCILIATION The chart below reflects non-GAAP financial measures utilized by Management which … |
| 5 | `q89953a08e494:chunk-56` | 0.8298117518424988 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## 2023 Performance Globe Life performed well in 2023 and we believe the… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q89953a08e494`)._

### ex-dev-q89fb186f5e49

- **example_id**: `dev:q89fb186f5e49`
- **state**: `completed`
- **query**: What investor views emerged on Linde’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.16958010263680806 · skipped= · n_scored=287

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89fb186f5e49:chunk-8` | 0.8411884307861328 |  | Table of Contents •cultural challenges associated with integrating employees from the acquired company into the existin… |
| 2 | `q89fb186f5e49:chunk-49` | 0.8372948169708252 |  | The APAC segment includes Linde's industrial gases operations in approximately 20 Asian and South Pacific countries and… |
| 3 | `q89fb186f5e49:chunk-24` | 0.8347015380859375 | 1.0 | The company manufactures and distributes its industrial gas products through networks of thousands of production plants… |
| 4 | `q89fb186f5e49:chunk-46` | 0.8274706602096558 |  | Table of Contents The EMEA segment includes Linde's industrial gases operations in approximately 45 European, Middle Ea… |
| 5 | `q89fb186f5e49:chunk-16` | 0.8127285838127136 |  | Table of Contents Peer Performance Table – The graph below compares the most recent five-year cumulative returns of Lin… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q89fb186f5e49`)._

### ex-dev-q8b55a229e784

- **example_id**: `dev:q8b55a229e784`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of C.H. Robinson Worldwide’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.6885288809404666 · gold=['10-K', '10-Q']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q8b55a229e784`)._

### ex-dev-q8ba6a388d681

- **example_id**: `dev:q8ba6a388d681`
- **state**: `completed`
- **query**: What questions were asked about Broadcom’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '8-K', '10-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8ba6a388d681:chunk-3` | 0.836540699005127 |  | Thank you, operator, and good afternoon, everyone. Joining me on today's call are Hock Tan, President and CEO; Kirsten … |
| 2 | `q8ba6a388d681:chunk-11` | 0.8287595510482788 |  | Hock, so yesterday, one of your peers suggested that the market for AI accelerators could be as large as $400 billion. … |
| 3 | `q8ba6a388d681:chunk-1` | 0.8244827389717102 |  | Welcome to Broadcom Inc.'s Fourth Quarter and Fiscal Year 2023 Financial Results Conference Call. At this time, for ope… |
| 4 | `q8ba6a388d681:chunk-69` | 0.8230509757995605 |  | Always with acquisitions in mind, we're continuing our share repurchase program that we promised. So that's -- we're de… |
| 5 | `q8ba6a388d681:chunk-113` | 0.8132824897766113 |  | Thank you, operator. In closing, Broadcom currently plans to report its earnings for the first quarter of fiscal '24 af… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q8ba6a388d681`)._

### ex-dev-q8cc1033cf552

- **example_id**: `dev:q8cc1033cf552`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What guidance did The Sherwin-Williams Company’s leadership provide on debt reduction or leverage targets for The Sherwin-Williams Company?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7378720384008995 · gold=['10-K', 'Earnings', '10-Q']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-K', '10-Q', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q8cc1033cf552`)._

### ex-dev-q8e053e02a010

- **example_id**: `dev:q8e053e02a010`
- **state**: `completed`
- **query**: What dependency risks exist for International Paper Company due to concentration of revenue in a limited number of end-use paper and packaging markets?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.950546328892843 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=225

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q8e053e02a010:chunk-2` | 0.8018686771392822 |  | # Dear Shareowner, (cont.) ## International Paper at a Glance (cont.) The image shows the logo of International Paper. … |
| 2 | `q8e053e02a010:chunk-140` | 0.7913689613342285 |  | # Supplemental (cont.) ## Most Important Performance Measures (cont.) Table of Contents The image shows a close-up view… |
| 3 | `q8e053e02a010:chunk-31` | 0.7886458039283752 |  | # Table of Contents (cont.) ## Mark S. Sutton Mr. Sutton has been Chairman of International Paper since January 1, 2015… |
| 4 | `q8e053e02a010:chunk-220` | 0.7860949039459229 |  | # Appendix B-Reconciliations of Non-GAAP Measures (cont.) Table of Contents World Headquarters International Paper 6400… |
| 5 | `q8e053e02a010:chunk-180` | 0.7787256240844727 |  | # INTERNATIONAL PAPER COMPANY 2024 Long-Term Incentive Compensation Plan (cont.) ## ARTICLE 2 DEFINITIONS 2.1. DEFINITI… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q8e053e02a010`)._

### ex-dev-q8e26f08be2bc

- **example_id**: `dev:q8e26f08be2bc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What challenges arise for Vertex Pharmaceuticals from data privacy regulations and handling of patient data?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5=0.5906415461191282 · gold=['10-K', 'DEF14A', '8-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'DEF14A', 'Earnings', '8-K', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q8e26f08be2bc`)._

### ex-dev-q909c4baef1ee

- **example_id**: `dev:q909c4baef1ee`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did analysts frame queries about Truist Financial Corporation’s shareholder returns, including dividends?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.6266239202359082 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q909c4baef1ee`)._

### ex-dev-q93fb2b2861c4

- **example_id**: `dev:q93fb2b2861c4`
- **state**: `completed`
- **query**: How does Church & Dwight view the pace of product innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9134693626978977 · gold=['10-K', '8-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.21739710475421564 · skipped= · n_scored=208

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q93fb2b2861c4:chunk-20` | 0.8096452355384827 |  | •Decreases in demand for our products would decrease our sales and profitability. Factors that can affect demand includ… |
| 2 | `q93fb2b2861c4:chunk-44` | 0.8038476705551147 | 1.0 | CHURCH & DWIGHT CO., INC AND SUBSIDIARIES (Dollars in millions, except share and per share data) Although we believe on… |
| 3 | `q93fb2b2861c4:chunk-182` | 0.7966868281364441 |  | CHURCH & DWIGHT CO., INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – (Continued) (In millions, excep… |
| 4 | `q93fb2b2861c4:chunk-11` | 0.7964076995849609 | 2.0 | COMPETITION We compete in the household and personal care consumer product categories, which are highly innovative cate… |
| 5 | `q93fb2b2861c4:chunk-102` | 0.7961398363113403 |  | CHURCH & DWIGHT CO., INC. AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS - (Continued) (In millions, excep… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q93fb2b2861c4`)._

### ex-dev-q95535bca90c9

- **example_id**: `dev:q95535bca90c9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Wells Fargo’s average cost per loan origination trend compared to the prior period?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6623468500578608 · gold=['10-Q', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q95535bca90c9`)._

### ex-dev-q95790ca7c1f5

- **example_id**: `dev:q95790ca7c1f5`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did Dayforce Inc.’s leadership say about Dayforce Inc.’s share repurchase plans?
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.4933965394160924 · gold=['10-K', 'Earnings']
- **S1 ordered**: `['8-K', 'Earnings', 'DEF14A', '10-Q', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q95790ca7c1f5`)._

### ex-dev-q9597b3e4d1b2

- **example_id**: `dev:q9597b3e4d1b2`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has investor sentiment shifted following Archer-Daniels-Midland Company’s most recent earnings release?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.68154288742782 · gold=['10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9597b3e4d1b2`)._

### ex-dev-q98c606bb3ce7

- **example_id**: `dev:q98c606bb3ce7`
- **state**: `completed`
- **query**: What litigation or dispute risks did Williams-Sonoma, Inc. identify and what is the potential financial impact for Williams-Sonoma, Inc.?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.07132875491150918 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q98c606bb3ce7:chunk-5` | 0.8255864381790161 |  | Table of Contents domain names, trade secrets and other intellectual property and proprietary technology that we hold a… |
| 2 | `q98c606bb3ce7:chunk-115` | 0.813225507736206 | 1.0 | Table of Contents contributions were vested immediately. Effective July 2022, all matching contributions become vested … |
| 3 | `q98c606bb3ce7:chunk-73` | 0.8090677857398987 |  | Table of Contents Williams-Sonoma, Inc. Notes to Consolidated Financial Statements Note A: Summary of Significant Accou… |
| 4 | `q98c606bb3ce7:chunk-139` | 0.8086355328559875 |  | 10.16####Lease for an additional Company distribution facility located in Olive Branch, Mississippi between Williams-So… |
| 5 | `q98c606bb3ce7:chunk-35` | 0.8083075881004333 |  | ##2/3/19##2/2/20##1/31/21##1/30/22##1/29/23##1/28/24 Williams-Sonoma, Inc.##$100.00##$133.59##$251.70##$307.13##$257.52… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q98c606bb3ce7`)._

### ex-dev-q99a077efaab0

- **example_id**: `dev:q99a077efaab0`
- **state**: `completed`
- **query**: What dependency risks exist for Align Technology due to concentration of revenue in a limited number of orthodontic practices or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3065735963827292 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99a077efaab0:chunk-81` | 0.8121768832206726 |  | You can always say that at Align, there's no single-variable equations. And this is another one. The Teen Guarantee, we… |
| 2 | `q99a077efaab0:chunk-7` | 0.8081273436546326 |  | Thanks, John. In closing, while I'm pleased with our better-than-expected fourth quarter results and start to the year,… |
| 3 | `q99a077efaab0:chunk-3` | 0.8079327940940857 | 1.0 | Thanks, Shirley. Good afternoon, and thanks for joining us. On our call today, I'll provide an overview of our fourth q… |
| 4 | `q99a077efaab0:chunk-63` | 0.8059428930282593 |  | On the guidance, maybe one other way I wanted to ask it and see if I could tease out a little bit of color on what's as… |
| 5 | `q99a077efaab0:chunk-5` | 0.8038920164108276 |  | Thanks, Joe. Now for our Q4 financial results. Total revenues for the fourth quarter were $956.7 million, down 0.4% fro… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q99a077efaab0`)._

### ex-dev-q99ec5f1aeea5

- **example_id**: `dev:q99ec5f1aeea5`
- **state**: `completed`
- **query**: What questions were asked about Federal Realty Investment Trust’s tenant retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9134693626978977 · gold=['Earnings', '8-K', '10-K', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=64

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99ec5f1aeea5:chunk-4` | 0.8421304225921631 |  | Federal Realty Investment Trust Announces Operating Results for the Year and Quarter Ended December 31, 2023 NORTH BETH… |
| 2 | `q99ec5f1aeea5:chunk-2` | 0.8355173468589783 |  | <hr />Safe Harbor Language Certain matters discussed within this Supplemental Information may be deemed to be forward-l… |
| 3 | `q99ec5f1aeea5:chunk-9` | 0.8353485465049744 |  | Certain matters discussed within this Press Release may be deemed to be forward-looking statements within the meaning o… |
| 4 | `q99ec5f1aeea5:chunk-6` | 0.8342958688735962 |  | Occupancy The portfolio was 92.2% occupied and 94.2% leased as of December 31, 2023. Additionally, our comparable resid… |
| 5 | `q99ec5f1aeea5:chunk-8` | 0.8284912109375 |  | (1)Does not assume the impact of potential acquisitions or dispositions which have not closed as of January 31, 2024. (… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q99ec5f1aeea5`)._

### ex-dev-q9a5cfe35fecd

- **example_id**: `dev:q9a5cfe35fecd`
- **state**: `completed`
- **query**: What dependency risks exist for CMS Energy Corporation due to concentration of revenue in a limited number of geographic regions or key utility customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5087403079104241 · skipped= · n_scored=194

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9a5cfe35fecd:chunk-19` | 0.8432967662811279 | 2.0 | •the investment performance of the assets of CMS Energy’s and Consumers’ pension and benefit plans, the discount rates,… |
| 2 | `q9a5cfe35fecd:chunk-20` | 0.8408185243606567 |  | •potential costs, lost revenues, reputational harm, or other consequences resulting from misappropriation of assets or … |
| 3 | `q9a5cfe35fecd:chunk-24` | 0.8385581970214844 | 2.0 | CMS Energy Corporation Consumers Energy Company Management’s Discussion and Analysis of Financial Condition and Results… |
| 4 | `q9a5cfe35fecd:chunk-18` | 0.8310784101486206 |  | •potentially adverse regulatory treatment, effects of a failure to receive timely regulatory orders that are or could c… |
| 5 | `q9a5cfe35fecd:chunk-177` | 0.8291873931884766 |  | liability company agreements. For additional details on these indemnity obligations, see Note 2, Contingencies and Comm… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9a5cfe35fecd`)._

### ex-dev-q9c255237096a

- **example_id**: `dev:q9c255237096a`
- **state**: `completed`
- **query**: What perquisites or fringe benefits are included in The AES Corporation’s executive compensation disclosures?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=1.0 · gold=['DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.6096731708870796 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9c255237096a:chunk-9` | 0.8882861137390137 | 2.0 | # Compensation and Benefits Best Practices Target Total Compensation at Approximately the 50th Percentile Independent C… |
| 2 | `q9c255237096a:chunk-40` | 0.8832130432128906 | 2.0 | # EXECUTIVE COMPENSATION COMPENSATION DISCUSSION AND ANALYSIS ("CD&A") (cont.) ## What AES Does ## What AES Doesn't Do … |
| 3 | `q9c255237096a:chunk-44` | 0.870642900466919 | 1.0 | # Overview of AES Total Compensation ## Elements of Compensation The following table presents each element of compensat… |
| 4 | `q9c255237096a:chunk-46` | 0.8641632199287415 |  | # Overview of AES Total Compensation (cont.) ## 2023 Performance Incentive Plan Payouts 2023 Company Performance Score … |
| 5 | `q9c255237096a:chunk-48` | 0.8581923246383667 |  | # Overview of AES Total Compensation (cont.) ## Overall score is 127%1 (1) The AES Corporate Performance score is round… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9c255237096a`)._

### ex-dev-q9dd3907388e3

- **example_id**: `dev:q9dd3907388e3`
- **state**: `completed`
- **query**: How does Duke Energy view the pace of innovation cycles in renewable energy technologies and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.6309297535714575 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9dd3907388e3:chunk-8` | 0.8205618262290955 |  | ◦Changes in rules for regional transmission organizations, including changes in rate designs and new and evolving capac… |
| 2 | `q9dd3907388e3:chunk-6` | 0.8186144232749939 | 1.0 | ◦The ability to implement our business strategy, including our carbon emission reduction goals; ◦State, federal and for… |
| 3 | `q9dd3907388e3:chunk-0` | 0.818453311920166 |  | News Release Media Contact: Gillian Moore 24-Hour: 800.559.3853 Analyst Contact: Abby Motsinger Office: 704.382.7624 Au… |
| 4 | `q9dd3907388e3:chunk-7` | 0.8107360601425171 |  | ◦The influence of weather and other natural phenomena on operations, including the economic, operational and other effe… |
| 5 | `q9dd3907388e3:chunk-5` | 0.8019632697105408 |  | The most directly comparable GAAP measure for adjusted segment income or adjusted other net loss is segment income and … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9dd3907388e3`)._

### ex-dev-q9f32df79b0d7

- **example_id**: `dev:q9f32df79b0d7`
- **state**: `completed`
- **query**: How does Capital One view the pace of digital banking innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.43067655807339306 · skipped= · n_scored=4

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9f32df79b0d7:chunk-2` | 0.8162325620651245 |  | •Auto average loans decreased $493 million, or 1 percent, to $75.7 billion. ◦Commercial Banking average loans decreased… |
| 2 | `q9f32df79b0d7:chunk-3` | 0.8115940093994141 |  | Capital One Financial Corporation (www.capitalone.com) is a financial holding company which, along with its subsidiarie… |
| 3 | `q9f32df79b0d7:chunk-1` | 0.78510981798172 |  | •Total net revenue increased 4 percent to $9.4 billion. •Total non-interest expense increased 1 percent to $4.9 billion… |
| 4 | `q9f32df79b0d7:chunk-0` | 0.7750875949859619 | 1.0 | Exhibit 99.1 News Release <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9f32df79b0d7`)._

### ex-dev-qa057a3d428a2

- **example_id**: `dev:qa057a3d428a2`
- **state**: `completed`
- **query**: What dependency risks exist for McKesson Corporation due to concentration of revenue in a limited number of pharmaceutical manufacturers or healthcare providers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.23449779936240625 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa057a3d428a2:chunk-20` | 0.8315284848213196 |  | McKESSON CORPORATION FINANCIAL NOTES (UNAUDITED) 1. Significant Accounting Policies Nature of Operations: McKesson Corp… |
| 2 | `qa057a3d428a2:chunk-96` | 0.8298133611679077 | 2.0 | MD&A Index McKESSON CORPORATION FINANCIAL REVIEW (CONTINUED) (UNAUDITED) The following summarizes our four reportable s… |
| 3 | `qa057a3d428a2:chunk-73` | 0.8187386989593506 |  | McKESSON CORPORATION FINANCIAL NOTES (CONTINUED) (UNAUDITED) State and Local Government Claims The Company and two othe… |
| 4 | `qa057a3d428a2:chunk-89` | 0.8185197114944458 |  | McKESSON CORPORATION FINANCIAL NOTES (CONTINUED) (UNAUDITED) The RxTS segment helps solve medication access, affordabil… |
| 5 | `qa057a3d428a2:chunk-22` | 0.8176976442337036 |  | McKESSON CORPORATION FINANCIAL NOTES (CONTINUED) (UNAUDITED) 2. Business Acquisitions and Divestitures Acquisitions Rx … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa057a3d428a2`)._

### ex-dev-qa33b36ffd2c1

- **example_id**: `dev:qa33b36ffd2c1`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Garmin’s fitness segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7146598531416503 · gold=['10-Q', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa33b36ffd2c1`)._

### ex-dev-qa5c748248a5b

- **example_id**: `dev:qa5c748248a5b`
- **state**: `completed`
- **query**: How has the ratio of MSCI’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-Q', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.24090885754831726 · skipped= · n_scored=255

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa5c748248a5b:chunk-50` | 0.8295561671257019 |  | ####################Period Ended################## ##########2022####################2023######## (in billions)####Marc… |
| 2 | `qa5c748248a5b:chunk-49` | 0.8270677924156189 | 1.0 | Total operating revenues increased 12.5% for the year ended December 31, 2023. Adjusting for the impact of acquisitions… |
| 3 | `qa5c748248a5b:chunk-83` | 0.8261325359344482 | 2.0 | Index operating revenues increased 11.4% for the year ended December 31, 2023, driven by strong growth from both recurr… |
| 4 | `qa5c748248a5b:chunk-235` | 0.8242887854576111 |  | (c). Changes in Internal Control Over Financial Reporting There have been no changes in our internal control over finan… |
| 5 | `qa5c748248a5b:chunk-135` | 0.8223485946655273 |  | Deferred Revenue Deferred revenues represent both cash received and the amounts billed to clients for products and serv… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa5c748248a5b`)._

### ex-dev-qa602975e3d19

- **example_id**: `dev:qa602975e3d19`
- **state**: `completed`
- **query**: How has the ratio of Mondelez International’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9411655511901171 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=189

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa602975e3d19:chunk-163` | 0.8418588638305664 | 2.0 | # Back to Contents (cont.) ## Back to Contents tax obligations under the enacted tax law changes. Refer to Note 16, Inc… |
| 2 | `qa602975e3d19:chunk-165` | 0.833713948726654 |  | # Back to Contents (cont.) ## Back to Contents <table><tr><th rowspan="2">Diluted EPS to Adjusted EPS¹ (Unaudited)</th>… |
| 3 | `qa602975e3d19:chunk-181` | 0.8281779289245605 |  | # ANNEX B: MONDELEZ INTERNATIONAL, INC. 2024 PERFORMANCE INCENTIVE PLAN (EFFECTIVE MAY 22, 2024) (cont.) ## SECTION 7. … |
| 4 | `qa602975e3d19:chunk-145` | 0.8281400203704834 |  | # THIRD-PARTY REPORT ASSESSING EFFECTIVENESS OF IMPLEMENTATION OF HUMAN RIGHTS POLICY (cont.) ## BOARD OF DIRECTORS' ST… |
| 5 | `qa602975e3d19:chunk-178` | 0.8277871012687683 |  | # ANNEX B: MONDELEZ INTERNATIONAL, INC. 2024 PERFORMANCE INCENTIVE PLAN (EFFECTIVE MAY 22, 2024) (cont.) ## SECTION 6. … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa602975e3d19`)._

### ex-dev-qa9744c8552ed

- **example_id**: `dev:qa9744c8552ed`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did analysts question TJX Companies’ management on their strategies for responsible sourcing and sustainable supply chain practices?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6729475164829866 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa9744c8552ed`)._

### ex-dev-qab00fabe02dc

- **example_id**: `dev:qab00fabe02dc`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How did Rockwell Automation’s executives address regulatory or policy developments and their potential implications for industrial automation solutions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7083232243990188 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', '8-K', 'Earnings', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qab00fabe02dc`)._

### ex-dev-qaf55b76bfcad

- **example_id**: `dev:qaf55b76bfcad`
- **state**: `completed`
- **query**: Which partnership with a major telecommunications provider was highlighted for bundling offers
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '8-K', '10-Q', 'DEF14A', '10-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qaf55b76bfcad:chunk-53` | 0.7801758050918579 |  | Sorry. Sorry, Phil. I was listening to your second question. I forgot your first one. Senior moment. What basically we'… |
| 2 | `qaf55b76bfcad:chunk-21` | 0.759874701499939 |  | I'll take the second part first. Our plan when we bring ESPN direct to consumer, which is inevitable, which is going to… |
| 3 | `qaf55b76bfcad:chunk-19` | 0.7568727731704712 |  | So first on DTC. I mean, pricing is about to step up. You announced the cost-cutting program, some of which might be a … |
| 4 | `qaf55b76bfcad:chunk-41` | 0.7516346573829651 |  | Good questions, John. Thank you. We've actually been licensing content to Netflix and are going to continue to. We're a… |
| 5 | `qaf55b76bfcad:chunk-35` | 0.7512847185134888 |  | Jessica, first of all, in India, our linear business actually does quite well, it's making money. But we know that othe… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qaf55b76bfcad`)._

### ex-dev-qb00e9c27fd32

- **example_id**: `dev:qb00e9c27fd32`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Monster Beverage Corporation’s segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb00e9c27fd32`)._

### ex-dev-qb2123a701a82

- **example_id**: `dev:qb2123a701a82`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Atmos Energy view the pace of pipeline technology innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.6388967123938784 · gold=['DEF14A', '8-K', '10-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb2123a701a82`)._

### ex-dev-qb22cbf2f4782

- **example_id**: `dev:qb22cbf2f4782`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Apple management recently commented on services attach rates and other value-added offerings?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.631251450669265 · gold=['10-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb22cbf2f4782`)._

### ex-dev-qb26bf8457b0f

- **example_id**: `dev:qb26bf8457b0f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What risks are associated with opening new healthcare facilities for Universal Health Services, Inc. when patient demand is uncertain?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7860353577841278 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb26bf8457b0f`)._

### ex-dev-qb35a5efa65ce

- **example_id**: `dev:qb35a5efa65ce`
- **state**: `completed`
- **query**: What dependency risks exist for Evergy, Inc. due to concentration of revenue in a limited number of service territories or key industrial customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'Earnings', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.6827658641914235 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb35a5efa65ce:chunk-7` | 0.7969100475311279 | 2.0 | Thanks, David, and good morning, everyone. Turning to Slide 14, I'll start with a review of our results for the fourth … |
| 2 | `qb35a5efa65ce:chunk-73` | 0.7933330535888672 | 1.0 | Very -- just one quick follow-up question from Paul Fremont's on the Slide 9, just as opposed to the earnings impact as… |
| 3 | `qb35a5efa65ce:chunk-3` | 0.7816882133483887 |  | Thank you, Valerie, and good morning, everyone. Welcome to Evergy's Fourth Quarter 2023 Earnings Conference Call. Our w… |
| 4 | `qb35a5efa65ce:chunk-41` | 0.7721483707427979 | 2.0 | In terms of earnings sensitivity, I wouldn't call it linear from that perspective. These are obviously large industrial… |
| 5 | `qb35a5efa65ce:chunk-39` | 0.7701897621154785 |  | Just in terms of the base demand, kind of the new incremental load customers, the 2% to 3% versus the base of 50 basis … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb35a5efa65ce`)._

### ex-dev-qb500a9b42ef8

- **example_id**: `dev:qb500a9b42ef8`
- **state**: `completed`
- **query**: How has the ratio of CMS Energy Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9452713619732751 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=488

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb500a9b42ef8:chunk-166` | 0.8431958556175232 |  | The fair value losses in the above table could be realized only if CMS Energy and Consumers transferred all of their fi… |
| 2 | `qb500a9b42ef8:chunk-378` | 0.8416410088539124 |  | CMS Energy has provided a valuation allowance of $2 million for the local tax loss carryforward. CMS Energy and Consume… |
| 3 | `qb500a9b42ef8:chunk-425` | 0.8407140970230103 |  | Table of Contents Report of Independent Registered Public Accounting Firm To the Board of Directors and Stockholders of… |
| 4 | `qb500a9b42ef8:chunk-307` | 0.8404591679573059 |  | 1CMS Energy’s and Consumers’ operating right-of-use lease assets are reported as other non‐current assets on their cons… |
| 5 | `qb500a9b42ef8:chunk-380` | 0.8334457874298096 |  | If recognized, all of these uncertain tax benefits would affect CMS Energy’s and Consumers’ annual effective tax rates … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb500a9b42ef8`)._

### ex-dev-qb590e4e6d1ec

- **example_id**: `dev:qb590e4e6d1ec`
- **state**: `completed`
- **query**: How has the ratio of PG&E Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.08703245752405495 · skipped= · n_scored=213

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb590e4e6d1ec:chunk-99` | 0.8476476073265076 |  | (1) This activity is primarily related to the change in unbilled revenue and amounts subject to refund, partially offse… |
| 2 | `qb590e4e6d1ec:chunk-121` | 0.843697190284729 |  | (1) Represents the cumulative differences between the recorded costs to remove assets and amounts collected through rat… |
| 3 | `qb590e4e6d1ec:chunk-134` | 0.8431223034858704 |  | On each of February 16, May 18, and September 14, 2023, the Board of Directors of the Utility declared common stock div… |
| 4 | `qb590e4e6d1ec:chunk-6` | 0.8390989303588867 | 1.0 | PG&E Corporation’s net loss primarily consists of interest expense on long-term debt. Utility The table below shows cer… |
| 5 | `qb590e4e6d1ec:chunk-178` | 0.8384968638420105 |  | The following table presents changes in the lower end of the range of PG&E Corporation’s and the Utility’s reasonably e… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb590e4e6d1ec`)._

### ex-dev-qba0102803c57

- **example_id**: `dev:qba0102803c57`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Kimco Realty Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5531464700081437 · skipped= · n_scored=332

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba0102803c57:chunk-142` | 0.8375034332275391 | 1.0 | KIMCO REALTY CORPORATION AND SUBSIDIARIES AND KIMCO REALTY OP, LLC AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STA… |
| 2 | `qba0102803c57:chunk-141` | 0.8280428051948547 | 1.0 | KIMCO REALTY CORPORATION AND SUBSIDIARIES AND KIMCO REALTY OP, LLC AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STA… |
| 3 | `qba0102803c57:chunk-145` | 0.8253653049468994 |  | KIMCO REALTY CORPORATION AND SUBSIDIARIES AND KIMCO REALTY OP, LLC AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STA… |
| 4 | `qba0102803c57:chunk-235` | 0.8242448568344116 |  | KIMCO REALTY CORPORATION AND SUBSIDIARIES AND KIMCO REALTY OP, LLC AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STA… |
| 5 | `qba0102803c57:chunk-139` | 0.8222930431365967 |  | KIMCO REALTY CORPORATION AND SUBSIDIARIES AND KIMCO REALTY OP, LLC AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STA… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qba0102803c57`)._

### ex-dev-qba50bc033945

- **example_id**: `dev:qba50bc033945`
- **state**: `completed`
- **query**: What commentary is provided by Teledyne Technologies on demand forecasts in light of government defense spending trends?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.45649691033014544 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba50bc033945:chunk-89` | 0.8100395798683167 | 1.0 | Yes. Okay. And then in past quarters, you sort of broke out [indiscernible] book-to-bill versus legacy Teledyne book-to… |
| 2 | `qba50bc033945:chunk-7` | 0.8009897470474243 | 1.0 | Thank you, Robert. This is Edwin and I will report on the Digital Imaging segment, which is 56% of Teledyne's portfolio… |
| 3 | `qba50bc033945:chunk-91` | 0.7939918041229248 | 1.0 | Sure. If you look at Instrumentation, which is all legacy Teledyne in some ways, which is marine, environmental and tes… |
| 4 | `qba50bc033945:chunk-109` | 0.7838282585144043 |  | That's very good. We look at our pipeline as necessarily say that we have better orders at this time. But we're talking… |
| 5 | `qba50bc033945:chunk-41` | 0.7813593149185181 | 2.0 | Well, sure. Obviously, CR is always an unpleasant occurrence for us. The way we're looking at it is we're only right no… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qba50bc033945`)._

### ex-dev-qbd63044fc6b3

- **example_id**: `dev:qbd63044fc6b3`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What risk is associated with franchisee financial health amid rapid expansion requirements
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.708583264987264 · gold=['10-K', 'Earnings', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', 'DEF14A', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qbd63044fc6b3`)._

### ex-dev-qbdbd002b0a41

- **example_id**: `dev:qbdbd002b0a41`
- **state**: `completed`
- **query**: How has the ratio of Caterpillar Inc.’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=1.0 · gold=['10-Q', 'Earnings', '10-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.6309297535714575 · skipped= · n_scored=94

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbdbd002b0a41:chunk-3` | 0.8120191097259521 |  | Thanks, Abby. Good morning, everyone, and welcome to Caterpillar's Fourth Quarter of 2023 Earnings Call. I'm Ryan Fiedl… |
| 2 | `qbdbd002b0a41:chunk-7` | 0.8091129064559937 | 1.0 | Thanks, Jim, and good morning, everyone. I'll begin with commentary on the fourth quarter results, including the perfor… |
| 3 | `qbdbd002b0a41:chunk-91` | 0.8041794300079346 |  | Thanks, everybody, and thank you, Jim, Andrew and everyone who joined the call today. A replay of our call will be avai… |
| 4 | `qbdbd002b0a41:chunk-27` | 0.7995885610580444 |  | Well, thank you for your question. We've been pleased by the progress we've made. You recall, we started with that 2016… |
| 5 | `qbdbd002b0a41:chunk-5` | 0.7988508939743042 |  | Thanks, Ryan. Good morning, everyone. Thank you for joining us. As we close out 2023, I'd like to start by recognizing … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qbdbd002b0a41`)._

### ex-dev-qc03648d89328

- **example_id**: `dev:qc03648d89328`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Moderna’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7591919243197319 · gold=['10-K', '10-Q', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc03648d89328`)._

### ex-dev-qc187429e2dc5

- **example_id**: `dev:qc187429e2dc5`
- **state**: `completed`
- **query**: What dependency risks exist for Huntington Ingalls Industries, Inc. due to concentration of revenue in a limited number of government defense contracts?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.8151510484299677 · skipped= · n_scored=249

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc187429e2dc5:chunk-109` | 0.8366701006889343 | 2.0 | HUNTINGTON INGALLS INDUSTRIES, INC. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS 1. DESCRIPTION OF BUSINESS Huntington In… |
| 2 | `qc187429e2dc5:chunk-11` | 0.8315383195877075 | 2.0 | Item 1A. Risk Factors Our consolidated financial position, results of operations and cash flows are subject to various … |
| 3 | `qc187429e2dc5:chunk-0` | 0.8305025100708008 | 2.0 | PART I ITEM 1. BUSINESS History and Organization Huntington Ingalls Industries, Inc. ("HII", the "Company", "we", "us",… |
| 4 | `qc187429e2dc5:chunk-142` | 0.8293407559394836 | 1.0 | For the year ended December 31, 2023, the Company recognized revenue of $690 million related to its contract liabilitie… |
| 5 | `qc187429e2dc5:chunk-127` | 0.8212156891822815 | 1.0 | 7. REVENUE The following is a description of principal activities from which the Company generates its revenues. For mo… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc187429e2dc5`)._

### ex-dev-qc20017b12da3

- **example_id**: `dev:qc20017b12da3`
- **state**: `completed`
- **query**: How does Moderna view the pace of mRNA vaccine development cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.6968778680746041 · skipped= · n_scored=11

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc20017b12da3:chunk-6` | 0.8634742498397827 | 1.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## About Moderna In over 1… |
| 2 | `qc20017b12da3:chunk-0` | 0.8627229928970337 |  | Exhibit 99.1 # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates Third quarter 2023 re… |
| 3 | `qc20017b12da3:chunk-1` | 0.8575619459152222 | 1.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## 2023 Commercial Updates… |
| 4 | `qc20017b12da3:chunk-4` | 0.8574421405792236 | 2.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## Clinical Updates Modern… |
| 5 | `qc20017b12da3:chunk-10` | 0.8570859432220459 | 1.0 | # (Unaudited, in millions) (cont.) ## Forward-Looking Statements This press release contains forward-looking statements… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc20017b12da3`)._

### ex-dev-qc20e5c5b254e

- **example_id**: `dev:qc20e5c5b254e`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Evergy manage equity award burn rate or share pool availability?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.8596355563650325 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc20e5c5b254e`)._

### ex-dev-qc28e5aa0181b

- **example_id**: `dev:qc28e5aa0181b`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are scenario analyses conducted by Humana Inc. for potential shifts in Medicare Advantage enrollment?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7332063582049065 · gold=['Earnings', '10-K', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc28e5aa0181b`)._

### ex-dev-qc4efe3f0f342

- **example_id**: `dev:qc4efe3f0f342`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How could global geopolitical tensions affect Mastercard's cross?border revenues?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5=0.6327646179298274 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc4efe3f0f342`)._

### ex-dev-qc6c8c1f4ddfe

- **example_id**: `dev:qc6c8c1f4ddfe`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has CMS Energy Corporation’s electric utility segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6594343379129768 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc6c8c1f4ddfe`)._

### ex-dev-qc8e6b0d72c52

- **example_id**: `dev:qc8e6b0d72c52`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Caesars Entertainment, Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc8e6b0d72c52:chunk-107` | 0.8104942440986633 |  | It's Shaun Kelley on for Julie. Two questions, if I could. First, on the regional side. Tom, you've been calling out fo… |
| 2 | `qc8e6b0d72c52:chunk-111` | 0.7938631772994995 |  | Great. And then as my follow-up for you or for Eric. Just how should we think about, let's call it, EBITDA flow through… |
| 3 | `qc8e6b0d72c52:chunk-1` | 0.7868748903274536 |  | Good day, and thank you for standing by. Welcome to the Caesars Entertainment, Inc. 2023 Fourth Quarter and Full Year E… |
| 4 | `qc8e6b0d72c52:chunk-11` | 0.7834663391113281 |  | Thanks, Bret. To touch briefly on the fourth quarter results. I know we pre-released about a month ago. So they've been… |
| 5 | `qc8e6b0d72c52:chunk-19` | 0.7827472686767578 |  | Great. And then just to get a sense of in Las Vegas, what type of operating expense growth you're anticipating? And may… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc8e6b0d72c52`)._

### ex-dev-qcbbca1138c08

- **example_id**: `dev:qcbbca1138c08`
- **state**: `completed`
- **query**: What investor views emerged on Freeport-McMoRan’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.324908057430603 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcbbca1138c08:chunk-37` | 0.8233964443206787 | 1.0 | Well, we're constantly monitoring the market and you can be confident that opportunities are available are presented to… |
| 2 | `qcbbca1138c08:chunk-51` | 0.8139123916625977 | 1.0 | With regard to your proposed investments in the U.S., maybe even looking in Latin America, maybe could you remind us on… |
| 3 | `qcbbca1138c08:chunk-3` | 0.8089594841003418 |  | Thank you, and good morning. Welcome to the Freeport-McMoRan conference call. Earlier this morning, we reported our fou… |
| 4 | `qcbbca1138c08:chunk-1` | 0.7676708698272705 |  | Ladies and gentlemen, thank you for standing by. Welcome to the Freeport-McMoRan Fourth Quarter Conference Call. [Opera… |
| 5 | `qcbbca1138c08:chunk-53` | 0.7671715021133423 | 1.0 | On the first part of the question, with respect to how we evaluate projects and returns, we don't target one number. We… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qcbbca1138c08`)._

### ex-dev-qcdb8bc16cf2f

- **example_id**: `dev:qcdb8bc16cf2f`
- **state**: `completed`
- **query**: What guidance was offered on Jack Henry & Associates’ technology platform modernization targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9499797323370371 · gold=['Earnings', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.24153350098894139 · skipped= · n_scored=126

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcdb8bc16cf2f:chunk-23` | 0.821346640586853 | 1.0 | Yes. No. I mean, fortunately, I took over for an individual that did a pretty good job. So nothing significant. I mean,… |
| 2 | `qcdb8bc16cf2f:chunk-63` | 0.8143270015716553 |  | No, Chris. I'll take that. This is Greg. So no, I mean typical -- and just as a reminder really for everybody that typi… |
| 3 | `qcdb8bc16cf2f:chunk-89` | 0.7967302799224854 | 1.0 | Yes. I think you hit on all of them. I think it is a combination of much of what you described. We continue to look at … |
| 4 | `qcdb8bc16cf2f:chunk-87` | 0.7907382249832153 |  | Okay. All right. That's helpful. And then just in terms of M&A, clearly, the pace of M&A has slowed. And just curious l… |
| 5 | `qcdb8bc16cf2f:chunk-3` | 0.7892310619354248 |  | Thank you, Drew. Good morning, and thank you for joining us for the Jack Henry Fourth Quarter and Full Year 2024 Earnin… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qcdb8bc16cf2f`)._

### ex-dev-qcf796a17c330

- **example_id**: `dev:qcf796a17c330`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How are scenario analyses conducted by FirstEnergy Corp. for fluctuations in electricity demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8498932729020808 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qcf796a17c330`)._

### ex-dev-qd08d64c0654c

- **example_id**: `dev:qd08d64c0654c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Fortive Corporation’s segment profitability trended over recent periods?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7659463877163701 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd08d64c0654c`)._

### ex-dev-qd177bdad4bdd

- **example_id**: `dev:qd177bdad4bdd`
- **state**: `completed`
- **query**: What pension discount rate assumption was used for year end valuation?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9751957567060058 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.8687949224876581 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd177bdad4bdd:chunk-173` | 0.8569982051849365 | 2.0 | (a)A pension discount rate of 4.75% was used for the applicable plans following the transaction and remeasurement recog… |
| 2 | `qd177bdad4bdd:chunk-77` | 0.8425348401069641 | 2.0 | Notwithstanding these actions, the impact of our postretirement benefit plans on our earnings may be volatile in that t… |
| 3 | `qd177bdad4bdd:chunk-85` | 0.8418536186218262 | 2.0 | How We Addressed the Matter in Our Audit We obtained an understanding, evaluated the design and tested the operating ef… |
| 4 | `qd177bdad4bdd:chunk-163` | 0.8227115869522095 | 2.0 | (a)Benefit obligation balances represent the projected benefit obligation for our qualified defined benefit pension pla… |
| 5 | `qd177bdad4bdd:chunk-166` | 0.8213568925857544 |  | Differences between the actual return and expected return on plan assets during the year, and changes in the benefit ob… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd177bdad4bdd`)._

### ex-dev-qd2e3bd55f2ee

- **example_id**: `dev:qd2e3bd55f2ee`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What questions were asked about HCA Healthcare’s patient engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7631679915955182 · gold=['DEF14A', 'Earnings', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd2e3bd55f2ee`)._

### ex-dev-qd422350b37cb

- **example_id**: `dev:qd422350b37cb`
- **state**: `completed`
- **query**: What investor views emerged on Martin Marietta Materials’ geographic expansion prospects within domestic markets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9452713619732751 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.4166158115319974 · skipped= · n_scored=312

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd422350b37cb:chunk-0` | 0.8501981496810913 | 1.0 | PART I ITEM 1 – BUSINESS General Martin Marietta Materials, Inc. (the Company or Martin Marietta) is a natural resource… |
| 2 | `qd422350b37cb:chunk-46` | 0.8474549055099487 | 1.0 | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations ITEM 7 – MANAG… |
| 3 | `qd422350b37cb:chunk-117` | 0.8421728610992432 |  | Part II ♦ Item 8 – Financial Statements and Supplementary Data Notes to Financial Statements Note A: Accounting Policie… |
| 4 | `qd422350b37cb:chunk-48` | 0.8252487182617188 | 1.0 | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations Magnesia Speci… |
| 5 | `qd422350b37cb:chunk-13` | 0.8138021230697632 |  | Part I ♦ Item 1A – Risk Factors ITEM 1A – RISK FACTORS An investment in Martin Marietta common stock or debt securities… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd422350b37cb`)._

### ex-dev-qd483c94f1ec6

- **example_id**: `dev:qd483c94f1ec6`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How do investors view American International Group, Inc.’s valuation relative to peers based on recent disclosures?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7373239404693707 · gold=['DEF14A', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd483c94f1ec6`)._

### ex-dev-qd5c685de4d7a

- **example_id**: `dev:qd5c685de4d7a`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What themes emerged regarding the convergence of technology and biotechnology in the company operating model
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.7373239404693707 · gold=['10-K', 'DEF14A', 'Earnings', '8-K']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd5c685de4d7a`)._

### ex-dev-qd639a486b106

- **example_id**: `dev:qd639a486b106`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: Which general medicine candidate in obesity was identified for upcoming mid stage data readout
- **S1**: top1=`8-K` in_gold=False · nDCG@5=0.5196610607458307 · gold=['Earnings', '10-K']
- **S1 ordered**: `['8-K', '10-Q', 'Earnings', 'DEF14A', '10-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd639a486b106`)._

### ex-dev-qd87c2da5e7da

- **example_id**: `dev:qd87c2da5e7da`
- **state**: `completed`
- **query**: How does Kenvue manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.21398626473452756 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd87c2da5e7da:chunk-60` | 0.8660138249397278 |  | # Compensation Clawback Policies (cont.) ## Compensation Risk Management Kenvue is committed to effective risk manageme… |
| 2 | `qd87c2da5e7da:chunk-9` | 0.8361362218856812 | 1.0 | # Executive Compensation Highlights (page 35) Kenvue's executive compensation program is designed to align behaviors wi… |
| 3 | `qd87c2da5e7da:chunk-58` | 0.83576899766922 |  | # Executive Compensation Decision-Making (cont.) ## Stock Ownership Guidelines Kenvue has adopted stock ownership guide… |
| 4 | `qd87c2da5e7da:chunk-54` | 0.8336908221244812 |  | # Executive Compensation (cont.) ## Founder Shares (Approved by the Kenvue CHCC) Following the Separation, the Kenvue C… |
| 5 | `qd87c2da5e7da:chunk-59` | 0.8259803056716919 |  | # Compensation Clawback Policies Kenvue maintains two compensation recoupment policies intended to encourage robust ris… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qd87c2da5e7da`)._

### ex-dev-qdb9da6a1e373

- **example_id**: `dev:qdb9da6a1e373`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Packaging Corporation of America manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.8596355563650325 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qdb9da6a1e373`)._

### ex-dev-qdbaa829dd4cc

- **example_id**: `dev:qdbaa829dd4cc`
- **state**: `completed`
- **query**: What questions were asked about Gen Digital Inc.’s customer retention and renewal rates?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.2960819109658652 · skipped= · n_scored=227

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdbaa829dd4cc:chunk-25` | 0.8359487056732178 |  | Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations Please read the following… |
| 2 | `qdbaa829dd4cc:chunk-9` | 0.8352386951446533 | 1.0 | •Our customers’ dissatisfaction with our efforts to market additional products and services; •Our customer service and … |
| 3 | `qdbaa829dd4cc:chunk-80` | 0.8288097381591797 |  | GEN DIGITAL INC. Notes to the Consolidated Financial Statements Note 1. Description of Business and Significant Account… |
| 4 | `qdbaa829dd4cc:chunk-21` | 0.8220338821411133 |  | PART II Item 5. Market for Registrant’s Common Equity, Related Stockholder Matters and Issuer Purchases of Equity Secur… |
| 5 | `qdbaa829dd4cc:chunk-0` | 0.8182514309883118 |  | PART I Item 1. Business Purpose and Mission Purpose: Powering Digital Freedom. Mission: We create technology solutions … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qdbaa829dd4cc`)._

### ex-dev-qdec70f55027f

- **example_id**: `dev:qdec70f55027f`
- **state**: `completed`
- **query**: What investor views emerged on Mettler-Toledo International Inc.’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9734136950814526 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.17921797188361427 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdec70f55027f:chunk-1` | 0.8146882057189941 |  | Good morning. My name is Audra, and I will be your conference operator today. At this time, I would like to welcome eve… |
| 2 | `qdec70f55027f:chunk-75` | 0.7953814268112183 |  | No. I mean I'll start and let Patrick jump in if he wants to. I think the challenge with pipettes right now is that the… |
| 3 | `qdec70f55027f:chunk-101` | 0.7787425518035889 | 1.0 | Yes. Thanks, Rachel. And I'll start and then Shawn if you have some additional comments, feel free to chime in. So I th… |
| 4 | `qdec70f55027f:chunk-9` | 0.7712758779525757 |  | Thanks, Shawn. Let me start with some comments on our operating businesses, starting with Lab. As we had expected, dema… |
| 5 | `qdec70f55027f:chunk-51` | 0.7702251672744751 | 1.0 | Sure, absolutely. And again, I'll probably give you some insights into the different regions, but also in different end… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qdec70f55027f`)._

### ex-dev-qdfe52ef66df5

- **example_id**: `dev:qdfe52ef66df5`
- **state**: `completed`
- **query**: How has the ratio of IDEXX Laboratories’ recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9452713619732751 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.5177220549768954 · skipped= · n_scored=271

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdfe52ef66df5:chunk-46` | 0.8466225862503052 | 1.0 | The prevalence of in-clinic testing, as opposed to outside reference laboratories such as IDEXX Reference Laboratories,… |
| 2 | `qdfe52ef66df5:chunk-104` | 0.8376091718673706 |  | Report of Independent Registered Public Accounting Firm To the Board of Directors and Stockholders of IDEXX Laboratorie… |
| 3 | `qdfe52ef66df5:chunk-62` | 0.8337715864181519 | 2.0 | CAG Diagnostics Recurring Revenue. The increase in CAG Diagnostics recurring revenue was primarily due to higher realiz… |
| 4 | `qdfe52ef66df5:chunk-45` | 0.833480179309845 | 2.0 | Our long-term success in the continuing growth of our CAG recurring diagnostic products and services is dependent upon:… |
| 5 | `qdfe52ef66df5:chunk-56` | 0.8247688412666321 | 1.0 | (1)Reported revenue growth and organic revenue growth may not recalculate due to rounding. Total Company Revenue. The i… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qdfe52ef66df5`)._

### ex-dev-qe1811f4fd3dc

- **example_id**: `dev:qe1811f4fd3dc`
- **state**: `completed`
- **query**: What questions were asked about Digital Realty Trust’s customer or tenant engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9293449960425915 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=108

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qe1811f4fd3dc:chunk-105` | 0.8419971466064453 |  | Thank you, Betsy. Digital Realty capped off a transformative 2023 with a strong fourth quarter that was highlighted by … |
| 2 | `qe1811f4fd3dc:chunk-5` | 0.8329201936721802 |  | Thanks, Jordan, and thanks to everyone for joining our call. 2023 was a milestone year for Digital Realty as we made st… |
| 3 | `qe1811f4fd3dc:chunk-1` | 0.8288774490356445 |  | Good afternoon, and welcome to the Digital Realty Fourth Quarter 2023 Earnings Call. Please note, this event is being r… |
| 4 | `qe1811f4fd3dc:chunk-3` | 0.8261877298355103 |  | Thank you, operator, and welcome, everyone, to Digital Realty's Fourth Quarter 2023 Earnings Conference Call. Joining m… |
| 5 | `qe1811f4fd3dc:chunk-29` | 0.8185288906097412 |  | Thanks, Michael. So I would say, on a year-over-year basis, we're -- the dynamics has changed tremendously on so many f… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qe1811f4fd3dc`)._

### ex-dev-qe2edf9d38872

- **example_id**: `dev:qe2edf9d38872`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Charter Communications’ broadband segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7659463877163701 · gold=['10-Q', '10-K', 'Earnings', 'DEF14A']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qe2edf9d38872`)._

### ex-dev-qe8a08fb7bfff

- **example_id**: `dev:qe8a08fb7bfff`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Meta Platforms, Inc.’s advertising segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qe8a08fb7bfff`)._

### ex-dev-qe93fa46ab352

- **example_id**: `dev:qe93fa46ab352`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does Philip Morris International view the pace of innovation cycles in reduced-risk products and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7189324940540128 · gold=['Earnings', '10-Q', '10-K', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qe93fa46ab352`)._

### ex-dev-qe99b7fb80e2c

- **example_id**: `dev:qe99b7fb80e2c`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Intercontinental Exchange’s data services segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.665593054087714 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qe99b7fb80e2c`)._

### ex-dev-qeccd6f3b9d06

- **example_id**: `dev:qeccd6f3b9d06`
- **state**: `completed`
- **query**: What feedback surfaced on Akamai Technologies' innovation or new product pipeline prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.6164336326286644 · skipped= · n_scored=140

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeccd6f3b9d06:chunk-5` | 0.8248796463012695 | 2.0 | Thanks, Tom, and thank you very much for the terrific job that you've done over the last 10 years at Akamai. It's truly… |
| 2 | `qeccd6f3b9d06:chunk-3` | 0.8115265369415283 |  | Thank you, operator. Good afternoon, everyone, and thank you for joining Akamai's Fourth Quarter 2023 Earnings Call. Sp… |
| 3 | `qeccd6f3b9d06:chunk-1` | 0.8097946643829346 |  | Good afternoon, and welcome to the Akamai Technologies, Inc. Fourth Quarter 2023 Earnings Conference Call. [Operator In… |
| 4 | `qeccd6f3b9d06:chunk-73` | 0.8001137375831604 | 2.0 | Great. So let me start with edge inferencing. And so some of the examples I gave, that's exactly what's happening for c… |
| 5 | `qeccd6f3b9d06:chunk-89` | 0.7983841300010681 | 2.0 | Yes. Great question. So what we're doing now is, as I mentioned in the last question, deploying more hardware in existi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qeccd6f3b9d06`)._

### ex-dev-qf13afdfcadcf

- **example_id**: `dev:qf13afdfcadcf`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did Howmet Aerospace Inc.’s leadership say about Howmet Aerospace Inc.’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.6857691422200264 · gold=['Earnings', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['DEF14A', 'Earnings', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf13afdfcadcf`)._

### ex-dev-qf25e1308bae4

- **example_id**: `dev:qf25e1308bae4`
- **state**: `completed`
- **query**: Which investor concerns about the company’s China exposure did management acknowledge?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9629964747243054 · gold=['Earnings', 'DEF14A', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '8-K', '10-K']`
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=74

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf25e1308bae4:chunk-61` | 0.7890028357505798 | 1.0 | At the core, remember, the U.S. government wants to limit the latest capabilities of NVIDIA's accelerated computing and… |
| 2 | `qf25e1308bae4:chunk-59` | 0.7700338363647461 |  | I wanted to ask about the China business. I know that in the prepared comments, you said that you started shipping some… |
| 3 | `qf25e1308bae4:chunk-27` | 0.7446216940879822 |  | I wanted to -- Colette, I wanted to touch on your comments that you expected the next generation of products, I assume … |
| 4 | `qf25e1308bae4:chunk-7` | 0.7444860339164734 |  | [Operator Instructions] Your first question comes from the line of Toshiya Hari from Goldman Sachs. |
| 5 | `qf25e1308bae4:chunk-10` | 0.7425392866134644 |  | Jensen Huang;Co-Founder, CEO, President & Director - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf25e1308bae4`)._

### ex-dev-qf38450369367

- **example_id**: `dev:qf38450369367`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Nordson Corporation’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.665593054087714 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf38450369367`)._

### ex-dev-qf5b4bbe60015

- **example_id**: `dev:qf5b4bbe60015`
- **state**: `completed`
- **query**: How has Cadence Design Systems’ IP segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.3065735963827292 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf5b4bbe60015:chunk-0` | 0.8490122556686401 |  | Exhibit 99.01 Cadence Reports Second Quarter 2024 Financial Results Second Quarter Backlog of $6.0 Billion Updating 202… |
| 2 | `qf5b4bbe60015:chunk-2` | 0.8426527976989746 |  | •Major long-term development partner broadly deployed Palladium Z3 to deliver to its next generation AI product roadmap… |
| 3 | `qf5b4bbe60015:chunk-1` | 0.8267948031425476 | 1.0 | For fiscal year 2024, the company expects: •Revenue in the range of $4.60 billion to $4.66 billion •GAAP operating marg… |
| 4 | `qf5b4bbe60015:chunk-10` | 0.8249120116233826 |  | * Includes, as applicable, equity in losses or income from investments, write-down of investments, gains or losses on i… |
| 5 | `qf5b4bbe60015:chunk-22` | 0.8184489011764526 |  | † The non-GAAP measures presented in the table above should not be considered a substitute for financial results and me… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf5b4bbe60015`)._

### ex-dev-qf7a3126727b8

- **example_id**: `dev:qf7a3126727b8`
- **state**: `completed`
- **query**: How does Sysco Corporation’s debt maturity profile affect liquidity and cost structure?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=148

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf7a3126727b8:chunk-140` | 0.8325161337852478 |  | # ANNEX I NON-GAAP RECONCILIATIONS (cont.) information to both management and investors that (1) is indicative of the p… |
| 2 | `qf7a3126727b8:chunk-16` | 0.8225246667861938 |  | # BOARD LEADERSHIP STRUCTURE (cont.) ## DIRECTOR INDEPENDENCE (cont.) The Board has reviewed all relevant relationships… |
| 3 | `qf7a3126727b8:chunk-3` | 0.8167009949684143 |  | # LETTER FROM OUR CEO AND CHAIRMAN (cont.) ## Dear Sysco Stockholder, Throughout our rich 54-year history, Sysco has ma… |
| 4 | `qf7a3126727b8:chunk-4` | 0.816469132900238 |  | # LETTER FROM OUR CEO AND CHAIRMAN (cont.) ## Recipe For Growth Strategy Remains the Forefront Sysco's Recipe For Growt… |
| 5 | `qf7a3126727b8:chunk-76` | 0.815686821937561 |  | # Compensation Arrangements for Messrs. Cheung and Russell (cont.) ## Recipe For Growth Strategic Business Objectives T… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf7a3126727b8`)._

### ex-dev-qf8cbcec9fec6

- **example_id**: `dev:qf8cbcec9fec6`
- **state**: `completed`
- **query**: How has the ratio of Ingersoll Rand’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9688823411593558 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=1.0 · skipped= · n_scored=117

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf8cbcec9fec6:chunk-113` | 0.8474985957145691 | 1.0 | # INGERSOLL RAND INC. AND SUBSIDIARIES ADJUSTED COMBINED FINANCIAL INFORMATION BY SEGMENT (Unaudited; in millions, exce… |
| 2 | `qf8cbcec9fec6:chunk-111` | 0.8390980362892151 |  | # Annex A (cont.) ## RECONCILIATION OF GAAP MEASURES TO NON-GAAP MEASURES In addition to consolidated GAAP financial me… |
| 3 | `qf8cbcec9fec6:chunk-112` | 0.8387530446052551 |  | # Annex A (cont.) ## RECONCILIATION OF GAAP MEASURES TO NON-GAAP MEASURES (cont.) to service its debt. Free Cash Flow i… |
| 4 | `qf8cbcec9fec6:chunk-116` | 0.8383550643920898 |  | # INGERSOLL RAND INC. AND SUBSIDIARIES UNAUDITED SUPPLEMENTAL ADJUSTED COMBINED FINANCIAL INFORMATION RECONCILIATION OF… |
| 5 | `qf8cbcec9fec6:chunk-115` | 0.8335255980491638 |  | # INGERSOLL RAND INC. AND SUBSIDIARIES RECONCILIATION OF DILUTED NET INCOME PER SHARE TO ADJUSTED DILUTED EARNINGS PER … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf8cbcec9fec6`)._

### ex-dev-qf8e3e71e08c9

- **example_id**: `dev:qf8e3e71e08c9`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has Principal Financial Group’s retirement solutions segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.7679992931079491 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf8e3e71e08c9`)._

### ex-dev-qf9c15fa46d48

- **example_id**: `dev:qf9c15fa46d48`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How has the ratio of Live Nation Entertainment’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.7189324940540128 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf9c15fa46d48`)._

### ex-dev-qfa38830206fb

- **example_id**: `dev:qfa38830206fb`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does The Clorox Company manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.7168795886624337 · gold=['DEF14A', '10-Q', '10-K', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qfa38830206fb`)._

### ex-dev-qfbef9973c7fb

- **example_id**: `dev:qfbef9973c7fb`
- **state**: `completed`
- **query**: What clarification did management provide on margin durability in the face of potential memory‑cost inflation?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.950546328892843 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.38685280723454163 · skipped= · n_scored=74

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qfbef9973c7fb:chunk-47` | 0.7791064381599426 |  | Congratulations on the results. Colette, I wanted to talk about your comment regarding gross margins and that it should… |
| 2 | `qfbef9973c7fb:chunk-49` | 0.7789846658706665 | 1.0 | Yes, thanks for the question. We highlighted in our opening remarks, really about our Q4 results and our outlook for Q1… |
| 3 | `qfbef9973c7fb:chunk-27` | 0.771821916103363 |  | I wanted to -- Colette, I wanted to touch on your comments that you expected the next generation of products, I assume … |
| 4 | `qfbef9973c7fb:chunk-33` | 0.7570602893829346 |  | Congrats on the results. I wanted to ask, I guess, a 2-part question, and it comes at what Stacy was getting at on your… |
| 5 | `qfbef9973c7fb:chunk-37` | 0.7522770166397095 |  | First, our CSPs have a very clear view of our product road map and transitions. And that transparency with our CSPs giv… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qfbef9973c7fb`)._

### ex-dev-qfd572ccfcb0f

- **example_id**: `dev:qfd572ccfcb0f`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What investor views emerged on Hasbro’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.6107229205982195 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qfd572ccfcb0f`)._

### ex-dev-qff56bedc2f87

- **example_id**: `dev:qff56bedc2f87`
- **state**: `completed`
- **query**: What questions were asked about Globe Life Inc.’s customer retention metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9293449960425915 · gold=['Earnings', '8-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=114

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff56bedc2f87:chunk-11` | 0.8495082259178162 |  | Thanks, Frank. First, let me spend a few minutes discussing our share repurchase program, available liquidity and capit… |
| 2 | `qff56bedc2f87:chunk-1` | 0.8442380428314209 |  | Hello, and welcome to Globe Life Inc.'s Fourth Quarter 2023 Earnings Release. My name is Melissa, and I will be your op… |
| 3 | `qff56bedc2f87:chunk-105` | 0.8251997828483582 |  | And then just one more, if I could. The -- so when I look at the dividends and share repo guidance for '24, $440 millio… |
| 4 | `qff56bedc2f87:chunk-7` | 0.8102794885635376 |  | Thank you, Frank. At American Income Life, life premiums were up 7% over the year ago quarter to $406 million, and life… |
| 5 | `qff56bedc2f87:chunk-23` | 0.8087043166160583 |  | Yes. Our plan is to unlock assumptions in the third quarter. So for instance, we've seen 2 quarters of good experience … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qff56bedc2f87`)._

### ex-dev-qff73996028bf

- **example_id**: `dev:qff73996028bf`
- **state**: `completed`
- **query**: How has Williams-Sonoma’s management addressed supply-chain risks and efforts to enhance Williams-Sonoma’s resilience?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.43942193198999935 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff73996028bf:chunk-39` | 0.8169137239456177 | 2.0 | Table of Contents Elevating our World-Class Customer Service We are continuing to improve our world-class customer serv… |
| 2 | `qff73996028bf:chunk-139` | 0.8095119595527649 |  | 10.16####Lease for an additional Company distribution facility located in Olive Branch, Mississippi between Williams-So… |
| 3 | `qff73996028bf:chunk-37` | 0.8088662624359131 | 1.0 | Table of Contents ITEM 7. MANAGEMENT’S DISCUSSION AND ANALYSIS OF FINANCIAL CONDITION AND RESULTS OF OPERATIONS The fol… |
| 4 | `qff73996028bf:chunk-21` | 0.8075810670852661 |  | Table of Contents •general economic conditions, changes in diplomatic and trade relationships, including the imposition… |
| 5 | `qff73996028bf:chunk-9` | 0.8067185878753662 | 1.0 | Table of Contents suppliers to our distribution centers. Factors such as labor disputes, union organizing activity, geo… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qff73996028bf`)._

### ex-eval-chunk-only-chunk-q0b530d

- **example_id**: `eval:chunk-only:chunk_q0b530d`
- **state**: `completed`
- **query**: How does Brown-Forman view the pace of product innovation cycles and their effect on market competitiveness in the spirits industry?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=90

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q0b530d:10-K:chunk-35` | 0.820074200630188 |  | That's helpful. And then maybe just one quick follow-up. You've sort of talked about your excitement about a return to … |
| 2 | `chunk_q0b530d:10-K:chunk-5` | 0.817528247833252 |  | Thank you, Sue, and good morning, everyone. Thank you for joining us today as we share Brown-Forman's fiscal 2024 resul… |
| 3 | `chunk_q0b530d:10-K:chunk-15` | 0.81075519323349 |  | All right. Leanne. And then, Lawson, maybe can you just give us a perspective as you're looking forward, I guess, this … |
| 4 | `chunk_q0b530d:10-K:chunk-21` | 0.8105502128601074 |  | One short term and one long term for me. On the short term, coming back to inventories, obviously, large headwind in th… |
| 5 | `chunk_q0b530d:10-K:chunk-17` | 0.8058869242668152 |  | Yes. All right. Bryan. A few things. One, U.S. whiskey and tequila, which are our two biggest categories continue to be… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q0b530d`)._

### ex-eval-chunk-only-chunk-q29280e

- **example_id**: `eval:chunk-only:chunk_q29280e`
- **state**: `completed`
- **query**: How does Atmos Energy Corporation manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=83

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q29280e:10-K:chunk-4` | 0.8366469144821167 |  | # About Atmos Energy Atmos Energy Corporation, an S&P 500 company headquartered in Dallas, is the country's largest nat… |
| 2 | `chunk_q29280e:10-K:chunk-25` | 0.8353755474090576 |  | # Director Compensation (cont.) ## Long-Term Compensation Each non-employee director is also eligible to participate in… |
| 3 | `chunk_q29280e:10-K:chunk-54` | 0.8281009793281555 |  | # Outstanding Equity Awards (cont.) ## Performance-Based Restricted Stock Units Vesting Schedule ³ <table><tr><th>Name<… |
| 4 | `chunk_q29280e:10-K:chunk-31` | 0.8250330090522766 |  | # Approval, on an Advisory Basis, of the Compensation of Our Named Executive Officers (cont.) ## Executive Compensation… |
| 5 | `chunk_q29280e:10-K:chunk-80` | 0.8171847462654114 |  | # Information About the Annual Meeting (cont.) ## Other Business In the event that any matter not described herein is p… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q29280e`)._

### ex-eval-chunk-only-chunk-q2ccba5

- **example_id**: `eval:chunk-only:chunk_q2ccba5`
- **state**: `completed`
- **query**: What questions were asked about Boston Scientific’s customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q2ccba5:Earnings:chunk-113` | 0.8461402654647827 |  | Thanks for joining us today. We appreciate your interest in Boston Scientific. If we were unable to get to your questio… |
| 2 | `chunk_q2ccba5:Earnings:chunk-15` | 0.8170579075813293 |  | Sure. Thanks, Robbie, for the comments. I'll start with WATCHMAN. It's just an excellent platform. With growth of 23% f… |
| 3 | `chunk_q2ccba5:Earnings:chunk-1` | 0.8162661790847778 |  | Good morning, and welcome to the Boston Scientific Fourth Quarter 2023 Earnings Call. [Operator Instructions] Please no… |
| 4 | `chunk_q2ccba5:Earnings:chunk-75` | 0.8127942085266113 |  | Congratulations for a strong end of the year. I wanted to ask about the international cardiac ablation market. Boston h… |
| 5 | `chunk_q2ccba5:Earnings:chunk-13` | 0.8075982332229614 |  | Great. Congrats on a really good quarter. And congratulations, Lauren, on the promotion. Wanted to ask on two of the bi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q2ccba5`)._

### ex-eval-chunk-only-chunk-q44d295

- **example_id**: `eval:chunk-only:chunk_q44d295`
- **state**: `completed`
- **query**: How has the ratio of Amphenol Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=235

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q44d295:10-Q:chunk-54` | 0.8649556040763855 |  | The following table reconciles Adjusted Operating Income, Adjusted Operating Margin, Adjusted Net Income from continuin… |
| 2 | `chunk_q44d295:10-Q:chunk-61` | 0.8647394180297852 |  | The following table reconciles Adjusted Operating Income, Adjusted Operating Margin, Adjusted Net Income from continuin… |
| 3 | `chunk_q44d295:10-Q:chunk-46` | 0.8552374839782715 |  | Income from continuing operations attributable to Amphenol Corporation are both non-GAAP financial measures, each as de… |
| 4 | `chunk_q44d295:10-Q:chunk-161` | 0.8496325016021729 |  | Note 8—Earnings Per Share The following is a reconciliation of net income from continuing operations, discontinued oper… |
| 5 | `chunk_q44d295:10-Q:chunk-5` | 0.8464121222496033 |  | reportable business segments), each led by a segment manager reporting directly to the Chief Executive Officer, reinfor… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q44d295`)._

### ex-eval-chunk-only-chunk-q5ebb5e

- **example_id**: `eval:chunk-only:chunk_q5ebb5e`
- **state**: `completed`
- **query**: How has investor sentiment shifted following The AES Corporation’s most recent earnings release?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q5ebb5e:Earnings:chunk-7` | 0.8304616212844849 |  | # CAUTIONARY NOTE REGARDING FORWARD-LOOKING STATEMENTS (cont.) 2024 Proxy Statement I 4 aes - our ability to achieve re… |
| 2 | `chunk_q5ebb5e:Earnings:chunk-48` | 0.8181981444358826 |  | # Overview of AES Total Compensation (cont.) ## Overall score is 127%1 (1) The AES Corporate Performance score is round… |
| 3 | `chunk_q5ebb5e:Earnings:chunk-109` | 0.8125556707382202 |  | # Growth Details: (cont.) ## Proxy - THE AES CORPORATION + Proxy Solicited on Behalf of the Board of Directors of The A… |
| 4 | `chunk_q5ebb5e:Earnings:chunk-9` | 0.8116708993911743 |  | # Compensation and Benefits Best Practices Target Total Compensation at Approximately the 50th Percentile Independent C… |
| 5 | `chunk_q5ebb5e:Earnings:chunk-5` | 0.811529815196991 |  | # PROXY STATEMENT The AES Corporation 4300 Wilson Blvd. Arlington, VA 22203, USA www.aes.com March 14, 2024 The Board o… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q5ebb5e`)._

### ex-eval-chunk-only-chunk-q829eae

- **example_id**: `eval:chunk-only:chunk_q829eae`
- **state**: `completed`
- **query**: What guidance was offered on Amazon’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q829eae:10-Q:chunk-89` | 0.8436083197593689 |  | Table of Contents Guidance We provided guidance on October 26, 2023, in our earnings release furnished on Form 8-K as s… |
| 2 | `chunk_q829eae:10-Q:chunk-63` | 0.805084228515625 |  | Table of Contents Item 2. Management’s Discussion and Analysis of Financial Condition and Results of Operations Forward… |
| 3 | `chunk_q829eae:10-Q:chunk-77` | 0.7985851764678955 |  | Table of Contents and related transaction costs are included in “Fulfillment,” AWS costs are primarily classified as “T… |
| 4 | `chunk_q829eae:10-Q:chunk-96` | 0.7984797954559326 |  | Table of Contents •the extent to which we invest in technology and infrastructure, fulfillment, and other expense categ… |
| 5 | `chunk_q829eae:10-Q:chunk-68` | 0.7895541191101074 |  | Table of Contents Results of Operations We have organized our operations into three segments: North America, Internatio… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q829eae`)._

### ex-eval-chunk-only-chunk-q8fc814

- **example_id**: `eval:chunk-only:chunk_q8fc814`
- **state**: `completed`
- **query**: What guidance was offered on Apollo Global Management’s fundraising targets for new investment vehicles?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '8-K', '10-Q', '10-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=78

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q8fc814:Earnings:chunk-9` | 0.8208407759666443 |  | Great. Thank you, Scott. And good morning, everyone. So as demonstrated by our results, 2023 was a very successful year… |
| 2 | `chunk_q8fc814:Earnings:chunk-1` | 0.8170484304428101 |  | Good morning, and welcome to Apollo Global Management's Fourth Quarter and Full Year 2023 Earnings Conference Call. [Op… |
| 3 | `chunk_q8fc814:Earnings:chunk-39` | 0.8056392073631287 |  | I think you're hearing from us. In a week or 2, on the fixed income call, you'll hear from Jim Belardi. And if you look… |
| 4 | `chunk_q8fc814:Earnings:chunk-65` | 0.801476001739502 |  | Yes. The color I would give in this -- and this is as you evaluate entering into this business. The reason we are succe… |
| 5 | `chunk_q8fc814:Earnings:chunk-63` | 0.7988513708114624 |  | Sure. So ADIP 2 fundraising, going quite well. We expect to wrap it up this summer in the $4 billion to $5 billion rang… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q8fc814`)._

### ex-eval-chunk-only-chunk-q9fad72

- **example_id**: `eval:chunk-only:chunk_q9fad72`
- **state**: `completed`
- **query**: What guidance was offered on CDW Corporation’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', '10-K', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5= · skipped=missing_stage2_labels · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `chunk_q9fad72:10-Q:chunk-104` | 0.8261058926582336 |  | CDW CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (dollars in millions, except per share data… |
| 2 | `chunk_q9fad72:10-Q:chunk-156` | 0.8172844648361206 |  | CDW CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (dollars in millions, except per share data… |
| 3 | `chunk_q9fad72:10-Q:chunk-166` | 0.8165807723999023 |  | CDW CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (dollars in millions, except per share data… |
| 4 | `chunk_q9fad72:10-Q:chunk-31` | 0.8153531551361084 |  | Item 7. Management’s Discussion and Analysis of Financial Condition and Results of Operations Unless otherwise indicate… |
| 5 | `chunk_q9fad72:10-Q:chunk-95` | 0.815015971660614 |  | CDW CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (dollars in millions, except per share data… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:chunk-only:chunk_q9fad72`)._

### ex-eval-doc-q0617ad

- **example_id**: `eval:doc_q0617ad`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: What did F5’s leadership say about F5’s share repurchase plans?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '8-K', '10-Q', '10-K']`
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
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:doc_q737b56`)._

### ex-eval-doc-qa9fda3

- **example_id**: `eval:doc_qa9fda3`
- **state**: `failed_retriable` · **error**: `empty_top1_chunks`
- **query**: How does The AES Corporation account for currency and economic volatility in its risk management disclosures?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5= · skipped=empty_top1_chunks · n_scored=0

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `eval:doc_qa9fda3`)._
