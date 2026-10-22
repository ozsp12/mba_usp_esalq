"""Stage 01 — synthetic branch data, ported from the original generation notebook.

The three legacy generator functions and their numeric parameters below are
reproduced verbatim from notebooks/create_dataframes.ipynb. Without a seed,
the generator intentionally retains the original stochastic behavior.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import random

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

#
def CreatesDFStateProba():
    #
    State = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB',
             'PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
    #
    Population = [906876,3365351,877613,4269995,14985284,9240580,3094325,4108508,7206589,7153262,
                  3567234,2839188,21411923,8777124,4059905,11597484,9674793,3289290,17463349,3560903,
                  11466630,1815278,652713,7338473,46649132,2338474,1607363]
    #
    df = pd.DataFrame({'State':State,'Population':Population})
    #
    df['Apriori'] = df['Population']/df['Population'].sum()
    #
    return df

#
def CreatesDFDP(k):
    #
    Features = ['NumberTellerCapacity','NumberManagerPersonalCapacity','NumberManagerBusinessCapacity','NumberATM',
    'NumberPersonalClientsTierA','NumberPersonalClientsTierB','NumberPersonalClientsTierC','NumberPersonalClientsTierD',
    'NumberINSSClients','NumberSalaryAccounts','NBusinessClientsTierA','NBusinessClientsTierB','NBusinessClientsTierC',
    'NBusinessClientsTierD','AvgMonthlyIncomePersonalClientTierA','AvgMonthlyIncomePersonalClientTierB',
    'AvgMonthlyIncomePersonalClientTierC','AvgMonthlyIncomePersonalClientTierD','AvgMonthlyINSSBenefitsAmount',
    'AvgMonthlySalaryValue','AvgMonthlyEBITDABusinessClientTierA','AvgMonthlyEBITDABusinessClientTierB',
    'AvgMonthlyEBITDABusinessClientTierC','AvgMonthlyEBITDABusinessClientTierD','BranchSizeSquareMeters',
    'AvgMonthlyATMPaymentsTransactions','AvgMonthlyATMWithdrawTransactions','AvgMonthlyATMTransferTransactions',
    'AvgMonthlyATMDepositTransactions','AvgMonthlyATMTransactions','AvgMonthlyTellerPaymentsTransactions',
    'AvgMonthlyTellerWithdrawTransactions','AvgMonthlyTellerTransferTransactions','AvgMonthlyTellerDepositTransactions',
    'AvgMonthlyTellerTransactions','AvgMonthlyManagerPersonalLoanTransactions',
    'AvgMonthlyManagerBusinessLoanTransactions',
    'AvgMonthlyManagerPersonalInvestmentTransactions','AvgMonthlyManagerBusinessInvestmentTransactions',
    'AvgMonthlyManagerTransactions','AvgMonthlyRevenueThousands','AvgMonthlyOperationalCostThousands',
    'AvgMonthlyOperationalLossThousands','AvgMontlhyEBITDA','AvgMonthlySavingsAccountDeposit',
    'AvgMonthlyPersonalLoanAmount','AvgMonthlyBusinessLoanAmount','AvgMonthlyPersonalCreditCardPaymentAmount',
    'AvgMonthlyBusinessCreditCardPaymentAmount','AvgMonthlyPersonalInvestmentsAmount',
    'AvgMonthlyBusinessInvestmentsAmount',
    ]
    #
    FeatureGrouping = ['Size', 'Size', 'Size', 'Size', 'Size', 'Size', 'Size', 'Size', 'Size', 'Size', 'Size', 'Size',
     'Size', 'Size', 'BusinessPotential', 'BusinessPotential', 'BusinessPotential', 'BusinessPotential',
     'BusinessPotential', 'BusinessPotential', 'BusinessPotential', 'BusinessPotential', 'BusinessPotential',
     'BusinessPotential', 'BusinessPotential', 'TransactionVolume', 'TransactionVolume', 'TransactionVolume',
     'TransactionVolume', 'TransactionVolume', 'TransactionVolume', 'TransactionVolume', 'TransactionVolume',
     'TransactionVolume', 'TransactionVolume', 'Credit', 'Credit', 'Investment', 'Investment', 'TransactionVolume',
     'FinancialHealth', 'FinancialHealth', 'FinancialHealth', 'FinancialHealth', 'TransactionValue',
     'TransactionValue', 'TransactionValue', 'Credit', 'Credit', 'TransactionValue', 'TransactionValue']
    #
    MeanC1 = [19000, 25000, 79000, 15000, 20000, 5000, 10000, 25000, 500000, 320000, 150000, 88000,
             1950, 4500, 3000, 2250, 1750, 150, 300, 100, 200, 750, 120000, 40000, 800, 1200, 1125, 550000,
             2800, 550, 25000, 20000, 78000, 15000, 18000, 350000, 500, 75, 220, 450, 850, 6, 1000, 2, 2,
             1000, 2000, 2500, 3500, 1250, 5]
    #
    MeanC2 = [8550, 11250, 63200, 6750, 9000, 5000, 10000, 30000, 400000, 256000, 120000, 70400, 1560,
             3600, 2400, 1800, 1400, 180, 360, 120, 240, 900, 240000, 80000, 800, 960, 1350, 660000, 2240,
             660, 20000, 16000, 62400, 12000, 14400, 560000, 800, 34, 264, 720, 1360, 10, 1600, 3, 3,
             450, 2000, 4000, 5600, 2000, 8]
    #
    MeanC3 = [22800, 30000, 94800, 18000, 24000, 6000, 12000, 30000, 600000, 384000, 180000, 105600, 2340,
             5400, 3600, 2700, 2100, 180, 360, 120, 240, 900, 180000, 60000, 960, 1440, 1350, 660000, 3360,
             660, 30000, 24000, 93600, 18000, 21600, 420000, 600, 90, 264, 540, 1020, 7, 1200, 2, 2,
             1200, 2400, 3000, 4200, 1500, 6]
    #
    MeanC4 = [30400, 40000, 126400, 24000, 32000, 8000, 16000, 40000, 800000, 512000, 240000, 140800, 3120,
             7200, 4800, 3600, 2800, 240, 480, 160, 320, 1200, 240000, 80000, 1280, 1920, 1800, 880000, 4480, 880,
             40000, 32000, 124800, 24000, 28800, 560000, 800, 120, 352, 720, 1360, 10, 1600, 3, 3, 1600, 3200, 4000,
             5600, 2000, 8]
    #
    MeanC5 = [30400, 40000, 126400, 24000, 32000, 8000, 8000, 40000, 800000, 512000, 240000, 140800, 3120,
             7200, 4800, 3600, 2800, 120, 480, 80, 320, 1200, 240000, 80000, 1280, 960, 1800, 880000, 4480, 880,
             40000, 32000, 124800, 24000, 28800, 280000, 600, 75, 352, 720, 1360, 10, 1600, 3, 3, 1200,
             3200, 4000, 5600, 2000, 8]
    #
    MeanC6 = [22800, 30000, 94800, 18000, 24000, 6000, 12000, 30000, 600000, 384000, 180000, 105600, 2340,
             5400, 3600, 2700, 2100, 180, 360, 120, 240, 900, 180000, 60000, 960, 1440, 1350, 660000, 3360, 660,
             30000, 24000, 93600, 18000, 21600, 420000, 600, 90, 264, 540, 1020, 7, 1200, 
             2, 2, 1200, 2400, 3000, 4200, 1500, 6]
    #
    df = pd.DataFrame({'Features':Features,
                       'FeatureGrouping':FeatureGrouping,
                       'c1':MeanC1,
                       'c2':MeanC2,
                       'c3':MeanC3,
                       'c4':MeanC4,
                       'c5':MeanC5,
                       'c6':MeanC6,
                      })
    #
    df = pd.melt(df, id_vars = ['FeatureGrouping','Features'], value_vars=['c1','c2','c3','c4','c5','c6'])
    #
    df.rename(columns = {'value':'Mean','variable':'ClusterName'}, inplace = True)
    #
    df['Std'] = k * df['Mean']
    #
    return df

def CreateCluster(dp,cluster,dpuf,dpdummy,n):
    #
    dp = dp[dp['ClusterName'] == cluster]
    #
    array_feature_names = list(dp.Features)
    #
    array_avg = list(dp.Mean)
    #
    array_std = list(dp.Std)
    #
    m = len(array_feature_names)
    #
    new_frame = pd.DataFrame()
    #
    id_number = np.arange(1,n+1)
    #
    df = pd.DataFrame({'id':id_number})
    #
    df['id'] = df['id'].astype(int).apply(lambda x: '{0:0>4}'.format(x)).astype(str)
    #
    df['ClusterName'] = dp['ClusterName'].unique()[0]  
    #
    df['IdBranch'] = df['ClusterName'] + '_' + df['id']  
    #
    for k in range(m):            
        #
        frame = np.array
        #
        frame = np.round(np.random.normal(array_avg[m - k - 1], array_std[m - k - 1], n),0).astype(int)
        #
        new_frame = pd.DataFrame({array_feature_names[m - k - 1]:frame})   
        #
        df = df.join(new_frame) 
    #
    df.loc[df['NumberManagerBusinessCapacity'] <= 0, 'NumberManagerBusinessCapacity'] = 1  
    #
    df.loc[df['NumberManagerPersonalCapacity'] <= 0, 'NumberManagerPersonalCapacity'] = 1  
    #
    df.loc[df['NumberTellerCapacity'] <= 0, 'NumberTellerCapacity'] = 1
    #
    array_uf = list(dpuf.State.unique())  
    #
    prob_uf = list(dpuf.Apriori.unique())  
    # creates array for estado_civil
    df['State'] = random.choices(population = array_uf, weights = prob_uf, k = n)
    # array for probability on branches inside shopping
    shopping = [1,0]
    # probability of dummy = 1 for branches inside shopping
    p = dpdummy[(dpdummy['ClusterName'] == cluster) & 
                (dpdummy['Features'] == 'DummyInsideShopping')]['Probability'].values[0]
    # probability array
    prob_shopping = [p,1-p]
    # creates feature DummyInsideShopping for branches inside shopping
    df['DummyInsideShopping'] = random.choices(population = shopping, weights = prob_shopping, k = n)
    # array for probability on branches localized on prime zone
    primezone = [1,0]
    # probability of dummy = 1 for branches localized on prime zones
    p = dpdummy[(dpdummy['ClusterName'] == cluster) & 
                (dpdummy['Features'] == 'DummyPrimeZone')]['Probability'].values[0]
    # probability array
    prob_primezone = [p,1-p]
    # creates feature DummyPrimeZone for branches localized on prime zones
    df['DummyPrimeZone']  = random.choices(population = primezone, weights = prob_primezone, k = n)
    #
    return df

def run(*, workbook: Path = ROOT / "data" / "deparas.xlsx",
        output: Path = ROOT / "assets" / "dataset.csv",
        seed: int | None = None) -> pd.DataFrame:
    """Reproduce the original notebook's generation steps and persist its DataFrame."""
    if seed is not None:
        np.random.seed(seed)
        random.seed(seed)
    #
    dpuf = CreatesDFStateProba()
    #
    dp = CreatesDFDP(k = 0.15)
    #
    dpdummy = pd.read_excel(workbook, sheet_name='dummy')
    #
    df1 = CreateCluster(dp,'c1',dpuf,dpdummy,2500)
    df2 = CreateCluster(dp,'c2',dpuf,dpdummy,800)
    df3 = CreateCluster(dp,'c3',dpuf,dpdummy,700)
    df4 = CreateCluster(dp,'c4',dpuf,dpdummy,400)
    df5 = CreateCluster(dp,'c5',dpuf,dpdummy,300)
    df6 = CreateCluster(dp,'c6',dpuf,dpdummy,500)
    df = pd.concat([df1,df2,df3,df4,df5,df6]).reset_index().drop(columns = 'index')
    if not output.parent.is_dir():
        raise FileNotFoundError(f"Output directory must exist: {output.parent}")
    df.to_csv(output, index=False)
    return df


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workbook", type=Path, default=ROOT / "data" / "deparas.xlsx")
    parser.add_argument("--output", type=Path, default=ROOT / "assets" / "dataset.csv")
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()
    df = run(workbook=args.workbook, output=args.output, seed=args.seed)
    print(f"stage01: {len(df)} rows, {len(df.columns)} columns -> {args.output}")


if __name__ == "__main__":
    main()
