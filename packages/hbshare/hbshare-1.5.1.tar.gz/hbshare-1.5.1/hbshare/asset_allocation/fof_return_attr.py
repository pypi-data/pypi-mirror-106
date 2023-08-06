import os

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings(action='ignore')


class FOFReturnAttr:
    def __init__(self, start_date, end_date, path):
        """
        :param start_date: 绩效分解的起始日期
        :param end_date: 绩效分解的结束日期
        :param 估值表文件存储地址
        """
        self.start_date = start_date
        self.end_date = end_date
        self.path = path
        self._load_data()

    def _load_data(self):
        """
        解析估值表数据
        """
        data_path = os.path.join(self.path, r'data')
        filenames = os.listdir(data_path)

        holding_data = []
        date_list = []
        mkt_list = []
        div_list = []
        for name in filenames:
            file_path = os.path.join(data_path, name)
            date = name.split('_')[0].replace('-', '')
            if (date > self.end_date) or (date < self.start_date):
                continue
            data = pd.read_excel(file_path, header=3)
            # 银行存款
            tmp = data[data['科目代码'] == '1002']
            bank_cash = float(tmp['市值'].values[0]) if not tmp.empty else 0
            # 基金投资
            tmp = data[data['科目代码'] == '1105']
            mutual_fund = float(tmp['市值'].values[0]) if not tmp.empty else 0
            # 理财产品
            tmp = data[data['科目代码'] == '1109']
            private_fund = float(tmp['市值'].values[0]) if not tmp.empty else 0
            # 应收股利
            tmp = data[data['科目代码'] == '1203']
            dividend = float(tmp['市值'].values[0]) if not tmp.empty else 0
            # 证券清算款
            tmp = data[data['科目代码'] == '30030501']
            settle_buy_m = float(tmp['市值'].values[0]) if not tmp.empty else 0
            tmp = data[data['科目代码'] == '30030502']
            settle_sell_m = float(tmp['市值'].values[0]) if not tmp.empty else 0
            tmp = data[data['科目代码'] == '30032001']
            settle_buy_p = float(tmp['市值'].values[0]) if not tmp.empty else 0
            tmp = data[data['科目代码'] == '30032002']
            settle_sell_p = float(tmp['市值'].values[0]) if not tmp.empty else 0
            # 应收申购款
            tmp = data[data['科目代码'] == '1207']
            subscribe = float(tmp['市值'].values[0]) if not tmp.empty else 0
            # 应付赎回款
            tmp = data[data['科目代码'] == '2203']
            redeem = float(tmp['市值'].values[0]) if not tmp.empty else 0
            # 基金资产净值
            net_asset = float(data[data['科目代码'] == '基金资产净值:']['市值'].values[0])
            # 持仓
            data1 = data[~data['科目代码'].isnull()]
            data1['sign'] = data1['科目代码'].apply(lambda x: x[:8])
            data1 = data1[data1['sign'].isin(['11050201', '11090601'])]
            data1['sign_2'] = data1['科目代码'].apply(lambda x: len(x))
            data1 = data1[data1['sign_2'] > 8][['科目名称', '数量', '单位成本', '成本', '市价']]
            data1.rename(
                columns={"科目名称": "name", "数量": "volume", "单位成本": "unit_cost", "成本": "cost", "市价": "price"},
                inplace=True)
            data1['date'] = date
            # 股利
            data2 = data[~data['科目代码'].isnull()]
            data2 = data2[data2['科目代码'].str.startswith('1203')]
            data2['len'] = data2['科目代码'].apply(lambda x: len(x))
            data2 = data2[data2['len'] > 8]
            data2['date'] = date

            holding_data.append(data1)
            date_list.append(date)
            mkt_list.append([mutual_fund, private_fund, settle_buy_m, settle_sell_m, settle_buy_p, settle_sell_p,
                             dividend, redeem, subscribe, bank_cash, net_asset])
            div_list.append(data2[['科目名称', '市值', 'date']])

        self.mkv_df = pd.DataFrame(
            data=mkt_list, index=date_list, columns=['基金投资', '理财产品', '证券清算款-基金申购', '证券清算款-基金赎回',
                                                     '证券清算款-理财申购', '证券清算款-理财赎回', '应收股利', '应付赎回款',
                                                     '应收申购款', '银行存款', '基金资产净值'])
        self.holding_df = pd.concat(holding_data)
        self.div_df = pd.concat(div_list)

    def calculate_actual_return(self):
        """
        证券资产层面的损益分析
        """
        mkv_df = self.mkv_df.copy()
        # 手动微调
        mkv_df.loc['20200121', '证券清算款-基金申购'] = 5000000.
        mkv_df.loc['20200121', '证券清算款-理财申购'] = 0.
        # 先处理申购赎回
        # part1：公募基金的申赎去重: 申购不重复，赎回在当天就生效，因此需要去掉连续重复非0的赎回数据, keep='first'
        tmp = mkv_df[(mkv_df['证券清算款-基金赎回'] > 0) &
                     (mkv_df['证券清算款-基金赎回'].shift(1) == mkv_df['证券清算款-基金赎回'])]
        mkv_df.loc[tmp.index.tolist(), '证券清算款-基金赎回'] = 0.
        # part2: 私募基金的申购去重：1、对于A A+B B类型的处理，把A+B替换成A
        tmp = mkv_df[(mkv_df['证券清算款-理财申购'] == mkv_df['证券清算款-理财申购'].shift(1) +
                      mkv_df['证券清算款-理财申购'].shift(-1)) & (mkv_df['证券清算款-理财申购'] > 0) &
                     (mkv_df['证券清算款-理财申购'].shift(1) > 0) &
                     (mkv_df['证券清算款-理财申购'].shift(-1) > 0)]
        mkv_df.loc[tmp.index.tolist(), '证券清算款-理财申购'] = np.NaN
        mkv_df['证券清算款-理财申购'] = mkv_df['证券清算款-理财申购'].fillna(method='ffill')
        # part2: 然后去掉连续重复非0的私募申购数据, keep='last'
        tmp = mkv_df[(mkv_df['证券清算款-理财申购'] > 0) &
                     (mkv_df['证券清算款-理财申购'].shift(-1) == mkv_df['证券清算款-理财申购'])]
        mkv_df.loc[tmp.index.tolist(), '证券清算款-理财申购'] = 0.
        # part3: 私募基金的赎回去重
        tmp = mkv_df[(mkv_df['证券清算款-理财赎回'] > 0) &
                     (mkv_df['证券清算款-理财赎回'].shift(1) == mkv_df['证券清算款-理财赎回'])]
        mkv_df.loc[tmp.index.tolist(), '证券清算款-理财赎回'] = 0.

        # 公募市值复权
        mkv_df['m_cum_subscribe'] = mkv_df['证券清算款-基金申购'].shift(1).fillna(0.).cumsum()
        mkv_df['m_cum_redeem'] = mkv_df['证券清算款-基金赎回'].cumsum()
        mkv_df['adj_na_m'] = mkv_df['基金投资'] - (mkv_df['m_cum_subscribe'] - mkv_df['m_cum_redeem'])

        # 私募市值复权
        mkv_df['p_cum_subscribe'] = mkv_df['证券清算款-理财申购'].shift(1).fillna(0.).cumsum()
        mkv_df['p_cum_redeem'] = mkv_df['证券清算款-理财赎回'].cumsum()
        mkv_df['adj_na_p'] = mkv_df['理财产品'] - (mkv_df['p_cum_subscribe'] - mkv_df['p_cum_redeem'])

        mkv_df['all'] = mkv_df['adj_na_m'] + mkv_df['adj_na_p']
        security_return = mkv_df['all'].diff().dropna()

        return security_return

    def calculate_return_attr(self):
        """
        细分到每个公私募基金层面的损益分析
        """
        date_list = sorted(self.mkv_df.index.tolist())
        return_attr = []
        for i in range(1, len(date_list)):
            tdate = date_list[i]
            pre_date = date_list[i - 1]
            df_pre = self.holding_df[self.holding_df['date'] == pre_date].set_index(
                'name').rename(columns={"volume": "pre_volume", "cost": "pre_cost", "price": "pre_price"})[
                ['pre_volume', 'pre_cost', 'pre_price']]
            df = self.holding_df[self.holding_df['date'] == tdate].set_index('name')[['volume', 'cost', 'price']]
            df = pd.merge(df, df_pre, left_index=True, right_index=True, how='outer').fillna(0.)
            # 1、数量不变
            part1 = df[df['volume'] == df['pre_volume']]
            part1['earning'] = part1['pre_volume'] * (part1['price'] - part1['pre_price'])
            # 2、数量从0到有
            part2 = df[(df['pre_volume'] == 0) & (df['volume'] > 0)]
            part2['earning'] = part2['volume'] * part2['price'] - part2['cost']
            # 3、数量从有到0
            part3 = df[(df['pre_volume'] > 0) & (df['volume'] == 0)]
            part3['earning'] = 0
            # 4、数量增加
            part4 = df[(df['volume'] > df['pre_volume']) * (df['pre_volume'] > 0)]
            part4['mkv_change'] = part4['price'] * part4['volume'] - part4['pre_price'] * part4['pre_volume']
            part4['cost_change'] = part4['cost'] - part4['pre_cost']
            part4['earning'] = part4['mkv_change'] - part4['cost_change']
            # 1、由于申购导致的数量增加; 2、由于分红但股利直接转化为份额
            part4['earning'] = np.where(
                part4['earning'].abs() > part4['mkv_change'].abs(), part4['mkv_change'], part4['earning'])
            del part4['mkv_change']
            del part4['cost_change']
            # 5-1、数量减少:由于赎回操作
            part5_1 = df[(df['volume'] < df['pre_volume']) * (df['volume'] > 0) & (df['cost'] < df['pre_cost'])]
            part5_1['earning'] = part5_1['volume'] * (part5_1['price'] - part5_1['pre_price'])
            # 5-2、数量减少：由于计提业绩报酬
            part5_2 = df[(df['volume'] < df['pre_volume']) * (df['volume'] > 0) & (df['cost'] == df['pre_cost'])]
            part5_2['earning'] = part5_2['volume'] * part5_2['price'] - part5_2['pre_volume'] * part5_2['pre_price']

            attr_df = pd.concat([part1, part2, part3, part4, part5_1, part5_2])[['earning']]
            attr_df['date'] = tdate
            return_attr.append(attr_df)

        return_attr = pd.concat(return_attr).reset_index()
        # 添加股利
        div_df = self.div_df.rename(columns={"科目名称": "name", "市值": "dividend"})
        div_df.sort_values(by=['name', 'date'], ascending=[False, True])
        div_df = div_df.drop_duplicates(subset=['name', 'dividend'], keep='first')
        return_attr = pd.merge(return_attr, div_df, on=['name', 'date'], how='outer').fillna(0.)
        return_attr['earning'] += return_attr['dividend']

        return return_attr

    def calculate_asset_return(self):
        """
        资产净值层面的损益分析
        """
        df = self.mkv_df.copy()
        # 赎回去重
        tmp = df[(df['应付赎回款'] > 0) &
                 (df['应付赎回款'].shift(1) == df['应付赎回款'])]
        df.loc[tmp.index.tolist(), '应付赎回款'] = 0.
        df['应付赎回款'] = df['应付赎回款'].cumsum()
        # 申购去重
        tmp = df[(df['应收申购款'] > 0) &
                 (df['应收申购款'].shift(1) == df['应收申购款'])]
        df.loc[tmp.index.tolist(), '应收申购款'] = 0.
        df['应收申购款'] = df['应收申购款'].cumsum()

        df['fund_asset'] = df['基金资产净值'] + df['应付赎回款'] - df['应收申购款']
        fof_return = df['fund_asset'].diff().dropna()

        return fof_return

    def return_attr_compare(self):

        return_attr = self.calculate_return_attr()
        security_return = self.calculate_actual_return()
        fof_return = self.calculate_asset_return()

        compare_df = return_attr.groupby('date')['earning'].sum().to_frame(name='return_attr').merge(
            security_return.to_frame(name='security_return'), left_index=True, right_index=True).merge(
            fof_return.to_frame(name='fof_return'), left_index=True, right_index=True)
        compare_df['diff'] = (compare_df['return_attr'] - compare_df['fof_return']).abs()
        compare_df.sort_values(by='diff', ascending=False, inplace=True)

        date_list = sorted(compare_df.index.tolist())
        select_date = compare_df.index.tolist()[:10]
        volume_change = []
        for date in select_date:
            pre_date = date_list[date_list.index(date) - 1]
            df_pre = self.holding_df[self.holding_df['date'] == pre_date].set_index(
                'name').rename(columns={"volume": "pre_volume", "cost": "pre_cost", "price": "pre_price"})[
                ['pre_volume', 'pre_cost', 'pre_price']]
            df = self.holding_df[self.holding_df['date'] == date].set_index('name')[['volume', 'cost', 'price']]
            df = pd.merge(df, df_pre, left_index=True, right_index=True, how='outer').fillna(0.)
            df = df[df['pre_volume'] != df['volume']]
            df['date'] = date
            volume_change.append(df)

        volume_change = pd.concat(volume_change)

        return compare_df, volume_change


if __name__ == '__main__':
    # res = FOFReturnAttr(start_date='20210104', end_date='20210429', path="D:\\kevin\\绩效归因").calculate_return_attr()
    res = FOFReturnAttr(start_date='20200104', end_date='20210429', path='D:\\kevin\\绩效归因').return_attr_compare()