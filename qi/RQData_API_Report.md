# RQData API 调用指南

## 米筐 A股财务与因子数据 API 调用指南

详细说明如何调用米筐 RQData 的 A股财务数据和因子数据

---

## 目录

- [一、A股财务数据 API](#一a股财务数据-api)
  - [1.1 get_pit_financials_ex - 季度财务数据](#11-get_pit_financials_ex---季度财务数据)
  - [1.2 三大报表字段列表](#12-三大报表字段列表)
  - [1.3 财务快报与预告](#13-财务快报与预告)
- [二、A股因子数据 API](#二a股因子数据-api)
  - [2.1 get_factor - 获取因子值](#21-get_factor---获取因子值)
  - [2.2 财务衍生指标因子](#22-财务衍生指标因子)
  - [2.3 技术指标因子](#23-技术指标因子)
  - [2.4 Alpha101 因子](#24-alpha101-因子)
- [三、使用示例](#三使用示例)

---

## 一、A股财务数据 API

米筐 RQData 提供完整的 A股财务数据接口，包括季度财务数据、财务快报、业绩预告等。所有财务数据均基于新会计准则，并实现了 LF、LYR、TTM 三种计算逻辑。

### 1.1 get_pit_financials_ex - 季度财务数据

**函数说明**：以给定一个报告期回溯的方式获取季度基础财务数据（三大表），即利润表、资产负债表、现金流量表。

```python
get_pit_financials_ex(order_book_ids, fields, start_quarter, end_quarter,
                      date=None, statements='latest', market='cn')
```

#### 参数说明

| 参数名 | 类型 | 说明 |
|--------|------|------|
| order_book_ids | str or list | 必填，合约代码，可传入 order_book_id 或 list |
| fields | list | 必填，需要的财务字段列表 |
| start_quarter | str | 必填，起始报告期，如"2015q2" |
| end_quarter | str | 必填，结束报告期，如"2015q4" |
| date | datetime | 查询日期，默认当前最新日期 |
| statements | str | 'latest'返回最新记录，'all'返回所有 |
| market | str | 市场，默认'cn'中国内地 |

#### 返回字段

| 字段名 | 类型 | 说明 |
|--------|------|------|
| quarter | str | 报告期 |
| info_date | Timestamp | 公告发布日 |
| fields | list | 返回的财务字段 |
| if_adjusted | int | 0代表当期，1代表非当期 |

---

### 1.2 三大报表字段列表

#### 利润表字段

| 字段名 | 说明 |
|--------|------|
| revenue | 营业总收入 |
| operating_revenue | 营业收入 |
| net_interest_income | 利息净收入 |
| net_commission_income | 手续费及佣金净收入 |
| total_expense | 营业总成本 |
| cost_of_goods_sold | 营业成本 |
| sales_tax | 营业税 |
| gross_profit | 主营业务利润 |
| selling_expense | 销售费用 |
| ga_expense | 管理费用 |
| financing_expense | 财务费用 |
| r_n_d | 研发费用 |
| profit_from_operation | 营业利润 |
| investment_income | 投资收益 |
| net_profit | 净利润 |
| net_profit_parent_company | 归属母公司净利润 |
| basic_earnings_per_share | 基本每股收益 |
| fully_diluted_earnings_per_share | 稀释每股收益 |

#### 资产负债表字段

| 字段名 | 说明 |
|--------|------|
| cash_equivalent | 货币资金 |
| bill_receivable | 应收票据 |
| net_accts_receivable | 应收账款净额 |
| prepayment | 预付账款 |
| inventory | 存货 |
| current_assets | 流动资产合计 |
| financial_asset_held_for_trading | 交易性金融资产 |
| total_fixed_assets | 固定资产合计 |
| total_assets | 总资产 |
| short_term_loans | 短期借款 |
| notes_payable | 应付票据 |
| accts_payable | 应付账款 |
| advance_from_customers | 预收账款 |
| payroll_payable | 应付职工薪酬 |
| tax_payable | 应交税费 |
| current_liabilities | 流动负债合计 |
| total_liabilities | 负债合计 |
| paid_in_capital | 实收资本(或股本) |
| capital_reserve | 资本公积金 |
| surplus_reserve | 盈余公积 |
| undistributed_profit | 未分配利润 |
| equity_parent_company | 归属于母公司所有者权益合计 |
| total_equity | 股东权益合计 |

#### 现金流量表字段

| 字段名 | 说明 |
|--------|------|
| cash_received_from_sales_of_goods | 销售商品、提供劳务收到的现金 |
| refunds_of_taxes | 收到的税费返还 |
| cash_received_from_other_operation_activities | 收到其他与经营活动有关的现金 |
| cash_paid_for_goods | 购买商品、接受劳务支付的现金 |
| cash_paid_for_employee | 支付给职工以及为职工支付的现金 |
| cash_paid_for_taxes | 支付的各项税费 |
| cash_paid_for_operation_activities | 经营活动现金流出小计 |
| cash_flow_from_operating_activities | 经营活动产生的现金流量净额 |
| cash_received_from_disposal_of_investment | 收回投资收到的现金 |
| cash_received_from_investment | 取得投资收益收到的现金 |
| cash_paid_for_asset | 购建固定资产支付的现金 |
| cash_paid_to_acquire_investment | 投资支付的现金 |
| cash_flow_from_investing_activities | 投资活动产生的现金流量净额 |
| cash_received_from_investors | 吸收投资收到的现金 |
| cash_received_from_financial_institution_borrows | 取得借款收到的现金 |
| cash_paid_for_debt | 偿还债务支付的现金 |
| cash_paid_for_dividend_and_interest | 分配股利、利润或偿付利息支付的现金 |
| cash_flow_from_financing_activities | 筹资活动产生的现金流量净额 |

---

### 1.3 财务快报与预告

#### current_performance - 财务快报

```python
current_performance(order_book_ids, info_date=None, quarter=None,
                    interval='1q', fields=None, market='cn')
```

**常用字段**：operating_revenue(营业收入), operating_profit(营业利润), total_profit(利润总额), np_parent_owners(归母净利润), total_assets(总资产), roe(净资产收益率)

#### performance_forecast - 业绩预告

```python
performance_forecast(order_book_ids, info_date=None, end_date=None,
                     fields=None, market='cn')
```

**常用字段**：forecast_type(预期类型), forecast_growth_rate_floor/ceiling(预期增长幅度), forecast_np_floor/ceiling(预期净利润)

---

## 二、A股因子数据 API

米筐 RQData 提供丰富的因子数据，包括财务衍生指标、技术指标、Alpha101 因子等。财务衍生指标经过 LF、LYR、TTM 三种处理逻辑，可满足不同量化研究需求。

### 2.1 get_factor - 获取因子值

```python
get_factor(order_book_ids, factor, start_date=None, end_date=None,
           universe=None, expect_df=True, market='cn')
```

#### 参数说明

| 参数名 | 类型 | 说明 |
|--------|------|------|
| order_book_ids | str or list | 必填，合约代码列表 |
| factor | str or list | 必填，因子名称，可通过 get_all_factor_names() 获取 |
| start_date | datetime | 开始日期（与 end_date 同时使用） |
| end_date | datetime | 结束日期（与 start_date 同时使用） |
| expect_df | bool | 默认 True，返回 pandas DataFrame |
| market | str | 市场，默认'cn' |

#### 财务数据处理逻辑

| 处理方式 | 说明 |
|----------|------|
| LF (Last File) | 基于最新期财报，时效性最好 |
| LYR (Last Year Ratio) | 基于最近一期年报，数据可靠性最高 |
| TTM (Trailing Twelve Months) | 滚动12个月，平滑偶然性 |

---

### 2.2 财务衍生指标因子

#### 估值类因子

| 因子名 | 说明 |
|--------|------|
| pe_ratio_lyr/ttm/lf | 市盈率 |
| pb_ratio_lyr/ttm/lf | 市净率 |
| ps_ratio_lyr/ttm | 市销率 |
| dividend_yield_ttm | 股息率 |
| peg_ratio_lyr/ttm | PEG值 |
| market_cap/market_cap_2/market_cap_3 | 总市值 |
| ev_lyr/ttm/lf | 企业价值 |
| ev_to_ebitda_lyr/ttm | 企业倍数 |
| book_to_market_ratio_lyr/ttm/lf | 账面市值比 |

#### 经营类因子

| 因子名 | 说明 |
|--------|------|
| diluted_earnings_per_share_lyr/ttm | 摊薄每股收益 |
| adjusted_earnings_per_share_lyr/ttm | 基本每股收益_扣除 |
| operating_revenue_per_share_lyr/ttm | 每股营业收入 |
| ebit_lyr/ttm | 息税前利润 |
| ebitda_lyr/ttm | 息税折旧摊销前利润 |
| return_on_equity_lyr/ttm | 净资产收益率(ROE) |
| return_on_equity_diluted_lyr/ttm | 摊薄净资产收益率 |
| net_profit_to_revenue_lyr/ttm | 经营净利率 |
| profit_from_operation_to_revenue_lyr/ttm | 营业利润率 |

#### 现金流类因子

| 因子名 | 说明 |
|--------|------|
| cash_flow_per_share_lyr/ttm | 每股现金流 |
| operating_cash_flow_per_share_lyr/ttm | 每股经营现金流 |
| fcff_lyr/ttm | 企业自由现金流量 |
| fcfe_lyr/ttm | 股东自由现金流量 |
| ocf_to_debt_lyr/ttm | 经营现金流/负债合计 |
| surplus_cash_protection_multiples_lyr/ttm | 盈余现金保障倍数 |

#### 财务类因子

| 因子名 | 说明 |
|--------|------|
| debt_to_asset_ratio_lyr/ttm/lf | 资产负债率 |
| equity_multiplier_lyr/ttm/lf | 权益乘数 |
| current_ratio_lyr/ttm/lf | 流动比率 |
| quick_ratio_lyr/ttm/lf | 速动比率 |
| cash_ratio_lyr/ttm/lf | 现金比率 |
| interest_bearing_debt_lyr/ttm/lf | 带息债务 |
| net_debt_lyr/ttm/lf | 净债务 |
| working_capital_lyr/ttm/lf | 营运资本 |
| book_value_per_share_lyr/ttm/lf | 每股净资产 |

#### 成长性因子

| 因子名 | 说明 |
|--------|------|
| net_profit_growth_ratio_lyr/ttm | 净利润同比增长率 |
| operating_revenue_growth_ratio_lyr/ttm | 营业收入同比增长率 |
| net_asset_growth_ratio_lyr/ttm/lf | 净资产同比增长率 |
| total_asset_growth_ratio_lyr/ttm/lf | 总资产同比增长率 |
| net_profit_parent_company_growth_ratio_lyr/ttm | 归母净利润同比增长率 |
| net_operate_cash_flow_growth_ratio_lyr/ttm | 经营现金流量净额同比增长率 |
| inc_book_per_share_lyr/ttm/lf | 每股净资产同比增长率 |

---

### 2.3 技术指标因子

#### 均线类指标

| 因子名 | 说明 |
|--------|------|
| MA3/5/10/20/30/60/120/250 | 移动平均线 |
| EMA3/5/10/20/30/60/120/250 | 指数移动平均线 |
| MACD_DIFF/MACD_DEA/MACD_HIST | MACD指标 |
| BOLL/BOLL_UP/BOLL_DOWN | 布林带 |
| BBI/BBIBOLL_UP/BBIBOLL_DOWN | 多空指标 |

#### 超买超卖类指标

| 因子名 | 说明 |
|--------|------|
| KDJ_K/KDJ_D/KDJ_J | KDJ随机指标 |
| RSI6/RSI10 | 相对强弱指标 |
| WR | 威廉指标 |
| BIAS5/BIAS10/BIAS20 | 乖离率 |
| OBOS | 超买超卖指标 |

#### 能量类指标

| 因子名 | 说明 |
|--------|------|
| OBV | 能量潮 |
| VOL3/5/10/20/30/60/120/250 | 平均换手率 |
| QTYR_5_20 | 5日20日量比 |
| DAVOL5/10/20 | 平均换手率与120日比值 |

#### 趋势类指标

| 因子名 | 说明 |
|--------|------|
| DI1/DI2/ADX/ADXR | DMI趋向指标 |
| TRIX/MATRIX | 三重指数平均线 |
| ASI/ASIT | 震动升降指标 |
| DPO/MADPO | 区间震荡线 |
| MCST | 市场成本 |

---

### 2.4 Alpha101 因子

Alpha101 是 WorldQuant 发布的 101 个量化因子，米筐 RQData 完整支持这些因子的调用。因子命名规则为 WorldQuant_alpha001 至 WorldQuant_alpha101。

```python
# 获取 Alpha101 因子
get_factor(['000001.XSHE', '600000.XSHG'],
           'WorldQuant_alpha010',
           '20190601', '20190610')
```

**常用 Alpha101 因子示例**：

| 因子名 | 说明 |
|--------|------|
| WorldQuant_alpha001 | 基于收益率和标准差的排序因子 |
| WorldQuant_alpha002 | 基于成交量和价格变化的相关性因子 |
| WorldQuant_alpha003 | 基于开盘价和成交量的相关性因子 |
| WorldQuant_alpha010 | 基于价格变动的趋势因子 |
| WorldQuant_alpha041 | 基于最高最低价的几何平均因子 |
| WorldQuant_alpha054 | 基于价格和成交量的综合因子 |
| WorldQuant_alpha060 | 基于价格波动的综合因子 |

---

## 三、使用示例

### 3.1 财务数据查询示例

```python
import rqdatac as rq

# 初始化
rq.init()

# 获取季度财务数据
financials = rq.get_pit_financials_ex(
    order_book_ids=['000001.XSHE', '600000.XSHG'],
    fields=['revenue', 'net_profit', 'total_assets'],
    start_quarter='2024q1',
    end_quarter='2024q2'
)
print(financials)
```

### 3.2 因子数据查询示例

```python
# 获取财务衍生指标
factors = rq.get_factor(
    order_book_ids=['000001.XSHE', '600000.XSHG'],
    factor=['pe_ratio_ttm', 'pb_ratio_lf', 'return_on_equity_ttm'],
    start_date='20240101',
    end_date='20240110'
)
print(factors)

# 获取技术指标
tech_factors = rq.get_factor(
    order_book_ids=['000001.XSHE'],
    factor=['MACD_DIFF', 'KDJ_K', 'RSI6'],
    start_date='20240101',
    end_date='20240110'
)
```

### 3.3 获取所有因子列表

```python
# 获取所有可用因子名称
all_factors = rq.get_all_factor_names()
print(f"共有 {len(all_factors)} 个因子")
print(all_factors[:20])  # 打印前20个因子
```

---

## 附录：官方文档链接

- 米筐 RQData 官方文档：https://www.ricequant.com/doc/rqdata/python/stock-mod

---

*文档生成时间：2026年3月*
