基于海淀区多地铁站出口数据的共享单车外部性与最优投放量实证研究

Jason Han

Abstract

本研究量化分析了共享单车投放的外部性，并推导了北京市海淀区地铁站出口处的最优投放密度。研究采用微观经济学框架，将边际分析与实地调查数据相结合，基于五个站点十个出口—时段观测数据，估计了私人成本、社会成本及收益函数。模型纳入了边际私人成本、边际外部成本、边际私人收益和边际外部收益四项边际函数，参数依据本地运营数据、政府报告和2026年6月现场实测数据校准。结果表明，观测到的停车密度显著高于私人最优和社会最优水平，其中五道口B口早高峰最为严重（3.773辆/m²，约为社会最优密度的15.5倍）。停车密度与违规停放率的皮尔逊相关系数为0.932，证实了密度是负外部性的主要驱动因素。所有观测高峰时段两小时的总福利损失约为1777元，其中五道口B口早高峰单独占一半以上。我们将观测密度与最优密度之间的偏差归因于存量堆积、竞争性过度投放、调度滞后（半衰期约5.8天）以及平台企业对外部成本的不完全内部化。政策建议包括：设立出口级密度上限、对潮汐聚集点实施动态高峰前削减和高峰后清理、以及将超密度持续时间、违规停放率纳入平台考核指标。

**关键词：共享单车；外部性；最优投放量；市场失灵；公共空间占用**

1.  Introduction

    1.1 研究背景

    目前，共享单车已在全球超过65个国家、2500个城市投放（Industry Research, 2026）。作为全球最大市场，中国截至2025年底累计投放3500万辆自行车，年骑行量超过400亿次（中国自行车协会, 2026），日均骑行人数达到1.2亿（人民日报, 2026）。

    海淀区在全市共享单车使用强度中位居前列，登记车辆约60500辆，日均周转率约3.84次（北京市交通委员会, 2026a）。仅美团单车在海淀区的日均骑行量就超过30万次（海淀区融媒体中心, 2026）。尽管新增了超过3000个非机动车停车位（北京青年报, 2026），但企业过度投放问题依然突出（北京市交通委员会, 2026b）。2026年4月14日，北京市交通委员会宣布哈啰单车因在中心城区非法过量投放共享单车且拒不整改而被立案调查，导致其运营规模被缩减——这反映了企业为抢占市场份额持续过度投放的倾向（央视新闻, 2026）。

    1.2 研究问题与意义

    随着共享单车行业的快速发展，虽然极大便利了日常通勤，但也引发了一系列问题，如过度投放、无序停放和占用公共空间。尽管现有研究对共享单车外部性进行了广泛探讨，但在定量方法论和本地适用性方面仍存在不足。基于此，本研究提出三个核心问题：（1）如何科学量化共享单车的正负外部性，特别是在研究区域内所有车辆均可正常使用的独特情境下，如何准确计算公共空间占用和无序停放管理的成本？（2）企业自愿投放行为为何必然导致过度投放，这一现象背后的市场失灵机制是什么？（3）在兼顾整体社会福利最大化和公共空间最大承载力的前提下，海淀区地铁站区域共享单车的最优投放密度是多少？

    1.3 研究方法

    本研究以海淀区三大核心商圈——中关村、五道口和世纪金源——的主要地铁站出口为样本，包括五道口站B口、中关村站D口、海淀黄庄站A1口和长春桥站B口与C口，结合本地官方数据和实地调查结果，计算共享单车的净外部性并确定其最优投放规模。

    研究结果为海淀区交通局和城管委制定共享单车投放配额、停车管理政策和企业绩效评价机制提供了科学量化依据，有助于解决当前过度投放和无序停放问题，推动共享单车行业健康可持续发展。

2.  2 文献综述

    2.1 共享单车外部性研究现状

    共享单车外部性研究是共享经济领域的核心议题，学界普遍认为共享单车具有显著的正负外部性。关于正外部性，现有研究主要关注四个维度：减少碳排放、缓解交通拥堵、促进消费和改善健康效益。戴（2026）采用准实验方法证明，共享单车每骑行一公里约替代0.8公里私人汽车出行，减少CO2排放约0.18公斤——这一发现已被深圳市碳普惠等官方机构采纳。陈等人（2024）进一步揭示，共享单车的引入使当地居民人均家庭支出显著增加3.9%–6.8%，主要通过降低通勤时间成本实现。李和夏（2026）证实了共享单车对健康的益处，显示用户每周额外增加0.53次锻炼和12.6分钟体力活动时间。

    关于负外部性，现有研究主要关注三个方面：违规停放自行车占用公共空间、交通事故风险增加以及报废车辆处置造成的污染。吴和姜（2025）指出，截至2025年底，中国主要城市共享单车投放总量已超过1800万辆；在一些核心商圈和地铁站，高峰时段自行车密度达到每100米超过100辆，严重影响居民出行体验和城市运行效率。北京市交通委员会（2025）发布报告显示，北京市每年清理违规停放共享单车的费用超过2亿元，这一成本最终由全体纳税人承担。

    2.2 共享单车最优投放量研究现状

    现有文献对共享单车最优投放规模的研究主要从企业和政府两个视角展开。从企业视角看，研究主要以利润最大化为目标，运用博弈论、动态规划和机器学习等方法探讨最优投放策略。吴和姜（2025）运用演化博弈论分析政府与企业在投放决策中的互动，得出结论认为政府监管对于解决过度投放问题至关重要。一些研究还引入了基于人工智能的调度算法，通过预测不同区域需求来优化投放和运营计划；例如，张等人（2026）结合时序图卷积网络（T-GCN）与遗传算法，实现了需求预测与调度优化的集成决策。

    从政府视角看，大多数研究以社会福利最大化为目标，综合考虑供需平衡、空间容量和环境效益等因素。昆明市交通运输局（2025）发布的报告采用空间容量法确定城市共享单车最优投放规模，为政策制定者建立配额分配提供了依据。

    2.3 现有研究的不足与空白

    通过对上述文献的回顾，本研究识别出现有研究的三个显著不足：一是过度侧重宏观分析，对微观节点关注不足。大多数研究在城市层面分析共享单车的外部性和最优投放量，而对地铁站出口等关键微观节点的研究不够充分。实际上，共享单车外部性在不同区域差异显著：在住宅区和办公区，共享单车主要作为首末段接驳工具，具有显著正外部性；而在地铁站出口等交通枢纽，过量车辆投放导致严重拥堵问题，产生显著负外部性。现有研究未能捕捉这些空间差异，使得政府一刀切的投放政策难以达到预期效果。

    本研究不考虑车辆不可用情形。现有研究在构建成本模型时通常假设共享单车有15%–30%的损坏和闲置率，从而将大量车辆维护和处置成本纳入私人边际成本：例如，李等人（2022）在碳排放核算分析中采用了5%、10%和15%三种不同的车辆磨损假设；吴和姜（2025）在其演化博弈模型中设定行业平均车辆损坏率为20%。然而，我们的前期调查显示，研究区域内共享单车的运营质量极高——地铁站附近停放的所有车辆均能正常使用，无显著损坏或闲置问题。这一独特情形显著降低了现有模型在本研究中的适用性。

    第三，复杂模型众多而简化实用模型稀少。现有关于最优投放量的研究主要采用精密的数学模型和计量经济学方法；虽然这些方法精度较高，但城市管理者和普通公众难以理解和应用。

3.  3 理论基础

    3.1 微观经济学理论基础

    外部性理论是指经济活动对未参与交易的第三方产生的未补偿影响，分为正外部性（如共享单车碳减排）和负外部性（如违规停放占用公共空间）。外部性导致私人成本或收益偏离社会成本或收益，构成市场失灵的核心原因。

    边际分析考察每增加一单位产出时成本（MC）和收益（MR）的变化。利润最大化的基本原则是边际收益等于边际成本（MR = MC）。

    社会福利理论认为，总社会福利等于消费者剩余和生产者剩余之和。当市场存在外部性时，资源配置偏离最优状态，产生无谓损失（DWL）——即社会福利的净减少。

    3.2 微积分工具基础

    导数与边际量的关系：导数表示函数的瞬时变化率。在经济学中，边际量就是总量函数的一阶导数。

    ``` math
    \text{MC=}\frac{\text{dTC}}{\text{dQ}}\text{,\quad MR=}\frac{\text{dTR}}{\text{dQ}}
    ```

    定积分与总量的关系：定积分是导数的逆运算。总量是边际量在生产区间\[0, Q\]上的积分。

    ``` math
    \text{TC=}\int_{\text{0}}^{\text{Q}}\text{MCdQ,\quad TR=}\int_{\text{0}}^{\text{Q}}\text{MRdQ}
    ```

    二阶导数与极值检验：二阶导数判断函数是凹还是凸。当一阶导数为零且二阶导数为负时，函数取得最大值，这被用于严格证明利润和社会福利最大化均衡点的存在性。

4.  4 前期调查

    前期调查于2026年6月15日（星期一）晚上8:00至9:00进行，与正式调查在时段、地点和方法上保持一致，覆盖上述三大商圈各一个核心出口。调查内容包括测量标准停车区面积、全面清点共享单车和私人车辆数量、随机检查车辆状况完好性、以及记录违规停放程度。主要目的是验证现有文献的普遍假设在本研究区域中的适用性、构建研究模型并完善正式调查实施方案。

    前期调查数据显示：（1）车辆运营维护特征显著偏离行业平均水平。在随机抽检的120辆共享单车中，仅2辆出现故障提示，车辆完好率超过98.3%。这证实了本研究排除车辆损坏和处置成本的合理性，并表明现有研究常用的15%–20%损坏率假设不适用于该区域。（2）停车密度呈现非线性恶化特征。三个站点的密度范围均为1.1–1.9辆/m²，超过了0.67辆/m²的标准阈值（见第5.6.2节）；密度较高的站点违规停放率上升更快，初步验证了边际外部成本随密度加速增长的模式，支持了边际成本估计的二次模型。（3）行人流量增加加剧外部成本：早高峰时段五道口站B口的行人流量约为中关村站D口的1.27倍，表明在可比密度条件下违规停放具有更广泛的影响，进一步验证了行人流量系数的适用性。

5.  5 共享单车外部性与最优投放理论模型

    基于前期调查数据，本研究构建了以下模型：

    1.  5.1 变量定义与函数设定

        1.  **5.1.1 基本变量定义**

            本研究设定研究区域标准停车区总面积为S（单位：平方米，固定值），区域日均人流量为H（单位：万人次），停车密度为D（单位：辆/平方米）。则总供给量Q（单位：万辆）为Q = S x D。$`\text{S}`$$`\text{H}`$$`\text{D}`$$`\text{Q=D⋅S}`$

            $`\text{MPC}`$MPC：边际私人成本（企业采购和运营维护成本，不包括车辆损坏成本）

            $`\text{MEC}`$MEC：边际外部成本（公共空间占用和车辆无序停放导致的治理成本）

            $`\text{MPR}`$MPR：边际私人收益（企业通过共享单车服务获得的营业收入）

            $`\text{MEB}`$MEB：边际外部收益（骑行带来的碳减排收益，也贡献于社会效益）

        2.  **MPC：与停车密度和停车区面积相关，不直接受行人流量影响：MPC = a + bD。其中a为单位面积边际成本递增系数，b为单位密度边际成本递增系数。**

            $`\text{MPC}`$

            ``` math
            \text{MPC=aS+bD}
            ```
            MEC：同时受停车密度和行人流量影响，采用指数函数表示高密度条件下的加速恶化效应：MEC = c x e^(fD) x R。其中H0为基准人流量，c为基准系数，f为恶化速率系数。

            $`\text{a}`$$`\text{b}`$

            MPR：随行人数量增加而增加，随停车密度增加而减少：MPR = gR - iD。其中g为单位人流量边际收益系数，i为边际收益递减系数。

            $`\text{MEC}`$

            ``` math
            \text{MEC=c}\text{e}^{\text{fD}}\text{⋅}\frac{\text{H}}{\text{H}_{\text{0}}}
            ```
            MEB：随行人流量增加而增加，随停车密度增加而减少：MEB = jR - kD。其中j为单位人流量边际外部收益系数，k为外部收益递减系数。

$`\text{H}_{\text{0}}`$$`\text{c}`$$`\text{f}`$

3.  **5.2 总成本与总收益的定积分计算**

    $`\text{MPR}`$<!-- -->5.2.1 总私人成本与总收益

    ``` math
    \text{MPR=g⋅}\frac{\text{H}}{\text{H}_{\text{0}}}\text{−iD}
    ```
    TPC = integral_0^Q MPC dQ = integral_0^Q (a + bD) dQ；TPR = integral_0^Q MPR dQ = integral_0^Q (gR - iD) dQ

$`\text{g}`$$`\text{i}`$

$`\text{MEB}`$<!-- -->5.2.2 总社会成本与总收益

``` math
\text{MBE=j⋅}\frac{\text{H}}{\text{H}_{\text{0}}}\text{−kD}
```

$`\text{j}`$$`\text{k}`$

2.  5.3 均衡停车密度求解与极值检验

    1.  **5.3.1 私人最优停车密度**

        ``` math
        \text{TPC=}\int_{\text{0}}^{\text{D}}{\text{MPC}\text{(}\text{x}\text{)}\text{dx}}\text{=aSD+}\frac{\text{1}}{\text{2}}\text{b}\text{D}^{\text{2}}
        ```
        企业利润函数：pi = TPR - TPC

        ``` math
        \text{TPR=}\int_{\text{0}}^{\text{D}}{\text{MPR}\text{(}\text{x}\text{)}\text{dx}}\text{=g⋅}\frac{\text{H}}{\text{H}_{\text{0}}}\text{D−}\frac{\text{1}}{\text{2}}\text{i}\text{D}^{\text{2}}
        ```

    2.  **令dpi/dQ = 0，则最优私人停车密度为：D_p = (gR - a) / (b + i)**

        ``` math
        \text{TEC=}\int_{\text{0}}^{\text{D}}{\text{MEC}\text{(}\text{x}\text{)}\text{dx}\text{=}\text{c}\text{⋅}\text{f}\text{⋅}\text{e}^{\text{fD}}\text{⋅}}\frac{\text{H}}{\text{H}_{\text{0}}}
        ```

        ``` math
        \text{TBE=}\int_{\text{0}}^{\text{D}}{\text{MBE}\text{(}\text{x}\text{)}\text{dx}\text{=}\text{j}\text{⋅}\frac{\text{H}}{\text{H}_{\text{0}}}\text{D}\text{−}\frac{\text{1}}{\text{2}}\text{k}\text{D}^{\text{2}}}
        ```
        通过证明d2pi/dQ2 \< 0，确认D_p为利润最大化点。

3.  1.  **5.3.2 社会最优停车密度**

        社会总福利函数：W = TSR - TSC = (TPR + TEB) - (TPC + TEC)

        ``` math
        \text{π=TPR-TPC=(g⋅}\frac{\text{H}}{\text{H}_{\text{0}}}\text{-aS)D-}\frac{\text{1}}{\text{2}}\text{(b+i)}\text{D}^{\text{2}}
        ```

        令dW/dQ = 0，则社会最优停车密度为：D_s = \[(g+j)R - a\] / (b + i + f + k)$`\text{ }\frac{\text{dπ}}{\text{dD}}\text{=0}`$

        ``` math
        \text{D}_{\text{p}}\text{=}\frac{\text{g⋅}\frac{\text{H}}{\text{H}_{\text{0}}}\text{−aS}}{\text{b+i}}
        ```

        当d2W/dQ2 \< 0时，D_s为福利最大化点。$`\text{D}_{\text{p}}`$$`\frac{\text{d}^{\text{2}}\text{π}}{\text{d}\text{D}^{\text{2}}}\text{=−(aS+b+i)<0}`$

    2.  5.4 市场失灵证明

        ``` math
        \text{SW=TPR+TEB-TPC-TEC=((g+j)⋅}\frac{\text{H}}{\text{H}_{\text{0}}}\text{-aS)D-}\frac{\text{1}}{\text{2}}\text{(b+i+k)}\text{D}^{\text{2}}\text{-c⋅f⋅}\text{e}^{\text{fD}}\text{⋅}\frac{\text{H}}{\text{H}_{\text{0}}}
        ```
        市场失灵的产生是因为共享单车企业基于私人利润而非社会总福利做出投放决策。从企业角度看，最优停车密度在边际私人收益等于边际私人成本时达到。然而，这一决策忽略了强加给行人、附近商户和城市管理者的外部成本，如人行道拥堵、无序停放和额外治理费用。同时，企业未能完全捕获所有正外部收益，包括碳减排和改善首末段接驳可达性。因此，私人选择的密度倾向于超过社会最优密度。当D_p \> D_s时，过度投放出现，证明了市场失灵的存在。

        $`\frac{\text{d(SW)}}{\text{dD}}\text{=(g+j)}\frac{\text{H}}{\text{H}_{\text{0}}}\text{−aS−(b+i+k)D−c}\text{f}^{\text{2}}\frac{\text{H}}{\text{H}_{\text{0}}}\text{e}^{\text{fD}}\text{=0}`$

        ``` math
        \text{D}_{\text{s}}\text{=}\frac{\text{(g+j)}\frac{\text{H}}{\text{H}_{\text{0}}}\text{−aS}}{\text{(b+i+k)}}\text{−}\frac{\text{1}}{\text{f}}\text{W}\left( \frac{\text{c}\text{f}^{\text{3}}\text{H}}{\text{(b+i+k)}\text{H}_{\text{0}}}\text{exp}\left\lbrack \frac{\text{f}\left( \text{(}\text{g}\text{+}\text{j}\text{)}\text{H}\text{−}\text{aS}\text{H}_{\text{0}} \right)}{\text{(b+i+k)}\text{H}_{\text{0}}} \right\rbrack \right)
        ```
        <!-- -->5.5 最优投放量与社会福利损失计算

        5.5.1 最优投放量$`\frac{\text{d}^{\text{2}}\text{(SW)}}{\text{d}\text{D}^{\text{2}}}\text{=−(b+i+k)−c}\text{f}^{\text{3}}\frac{\text{H}}{\text{H}_{\text{0}}}\text{e}^{\text{fD}}\text{<0}`$$`\text{D}_{\text{s}}`$

    3.  **由总投放量Q = S x D，可得：私人最优投放量Q_p = S x D_p；社会最优投放量Q_s = S x D_s；超额投放量deltaQ = Q_p - Q_s（当Q_p \> Q_s时）**

        $`\text{ }\text{D}_{\text{p}}\text{>}\text{D}_{\text{s}}`$

4.  5.5.2 社会福利损失

    1.  社会福利损失（无谓损失）DWL = integral\_{Q_s}^{Q_p} (MSC - MSB) dQ，其中MSC为社会边际成本，MSB为社会边际收益。$`\text{Q=D⋅S}`$

        $`\text{Q}_{\text{p}}\text{=}\text{D}_{\text{p}}\text{⋅S}`$

        5.6 动态投放微分方程$`\text{Q}_{\text{s}}\text{=}\text{D}_{\text{s}}\text{⋅S}`$

        企业调整投放速度与其边际利润成正比：当边际利润为正时，企业增加投放；当边际利润为负时，企业减少投放。基于5.3.1节的私人利润函数，停车密度的动态调整满足以下微分关系：dD/dt = lambda(MPR - MPC)。$`\text{ΔQ=(}\text{D}_{\text{p}}\text{−}\text{D}_{\text{s}}\text{)⋅S}`$

    2.  
        ``` math
        \text{DWL=}\int_{\text{D}_{\text{s}}}^{\text{D}_{\text{p}}}{\text{(}\text{MPC}\text{+}\text{MEC}\text{-}\text{MPR}\text{-}\text{MEB}\text{)}}\text{dD=}\int_{\text{D}_{\text{s}}}^{\text{D}_{\text{p}}}\text{[aS+}\frac{\text{H}}{\text{H}_{\text{0}}}\text{(c}\text{e}^{\text{fD}}\text{+c-g-j)+(b+i+k)D]dD}
        ```

5.  lambda为反映企业对利润信号响应速度的调节速率系数；D(t)为t时刻的区域停车密度。

    ``` math
    \frac{\text{dD(t)}}{\text{dt}}\text{=λ⋅}\left( \text{g}\text{⋅}\frac{\text{H}}{\text{H}_{\text{0}}}\text{−}\text{aS}\text{−(}\text{b}\text{+}\text{i}\text{)}\text{D}\text{(}\text{t}\text{)} \right)
    ```

    $`\text{λ>0}`$$`\text{D(t)}`$

6.  本研究所有模型参数遵循一手实地数据优先、本地官方数据校准、权威文献基准补充的原则，时间维度统一以单日为基准，空间维度统一以平方米为基准，确保各参数物理意义明确、取值可追溯，且可与实地调查数据直接对接。各类参数的取值方法、参考区间与数据来源如下。

    **5.6.1 基础场景参数**

    此类参数为模型的外生输入变量，无需估算，可通过实地测量或官方公开数据直接获取。

    标准停车区面积$`S`$

    数据来源：本研究2026年6月实地测量数据。

    站点日均出站人流量$`H`$

    数据来源：实地调查数据。Kaggle平台公开数据集北京地铁各站进站出站10min客流统计。

    基准人流量$`\text{H}_{\text{0}}`$

    取值：固定为1000人次/天。

    数据来源：本研究设定。

    **5.6.2 私人成本参数**

    对应函数：MPC = a + bD$`\text{MPC}`$

    单位面积固定边际成本系数a

取值参考：0.07元/小时·m²。

数据来源：基于iResearch and Analysys（2026）《2026年中国共享单车行业研究报告》披露的北京地区单辆车日均运维成本约2.5元的基准值；北京公共非机动车停车设施的面积标准为1.5–1.8m²/车（北京市市场监督管理局, 2023），换算成面积约为0.56–0.67辆/m²，本研究默认企业追求最大投放密度，故取0.67辆/m²为标准投放密度。单辆车日均运维成本与标准投放密度相乘得到a。

密度边际成本递增系数b

取值参考：0.07313元/小时·(辆/m²)。

数据来源：由上文知标准投放密度为0.67辆/m²，单位面积成本为0.07元/小时·m²。Wu和Jiang（2025）演化博弈模型中高密度场景下运维成本递增幅度的测算结果显示：当企业实际投放量超出区域承载阈值的40%–60%时，单位运维成本较基准水平上升28%–42%。带入计算出成本增加量与密度增加量，前者除以后者计算出密度边际成本递增系数b的上限与下限（均约为0.07313）。

**5.6.3 边际外部成本参数**

对应MEC函数：MEC = c x e^(fD) x R

基准外部成本系数c

取值参考：0.022–0.025元/小时·(辆/m²)，基准取值0.0235元/小时·(辆/m²)。

数据来源：由低密度下共享单车乱停治理基础成本与公共空间占用机会成本两部分加总得出：乱停治理基础成本基于北京市交通委员会（2025）公布的全市年均超2亿元共享单车秩序清理总费用、覆盖约137万辆运营车辆的规模，折算得到单辆车日均基础治理成本约0.4元；公共空间机会成本以北京市城镇土地使用税二级区域24元/m²·年的税额标准为基准，折算得到日均单位面积空间成本约0.066元/m²，叠加商圈公共空间稀缺性2–3倍溢价修正为0.132–0.198元/天·(辆/m²)。单辆车日均基础治理成本与商圈日均单位面积空间成本相加得到c。

高密度恶化速率系数f

取值参考：0.42–0.50，基准取值0.46。

数据来源：本研究2026年6月实地调查数据拟合所得：基于五道口站B口与中关村站D口的早晚高峰停车密度—违规停放率观测样本，结合各站点出站人流量差异对外部成本的放大修正作用，对超出0.67辆/m²规范停放密度阈值后的违规率加速增长规律进行指数函数回归拟合得到恶化速率区间；该区间与Wu和Jiang（2025）中高密度下治理成本加速增长的实证结论一致。

**5.6.4 私人收益参数**

对应MPR函数：MPR = gR - iD

单位人流量边际收益系数g

取值参考：0.0133–0.0203元/小时·(辆/m²)。

基于官方行业运营数据结合商圈站点场景特征校准得出：依据北京市交通委员会（2026a）公布的海淀区共享单车全场景日均周转率3.84次/辆·天，结合iResearch and Analysys（2026）统计的北京市场单次骑行均价约1.5元，可测算全场景单辆车日均骑行收入为5.76元；考虑到核心商圈地铁站为地铁接驳高频需求场景，车辆周转效率显著高于全区平均水平，依据北京市交通委员会（2026a）《2025年北京市共享单车行业发展报告》中重点站点专项监测数据，中心城区核心商圈地铁接驳站点的共享单车日均周转率可达10–14次，对应单辆车日均骑行收入为15–21元/辆·天；该周转率水平对应日均出站客流4.3–4.7万人次的核心商圈站点，客流数据源自北京市交通委员会（2026a）配套站点客流统计与北京地铁运营有限公司2025年公开客流数据，与本研究样本站点的中位客流水平匹配；按人流量线性比例折算至人次/天的基准人流量下，最终得到基准人流量下单位停车密度的边际收益系数g的取值区间为0.0133–0.0203元/小时·(辆/m²)。$`H_{0} = 1000`$

边际收益递减系数i

取值参考：0.49–0.61元/小时·(辆/m²)，基准取值0.55元/小时·(辆/m²)。

数据来源：基于北京市交通委员会公布的行业运行数据校准。2019年上半年北京互联网租赁自行车日均骑行量约160.4万人次，车辆日均周转率约1.1次；2024年下半年日均骑行量为353.41万人次，车辆日均周转率为3.57次。由车辆规模=日均骑行量/日均周转率反推，2019年上半年运营车辆约145.82万辆，2024年下半年约98.99万辆。以北京市公共非机动车停车标准密度0.67辆/m²作为规范密度，则2019年过量投放状态对应密度约为0.99辆/m²，密度差为0.32辆/m²。周转率差为2.47次/辆·天，按北京共享单车单次骑行价格1.5–1.88元折算，单车小时收入差为2.47x(1.5–1.88)/24=0.154–0.193元/小时。再除以密度差0.32，得到i约等于0.49–0.61元/小时·(辆/m²)，基准值取0.55。

**5.6.5 边际外部收益参数**

对应MEB函数：MEB = jR - kD

单位人流量外部收益系数j

取值参考：0.022–0.034元/小时·(辆/m²)，基准取值0.028元/小时·(辆/m²)。

数据来源：外部收益主要由通勤时间节约和碳减排收益组成。中国城市规划设计研究院等发布的《2024年度中国主要城市共享单车/电单车骑行报告》显示，共享单车单次平均骑行距离约1.5公里、平均骑行时长约12.1分钟；若按普通步行速度4km/h计算，同距离步行约需22.5分钟，因此每次骑行节约通勤时间约10.4分钟。北京市统计局公布的2025年北京居民人均工资性收入为57376元，按年工作2000小时折算小时工资约28.69元；保守按50%工资率计入通勤时间价值，则每次骑行时间节约价值为28.69x50%x10.4/60约等于2.49元。碳减排部分依据共享出行生命周期研究中约48.7 gCO2e/人公里的减排强度，1.5公里对应约0.000073吨CO2e；按全国CCER市场约63.5–89.4元/吨的成交价格计算，碳减排货币价值仅约0.0046–0.0065元/次。因此单次外部收益约为2.50元。结合本文前文g使用的核心商圈地铁接驳站点日均周转率10–14次/辆·天、站点日均出站客流约4.3–4.7万人次，即R=43–47，可得j=\[(10–14)x2.50/24\]/(43–47)约等于0.022–0.034元/小时·(辆/m²)。$`\frac{H}{H_{0}}`$

外部收益递减系数k

取值参考：0.245–0.305元/小时·(辆/m²)，基准取值0.275元/小时·(辆/m²)。

数据来源：基于预调查车辆闲置率的边际变化规律：闲置车辆不产生碳减排与通勤效益，因此外部收益随密度递减；递减幅度约为私人收益递减系数的50%，参考Li和Xia（2026）中健康外部效益边际递减的特征校准。

**5.6.6 动态调整参数**

对应动态方程：dD/dt = lambda(MPR - MPC)

投放调整速度系数lambda

物理意义：企业根据边际利润信号调整区域投放密度的速度系数。为统一本文时间口径，lambda按小时计量，表示每小时可被调运或重新配置的车辆比例。

取值参考：0.0078–0.0082 h-1，基准取值0.008 h-1。

数据来源：北京市交通委员会《北京市交通委员会关于互联网租赁自行车行业2024年下半年运营监管情况的公示》显示，2024年全年北京市互联网租赁自行车日均骑行量为312.58万人次，车辆日均周转率为3.31次，日均调运17.70万辆次；由此反推车辆规模约为312.58/3.31=94.44万辆，日调运比例为17.70/94.44=18.74%，折算为小时调整率为18.74%/24=0.0078 h-1。2024年下半年日均骑行量为353.41万人次，车辆日均周转率为3.57次，日均调运19.40万辆次，反推车辆规模约为98.99万辆，小时调整率为(19.40/98.99)/24=0.0082 h-1。因此本文取lambda=0.0078–0.0082 h-1，基准值为0.008 h-1。

6.  Field Survey and Data Collection

    本研究选取北京市海淀区典型地铁站出口作为样本，包括五道口站B口、海淀黄庄站A1口、中关村站D口、长春桥站B口和C口。调查对象为各出站口附近的共享单车停放区域，调查时段覆盖早高峰与晚高峰，以观察共享单车在通勤接驳场景中的空间集聚、违规停放和潮汐变化。

本研究使用两类人流量数据。倒数第二列为2026年6月24日实地抽测的5分钟进出站人流量，主要用于反映现场观测时的人流状态；最后一列为Kaggle公开数据集北京地铁各站进站出站10min客流统计中2019年1月14日对应高峰期2小时总人流量，用于模型计算。由于本文模型时间单位统一为小时，因此将2小时总人流量除以2，得到小时人流量。考虑到研究对象为单个出站口，而非整站日客流，模型中采用站口级标准化客流强度R=H_h/100，其中H_h为小时人流量。

本研究共获得10个站口—时段观测点。其中长春桥B口早高峰未出现共享单车聚集，作为零投放观测保留，但不纳入密度—违规率回归。其余9个有效密度观测点共记录共享单车864辆，其中违规停放216辆，整体违规率为25.0%。9个有效观测点的平均停放密度为1.56辆/m²，中位数为1.28辆/m²，明显高于0.67辆/m²的标准停放密度。

Table 6-1. Field Survey Data by Exit and Peak Period

| Exit and Period | Area m2 | Bikes | Density bikes/m2 | Illegal Bikes | Illegal Rate | 2-hour Flow |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
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

Figure 6-1 shows that nearly all effective observations exceed the standard parking density. Wudaokou B AM is the most serious case, with a density of 3.773 bikes/m², approximately 5.63 times the standard threshold. This indicates that over-deployment is not an isolated phenomenon, but a common pattern around major metro exits.

Figure 6-1. Observed Parking Density vs. Standard Threshold

<img src="media/image1.png" style="width:5.5in;height:2.86in" />

7.  Empirical Analysis

    在站口级实证部分，本文采用单位面积标准化模型，以便比较不同面积停车区的投放密度。边际函数设定如下：

MPC = a + bD  
  
MEC = c x e^(fD) x R  
  
MPR = gR - iD  
  
MEB = jR - kD

其中，D为共享单车停放密度，R为标准化小时客流强度。基准参数取值为：a=0.07，b=0.07313，c=0.0235，f=0.46，g=0.0168，i=0.55，j=0.028，k=0.28。私人最优密度D_p由MPR=MPC得到，社会最优密度D_s由MPR+MEB=MPC+MEC得到。

7.2 为什么实际投放密度远高于标准密度、私人最优密度和社会最优密度

模型结果显示，实际观测密度不仅普遍高于标准密度0.67辆/m²，也显著高于私人最优密度和社会最优密度。以五道口B口早高峰为例，实际密度为3.773辆/m²，是标准密度的5.63倍，是私人最优密度0.311的约12.1倍，是社会最优密度0.244的约15.5倍。这一差异说明，现实中的共享单车投放并不是简单围绕边际收益和边际成本自动收敛，而是受到多重机制影响。  
  
第一，实际密度反映的是存量堆积，而模型最优密度反映的是当前时段的边际最优。共享单车不会在一个高峰期开始时自动归零，而是受到前一时段遗留车辆、用户骑行方向和平台调度滞后的影响。因此，观测到的车辆数量往往包含历史积压，而不只是当前小时新增需求。  
  
第二，高客流站点具有明显的覆盖竞争效应。五道口、中关村和海淀黄庄等站点具有较高潜在订单量，企业为了提升用户可见度和可获得性，倾向于在这些站点保留更多车辆。即使边际利润已经下降，车辆仍然可能因为市场份额竞争、品牌曝光和抢占高需求点位而继续堆积。  
  
第三，企业并未完全承担公共空间外部成本。违规停放造成的行人绕行、通道占用和治理成本主要由行人、地铁周边商户和城市管理部门承担，而不是直接由平台企业承担。因此，在缺少强约束的情况下，企业的投放密度会系统性高于社会最优密度。  
  
第四，调度速度不足导致高密度状态持续存在。动态方程显示，企业自然调整的收敛速度为lambda(b+i)。基准参数下lambda=0.008，b+i=0.62313，因此半衰期约为139小时，接近5.8天。这说明如果只依靠企业根据利润信号自然调整，车辆密度很难在早晚高峰之间迅速回到合理水平。  
  
第五，部分站点停车区面积较小，导致少量车辆变化也会造成密度剧烈上升。例如长春桥B口停车区面积仅37.73m²，晚高峰53辆车即可形成1.405辆/m²的高密度。说明共享单车治理不能只看车辆绝对数量，还必须结合停车区面积和单位面积密度。  
  
因此，实际密度远高于标准、私人最优和社会最优密度，并不意味着模型失效，而是说明现实市场中存在存量惯性、潮汐错配、竞争性投放和外部成本转嫁。这些因素共同导致企业实际行为偏离私人静态最优，更偏离社会福利最优。

7.3 密度与违规停放关系  
  
Figure 7-1 shows a strong positive relationship between parking density and illegal parking rate. The Pearson correlation coefficient is 0.932, and the fitted relationship is:  
  
Illegal Rate = -21.9 + 22.4 x Density  
  
with R² = 0.869. This indicates that density is a key driver of negative externalities. When density exceeds the standard threshold, disorderly parking rises sharply rather than gradually. Wudaokou B AM again provides the clearest example: density reaches 3.773 bikes/m² and the illegal parking rate reaches 66.9%.

Figure 7-1. Parking Density and Illegal Parking Rate

<img src="media/image2.png" style="width:5.5in;height:3.40476in" />

7.4 私人总收益与社会总收益曲线  
  
根据修正后的定义，私人总收益为TPR-TPC，社会总收益为TBE-TEC。Figure 7-2 plots the two curves under the representative case of Wudaokou B AM. The private net benefit curve reaches its maximum at D_p约等于0.311, while the social net benefit curve reaches its maximum at D_s约等于0.155. The social peak appears much earlier than the private peak, showing that external benefits are quickly offset by congestion and governance costs once density increases.  
  
At the observed density D=3.773, both curves are already on the declining side. Under the baseline parameters, TPR-TPC约等于-3.71 yuan/hour and TBE-TEC约等于-4.08 yuan/hour. This means the observed over-deployment no longer improves either private net benefit or social net benefit. It is therefore not merely a case of private optimum exceeding social optimum; rather, the actual market outcome has moved far beyond both optima due to stock accumulation, delayed dispatch, and competitive over-presence.

Figure 7-2. Private Net Benefit and Social Net Benefit by Density

<img src="media/image3.png" style="width:5.5in;height:3.40476in" />

7.5 社会福利损失  
  
Table 7-2. Welfare Loss by Exit and Peak Period  
  
The total welfare loss over all observed two-hour peak periods is approximately 1776.99 yuan. Wudaokou B AM alone accounts for more than half of the total loss, making it the most urgent governance target.

|      Exit and Period      | Welfare Loss yuan/2h |
|:-------------------------:|:--------------------:|
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

7.6 潮汐现象与动态调控  
  
Table 7-3. Tidal Pattern between Morning and Evening Peaks  
  
The data show clear tidal movement. Wudaokou B and Zhongguancun D experience severe morning accumulation, while Haidian Huangzhuang A1 and Changchunqiao B show evening return patterns. This means fixed daily quotas are insufficient. Regulation should be time-specific and exit-specific.  
  
Based on the dynamic equation, firms adjust toward the private optimum slowly. Figure 7-3 shows that even under the highest lambda value, the adjustment path remains gradual. Therefore, firms should not wait for passive market adjustment. Instead, they should implement pre-peak dispatch and post-peak clearing. For Wudaokou B and Zhongguancun D, vehicles should be moved away before the morning peak. For Haidian Huangzhuang A1 and Changchunqiao B, evening return should be monitored and cleared after the peak.

| Exit | Change in Bikes PM-AM | Change in Density | Pattern |
|:--:|:--:|:--:|:--:|
| Wudaokou B | -166 | -2.495 | Morning accumulation |
| Haidian Huangzhuang A1 | +30 | +0.380 | Evening return |
| Zhongguancun D | -97 | -1.355 | Morning accumulation |
| Changchunqiao C | -6 | -0.194 | Low-intensity stable |
| Changchunqiao B | +53 | +1.405 | Evening return surge |

Figure 7-3. Dynamic Adjustment Path under the Deployment Equation

<img src="media/image4.png" style="width:5.5in;height:3.40476in" />

7.7 敏感性分析  
  
Figures 7-4 and 7-5 present sensitivity analysis for c, f, g, i, j, k, and lambda. The results show that j has the strongest effect on socially optimal density. When j rises from 0.022 to 0.034, average socially optimal density increases from 0.087 to 0.194 bikes/m². This means that if the external benefits of shared bikes, such as time savings and carbon reduction, are larger, society can tolerate a higher density.  
  
In contrast, higher c, f, i, and k generally increase welfare loss or reduce the socially optimal density. lambda does not change the equilibrium density; it only affects the speed of adjustment. Therefore, lambda is more relevant for operational dispatch than for determining the optimal deployment level.

Figure 7-4. Sensitivity Analysis: Welfare Loss under Observed Density

<img src="media/image5.png" style="width:5.5in;height:2.93333in" />

Figure 7-5. Sensitivity Analysis: Average Socially Optimal Density

<img src="media/image6.png" style="width:5.5in;height:2.93333in" />

8.  Conclusions

    本研究表明，海淀区地铁站出口周围的共享单车投放量远高于空间标准、私人最优和社会最优水平。差距在五道口B口早高峰和中关村D口早高峰尤为显著。主要原因是观测密度反映了存量堆积、竞争性过度投放和调度滞后，而模型最优反映的是当前时段成本与收益的边际平衡。  
      
    结果证实了市场失灵的存在。企业未能完全内部化人行道占用、无序停放、行人延误和治理成本。因此，其投放行为倾向于超过社会最优水平。在某些情况下，实际密度甚至超过了私人最优，表明真实市场结果不仅由即时利润最大化塑造，还受到竞争和运营惯性的影响。  
      
    因此，政策应结合三种工具。第一，应建立站点出口级密度上限。0.67辆/m²的标准密度可作为基本上限，而基于模型的社会最优可为严重拥堵出口提供更严格的控制指引。第二，调度应是动态的。五道口B口和中关村D口等早高峰聚集点需要高峰前削减；海淀黄庄A1口和长春桥B口等晚高峰回流点需要高峰后清理。第三，平台考核应纳入超密度持续时间、违规停放率、调度响应时间和站点出口级合规性指标。  
      
    总体而言，共享单车为地铁接驳提供了正向价值，但前提是密度保持在公共空间的承载能力之内。一旦密度超过社会最优，边际社会成本迅速上升，系统从改善流动性转向公共空间拥堵。因此，核心政策目标不是普遍减少共享单车，而是使单车密度与站点级需求、停车容量和时段性潮汐流动相匹配。

    References

    北京市交通委员会. (2026a). 2025年北京市共享单车行业发展报告. https://jtysj.beijing.gov.cn/

    北京市交通委员会. (2026b, 4月14日). 关于哈啰单车非法过量投放共享单车的通报. https://jtysj.beijing.gov.cn/

    北京青年报. (2026, 4月7日). 上地街道新增3000余个非机动车停车位. https://www.ynet.com/

    中国自行车协会. (2026, 1月22日). 2025年中国共享单车行业发展报告. https://www.chinabicycle.org.cn/

    海淀区融媒体中心. (2026, 5月21日). 美团单车在海淀区日均骑行量超过30万次. https://www.bjhd.gov.cn/

    Industry Research. (2026, 3月5日). 2026年全球共享单车市场报告. https://www.industryresearch.biz/

    iResearch and Analysys. (2026, 5月22日). 2026年中国共享单车行业研究报告. https://www.iresearch.com.cn/

    人民日报. (2026, 5月14日). 全国日均共享单车骑行量达1.2亿次. https://www.people.com.cn/

    央视新闻. (2026, 4月14日). 哈啰单车因非法过量投放共享单车被立案调查. https://news.cctv.cn/2026/04/14/ARTI6VXb1l6zr75z6Z9PcYVT260414.shtml

    Chen, Y., Zhu, X., Li, J., and Bai, Y. (2024). Chinas bike-sharing boom: How two wheels drive urban consumption. China Economic Quarterly International, 4(2), 123-136. https://doi.org/10.1016/j.ceqi.2024.03.002

    Dai, Y. (2026). The green ride: Bike-sharing platforms and urban carbon reduction. China Economist, 21(1), 45-62.

    Li, X., and Xia, C. (2026). Pedaling to wellness: The impact of dockless bike-sharing services on physical and mental health in China. Journal of Development Economics, 179, 103619. https://doi.org/10.1016/j.jdeveco.2025.103619

    Wu, X., and Jiang, L. (2025). Evolutionary game research on the decision-making of shared bike placement volume based on dynamic and static punishment mechanisms. Transportation Planning and Technology, 48(5), 853-876. https://doi.org/10.1080/03081060.2024.2383304

    Zhang, H., Wang, X., and Liu, S. (2026). A city shared bike dispatch approach based on temporal graph convolutional network and genetic algorithm. Computational Intelligence and Neuroscience, 2026, 1-12. https://doi.org/10.1155/2026/9876543

    北京市交通委员会. (2025). 北京市互联网租赁自行车行业2024年下半年运营监管情况的公示. https://jtw.beijing.gov.cn/xxgk/tzgg/202505/t20250530_4102425.html

    昆明市交通运输局. (2025). 昆明市互联网租赁自行车投放数量及停车泊位规模测算报告. https://jtys.km.gov.cn/upload/resources/file/2025/11/19/4151068.pdf

    Beijing Municipal Administration for Market Regulation. (2023). Specifications of setting parking facilities for non-motor vehicle in urban road spaces (DB11/T 2112-2023). Beijing: Beijing Municipal Administration for Market Regulation.

    \[与上文重复，已删除以避免重复。\]

    北京市统计局, and 国家统计局北京调查总队. (2026, 3月25日). 北京市2025年国民经济和社会发展统计公报. https://tjj.beijing.gov.cn/zxfbu/202603/t20260324_4564401.html

    人民日报. (2019, 8月1日). 一辆共享单车日周转率仅为1.1次. 人民网财经. https://capital.people.com.cn/n1/2019/0801/c405954-31269731.html

    中国城市规划设计研究院, 住房和城乡建设部城市交通基础设施监测与治理实验室, and 滴滴青桔. (2024, 9月). 2024年度中国主要城市共享单车/电单车骑行报告. https://www.cswcr.com/2024年度中国主要城市共享单车电单车骑行报告.pdf

    中华人民共和国建设部. (1995). 城市道路交通规划设计规范（GB 50220-95）. 中国建筑工业出版社.

    全国温室气体自愿减排交易系统. (n.d.). 交易数据. 2026年6月25日获取, https://www.ccer.com.cn/

    北京绿色交易所有限公司. (2026). 2025年全国温室气体自愿减排（CCER）交易市场运行情况一览. https://www.cbgex.com.cn/details/408310521591238656

    IT之家. (2026, 6月18日). 美团、滴滴北京共享单车调价，平日起步价上涨、时间延长至60分钟. https://www.ithome.com/0/965/752.htm

    Niu, Z., and Chai, L. (2022). Carbon emission reduction by bicycle-sharing in China. Energies, 15(14), 5136. https://doi.org/10.3390/en15145136

    Appendices

    附录A：实地调查原始数据与计算表
