import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from p_analysis import m_analysis as man

# reporting functions


def input_country(countr,df):
    if countr == "":
        return df
    else:
        return df[df["Country"]==countr]



def challenge1_final(mergedtable):
    final_table = man.challenge1(mergedtable)
    final_table.to_csv(f'data/results/challenge1.csv',index=False)
    return final_table



def top10_topdf(df):
    top10=df.head(10)
    fig, ax =plt.subplots(figsize=(12,4))
    ax.axis('tight')
    ax.axis('off')
    the_table = ax.table(cellText=top10.values,colLabels=top10.columns,loc='center')
    pp = PdfPages("data/results/challenge1.pdf")
    pp.savefig(fig, bbox_inches='tight')
    pp.close()
    print("saving into a pdf the top10")
    return the_table