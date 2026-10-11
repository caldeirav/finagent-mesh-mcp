# Pair `lux-clm` — `paper-n200-full`

[← compact index](../paper-n200-full.inspect.md) · **Download full HTML**: [raw](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) · [`paper-n200-full.inspect.html`](../paper-n200-full.inspect.html)

- eval_run_id: `paper-n200-retry:lux-clm`
- S1=`decision20-lux` · S2=`clm-8b`
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
| 1 | `q075970f6eb46:DEF14A:chunk-44` | 0.3025074005126953 |  | In any period, the number of closings tends to reflect normal churn in our business, whether due to redefining or exiti… |
| 2 | `q075970f6eb46:DEF14A:chunk-2` | 0.25139138102531433 |  | See accompanying Notes to Condensed Consolidated Financial Statements. 1 |
| 3 | `q075970f6eb46:DEF14A:chunk-84` | 0.10053319483995438 |  | ########Nine-month Period###### ####2023####2022####Change## Weighted FASTBin/FASTVend signings (MEUs)####18,664####16,… |
| 4 | `q075970f6eb46:DEF14A:chunk-5` | 0.04911479353904724 |  | See accompanying Notes to Condensed Consolidated Financial Statements. 2 |
| 5 | `q075970f6eb46:DEF14A:chunk-58` | 0.046231579035520554 |  | ########Three-month Period###### ####2023####2022####Change## Weighted FASTBin/FASTVend signings (MEUs)####5,969####5,1… |

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
| 1 | `q0fd4ca04c0a5:10-K:chunk-176` | 0.34921443462371826 |  | The total amount of unrecognized tax benefits at December 31, 2023, 2022 and 2021 that, if recognized, would affect the… |
| 2 | `q0fd4ca04c0a5:10-K:chunk-62` | 0.0399140901863575 |  | Medical claims and benefits payable consist mainly of fee-for-service IBNP, unpaid pharmacy claims, capitation costs, o… |
| 3 | `q0fd4ca04c0a5:10-K:chunk-65` | 0.037126827985048294 |  | Molina Healthcare, Inc. 2023 Form 10-K \| 48 |
| 4 | `q0fd4ca04c0a5:10-K:chunk-145` | 0.03415915369987488 |  | The changes in the carrying amounts of both goodwill and intangible assets, net, in 2023, were due to the Molina Health… |
| 5 | `q0fd4ca04c0a5:10-K:chunk-16` | 0.03085569478571415 |  | plans maintained, and one plan had an increase of 0.5 Stars. The decreases to the 2024 Star Ratings impact the 2025 bon… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q0fd4ca04c0a5`)._

### ex-dev-chunk-only-q299865e6e67e

- **example_id**: `dev:chunk-only:q299865e6e67e`
- **state**: `completed`
- **query**: What dependency risks exist for Consolidated Edison due to concentration of revenue in a limited number of service territories or customer segments?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.05652670087893601 · skipped= · n_scored=286

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q299865e6e67e:10-K:chunk-191` | 0.13075542449951172 |  | ####For the Three Months Ended#### (Millions of Dollars)##September 30, 2023####September 30, 2022##Variation Operating… |
| 2 | `q299865e6e67e:10-K:chunk-184` | 0.08916065096855164 |  | ####For the Three Months Ended September 30, 2023########For the Three Months Ended September 30, 2022###### (Millions … |
| 3 | `q299865e6e67e:10-K:chunk-243` | 0.049827683717012405 | 1.0 | ####For the Nine Months Ended September 30, 2023########For the Nine Months Ended September 30, 2022###### (Millions of… |
| 4 | `q299865e6e67e:10-K:chunk-88` | 0.045864906162023544 |  | ####Con Edison######CECONY## (Millions of Dollars)##2023####2022##2023####2022 Accrued liability – asbestos suits##$8##… |
| 5 | `q299865e6e67e:10-K:chunk-24` | 0.042495518922805786 |  | The accompanying notes are an integral part of these financial statements. 11 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q299865e6e67e`)._

### ex-dev-chunk-only-q2a401c1edf73

- **example_id**: `dev:chunk-only:q2a401c1edf73`
- **state**: `completed`
- **query**: How often is Exxon Mobil Corporation’s executive compensation program reviewed and updated?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.360054614577234 · skipped= · n_scored=142

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2a401c1edf73:DEF14A:chunk-29` | 0.2524411082267761 |  | # Table of Contents <table><tr><th>Director &amp; key qualifications</th><th></th><th></th><th></th><th></th><th></th><… |
| 2 | `q2a401c1edf73:DEF14A:chunk-54` | 0.20088239014148712 | 2.0 | # Table of Contents (cont.) ## COMPENSATION COMMITTEE REPORT The Compensation Committee of the Board of Directors has r… |
| 3 | `q2a401c1edf73:DEF14A:chunk-136` | 0.17657984793186188 |  | # Table of Contents (cont.) ## Earnings (loss) excluding Identified Items (Non-GAAP) (cont.) <table><tr><th>Upstream (m… |
| 4 | `q2a401c1edf73:DEF14A:chunk-84` | 0.10231049358844757 | 2.0 | # EXECUTIVE COMPENSATION TABLES (cont.) ## TOTAL DIRECT COMPENSATION The following pro forma table displays total direc… |
| 5 | `q2a401c1edf73:DEF14A:chunk-85` | 0.05073902755975723 |  | # Table of Contents (cont.) For Ms. Mikells, the amount in the Summary Compensation Table for 2021 also includes an ini… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q2a401c1edf73`)._

### ex-dev-chunk-only-q3a71644741b7

- **example_id**: `dev:chunk-only:q3a71644741b7`
- **state**: `completed`
- **query**: What questions were asked about Conagra Brands’ customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.2577212905719748 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3a71644741b7:Earnings:chunk-43` | 0.31220898032188416 |  | That's helpful. And then Sean, just kind of thinking about the productivity number, and it's a question being asked of … |
| 2 | `q3a71644741b7:Earnings:chunk-77` | 0.2859220504760742 | 2.0 | I just wanted to clarify on promotional activity and other types of brand building that you've referenced. How does the… |
| 3 | `q3a71644741b7:Earnings:chunk-27` | 0.047231897711753845 |  | I wanted just to ask you about the challenging environment comments. You made that comment a few times during the prepa… |
| 4 | `q3a71644741b7:Earnings:chunk-97` | 0.035746678709983826 |  | Great. I guess, Sean, just to come back to the Grocery, maybe more staples business, it does seem like it's lagging a l… |
| 5 | `q3a71644741b7:Earnings:chunk-79` | 0.03352036327123642 | 1.0 | I would say on the categories that where we've invested, the lifts have been better. And the way I describe that to fol… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q3a71644741b7`)._

### ex-dev-chunk-only-q40d417892141

- **example_id**: `dev:chunk-only:q40d417892141`
- **state**: `completed`
- **query**: What investor views emerged on D.R. Horton’s geographic expansion prospects within new U.S. housing markets?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.13120507751234178 · skipped= · n_scored=27

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q40d417892141:Earnings:chunk-3` | 0.9478538632392883 |  | Forestar Group Inc. (NYSE:FOR) (“Forestar”) is a publicly traded residential lot development company that is a majority… |
| 2 | `q40d417892141:Earnings:chunk-5` | 0.012610485777258873 |  | Forward-looking statements in this release include that we are well-positioned to meet changing market conditions with … |
| 3 | `q40d417892141:Earnings:chunk-13` | 0.012225090526044369 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 4 | `q40d417892141:Earnings:chunk-18` | 0.011885315179824829 |  | [Chunk Index 19] <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><… |
| 5 | `q40d417892141:Earnings:chunk-27` | 0.002767589408904314 | 1.0 | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q40d417892141`)._

### ex-dev-chunk-only-q504aef305d62

- **example_id**: `dev:chunk-only:q504aef305d62`
- **state**: `completed`
- **query**: How did management describe the performance of the China market in Q4 2023?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q504aef305d62:Earnings:chunk-6` | 0.08676671981811523 |  | Rachel Ruggeri - Executives |
| 2 | `q504aef305d62:Earnings:chunk-22` | 0.0862853154540062 |  | Rachel Ruggeri - Executives |
| 3 | `q504aef305d62:Earnings:chunk-28` | 0.08386700600385666 |  | Rachel Ruggeri - Executives |
| 4 | `q504aef305d62:Earnings:chunk-36` | 0.08336495608091354 |  | Rachel Ruggeri - Executives |
| 5 | `q504aef305d62:Earnings:chunk-46` | 0.0812840536236763 |  | Rachel Ruggeri - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q504aef305d62`)._

### ex-dev-chunk-only-q5bb4a350edd8

- **example_id**: `dev:chunk-only:q5bb4a350edd8`
- **state**: `completed`
- **query**: How has aircraft delivery volume trended across the last four quarters for the F 35 program?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.33916020527361607 · skipped= · n_scored=98

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5bb4a350edd8:10-Q:chunk-5` | 0.15663570165634155 | 2.0 | Thanks, Maria. Good morning, everyone, and thank you for joining us on our fourth quarter and full year 2023 earnings c… |
| 2 | `q5bb4a350edd8:10-Q:chunk-11` | 0.12100959569215775 |  | I was hoping to lead off with Aero and F-35 in particular, and the margins, number one, that you're looking for in '24 … |
| 3 | `q5bb4a350edd8:10-Q:chunk-49` | 0.0699060708284378 |  | Look -- it's -- Doug, it's Jim. I think we can continue at this rate. Demand from the U.S. service and our internationa… |
| 4 | `q5bb4a350edd8:10-Q:chunk-39` | 0.04598107933998108 |  | Jay, just a quick clarification then one for Jim and sorry if I missed this, but the deliveries that you're expecting f… |
| 5 | `q5bb4a350edd8:10-Q:chunk-43` | 0.04204879328608513 |  | Yes. Sure, Jay. So look, there's a near-term and a long-term approach that we're taking to government contracting with … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q5bb4a350edd8`)._

### ex-dev-chunk-only-q7b219decf5da

- **example_id**: `dev:chunk-only:q7b219decf5da`
- **state**: `completed`
- **query**: What did Everest Group, Ltd.’s leadership say about Everest Group, Ltd.’s dividend policy?
- **S1**: top1=`DEF14A` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['DEF14A', 'Earnings', '10-K', '10-Q', '8-K']`
- **S2**: nDCG@5=0.33916020527361607 · skipped= · n_scored=138

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7b219decf5da:DEF14A:chunk-119` | 0.08183735609054565 | 2.0 | Mike, it's Mark. The first point that I would make is we have ample capital. There's a lot of capital that we have at o… |
| 2 | `q7b219decf5da:DEF14A:chunk-89` | 0.048846535384655 |  | Greg, it's Mark. I'll just add another point to it. I do think that you will see a movement to the right on that slide … |
| 3 | `q7b219decf5da:DEF14A:chunk-4` | 0.042177554219961166 |  | Juan Carlos Andrade - Executives |
| 4 | `q7b219decf5da:DEF14A:chunk-16` | 0.0405886135995388 |  | Juan Carlos Andrade - Executives |
| 5 | `q7b219decf5da:DEF14A:chunk-32` | 0.040460534393787384 |  | Juan Carlos Andrade - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q7b219decf5da`)._

### ex-dev-chunk-only-q7ca4de540868

- **example_id**: `dev:chunk-only:q7ca4de540868`
- **state**: `completed`
- **query**: How does Hologic view the pace of innovation cycles in women's health diagnostics and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.16958010263680803 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ca4de540868:10-K:chunk-87` | 0.48108765482902527 | 1.0 | # MR. GRIFFIN (cont.) ## Performance Objectives and Outcomes Mr. Griffin's individual performance objectives were desig… |
| 2 | `q7ca4de540868:10-K:chunk-97` | 0.17202921211719513 |  | # Summary of Performance of Fiscal 2020 and Fiscal 2021 PSUs (cont.) ## THE ROLE OF THE INDEPENDENT COMPENSATION CONSUL… |
| 3 | `q7ca4de540868:10-K:chunk-85` | 0.09990814328193665 | 1.0 | # MS. OBERTON (cont.) ## Performance Objectives and Outcomes Ms. Oberton's individual performance objectives were desig… |
| 4 | `q7ca4de540868:10-K:chunk-86` | 0.07411186397075653 |  | # MS. OBERTON (cont.) ## Performance Objectives and Outcomes Mr. Mitchell's individual performance objectives were desi… |
| 5 | `q7ca4de540868:10-K:chunk-84` | 0.03130346164107323 |  | # Individual Bonus Opportunity Ranges (1) (cont.) ## Performance Objectives and Outcomes Mr. MacMillan's individual per… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q7ca4de540868`)._

### ex-dev-chunk-only-q7ff47a7d2a20

- **example_id**: `dev:chunk-only:q7ff47a7d2a20`
- **state**: `completed`
- **query**: How does Consolidated Edison, Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=212

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7ff47a7d2a20:10-K:chunk-155` | 0.29231688380241394 |  | # PAY VERSUS PERFORMANCE (cont.) ## Relationship between CAP and Company Performance For all charts below, 2020 CEO Com… |
| 2 | `q7ff47a7d2a20:10-K:chunk-107` | 0.10593803226947784 |  | # Long-Term Incentive Compensation (cont.) ## Footnote: (1) Interpolated for actual performance between minimum, target… |
| 3 | `q7ff47a7d2a20:10-K:chunk-85` | 0.06694363057613373 |  | # Median Level Compensation In 2023, the target total direct compensation awarded to the Named Executive Officers was c… |
| 4 | `q7ff47a7d2a20:10-K:chunk-96` | 0.06664067506790161 |  | # Median Level Compensation (cont.) ## Footnotes: (1) The payout relative to the operating budget target is interpolate… |
| 5 | `q7ff47a7d2a20:10-K:chunk-101` | 0.05804504454135895 |  | # Achievement of 2023 Financial and Operating Objectives The following table shows, for each Named Executive Officer, w… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q7ff47a7d2a20`)._

### ex-dev-chunk-only-q853c16a74704

- **example_id**: `dev:chunk-only:q853c16a74704`
- **state**: `completed`
- **query**: What did Tapestry’s management say about Tapestry’s margin outlook and initiatives to improve profitability?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.2512232823714198 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q853c16a74704:Earnings:chunk-39` | 0.13150286674499512 |  | I wanted to touch on Kate Spade for a minute. You spoke of a need to amplify the efforts there through holistic marketi… |
| 2 | `q853c16a74704:Earnings:chunk-53` | 0.10923971980810165 | 1.0 | Just a quick one on another question. Just you said flat in the quarter, but it was largely geography mix. Maybe where … |
| 3 | `q853c16a74704:Earnings:chunk-21` | 0.09852152317762375 |  | So similar to Bob, just a question around the deal. I guess just, Scott, you kind of alluded to it to Bob's question an… |
| 4 | `q853c16a74704:Earnings:chunk-29` | 0.08000170439481735 | 1.0 | Great. So Joanne, could you elaborate on current health of the Coach brand in North America? Maybe any changes in custo… |
| 5 | `q853c16a74704:Earnings:chunk-25` | 0.04608319699764252 | 2.0 | Yes, sure. So while Plan A is our priority, should we find ourselves in the plan B scenario, a couple of things I'd jus… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q853c16a74704`)._

### ex-dev-chunk-only-q90faabe2b483

- **example_id**: `dev:chunk-only:q90faabe2b483`
- **state**: `completed`
- **query**: What operational risks related to technology or IT systems has UDR, Inc. highlighted, and how are these managed?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.14606834984270645 · skipped= · n_scored=31

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q90faabe2b483:10-K:chunk-29` | 0.49317216873168945 |  | # DEFINITIONS AND RECONCILIATIONS (cont.) <table><tr><th rowspan="2">In thousands, except per share and unit amounts</t… |
| 2 | `q90faabe2b483:10-K:chunk-6` | 0.1547316014766693 |  | # ACCRETIVE CAPITAL ALLOCATION UDR has a track record of being a proficient steward of capital and can utilize various … |
| 3 | `q90faabe2b483:10-K:chunk-8` | 0.0938986986875534 |  | # RECENT EXTERNAL GROWTH ACTIVITY (cont.) ## LaSalle Joint Venture ## Texas Acquisitions i Deal Specifics Contributed 4… |
| 4 | `q90faabe2b483:10-K:chunk-30` | 0.052254818379879 | 1.0 | # FORWARD LOOKING STATEMENTS Certain statements made in this presentation may constitute "forward-looking statements." … |
| 5 | `q90faabe2b483:10-K:chunk-2` | 0.04143034666776657 |  | # UDR AT A GLANCE (1)(2) UDR is a full-cycle investment that consistently generates strong total shareholder return ("T… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q90faabe2b483`)._

### ex-dev-chunk-only-q9ee9b517f484

- **example_id**: `dev:chunk-only:q9ee9b517f484`
- **state**: `completed`
- **query**: What feedback have investors provided regarding Valero Energy Corporation’s refining margin outlook?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=203

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9ee9b517f484:Earnings:chunk-2` | 0.3538949489593506 |  | See Condensed Notes to Consolidated Financial Statements. 1 |
| 2 | `q9ee9b517f484:Earnings:chunk-5` | 0.10129035264253616 |  | See Condensed Notes to Consolidated Financial Statements. 2 |
| 3 | `q9ee9b517f484:Earnings:chunk-47` | 0.05947776138782501 |  | Nonconsolidated VIEs We hold variable interests in VIEs that have not been consolidated because we are not considered t… |
| 4 | `q9ee9b517f484:Earnings:chunk-85` | 0.04505229368805885 |  | The securities categorized in Level 1 are measured at fair value using a market approach based on quoted prices from na… |
| 5 | `q9ee9b517f484:Earnings:chunk-98` | 0.038506317883729935 |  | Derivatives Not Designated as Hedging Instruments##Location of Gain (Loss) Recognized in Income on Derivatives######Thr… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:q9ee9b517f484`)._

### ex-dev-chunk-only-qa431f3f55a5e

- **example_id**: `dev:chunk-only:qa431f3f55a5e`
- **state**: `completed`
- **query**: How are scenario analyses conducted by EPAM Systems, Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=252

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa431f3f55a5e:10-K:chunk-29` | 0.0916137844324112 |  | Company/Index####Base period 12/31/2018####12/31/2019####12/31/2020####12/31/2021####12/31/2022####12/31/2023 EPAM Syst… |
| 2 | `qa431f3f55a5e:10-K:chunk-143` | 0.07743799686431885 |  | ####Amount Contingent consideration liabilities as of January 1, 2021##$##7,470 Acquisition date fair value of continge… |
| 3 | `qa431f3f55a5e:10-K:chunk-207` | 0.050678059458732605 |  | ####Equity-Classified Restricted Stock########Equity-Classified Equity-Settled Restricted Stock Units########Liability-… |
| 4 | `qa431f3f55a5e:10-K:chunk-242` | 0.04660549387335777 |  | ####As of December 31, 2023####As of December 31, 2022####As of December 31, 2021 Ukraine##$##62,653##$##70,183##$##78,… |
| 5 | `qa431f3f55a5e:10-K:chunk-202` | 0.043802108615636826 |  | ##Number of Options####Weighted Average Exercise Price####Aggregate Intrinsic Value##Weighted Average Remaining Contrac… |

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
| 1 | `qaf2d41946676:10-K:chunk-119` | 0.8210048675537109 |  | The Crown Rock acquisition stood on its own in terms of quality and how it fit within our portfolio in the Midland Basi… |
| 2 | `qaf2d41946676:10-K:chunk-95` | 0.01144260074943304 |  | Yes. I think just from a permit standpoint, it's been very productive over the last couple of years. So we stand today … |
| 3 | `qaf2d41946676:10-K:chunk-87` | 0.008391648530960083 | 1.0 | Yes. So when we think about capital allocation in the oil and gas segment, what you're trying to do is we're trying to … |
| 4 | `qaf2d41946676:10-K:chunk-47` | 0.006720858626067638 |  | Yes. So one of the main drivers for the relatively lower guidance for this year is an assumption on the spread for the … |
| 5 | `qaf2d41946676:10-K:chunk-21` | 0.005945260636508465 |  | It's Ken here. Maybe I can add a couple of things. So we feeling pretty good about the date. And for example, we're sen… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qaf2d41946676`)._

### ex-dev-chunk-only-qb3a6bec7aedc

- **example_id**: `dev:chunk-only:qb3a6bec7aedc`
- **state**: `completed`
- **query**: What exposure to foreign exchange fluctuations did Citizens Financial Group, Inc. disclose and how is Citizens Financial Group, Inc. managing it?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=423

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb3a6bec7aedc:10-K:chunk-418` | 0.06226436421275139 |  | ##CITIZENS FINANCIAL GROUP, INC.## ##(Registrant)## By:####/s/ Bruce Van Saun ####Name: Bruce Van Saun ####Title: Chair… |
| 2 | `qb3a6bec7aedc:10-K:chunk-30` | 0.05919488146901131 |  | ##12/31/2023##12/31/2022##12/31/2021##12/31/2020##12/31/2019##12/31/2018 CFG##$140##$157##$181##$132##$142##$100 S&P 50… |
| 3 | `qb3a6bec7aedc:10-K:chunk-91` | 0.050191495567560196 |  | CAPITAL AND REGULATORY MATTERS As a BHC and FHC, we are subject to regulation and supervision by the FRB. Our banking s… |
| 4 | `qb3a6bec7aedc:10-K:chunk-77` | 0.03873899206519127 |  | ##Table 16: Commercial Real Estate by Property Type and State############## ####December 31, 2023########December 31, 2… |
| 5 | `qb3a6bec7aedc:10-K:chunk-102` | 0.034665316343307495 |  | Table 26: Credit Ratings###### ####December 31, 2023## ##Moody’s##Standard and Poor’s##Fitch Citizens Financial Group, … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qb3a6bec7aedc`)._

### ex-dev-chunk-only-qb7d1dfae8271

- **example_id**: `dev:chunk-only:qb7d1dfae8271`
- **state**: `completed`
- **query**: What guidance was offered on International Flavors & Fragrances Inc.’s inventory or supply chain efficiency targets?
- **S1**: top1=`10-Q` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=304

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb7d1dfae8271:10-Q:chunk-246` | 0.142613485455513 |  | 99 |
| 2 | `qb7d1dfae8271:10-Q:chunk-283` | 0.11946091800928116 |  | 111 |
| 3 | `qb7d1dfae8271:10-Q:chunk-261` | 0.0641946792602539 |  | _______________________ (1)The foreign currency contract net gains (losses) offset any recognized gains (losses) arisin… |
| 4 | `qb7d1dfae8271:10-Q:chunk-34` | 0.05069265887141228 |  | Year-end Data####2018####2019####2020####2021####2022####2023 International Flavors & Fragrances##$##100.00##$##98.30##… |
| 5 | `qb7d1dfae8271:10-Q:chunk-103` | 0.033643096685409546 |  | The unaudited pro forma results for the year ended December 31, 2021 were as follows: |

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
| 1 | `qbcda53de470c:DEF14A:chunk-85` | 0.07708001136779785 |  | I have 2 of them, too. First one, Luca, thanks for the color on gross margin. And when I look at it over the last 4 qua… |
| 2 | `qbcda53de470c:DEF14A:chunk-23` | 0.06782698631286621 |  | Congratulations on the execution in the quarter. I'm curious, Tim, if you could help us characterize what the demand en… |
| 3 | `qbcda53de470c:DEF14A:chunk-43` | 0.0639304667711258 |  | I know you covered China. I want to pivot to the U.S. for a second. Obviously, iPhone and the business looks like it re… |
| 4 | `qbcda53de470c:DEF14A:chunk-55` | 0.03385860100388527 |  | I have 2 as well. I guess first off, just the Services growth rate, there was a tremendous acceleration, I think, in Se… |
| 5 | `qbcda53de470c:DEF14A:chunk-33` | 0.03288744017481804 |  | Maybe if I start -- Luca, I know that the iPhone 15 Pro and Pro Max are constrained today, but I think some of your com… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qbcda53de470c`)._

### ex-dev-chunk-only-qd7ede96b88aa

- **example_id**: `dev:chunk-only:qd7ede96b88aa`
- **state**: `completed`
- **query**: What observations were made about TransDigm Group’s market share trends or competitive positioning in the aerospace components sector?
- **S1**: top1=`Earnings` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd7ede96b88aa:Earnings:chunk-76` | 0.3141545057296753 |  | # Option Holders Would Lose Value After a Dividend If They Did Not Receive DEPs (cont.) ## Shareholder Engagement Summa… |
| 2 | `qd7ede96b88aa:Earnings:chunk-96` | 0.10421132296323776 |  | # Executive Compensation (cont.) ## Pay Versus Performance (cont.) (2) Compensation Actually Paid to our PEO reflects t… |
| 3 | `qd7ede96b88aa:Earnings:chunk-64` | 0.08291859924793243 |  | # Executive Compensation (cont.) ## Executive Compensation (cont.) Annual Cash Incentive Percentage <table> <tr> <th>Pe… |
| 4 | `qd7ede96b88aa:Earnings:chunk-61` | 0.06722065061330795 |  | # Executive Compensation (cont.) ## 2024 NEO Compensation Our executive compensation program is designed to motivate an… |
| 5 | `qd7ede96b88aa:Earnings:chunk-19` | 0.0485718734562397 |  | # Nominating and Corporate Governance Committee (cont.) ## Corporate Governance Policies and Practices TransDigm's gove… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qd7ede96b88aa`)._

### ex-dev-chunk-only-qddfea8300793

- **example_id**: `dev:chunk-only:qddfea8300793`
- **state**: `completed`
- **query**: How does Chesapeake Energy view the pace of technological advancements in drilling techniques and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=345

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qddfea8300793:10-K:chunk-88` | 0.15249070525169373 |  | ######Successor#### ######Year Ended December 31,#### ####2023######2022 Total G&A, net##$##127####$##142 G&A, net per … |
| 2 | `qddfea8300793:10-K:chunk-250` | 0.05761438235640526 |  | ######Successor#### ####December 31, 2023######December 31, 2022 Natural gas, oil and NGL sales##$##406####$##1,171 Joi… |
| 3 | `qddfea8300793:10-K:chunk-289` | 0.052860550582408905 |  | ##########Successor######## ####December 31, 2023##########December 31, 2022#### ##Notional Volume######Fair Value####N… |
| 4 | `qddfea8300793:10-K:chunk-84` | 0.04578942060470581 |  | ######Successor#### ######Year Ended December 31,#### ####2023######2022 Natural gas derivatives - realized gains (loss… |
| 5 | `qddfea8300793:10-K:chunk-21` | 0.04347079247236252 |  | ####Developed Leasehold######Undeveloped Leasehold######Total## ##Gross Acres####Net Acres##Gross Acres####Net Acres##G… |

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
| 1 | `qed0361d5a9ae:Earnings:chunk-22` | 0.5906198620796204 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 7 |
| 2 | `qed0361d5a9ae:Earnings:chunk-33` | 0.1616942286491394 |  | Apple Inc. \| Q3 2023 Form 10-Q \| 9 |
| 3 | `qed0361d5a9ae:Earnings:chunk-50` | 0.03875476121902466 |  | Contingencies The Company is subject to various legal proceedings and claims that have arisen in the ordinary course of… |
| 4 | `qed0361d5a9ae:Earnings:chunk-17` | 0.03155779838562012 |  | Approximately 32 million restricted stock units (“RSUs”) were excluded from the computation of diluted earnings per sha… |
| 5 | `qed0361d5a9ae:Earnings:chunk-14` | 0.019324520602822304 |  | See accompanying Notes to Condensed Consolidated Financial Statements. Apple Inc. \| Q3 2023 Form 10-Q \| 5 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:chunk-only:qed0361d5a9ae`)._

### ex-dev-chunk-only-qeeb1c1a41ae3

- **example_id**: `dev:chunk-only:qeeb1c1a41ae3`
- **state**: `completed`
- **query**: What dependency risks exist for DuPont de Nemours, Inc. due to concentration of revenue in a limited number of end-use industries such as automotive or electronics?
- **S1**: top1=`10-K` in_gold=False · nDCG@5= · gold=[]
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=112

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeeb1c1a41ae3:10-K:chunk-59` | 0.338894784450531 |  | # Table of Contents # Compensation Discussion & Analysis ## 2023 PSU Awards PSU awards are designed to align executive … |
| 2 | `qeeb1c1a41ae3:10-K:chunk-5` | 0.1163143590092659 |  | # Director Nominees (cont.) <table><tr><th>(As of the date of this Proxy Statement) Name Age Current Position</th><th>I… |
| 3 | `qeeb1c1a41ae3:10-K:chunk-13` | 0.10293979197740555 |  | # Committees (cont.) ## Committees <table><tr><th rowspan="8">Audit Committee Held nine meetings during 2023.</th><th>N… |
| 4 | `qeeb1c1a41ae3:10-K:chunk-52` | 0.07810987532138824 |  | # 2023 Executive Compensation Decisions (cont.) ## Segment Adjusted Free Cash Flow* Cash provided by/(used for) operati… |
| 5 | `qeeb1c1a41ae3:10-K:chunk-15` | 0.05149766057729721 |  | # Table of Contents (cont.) ## Board's Role in the Oversight of Risk Management The Board is responsible for overseeing… |

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
| 1 | `qf3b87e3d287f:10-K:chunk-22` | 0.21914216876029968 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 2 | `qf3b87e3d287f:10-K:chunk-19` | 0.14082354307174683 |  | 1) Includes the quarterly results of a business that has met the held-for-sale criteria since December 31, 2023. BIO-TE… |
| 3 | `qf3b87e3d287f:10-K:chunk-6` | 0.12254228442907333 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 4 | `qf3b87e3d287f:10-K:chunk-12` | 0.096920445561409 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 5 | `qf3b87e3d287f:10-K:chunk-20` | 0.06906908005475998 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

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
| 1 | `qf59bea60dc8d:DEF14A:chunk-58` | 0.7083926796913147 |  | At September 30, 2023, the remaining authorized amount for share repurchases under the Repurchase Program was approxima… |
| 2 | `qf59bea60dc8d:DEF14A:chunk-123` | 0.04718514159321785 |  | ####Ratings#### ##Senior Long-term Debt####Commercial Paper##Outlook Standard & Poor’s##A-####A-2##Stable Moody’s Inves… |
| 3 | `qf59bea60dc8d:DEF14A:chunk-21` | 0.02331702969968319 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |
| 4 | `qf59bea60dc8d:DEF14A:chunk-20` | 0.020865878090262413 |  | Consolidated revenue from contracts with customers by geographic area, which is attributed on the basis of where the se… |
| 5 | `qf59bea60dc8d:DEF14A:chunk-8` | 0.015855133533477783 |  | See accompanying Notes to Condensed Consolidated Financial Statements (Unaudited). 8 |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=160

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0346b2bc5a8b:chunk-149` | 0.1482633799314499 |  | I was just wondering with your announced price increase, to be effective January 1, if you maybe saw some demand get pu… |
| 2 | `q0346b2bc5a8b:chunk-5` | 0.11271433532238007 |  | Thank you, Mark. As Mark mentioned, Packaging segment volume for the quarter exceeded our guidance estimates. Corrugate… |
| 3 | `q0346b2bc5a8b:chunk-33` | 0.10222902148962021 |  | Congrats on a really good quarter. Just wanted to get a sense from you regarding the mix in 4Q. Box prices looked like … |
| 4 | `q0346b2bc5a8b:chunk-47` | 0.05613495782017708 |  | I think our mix will be traditional to what we typically have. |
| 5 | `q0346b2bc5a8b:chunk-69` | 0.04383033141493797 |  | Okay. And then maybe 2 questions on the Jackson conversion. It sounds like -- I know sometimes that they're not always … |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=315

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q05bfc5cb3e17:chunk-58` | 0.15644177794456482 |  | Note: Segment results are stated on an FTE basis. The FTE adjustments are eliminated in the reconciling items column wi… |
| 2 | `q05bfc5cb3e17:chunk-83` | 0.1485050469636917 |  | For an overall discussion on the loan portfolio and on the allowance, refer to Note 5—Loans and Note 6—Allowance for Cr… |
| 3 | `q05bfc5cb3e17:chunk-103` | 0.13528195023536682 |  | FORWARD-LOOKING STATEMENTS This report may include statements which constitute “forward-looking statements” within the … |
| 4 | `q05bfc5cb3e17:chunk-32` | 0.12151485681533813 |  | (1)Interest-Bearing Due from and Deposits with Banks includes the interest-bearing component of Cash and Due from Banks… |
| 5 | `q05bfc5cb3e17:chunk-3` | 0.043334148824214935 |  | Asset Servicing Custody and Fund Administration fees, the largest component of Asset Servicing fees, are driven primari… |

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
| 1 | `q09b8cfa51b60:chunk-52` | 0.14113904535770416 |  | Category##Classification####September 30, 2023####December 31, 2022 Assets########## Operating##Operating lease assets#… |
| 2 | `q09b8cfa51b60:chunk-2` | 0.09631016850471497 |  | The accompanying notes are an integral part of these consolidated financial statements. 1 |
| 3 | `q09b8cfa51b60:chunk-88` | 0.08230620622634888 |  | Core EBITDA is calculated as follows (dollars in thousands): |
| 4 | `q09b8cfa51b60:chunk-46` | 0.0720634013414383 |  | _______________ (1)Included in net (loss) income are realized and unrealized earnings and losses in investments in unco… |
| 5 | `q09b8cfa51b60:chunk-4` | 0.04232891649007797 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |

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
| 1 | `q0b8d55d58be2:chunk-79` | 0.1541324257850647 |  | NOTES TO CONSOLIDATED FINANCIAL STATEMENTS – continued (Unaudited) Chubb Limited and Subsidiaries Derivatives designate… |
| 2 | `q0b8d55d58be2:chunk-120` | 0.0673099160194397 |  | (1)Recognized in Policy acquisition costs in the Consolidated statements of operations. (2)Recognized in Other (income)… |
| 3 | `q0b8d55d58be2:chunk-68` | 0.04611760750412941 |  | ##Expected Liquidation Period of Underlying Assets######September 30, 2023##########December 31, 2022#### (in millions … |
| 4 | `q0b8d55d58be2:chunk-16` | 0.03647569566965103 |  | Excluded from the table above is the reclassification of Separate account assets, Separate account liabilities, and Pol… |
| 5 | `q0b8d55d58be2:chunk-297` | 0.034224990755319595 |  | 88 |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q0faf9d780cdc:chunk-99` | 0.13167497515678406 |  | ####Common Stock######Additional Paid-In Capital####Retained Earnings######Accumulated Other Comprehensive Loss######To… |
| 2 | `q0faf9d780cdc:chunk-11` | 0.07386113703250885 |  | contracts and orders. In addition, the U.S. Government could terminate a prime contract under which we are a subcontrac… |
| 3 | `q0faf9d780cdc:chunk-74` | 0.07319177687168121 |  | ####Total Commitment####Less Than 1 Year Standby letters of credit (a)##$##2,546##$##1,234 Surety bonds####354####354 T… |
| 4 | `q0faf9d780cdc:chunk-120` | 0.06731832772493362 |  | ############2023######## ####Aeronautics####MFC####RMS####Space####Total Net sales#################### Products##$##22,… |
| 5 | `q0faf9d780cdc:chunk-5` | 0.05348598212003708 |  | (a)Based on employees who self-identify. Includes only U.S. employees and expatriates except for data relating to women… |

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
| 1 | `q11ef281af9cd:chunk-189` | 0.27595284581184387 |  | ####First Quarter####Second Quarter####Third Quarter####Fourth Quarter####Full Year For the year ended December 31, 202… |
| 2 | `q11ef281af9cd:chunk-114` | 0.10622809827327728 |  | ####General rentals######Specialty######Total## 2023################## Equipment rentals##$####8,803##$####3,261##$####… |
| 3 | `q11ef281af9cd:chunk-51` | 0.08347310870885849 |  | ####General rentals####Specialty####Total Year Ended December 31, 2023############ Equipment rentals##$##8,803##$##3,26… |
| 4 | `q11ef281af9cd:chunk-47` | 0.061296045780181885 |  | To the extent that the useful lives of all of our rental equipment were to increase or decrease by one year, we estimat… |
| 5 | `q11ef281af9cd:chunk-194` | 0.04830555245280266 |  | Description####Balance at Beginning of Period####Charged to Costs and Expenses######Charged to Revenue######Deductions … |

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
- **S2**: nDCG@5=0.38722694780001 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q1ded233d05aa:chunk-23` | 0.22849006950855255 |  | Congrats on the quarter, strong end to the year. I wanted to expand a little bit on the inVue. You guys had a great lau… |
| 2 | `q1ded233d05aa:chunk-33` | 0.08438417315483093 |  | Just a follow-up on inVue, if you could provide maybe the early KOL feedback regarding the slide-free and load-and-go t… |
| 3 | `q1ded233d05aa:chunk-55` | 0.06561926752328873 | 2.0 | Okay. So just on the first one, maybe a simple way to understand this is post Q1, we're, I think I said this in my comm… |
| 4 | `q1ded233d05aa:chunk-53` | 0.056889668107032776 | 2.0 | Okay. Great. That was very helpful. And then just sort of a long second question, more clarification. So it seems like … |
| 5 | `q1ded233d05aa:chunk-2` | 0.0373724028468132 |  | Brian McKeon - Executives |

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
| 1 | `q2173e7c263c1:chunk-95` | 0.23820748925209045 |  | Three months ended September 30, 2023## Properties available for lease at June 30, 2023##137 Lease expirations (1)##310… |
| 2 | `q2173e7c263c1:chunk-142` | 0.1378725916147232 |  | ######Three months ended September 30,##########Nine months ended September 30,#### ####2023######2022####2023######202… |
| 3 | `q2173e7c263c1:chunk-136` | 0.06714992225170135 |  | ######Three months ended September 30,##########Nine months ended September 30,#### ####2023######2022####2023######202… |
| 4 | `q2173e7c263c1:chunk-27` | 0.055140331387519836 |  | (1)The initial weighted average cash lease yield for a property is generally computed as estimated contractual first ye… |
| 5 | `q2173e7c263c1:chunk-37` | 0.042422469705343246 |  | As Of##Number of Properties (1)##Weighted Average Stated Interest Rate (2)####Weighted Average Effective Interest Rate … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2173e7c263c1`)._

### ex-dev-q238a8429d152

- **example_id**: `dev:q238a8429d152`
- **state**: `completed`
- **query**: How does Dominion Energy view the pace of innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9734136950814526 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=209

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q238a8429d152:chunk-160` | 0.3656291961669922 |  | # Your Board of Directors recommends that you vote AGAINST this item. (cont.) ## Your Board of Directors recommends tha… |
| 2 | `q238a8429d152:chunk-68` | 0.08651208132505417 |  | # Compensation Discussion and Analysis (cont.) ## Financial Performance - We achieved reported earnings of $2.29 per sh… |
| 3 | `q238a8429d152:chunk-92` | 0.08325468003749847 |  | # 2023 Companywide Operating & Stewardship Goals (cont.) ## The Compensation Peer Group The CTD Committee uses the Comp… |
| 4 | `q238a8429d152:chunk-113` | 0.07248111069202423 |  | # Grants of Plan-Based Awards (cont.) ## Outstanding Equity Awards at Fiscal Year-End The following table summarizes eq… |
| 5 | `q238a8429d152:chunk-67` | 0.0598730705678463 |  | # Compensation Discussion and Analysis (cont.) ## Business Highlights Our 2023 business highlights include the followin… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q238a8429d152`)._

### ex-dev-q2451f8377cf4

- **example_id**: `dev:q2451f8377cf4`
- **state**: `completed`
- **query**: What dependency risks exist for Pool Corporation due to concentration of revenue in specific geographic regions or major pool supply distributors?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3077256276560777 · skipped= · n_scored=144

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2451f8377cf4:chunk-35` | 0.12808622419834137 |  | Just so we have this information on one place, could you give us base business volume and price across blue, green, and… |
| 2 | `q2451f8377cf4:chunk-11` | 0.09211181849241257 |  | Thanks for all the details on the guidance. I think what I want to do is just talk about the first quarter because ther… |
| 3 | `q2451f8377cf4:chunk-7` | 0.07871396094560623 | 1.0 | Thank you, Pete. Good morning, everyone. I'll begin our fourth quarter results, move into how we finished out 2023 and … |
| 4 | `q2451f8377cf4:chunk-121` | 0.04654938727617264 | 2.0 | Yes. I think you really -- you have to go deeper than just seasonal and year-round. Garik, I think you got to look at s… |
| 5 | `q2451f8377cf4:chunk-25` | 0.025161227211356163 |  | My first question, Pete, is I'd like to talk a little bit about the operating environment as you're coming into this ye… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2451f8377cf4`)._

### ex-dev-q24d0f908cfe3

- **example_id**: `dev:q24d0f908cfe3`
- **state**: `completed`
- **query**: What guidance was offered on Fox Corporation’s advertising revenue growth targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9278143341459562 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.6131471927654584 · skipped= · n_scored=111

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q24d0f908cfe3:chunk-62` | 0.21113085746765137 | 1.0 | # COMPENSATION DISCUSSION AND ANALYSIS <table><tr><th>Qualitative Performance Factor</th><th>Fiscal 2023 Achievements</… |
| 2 | `q24d0f908cfe3:chunk-39` | 0.15370750427246094 |  | # CORPORATE CULTURE AND SOCIAL RESPONSIBILITY (cont.) ## CORPORATE CULTURE AND SOCIAL RESPONSIBILITY Creating and maint… |
| 3 | `q24d0f908cfe3:chunk-7` | 0.15222449600696564 |  | # Board Nominees (cont.) ## Fiscal 2023 Business Highlights (cont.) - In fiscal 2023, Tubi delivered record revenues, w… |
| 4 | `q24d0f908cfe3:chunk-103` | 0.0643797293305397 |  | # INFORMATION ABOUT THE ANNUAL MEETING (cont.) ## Voting and Submission of Proxies The persons named on the proxy card … |
| 5 | `q24d0f908cfe3:chunk-20` | 0.04164071008563042 |  | # CORPORATE GOVERNANCE (cont.) - our total federal lobbying expenses of $3.8 million; - the federal public policy matte… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q24d0f908cfe3`)._

### ex-dev-q25119b32a2f9

- **example_id**: `dev:q25119b32a2f9`
- **state**: `completed`
- **query**: What performance metrics does Snap-on Incorporated use to establish annual cash incentives or bonuses?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9882048111454694 · gold=['DEF14A', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['DEF14A', '10-K', 'Earnings', '10-Q', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=21

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q25119b32a2f9:chunk-7` | 0.5098487734794617 |  | <table> <tr> <td colspan="16">SNAP-ON INCORPORATED Supplemental Segment Information (Amounts in millions) (unaudited)</… |
| 2 | `q25119b32a2f9:chunk-6` | 0.08138347417116165 |  | <hr /> |
| 3 | `q25119b32a2f9:chunk-8` | 0.08138347417116165 |  | <hr /> |
| 4 | `q25119b32a2f9:chunk-10` | 0.0786057710647583 |  | <hr /> |
| 5 | `q25119b32a2f9:chunk-12` | 0.06881048530340195 |  | <hr /> |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=47

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q29d3cb8df822:chunk-45` | 0.38000696897506714 |  | 11) What Divisions comprise SLBs Core business and what was their revenue and pretax operating income for the nine mon… |
| 2 | `q29d3cb8df822:chunk-12` | 0.17689062654972076 |  | n/m = not meaningful Reservoir Performance revenue of $1.68 billion grew 2% sequentially primarily due to increased eva… |
| 3 | `q29d3cb8df822:chunk-18` | 0.09955118596553802 |  |  In the Republic of the Congo, a successful five-well, eight-stage acid stimulation campaign was performed for Perenco… |
| 4 | `q29d3cb8df822:chunk-14` | 0.0903494730591774 |  | n/m = not meaningful Well Construction revenue of $3.43 billion increased 2% sequentially led by strong growth in the M… |
| 5 | `q29d3cb8df822:chunk-17` | 0.03771257773041725 |  | The agreement will combine bps experience to frame, build, and execute projects with the Alliances capability to deli… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=210

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2c832749ca0b:chunk-67` | 0.11353364586830139 |  | Description####At September 30, 2023##Valuation Technique##Significant Input##Range, Point Estimate or Average## Contin… |
| 2 | `q2c832749ca0b:chunk-55` | 0.042371295392513275 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |
| 3 | `q2c832749ca0b:chunk-78` | 0.03474356234073639 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |
| 4 | `q2c832749ca0b:chunk-191` | 0.03441799804568291 |  | combined company will be affected by the ability of its officers and key employees to manage changing business conditio… |
| 5 | `q2c832749ca0b:chunk-169` | 0.03384105861186981 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q2fe5769567d7:chunk-1` | 0.12294594943523407 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### ####2023######2022####2023######202… |
| 2 | `q2fe5769567d7:chunk-35` | 0.10314533859491348 |  | Investments in Privately Held Companies Our investments in privately held companies in which we cannot exercise signifi… |
| 3 | `q2fe5769567d7:chunk-98` | 0.08769858628511429 |  | ########Three Months Ended September 30,##################Nine Months Ended September 30,########## ####2023########202… |
| 4 | `q2fe5769567d7:chunk-37` | 0.08039573580026627 |  | ####September 30, 2023#### ##Local Currency Amount######Notional Contract Amount (USD) Euro##€271,600####$##287,705 Can… |
| 5 | `q2fe5769567d7:chunk-50` | 0.0688636302947998 |  | 1 Included in Other long-term liabilities within our Condensed Consolidated Balance Sheet During the three months ended… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q2fe5769567d7`)._

### ex-dev-q318eb902f451

- **example_id**: `dev:q318eb902f451`
- **state**: `completed`
- **query**: What questions were asked about Franklin Resources, Inc.’s client retention and engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9199642183398656 · gold=['Earnings', '8-K', 'DEF14A', '10-K']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q318eb902f451:chunk-53` | 0.1317249983549118 |  | Yes. The only thing I'll add is I think part of John's question may have been about Fiduciary Trust and our growth targ… |
| 2 | `q318eb902f451:chunk-37` | 0.0965472087264061 |  | Thanks for the new PowerPoint deck presentation disclosure there across. Appreciate that. Just as we think about your t… |
| 3 | `q318eb902f451:chunk-2` | 0.052940960973501205 |  | Selene Oh - Executives |
| 4 | `q318eb902f451:chunk-23` | 0.05206911265850067 |  | Sure. So let me start. The focus on that is actually from our existing managers. So -- and just to give you a perspecti… |
| 5 | `q318eb902f451:chunk-4` | 0.0394805483520031 |  | Jennifer Johnson - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q318eb902f451`)._

### ex-dev-q31f6fd1f392c

- **example_id**: `dev:q31f6fd1f392c`
- **state**: `completed`
- **query**: What governance processes are in place for approving changes to Targa Resources Corp.’s compensation policies?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=0.9979470946084208 · gold=['DEF14A', '10-K', '8-K', 'Earnings']
- **S1 ordered**: `['DEF14A', '10-K', '8-K', '10-Q', 'Earnings']`
- **S2**: nDCG@5=0.3494746300967186 · skipped= · n_scored=99

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q31f6fd1f392c:chunk-77` | 0.19158217310905457 |  | # Table of Contents <table><tr><th colspan="2">2023</th></tr><tr><td>Non-PEO NEOs Summary Compensation Table Totals</td… |
| 2 | `q31f6fd1f392c:chunk-7` | 0.17489463090896606 |  | # QUORUM AND VOTING (cont.) ## Our Operations We are engaged primarily in the business of: - gathering, compressing, tr… |
| 3 | `q31f6fd1f392c:chunk-40` | 0.11270938068628311 | 2.0 | # Track Record of Growth Driving an Increasing Return of Capital to Shareholders (cont.) ## Shareholder Outreach - We r… |
| 4 | `q31f6fd1f392c:chunk-1` | 0.049161188304424286 | 1.0 | # TABLE OF CONTENTS <table><tr><th>PROXY STATEMENT 2024 ANNUAL MEETING OF STOCKHOLDERS</th><th></th><th>3</th></tr><tr>… |
| 5 | `q31f6fd1f392c:chunk-41` | 0.044777486473321915 | 2.0 | # Track Record of Growth Driving an Increasing Return of Capital to Shareholders (cont.) ## Good Governance Foundation … |

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
- **S2**: nDCG@5=1.0 · skipped= · n_scored=92

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3ef7ce37ae77:chunk-53` | 0.18532423675060272 | 1.0 | Just a quick one on another question. Just you said flat in the quarter, but it was largely geography mix. Maybe where … |
| 2 | `q3ef7ce37ae77:chunk-21` | 0.12025513499975204 |  | So similar to Bob, just a question around the deal. I guess just, Scott, you kind of alluded to it to Bob's question an… |
| 3 | `q3ef7ce37ae77:chunk-39` | 0.1136554479598999 |  | I wanted to touch on Kate Spade for a minute. You spoke of a need to amplify the efforts there through holistic marketi… |
| 4 | `q3ef7ce37ae77:chunk-23` | 0.0999840795993805 |  | Well, maybe I'll kick it off, Ike, and then pass it to Scott again. We do have both strategic and financial strength an… |
| 5 | `q3ef7ce37ae77:chunk-25` | 0.07563420385122299 |  | Yes, sure. So while Plan A is our priority, should we find ourselves in the plan B scenario, a couple of things I'd jus… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q3ef7ce37ae77`)._

### ex-dev-q3f9446fe3b94

- **example_id**: `dev:q3f9446fe3b94`
- **state**: `completed`
- **query**: How are scenario analyses conducted by American Tower Corporation for risks related to fluctuations in mobile data demand?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9484971533659527 · gold=['10-K', 'Earnings', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=342

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q3f9446fe3b94:chunk-284` | 0.14889037609100342 |  | ####Options Outstanding##########Options Exercisable#### Range of Exercise Price Per Share##Outstanding Number of Optio… |
| 2 | `q3f9446fe3b94:chunk-98` | 0.08924630284309387 |  | ##Issuer or Borrower##Notes/Securities Issued####Conditions Limiting Distributions of Excess Cash## ######Cash Trap DSC… |
| 3 | `q3f9446fe3b94:chunk-34` | 0.07387469708919525 |  | ##Number of Data Centers##Total NRSF (1) ####(in thousands) San Francisco Bay, CA##8##939 Los Angeles, CA##3##724 North… |
| 4 | `q3f9446fe3b94:chunk-102` | 0.0625237226486206 |  | operations are included with our results from the dates of the respective acquisitions. Any excess of the purchase pric… |
| 5 | `q3f9446fe3b94:chunk-84` | 0.04884318634867668 |  | Senior Notes####Aggregate Principal Amount (in millions)##Issue Date and Interest Accrual Date##Maturity Date##Contract… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=116

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q44cfaf358c37:chunk-65` | 0.2835768461227417 |  | Sure, Gavin. So Chris, I think Gavin answered the question a little bit earlier around buyback, right? But our capital … |
| 2 | `q44cfaf358c37:chunk-11` | 0.10116375237703323 |  | Thanks, Gavin, Greg. Just on the assumptions for your guide, right? So are you expecting -- it seems from the phasing t… |
| 3 | `q44cfaf358c37:chunk-61` | 0.038277070969343185 |  | Gavin, can you just comment on the portfolio outside of Coors [indiscernible] and how you feel about shelf for this yea… |
| 4 | `q44cfaf358c37:chunk-6` | 0.03457636013627052 |  | Greg Tierney - Executives |
| 5 | `q44cfaf358c37:chunk-36` | 0.033501822501420975 |  | Greg Tierney - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q44cfaf358c37`)._

### ex-dev-q4acd5677c3da

- **example_id**: `dev:q4acd5677c3da`
- **state**: `completed`
- **query**: What questions were asked about Hasbro’s customer or user engagement metrics?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9359826917490579 · gold=['Earnings', '8-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4acd5677c3da:chunk-71` | 0.08898530900478363 |  | I'd be interested to hear how you guys feel you have completed the brand pruning process. Is that largely done? Is it s… |
| 2 | `q4acd5677c3da:chunk-91` | 0.08182261884212494 |  | That's just a quick clarification. I think you said earlier that you're expecting -- I think you said digital game lice… |
| 3 | `q4acd5677c3da:chunk-47` | 0.060764484107494354 |  | I was wondering, Gina, if maybe we could unpack the revenue guidance for consumer products just a bit more, you cited t… |
| 4 | `q4acd5677c3da:chunk-121` | 0.045087818056344986 |  | One on longer-term margins and one on CapEx, maybe first for Gina on margins, just given the new cost efficiency target… |
| 5 | `q4acd5677c3da:chunk-97` | 0.037512246519327164 |  | So I guess I took from your comments that you said that cash balance would be down in the end of 2024 versus 2023. So I… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4acd5677c3da`)._

### ex-dev-q4bf1699a63fe

- **example_id**: `dev:q4bf1699a63fe`
- **state**: `completed`
- **query**: What dependency risks exist for Boston Properties, Inc. due to concentration of revenue in a limited number of geographic markets or key tenants?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', '10-Q', 'Earnings', 'DEF14A']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.42870185423738655 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4bf1699a63fe:chunk-37` | 0.12629319727420807 | 1.0 | Yes. So I'll turn it over to Mike for the second question. But in terms of the first question, I mentioned the yield th… |
| 2 | `q4bf1699a63fe:chunk-81` | 0.05647394433617592 |  | On the 6 projects that are scheduled to be stabilized in 2025 and have started or are starting initial occupancy this y… |
| 3 | `q4bf1699a63fe:chunk-75` | 0.03917152062058449 | 2.0 | Maybe just a question. Google announced last night meaningful office optimization charges, 1.2 billion in the quarter. … |
| 4 | `q4bf1699a63fe:chunk-9` | 0.039148811250925064 | 2.0 | Great. Thanks, Doug. Good morning, everybody. So this morning, I plan to cover the details of the fourth quarter and ou… |
| 5 | `q4bf1699a63fe:chunk-31` | 0.03515433520078659 |  | Yes. I think the -- Alex, to answer your question on the debt side, Mike should answer. But in general, as you know, we… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q4bf1699a63fe`)._

### ex-dev-q4d8ac905167b

- **example_id**: `dev:q4d8ac905167b`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Citigroup Inc. for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.04868944994756881 · skipped= · n_scored=894

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4d8ac905167b:chunk-43` | 0.0672038197517395 |  | (1) Excludes loans that are carried at fair value for all periods. NM Not meaningful 23 |
| 2 | `q4d8ac905167b:chunk-224` | 0.06355561316013336 |  | ####Citigroup Inc.######Citibank, N.A.## ##Long-term##Short-term##Outlook##Long- term##Short- term##Outlook Fitch Ratin… |
| 3 | `q4d8ac905167b:chunk-341` | 0.061775173991918564 |  | Income Taxes (Topic 740): Improvements to Income Tax Disclosures In December 2023, the FASB issued ASU No. 2023-09, Inc… |
| 4 | `q4d8ac905167b:chunk-290` | 0.02924627810716629 | 1.0 | ######Quarterly average########## U.S. unemployment##1Q24####3Q24####1Q25####8-quarter average(1)## Citi forecast at 4Q… |
| 5 | `q4d8ac905167b:chunk-22` | 0.028923913836479187 |  | (1)The information presented in the table above reflects select GAAP balance sheet items by reportable segment and comp… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=170

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q4f1cc6ea4ba6:chunk-15` | 0.16540339589118958 |  | Yes, Vijay. Let me take that. I think if you look at the book-to-bill ratio, it's -- for LSAG instruments, it's actuall… |
| 2 | `q4f1cc6ea4ba6:chunk-35` | 0.11921652406454086 |  | Yes. And Patrick, you asked about Q1, as I mentioned in the prepared remarks, I think we're taking a prudent approach h… |
| 3 | `q4f1cc6ea4ba6:chunk-114` | 0.04593226686120033 |  | Puneet Souda - Analysts |
| 4 | `q4f1cc6ea4ba6:chunk-118` | 0.04593226686120033 |  | Puneet Souda - Analysts |
| 5 | `q4f1cc6ea4ba6:chunk-109` | 0.04325360804796219 |  | Yes. So the orders were down year-on-year, but obviously down not as much as revenue was down year-on-year. And so when… |

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
| 1 | `q53994e82efbb:chunk-17` | 0.21127116680145264 |  | 8 |
| 2 | `q53994e82efbb:chunk-11` | 0.1874273717403412 |  | 1.Pursuant to repurchase programs authorized by our board of directors, we repurchased and retired 1.7 million shares, … |
| 3 | `q53994e82efbb:chunk-57` | 0.12292326986789703 |  | Item 5. Other Information None. 22 |
| 4 | `q53994e82efbb:chunk-16` | 0.10473333299160004 |  | ######Three Months Ended September 30,############Nine Months Ended September 30,#### ####2023######2022######2023#####… |
| 5 | `q53994e82efbb:chunk-55` | 0.044352468103170395 |  | Period##Total Number of Shares Purchased####Average Price Paid per Share (including fees)##Total Number of Shares Purch… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q53994e82efbb`)._

### ex-dev-q56c2aa1b3aa2

- **example_id**: `dev:q56c2aa1b3aa2`
- **state**: `completed`
- **query**: How are scenario analyses conducted by FedEx Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=165

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q56c2aa1b3aa2:chunk-90` | 0.20302467048168182 |  | # Executive Compensation - Summary Compensation Table (cont.) - Personal use of corporate aircraft: FedEx maintains a f… |
| 2 | `q56c2aa1b3aa2:chunk-76` | 0.19096754491329193 |  | # Future LTI Payout Opportunities (cont.) ## CapEx/Revenue The second metric in the FY22-FY24 and FY23-FY25 LTI plans, … |
| 3 | `q56c2aa1b3aa2:chunk-77` | 0.12279848754405975 |  | # Future LTI Payout Opportunities (cont.) ## ROIC The second metric selected for the FY24-FY26 LTI plan is ROIC, which … |
| 4 | `q56c2aa1b3aa2:chunk-3` | 0.07075867056846619 |  | # NOTICE OF ANNUAL MEETING OF STOCKHOLDERS ## Items of Business <table><tr><th colspan="2">Voting Proposal</th><th>Boar… |
| 5 | `q56c2aa1b3aa2:chunk-118` | 0.05071837827563286 |  | # Executive Compensation - Potential Payments Upon Termination or Change of Control (cont.) ## Pay Versus Performance (… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q56c2aa1b3aa2`)._

### ex-dev-q57e9d5635f56

- **example_id**: `dev:q57e9d5635f56`
- **state**: `completed`
- **query**: What quarter did guidance point to for streaming breakeven achievement
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=1.0 · gold=['Earnings']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=60

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q57e9d5635f56:chunk-47` | 0.11497583240270615 |  | Bob, first follow-up on ESPN, clearly a big priority, can you give us some update on types of potential ESPN partners a… |
| 2 | `q57e9d5635f56:chunk-2` | 0.07557894289493561 |  | Alexia Quadrani - Executives |
| 3 | `q57e9d5635f56:chunk-8` | 0.07327738404273987 |  | Alexia Quadrani - Executives |
| 4 | `q57e9d5635f56:chunk-42` | 0.07302539050579071 |  | Alexia Quadrani - Executives |
| 5 | `q57e9d5635f56:chunk-50` | 0.0711624026298523 |  | Alexia Quadrani - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q57e9d5635f56`)._

### ex-dev-q587ea3fc913d

- **example_id**: `dev:q587ea3fc913d`
- **state**: `completed`
- **query**: What guidance did Textron’s leadership give on cost structure optimization efforts?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', 'DEF14A', '10-K', '8-K']`
- **S2**: nDCG@5=0.3938807921944381 · skipped= · n_scored=174

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q587ea3fc913d:chunk-5` | 0.29442691802978516 |  | Thanks, David, and good morning, everyone. Our business has closed out the year with another solid quarter with strong … |
| 2 | `q587ea3fc913d:chunk-131` | 0.1448746770620346 | 2.0 | George, I think look, we're continuing to see good margins on our military business, obviously outside of the FLRAA sid… |
| 3 | `q587ea3fc913d:chunk-59` | 0.1185879334807396 |  | Well, look, no, I think as I said at the beginning, we feel good about the end market. Customer dialogues are robust. F… |
| 4 | `q587ea3fc913d:chunk-157` | 0.10801447182893753 | 1.0 | Well, look, I listed the challenge of the world we're listening, right? I mean, we had some pretty significant impacts … |
| 5 | `q587ea3fc913d:chunk-7` | 0.07396906614303589 | 2.0 | Thanks, Scott, and good morning, everyone. Let's review how each of the segments contributed, starting with Textron Avi… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q587ea3fc913d`)._

### ex-dev-q5ce8ea5bf1b9

- **example_id**: `dev:q5ce8ea5bf1b9`
- **state**: `completed`
- **query**: What dependency risks exist for Global Payments Inc. due to concentration of revenue in a limited number of payment processing partners or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.21398626473452753 · skipped= · n_scored=119

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q5ce8ea5bf1b9:chunk-76` | 0.3189381957054138 |  | ####Nine Months Ended## ##September 30, 2023####September 30, 2022 Risk-free interest rate##3.84%####1.87% Expected vol… |
| 2 | `q5ce8ea5bf1b9:chunk-33` | 0.08802703022956848 | 2.0 | From the acquisition date through September 30, 2023, the acquired operations of EVO contributed less than 10% to our c… |
| 3 | `q5ce8ea5bf1b9:chunk-66` | 0.052684083580970764 |  | As of September 30, 2023, the amount of net unrealized gains in accumulated other comprehensive loss related to our int… |
| 4 | `q5ce8ea5bf1b9:chunk-30` | 0.049946170300245285 |  | As of September 30, 2023, we considered these amounts to be provisional because we were still in the process of gatheri… |
| 5 | `q5ce8ea5bf1b9:chunk-29` | 0.031461264938116074 |  | ####Provisional Amounts at Acquisition Date####Measurement-period Adjustments####Provisional Amounts at September 30, 2… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=134

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q63259a02ade0:chunk-64` | 0.7051172852516174 |  | # Executive Compensation Tables (cont.) <table><tr><th>Name and Principal Position</th><th>Year</th><th>Salary ($)</th>… |
| 2 | `q63259a02ade0:chunk-68` | 0.09130078554153442 |  | # Executive Compensation Tables (cont.) ## Grants of Plan-Based Awards-2023 (cont.) <table><tr><th colspan="3"></th><th… |
| 3 | `q63259a02ade0:chunk-93` | 0.05767424777150154 |  | # Proposal No. 5 Shareholder Proposal (cont.) ## Supporting Statement: (cont.) As shareholders of Apple Inc., we believ… |
| 4 | `q63259a02ade0:chunk-77` | 0.020979583263397217 |  | # Pay versus Performance (cont.) <table><tr><td rowspan="2"></td><th colspan="2">2023</th><th colspan="2">2022</th><th … |
| 5 | `q63259a02ade0:chunk-45` | 0.014898105524480343 |  | # The Role of the Compensation Consultant (cont.) ## Actions Taken in Response (cont.) - The 2023 time-based RSUs grant… |

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
| 1 | `q64898e5ba36c:chunk-250` | 0.2292153239250183 |  | 99 |
| 2 | `q64898e5ba36c:chunk-15` | 0.09883487969636917 |  | the forward-looking statements, whether because of these factors or for other reasons. All forward-looking statements s… |
| 3 | `q64898e5ba36c:chunk-235` | 0.09612257778644562 |  | ####U.S. Retiree Healthcare Plans####Non-U.S. Pension Plans####Total 2024##$##1,959##$##4,018##$##5,977 2025####2,068##… |
| 4 | `q64898e5ba36c:chunk-66` | 0.04175993427634239 |  | Recent Accounting Standard Changes and Developments Information regarding recent accounting standard changes and develo… |
| 5 | `q64898e5ba36c:chunk-102` | 0.034377530217170715 |  | ####Total at December 31, 2023####Quoted Prices in Active Markets for Identical Assets (Level 1)####Significant Other O… |

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
| 1 | `q6d2cc453ca8c:chunk-51` | 0.1527685523033142 |  | I think just more longer term on the SaaS migration. We have a little bit over $900 million in on-premise maintenance. … |
| 2 | `q6d2cc453ca8c:chunk-71` | 0.14925386011600494 |  | Great. And then about the aspiration to 8% to 9% organic growth and driving things higher. Certainly, I understand you … |
| 3 | `q6d2cc453ca8c:chunk-107` | 0.08493854105472565 |  | Correct. |
| 4 | `q6d2cc453ca8c:chunk-73` | 0.06301991641521454 |  | So we appreciate the question, right? So we started this portfolio of 5% to 6% growth. We're in a way point of, we thin… |
| 5 | `q6d2cc453ca8c:chunk-119` | 0.061482496559619904 |  | Really appreciate the opportunity to address this question because one of the aspects of the business that we like quit… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q70e4aac30ddb:chunk-63` | 0.2035755068063736 |  | Laxman, in the press release, you were mentioning that the reinvention plan is moving ahead of schedule. So which aspec… |
| 2 | `q70e4aac30ddb:chunk-19` | 0.17693357169628143 |  | Great. I had a question and then just one clarification. The question is on the U.S. comp. Laxman, I think you mentione… |
| 3 | `q70e4aac30ddb:chunk-65` | 0.08725564926862717 |  | I'm very pleased with the way that the reinvention plan is being implemented. A couple of highlights. I think the progr… |
| 4 | `q70e4aac30ddb:chunk-51` | 0.07683105021715164 |  | There's been a lot of conversation this quarter about throughput, particularly at the drive-thru, but we can also talk … |
| 5 | `q70e4aac30ddb:chunk-35` | 0.041393835097551346 |  | Congrats on the quarter. Also on the U.S. comps and traffic, can you help unpack where the growth is coming from? Is it… |

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
| 1 | `q719082ac2068:chunk-1` | 0.9637057185173035 |  | # Q4 Fiscal 2024 Summary <table><tr><td>GAAP</td></tr></table> <table><tr><td>($ in millions, except earnings per share… |
| 2 | `q719082ac2068:chunk-5` | 0.026675360277295113 |  | # Q4 Fiscal 2024 Summary (cont.) ## About NVIDIA (cont.) Simona Jankowski Investor Relations NVIDIA Corporation sjankow… |
| 3 | `q719082ac2068:chunk-7` | 0.005196744576096535 |  | # Q4 Fiscal 2024 Summary (cont.) ## About NVIDIA (cont.) © 2024 NVIDIA Corporation. All rights reserved. INVIDIA, the N… |
| 4 | `q719082ac2068:chunk-8` | 0.002790715079754591 |  | # CONDENSED CONSOLIDATED STATEMENTS OF INCOME (In millions, except per share data) (Unaudited) <table><tr><td rowspan="… |
| 5 | `q719082ac2068:chunk-4` | 0.0004547166172415018 |  | # Q4 Fiscal 2024 Summary (cont.) ## Conference Call and Webcast Information NVIDIA will conduct a conference call with … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q719082ac2068`)._

### ex-dev-q76caada13eca

- **example_id**: `dev:q76caada13eca`
- **state**: `completed`
- **query**: What causes differences between Weyerhaeuser Company’s cash flow and net income (e.g., timberland harvest cycles or non-cash depreciation)?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9199642183398656 · gold=['10-K', '8-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['10-K', 'Earnings', '10-Q', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=86

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q76caada13eca:chunk-2` | 0.15749962627887726 |  | Andy Taylor - Executives |
| 2 | `q76caada13eca:chunk-4` | 0.04154929891228676 |  | Devin Stockfish - Executives |
| 3 | `q76caada13eca:chunk-8` | 0.04154929891228676 |  | Devin Stockfish - Executives |
| 4 | `q76caada13eca:chunk-14` | 0.04128427058458328 |  | Devin Stockfish - Executives |
| 5 | `q76caada13eca:chunk-18` | 0.0411340668797493 |  | Devin Stockfish - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q76caada13eca`)._

### ex-dev-q78d98dc75a82

- **example_id**: `dev:q78d98dc75a82`
- **state**: `completed`
- **query**: How has Humana’s Medicare Advantage segment profitability trended over recent periods?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '8-K', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=283

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q78d98dc75a82:chunk-131` | 0.5590391755104065 |  | Humana Inc. NOTES TO CONSOLIDATED FINANCIAL STATEMENTS—(Continued) Generally, under the equity method, original investm… |
| 2 | `q78d98dc75a82:chunk-47` | 0.08137103170156479 |  | ####12/31/2018####12/31/2019####12/31/2020####12/31/2021####12/31/2022####12/31/2023 HUM##$##100##$##129##$##145##$##16… |
| 3 | `q78d98dc75a82:chunk-174` | 0.03958701342344284 |  | ##Weighted Average Life########2023##############2022#### ######Cost####Accumulated Amortization####Net######Cost####Ac… |
| 4 | `q78d98dc75a82:chunk-167` | 0.03366107866168022 |  | ######2023############2022#### ####Risk Corridor Settlement######CMS Subsidies/ Discounts######Risk Corridor Settlement… |
| 5 | `q78d98dc75a82:chunk-14` | 0.022455940023064613 |  | Provider Arrangements We provide our members with access to health care services through our networks of health care pr… |

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
| 1 | `q79acb772ca6b:chunk-18` | 0.20338021218776703 |  | ####Type of Significant Property## ##Manufacturing####Sales, Service and Warehouse Industrial Technologies and Services… |
| 2 | `q79acb772ca6b:chunk-74` | 0.08076338469982147 |  | ########For the Years Ended December 31,#### ####2023####2022####2021 Revenues##$##6,876.1##$##5,916.3##$##5,152.4 Cost… |
| 3 | `q79acb772ca6b:chunk-166` | 0.06333425641059875 |  | ##U.S. Plans####UK Plan## Asset category:######## Equity##13##%##18##% Fixed income##84##%##72##% Real estate and other… |
| 4 | `q79acb772ca6b:chunk-231` | 0.06176772713661194 |  | ############December 31, 2022############ ##Derivative Classification####Notional Amount(1)####Fair Value(1) Other Curr… |
| 5 | `q79acb772ca6b:chunk-20` | 0.04706288501620293 |  | Of the 136 significant properties included in the above table, 84 of the properties are leased and 52 of the properties… |

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
- **S2**: nDCG@5=0.6061680178534535 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7c284aabbba4:chunk-7` | 0.26710328459739685 | 2.0 | Thanks, Stéphane, and hello, everyone. Today, I will review our financial performance for both the fourth quarter and t… |
| 2 | `q7c284aabbba4:chunk-25` | 0.06308096647262573 | 2.0 | Thanks, Stephen. And Gena, it's Stéphane. On the upside and downside on the sales for this year, I think on the upside,… |
| 3 | `q7c284aabbba4:chunk-21` | 0.05671737343072891 |  | I have 2 very quick questions. First one is regarding the RSV vaccine. What portion of 35,000 to 36,000 participants th… |
| 4 | `q7c284aabbba4:chunk-57` | 0.05020090565085411 |  | Sorry -- small technical stuff. So I'm back. I believe I caught the end of the question, which is how -- when do we thi… |
| 5 | `q7c284aabbba4:chunk-53` | 0.042449865490198135 |  | This is Alex Hammond on for Geoff Meacham. So a great way to equalize vaccine efficacy results is to use a correlative … |

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
| 1 | `q7eb4e8a11956:chunk-2` | 0.06472557038068771 |  | Suhasini Chandramouli - Executives |
| 2 | `q7eb4e8a11956:chunk-8` | 0.06288332492113113 |  | Suhasini Chandramouli - Executives |
| 3 | `q7eb4e8a11956:chunk-114` | 0.05893341451883316 |  | Suhasini Chandramouli - Executives |
| 4 | `q7eb4e8a11956:chunk-6` | 0.04142792150378227 |  | Luca Maestri - Executives |
| 5 | `q7eb4e8a11956:chunk-28` | 0.041006073355674744 |  | Luca Maestri - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q7eb4e8a11956`)._

### ex-dev-q7eb5b91e2366

- **example_id**: `dev:q7eb5b91e2366`
- **state**: `completed`
- **query**: What dependency risks exist for Becton, Dickinson and Company due to concentration of revenue in a limited number of healthcare providers or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9935051443580323 · gold=['10-K', '10-Q', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=76

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q7eb5b91e2366:chunk-61` | 0.27925029397010803 |  | Yes. Thanks for the question, Matt. We couldn't be more excited about APMs coming into BD. We're really happy having Ka… |
| 2 | `q7eb5b91e2366:chunk-55` | 0.22779706120491028 |  | Yes. Thank you for the question, Matt. You're kind of teeing us up for our Investor Day on February 26, where we'll act… |
| 3 | `q7eb5b91e2366:chunk-11` | 0.07002615183591843 |  | Maybe on this guidance question here. Thanks for all the details. The 125 basis points of headwinds on pharma, bioscien… |
| 4 | `q7eb5b91e2366:chunk-31` | 0.06285334378480911 |  | Yes. Thanks, Travis. It's Chris. I'll try and give a little extra color. I think consistent with what I've said, again,… |
| 5 | `q7eb5b91e2366:chunk-73` | 0.03937630355358124 |  | Well, thank you for joining us on our call today. I'd like to take a moment and again, thank our global team of associa… |

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
| 1 | `q7ed5279a28b4:chunk-58` | 0.14645850658416748 |  | As of October 1, 2023, the conversion price was approximately $31.41 per share and the if converted value of the notes … |
| 2 | `q7ed5279a28b4:chunk-60` | 0.08660662919282913 |  | ####October 1, 2023######December 31, 2022 ######(in thousands)#### Contract manufacturer and supplier prepayments##$##… |
| 3 | `q7ed5279a28b4:chunk-110` | 0.043833717703819275 |  | ######For the Three Months Ended########## ####October 1, 2023######October 2, 2022####Dollar Change## ##########(in mi… |
| 4 | `q7ed5279a28b4:chunk-35` | 0.03609330579638481 |  | ####Cost####Unrealized Gain####Unrealized (Loss)######Fair Market Value####Fair Market Value of Investments with Unreal… |
| 5 | `q7ed5279a28b4:chunk-31` | 0.03281904384493828 |  | The fair values of accounts receivable, net and accounts payable approximate the carrying value due to the short-term n… |

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
| 1 | `q84038a74fd59:chunk-5` | 0.37934422492980957 | 2.0 | Thank you very much, Brett. We had a solid close to our fiscal year. The Microsoft Cloud surpassed $110 billion in annu… |
| 2 | `q84038a74fd59:chunk-29` | 0.06724094599485397 |  | And congrats on the quarter. Amy, CapEx moved up significantly Q-over-Q and year-over-year and it's increasing moving f… |
| 3 | `q84038a74fd59:chunk-33` | 0.06496676057577133 |  | Yes. And I think just for perspective, I think it's sort of always good to think about it, right, where we have, what, … |
| 4 | `q84038a74fd59:chunk-59` | 0.037271708250045776 |  | I guess maybe just a multi-parter. You mentioned a couple of times that with the AI workload adoption that you're seein… |
| 5 | `q84038a74fd59:chunk-2` | 0.02858097106218338 |  | Brett Iversen - Executives |

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
- **S2**: nDCG@5=0.5052077707304854 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88819064dbb7:chunk-53` | 0.1237611472606659 | 1.0 | Just wanted to ask, first off, two questions related to the store closures. I guess, number one, is there additional op… |
| 2 | `q88819064dbb7:chunk-33` | 0.1051662340760231 |  | Just a couple for me. Jeff, can you unpack the margin guide by banner? I'm just trying to isolate if you're still antic… |
| 3 | `q88819064dbb7:chunk-25` | 0.08147692680358887 | 2.0 | So two questions. Maybe, could you elaborate on the traffic trends and market share by demographic that you're seeing a… |
| 4 | `q88819064dbb7:chunk-81` | 0.02972273901104927 |  | I wanted to dig into the SNAP headwind of negative 5% on Family Dollar. Could you quantify how you got to that math? Be… |
| 5 | `q88819064dbb7:chunk-23` | 0.02791985124349594 |  | Your next question is coming from Matthew Boss from JPMorgan. |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q88819064dbb7`)._

### ex-dev-q88db5d96c8dd

- **example_id**: `dev:q88db5d96c8dd`
- **state**: `completed`
- **query**: How does Bristol-Myers Squibb manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=1.0 · gold=['10-K', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=176

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q88db5d96c8dd:chunk-55` | 0.18683557212352753 |  | (a) Included in Other current assets and Other non-current assets. (b) Included in Other current liabilities and Other … |
| 2 | `q88db5d96c8dd:chunk-105` | 0.07688571512699127 |  | In the UK, Sandoz and Teva filed lawsuits in the United Kingdom seeking revocation of the UK composition-of-matter pate… |
| 3 | `q88db5d96c8dd:chunk-51` | 0.07635842263698578 |  | Cumulative upwards adjustments and cumulative impairments and downward adjustments based on observable price changes in… |
| 4 | `q88db5d96c8dd:chunk-103` | 0.07427115738391876 |  | Note 18. LEGAL PROCEEDINGS AND CONTINGENCIES BMS and certain of its subsidiaries are involved in various lawsuits, clai… |
| 5 | `q88db5d96c8dd:chunk-76` | 0.07213781774044037 |  | Amortization expense of Other intangible assets was $2.3 billion and $6.9 billion during the three and nine months ende… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q88db5d96c8dd`)._

### ex-dev-q89953a08e494

- **example_id**: `dev:q89953a08e494`
- **state**: `completed`
- **query**: How does Globe Life Inc. manage equity award burn rate or share pool availability?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', 'DEF14A', '10-Q', '8-K']
- **S1 ordered**: `['10-K', 'DEF14A', '10-Q', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.11338325082575977 · skipped= · n_scored=125

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89953a08e494:chunk-124` | 0.28641194105148315 |  | # GLOBE LIFE INC. ANNUAL MEETING OF SHAREHOLDERS Thursday, April 25, 2024 10:00 a.m. (CDT) Virtual Meeting Online via l… |
| 2 | `q89953a08e494:chunk-24` | 0.15087781846523285 |  | # OTHER BUSINESS (cont.) ## Executive Officers (cont.) <table><tr><th>Name</th><th>Current Age</th><th>Principal Occupa… |
| 3 | `q89953a08e494:chunk-42` | 0.1434461921453476 |  | # Risk Reporting Structure (cont.) ## Committees of the Board of Directors (cont.) 22 GL 2024 Proxy Statement <table><t… |
| 4 | `q89953a08e494:chunk-63` | 0.08152066171169281 | 1.0 | # Assessment of 2023 Advisory Vote on Executive Compensation (cont.) ## Elements of Compensation The total compensation… |
| 5 | `q89953a08e494:chunk-80` | 0.06858118623495102 | 1.0 | # 2023 GRANTS OF PLAN-BASED AWARDS <table><tr><th></th><th rowspan="2">Award Type</th><th rowspan="2">Grant Date</th><t… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q89953a08e494`)._

### ex-dev-q89fb186f5e49

- **example_id**: `dev:q89fb186f5e49`
- **state**: `completed`
- **query**: What investor views emerged on Linde’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.93228165068934 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=287

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q89fb186f5e49:chunk-12` | 0.16729487478733063 |  | Table of Contents The Americas segment operates production facilities primarily in the U.S., Canada, Mexico and Brazil,… |
| 2 | `q89fb186f5e49:chunk-10` | 0.16473199427127838 |  | Table of Contents Changes in tax laws or policy could adversely impact the company’s financial position or results of o… |
| 3 | `q89fb186f5e49:chunk-0` | 0.1098775863647461 |  | PART I ITEM 1. BUSINESS General Linde plc is a public limited company formed under the laws of Ireland with its princip… |
| 4 | `q89fb186f5e49:chunk-238` | 0.07658090442419052 |  | The descriptions and fair value methodologies for the company's pension plan assets are as follows: Cash and Cash Equiv… |
| 5 | `q89fb186f5e49:chunk-4` | 0.05472656339406967 |  | Table of Contents regional cluster in Eastern Europe with an increasing number of countries. In 2017, he was promoted t… |

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
| 1 | `q8ba6a388d681:chunk-75` | 0.1862386018037796 |  | We just bought a company that's pretty sizable. We are restructuring the business model and we're changing, among other… |
| 2 | `q8ba6a388d681:chunk-11` | 0.09731898456811905 |  | Hock, so yesterday, one of your peers suggested that the market for AI accelerators could be as large as $400 billion. … |
| 3 | `q8ba6a388d681:chunk-73` | 0.08050888031721115 |  | Great. And maybe a quick follow-up. Thoughts on just why you didn't offer next quarter in favor of the full year? And i… |
| 4 | `q8ba6a388d681:chunk-69` | 0.0641205832362175 |  | Always with acquisitions in mind, we're continuing our share repurchase program that we promised. So that's -- we're de… |
| 5 | `q8ba6a388d681:chunk-6` | 0.04674120992422104 |  | Kirsten Spears - Executives |

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
| 1 | `q8e053e02a010:chunk-16` | 0.16203732788562775 |  | # Table of Contents (cont.) ## 2. Pay at Risk We believe a significant portion of an executive's compensation should be… |
| 2 | `q8e053e02a010:chunk-73` | 0.14084896445274353 |  | # Compensation Governance Best Practices - Pay-for-Performance. 100% of incentive pay is performance-based and/or stock… |
| 3 | `q8e053e02a010:chunk-5` | 0.1268908828496933 |  | # Table of Contents <table><tr><th>Proxy Summary</th><th>4</th></tr><tr><td>ITEM 1 Election of 9 Directors</td><td>13</… |
| 4 | `q8e053e02a010:chunk-3` | 0.10886891186237335 |  | # Notice of Annual Meeting of Shareowners Date and Time Monday, May 13, 2024, at 11:00 a.m. CDT Place International Pap… |
| 5 | `q8e053e02a010:chunk-134` | 0.06116493046283722 |  | # CEO Equity Component of CAP for FY 2023: <table><tr><th>Year</th><th>Equity Type</th><th>Fair Value of Current Year E… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=208

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q93fb2b2861c4:chunk-17` | 0.25784844160079956 |  | PUBLIC INFORMATION We maintain a website at www.churchdwight.com and on the “Investors-Financial Information-SEC Filing… |
| 2 | `q93fb2b2861c4:chunk-194` | 0.10239184647798538 |  | *##(10.21)##First Amendment to Church & Dwight Co., Inc. Amended and Restated Omnibus Equity Compensation Plan, incorpo… |
| 3 | `q93fb2b2861c4:chunk-75` | 0.07962627708911896 |  | CHURCH & DWIGHT CO., INC AND SUBSIDIARIES (Dollars in millions, except share and per share data) OTHER ITEMS Market ris… |
| 4 | `q93fb2b2861c4:chunk-36` | 0.07341941446065903 |  | Company / Index##2018##2019##2020##2021##2022##2023 ■ Church & Dwight Co., Inc.##100.00##108.36##135.96##161.63##128.63… |
| 5 | `q93fb2b2861c4:chunk-163` | 0.05685284733772278 |  | ####Options Outstanding########Options Exercisable#### ####Weighted####Weighted########Weighted ##Outstanding##Average#… |

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
- **S2**: nDCG@5=0.20253383242385095 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q98c606bb3ce7:chunk-3` | 0.177176371216774 |  | Table of Contents Talent Development and Career Mobility We invest in our associates through accessible resources and s… |
| 2 | `q98c606bb3ce7:chunk-30` | 0.11767178028821945 | 1.0 | Table of Contents ITEM 3. LEGAL PROCEEDINGS We are involved in lawsuits, claims and proceedings incident to the ordinar… |
| 3 | `q98c606bb3ce7:chunk-5` | 0.10414032638072968 |  | Table of Contents domain names, trade secrets and other intellectual property and proprietary technology that we hold a… |
| 4 | `q98c606bb3ce7:chunk-36` | 0.09045866876840591 |  | Notes: A.The lines represent monthly index levels derived from compounded daily returns that include all dividends. B.T… |
| 5 | `q98c606bb3ce7:chunk-23` | 0.07653136551380157 | 2.0 | Table of Contents cause delays in locating and shipping products, and increases in costs associated with inventory that… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q98c606bb3ce7`)._

### ex-dev-q99a077efaab0

- **example_id**: `dev:q99a077efaab0`
- **state**: `completed`
- **query**: What dependency risks exist for Align Technology due to concentration of revenue in a limited number of orthodontic practices or geographic regions?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9873464281832952 · gold=['10-K', '10-Q', '8-K', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=128

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q99a077efaab0:chunk-95` | 0.1340024471282959 |  | I mean obviously, the scale, you look at retainers first because units of one. And that's why you'd end up with compreh… |
| 2 | `q99a077efaab0:chunk-115` | 0.13001197576522827 |  | Joe, given the positive macro shift we've seen in the last few months with consumer confidence coming back, any chance … |
| 3 | `q99a077efaab0:chunk-87` | 0.10273618996143341 |  | Michael, this is John. I would say as we look to expand this out, it's been successful every place that we've gone. We'… |
| 4 | `q99a077efaab0:chunk-69` | 0.09134234488010406 |  | Brandon, Joe again. On the Lumina side, remember, our restorative scanner for GPs comes out in the third quarter. But a… |
| 5 | `q99a077efaab0:chunk-39` | 0.03910896182060242 |  | There's no charity here at Align. There will be a charge. |

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
| 1 | `q99ec5f1aeea5:chunk-38` | 0.21443037688732147 |  | (2)The interest rate is effectively fixed at 5.03% through the initial maturity date, as a result of three interest rat… |
| 2 | `q99ec5f1aeea5:chunk-51` | 0.11218811571598053 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 3 | `q99ec5f1aeea5:chunk-55` | 0.09712684154510498 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="3">Notes:</td><td colspan="3"></… |
| 4 | `q99ec5f1aeea5:chunk-60` | 0.07561936974525452 |  | See Glossary of Terms. Individual items may not add up to total due to rounding. <table><tr><td></td><td></td><td></td>… |
| 5 | `q99ec5f1aeea5:chunk-30` | 0.07402095943689346 |  | Notes: (1)There is no guarantee that the Trust will ultimately complete any or all of these opportunities, that the ROI… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q99ec5f1aeea5`)._

### ex-dev-q9a5cfe35fecd

- **example_id**: `dev:q9a5cfe35fecd`
- **state**: `completed`
- **query**: What dependency risks exist for CMS Energy Corporation due to concentration of revenue in a limited number of geographic regions or key utility customers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.21398626473452753 · skipped= · n_scored=194

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9a5cfe35fecd:chunk-16` | 0.17945732176303864 |  | Wolverine Power Wolverine Power Supply Cooperative, Inc., a non-affiliated company 8 |
| 2 | `q9a5cfe35fecd:chunk-19` | 0.10046886652708054 | 2.0 | •the investment performance of the assets of CMS Energy’s and Consumers’ pension and benefit plans, the discount rates,… |
| 3 | `q9a5cfe35fecd:chunk-18` | 0.0844428539276123 |  | •potentially adverse regulatory treatment, effects of a failure to receive timely regulatory orders that are or could c… |
| 4 | `q9a5cfe35fecd:chunk-181` | 0.062167420983314514 |  | ##In Millions ## September 30## Retention benefit liability at beginning of period## Costs deferred as a regulatory ass… |
| 5 | `q9a5cfe35fecd:chunk-140` | 0.05351240932941437 |  | ##########Forward Price Per Share#### Contract Date##Maturity Date##Number of Shares##Initial######September 30, 2023##… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9a5cfe35fecd`)._

### ex-dev-q9c255237096a

- **example_id**: `dev:q9c255237096a`
- **state**: `completed`
- **query**: What perquisites or fringe benefits are included in The AES Corporation’s executive compensation disclosures?
- **S1**: top1=`DEF14A` in_gold=True · nDCG@5=1.0 · gold=['DEF14A']
- **S1 ordered**: `['DEF14A', '10-K', '10-Q', '8-K', 'Earnings']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=110

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9c255237096a:chunk-106` | 0.3841620087623596 |  | # Appendix C: Short-Term Incentive Plan Performance Targets As described in the the Compensation Discussion and Analysi… |
| 2 | `q9c255237096a:chunk-47` | 0.17822106182575226 |  | # Overview of AES Total Compensation (cont.) ## 2023 Performance Incentive Plan Payouts (cont.) In early 2024, the Comp… |
| 3 | `q9c255237096a:chunk-41` | 0.07750637829303741 |  | # EXECUTIVE COMPENSATION COMPENSATION DISCUSSION AND ANALYSIS ("CD&A") (cont.) ## Our Executive Compensation Philosophy… |
| 4 | `q9c255237096a:chunk-7` | 0.05007558688521385 |  | # CAUTIONARY NOTE REGARDING FORWARD-LOOKING STATEMENTS (cont.) 2024 Proxy Statement I 4 aes - our ability to achieve re… |
| 5 | `q9c255237096a:chunk-45` | 0.0408555343747139 |  | # Overview of AES Total Compensation (cont.) ## Compensation Mix The Company does not target a specific allocation of c… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9c255237096a`)._

### ex-dev-q9dd3907388e3

- **example_id**: `dev:q9dd3907388e3`
- **state**: `completed`
- **query**: How does Duke Energy view the pace of innovation cycles in renewable energy technologies and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'DEF14A', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=72

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9dd3907388e3:chunk-72` | 0.8822866082191467 |  | (a) Piedmont has a margin decoupling mechanism in North Carolina, weather normalization mechanisms in South Carolina an… |
| 2 | `q9dd3907388e3:chunk-71` | 0.020867666229605675 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 3 | `q9dd3907388e3:chunk-1` | 0.015632646158337593 |  | Business segment results In addition to the following summary of second-quarter 2024 business segment performance, comp… |
| 4 | `q9dd3907388e3:chunk-0` | 0.01401226595044136 |  | News Release Media Contact: Gillian Moore 24-Hour: 800.559.3853 Analyst Contact: Abby Motsinger Office: 704.382.7624 Au… |
| 5 | `q9dd3907388e3:chunk-67` | 0.012682469561696053 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9dd3907388e3`)._

### ex-dev-q9f32df79b0d7

- **example_id**: `dev:q9f32df79b0d7`
- **state**: `completed`
- **query**: How does Capital One view the pace of digital banking innovation cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9567050450675799 · gold=['10-K', 'Earnings', 'DEF14A', '10-Q']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.5 · skipped= · n_scored=4

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `q9f32df79b0d7:chunk-2` | 0.7430176138877869 |  | •Auto average loans decreased $493 million, or 1 percent, to $75.7 billion. ◦Commercial Banking average loans decreased… |
| 2 | `q9f32df79b0d7:chunk-1` | 0.19270892441272736 |  | •Total net revenue increased 4 percent to $9.4 billion. •Total non-interest expense increased 1 percent to $4.9 billion… |
| 3 | `q9f32df79b0d7:chunk-0` | 0.06423266977071762 | 1.0 | Exhibit 99.1 News Release <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><… |
| 4 | `q9f32df79b0d7:chunk-3` | 4.073948002769612e-05 |  | Capital One Financial Corporation (www.capitalone.com) is a financial holding company which, along with its subsidiarie… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:q9f32df79b0d7`)._

### ex-dev-qa057a3d428a2

- **example_id**: `dev:qa057a3d428a2`
- **state**: `completed`
- **query**: What dependency risks exist for McKesson Corporation due to concentration of revenue in a limited number of pharmaceutical manufacturers or healthcare providers?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9979470946084208 · gold=['10-K', '10-Q', 'Earnings', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa057a3d428a2:chunk-19` | 0.17160047590732574 |  | See Financial Notes 8 |
| 2 | `qa057a3d428a2:chunk-16` | 0.13822874426841736 |  | See Financial Notes 7 |
| 3 | `qa057a3d428a2:chunk-12` | 0.1200294941663742 |  | See Financial Notes 6 |
| 4 | `qa057a3d428a2:chunk-5` | 0.08440234512090683 |  | See Financial Notes 4 |
| 5 | `qa057a3d428a2:chunk-62` | 0.07123268395662308 |  | McKESSON CORPORATION FINANCIAL NOTES (CONTINUED) (UNAUDITED) (4)Represents cross-currency fixed-to-fixed interest rate … |

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
- **S2**: nDCG@5=0.04373502583744726 · skipped= · n_scored=255

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa5c748248a5b:chunk-40` | 0.30049556493759155 |  | ########Years Ended###### ##December 31, 2018##December 31, 2019##December 31, 2020####December 31, 2021##December 31, … |
| 2 | `qa5c748248a5b:chunk-193` | 0.07443264871835709 |  | ##Common Stock Issued##Treasury Stock##Common Stock Outstanding Balance At December 31, 2020##132,829,175##(50,255,768)… |
| 3 | `qa5c748248a5b:chunk-175` | 0.04765770211815834 |  | (in thousands)####Index####Analytics####ESG and Climate####All Other - Private Assets####Total Goodwill at December 31,… |
| 4 | `qa5c748248a5b:chunk-160` | 0.04331411421298981 |  | ##Interest payment frequency##First interest payment date Senior Notes and Tranche A Term Loans#### 4.000% senior unsec… |
| 5 | `qa5c748248a5b:chunk-133` | 0.03070264868438244 | 1.0 | For services where the transaction price is variable such as based upon assets under management (“AUM”), volume of trad… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qa5c748248a5b`)._

### ex-dev-qa602975e3d19

- **example_id**: `dev:qa602975e3d19`
- **state**: `completed`
- **query**: How has the ratio of Mondelez International’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9411655511901171 · gold=['10-Q', '10-K', 'DEF14A', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=189

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qa602975e3d19:chunk-151` | 0.21271391212940216 |  | # FREQUENTLY ASKED QUESTIONS ABOUT THE ANNUAL MEETING AND VOTING (cont.) ## 7. How do I vote my shares? ## If you are a… |
| 2 | `qa602975e3d19:chunk-175` | 0.12091556936502457 |  | # ANNEX B: MONDELEZ INTERNATIONAL, INC. 2024 PERFORMANCE INCENTIVE PLAN (EFFECTIVE MAY 22, 2024) (cont.) ## SECTION 5. … |
| 3 | `qa602975e3d19:chunk-90` | 0.09197386354207993 |  | # 2023 GRANTS OF PLAN-BASED AWARDS <table><tr><th rowspan="2">Name</th><th></th><th></th><th colspan="2">Estimated Futu… |
| 4 | `qa602975e3d19:chunk-68` | 0.06763938069343567 |  | # Back to Contents <table><tr><th>Performance Measures¹</th><th>Threshold</th><th></th><th>Target</th><th>Maximum</th><… |
| 5 | `qa602975e3d19:chunk-159` | 0.05401761457324028 |  | # Back to Contents <table><tr><th>Measures</th><th>Definitions (Including Adjustment to GAAP Measure)</th><th>Modificat… |

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
| 1 | `qaf55b76bfcad:chunk-47` | 0.15330743789672852 |  | Bob, first follow-up on ESPN, clearly a big priority, can you give us some update on types of potential ESPN partners a… |
| 2 | `qaf55b76bfcad:chunk-49` | 0.145587757229805 |  | The first question. |
| 3 | `qaf55b76bfcad:chunk-2` | 0.09386307746171951 |  | Alexia Quadrani - Executives |
| 4 | `qaf55b76bfcad:chunk-8` | 0.09204936027526855 |  | Alexia Quadrani - Executives |
| 5 | `qaf55b76bfcad:chunk-42` | 0.09054693579673767 |  | Alexia Quadrani - Executives |

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
- **S2**: nDCG@5=0.2625111813898523 · skipped= · n_scored=82

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb35a5efa65ce:chunk-13` | 0.11750264465808868 |  | So thanks, Nick, for the question. We won't get ahead of the process in terms of describing the details that is emphasi… |
| 2 | `qb35a5efa65ce:chunk-5` | 0.07951264083385468 | 2.0 | Thanks, Pete, and good morning, everyone. Before we begin, we'd like to extend our deepest sympathies to the family of … |
| 3 | `qb35a5efa65ce:chunk-2` | 0.056938059628009796 |  | Peter Flynn - Executives |
| 4 | `qb35a5efa65ce:chunk-6` | 0.053446751087903976 |  | Kirkland Andrews - Executives |
| 5 | `qb35a5efa65ce:chunk-16` | 0.05220089107751846 |  | Kirkland Andrews - Executives |

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
| 1 | `qb500a9b42ef8:chunk-161` | 0.08310399949550629 |  | ############In Millions########## ######DB Pension Plans############OPEB Plan#### ##Credit######Contribution######Credi… |
| 2 | `qb500a9b42ef8:chunk-37` | 0.0784626305103302 |  | Table of Contents •adverse consequences resulting from any past, present, or future assertion of indemnity or warranty … |
| 3 | `qb500a9b42ef8:chunk-36` | 0.0758596807718277 |  | Table of Contents •national, regional, and local economic, competitive, and regulatory policies, conditions, and develo… |
| 4 | `qb500a9b42ef8:chunk-268` | 0.07295020669698715 |  | ##########Forward Price Per Share#### Contract Date##Maturity Date##Number of Shares##Initial######December 31, 2023## … |
| 5 | `qb500a9b42ef8:chunk-309` | 0.07002865523099899 |  | ####In Millions#### Years Ended December 31##2023####2022## CMS Energy, including Consumers######## Operating lease cos… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb500a9b42ef8`)._

### ex-dev-qb590e4e6d1ec

- **example_id**: `dev:qb590e4e6d1ec`
- **state**: `completed`
- **query**: How has the ratio of PG&E Corporation’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9754666004730318 · gold=['10-Q', '10-K', 'Earnings', '8-K']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=213

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qb590e4e6d1ec:chunk-38` | 0.3715674877166748 |  | ##########Revenue Requirement (in billions)############ Year####Request (1)####PD (2)######Difference Between PD and Re… |
| 2 | `qb590e4e6d1ec:chunk-174` | 0.07158254832029343 |  | ######Three Months Ended September 30,##########Nine Months Ended September 30,#### (in millions)####2023######2022####… |
| 3 | `qb590e4e6d1ec:chunk-129` | 0.047113168984651566 |  | On June 5, 2023, the Utility completed the sale of (i) $850 million aggregate principal amount of 6.100% First Mortgage… |
| 4 | `qb590e4e6d1ec:chunk-41` | 0.03619043901562691 |  | ##########Rate Base (in billions)############ Year####Request####PD######Difference Between PD and Request####APD####Di… |
| 5 | `qb590e4e6d1ec:chunk-8` | 0.03475789353251457 |  | (1) These items impacted earnings for the three months ended September 30, 2023 and 2022. 16 |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qb590e4e6d1ec`)._

### ex-dev-qba0102803c57

- **example_id**: `dev:qba0102803c57`
- **state**: `completed`
- **query**: How are scenario analyses conducted by Kimco Realty Corporation for recessionary or downturn risks?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=332

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba0102803c57:chunk-208` | 0.21187680959701538 |  | Date Issued####Face Amount##Interest Rate##Maturity Date Nov-23##$##7.3##10.50%##Nov-26 Mar-23##$##25.0##8.00%##Apr-24 … |
| 2 | `qba0102803c57:chunk-214` | 0.13153022527694702 |  | Date Paid####Amount Repaid##Interest Rate##Maturity Date Sep-22 (1)##$##299.7##3.500%##Apr-23 Sep-22 (1) (2)##$##350.0#… |
| 3 | `qba0102803c57:chunk-162` | 0.09334594011306763 |  | ####Month##########Purchase Price########## Property Name##Location##Acquired####Cash####Debt######Other####Total##GLA … |
| 4 | `qba0102803c57:chunk-3` | 0.048374708741903305 |  | Business Strategies The Company believes it is well positioned to achieve sustainable growth, with its strong core port… |
| 5 | `qba0102803c57:chunk-212` | 0.03336729854345322 |  | Date Issued####Amount Issued##Interest Rate##Maturity Date Oct-23##$##500.0##6.400%##Mar-34 Aug-22##$##650.0##4.600%##F… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qba0102803c57`)._

### ex-dev-qba50bc033945

- **example_id**: `dev:qba50bc033945`
- **state**: `completed`
- **query**: What commentary is provided by Teledyne Technologies on demand forecasts in light of government defense spending trends?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9754666004730318 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.08750372712995078 · skipped= · n_scored=146

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qba50bc033945:chunk-119` | 0.09734571725130081 |  | Got it. Okay. Great. |
| 2 | `qba50bc033945:chunk-99` | 0.04104241356253624 | 1.0 | Robert, your full year 2024 framework is assuming 4% full year organic revenue growth. Is that correct? |
| 3 | `qba50bc033945:chunk-2` | 0.029131753370165825 |  | Jason VanWees - Executives |
| 4 | `qba50bc033945:chunk-142` | 0.02885723114013672 |  | Jason VanWees - Executives |
| 5 | `qba50bc033945:chunk-12` | 0.02657829225063324 |  | Stephen Blackwood - Executives |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=94

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qbdbd002b0a41:chunk-25` | 0.19085071980953217 |  | My question is more of a medium to long term in nature. So services growth was 5% in 2023. If you want to hit that $28 … |
| 2 | `qbdbd002b0a41:chunk-93` | 0.11003872007131577 |  | Thank you. Ladies and gentlemen, that concludes our call. We thank you for joining. You may now disconnect. |
| 3 | `qbdbd002b0a41:chunk-65` | 0.08434033393859863 |  | So on the price cost, so I think in your full year guide, you talked about price modestly exceeding manufacturing costs… |
| 4 | `qbdbd002b0a41:chunk-21` | 0.08141665905714035 |  | All right. Well, thanks for your question. Maybe just talk about some of the areas that we're most excited about as we … |
| 5 | `qbdbd002b0a41:chunk-89` | 0.07751589268445969 |  | Yes. Really, what we continue to talk about is the fact that we will -- we intend to return essentially all free cash f… |

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
- **S2**: nDCG@5=0.17989452745991058 · skipped= · n_scored=249

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc187429e2dc5:chunk-214` | 0.12425093352794647 |  | ##Stock Awards (in thousands)####Weighted-Average Grant Date Fair Value##Weighted Average Remaining Contractual Term Ou… |
| 2 | `qc187429e2dc5:chunk-227` | 0.08934058994054794 |  | ####Equity Compensation Plan Information#### Plan category##Number of Securities to be Issued Upon Exercise of Outstand… |
| 3 | `qc187429e2dc5:chunk-218` | 0.0881020650267601 |  | Name and Title##Date of Adoption##Duration of Trading Arrangement1##Aggregate Number of Securities to be Sold2##Type Ed… |
| 4 | `qc187429e2dc5:chunk-15` | 0.08069078624248505 | 1.0 | operating results could be adversely affected if we are unable to control costs, particularly if we are unable to negot… |
| 5 | `qc187429e2dc5:chunk-3` | 0.04114276170730591 | 2.0 | C5ISR C5ISR designs, develops, integrates, and manages the sensors, systems and other assets necessary to support integ… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc187429e2dc5`)._

### ex-dev-qc20017b12da3

- **example_id**: `dev:qc20017b12da3`
- **state**: `completed`
- **query**: How does Moderna view the pace of mRNA vaccine development cycles and their effect on market competitiveness?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.955982033547129 · gold=['10-K', 'DEF14A', '10-Q', 'Earnings']
- **S1 ordered**: `['10-K', '10-Q', 'Earnings', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.19441677923204098 · skipped= · n_scored=11

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qc20017b12da3:chunk-0` | 0.4249662160873413 |  | Exhibit 99.1 # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates Third quarter 2023 re… |
| 2 | `qc20017b12da3:chunk-8` | 0.3273128867149353 |  | # MODERNA, INC. # CONDENSED CONSOLIDATED BALANCE SHEETS (Unaudited, in millions) <table><tr><th></th><th>September 30, … |
| 3 | `qc20017b12da3:chunk-6` | 0.09951169788837433 | 1.0 | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## About Moderna In over 1… |
| 4 | `qc20017b12da3:chunk-7` | 0.08933485299348831 |  | # Moderna Reports Third Quarter 2023 Financial Results and Provides Business Updates (cont.) ## About Moderna (cont.) M… |
| 5 | `qc20017b12da3:chunk-10` | 0.04031693935394287 | 1.0 | # (Unaudited, in millions) (cont.) ## Forward-Looking Statements This press release contains forward-looking statements… |

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
| 1 | `qc8e6b0d72c52:chunk-119` | 0.08525034785270691 |  | That's fair. |
| 2 | `qc8e6b0d72c52:chunk-15` | 0.07744933664798737 |  | Going back to your comments on F1. Can F1 be a successful non-high-end event? Can it be a pretty good growth driver at … |
| 3 | `qc8e6b0d72c52:chunk-4` | 0.03560676798224449 |  | Anthony Carano - Executives |
| 4 | `qc8e6b0d72c52:chunk-107` | 0.03479567542672157 |  | It's Shaun Kelley on for Julie. Two questions, if I could. First, on the regional side. Tom, you've been calling out fo… |
| 5 | `qc8e6b0d72c52:chunk-2` | 0.032121989876031876 |  | Brian Agnew - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qc8e6b0d72c52`)._

### ex-dev-qcbbca1138c08

- **example_id**: `dev:qcbbca1138c08`
- **state**: `completed`
- **query**: What investor views emerged on Freeport-McMoRan’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9437153337836448 · gold=['Earnings', '10-K', '10-Q', 'DEF14A']
- **S1 ordered**: `['Earnings', 'DEF14A', '10-Q', '10-K', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=118

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcbbca1138c08:chunk-41` | 0.16049839556217194 |  | Two questions from my side. So firstly, can you give an update on the status of the negotiations over a concentrate exp… |
| 2 | `qcbbca1138c08:chunk-67` | 0.07223309576511383 |  | Correct. And your $4 is absolutely right. I mean you just look at recent projects and look at how costs escalate and th… |
| 3 | `qcbbca1138c08:chunk-2` | 0.033073559403419495 |  | Kathleen Quirk - Executives |
| 4 | `qcbbca1138c08:chunk-12` | 0.03270832076668739 |  | Kathleen Quirk - Executives |
| 5 | `qcbbca1138c08:chunk-6` | 0.03270832076668739 |  | Kathleen Quirk - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qcbbca1138c08`)._

### ex-dev-qcdb8bc16cf2f

- **example_id**: `dev:qcdb8bc16cf2f`
- **state**: `completed`
- **query**: What guidance was offered on Jack Henry & Associates’ technology platform modernization targets?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9499797323370371 · gold=['Earnings', '10-K', '10-Q']
- **S1 ordered**: `['Earnings', '10-Q', '8-K', '10-K', 'DEF14A']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=126

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qcdb8bc16cf2f:chunk-115` | 0.27558499574661255 |  | Yes, it's a great question, James. And so I have a couple of different reference points for you, too. So I know Northco… |
| 2 | `qcdb8bc16cf2f:chunk-41` | 0.11769118160009384 |  | Greg, I wanted to circle back to core wins. I think you called out 15 were greater than $1 billion in assets versus 5 j… |
| 3 | `qcdb8bc16cf2f:chunk-97` | 0.10815863311290741 |  | Got it. I'm sorry if I cut you off. But my follow-up was around sort of a follow-up to Kartik's question around segment… |
| 4 | `qcdb8bc16cf2f:chunk-75` | 0.09311293810606003 |  | And Kartik, this is Mimi, if I could just add on. The tremendous fourth quarter that Greg talked about, the step up of … |
| 5 | `qcdb8bc16cf2f:chunk-71` | 0.0449659638106823 |  | Greg, I wanted to just get your perspective on the core business. I know the focus should be the year, but after saying… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=221

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd177bdad4bdd:chunk-120` | 0.09911955147981644 |  | ############2023######## ####Aeronautics####MFC####RMS####Space####Total Net sales#################### Products##$##22,… |
| 2 | `qd177bdad4bdd:chunk-5` | 0.07394556701183319 |  | (a)Based on employees who self-identify. Includes only U.S. employees and expatriates except for data relating to women… |
| 3 | `qd177bdad4bdd:chunk-99` | 0.06977856159210205 |  | ####Common Stock######Additional Paid-In Capital####Retained Earnings######Accumulated Other Comprehensive Loss######To… |
| 4 | `qd177bdad4bdd:chunk-80` | 0.05752958729863167 |  | working capital, long term business plans and recent operating performance. The discount rates utilized in the DCF anal… |
| 5 | `qd177bdad4bdd:chunk-121` | 0.05533705651760101 |  | ############2022######## ####Aeronautics####MFC####RMS####Space####Total Net sales#################### Products##$##22,… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=312

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd422350b37cb:chunk-149` | 0.21057848632335663 |  | Intangible assets deemed to have an indefinite life that are therefore not amortized consist of the following: |
| 2 | `qd422350b37cb:chunk-202` | 0.15845534205436707 |  | ####Percentage of Plan Assets#### ##2023###### ##Target####December 31## Asset Class##Allocation##2023####2022 Equity s… |
| 3 | `qd422350b37cb:chunk-82` | 0.05576380342245102 |  | Part II ♦ Item 7 – Management’s Discussion and Analysis of Financial Condition and Results of Operations Other Financia… |
| 4 | `qd422350b37cb:chunk-165` | 0.05347207188606262 |  | ####Principal Amount (in millions)##Effective Interest Rate##Maturity Date 4.250% Senior Notes##$##400.0##4.40%##July 2… |
| 5 | `qd422350b37cb:chunk-255` | 0.03971562907099724 |  | (in millions)####Contracts of Affreightment####Royalty Commitments 2024##$##16.9##$##26.4 2025####17.1####14.1 2026####… |

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
- **S2**: nDCG@5=0.13120507751234178 · skipped= · n_scored=120

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qd87c2da5e7da:chunk-7` | 0.18401135504245758 |  | # 2024 Director Nominees Snapshot (Page 10) (cont.) ## Betsy D. Holden Former Co-CEO of Kraft Foods Inc. - Independent … |
| 2 | `qd87c2da5e7da:chunk-53` | 0.12860722839832306 |  | # Executive Compensation (cont.) ## Conversion of J&J Long-Term Incentive Awards (Approved by the J&J CBC) Prior to Sep… |
| 3 | `qd87c2da5e7da:chunk-97` | 0.07811261713504791 |  | # Certain Relationships and Related Person Transactions (cont.) ## Cross-Licenses Pursuant to the Intellectual Property… |
| 4 | `qd87c2da5e7da:chunk-82` | 0.07398940622806549 |  | # Approve, on a Non-Binding Advisory Basis, the Frequency of Future Advisory Votes on Named Executive Officer Compensat… |
| 5 | `qd87c2da5e7da:chunk-43` | 0.06269597262144089 | 1.0 | # Compensation Philosophy and Design (cont.) ## Kenvue Compensation Peer Group (informed post-Separation 2023 and 2024 … |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=227

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdbaa829dd4cc:chunk-202` | 0.08170687407255173 |  | (In millions)####March 29, 2024 2025##$##324 2026####73 2027####47 2028####36 2029####28 Thereafter####2 Total purchase… |
| 2 | `qdbaa829dd4cc:chunk-103` | 0.0659320279955864 |  | Accounts receivable, net: |
| 3 | `qdbaa829dd4cc:chunk-104` | 0.06224745884537697 |  | (In millions)####March 29, 2024####March 31, 2023 Accounts receivable##$##165##$##169 Allowance for doubtful accounts##… |
| 4 | `qdbaa829dd4cc:chunk-150` | 0.040181856602430344 |  | As of March 29, 2024, we estimate that $12 million of net deferred gains related to our interest rate hedges will be re… |
| 5 | `qdbaa829dd4cc:chunk-36` | 0.03946191072463989 |  | (1) Non-GAAP Direct customer revenue differs from U.S. GAAP direct customer revenue in fiscal 2023 because it excludes … |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qdbaa829dd4cc`)._

### ex-dev-qdec70f55027f

- **example_id**: `dev:qdec70f55027f`
- **state**: `completed`
- **query**: What investor views emerged on Mettler-Toledo International Inc.’s international or geographic expansion prospects?
- **S1**: top1=`Earnings` in_gold=True · nDCG@5=0.9734136950814526 · gold=['Earnings', '10-K', '10-Q', '8-K']
- **S1 ordered**: `['Earnings', '10-Q', '10-K', 'DEF14A', '8-K']`
- **S2**: nDCG@5=0.3672919835537663 · skipped= · n_scored=136

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdec70f55027f:chunk-15` | 0.5101231336593628 | 1.0 | Yes, sure. So let me start with the Lab business. So we expect Lab in Q4 -- I mean, I'm sorry, in Q1 2024 to be down lo… |
| 2 | `qdec70f55027f:chunk-69` | 0.05603843554854393 |  | Two questions. First off, what was the pricing benefit in Q4? And what is your outlook for 2024? |
| 3 | `qdec70f55027f:chunk-109` | 0.029993783682584763 |  | Patrick, the service business remains pretty healthy. I mean you grew 10% last year against the double-digit comp. Wher… |
| 4 | `qdec70f55027f:chunk-101` | 0.029447220265865326 | 1.0 | Yes. Thanks, Rachel. And I'll start and then Shawn if you have some additional comments, feel free to chime in. So I th… |
| 5 | `qdec70f55027f:chunk-123` | 0.025100257247686386 | 1.0 | Shawn, I wanted to pick up on that kind of the ramp question. I think Rachel and Brandon both hit on a little bit there… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qdec70f55027f`)._

### ex-dev-qdfe52ef66df5

- **example_id**: `dev:qdfe52ef66df5`
- **state**: `completed`
- **query**: How has the ratio of IDEXX Laboratories’ recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9452713619732751 · gold=['10-Q', '10-K', '8-K', 'DEF14A']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.3716702184910473 · skipped= · n_scored=271

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qdfe52ef66df5:chunk-61` | 0.09645787626504898 | 2.0 | ######For the Years Ended December 31,######################## Net Revenue (dollars in thousands)####2023######2022####… |
| 2 | `qdfe52ef66df5:chunk-79` | 0.08282770961523056 |  | ######For the Three Months Ended#### ##December 31, 2023##September 30, 2023##June 30, 2023##March 31, 2023##December 3… |
| 3 | `qdfe52ef66df5:chunk-40` | 0.05826789513230324 |  | ##2018##2019##2020##2021##2022##2023 IDEXX Laboratories, Inc.##$100.00##$140.38##$268.72##$353.97##$219.31##$298.38 NAS… |
| 4 | `qdfe52ef66df5:chunk-68` | 0.05510195344686508 |  | Revenue. The increase in our Water business revenue was primarily due to higher realized price and, to a lesser extent,… |
| 5 | `qdfe52ef66df5:chunk-50` | 0.04671378433704376 |  | determination was made. Likewise, should we determine that we would not be able to realize all or part of our net defer… |

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
| 1 | `qe1811f4fd3dc:chunk-39` | 0.14215852320194244 |  | I'll stick to one. Andy, you mentioned demand for large blocks of capacity in several key markets such as NOVA and Sili… |
| 2 | `qe1811f4fd3dc:chunk-91` | 0.10914629697799683 |  | I was wondering if you could expand a little bit on the assumptions you're making about the broader lease environment a… |
| 3 | `qe1811f4fd3dc:chunk-19` | 0.036667536944150925 |  | Maybe first, last night, we heard from one of your peers that the higher power prices in 2023 have created some sort of… |
| 4 | `qe1811f4fd3dc:chunk-4` | 0.02870611660182476 |  | Andrew Power - Executives |
| 5 | `qe1811f4fd3dc:chunk-12` | 0.028493426740169525 |  | Andrew Power - Executives |

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
- **S2**: nDCG@5=0.21398626473452753 · skipped= · n_scored=140

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qeccd6f3b9d06:chunk-79` | 0.25849679112434387 |  | Two if I may. Just first on Gecko. Presumably, the PoPs that you have, they are already supporting security and deliver… |
| 2 | `qeccd6f3b9d06:chunk-115` | 0.1481172740459442 | 2.0 | Sure. Why don't I go to the first one. On the spirit of it being a year-end call, I'll break out these numbers at a hig… |
| 3 | `qeccd6f3b9d06:chunk-117` | 0.05667255446314812 |  | Just to be clear, is this the full year growth rate? Or is this the fourth quarter growth rate? |
| 4 | `qeccd6f3b9d06:chunk-87` | 0.04170403257012367 |  | Maybe, Tom, just a follow-up to a prior question. As we think about Gecko and you mentioned that your edge sites right … |
| 5 | `qeccd6f3b9d06:chunk-25` | 0.039588797837495804 |  | Sure. Happy to do that. Yes. I would say, just as a reminder, when we acquired the businesses, we actually acquired sel… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=74

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf25e1308bae4:chunk-59` | 0.14511246979236603 |  | I wanted to ask about the China business. I know that in the prepared comments, you said that you started shipping some… |
| 2 | `qf25e1308bae4:chunk-41` | 0.08106851577758789 |  | I wanted to ask about how you're converting backlog into revenue. Obviously, lead times for your products have come dow… |
| 3 | `qf25e1308bae4:chunk-9` | 0.04705669730901718 |  | Congratulations on the really strong results. My question is for Jensen on the Data Center business. Clearly, you're do… |
| 4 | `qf25e1308bae4:chunk-10` | 0.04612163454294205 |  | Jensen Huang;Co-Founder, CEO, President & Director - Executives |
| 5 | `qf25e1308bae4:chunk-16` | 0.04584956169128418 |  | Jensen Huang;Co-Founder, CEO, President & Director - Executives |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=25

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf5b4bbe60015:chunk-23` | 0.142050638794899 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 2 | `qf5b4bbe60015:chunk-21` | 0.12485098838806152 |  | <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td>… |
| 3 | `qf5b4bbe60015:chunk-3` | 0.11390645056962967 |  | In addition, the timing and amount of Cadence’s repurchases of its common stock are subject to business and market cond… |
| 4 | `qf5b4bbe60015:chunk-22` | 0.10452345013618469 |  | † The non-GAAP measures presented in the table above should not be considered a substitute for financial results and me… |
| 5 | `qf5b4bbe60015:chunk-6` | 0.08436521887779236 |  | [Chunk Index 7] <table><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><t… |

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
| 1 | `qf7a3126727b8:chunk-13` | 0.3587602376937866 |  | # Governance Highlights <table><tr><th></th><th>BOARD COMPOSITION AND ACCOUNTABILITY:</th></tr><tr><td>Board Leadership… |
| 2 | `qf7a3126727b8:chunk-19` | 0.08912500739097595 |  | # CORPORATE GOVERNANCE (cont.) ## Corporate Governance and Nominating <table><tr><th>and Nominating Committee</th><th>P… |
| 3 | `qf7a3126727b8:chunk-101` | 0.070517398416996 |  | # GRANTS OF PLAN-BASED AWARDS (cont.) ## OUTSTANDING EQUITY AWARDS AT YEAR-END (cont.) <table><tr><th rowspan="2">Name<… |
| 4 | `qf7a3126727b8:chunk-80` | 0.05143982544541359 |  | # COMPENSATION DISCUSSION AND ANALYSIS (cont.) ## Progress on Scope 1 and 2 Emissions Reductions Goals The Committee de… |
| 5 | `qf7a3126727b8:chunk-147` | 0.04031447693705559 |  | # Adjusted Operating Income and Adjusted Earnings Per Share Non-GAAP Reconciliations (Pay Versus Performance) <table><t… |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qf7a3126727b8`)._

### ex-dev-qf8cbcec9fec6

- **example_id**: `dev:qf8cbcec9fec6`
- **state**: `completed`
- **query**: How has the ratio of Ingersoll Rand’s recurring to one-time revenue evolved in the latest reporting period?
- **S1**: top1=`10-Q` in_gold=True · nDCG@5=0.9688823411593558 · gold=['10-Q', '10-K', 'DEF14A', 'Earnings']
- **S1 ordered**: `['10-Q', 'Earnings', '10-K', '8-K', 'DEF14A']`
- **S2**: nDCG@5=0.43067655807339306 · skipped= · n_scored=117

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qf8cbcec9fec6:chunk-66` | 0.53426194190979 |  | # Long-Term Equity Incentive Awards (cont.) ## Rationale The Committee believes that Mr. Reynal's vision and leadership… |
| 2 | `qf8cbcec9fec6:chunk-63` | 0.07734064012765884 |  | # Long-Term Equity Incentive Awards 2023 Annual PSU, RSU and Stock Option Awards Our long-term incentive awards, establ… |
| 3 | `qf8cbcec9fec6:chunk-57` | 0.0654955729842186 |  | # Compensation Discussion and Analysis (cont.) ## Compensation Elements (cont.) CEO Target Compensation Mix Other NEO A… |
| 4 | `qf8cbcec9fec6:chunk-113` | 0.04393333941698074 | 1.0 | # INGERSOLL RAND INC. AND SUBSIDIARIES ADJUSTED COMBINED FINANCIAL INFORMATION BY SEGMENT (Unaudited; in millions, exce… |
| 5 | `qf8cbcec9fec6:chunk-29` | 0.04155464842915535 |  | # THE BOARD OF DIRECTORS AND CERTAIN GOVERNANCE MATTERS (cont.) ## Commitment to Sustainability Guided by our mission o… |

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
- **S2**: nDCG@5=0.0 · skipped= · n_scored=74

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qfbef9973c7fb:chunk-2` | 0.12670369446277618 |  | Simona Stefan Jankowski - Executives |
| 2 | `qfbef9973c7fb:chunk-10` | 0.05270645394921303 |  | Jensen Huang;Co-Founder, CEO, President & Director - Executives |
| 3 | `qfbef9973c7fb:chunk-16` | 0.052501775324344635 |  | Jensen Huang;Co-Founder, CEO, President & Director - Executives |
| 4 | `qfbef9973c7fb:chunk-22` | 0.052501775324344635 |  | Jensen Huang;Co-Founder, CEO, President & Director - Executives |
| 5 | `qfbef9973c7fb:chunk-28` | 0.05227654427289963 |  | Jensen Huang;Co-Founder, CEO, President & Director - Executives |

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
| 1 | `qff56bedc2f87:chunk-65` | 0.045338425785303116 |  | You talked about an acceleration in recruiting in the second half of '23. I guess as we think about '24, is the plan to… |
| 2 | `qff56bedc2f87:chunk-2` | 0.04522399231791496 |  | Stephen Mota - Executives |
| 3 | `qff56bedc2f87:chunk-110` | 0.04360029101371765 |  | Stephen Mota - Executives |
| 4 | `qff56bedc2f87:chunk-39` | 0.040006138384342194 |  | Yes. For 2024, we have about $70 million of our total direct commercial mortgage loans maturing. Of that is about $4 mi… |
| 5 | `qff56bedc2f87:chunk-4` | 0.0399649553000927 |  | Frank Svoboda - Executives |

_Full I/O traces & longer passage text: [download HTML](https://raw.githubusercontent.com/caldeirav/finagent-mesh-mcp/main/artifacts/benchmarks/paper-n200-full.inspect.html) (search for `dev:qff56bedc2f87`)._

### ex-dev-qff73996028bf

- **example_id**: `dev:qff73996028bf`
- **state**: `completed`
- **query**: How has Williams-Sonoma’s management addressed supply-chain risks and efforts to enhance Williams-Sonoma’s resilience?
- **S1**: top1=`10-K` in_gold=True · nDCG@5=0.9506817003345661 · gold=['10-K', 'Earnings', '10-Q', '8-K']
- **S1 ordered**: `['10-K', '10-Q', 'DEF14A', 'Earnings', '8-K']`
- **S2**: nDCG@5=0.0 · skipped= · n_scored=147

| Rank | Chunk | Score | Gold | Text |
|---:|---|---:|---:|---|
| 1 | `qff73996028bf:chunk-47` | 0.16117405891418457 |  | ####Fiscal 2023######Fiscal 2022## ##Store Count####Avg. LSF Per Store##Store Count####Avg. LSF Per Store Pottery Barn#… |
| 2 | `qff73996028bf:chunk-136` | 0.11910279840230942 |  | ##STOCK PLANS## 10.3+####Williams-Sonoma, Inc. 2001 Long-Term Incentive Plan, as amended (incorporated by reference to … |
| 3 | `qff73996028bf:chunk-5` | 0.07111790776252747 |  | Table of Contents domain names, trade secrets and other intellectual property and proprietary technology that we hold a… |
| 4 | `qff73996028bf:chunk-23` | 0.07004617899656296 |  | Table of Contents cause delays in locating and shipping products, and increases in costs associated with inventory that… |
| 5 | `qff73996028bf:chunk-36` | 0.051357451826334 |  | Notes: A.The lines represent monthly index levels derived from compounded daily returns that include all dividends. B.T… |

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
| 1 | `chunk_q0b530d:10-K:chunk-2` | 0.06097594276070595 |  | Susanne Perram - Executives |
| 2 | `chunk_q0b530d:10-K:chunk-86` | 0.05875486508011818 |  | Susanne Perram - Executives |
| 3 | `chunk_q0b530d:10-K:chunk-12` | 0.05840480327606201 |  | Leanne Cunningham - Executives |
| 4 | `chunk_q0b530d:10-K:chunk-6` | 0.05840480327606201 |  | Leanne Cunningham - Executives |
| 5 | `chunk_q0b530d:10-K:chunk-22` | 0.05793990194797516 |  | Leanne Cunningham - Executives |

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
| 1 | `chunk_q29280e:10-K:chunk-40` | 0.2880989909172058 |  | # 2023 Elements of Compensation (cont.) ## Performance Levels and Achievement The following table summarizes the perfor… |
| 2 | `chunk_q29280e:10-K:chunk-34` | 0.08980385959148407 |  | # Compensation Discussion & Analysis (cont.) ## Fiscal 2023 Business and Performance Highlights Over the past twelve ye… |
| 3 | `chunk_q29280e:10-K:chunk-15` | 0.07161550223827362 |  | # Board Leadership Structure The Company's Corporate Governance Guidelines provide that our Board has the right to exer… |
| 4 | `chunk_q29280e:10-K:chunk-49` | 0.07116560637950897 |  | # Named Executive Officer Compensation and Related Matters (cont.) ## Summary Compensation Table for Fiscal Year 2023(a… |
| 5 | `chunk_q29280e:10-K:chunk-69` | 0.048530545085668564 |  | # CEO Pay Ratio Our chief executive officer ("CEO") to median employee pay ratio is calculated in accordance with SEC r… |

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
| 1 | `chunk_q2ccba5:Earnings:chunk-27` | 0.2611890137195587 |  | Congrats on a strong finish here and the approval of FARAPULSE in the U.S. On FARAPULSE, can you talk about the manufac… |
| 2 | `chunk_q2ccba5:Earnings:chunk-37` | 0.10079861432313919 |  | Congrats on a really strong finish year. Maybe just one on the guidance here, perhaps for Dan. Dan, the 8% to 9%, it lo… |
| 3 | `chunk_q2ccba5:Earnings:chunk-19` | 0.09713751822710037 |  | I don't want to leave FARAPULSE quite yet, and I suspect there will be a lot of questions on it this call. But if you'r… |
| 4 | `chunk_q2ccba5:Earnings:chunk-13` | 0.06163470819592476 |  | Great. Congrats on a really good quarter. And congratulations, Lauren, on the promotion. Wanted to ask on two of the bi… |
| 5 | `chunk_q2ccba5:Earnings:chunk-47` | 0.04757557809352875 |  | Just a follow-up question on ACURATE neo2, Mike, if I could. So appreciate the comments that you did provide. Just curi… |

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
| 1 | `chunk_q44d295:10-Q:chunk-9` | 0.27782267332077026 |  | Defense - Amphenol is a world leader in the design, manufacture and supply of high-performance interconnect systems for… |
| 2 | `chunk_q44d295:10-Q:chunk-212` | 0.12997911870479584 |  | Net sales by geography:####2023####2022####2021 United States:############ Harsh Environment Solutions##$##1,790.5##$##… |
| 3 | `chunk_q44d295:10-Q:chunk-3` | 0.039911024272441864 |  | For further details related to the Company’s reportable business segments, information regarding the Company’s operatio… |
| 4 | `chunk_q44d295:10-Q:chunk-38` | 0.03718385472893715 |  | ####2023####2022 First Quarter##$##0.21##$##0.20 Second Quarter####0.21####0.20 Third Quarter####0.21####0.20 Fourth Qu… |
| 5 | `chunk_q44d295:10-Q:chunk-211` | 0.03708313778042793 |  | Net sales by sales channel:####2023####2022####2021 End customers and contract manufacturers:############ Harsh Environ… |

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
| 1 | `chunk_q5ebb5e:Earnings:chunk-106` | 0.3384338617324829 |  | # Appendix C: Short-Term Incentive Plan Performance Targets As described in the the Compensation Discussion and Analysi… |
| 2 | `chunk_q5ebb5e:Earnings:chunk-47` | 0.2672823965549469 |  | # Overview of AES Total Compensation (cont.) ## 2023 Performance Incentive Plan Payouts (cont.) In early 2024, the Comp… |
| 3 | `chunk_q5ebb5e:Earnings:chunk-49` | 0.1278093308210373 |  | # Overview of AES Total Compensation (cont.) ## Long-Term Compensation 2023 Long-term Compensation Mix: In 2023, we uti… |
| 4 | `chunk_q5ebb5e:Earnings:chunk-45` | 0.09649596363306046 |  | # Overview of AES Total Compensation (cont.) ## Compensation Mix The Company does not target a specific allocation of c… |
| 5 | `chunk_q5ebb5e:Earnings:chunk-7` | 0.0316164493560791 |  | # CAUTIONARY NOTE REGARDING FORWARD-LOOKING STATEMENTS (cont.) 2024 Proxy Statement I 4 aes - our ability to achieve re… |

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
| 1 | `chunk_q829eae:10-Q:chunk-22` | 0.3737797737121582 |  | Inventories Inventories, consisting of products available for sale, are primarily accounted for using the first-in, fir… |
| 2 | `chunk_q829eae:10-Q:chunk-73` | 0.11208678781986237 |  | Operating income increased from $2.5 billion in Q3 2022 to $11.2 billion in Q3 2023, and increased from $9.5 billion fo… |
| 3 | `chunk_q829eae:10-Q:chunk-35` | 0.04318685457110405 |  | 12 |
| 4 | `chunk_q829eae:10-Q:chunk-28` | 0.03959187865257263 |  | Actual maturities may differ from the contractual maturities because borrowers may have certain prepayment conditions. … |
| 5 | `chunk_q829eae:10-Q:chunk-89` | 0.03247193247079849 |  | Table of Contents Guidance We provided guidance on October 26, 2023, in our earnings release furnished on Form 8-K as s… |

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
| 1 | `chunk_q8fc814:Earnings:chunk-9` | 0.37482601404190063 |  | Great. Thank you, Scott. And good morning, everyone. So as demonstrated by our results, 2023 was a very successful year… |
| 2 | `chunk_q8fc814:Earnings:chunk-37` | 0.11153432726860046 |  | My question is on the retirement services growth guide run rating at $80 billion in 4Q but guiding to $70 billion for 2… |
| 3 | `chunk_q8fc814:Earnings:chunk-39` | 0.06180717796087265 |  | I think you're hearing from us. In a week or 2, on the fixed income call, you'll hear from Jim Belardi. And if you look… |
| 4 | `chunk_q8fc814:Earnings:chunk-8` | 0.05340952053666115 |  | Martin Kelly - Executives |
| 5 | `chunk_q8fc814:Earnings:chunk-44` | 0.05295831337571144 |  | Martin Kelly - Executives |

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
| 1 | `chunk_q9fad72:10-Q:chunk-3` | 0.257811039686203 |  | In our US business, which represents approximately 90% of our Net sales, we currently have five dedicated customer chan… |
| 2 | `chunk_q9fad72:10-Q:chunk-2` | 0.25623396039009094 |  | Customers We provide integrated IT solutions to over 250,000 small, medium and large business, government, education an… |
| 3 | `chunk_q9fad72:10-Q:chunk-100` | 0.23747223615646362 |  | CDW CORPORATION AND SUBSIDIARIES NOTES TO CONSOLIDATED FINANCIAL STATEMENTS (dollars in millions, except per share data… |
| 4 | `chunk_q9fad72:10-Q:chunk-11` | 0.059222105890512466 |  | 9 |
| 5 | `chunk_q9fad72:10-Q:chunk-1` | 0.03312075510621071 |  | ##Our value proposition to our customers######Our value proposition to our vendor partners## ●####Broad selection of pr… |

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
