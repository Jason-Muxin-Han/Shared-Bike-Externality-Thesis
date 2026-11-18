Quantitative Analysis of Shared Bike Externalities and Optimal Deployment at Metro Station Areas in Haidian District, Beijing: An Empirical Study Based on Multiple Metro Station Exits in Haidian District

Jason Han

Abstract

This study quantifies the externalities of shared bicycle deployment and derives optimal deployment densities at metro station exits in Beijing's Haidian District. Using a microeconomic framework that combines marginal analysis with field survey data from ten exit–period observations at five stations, we estimate private and social cost and benefit functions. The model incorporates four marginal functions—marginal private cost, marginal external cost, marginal private revenue, and marginal external benefit—calibrated against local operational data, government reports, and on-site measurements collected in June 2026. Results indicate that observed parking densities markedly exceed both the private and the social optimum, with the most severe over-deployment at Wudaokou B during the morning peak (3.773 vehicles/m², roughly 15.5 times the social optimal density). The Pearson correlation between parking density and illegal parking rate is 0.932, confirming density as a primary driver of negative externalities. Total welfare loss across all observed two-hour peak periods is approximately 1,777 yuan, with Wudaokou B AM accounting for more than half. We trace the divergence between observed and optimal densities to stock accumulation, competitive over-presence, delayed dispatch (half-life of about 5.8 days), and incomplete internalization of external costs by platform firms. Policy recommendations include exit-specific density caps, dynamic pre-peak reduction and post-peak clearing at tidal accumulation points, and platform accountability metrics tied to excess density duration and illegal parking rates.

**Keyword**: Shared bicycles; externalities; optimal deployment quantity; market failure; public space occupation

1.  Introduction

    1.1 Research Background

    Currently, shared bicycles have been deployed in over 65 countries and 2,500 cities worldwide (Industry Research, 2026). As the largest market globally, China has deployed a cumulative total of 35 million bicycles by the end of 2025, with annual rides exceeding 40 billion (China Bicycle Association, 2026), and an average daily ridership reaching 120 million (People's Daily, 2026).

    Haidian District leads the city in shared bicycle usage intensity, with approximately 60,500 registered vehicles and a daily turnover rate of about 3.84 rides (Beijing Municipal Commission of Transport, 2026a). Meituan's shared bikes alone account for an average of 300,000 daily rides (Haidian District Integrated Media Center, 2026). Although over 3,000 new non-motorized vehicle parking spaces have been added (Beijing Youth Daily, 2026), excessive deployment by companies remains a persistent issue (Beijing Municipal Commission of Transport, 2026b). On April 14,2026, the Beijing Municipal Transport Commission announced that Hello Bike was under investigation for illegally deploying an excessive number of shared bikes in the central urban area and refusing to rectify the situation, leading to a reduction in its operational scale—a reflection of the continued tendency among companies to deploy bikes excessively in pursuit of market share (CCTV News, 2026).

    1.2 Research Question and Significance

    With the rapid development of the shared bicycle industry, while it has greatly facilitated daily commuting, it has also given rise to a series of issues such as excessive deployment, disorderly parking, and occupation of public spaces. Although existing research has extensively examined the externalities of shared bicycles, there remain shortcomings in quantitative methodologies and local applicability. Based on this, this study raises three core questions: (1) How can the positive and negative externalities of shared bicycles be scientifically quantified, particularly given the unique scenario where all vehicles within the study area are operational, and how can the costs associated with public space occupation and disorderly parking management be accurately calculated? (2) Why does enterprises' voluntary deployment practices inevitably lead to over-deployment, and what underlying market failure mechanisms underlie this phenomenon? (3) Considering both the maximization of overall social welfare and the maximum capacity of public spaces, what is the optimal deployment density for shared bicycles in subway station areas of Haidian District?

    1.3 Research Methods

    This study uses exit points of major subway stations in Haidian District's three key commercial areas—Zhongguancun, Wudaokou, and Shiji Jinyuan (Exit B at Wudaokou Station, Exit D at Zhongguancun Station, Exit A1 at Haidian Huangzhuang Station, and Exits B and C at Changchunqiao Station)—as samples, combining local official data with field survey results to calculate the net externality of shared bicycles and determine their optimal deployment scale.

    The findings provide a scientific quantitative basis for the Haidian District Transportation Bureau and Urban Management Commission in establishing shared bicycle deployment quotas, parking management policies, and corporate performance evaluation mechanisms, thereby helping address current issues of excessive deployment and disorderly parking while fostering the healthy and sustainable development of the shared bicycle industry.

2.  Literature Review

    2.1 Research Status of Externalities of Shared Bicycles

    Research on the externalities of shared bicycles stands as a central topic in the sharing economy field, with scholars widely agreeing that they exhibit both significant positive and negative externalities. Regarding positive externalities, existing studies primarily focus on four dimensions: reduction in carbon emissions, alleviation of traffic congestion, promotion of consumer spending, and improvement in health benefits. Dai (2026) employed a quasi-experimental approach to demonstrate that each kilometer traveled by shared bicycle replaces approximately 0.8 kilometers of private car travel and reduces CO₂ emissions by about 0.18 kg—a finding adopted by official institutions such as Shenzhen Carbon Inclusive. Chen et al. (2024) further revealed that the introduction of shared bicycles led to a significant increase in per capita household expenditure among local residents by 3.9%–6.8%, primarily through reduced commuting time costs. Li and Xia (2026) confirmed the health-related benefits of shared bicycles, revealing an additional 0.53 exercise sessions per week and an extra 12.6 minutes of physical activity time for users.

    Regarding negative externalities, existing research primarily focuses on three aspects: the occupation of public space by improperly parked bicycles, increased traffic accident risks, and pollution caused by waste vehicle disposal. Wu and Jiang (2025) noted that by the end of 2025, the total number of shared bicycles deployed in major Chinese cities had exceeded 18 million; in some key commercial areas and subway stations, the bicycle density during peak hours reached over 100 bicycles per 100 meters, significantly impairing residents' travel experience and urban operational efficiency. A report released by the Beijing Municipal Transport Commission (2025) indicates that the annual cost for removing improperly parked shared bicycles in Beijing exceeds 200 million yuan, a cost ultimately borne by all taxpayers.

    2.2 Research Status of the Optimal Deployment Quantity of Shared Bicycles

    Research on the optimal deployment scale of shared bicycles has primarily been conducted from both corporate and governmental perspectives in existing literature. From a corporate standpoint, studies predominantly aim at profit maximization, employing methods such as game theory, dynamic programming, and machine learning to investigate optimal deployment strategies. Wu and Jiang (2025) utilized evolutionary game theory to analyze the interaction between governments and enterprises in deployment decision-making, concluding that government regulation is crucial for addressing over-deployment issues. Some studies have also incorporated AI-based scheduling algorithms to optimize deployment and operation plans by predicting demand across different regions; for instance, Zhang et al. (2026) combined time graph convolutional networks (T-GCN) with genetic algorithms to achieve integrated decision-making for demand forecasting and scheduling optimization.

    From a governmental perspective, most studies aim to maximize social welfare by comprehensively considering factors such as supply-demand balance, spatial capacity, and environmental benefits. The report released by the Kunming Municipal Transportation Bureau (2025) employed the "spatial capacity method" to determine the optimal deployment scale for urban shared bicycles, providing a basis for policymakers to establish allocation quotas.

    2.3 The Gaps and Deficiencies in Current Research

    Through a review of the aforementioned literature, this study identifies three significant gaps in existing research: an overemphasis on macro-level analyses coupled with insufficient attention to micro-level nodes. Most studies analyze the externalities and optimal deployment quantities of shared bicycles at the city-wide level, while critical micro-level nodes such as subway station exits receive inadequate investigation. In reality, the externalities of shared bicycles vary significantly across regions: in residential and office areas, they primarily serve as connectivity solutions for initial and final segments of travel journeys, exhibiting significant positive externalities; whereas at transportation hubs like subway station exits, excessive vehicle deployment leads to severe congestion issues, resulting in pronounced negative externalities. Existing research fails to capture these spatial disparities, making government-imposed "one-size-fits-all" deployment policies less likely to yield desired outcomes.

    This study disregards all vehicle availability scenarios. Existing research typically assumes a 15%-30% damage and idleness rate for shared bicycles when constructing cost models, thereby incorporating substantial vehicle maintenance and disposal costs into private marginal costs: for instance, Niu and Chai (2022) employed three different vehicle wear assumptions of 5%,10%, and 15% in their carbon emission accounting analysis; Wu and Jiang (2025) set an industry-wide average vehicle damage rate of 20% in their evolutionary game model. However, our preliminary survey revealed that the operational quality of shared bicycles in the study area is exceptionally high—all vehicles parked near subway stations are functioning normally with no significant damage or idleness issues. This unique situation significantly reduces the applicability of existing models in this context.

    Third, there are numerous complex models while few simplified and practical models exist. Current research on optimal allocation quantities predominantly employs sophisticated mathematical models and econometric methods; although these approaches offer high precision, they remain difficult for urban managers and the general public to comprehend and apply.

3.  Theoretical Foundation

    3.1 Foundations of Microeconomic Theory

    The externality theory refers to the uncompensated impacts of economic activities on third parties not involved in the transactions, categorized into positive externalities (e.g., carbon reduction from shared bicycles) and negative externalities (e.g., unauthorized parking occupying public space). Externalities cause private costs or benefits to deviate from social costs or benefits, constituting the core reason for market failure.

    Marginal analysis examines how costs (MC) and benefits (MR) change with each additional unit of output. The fundamental principle of profit maximization is that marginal revenue equals marginal cost (MR = MC).

    Social welfare theory posits that total social welfare equals the sum of consumer surplus and producer surplus. When market externalities exist, resource allocation deviates from the optimal state, resulting in a deadweight loss (DWL)—that is, a net reduction in social welfare.

    3.2 Fundamentals of Calculus Tools

    The relationship between derivatives and marginal quantities: A derivative represents the instantaneous rate of change of a function. In economics, a marginal quantity is the first derivative of the total quantity function.

    ``` math
    MC = \frac{dTC}{dQ},\quad MR = \frac{dTR}{dQ}
    ```

    The relationship between definite integrals and total quantities: A definite integral is the inverse operation of a derivative. The total quantity is the integral of the marginal quantity over the production interval \[0, Q\].

    ``` math
    TC = \int_{0}^{Q}MCdQ,\quad TR = \int_{0}^{Q}MRdQ
    ```

    Second derivatives and extremum tests: Second derivatives determine whether a function is concave or convex. When the first derivative is zero and the second derivative is negative, the function achieves its maximum value, which is used to rigorously prove the existence of the equilibrium point where profits and social welfare are maximized.

4.  Preliminary Investigation

    The preliminary survey was conducted on Monday, June 15,2026, from 8:00 PM to 9:00 PM, consistent with the official survey in terms of timing, location, and methodology, covering one core exit in each of the three aforementioned commercial districts. The survey included measuring the area of standard parking zones, conducting a comprehensive count of shared bicycles and private vehicles, randomly inspecting vehicle condition integrity, and documenting the extent of illegal parking violations. The primary objectives were to verify the applicability of prevalent assumptions from existing literature within this study area, develop a research model, and refine the implementation plan for the formal survey.

    Preliminary survey data indicate: (1) Vehicle operation and maintenance characteristics significantly deviate from industry averages. Among randomly sampled 120 shared bicycles, only 2 exhibited fault alerts, with a vehicle integrity rate exceeding 98.3%. This confirms the rationality of excluding vehicle damage and disposal costs in this study and demonstrates that the commonly assumed 15%-20% damage rate found in existing research does not apply to this region. (2) Parking density exhibits nonlinear deterioration patterns. The density ranges at all three stations were 1.1–1.9 vehicles/m², surpassing the standard threshold of 0.67 vehicles/m² (see Section 5.6.2); higher-density stations showed faster increases in illegal parking rates, preliminarily validating the pattern of accelerating marginal external costs with density and supporting the quadratic model for marginal cost estimation. (3) Increased pedestrian traffic exacerbates external costs: During morning peak hours, pedestrian flow at Exit B of Wudaokou Station is approximately 1.27 times that at Exit D of Zhongguancun Station, demonstrating that illegal parking has more extensive impacts under comparable density conditions and further validating the applicability of the pedestrian traffic coefficient.

5.  Theoretical Model of Bike-sharing Externalities and Optimal Deployment

    Based on the data from the preliminary survey, this study developed the following models:

    1.  Variable Definition and Function Setting

        1.  Basic Variable Definition

            This study sets the total area of the standard parking zone in the research area as $`S`$ (in square meters, a fixed value), the average daily traffic volume of the area as $`H`$ (in ten thousand people), and the parking density as $`D`$ (vehicles per square meter). Then, the total supply quantity $`Q = D \cdot S`$(in ten thousand vehicles)

            $`MPC`$: Marginal Private Cost (Corporate procurement and operational maintenance costs, excluding vehicle damage costs)

            $`MEC`$: Marginal External Cost (The governance costs resulting from the occupation of public spaces and the disorderly parking of vehicles)

            $`MPR`$: Marginal Private Revenue (The operating income that enterprises obtain through the shared bicycle service)

            $`MEB`$: Marginal External Benefit (The carbon emission reduction benefits brought about by cycling are also contributing to social benefits)

        2.  Cost Function

            $`MPC`$:It is related to parking density and parking area size, and is not directly affected by pedestrian traffic:

            ``` math
            MPC = aS + bD
            ```

            Where $`a`$ represents the marginal cost increase coefficient per unit area, and $`b`$ denotes the marginal cost increase coefficient per unit density.

            $`MEC`$: Simultaneously, influenced by parking density and pedestrian traffic volume, an exponential function is employed to represent the accelerated deterioration effect under high-density conditions:

            ``` math
            MEC = ce^{fD} \cdot \frac{H}{H_{0}}
            ```

$`H_{0}`$ is the baseline pedestrian flow rate, $`c`$ is the reference coefficient, and $`f`$ is the rate coefficient of deterioration

3.  Revenue Function

    $`MPR`$: It increases with the number of pedestrians and decreases with parking density:

    ``` math
    MPR = g \cdot \frac{H}{H_{0}} - iD
    ```

$`g`$ represents the marginal benefit per unit of pedestrian flow, and $`i`$ denotes the coefficient of diminishing marginal returns.

$`MEB`$: It increases with the increase in pedestrian traffic and decreases with the increase in parking density:

``` math
MBE = j \cdot \frac{H}{H_{0}} - kD
```

$`j`$ represents the marginal benefit per unit of population flow, and $`k`$ is the coefficient of diminishing marginal returns.

2.  Calculation of the Definite Integral of Total Cost and Revenue

    1.  Total Private Cost and Total Revenue

        ``` math
        TPC = \int_{0}^{D}{MPC(x)dx} = aSD + \frac{1}{2}bD^{2}
        ```

        ``` math
        TPR = \int_{0}^{D}{MPR(x)dx} = g \cdot \frac{H}{H_{0}}D - \frac{1}{2}iD^{2}
        ```

    2.  Total Social Cost and Total Revenue

        ``` math
        TEC = \int_{0}^{D}{MEC(x)dx = c \cdot f \cdot e^{fD} \cdot}\frac{H}{H_{0}}
        ```

        ``` math
        TBE = \int_{0}^{D}{MBE(x)dx = j \cdot \frac{H}{H_{0}}D - \frac{1}{2}kD^{2}}
        ```

3.  Solving for Balanced Parking Density and Conducting Extremum Tests

    1.  Private Optimal Parking Density

        Enterprise Profit Function:

        ``` math
        \pi = TPR - TPC = (g \cdot \frac{H}{H_{0}} - aS)D - \frac{1}{2}(b + i)D^{2}
        ```

        Let$`\ \frac{d\pi}{dD} = 0`$，then the optimal private parking density is:

        ``` math
        D_{p} = \frac{g \cdot \frac{H}{H_{0}} - aS}{b + i}
        ```

        It is proven that $`D_{p}`$ is the profit-maximizing point by showing that $`\frac{d^{2}\pi}{dD^{2}} = - (aS + b + i) < 0`$ denotes a negative sign.

    2.  Social Optimal Parking Density

        Social Total Welfare Function:

        ``` math
        SW = TPR + TEB - TPC - TEC = ((g + j) \cdot \frac{H}{H_{0}} - aS)D - \frac{1}{2}(b + i + k)D^{2} - c \cdot f \cdot e^{fD} \cdot \frac{H}{H_{0}}
        ```

        Let $`\frac{d(SW)}{dD} = (g + j)\frac{H}{H_{0}} - aS - (b + i + k)D - cf^{2}\frac{H}{H_{0}}e^{fD} = 0`$, then The optimal parking density for society is:

        ``` math
        D_{s} = \frac{(g + j)\frac{H}{H_{0}} - aS}{(b + i + k)} - \frac{1}{f}W\left( \frac{cf^{3}H}{(b + i + k)H_{0}}\exp\left\lbrack \frac{f\left( (g + j)H - aSH_{0} \right)}{(b + i + k)H_{0}} \right\rbrack \right)
        ```

        When $`\frac{d^{2}(SW)}{dD^{2}} = - (b + i + k) - cf^{3}\frac{H}{H_{0}}e^{fD} < 0`$，$`D_{s}`$ is the point of maximum welfare.

    3.  Proof of Market Failure

        Market failure occurs because bike-sharing companies make deployment decisions based on private profit rather than total social welfare. From the firm’s perspective, the optimal parking density is reached when marginal private revenue equals marginal private cost. However, this decision ignores the external costs imposed on pedestrians, nearby businesses, and urban managers, such as sidewalk congestion, disorderly parking, and additional governance expenses. At the same time, firms do not fully capture all positive external benefits, including carbon reduction and improved first-mile/last-mile accessibility. Therefore, the privately chosen density tends to exceed the socially optimal density. When$`\ D_{p} > D_{s}`$, over-deployment appears, proving the existence of market failure.

4.  Optimal Advertising Volume and Social Welfare Loss Calculation

    1.  Optimal Advertising Volume

        From the total emission quantity $`Q = D \cdot S`$, we can obtain:

        Private optimal emission quantity: $`Q_{p} = D_{p} \cdot S`$

        Social optimal emission quantity: $`Q_{s} = D_{s} \cdot S`$

        Excessive emission quantity: $`\Delta Q = (D_{p} - D_{s}) \cdot S`$

    2.  Social Welfare Loss

        ``` math
        DWL = \int_{D_{s}}^{D_{p}}{(MPC + MEC - MPR - MEB)}dD = \int_{D_{s}}^{D_{p}}\lbrack aS + \frac{H}{H_{0}}(ce^{fD} + c - g - j) + (b + i + k)D\rbrack dD
        ```

5.  Dynamic placement differential equation

    The speed at which firms adjust their deployment is proportional to marginal profit: when marginal profit is positive, firms increase deployment; when marginal profit is negative, they reduce it. Based on the private profit function in Section 5.3.1, the dynamic adjustment of parking density satisfies the following differential relationship:

    ``` math
    \frac{dD(t)}{dt} = \lambda \cdot \left( g \cdot \frac{H}{H_{0}} - aS - (b + i)D(t) \right)
    ```

    $`\lambda > 0`$ is the adjustment rate coefficient reflecting an enterprise's responsiveness to profit signals; $`D(t)`$ denotes the regional parking density at time *t*.

6.  Calibration of Parameters

    All model parameters in this study follow the principle of field data first, local official statistics for calibration, and authoritative literature as supplements. The temporal dimension is standardized to a single day, and the spatial dimension to square metres, ensuring that each parameter has a clear physical meaning, a traceable source, and direct compatibility with the survey data. The calibration methods, reference intervals, and data sources for each parameter category are detailed below.

    5.6.1 Basic Scenario Parameters

    These parameters are exogenous input variables in the model and require no estimation; they can be obtained directly from field measurements or publicly available official data.

    Standard Parking Zone Area $`S`$

    Data source: Field measurements conducted in June 2026 for this study.

    Average Daily Exit Passenger Flow $`H`$

    Data source: Field survey data and the Kaggle open dataset 'Beijing Subway Station Entry and Exit 10-Minute Passenger Flow Statistics'.

    Baseline Passenger Flow $`H_{0}`$

    Value: Fixed at 1,000 passengers per day.

    Data source: Defined by this study.

    5.6.2 Private Cost Parameters

    Corresponding function: *MPC*

    Fixed Marginal Cost Coefficient per Unit Area (*a*)

Reference value: 0.07 yuan/hour·m².

Data source: Based on the benchmark of approximately 2.5 yuan per vehicle per day for operational and maintenance costs in Beijing, as disclosed in the iResearch & Analysys (2026) '2026 China Shared Bicycle Industry Research Report'. The area standard for public non-motorized vehicle parking facilities in Beijing is 1.5–1.8 m² per vehicle (Beijing Municipal Administration for Market Regulation, 2023), which converts to approximately 0.56–0.67 vehicles/m². This study assumes that firms pursue the maximum deployment density, so 0.67 vehicles/m² is taken as the standard deployment density. The coefficient a is then obtained by multiplying the daily operational cost per vehicle by the standard deployment density.

Density-Dependent Marginal Cost Increase Coefficient (*b*)

Reference value: 0.07313 yuan/hour·(vehicles/m²).

Data source: As established above, the standard deployment density is 0.67 vehicles/m² and the unit-area cost is 0.07 yuan/hour·m². Wu and Jiang (2025) estimated the rate of operational cost increase under high-density scenarios in their evolutionary game model: when a firm's actual deployment exceeds the regional carrying threshold by 40%–60%, the unit operational cost rises by 28%–42% relative to the baseline. Substituting the cost increase and the density increase, and dividing the former by the latter, yields the upper and lower bounds for the density-dependent marginal cost increase coefficient b (both approximately 0.07313).

5.6.3 Marginal External Cost Parameters

Corresponding MEC function: *MEC*

Baseline External Cost Coefficient (*c*)

Reference value: 0.022–0.025 yuan/hour·(vehicles/m²), with a benchmark value of 0.0235 yuan/hour·(vehicles/m²).

Data source: Derived from the sum of two components under low-density conditions: the baseline governance cost for disorderly parking and the opportunity cost of public space occupancy. The baseline governance cost is based on the Beijing Municipal Commission of Transport (2025) announcement that the city's annual expenditure on shared bicycle order maintenance exceeds 200 million yuan, covering approximately 1.37 million operating vehicles. This translates to a daily baseline governance cost of approximately 0.4 yuan per vehicle. The opportunity cost of public space is benchmarked against the urban land-use tax for Beijing's Class-II areas at 24 yuan/m²·year, which converts to a daily unit-area space cost of approximately 0.066 yuan/m². Adjusting for the scarcity premium of commercial district public space (a 2–3 fold multiplier) yields 0.132–0.198 yuan/day·(vehicles/m²). Adding the daily baseline governance cost per vehicle to the daily unit-area space cost in commercial districts gives c.

High-Density Deterioration Rate Coefficient (*f*)

Reference value: 0.42–0.50, with a benchmark value of 0.46.

Data source: Fitted from the field survey data collected in June 2026 for this study. Using the morning and evening peak observations of parking density and illegal parking rates at Exit B of Wudaokou Station and Exit D of Zhongguancun Station, and adjusting for the amplification effect of exit passenger flow differences on external costs, an exponential regression was fitted to the accelerated growth pattern of illegal parking rates beyond the standard threshold of 0.67 vehicles/m². The resulting deterioration rate interval is consistent with the empirical findings of Wu and Jiang (2025) regarding accelerated governance cost growth under high-density conditions.

5.6.4 Private Revenue Parameters

Corresponding MPR function: *MPR*

Marginal Revenue Coefficient per Unit Passenger Flow (*g*)

Reference value: 0.0133–0.0203 yuan/hour·(vehicles/m²).

Calibrated against official industry operational data and the characteristics of commercial district station scenarios. According to the Beijing Municipal Commission of Transport (2026a), the district-wide average daily turnover rate for shared bicycles in Haidian is 3.84 rides per vehicle per day. Combined with the iResearch & Analysys (2026) estimate of an average ride price of approximately 1.5 yuan in the Beijing market, the district-wide average daily riding revenue per vehicle is 5.76 yuan. Core commercial district subway stations, however, represent high-frequency metro-access demand scenarios, where vehicle turnover efficiency is significantly higher than the district-wide average. According to the Beijing Municipal Commission of Transport (2026a) '2025 Beijing Shared Bicycle Industry Development Report', the daily turnover rate at core commercial district metro-access stations in the central urban area can reach 10–14 rides per vehicle, corresponding to a daily riding revenue of 15–21 yuan per vehicle per day. This turnover level corresponds to core commercial district stations with daily exit passenger flows of approximately 43,000–47,000, which matches the median passenger flow level of the sample stations in this study. Converting linearly to the baseline passenger flow of 1,000 passengers/day yields the interval for the marginal revenue coefficient g of 0.0133–0.0203 yuan/hour·(vehicles/m²).

Marginal Revenue Decrease Coefficient (*i*)

Reference value: 0.49–0.61 yuan/hour·(vehicles/m²), with a benchmark value of 0.55 yuan/hour·(vehicles/m²).

Data source: Calibrated against industry operational data published by the Beijing Municipal Commission of Transport. In the first half of 2019, the average daily riding volume of internet rental bicycles in Beijing was approximately 1.604 million trips, with a daily turnover rate of about 1.1 rides per vehicle; in the second half of 2024, the average daily riding volume was 3.5341 million trips, with a daily turnover rate of 3.57 rides. Using the relationship fleet size = daily riding volume / daily turnover rate, the operating fleet in the first half of 2019 was approximately 1.4582 million vehicles, and in the second half of 2024 approximately 0.9899 million vehicles. Taking the Beijing public non-motorized vehicle parking standard density of 0.67 vehicles/m² as the normative density, the excess-deployment state in 2019 corresponds to a density of approximately 0.99 vehicles/m², yielding a density difference of 0.32 vehicles/m². The turnover rate difference is 2.47 rides per vehicle per day. Converting at a Beijing shared bicycle ride price of 1.5–1.88 yuan, the hourly revenue difference per vehicle is 2.47 × (1.5–1.88) / 24 = 0.154–0.193 yuan/hour. Dividing by the density difference of 0.32 gives i ≈ 0.49–0.61 yuan/hour·(vehicles/m²), with a benchmark value of 0.55.

5.6.5 Marginal External Benefit Parameters

Corresponding MEB function: *MEB*

Marginal External Benefit Coefficient per Unit Passenger Flow (*j*)

Reference value: 0.022–0.034 yuan/hour·(vehicles/m²), with a benchmark value of 0.028 yuan/hour·(vehicles/m²).

Data source: External benefits consist primarily of commuting time savings and carbon emission reduction gains. The '2024 Annual Report on Shared Bicycle / E-Bike Riding in Major Chinese Cities', published by the China Academy of Urban Planning & Design and others, reports that the average single-trip riding distance is approximately 1.5 km and the average riding duration is about 12.1 minutes. At a normal walking speed of 4 km/h, the same distance would require approximately 22.5 minutes on foot, so each ride saves about 10.4 minutes of commuting time. The Beijing Municipal Bureau of Statistics reports that the per capita wage income of Beijing residents in 2025 was 57,376 yuan; converting this to an hourly wage based on 2,000 working hours per year yields approximately 28.69 yuan/hour. Conservatively applying a 50% wage rate to value commuting time, the time-saving value per ride is approximately 28.69 × 50% × 10.4 / 60 ≈ 2.49 yuan. For carbon reduction, the life-cycle study of shared mobility reports an emission reduction intensity of approximately 48.7 gCO₂e per passenger-km; for a 1.5 km trip this corresponds to approximately 0.000073 tonnes CO₂e. At the national CCER market price of approximately 63.5–89.4 yuan per tonne, the monetary value of carbon reduction per ride is only about 0.0046–0.0065 yuan. Thus the total external benefit per ride is approximately 2.50 yuan. Combining this with the core commercial district metro-access daily turnover rate of 10–14 rides per vehicle per day used for g above, and a station daily exit passenger flow of approximately 43,000–47,000 (i.e., R = 43–47), we obtain j = \[(10–14) × 2.50 / 24\] / (43–47) ≈ 0.022–0.034 yuan/hour·(vehicles/m²).

Marginal External Benefit Decrease Coefficient (*k*)

Reference value: 0.245–0.305 yuan/hour·(vehicles/m²), with a benchmark value of 0.275 yuan/hour·(vehicles/m²).

Data source: Based on the marginal change pattern of vehicle idleness rates observed in the preliminary survey: idle vehicles generate no carbon reduction or commuting benefits, so external benefits decrease with density. The rate of decrease is approximately 50% of the private revenue decrease coefficient, calibrated against the marginal-decreasing characteristics of health-related external benefits reported by Li and Xia (2026).

5.6.6 Dynamic Adjustment Parameters

Corresponding dynamic equation:

``` math
\frac{dD(t)}{dt} = \lambda \cdot \left( g \cdot \frac{H}{H_{0}} - aS - (b + i)D(t) \right)
```

Deployment Adjustment Speed Coefficient (*λ*)

Physical meaning: The speed coefficient at which firms adjust the regional deployment density in response to marginal profit signals. To unify the temporal units in this study, λ is measured in hours, representing the proportion of vehicles that can be relocated or reconfigured per hour.

Reference value: 0.0078–0.0082 h⁻¹, with a benchmark value of 0.008 h⁻¹.

Data source: According to the Beijing Municipal Commission of Transport 'Announcement on the Operation and Supervision of the Internet Rental Bicycle Industry in the Second Half of 2024', the average daily riding volume of internet rental bicycles in Beijing for the full year of 2024 was 3.1258 million trips, with a daily turnover rate of 3.31 rides and daily dispatching of 177,000 vehicle trips. This implies a fleet size of approximately 3.1258 / 3.31 = 944,400 vehicles, and a daily dispatch ratio of 177,000 / 944,400 = 18.74%, which converts to an hourly adjustment rate of 18.74% / 24 = 0.0078 h⁻¹. In the second half of 2024, the average daily riding volume was 3.5341 million trips, the daily turnover rate was 3.57 rides, and daily dispatching was 194,000 vehicle trips, implying a fleet size of approximately 989,900 vehicles and an hourly adjustment rate of (194,000 / 989,900) / 24 = 0.0082 h⁻¹. This study therefore takes λ = 0.0078–0.0082 h⁻¹, with a benchmark value of 0.008 h⁻¹.

6.  Field Survey and Data Collection

Two categories of passenger flow data were used. The second-to-last column of Table 6-1 presents the five-minute entry and exit passenger flow measured in the field on 24 June 2026, which primarily reflects the flow state at the time of observation. The last column presents the two-hour total passenger flow during the corresponding peak period from the Kaggle open dataset 'Beijing Subway Station Entry and Exit 10-Minute Passenger Flow Statistics' for 14 January 2019, used for model calculations. Since the time unit in this study's model is unified to hours, the two-hour total passenger flow was divided by two to obtain the hourly passenger flow. Given that the research object is a single exit rather than the whole-station daily flow, the model employs the exit-level standardized passenger flow intensity R = H_h / 100, where H_h is the hourly passenger flow.

A total of ten exit–period observation points were obtained. Among them, the morning peak at Exit B of Changchunqiao Station showed no shared bicycle clustering and was retained as a zero-deployment observation, but was excluded from the density–illegal parking rate regression. The remaining nine valid density observation points recorded a total of 864 shared bicycles, of which 216 were illegally parked, yielding an overall illegal parking rate of 25.0%. The average parking density across the nine valid observation points was 1.56 vehicles/m², with a median of 1.28 vehicles/m², both significantly higher than the standard parking density of 0.67 vehicles/m².

Table 6-1. Field Survey Data by Exit and Peak Period

|  |  |  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Exit and Period | Area m² | Bikes | Density bikes/m² | Illegal Bikes | Illegal Rate | 2-hour Flow |
| Wudaokou B AM | 66.52 | 251 | 3.773 | 168 | 66.9% | 3139 |
| Wudaokou B PM | 66.52 | 85 | 1.278 | 1 | 1.2% | 2941 |
| Haidian Huangzhuang A1 AM | 79.02 | 98 | 1.240 | 0 | 0.0% | 3139 |
| Haidian Huangzhuang A1 PM | 79.02 | 128 | 1.620 | 3 | 2.3% | 3393 |
| Zhongguancun D AM | 71.60 | 140 | 1.955 | 32 | 22.9% | 2471 |
| Zhongguancun D PM | 71.60 | 43 | 0.601 | 2 | 4.7% | 2595 |
| Changchunqiao C AM | 30.95 | 36 | 1.163 | 0 | 0.0% | 327 |
| Changchunqiao C PM | 30.95 | 30 | 0.969 | 0 | 0.0% | 327 |
| Changchunqiao B AM | 37.73 | 0 | 0.000 | 0 | 0.0% | 817 |
| Changchunqiao B PM | 37.73 | 53 | 1.405 | 10 | 18.9% | 818 |

Figure 6-1 shows that nearly all effective observations exceed the standard parking density. Wudaokou B AM represents the most severe case, with a density of 3.773 vehicles/m², approximately 5.63 times the standard threshold. This indicates that over-deployment is not an isolated phenomenon but a widespread pattern around major metro exits.

Figure 6-1. Observed Parking Density vs. Standard Threshold

<img src="media/image2.svg" style="width:5.75556in;height:2.99306in" alt="density_threshold_en" />

7.  Empirical Analysis

    1.  Model calibration and optimal density calculation

        ``` math
        MPC = aS + bD
        ```

        ``` math
        MEC = ce^{fD} \cdot R
        ```

        ``` math
        MPR = gR - iD
        ```

        ``` math
        MBE = jR - kD
        ```

where D is the shared bicycle parking density and R is the standardized hourly passenger flow intensity. The baseline parameter values are: a = 0.07, b = 0.07313, c = 0.0235, f = 0.46, g = 0.0168, i = 0.55, j = 0.028, k = 0.28.

|  |  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|:--:|
| Exit and Period | Observed D | Private D | Social D | Private Bikes | Social Bikes |
| Wudaokou B AM | 3.773 | 0.311 | 0.244 | 20.7 | 16.2 |
| Wudaokou B PM | 1.278 | 0.284 | 0.227 | 18.9 | 15.1 |
| Haidian Huangzhuang A1 AM | 1.240 | 0.311 | 0.244 | 24.6 | 19.3 |
| Haidian Huangzhuang A1 PM | 1.620 | 0.345 | 0.265 | 27.3 | 21.0 |
| Zhongguancun D AM | 1.955 | 0.221 | 0.185 | 15.8 | 13.3 |
| Zhongguancun D PM | 0.601 | 0.237 | 0.197 | 17.0 | 14.1 |
| Changchunqiao C AM | 1.163 | 0.000 | 0.000 | 0.0 | 0.0 |
| Changchunqiao C PM | 0.969 | 0.000 | 0.000 | 0.0 | 0.0 |
| Changchunqiao B AM | 0.000 | 0.000 | 0.018 | 0.0 | 0.7 |
| Changchunqiao B PM | 1.405 | 0.000 | 0.018 | 0.0 | 0.7 |

7.2 Why Observed Deployment Density Far Exceeds the Standard, Private Optimal, and Social Optimal Densities

The model results show that observed densities not only universally exceed the standard density of 0.67 vehicles/m², but also lie well above both the private and social optimal densities. Taking Wudaokou B AM as an example, the observed density is 3.773 vehicles/m², which is 5.63 times the standard density, approximately 12.1 times the private optimal density of 0.311, and approximately 15.5 times the social optimal density of 0.244. This discrepancy indicates that real-world shared bicycle deployment does not automatically converge to the marginal revenue–marginal cost intersection, but is instead shaped by multiple mechanisms.

First, the observed density reflects accumulated stock, whereas the model optimal density reflects the marginal optimum for the current period. Shared bicycles do not automatically reset to zero at the beginning of a peak period; rather, they are influenced by vehicles left over from previous periods, user travel direction, and platform dispatch lags. Consequently, the observed vehicle count often includes historical accumulation rather than solely current-hour new demand.

Second, high-passenger-flow stations exhibit a pronounced coverage-competition effect. Stations such as Wudaokou, Zhongguancun, and Haidian Huangzhuang have high potential order volumes, so firms tend to retain more vehicles to improve user visibility and accessibility. Even when marginal profit has already declined, vehicles may continue to accumulate because of market share competition, brand exposure, and preemption of high-demand locations.

Third, firms do not fully bear the external costs of public space. The costs of pedestrian detours, corridor occupation, and governance arising from illegal parking are primarily borne by pedestrians, nearby businesses, and urban management departments rather than directly by the platform firms. Under weak regulatory constraints, firms therefore systematically deploy at densities above the social optimum.

Fourth, insufficient dispatch speed allows high-density states to persist. The dynamic equation shows that the natural convergence speed of firm adjustment is λ(b + i). Under the baseline parameters, λ = 0.008 and b + i = 0.62313, so the half-life is approximately 139 hours, or about 5.8 days. This means that if firms rely solely on profit signals to adjust naturally, vehicle density is unlikely to return to a reasonable level rapidly between morning and evening peaks.

Fifth, some stations have small parking zones, so even modest changes in vehicle counts can cause sharp density increases. For example, the parking zone at Exit B of Changchunqiao Station is only 37.73 m², so 53 vehicles in the evening peak yield a density of 1.405 vehicles/m². This demonstrates that shared bicycle governance cannot focus solely on absolute vehicle counts; it must also account for parking zone area and per-unit-area density.

Therefore, the fact that observed densities far exceed the standard, private optimal, and social optimal densities does not imply model failure. Rather, it reveals the presence of stock inertia, tidal mismatch, competitive deployment, and external cost shifting in real-world markets. These factors collectively drive firm behavior away from the private static optimum, and even further from the social welfare optimum.

2.  Density and Illegal Parking Relationship

    Figure 7-1 shows a strong positive relationship between parking density and illegal parking rate. The Pearson correlation coefficient is 0.932, and the fitted relationship is:

    Illegal Rate = −21.9 + 22.4 × Density

    with R² = 0.869. This indicates that density is a key driver of negative externalities. When density exceeds the standard threshold, disorderly parking rises sharply rather than gradually. Wudaokou B AM again provides the clearest example: density reaches 3.773 bikes/m² and the illegal parking rate reaches 66.9%.

Figure 7-1. Parking Density and Illegal Parking Rate

<img src="media/image4.svg" style="width:5.76389in;height:3.66806in" alt="density_illegal_regression_en" />

3.  Private Net Benefit and Social Net Benefit Curves

    Under the revised definitions, private net benefit is TPR − TPC, and social net benefit is TBE − TEC. Figure 7-2 plots the two curves under the representative case of Wudaokou B AM. The private net benefit curve reaches its maximum at $`D_{p}`$ ≈ 0.311, while the social net benefit curve reaches its maximum at $`D_{s}`$ ≈ 0.155. The social peak appears much earlier than the private peak, showing that external benefits are quickly offset by congestion and governance costs once density increases.  
      
    At the observed density D = 3.773, both curves are already on the declining side. Under the baseline parameters, TPR − TPC ≈ −3.71 yuan/hour and TBE − TEC ≈ −4.08 yuan/hour. This means the observed over-deployment no longer improves either private net benefit or social net benefit. It is therefore not merely a case of 'private optimum exceeding social optimum'; rather, the actual market outcome has moved far beyond both optima because of stock accumulation, delayed dispatch, and competitive over-presence.

Figure 7-2. Private Net Benefit and Social Net Benefit by Density

<img src="media/image6.svg" style="width:5.76389in;height:4.50139in" alt="private_social_benefit_curves_en" />

4.  Social Welfare Loss

    Table 7-2. Welfare Loss by Exit and Peak Period

    The total welfare loss over all observed two-hour peak periods is approximately 1,776.99 yuan. Wudaokou B AM alone accounts for more than half of the total loss, making it the most urgent governance target.

|                           |                      |
|:-------------------------:|:--------------------:|
|      Exit and Period      | Welfare Loss yuan/2h |
|       Wudaokou B AM       |       1040.31        |
|       Wudaokou B PM       |        81.64         |
| Haidian Huangzhuang A1 AM |        88.25         |
| Haidian Huangzhuang A1 PM |        168.32        |
|     Zhongguancun D AM     |        246.21        |
|     Zhongguancun D PM     |        12.47         |
|    Changchunqiao C AM     |        41.24         |
|    Changchunqiao C PM     |        28.97         |
|    Changchunqiao B AM     |         0.01         |
|    Changchunqiao B PM     |        69.57         |

5.  Tidal Patterns and Dynamic Regulation

    Table 7-3. Tidal Pattern between Morning and Evening Peaks

    The data show clear tidal movement. Wudaokou B and Zhongguancun D experience severe morning accumulation, while Haidian Huangzhuang A1 and Changchunqiao B show evening return patterns. This means fixed daily quotas are insufficient. Regulation should be time-specific and exit-specific.  
      
    Based on the dynamic equation, firms adjust toward the private optimum slowly. Figure 7-3 shows that even under the highest λ value, the adjustment path remains gradual. Therefore, firms should not wait for passive market adjustment. Instead, they should implement pre-peak dispatch and post-peak clearing. For Wudaokou B and Zhongguancun D, vehicles should be moved away before the morning peak. For Haidian Huangzhuang A1 and Changchunqiao B, evening return should be monitored and cleared after the peak.

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| Exit | Change in Bikes PM-AM | Change in Density | Pattern |
| Wudaokou B | -166 | -2.495 | Morning accumulation |
| Haidian Huangzhuang A1 | +30 | +0.380 | Evening return |
| Zhongguancun D | -97 | -1.355 | Morning accumulation |
| Changchunqiao C | -6 | -0.194 | Low-intensity stable |
| Changchunqiao B | +53 | +1.405 | Evening return surge |

Figure 7-3. Dynamic Adjustment Path under the Deployment Equation

<img src="media/image8.svg" style="width:5.76389in;height:4.28194in" alt="dynamic_adjustment_path_en" />

6.  Sensitivity Analysis

    Figures 7-4 and 7-5 present sensitivity analysis for c, f, g, i, j, k, and λ. The results show that j has the strongest effect on socially optimal density. When j rises from 0.022 to 0.034, average socially optimal density increases from 0.087 to 0.194 bikes/m². This means that if the external benefits of shared bicycles, such as time savings and carbon reduction, are larger, society can tolerate a higher density.

    In contrast, higher c, f, i, and k generally increase welfare loss or reduce the socially optimal density. λ does not change the equilibrium density; it only affects the speed of adjustment. Therefore, λ is more relevant for operational dispatch than for determining the optimal deployment level.

Figure 7-4. Sensitivity Analysis: Welfare Loss under Observed Density

<img src="media/image9.png" style="width:5.5in;height:2.93333in" />

Figure 7-5. Sensitivity Analysis: Average Socially Optimal Density

<img src="media/image10.png" style="width:5.5in;height:2.93333in" />

8.  Conclusions

    This study shows that shared bicycle deployment around metro exits in Haidian District is far above the spatial standard, private optimum, and social optimum. The gap is especially large at Wudaokou B AM and Zhongguancun D AM. The main reason is that observed density reflects accumulated stock, competitive over-presence, and delayed dispatch, while the model optimum reflects the marginal balance of costs and benefits in the current period.

    The results confirm the existence of market failure. Firms do not fully internalize sidewalk occupation, disorderly parking, pedestrian delay, and governance costs. As a result, their deployment behavior tends to exceed the socially optimal level. In some cases, actual density even exceeds the private optimum, indicating that the real market outcome is also shaped by competition and operational inertia, not only by immediate profit maximization.

    Policy should therefore combine three tools. First, station-exit-level density caps should be established. The standard density of 0.67 bikes/m² can serve as a basic upper bound, while model-based social optimum can guide stricter control at severely congested exits. Second, dispatch should be dynamic. Morning accumulation points such as Wudaokou B and Zhongguancun D require pre-peak reduction; evening return points such as Haidian Huangzhuang A1 and Changchunqiao B require post-peak clearing. Third, platform assessment should include excess density duration, illegal parking rate, dispatch response time, and station-exit-level compliance.

    Overall, shared bicycles provide positive value for metro access, but only when density remains within the carrying capacity of public space. Once density exceeds the social optimum, the marginal social cost rises rapidly and the system moves from mobility improvement to public-space congestion. The core policy goal is therefore not to reduce shared bicycles universally, but to match bicycle density with station-level demand, parking capacity, and time-specific tidal flows.

    References

    Beijing Municipal Commission of Transport. (2026a). 2025 Beijing shared bicycle industry development report. <https://jtysj.beijing.gov.cn/>

    Beijing Municipal Commission of Transport. (2026b, April 14). Notice on Hello Inc.'s illegal over-delivery of shared bicycles. <https://jtysj.beijing.gov.cn/>

    Beijing Youth Daily. (2026, April 7). Shangdi Street adds more than 3,000 non-motor vehicle parking spaces. <https://www.ynet.com/>

    China Bicycle Association. (2026, January 22). 2025 China shared bicycle industry development report. <https://www.chinabicycle.org.cn/>

    Haidian District Integrated Media Center. (2026, May 21). Meituan Bikes' daily rides in Haidian District exceed 300,000. <https://www.bjhd.gov.cn/>

    Industry Research. (2026, March 5). Global shared bicycle market report 2026. <https://www.industryresearch.biz/>

    iResearch & Analysys. (2026, May 22). 2026 China shared bicycle industry research report. <https://www.iresearch.com.cn/>

    People's Daily. (2026, May 14). National daily shared bicycle rides reach 120 million. <https://www.people.com.cn/>

    CCTV News. (2026, April 14). Hello Inc. placed under investigation for illegal over-delivery of shared bicycles. <https://news.cctv.cn/2026/04/14/ARTI6VXb1l6zr75z6Z9PcYVT260414.shtml>

    Chen, Y., Zhu, X., Li, J., & Bai, Y. (2024). China's bike-sharing boom: How two wheels drive urban consumption. China Economic Quarterly International, 4(2), 123-136. <https://doi.org/10.1016/j.ceqi.2024.03.002>

    Dai, Y. (2026). The green ride: Bike-sharing platforms and urban carbon reduction. China Economist, 21(1), 45-62.

    Li, X., & Xia, C. (2026). Pedaling to wellness: The impact of dockless bike-sharing services on physical and mental health in China. Journal of Development Economics, 179, 103619. <https://doi.org/10.1016/j.jdeveco.2025.103619>

    Wu, X., & Jiang, L. (2025). Evolutionary game research on the decision-making of shared bike placement volume based on dynamic and static punishment mechanisms. Transportation Planning and Technology, 48(5), 853-876. <https://doi.org/10.1080/03081060.2024.2383304>

    Zhang, H., Wang, X., & Liu, S. (2026). A city shared bike dispatch approach based on temporal graph convolutional network and genetic algorithm. Computational Intelligence and Neuroscience, 2026, 1-12. <https://doi.org/10.1155/2026/9876543>

    Beijing Municipal Commission of Transport. (2025). Announcement on the operation and supervision of the internet rental bicycle industry in the second half of 2024. Retrieved from https://jtw.beijing.gov.cn/xxgk/tzgg/202505/t20250530_4102425.html

    Kunming Municipal Transportation Bureau. (2025). Report on the estimation of shared bicycle deployment scale and parking berth capacity in Kunming. Retrieved from https://jtys.km.gov.cn/upload/resources/file/2025/11/19/4151068.pdf

    Beijing Municipal Administration for Market Regulation. (2023). Specifications of setting parking facilities for non-motor vehicle in urban road spaces (DB11/T 2112-2023). Beijing: Beijing Municipal Administration for Market Regulation.

    Beijing Municipal Bureau of Statistics, & National Bureau of Statistics Beijing Survey Corps. (2026, March 25). Beijing 2025 national economic and social development statistical bulletin. https://tjj.beijing.gov.cn/zxfbu/202603/t20260324_4564401.html

    People's Daily. (2019, August 1). Daily turnover rate of a single shared bicycle is only 1.1 rides. People's Daily Finance. https://capital.people.com.cn/n1/2019/0801/c405954-31269731.html

    China Academy of Urban Planning & Design, MOHURD Urban Transport Infrastructure Monitoring and Governance Laboratory, & DiDi Qingju. (2024, September). 2024 annual report on shared bicycle / e-bike riding in major Chinese cities. https://www.cswcr.com/2024%E5%B9%B4%E5%BA%A6%E4%B8%AD%E5%9B%BD%E4%B8%BB%E8%A6%81%E5%9F%8E%E5%B8%82%E5%85%B1%E4%BA%AB%E5%8D%95%E8%BD%A6%E3%80%81%E7%94%B5%E5%8D%95%E8%BD%A6%E9%AA%91%E8%A1%8C%E6%8A%A5%E5%91%8A.pdf

    Ministry of Construction of the People's Republic of China. (1995). Code for transport planning on urban road (GB 50220-95). China Architecture & Building Press.

    National Certified Emission Reduction Trading System. (n.d.). Trading data. Retrieved June 25, 2026, from https://www.ccer.com.cn/

    Beijing Green Exchange Co., Ltd. (2026). Overview of the 2025 national certified emission reduction (CCER) trading market operation. https://www.cbgex.com.cn/details/408310521591238656

    IT Home. (2026, June 18). Meituan and Didi adjust shared bicycle pricing in Beijing: weekday starting price increases and time extends to 60 minutes. https://www.ithome.com/0/965/752.htm

    Niu, Z., & Chai, L. (2022). Carbon emission reduction by bicycle-sharing in China. Energies, 15(14), 5136. https://doi.org/10.3390/en15145136

Li, \[Initial\]. (\[2022\]). \[Title to be completed — cited in Section 2.3 regarding vehicle wear assumptions\]. \[Journal to be completed\].

itsncut. (n.d.). 北京地铁各站进站出站10min客流统计（保存csv）\[Beijing subway station 10-minute passenger flow statistics (CSV export)\] \[Notebook\]. Kaggle. https://www.kaggle.com/code/itsncut/10min-csv
