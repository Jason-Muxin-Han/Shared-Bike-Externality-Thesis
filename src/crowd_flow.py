import pandas as pd

# 原始地铁客流 CSV 为第三方数据，未随本仓库分发。
# 如需复现，请自行准备并放到 data/ 目录下。
df_data = pd.read_csv(
    'data/metro_passengers_20190114.csv',
    encoding='gbk'
)

stations = ['中关村', '海淀黄庄', '长春桥', '五道口']

# 转换进站、出站时间
df_data['entry_tm'] = pd.to_datetime(df_data['entry_tm'], format='%Y%m%d%H%M%S')
df_data['exit_tm'] = pd.to_datetime(df_data['exit_tm'], format='%Y%m%d%H%M%S')

# 筛选进站数据
entry = df_data[df_data['entry_Station_Nme'].isin(stations)].copy()
entry = entry[['entry_Station_Nme', 'entry_tm']]
entry.columns = ['站点', '时间']

# 筛选出站数据
exit_ = df_data[df_data['exit_Station_Nme'].isin(stations)].copy()
exit_ = exit_[['exit_Station_Nme', 'exit_tm']]
exit_.columns = ['站点', '时间']

# 合并进站和出站，作为总人流量
flow = pd.concat([entry, exit_], ignore_index=True)

# 判断早晚高峰
def get_period(t):
    hour = t.hour + t.minute / 60

    if 7 <= hour < 9:
        return '早上7-9点'
    elif 17 <= hour < 19:
        return '晚上5-7点'
    else:
        return None

flow['时间段'] = flow['时间'].apply(get_period)

# 只保留早晚高峰
flow = flow.dropna(subset=['时间段'])

# 统计人数
result = (
    flow
    .groupby(['站点', '时间段'])
    .size()
    .reset_index(name='总人流量')
)

# 排序
result['站点'] = pd.Categorical(result['站点'], categories=stations, ordered=True)
result['时间段'] = pd.Categorical(
    result['时间段'],
    categories=['早上7-9点', '晚上5-7点'],
    ordered=True
)

result = result.sort_values(['站点', '时间段']).reset_index(drop=True)

print(result)
